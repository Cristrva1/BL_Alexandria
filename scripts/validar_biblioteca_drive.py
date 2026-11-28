"""Valida una copia local de la biblioteca de Drive (v2) contra `curation/drive/PROTOCOLO.md`.

Uso:
    uv run python scripts/validar_biblioteca_drive.py <copia_local_de_la_biblioteca>
        [--corridas-desde AAAA-MM-DD] [--terminos-privados archivo.txt] [--json informe.json]

Sale con código 1 si hay errores. Los avisos no bloquean.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

KEYS = [
    "id", "responsable", "plataforma", "formato", "autor", "publicado", "capturado", "tipo",
    "prioridad", "fuente", "fuentes_extra", "repos", "enlaces", "contenido", "riesgo",
    "compartido_por", "legado",
]
ALLOWED = {
    "responsable": {"grok", "muse"},
    "plataforma": {"X", "Instagram", "Facebook", "Otro"},
    "formato": {"publicación", "hilo", "artículo", "reel", "carrusel", "video", "imagen", "mensaje", "otro"},
    "tipo": {
        "Técnica o estrategia", "Guía o tutorial", "Lista de recursos", "Herramienta o servicio",
        "Repositorio", "Skill o plugin", "Prompt", "Modelo o API", "Novedad", "Opinión o estudio",
        "Aprendizaje", "Entretenimiento", "Otro",
    },
    "prioridad": {"", "alta", "media", "exploratoria"},
    "contenido": {"completo", "parcial", "sin_contenido"},
}
RIESGOS = {"seguridad", "privacidad", "legal", "financiero", "pago", "instrucciones"}
DECISIONES = {
    "nueva", "fusion", "fusion_propuesta", "pendiente_contenido", "duplicado", "omitida",
    "correccion", "propuesta_subcategoria", "archivo_grande", "error_escritura",
}
ID_RE = re.compile(r"^(X-\d{5,25}|IG-[A-Za-z0-9_-]{5,40}|FB-[A-Za-z0-9]{4,100}|MSG-(IG|FB)-\d{8}-[0-9a-f]{6})$")
HEAD_RE = re.compile(r"^## (\S+) · (.+)$")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
GH_URL_RE = re.compile(r"https?://(?:www\.)?github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
GH_RESERVED = {"orgs", "topics", "features", "marketplace", "sponsors", "settings", "apps", "collections",
               "trending", "login", "about", "pricing", "enterprise", "search", "explore", "users", "site"}
STATUS_RE = re.compile(r"Ya integrado en BL_Alexandria|Candidato BL_Alexandria|Estado catálogo", re.I)
MAX_WARN, MAX_ERR = 150_000, 300_000


def id_from_url(url: str) -> str | None:
    """ID estable a partir de la URL de origen (protocolo §4)."""
    if m := re.search(r"(?:x|twitter)\.com/[^/\s]+/status(?:es)?/(\d+)", url):
        return "X-" + m.group(1)
    if m := re.search(r"instagram\.com/(?:[^/\s]+/)?(?:p|reel|reels|tv)/([A-Za-z0-9_-]+)", url):
        return "IG-" + m.group(1)
    if m := re.search(r"facebook\.com/.*?(?:reel/|videos/|posts/|story_fbid=|[?&]v=|permalink/|share/[rvp]/)([A-Za-z0-9]+)", url):
        return "FB-" + m.group(1)
    return None


def message_id(platform: str, date_iso: str, title: str) -> str:
    plat = "FB" if platform.lower().startswith("f") else "IG"
    return f"MSG-{plat}-{date_iso.replace('-', '')}-{hashlib.sha1(title.encode('utf-8')).hexdigest()[:6]}"


@dataclass
class Ficha:
    id: str
    title: str
    file: str
    line: int
    meta: dict
    body: str


@dataclass
class Report:
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    fichas: list = field(default_factory=list)
    stats: dict = field(default_factory=dict)
    to_review: list = field(default_factory=list)

    def err(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{where}: {msg}")


def split_outside_fences(lines):
    """Devuelve [(nº línea, texto, dentro_de_bloque)] y si quedó un bloque abierto."""
    out, fence = [], None
    for n, line in enumerate(lines, 1):
        m = FENCE_RE.match(line)
        if m:
            mark = m.group(1)
            if fence is None:
                fence = mark
                out.append((n, line, True))
                continue
            if mark[0] == fence[0] and len(mark) >= len(fence) and not m.group(2).strip():
                fence = None
                out.append((n, line, True))
                continue
        out.append((n, line, fence is not None))
    return out, fence is not None


def parse_meta(block_lines):
    meta, order = {}, []
    for raw in block_lines:
        if not raw.strip():
            continue
        key, sep, value = raw.partition(":")
        if not sep:
            meta.setdefault("_malformed", []).append(raw)
            continue
        key = key.strip()
        meta[key] = value.strip()
        order.append(key)
    meta["_order"] = order
    return meta


def parse_file(path: Path, rel: str, rep: Report):
    text = path.read_text(encoding="utf-8")
    size = len(text.encode("utf-8"))
    if size > MAX_ERR:
        rep.err(rel, f"archivo de {size // 1000} KB supera el límite de {MAX_ERR // 1000} KB")
    elif size > MAX_WARN:
        rep.warn(rel, f"archivo de {size // 1000} KB: conviene dividirlo")
    lines = text.splitlines()
    marked, open_fence = split_outside_fences(lines)
    if open_fence:
        rep.err(rel, "bloque de código sin cerrar")
    if lines and not lines[0].startswith("# "):
        rep.warn(rel, "la primera línea debería ser el título '# …'")
    heads = [(n, l) for n, l, inf in marked if not inf and l.startswith("## ")]
    fichas = []
    for idx, (n, line) in enumerate(heads):
        m = HEAD_RE.match(line)
        if not m:
            rep.err(f"{rel}:{n}", f"encabezado de ficha inválido: {line[:80]!r}")
            continue
        end = heads[idx + 1][0] - 1 if idx + 1 < len(heads) else len(lines)
        chunk = lines[n:end]
        j = 0
        while j < len(chunk) and not chunk[j].strip():
            j += 1
        if j >= len(chunk) or chunk[j].strip() != "```ficha":
            rep.err(f"{rel}:{n}", f"{m.group(1)}: falta el bloque ```ficha tras el encabezado")
            continue
        k = j + 1
        while k < len(chunk) and chunk[k].strip() != "```":
            k += 1
        meta = parse_meta(chunk[j + 1:k])
        body = "\n".join(chunk[k + 1:])
        fichas.append(Ficha(m.group(1), m.group(2).strip(), rel, n, meta, body))
    return fichas


def check_ficha(f: Ficha, rep: Report, private_terms):
    where = f"{f.file}:{f.line} {f.id}"
    meta = f.meta
    if not ID_RE.match(f.id):
        rep.err(where, "ID con formato inválido")
    missing = [k for k in KEYS if k not in meta]
    if missing:
        rep.err(where, "faltan claves: " + ", ".join(missing))
    if meta.get("_malformed"):
        rep.err(where, f"líneas sin 'clave: valor' en el bloque: {meta['_malformed'][:2]}")
    extra = [k for k in meta["_order"] if k not in KEYS]
    if extra:
        rep.warn(where, "claves desconocidas: " + ", ".join(extra))
    if meta.get("id") and meta["id"] != f.id:
        rep.err(where, f"el id del bloque ({meta['id']}) no coincide con el encabezado")
    for key, allowed in ALLOWED.items():
        if key in meta and meta[key] not in allowed:
            rep.err(where, f"{key}={meta[key]!r} no es un valor permitido")
    for r in meta.get("riesgo", "").split():
        if r not in RIESGOS:
            rep.err(where, f"riesgo {r!r} no permitido")
    for key in ("publicado", "capturado"):
        v = meta.get(key, "")
        if v and not DATE_RE.match(v):
            rep.err(where, f"{key}={v!r} no es AAAA-MM-DD")
    if not meta.get("capturado") and not meta.get("legado"):
        rep.err(where, "falta 'capturado' en una ficha nueva")
    fuente = meta.get("fuente", "")
    if fuente:
        derived = id_from_url(fuente)
        if derived and derived != f.id:
            rep.err(where, f"el ID no corresponde a la fuente (debería ser {derived})")
        if not derived and not f.id.startswith("MSG-"):
            rep.warn(where, "no se puede derivar un ID de la fuente")
    elif not f.id.startswith("MSG-"):
        rep.err(where, "falta la fuente")
    repos = meta.get("repos", "").split()
    for r in repos:
        if not REPO_RE.match(r):
            rep.err(where, f"repo {r!r} no tiene forma owner/repo")
    for u in meta.get("enlaces", "").split() + meta.get("fuentes_extra", "").split():
        if not u.startswith("http"):
            rep.err(where, f"enlace {u!r} no es una URL")
    declared = {r.lower() for r in repos}
    in_body = {f"{o}/{re.sub(r'.git$', '', n)}".lower().rstrip(".")
               for o, n in GH_URL_RE.findall(f.body) if o.lower() not in GH_RESERVED}
    undeclared = sorted(in_body - declared)
    if undeclared:
        rep.warn(where, "repos en el texto que faltan en 'repos': " + ", ".join(undeclared[:5]))
    if STATUS_RE.search(f.body):
        rep.warn(where, "el texto marca estados de Alexandría (lo lleva Codex)")
    if private_terms:
        public_part = f.body.split("**Notas privadas:**")[0]
        hits = [t for t in private_terms
                if re.search(rf"(?<![\w]){re.escape(t)}(?![\w])", public_part, re.IGNORECASE)]
        if hits:
            rep.warn(where, "términos privados fuera de 'Notas privadas': " + ", ".join(hits[:3]))


def parse_run(path: Path, rel: str, rep: Report):
    lines = path.read_text(encoding="utf-8").splitlines()
    state = lines[0].strip() if lines else ""
    if state not in ("estado: terminada", "estado: en_curso"):
        rep.err(rel, "la primera línea debe ser 'estado: terminada' o 'estado: en_curso'")
    rows = []
    for n, line in enumerate(lines, 1):
        if not line.startswith("|") or set(line.replace("|", "").strip()) <= {"-", " "}:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0] == "id":
            continue
        if len(cells) < 3:
            rep.err(f"{rel}:{n}", "fila con menos de 3 columnas")
            continue
        rows.append((n, cells[0], cells[1], cells[2], state))
    return rows


def validate(root: Path, since: str | None = None, private_terms=()):
    rep = Report()
    for name in ("00_LEEME_PROTOCOLO.md", "00_INDICE.md"):
        if not (root / name).is_file():
            rep.err(name, "falta en la raíz")
    runs_dir = root / "90_Corridas"
    for agent in ("grok", "muse"):
        if not (runs_dir / agent).is_dir():
            rep.warn(f"90_Corridas/{agent}", "no existe la carpeta de corridas")
    fichas: list[Ficha] = []
    per_cat = Counter()
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        parts = rel.split("/")
        if parts[0] == "90_Corridas" or len(parts) == 1:
            continue
        if len(parts) != 3 or not re.match(r"^\d\d_", parts[2]):
            rep.warn(rel, "ruta fuera de la estructura <área>/<categoría>/<NN_subcategoría>.md")
        found = parse_file(path, rel, rep)
        fichas.extend(found)
        per_cat["/".join(parts[:2])] += len(found)
    by_id = defaultdict(list)
    for f in fichas:
        by_id[f.id].append(f)
        check_ficha(f, rep, private_terms)
    for fid, group in by_id.items():
        if len(group) > 1:
            rep.err(fid, "ID repetido en " + ", ".join(f"{g.file}:{g.line}" for g in group))
    ids = set(by_id)
    for f in fichas:
        for u in f.meta.get("fuentes_extra", "").split():
            other = id_from_url(u)
            if other and other in ids and other != f.id:
                rep.warn(f"{f.file}:{f.line} {f.id}", f"fuente extra {other} también es una ficha: ¿duplicado?")
    repo_owners = defaultdict(set)
    for f in fichas:
        for r in f.meta.get("repos", "").split():
            repo_owners[r.lower()].add(f.id)
    shared = {r: sorted(v) for r, v in repo_owners.items() if len(v) > 1}
    run_rows = []
    if runs_dir.is_dir():
        for path in sorted(runs_dir.rglob("*.md")):
            rel = path.relative_to(root).as_posix()
            if rel.startswith("90_Corridas/migracion/") or path.name == "LEEME.md":
                continue
            if not re.match(r"^\d{4}-\d{2}-\d{2}", path.name):
                rep.warn(rel, "el nombre de una corrida debe empezar por AAAA-MM-DD")
            for n, fid, decision, archivo, state in parse_run(path, rel, rep):
                where = f"{rel}:{n}"
                before = len(rep.errors)
                if decision not in DECISIONES:
                    rep.err(where, f"decisión {decision!r} no permitida")
                if fid and not ID_RE.match(fid):
                    rep.err(where, f"ID {fid!r} con formato inválido")
                if decision in ("nueva", "fusion"):
                    target = root / archivo if archivo else None
                    if not target or not target.is_file():
                        rep.err(where, f"{fid}: el archivo {archivo!r} no existe")
                    elif fid not in ids or all(f.file != archivo for f in by_id[fid]):
                        rep.err(where, f"{fid}: no aparece en {archivo}")
                run_rows.append({"run": rel, "id": fid, "decision": decision, "archivo": archivo,
                                 "estado": state, "valida": len(rep.errors) == before})
    if since:
        rep.to_review = [r for r in run_rows if Path(r["run"]).name[:10] >= since
                         and r["decision"] in ("nueva", "fusion") and r["estado"] == "estado: terminada"
                         and r["valida"]]
    rep.fichas = fichas
    rep.stats = {
        "fichas": len(fichas),
        "por_categoria": dict(sorted(per_cat.items())),
        "responsable": dict(Counter(f.meta.get("responsable", "") for f in fichas)),
        "contenido": dict(Counter(f.meta.get("contenido", "") for f in fichas)),
        "riesgo": dict(Counter(r for f in fichas for r in f.meta.get("riesgo", "").split())),
        "repos_unicos": len(repo_owners),
        "repos_en_varias_fichas": len(shared),
        "corridas": dict(Counter(r["decision"] for r in run_rows)),
    }
    return rep


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("root", type=Path)
    ap.add_argument("--corridas-desde", dest="since")
    ap.add_argument("--terminos-privados", type=Path)
    ap.add_argument("--json", type=Path)
    args = ap.parse_args(argv)
    terms = []
    if args.terminos_privados and args.terminos_privados.is_file():
        terms = [t.strip() for t in args.terminos_privados.read_text(encoding="utf-8").splitlines() if t.strip()]
    rep = validate(args.root, args.since, terms)
    print(json.dumps(rep.stats, ensure_ascii=False, indent=1))
    print(f"\nErrores: {len(rep.errors)} · Avisos: {len(rep.warnings)}")
    for e in rep.errors[:50]:
        print("  ERROR", e)
    for w in rep.warnings[:30]:
        print("  aviso", w)
    if args.since:
        print(f"\nFichas a revisar desde {args.since}: {len(rep.to_review)}")
    if args.json:
        args.json.write_text(json.dumps({
            "stats": rep.stats, "errors": rep.errors, "warnings": rep.warnings, "to_review": rep.to_review,
        }, ensure_ascii=False, indent=1), encoding="utf-8")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
