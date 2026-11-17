"""Markdown compacto para agentes de código (Codex, Claude Code): uno por categoría y uno por subcategoría.

Solo lee ``INDICE_IA.json`` e ``INDICE_IA.detalle.json``. No inventa comandos: si el catálogo no tiene
uno documentado, lo dice y cita la fuente oficial. Los archivos grandes se dividen en partes.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

SITE = "https://cristrva1.github.io/BL_Alexandria/"
MAX_TOKENS = 25_000
CHARS_PER_TOKEN = 3.5  # estimación conservadora para español con tokenizadores o200k/cl100k
NIVEL = {1: "Básico", 2: "Intermedio", 3: "Avanzado", 4: "Experto"}
DUAL_SUBS = {(16, s) for s in ("reconocimiento", "pruebas", "agentes", "skills")}
OFFENSIVE_SUBS = {(16, "explotacion-c2"), (16, "ad-interno")}
PRIVACY_SUBS = {(10, "osint"), (28, "rostros")}
LIC_CLASS = {"osi_permisiva": "OSI permisiva", "osi_copyleft": "OSI copyleft", "open_core": "open-core",
             "source_available": "source-available", "propietaria": "propietaria", "desconocida": "sin licencia detectada"}
LIC_FLAGS = [
    (r"\bBSL\b|\bBUSL|Business Source", "BSL (source-available): no es OSI; revisa usos comerciales y la fecha de cambio de licencia"),
    (r"Elastic License|ELv2|Elastic-2\.0", "Elastic License 2.0 (source-available, no OSI): limita ofrecerlo como servicio gestionado"),
    (r"\bSSPL\b", "SSPL (no OSI)"),
    (r"\bAGPL", "AGPL: si lo modificas y lo expones en red, debes publicar tus cambios"),
    (r"de pago|premium|enterprise|comercial", "open-core o uso comercial limitado: parte de las funciones o datos son de pago"),
    (r"no OSI|NPSL|FSL-|Sustainable Use|Commons Clause|PolyForm", "licencia no OSI: revisa las condiciones de uso y redistribución"),
]
GENERIC_PREREQ = {"Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.",
                  "Un entorno de instalación o servidor y las dependencias indicadas por el README."}
INSTRUCTIONS = [
    "1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y "
    "lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.",
    "2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). "
    "Si nada encaja, dilo; no fuerces una elección.",
    "3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. "
    "Muestra el comando exacto y dónde se ejecutará antes de pedirla.",
    "4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.",
    "5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y "
    "licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).",
    "6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», "
    "lee la fuente oficial y cita la URL; no inventes comandos.",
    "7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.",
    "8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, "
    "la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio "
    "separado de producción.",
]


def estimate_tokens(text: str) -> int:
    return int(len(text) / CHARS_PER_TOKEN) + 1


def short(text: str | None, n: int = 220) -> str:
    text = re.sub(r"\s+", " ", (text or "").strip())
    if len(text) <= n:
        return text
    head = text[:n]
    cut = head.rsplit(". ", 1)[0] if ". " in head else ""
    if len(cut) > n * 0.6:
        return cut + "."
    return head.rsplit(" ", 1)[0].rstrip(",;:(") + "…"


def sentence(text: str | None) -> str:
    text = (text or "").strip().rstrip(".")
    return text[:1].upper() + text[1:] if text else ""


def _cell(text: str) -> str:
    return text.replace("|", "/").replace("\n", " ")


def _clean_when(text: str) -> str:
    return re.sub(r"^(Tu objetivo encaja con estos ejemplos|Usos propuestos):\s*", "Casos: ", (text or "").strip())


class _Ctx:
    def __init__(self, root: Path):
        self.compact = json.loads((root / "INDICE_IA.json").read_text(encoding="utf-8"))
        self.detail = json.loads((root / "INDICE_IA.detalle.json").read_text(encoding="utf-8"))["repos"]
        self.repos = [r for r in self.compact["repos"] if not r.get("alias_of") and int(r.get("cat") or 0) > 0]
        self.names = {r["id"]: r.get("name") or r["id"] for r in self.compact["repos"]}
        self.where = {r["id"]: (int(r["cat"]), r.get("sub")) for r in self.compact["repos"]}
        freq = Counter(v for x in self.detail.values() for v in (x.get("avoid_if"), x.get("limits")) if isinstance(v, str))
        self.generic = {v for v, n in freq.items() if n >= 15}
        dates = [(x.get("getting_started") or {}).get("checked_at") or "" for x in self.detail.values()]
        self.date = max((d for d in dates if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d)), default="")

    def licence(self, r: dict) -> str:
        d = self.detail.get(r["id"], {})
        return str(r.get("license") or d.get("license") or "—")

    def repo_url(self, r: dict) -> str:
        d = self.detail.get(r["id"], {})
        return d.get("repo_url") or (f"https://github.com/{r['gh']}" if r.get("gh") else d.get("repo") or "")


def _sorted(repos: list[dict]) -> list[dict]:
    return sorted(repos, key=lambda r: (-(r.get("puntuacion") or 0), r["id"]))


def _group(d: dict, rid: str) -> tuple[str, list[str], str]:
    sim = d.get("similares") or {}
    if not sim:
        return "sin grupo", [], ""
    return sim.get("papel", "—"), [x["id"] for x in sim.get("ranking", []) if x["id"] != rid], sim.get("titulo", "")


def _lic_flags(ctx: _Ctx, r: dict, d: dict) -> list[str]:
    lic = ctx.licence(r)
    lv = d.get("licencia_verificada") or {}
    blob = " ".join(str(x or "") for x in (lic, lv.get("texto"), lv.get("nota"), d.get("licencia_nota"), d.get("que_es"), d.get("descripcion_notas")))
    out = [msg for rx, msg in LIC_FLAGS if re.search(rx, blob, re.I)]
    if lic.upper() == "NOASSERTION":
        out.append("GitHub no identifica la licencia (NOASSERTION): confírmala en el archivo LICENSE/COPYING")
    elif lv.get("texto"):
        out.append(f"licencia confirmada leyendo LICENSE el {lv.get('fecha')} (GitHub: NOASSERTION)")
    return out


def _table(ctx: _Ctx, repos: list[dict], with_sub: bool) -> list[str]:
    head = "| Repo |" + (" Sub |" if with_sub else "") + " Para qué | Nivel | Puntuación | Licencia | Papel |"
    sep = "|---|" + ("---|" if with_sub else "") + "---|---|---:|---|---|"
    rows = [head, sep]
    for r in repos:
        d = ctx.detail.get(r["id"], {})
        role = _group(d, r["id"])[0]
        lvl = r.get("complejidad")
        cls = LIC_CLASS.get((d.get("calidad") or {}).get("licencia"), "")
        raw = ctx.licence(r)
        if raw.upper() == "NOASSERTION" and cls:
            lic = f"{raw} (sin confirmar)" if cls == LIC_CLASS["desconocida"] else f"{raw} → {cls} según el texto"
        else:
            lic = f"{raw} ({cls})" if cls else raw
        rows.append(f"| `{r['id']}` |" + (f" {r.get('sub')} |" if with_sub else "")
                    + f" {_cell(short(r.get('one'), 80))} | {lvl or '—'} {NIVEL.get(lvl, '')} | {r.get('puntuacion', '—')} | {_cell(short(lic, 90))} | {role} |")
    return rows


def _ficha(ctx: _Ctx, r: dict, cat: int, sub: str) -> list[str]:
    rid, d = r["id"], ctx.detail.get(r["id"], {})
    role, others, gtitle = _group(d, rid)
    gs = d.get("getting_started") or {}
    cx = d.get("complejidad_detalle") or {}
    acc = d.get("access") or {}
    L = [f"### {ctx.names[rid]} (`{rid}`)", "",
         f"- **Repo:** {ctx.repo_url(r)} · {ctx.licence(r)} · nivel {r.get('complejidad') or '—'} · {r.get('puntuacion', '—')}/100"
         + (f" · {role} en «{gtitle}»" if gtitle else ""),
         f"- **Qué es:** {short(d.get('que_es') or r.get('one'), 240)}"]
    row = next((x for x in (d.get("similares") or {}).get("ranking", []) if x["id"] == rid), {})
    when = row.get("cuando") if row.get("cuando_origen") == "curado" else (d.get("choose_if") or row.get("cuando"))
    if when:
        avoid = d.get("avoid_if") if d.get("avoid_if") and d["avoid_if"] not in ctx.generic else ""
        L.append(f"- **Cuándo elegirlo:** {sentence(short(_clean_when(when), 200))}." + (f" Evítalo si {avoid.rstrip('.')}." if avoid else ""))
    req = [x.strip() for x in gs.get("prerequisites", []) if x.strip() and x not in GENERIC_PREREQ]
    bits = [f"nivel {cx.get('nivel')}: {', '.join(cx.get('motivos') or [])}" if cx else "", d.get("stack") or "",
            f"hardware {acc.get('hardware')}" if acc.get("hardware") and acc.get("hardware") != "ordinary" else "",
            "API de IA: " + {"not_required": "no", "required": "sí", "optional": "opcional"}.get(acc.get("api"), acc.get("api") or "—")] + req
    L.append("- **Requisitos:** " + "; ".join(b for b in bits if b) + ".")
    cmd = (gs.get("command") or "").strip()
    src = gs.get("source") or (d.get("sources") or [ctx.repo_url(r)])[0]
    if cmd and gs.get("command_status") == "documented":
        lang = gs.get("command_language") or "bash"
        if "\n" in cmd or len(cmd) > 140:
            L += [f"- **Instalación (documentada en la fuente; no ejecutada):** fuente {src}", "", f"  ```{lang}", *[f"  {x}" for x in cmd.splitlines()], "  ```"]
        else:
            L.append(f"- **Instalación (documentada en la fuente; no ejecutada):** `{cmd}` — fuente: {src}")
    else:
        L.append(f"- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: {src}")
    ft = d.get("first_try") or {}
    if ft.get("action"):
        L.append(f"- **Primera prueba propuesta (no ejecutada):** {short(ft['action'], 200)}"
                 + (f" Éxito: {short(ft.get('success'), 120)}" if ft.get("success") else ""))
    combos = []
    for c in d.get("combina_con") or []:
        cid = c.get("id")
        if cid not in ctx.where:
            continue
        loc = "" if ctx.where[cid] == (cat, sub) else f" [{ctx.where[cid][0]}/{ctx.where[cid][1]}]"
        combos.append(f"`{cid}`{loc}")
    if combos:
        L.append("- **Combina con:** " + ", ".join(combos))
    alts = [a for a in dict.fromkeys(others + (r.get("alt") or [])) if a in ctx.where]
    if alts:
        L.append("- **Alternativas:** " + ", ".join(f"`{a}`" for a in alts))
    risks = []
    if (cat, sub) in OFFENSIVE_SUBS:
        risks.append("herramienta ofensiva: solo con autorización escrita y alcance definido")
    elif (cat, sub) in DUAL_SUBS:
        risks.append("uso dual: solo contra sistemas propios o con autorización")
    elif (cat, sub) in PRIVACY_SUBS:
        risks.append("uso dual con datos personales: respeta la privacidad y la base legal del tratamiento")
    risks += _lic_flags(ctx, r, d)
    if d.get("descripcion_notas"):
        risks.append(short(d["descripcion_notas"], 160))
    if d.get("limits") and d["limits"] not in ctx.generic and "revisión es documental" not in d["limits"]:
        risks.append(short(d["limits"], 160))
    if risks:
        L.append("- **Riesgos y avisos:** " + ". ".join(sentence(x) for x in risks) + ".")
    return L + [""]


def _snippet(name: str, topic: str) -> list[str]:
    return ["## Cómo referenciarlo desde AGENTS.md o CLAUDE.md", "",
            f"Guarda este archivo como `docs/alexandria/{name}` y añade:", "", "```markdown", "## Herramientas externas",
            f"Antes de proponer herramientas de «{topic}», lee `docs/alexandria/{name}` y sigue sus",
            "«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.", "```", "",
            f"En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/{name}` "
            "(carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).", ""]


def _header(title: str, scope: str, explore: str, date: str) -> list[str]:
    return [f"# Alexandría para agentes · {title}", "",
            f"{scope} Generado{' el ' + date if date else ''} desde `INDICE_IA.json` e `INDICE_IA.detalle.json` "
            "(Biblioteca de Alexandría, Binarias Labs).",
            f"Explorador en línea: {explore} · Ficha de cada repo: `{SITE}#/repo/<id>`", "",
            "## Instrucciones para el agente", "", *INSTRUCTIONS, ""]


SCORE_NOTE = ("Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. "
              "Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.")


def _pack(blocks: list[list[str]], budget_chars: int) -> list[list[list[str]]]:
    parts: list[list[list[str]]] = [[]]
    size = 0
    for block in blocks:
        n = sum(len(x) + 1 for x in block)
        if parts[-1] and size + n > budget_chars:
            parts.append([])
            size = 0
        parts[-1].append(block)
        size += n
    return parts


def _write_doc(out: Path, name: str, title: str, scope: str, explore: str, ctx: _Ctx, repos: list[dict],
               fichas: list[list[str]], with_sub: bool, meta: dict) -> list[dict]:
    """Escribe ``name`` y, si supera MAX_TOKENS, lo divide en partes ``-parte-N``."""
    head = _header(title, scope, explore, ctx.date)
    table = ["## Tabla de decisión", "", *_table(ctx, repos, with_sub), "", SCORE_NOTE, ""]
    body = [line for block in fichas for line in block]
    text = "\n".join(head + table + ["## Fichas", ""] + body + _snippet(name, title))
    if estimate_tokens(text) <= MAX_TOKENS:
        (out / name).write_text(text, encoding="utf-8")
        return [{**meta, "archivo": name, "caracteres": len(text), "tokens_estimados": estimate_tokens(text)}]
    fixed = len("\n".join(head + table)) + 2_500
    parts = _pack(fichas, int(MAX_TOKENS * CHARS_PER_TOKEN) - fixed)
    stem = name[:-3]
    names = [f"{stem}-parte-{i}.md" for i in range(1, len(parts) + 1)]
    index = head + table + [f"## Partes ({len(parts)})", "",
                            "Este tema supera ~25k tokens, así que las fichas están en partes. Carga solo la parte que contiene los repos de la tabla que te interesan:", ""]
    files = []
    for i, (pname, blocks) in enumerate(zip(names, parts), 1):
        ids = [re.search(r"\(`([^`]+)`\)", b[0]).group(1) for b in blocks]
        index.append(f"- `{pname}`: " + ", ".join(f"`{x}`" for x in ids))
        ptext = "\n".join(_header(f"{title} (parte {i} de {len(parts)})", scope, explore, ctx.date)
                          + [f"Índice y tabla de decisión completa: `{name}`.", "", "## Fichas", ""]
                          + [line for b in blocks for line in b] + _snippet(pname, title))
        (out / pname).write_text(ptext, encoding="utf-8")
        files.append({**meta, "archivo": pname, "parte": i, "caracteres": len(ptext), "tokens_estimados": estimate_tokens(ptext)})
    itext = "\n".join(index + [""] + _snippet(name, title))
    (out / name).write_text(itext, encoding="utf-8")
    return [{**meta, "archivo": name, "partes": names, "caracteres": len(itext), "tokens_estimados": estimate_tokens(itext)}] + files


def export_llm(project_root: Path, output_dir: Path) -> dict[str, Any]:
    """Genera ``categoria-N.md`` y ``categoria-N-<sub>.md`` (más partes si hace falta) e ``index.json``."""
    ctx = _Ctx(Path(project_root))
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("categoria-*.md"):
        old.unlink()
    files: list[dict] = []
    for category in sorted(ctx.compact["categories"], key=lambda c: int(c["num"])):
        cat = int(category["num"])
        if cat <= 0:
            continue
        in_cat = [r for r in ctx.repos if int(r["cat"]) == cat]
        if not in_cat:
            continue
        cat_fichas: list[list[str]] = []
        cat_repos: list[dict] = []
        for s in category.get("subs") or []:
            repos = _sorted([r for r in in_cat if r.get("sub") == s["key"]])
            if not repos:
                continue
            fichas = [_ficha(ctx, r, cat, s["key"]) for r in repos]
            files += _write_doc(out, f"categoria-{cat}-{s['key']}.md", s["title"],
                                f"Categoría {cat} «{category['title']}» › subcategoría `{s['key']}`. {len(repos)} repos.",
                                f"{SITE}#/explorar?cat={cat}&sub={s['key']}", ctx, repos, fichas, False,
                                {"cat": cat, "sub": s["key"], "titulo": s["title"], "repos": len(repos)})
            cat_repos += repos
            cat_fichas += fichas
        if not cat_repos:
            continue
        files += _write_doc(out, f"categoria-{cat}.md", category["title"],
                            f"Categoría {cat} completa ({len(cat_repos)} repos, {len(category.get("subs") or [])} subcategorías).",
                            f"{SITE}#/explorar?cat={cat}", ctx, cat_repos, cat_fichas, True,
                            {"cat": cat, "sub": None, "titulo": category["title"], "repos": len(cat_repos)})
    manifest = {"fecha": ctx.date, "max_tokens": MAX_TOKENS, "estimacion": f"caracteres / {CHARS_PER_TOKEN}", "archivos": files}
    (out / "index.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    largest = sorted(files, key=lambda f: -f["tokens_estimados"])[:5]
    return {"output_dir": str(out), "files": len(files), "largest": largest, "manifest": manifest}


def web_manifest(manifest: dict, prefix: str = "llm/") -> dict[str, dict]:
    """Mapa ``"16"`` / ``"16/deteccion"`` → archivo descargable para el explorador web."""
    out: dict[str, dict] = {}
    for f in manifest["archivos"]:
        if f.get("parte"):
            continue
        key = str(f["cat"]) if f["sub"] is None else f"{f['cat']}/{f['sub']}"
        out[key] = {"file": prefix + f["archivo"], "tokens": f["tokens_estimados"],
                    "parts": [prefix + p for p in f.get("partes") or []]}
    return out
