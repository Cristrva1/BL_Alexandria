"""Métricas canónicas de Codeberg y del Hub de modelos de Hugging Face."""
from __future__ import annotations

import base64
import re
import tomllib
from collections import Counter
from datetime import datetime, timedelta
from urllib.parse import quote, urlsplit

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .metrics import RECENT_ISSUES, UA, response_stats, semver_major


def pages(session, url):
    """Seguir únicamente la paginación del mismo origen, sin contar páginas parciales."""
    origin = urlsplit(url).netloc
    visited = set()
    while url:
        if url in visited or urlsplit(url).netloc != origin or urlsplit(url).scheme != "https":
            raise ValueError("Paginación inesperada al consultar las métricas")
        visited.add(url)
        response = session.get(url, timeout=30)
        response.raise_for_status()
        rows = response.json()
        if not isinstance(rows, list):
            raise ValueError(f"Se esperaba una lista en {url}")
        yield from rows
        url = response.links.get("next", {}).get("url")


def document(session, url, *, optional=False):
    response = session.get(url, timeout=30)
    if optional and response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()


def timestamp(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def history(rows, now, *, provider):
    commits_90d = commits_365d = 0
    authors = Counter()
    unknown = False
    for row in rows:
        if provider == "codeberg":
            info = row["commit"]
            when = timestamp(info["committer"]["date"])
            author = (row.get("author") or {}).get("login")
            if not author or author.casefold() == "ghost":
                author = info["author"].get("email") or info["author"].get("name")
        else:
            when = timestamp(row["date"])
            names = row["authors"]
            author = names[0].get("user") if names else None
        commits_90d += now - timedelta(days=90) <= when <= now
        commits_365d += now - timedelta(days=365) <= when <= now
        if not author:
            unknown = True
        elif "[bot]" not in author.casefold():
            authors[author.casefold()] += 1
    top = [count for _, count in authors.most_common(100)]
    return {"commits_90d": commits_90d, "commits_365d": commits_365d,
            "contribuidores_top100": None if unknown else len(top),
            "cuota_principal": round(top[0] / sum(top), 3) if top and not unknown else None}


def codeberg_user(row):
    login = row.get("original_author") or (row.get("user") or {}).get("login") or ""
    return login if login.casefold() != "ghost" else ""


def codeberg(session, target, now):
    base = "https://codeberg.org/api/v1/repos/" + target["source"]
    repo = document(session, base)
    if repo["full_name"].casefold() != target["source"].casefold():
        raise ValueError("La identidad de Codeberg no coincide con la ficha")
    branch = base + "/branches/" + quote(repo["default_branch"], safe="")
    revision = document(session, branch)["commit"]["id"]
    commits = base + f"/commits?sha={revision}&limit=50&stat=false&files=false&verification=false"
    releases_url = base + "/releases?limit=50"
    releases = [r for r in pages(session, releases_url) if not r["draft"] and not r["prerelease"] and r.get("published_at")]
    releases.sort(key=lambda r: timestamp(r["published_at"]), reverse=True)
    names = [r["tag_name"] for r in releases]
    issues_url = base + "/issues?type=issues&state=all&sort=latest&limit=50"
    issues = list(pages(session, issues_url)) if repo["has_issues"] else []
    issues.sort(key=lambda i: timestamp(i["created_at"]), reverse=True)
    closed = sum(i["state"] == "closed" for i in issues)
    sample = []
    for issue in issues[:RECENT_ISSUES]:
        author = codeberg_user(issue)
        if not author:
            continue
        comments = []
        if issue["comments"]:
            url = f"{base}/issues/{issue['number']}/comments?limit=6"
            comments = document(session, url)
            if any(not codeberg_user(c) for c in comments):
                continue
        sample.append({"createdAt": issue["created_at"], "closedAt": issue.get("closed_at"), "author": {"login": author},
                       "comments": {"nodes": [{"createdAt": c["created_at"], "author": {"login": codeberg_user(c)}} for c in comments]}})
    project_url = f"{base}/contents/pyproject.toml?ref={revision}"
    project = document(session, project_url, optional=True)
    license_id = None
    if project:
        package = tomllib.loads(base64.b64decode(project["content"]).decode("utf8"))
        expression = package.get("project", {}).get("license")
        if isinstance(expression, str):
            license_id = expression
    owner = repo["owner"]["login"]
    org_url = "https://codeberg.org/api/v1/orgs/" + quote(owner, safe="")
    org = document(session, org_url, optional=True)
    age = max((now - timestamp(repo["created_at"])).days, 0)
    return {"full_name": repo["full_name"], "revision": revision, "creado": repo["created_at"][:10], "edad_dias": age,
            "estrellas": repo["stars_count"], "estrellas_anio": round(repo["stars_count"] / max(age / 365, 0.25), 1),
            "forks": repo["forks_count"], "archivado": repo["archived"], "propietario": owner,
            "propietario_tipo": "Organization" if org else "User", "lenguaje": repo["language"], "homepage": repo["website"],
            "licencia_spdx": license_id, "issues_habilitadas": repo["has_issues"],
            "issues_abiertas": len(issues) - closed if repo["has_issues"] else None,
            "issues_cerradas": closed if repo["has_issues"] else None, "ratio_cerradas": round(closed / len(issues), 3) if issues else None,
            "issues_omitidas_por_anonimato": min(RECENT_ISSUES, len(issues)) - len(sample), **response_stats(sample, now),
            "releases_365d": sum(now - timedelta(days=365) <= timestamp(r["published_at"]) <= now for r in releases),
            "ultima_version": names[0] if names else None, "semver_mayor": semver_major(names),
            **history(pages(session, commits), now, provider="codeberg"),
            "fuentes": {"repositorio": base, "rama": branch, "commits": commits, "releases": releases_url, "issues": issues_url,
                        "licencia": project_url, "organizacion": org_url},
            "notas_fuente": ["Estrellas y antigüedad desde el alta en Codeberg. El historial importado cuenta para la actividad.",
                             f"Primera respuesta: {len(sample)} de {min(RECENT_ISSUES, len(issues))} incidencias recientes "
                             "con identidades reconocibles para el cálculo."]}


def huggingface(session, target, now):
    base = "https://huggingface.co/api/models/" + target["source"]
    model = document(session, base)
    if model["id"].casefold() != target["source"].casefold():
        raise ValueError("La identidad del modelo no coincide con la ficha")
    sha = model["sha"]
    commits = f"{base}/commits/{sha}"
    owner = model["author"]
    org_url = "https://huggingface.co/api/organizations/" + quote(owner, safe="") + "/overview"
    org = document(session, org_url, optional=True)
    card = model.get("cardData") or {}
    license_id = card.get("license")
    license_name = card.get("license_name")
    page = f"https://huggingface.co/{model['id']}"
    readme_url = f"{page}/raw/{sha}/README.md"
    readme = session.get(readme_url, timeout=30)
    readme.raise_for_status()
    homepage = target.get("homepage")
    links = {link.rstrip("/") for link in re.findall(r"https?://[^\s<>\")]+", readme.text)}
    age = max((now - timestamp(model["createdAt"])).days, 0)
    out = {"full_name": model["id"], "revision": sha, "creado": model["createdAt"][:10], "edad_dias": age,
           "likes": model["likes"], "likes_anio": round(model["likes"] / max(age / 365, 0.25), 1),
           "huggingface_mes": model["downloads"], "ultimo_push": model["lastModified"][:10],
           "propietario": owner, "propietario_tipo": "Organization" if org else "User",
           "homepage": homepage if homepage and homepage.rstrip("/") in links else None,
           "licencia_spdx": license_id.upper() if isinstance(license_id, str) else None, "nombre_licencia": license_name,
           **history(pages(session, commits), now, provider="huggingface"),
           "fuentes": {"modelo": base, "commits": commits, "organizacion": org_url, "ficha": readme_url,
                       "licencia": f"{page}/blob/{sha}/LICENSE", "descargas": "https://huggingface.co/docs/hub/models-download-stats"},
           "notas_fuente": ["Adopción: los «me gusta» del Hub se usan como señal comparable a estrellas, junto con las descargas de 30 días.",
                            "El historial corresponde a la publicación de los pesos. Las discusiones del Hub y las versiones comerciales quedan fuera de los indicadores de incidencias y lanzamientos."]}
    if license_id == "other" and license_name == "modified-mit":
        out.update(licencia_clase_auto="source_available", licencia_motivo_auto="Modified MIT según la ficha y licencia de los pesos.")
    return out


def collect_native(target, now):
    with requests.Session() as session:
        session.headers.update(UA)
        retries = Retry(total=2, backoff_factor=0.5, status_forcelist=(429, 500, 502, 503, 504))
        session.mount("https://", HTTPAdapter(max_retries=retries))
        provider = target["provider"]
        result = {"codeberg": codeberg, "huggingface": huggingface}[provider](session, target, now)
    return {**result, "id": target["id"], "proveedor_metricas": provider, "fecha": now.date().isoformat(),
            "observado_en": now.isoformat(timespec="seconds")}
