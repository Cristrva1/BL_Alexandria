"""Recolección de métricas públicas por repo para la rúbrica de calidad.

Fuentes (todas de solo lectura):

* GitHub GraphQL (``gh api graphql``): estrellas, edad, licencia, propietario, issues,
  releases, etiquetas, commits en 90/365 días y las 40 issues más recientes con sus
  primeros comentarios (para el tiempo de primera respuesta).
* GitHub REST ``contributors`` (top 100) para el bus factor.
* OpenSSF Scorecard (``api.securityscorecards.dev``).
* Descargas: pypistats.org (último mes), api.npmjs.org (último mes) y Docker Hub (pulls totales).

Cada repo se guarda en ``data/metricas/cache/<id>.json`` con ``fecha`` de obtención. Ninguna
llamada instala ni ejecuta proyectos del catálogo.
"""
from __future__ import annotations

import json
import re
import statistics
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable

import requests

UA = {"User-Agent": "BL_Alexandria-metricas/1.0"}
CACHE_DIR = Path("data") / "metricas" / "cache"
RECENT_ISSUES = 40


class MetricsError(RuntimeError):
    pass


# --------------------------------------------------------------------------------------------
# Transporte
# --------------------------------------------------------------------------------------------

def _gh(args: list[str], body: dict | None = None, retries: int = 4) -> Any:
    """``gh api`` con reintentos y espera ante límites de tasa."""
    for attempt in range(retries):
        proc = subprocess.run(["gh", "api", *args] + (["--input", "-"] if body is not None else []),
                              input=json.dumps(body) if body is not None else None,
                              capture_output=True, text=True, encoding="utf-8", timeout=120)
        out = proc.stdout.strip()
        if proc.returncode == 0:
            return json.loads(out) if out else None
        err = (proc.stderr + out).lower()
        if "rate limit" in err or "secondary" in err or "abuse" in err:
            _wait_for_rate_limit(attempt)
            continue
        if any(code in err for code in ("502", "503", "504", "timeout", "something went wrong")):
            time.sleep(5 * (attempt + 1))
            continue
        raise MetricsError(f"gh api {' '.join(args[:2])}: {proc.stderr.strip()[:300] or out[:300]}")
    raise MetricsError(f"gh api {' '.join(args[:2])}: reintentos agotados")


def _wait_for_rate_limit(attempt: int) -> None:
    try:
        data = json.loads(subprocess.run(["gh", "api", "rate_limit"], capture_output=True, text=True, timeout=30).stdout)
        res = data["resources"]
        waits = [r["reset"] - time.time() for r in (res["core"], res["graphql"]) if r["remaining"] < 20]
        delay = max(waits) + 5 if waits else 60 * (attempt + 1)
    except Exception:  # noqa: BLE001 - sin datos de límite: espera prudente
        delay = 60 * (attempt + 1)
    time.sleep(min(max(delay, 30), 3700))


def _http_json(url: str, retries: int = 3) -> Any:
    for attempt in range(retries):
        try:
            resp = requests.get(url, headers=UA, timeout=30)
        except requests.RequestException:
            time.sleep(3 * (attempt + 1))
            continue
        if resp.status_code == 404:
            return None
        if resp.status_code == 429:
            time.sleep(int(resp.headers.get("Retry-After", "0") or 0) or 10 * (attempt + 1))
            continue
        if resp.ok:
            return resp.json()
        time.sleep(3 * (attempt + 1))
    return None


# --------------------------------------------------------------------------------------------
# GraphQL
# --------------------------------------------------------------------------------------------

_REPO_FIELDS = """
  nameWithOwner url homepageUrl stargazerCount forkCount createdAt pushedAt isArchived isFork hasIssuesEnabled
  parent { nameWithOwner }
  owner { __typename login id }
  licenseInfo { spdxId name }
  primaryLanguage { name }
  openIssues: issues(states: OPEN) { totalCount }
  closedIssues: issues(states: CLOSED) { totalCount }
  releases(first: 100, orderBy: {field: CREATED_AT, direction: DESC}) { totalCount nodes { tagName publishedAt isPrerelease isDraft } }
  tags: refs(refPrefix: "refs/tags/", first: 60, orderBy: {field: TAG_COMMIT_DATE, direction: DESC}) {
    totalCount nodes { name target { __typename ... on Commit { committedDate } ... on Tag { target { ... on Commit { committedDate } } } } } }
  defaultBranchRef { name target { ... on Commit { h90: history(since: "%(s90)s") { totalCount } h365: history(since: "%(s365)s") { totalCount } } } }
  recentIssues: issues(first: %(n)d, orderBy: {field: CREATED_AT, direction: DESC}) {
    nodes { createdAt closedAt author { login } comments(first: 6) { nodes { createdAt author { __typename login } } } } }
"""


def _iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def graphql_batch(full_names: list[str], now: datetime, gh: Callable = _gh) -> dict[str, dict | None]:
    """Consulta varias repos en una sola petición GraphQL. Devuelve ``{full_name: nodo | None}``."""
    fields = _REPO_FIELDS % {"s90": _iso(now - timedelta(days=90)), "s365": _iso(now - timedelta(days=365)), "n": RECENT_ISSUES}
    parts = []
    for i, fn in enumerate(full_names):
        owner, name = fn.split("/", 1)
        parts.append(f'r{i}: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) {{{fields}}}')
    query = "query {\n" + "\n".join(parts) + "\n rateLimit { cost remaining resetAt } }"
    try:
        data = gh(["graphql"], {"query": query})
    except MetricsError as error:
        if len(full_names) == 1:
            return {full_names[0]: None}
        # Un repo inexistente o renombrado invalida el lote: se reintenta uno a uno.
        if "could not resolve" in str(error).lower() or "not_found" in str(error).lower():
            out: dict[str, dict | None] = {}
            for fn in full_names:
                out.update(graphql_batch([fn], now, gh))
            return out
        raise
    nodes = (data or {}).get("data") or {}
    return {fn: nodes.get(f"r{i}") for i, fn in enumerate(full_names)}


def owner_history(full_name: str, owner_id: str, now: datetime, gh: Callable = _gh) -> dict[str, int]:
    """Commits del propietario en 90/365 días (para repos derivados que fusionan su upstream)."""
    owner, name = full_name.split("/", 1)
    q = ("query { repository(owner: %s, name: %s) { defaultBranchRef { target { ... on Commit {"
         " h90: history(since: \"%s\", author: {id: \"%s\"}) { totalCount }"
         " h365: history(since: \"%s\", author: {id: \"%s\"}) { totalCount } } } } } }") % (
        json.dumps(owner), json.dumps(name), _iso(now - timedelta(days=90)), owner_id, _iso(now - timedelta(days=365)), owner_id)
    data = gh(["graphql"], {"query": q})
    target = ((((data or {}).get("data") or {}).get("repository") or {}).get("defaultBranchRef") or {}).get("target") or {}
    return {"commits_90d": (target.get("h90") or {}).get("totalCount"), "commits_365d": (target.get("h365") or {}).get("totalCount")}


def contributors(full_name: str, gh: Callable = _gh) -> list[dict] | None:
    try:
        data = gh([f"repos/{full_name}/contributors?per_page=100"])
    except MetricsError as error:
        if "too large" in str(error).lower():
            return None
        raise
    return [{"login": c.get("login"), "n": c.get("contributions", 0), "bot": (c.get("type") == "Bot") or str(c.get("login", "")).endswith("[bot]")}
            for c in (data or []) if isinstance(c, dict)]


# --------------------------------------------------------------------------------------------
# Métricas derivadas
# --------------------------------------------------------------------------------------------

def _parse(ts: str | None) -> datetime | None:
    return datetime.fromisoformat(ts.replace("Z", "+00:00")) if ts else None


def response_stats(issues: list[dict], now: datetime) -> dict:
    """Primera respuesta: primer comentario de otra persona (no bot) o el cierre, lo que ocurra antes.

    Las issues sin respuesta cuentan como «censuradas» con el tiempo transcurrido hasta hoy; así la
    mediana no premia a quien no responde. Las issues abiertas hace menos de 2 días se ignoran.
    """
    waits: list[float] = []
    answered = 0
    closes: list[float] = []
    for it in issues:
        created = _parse(it.get("createdAt"))
        if not created:
            continue
        author = ((it.get("author") or {}).get("login") or "").lower()
        firsts = []
        for c in ((it.get("comments") or {}).get("nodes") or []):
            ca = c.get("author") or {}
            login = (ca.get("login") or "").lower()
            if ca.get("__typename") == "Bot" or login.endswith("[bot]") or login in ("", author):
                continue
            firsts.append(_parse(c["createdAt"]))
            break
        closed = _parse(it.get("closedAt"))
        if closed:
            closes.append((closed - created).total_seconds() / 86400)
            firsts.append(closed)
        if firsts:
            answered += 1
            waits.append(max((min(firsts) - created).total_seconds() / 86400, 0.0))
        elif (now - created).days >= 2:
            waits.append((now - created).total_seconds() / 86400)
    return {"primera_respuesta_dias": round(statistics.median(waits), 2) if waits else None,
            "respondidas": answered, "muestra_issues": len(waits),
            "cierre_reciente_dias": round(statistics.median(closes), 2) if closes else None}


SEMVER = re.compile(r"(?:^|[^0-9])v?(\d+)\.(\d+)(?:\.(\d+))?")


def _release_dates(node: dict) -> tuple[list[datetime], list[str]]:
    rel = [r for r in ((node.get("releases") or {}).get("nodes") or []) if not r.get("isDraft")]
    dates = [_parse(r["publishedAt"]) for r in rel if r.get("publishedAt")]
    names = [r["tagName"] for r in rel if not r.get("isPrerelease")]
    if dates:
        return [d for d in dates if d], names
    tag_dates: list[datetime] = []
    tag_names: list[str] = []
    for t in ((node.get("tags") or {}).get("nodes") or []):
        tgt = t.get("target") or {}
        when = tgt.get("committedDate") or (tgt.get("target") or {}).get("committedDate")
        if when:
            tag_dates.append(_parse(when))
            tag_names.append(t["name"])
    return tag_dates, tag_names


def semver_major(names: list[str]) -> int | None:
    for name in names:
        if re.search(r"(alpha|beta|rc|dev|nightly|pre)", name, re.I):
            continue
        m = SEMVER.search(name)
        if m:
            return int(m.group(1))
    return None


def summarize(node: dict, contribs: list[dict] | None, now: datetime) -> dict:
    created = _parse(node["createdAt"])
    age_days = max((now - created).days, 1)
    dates, names = _release_dates(node)
    year_ago = now - timedelta(days=365)
    rel365 = sum(1 for d in dates if d >= year_ago)
    capped = len(dates) >= 60 and all(d >= year_ago for d in dates)
    target = ((node.get("defaultBranchRef") or {}).get("target") or {})
    humans = [c for c in (contribs or []) if not c["bot"]]
    total = sum(c["n"] for c in humans)
    top1 = round(humans[0]["n"] / total, 3) if humans and total else None
    open_i = (node.get("openIssues") or {}).get("totalCount")
    closed_i = (node.get("closedIssues") or {}).get("totalCount")
    resp = response_stats((node.get("recentIssues") or {}).get("nodes") or [], now) if node.get("hasIssuesEnabled") else {
        "primera_respuesta_dias": None, "respondidas": 0, "muestra_issues": 0, "cierre_reciente_dias": None}
    return {
        "full_name": node["nameWithOwner"],
        "estrellas": node["stargazerCount"],
        "forks": node["forkCount"],
        "creado": node["createdAt"][:10],
        "edad_dias": age_days,
        "estrellas_anio": round(node["stargazerCount"] / max(age_days / 365, 0.25), 1),
        "ultimo_push": (node.get("pushedAt") or "")[:10],
        "archivado": node["isArchived"],
        "fork_de": (node.get("parent") or {}).get("nameWithOwner"),
        "propietario": node["owner"]["login"],
        "propietario_tipo": node["owner"]["__typename"],
        "propietario_id": node["owner"]["id"],
        "homepage": node.get("homepageUrl") or None,
        "licencia_spdx": (node.get("licenseInfo") or {}).get("spdxId"),
        "lenguaje": (node.get("primaryLanguage") or {}).get("name"),
        "issues_habilitadas": node["hasIssuesEnabled"],
        "issues_abiertas": open_i,
        "issues_cerradas": closed_i,
        "ratio_cerradas": round(closed_i / (open_i + closed_i), 3) if node["hasIssuesEnabled"] and (open_i or closed_i) else None,
        "commits_90d": (target.get("h90") or {}).get("totalCount"),
        "commits_365d": (target.get("h365") or {}).get("totalCount"),
        "releases_365d": rel365,
        "releases_365d_tope": capped,
        "releases_fuente": "releases" if (node.get("releases") or {}).get("totalCount") else "etiquetas",
        "ultima_version": names[0] if names else None,
        "semver_mayor": semver_major(names),
        "contribuidores_top100": len(humans) if contribs is not None else None,
        "cuota_principal": top1,
        **resp,
    }


# --------------------------------------------------------------------------------------------
# Licencias no reconocidas por GitHub (NOASSERTION / sin SPDX)
# --------------------------------------------------------------------------------------------

_SOURCE_AVAILABLE = ("business source license", "elastic license", "commons clause", "server side public license",
                     "polyform", "noncommercial", "non-commercial", "sustainable use license", "source available license",
                     "community license", "model use license", "openrail", "rail license", "fair source",
                     "modified version of the apache license", "with the following additional conditions",
                     "subject to the additional terms", "research use only", "academic or non-profit")
_OPEN_CORE = ("portions of this software are licensed as follows", "enterprise edition", "/ee/", "\"ee/\"", "ee directories",
              "commercial license", "proprietary license for certain", "/proprietary", "enterprise/")


def classify_licence_text(text: str | None) -> tuple[str, str]:
    """Clase de licencia a partir del texto de LICENSE (heurística; se puede corregir en config/calidad.yaml)."""
    if not text:
        return "desconocida", "sin archivo de licencia"
    t = re.sub(r"\s+", " ", text.lower())
    head = t[:1500]  # los textos GPL completos mencionan «noncommercially» más abajo
    if "open webui license" in head:
        return "source_available", "licencia propia con cláusula de marca"
    hit = next((k for k in _SOURCE_AVAILABLE if k in head), None)
    if hit:
        return "source_available", f"texto de licencia: «{hit}»"
    osi = any(k in t for k in ("permission is hereby granted", "apache license", "redistribution and use in source and binary forms",
                               "gnu general public", "gnu affero", "gnu lesser", "european union public licence",
                               "european union public license", "mozilla public license", "isc license", "cc0 1.0",
                               "postgresql", "the unlicense", "creative commons attribution 4.0", "permission to use, copy, modify"))
    hit = next((k for k in _OPEN_CORE + ("variously licensed", "certain files", "licensed per component") if k in head), None)
    if hit and osi:
        return "open_core", f"núcleo OSI con partes comerciales («{hit}»)"
    if any(k in t for k in ("gnu affero", "gnu general public", "gnu lesser", "european union public", "mozilla public license",
                            "attribution-sharealike")):
        return "osi_copyleft", "GPL/AGPL/LGPL/EUPL/MPL según el texto"
    if osi:
        return "osi_permisiva", "MIT/Apache/BSD/ISC/CC0 o equivalente según el texto"
    return "desconocida", "texto de licencia no reconocido"


def licence_text(full_name: str, gh: Callable = _gh) -> str | None:
    try:
        data = gh([f"repos/{full_name}/license"])
    except MetricsError:
        return None
    import base64
    try:
        return base64.b64decode((data or {}).get("content") or "").decode("utf-8", "replace")
    except Exception:  # noqa: BLE001
        return None


# --------------------------------------------------------------------------------------------
# Paquetes y descargas
# --------------------------------------------------------------------------------------------

_DOCKER_FLAGS_WITH_VALUE = {"-p", "--publish", "-v", "--volume", "-e", "--env", "--name", "-u", "--user", "-w", "--workdir",
                            "--network", "--net", "--gpus", "--env-file", "--add-host", "--restart", "--mount", "-m", "--memory",
                            "--entrypoint", "--platform", "--shm-size", "--cap-add", "--device", "-h", "--hostname", "--ipc",
                            "-l", "--label", "--pull", "--security-opt", "--ulimit", "--tmpfs", "--cpus"}


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def _plausible(pkg: str, rid: str, full_name: str) -> bool:
    p = _norm(pkg.split("/")[-1])
    cands = {_norm(rid), _norm(full_name.split("/")[1]), _norm(full_name.split("/")[0])}
    return bool(p) and any(c and (p == c or (len(p) >= 4 and (p in c or c in p))) for c in cands)


def detect_packages(rid: str, full_name: str, texts: list[str]) -> dict[str, str]:
    """Deduce paquetes PyPI/npm/Docker Hub de los comandos de instalación (solo si el nombre encaja con el repo)."""
    found: dict[str, str] = {}
    for text in texts:
        for line in re.split(r"[\n;&|]+", text or ""):
            toks = [t.strip("`'\"") for t in line.split()]
            for i, tok in enumerate(toks):
                nxt = [t for t in toks[i + 1:] if t]
                if tok in ("pip", "pip3", "pipx", "uv") and nxt:
                    sub = nxt[0]
                    rest = nxt[1:]
                    if tok == "uv" and sub == "pip":
                        sub, rest = (rest[0] if rest else ""), rest[1:]
                    if sub in ("install", "add") or (tok == "uv" and sub == "tool" and rest[:1] == ["install"]):
                        if tok == "uv" and sub == "tool":
                            rest = rest[1:]
                        name = next((r for r in rest if not r.startswith("-")), "")
                        name = re.split(r"[\[<>=!~ ]", name)[0]
                        if name and "/" not in name and not name.startswith(("git+", ".", "http")) and _plausible(name, rid, full_name):
                            found.setdefault("pypi", name.lower())
                elif tok in ("uvx",) and nxt:
                    name = re.split(r"[\[<>=@]", nxt[0])[0]
                    if _plausible(name, rid, full_name):
                        found.setdefault("pypi", name.lower())
                elif tok in ("npm", "pnpm", "yarn", "bun") and nxt and nxt[0] in ("i", "install", "add"):
                    name = next((r for r in nxt[1:] if not r.startswith("-")), "")
                    if name.startswith("@"):
                        name = "@" + name[1:].split("@")[0]
                    else:
                        name = name.split("@")[0]
                    if name and _plausible(name, rid, full_name):
                        found.setdefault("npm", name)
                elif tok == "npx" and nxt:
                    name = next((r for r in nxt if not r.startswith("-")), "")
                    name = "@" + name[1:].split("@")[0] if name.startswith("@") else name.split("@")[0]
                    if name and _plausible(name, rid, full_name):
                        found.setdefault("npm", name)
                elif tok == "docker" and nxt and nxt[0] in ("run", "pull"):
                    j = 1
                    while j < len(nxt):
                        t = nxt[j]
                        if t.startswith("-"):
                            j += 2 if (t in _DOCKER_FLAGS_WITH_VALUE and "=" not in t) else 1
                            continue
                        image = t
                        break
                    else:
                        image = ""
                    if image and not re.match(r"^(ghcr\.io|quay\.io|gcr\.io|public\.ecr|mcr\.|registry\.)", image):
                        image = image.removeprefix("docker.io/").split(":")[0].split("@")[0]
                        if image and re.match(r"^[a-z0-9._/-]+$", image) and _plausible(image, rid, full_name):
                            found.setdefault("docker", image if "/" in image else f"library/{image}")
    return found


def _links_to(full_name: str, *values: Any) -> bool:
    blob = json.dumps(values).lower().replace("\\/", "/")
    return re.search(r"github\.com[/:]" + re.escape(full_name.lower()) + r"(?:\.git)?(?![\w.-])", blob) is not None


def verify_guesses(rid: str, full_name: str, found: dict[str, str], http: Callable = _http_json) -> dict[str, str]:
    """Completa paquetes no deducidos probando nombres obvios y aceptándolos solo si el registro
    enlaza al repo de GitHub (PyPI/npm) o si la imagen de Docker Hub está en el espacio del propietario."""
    owner, name = full_name.split("/", 1)
    names = list(dict.fromkeys(n.lower() for n in (rid, name, f"{owner}-{name}") if n))
    out = dict(found)
    if "pypi" not in out:
        for n in names:
            data = http(f"https://pypi.org/pypi/{n}/json")
            info = (data or {}).get("info") or {}
            if info and _links_to(full_name, info.get("project_urls"), info.get("home_page"), info.get("download_url")):
                out["pypi"] = n
                break
    if "npm" not in out:
        for n in names + [f"@{owner.lower()}/{name.lower()}"]:
            data = http(f"https://registry.npmjs.org/{n.replace('/', '%2F')}")
            if data and _links_to(full_name, data.get("repository"), data.get("homepage"), data.get("bugs")):
                out["npm"] = n
                break
    if "docker" not in out:
        data = http(f"https://hub.docker.com/v2/repositories/{owner.lower()}/{name.lower()}/")
        if data and data.get("pull_count") is not None:
            out["docker"] = f"{owner.lower()}/{name.lower()}"
    return out


def downloads(pkgs: dict[str, str], http: Callable = _http_json) -> dict:
    out: dict[str, Any] = {"paquetes": pkgs}
    if pkgs.get("pypi"):
        data = http(f"https://pypistats.org/api/packages/{pkgs['pypi']}/recent")
        out["pypi_mes"] = ((data or {}).get("data") or {}).get("last_month")
    if pkgs.get("npm"):
        data = http(f"https://api.npmjs.org/downloads/point/last-month/{pkgs['npm']}")
        out["npm_mes"] = (data or {}).get("downloads")
    if pkgs.get("docker"):
        data = http(f"https://hub.docker.com/v2/repositories/{pkgs['docker']}/")
        out["docker_pulls"] = (data or {}).get("pull_count")
    month = [v for v in (out.get("pypi_mes"), out.get("npm_mes")) if v]
    out["descargas_mes"] = max(month) if month else None
    return out


def scorecard(full_name: str, http: Callable = _http_json) -> dict:
    data = http(f"https://api.securityscorecards.dev/projects/github.com/{full_name}")
    if not data or data.get("score") is None:
        return {"scorecard": None, "scorecard_fecha": None}
    return {"scorecard": data["score"], "scorecard_fecha": (data.get("date") or "")[:10]}


# --------------------------------------------------------------------------------------------
# Orquestación
# --------------------------------------------------------------------------------------------

def catalog_targets(compact: dict, detail: dict) -> list[dict]:
    out = []
    for r in compact["repos"]:
        if r.get("alias_of") or not r.get("gh") or r.get("repository_host") not in (None, "github", "github.com"):
            continue
        d = detail.get(r["id"], {})
        gs = d.get("getting_started") or {}
        texts = [gs.get("command") or "", " ".join(str(s) for s in (gs.get("steps") or []) if isinstance(s, str)), d.get("install") or ""]
        out.append({"id": r["id"], "gh": r["gh"], "texts": texts})
    return out


def load_cache(root: Path, rid: str) -> dict | None:
    path = root / CACHE_DIR / f"{rid}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def save_cache(root: Path, rid: str, data: dict) -> None:
    path = root / CACHE_DIR / f"{rid}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def is_fresh(cached: dict | None, max_days: int, now: datetime) -> bool:
    if not cached or not cached.get("fecha") or cached.get("error"):
        return False
    return (now.date() - datetime.fromisoformat(cached["fecha"]).date()).days < max_days


def collect(root: Path, targets: list[dict], *, config: dict, refresh: bool = False, now: datetime | None = None,
            gh: Callable = _gh, http: Callable = _http_json, batch: int = 6, workers: int = 4,
            log: Callable[[str], None] = lambda _m: None) -> dict[str, dict]:
    """Obtiene (o reutiliza de caché) las métricas de ``targets``. Devuelve ``{id: métricas}``."""
    now = now or datetime.now(timezone.utc)
    max_days = int(config.get("cache_dias", 25))
    out: dict[str, dict] = {}
    pending = []
    for t in targets:
        cached = load_cache(root, t["id"])
        if not refresh and is_fresh(cached, max_days, now):
            out[t["id"]] = cached
        else:
            pending.append(t)
    log(f"Métricas en caché: {len(out)}; por obtener: {len(pending)}")
    derived = config.get("derivados") or {}
    manual_pkgs = config.get("paquetes") or {}

    def work(chunk: list[dict]) -> list[tuple[str, dict]]:
        try:
            nodes = graphql_batch([t["gh"] for t in chunk], now, gh)
        except MetricsError as error:
            return [(t["id"], {"id": t["id"], "gh": t["gh"], "fecha": now.date().isoformat(), "error": str(error)[:300]}) for t in chunk]
        results = []
        for t in chunk:
            node = nodes.get(t["gh"])
            if not node:
                results.append((t["id"], {"id": t["id"], "gh": t["gh"], "fecha": now.date().isoformat(), "error": "no resuelto por la API de GitHub"}))
                continue
            fn = node["nameWithOwner"]
            try:
                contribs = contributors(fn, gh)
            except MetricsError as error:
                contribs, cerr = None, str(error)[:200]
            else:
                cerr = None
            m = summarize(node, contribs, now)
            upstream = derived.get(t["id"]) or None
            if upstream:
                m["derivado_de"] = upstream
                m["commits_brutos_90d"], m["commits_brutos_365d"] = m["commits_90d"], m["commits_365d"]
                m.update(owner_history(fn, m["propietario_id"], now, gh))
                try:
                    up = {c["login"] for c in (contributors(upstream, gh) or [])}
                except MetricsError:
                    up = set()
                own = [c for c in (contribs or []) if not c["bot"] and c["login"] not in up]
                tot = sum(c["n"] for c in own)
                m["contribuidores_top100"] = len(own)
                m["cuota_principal"] = round(own[0]["n"] / tot, 3) if own and tot else None
            if m.get("licencia_spdx") in (None, "NOASSERTION", "OTHER"):
                m["licencia_clase_auto"], m["licencia_motivo_auto"] = classify_licence_text(licence_text(fn, gh))
            pkgs = dict(manual_pkgs.get(t["id"]) or {}) or verify_guesses(t["id"], fn, detect_packages(t["id"], fn, t["texts"]), http)
            m.update(downloads(pkgs, http))
            m.update(scorecard(fn, http))
            m.update({"id": t["id"], "gh": t["gh"], "fecha": now.date().isoformat()})
            if cerr:
                m["error_contribuidores"] = cerr
            results.append((t["id"], m))
        return results

    chunks = [pending[i:i + batch] for i in range(0, len(pending), batch)]
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for res in pool.map(work, chunks):
            for rid, m in res:
                save_cache(root, rid, m)
                out[rid] = m
            done += 1
            if done % 10 == 0:
                log(f"  lotes {done}/{len(chunks)}")
    return out
