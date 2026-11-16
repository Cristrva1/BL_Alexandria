"""Ampliación del catálogo aprobada por el propietario, 2026-11-16 (190 repos en lotes).

Cada lote vive en dos archivos editables:

- ``curation/expansion-2026-11-16/<lote>.json``: identidad, categoría, acceso, ejemplos y
  primera prueba de cada repo (campos del índice compacto y del detalle);
- ``curation/descripciones-4s/47-expansion-<lote>.json``: las 4 secciones, que se aplican con
  ``apply_descripciones_4s.py``.

El script audita cada identidad con la API de GitHub (metadatos, README y árbol raíz) en
``data/reports/expansion-20261116/`` (ignorado), rechaza repos ya catalogados, retirados o
archivados, y escribe las entradas. No instala ni ejecuta ningún proyecto catalogado.

    uv run python scripts/catalog_expansion_20261116.py p01 --fetch   # auditoría vía gh api
    uv run python scripts/catalog_expansion_20261116.py p01 --apply   # escribe los índices
"""
from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))

import document_curation_20261114 as base  # noqa: E402
from import_document_repos import inspect_repository  # noqa: E402
from repo_intelligence.core.access import access_routes  # noqa: E402

DATE = "2026-11-16"
base.DATE = DATE
AUDIT = ROOT / "data/reports/expansion-20261116"
SPECS = ROOT / "curation/expansion-2026-11-16"
REPORT = ROOT / "reports/catalog-expansion-2026-11-16.json"
ROLE = {"skill": "skill", "reference": "directory", "library": "library", "app": "app", "server": "platform", "model": "runtime",
        "mcp": "runtime", "agent": "app", "framework": "library", "engine": "runtime", "template": "library"}
AI = {"local": base.LOCAL, "local_choice": base.LOCAL_CHOICE, "optional": base.OPTIONAL, "required": base.REQUIRED, "depends": base.PROVIDER}
AVOID = {"library": "buscas una aplicación lista y no quieres preparar un proyecto de código",
         "framework": "buscas una aplicación lista y no quieres preparar un proyecto de código",
         "mcp": "necesitas un producto autónomo y esta pieza requiere un cliente MCP",
         "reference": "necesitas una aplicación lista para ejecutar en lugar de material de consulta",
         "model": "no tienes el hardware o no aceptas la licencia de los pesos",
         "engine": "no quieres preparar modelos, dependencias y hardware propios",
         "server": "no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones",
         "agent": "necesitas una herramienta estable y auditada para datos sensibles",
         "app": "necesitas una instalación sin cuentas ni dependencias adicionales"}


def gh(path: str) -> dict:
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    return json.loads(out.stdout) if out.returncode == 0 else {}


def load(batch: str) -> list[dict]:
    specs = json.loads((SPECS / f"{batch}.json").read_text(encoding="utf8"))["repos"]
    for s in specs:
        assert 60 <= len(s["one"]) <= 175, (s["id"], len(s["one"]))
        assert len(s["examples"]) == 2 and len(s["try"]) == 2, s["id"]
    return specs


def review_fields(spec, entry, access, source):
    scenarios = spec["examples"]
    action, success = spec["try"]
    return {
        "cases": scenarios, "why": "Usos propuestos: " + "; ".join(scenarios) + ".",
        "choose_if": "Tu objetivo encaja con estos ejemplos: " + "; ".join(scenarios),
        "models": spec.get("models") or "No usa LLM ni API de IA", "source_archived": False,
        "practical_examples": [{"scenario": s, "status": "illustrative"} for s in scenarios],
        "first_try": {"action": action, "success": success, "execution": "proposed_not_executed"},
        "editorial_review": {"status": "source_reviewed", "checked_at": DATE, "source": source["html_url"],
                             "source_blob_sha": source["sha"], "previous_category": [entry["cat"], entry["sub"]],
                             "category_verdict": "confirmed", "note": spec.get("note") or access.get("api_note", ""),
                             "checks": ["identity", "category", "examples", "installation_source", "api_costs",
                                        "claude_code", "codex", "antigravity", "local_model"],
                             "installation_tested": False},
    }


def github_block(meta: dict) -> dict:
    rel = gh(f"repos/{meta['full_name']}/releases/latest")
    block = {"name_with_owner": meta["full_name"], "archived": bool(meta.get("archived")), "pushed_at": (meta.get("pushed_at") or "")[:10],
             "license": (meta.get("license") or {}).get("spdx_id"), "primary_language": meta.get("language"), "checked_at": DATE}
    if rel.get("tag_name"):
        block["latest_release"] = f"{rel['tag_name']} ({(rel.get('published_at') or '')[:10]})"
    return block


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch")
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    compact = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))
    specs = load(args.batch)
    known = {str(r["github_id"]): r["id"] for r in compact["repos"] if r.get("github_id") and not r.get("alias_of")}
    records = {}
    for s in specs:
        if s["id"] in {r["id"] for r in compact["repos"]}:
            continue  # ya aplicado: la migración es idempotente
        rec = inspect_repository(s["gh"], known, AUDIT / "github") if args.fetch else json.loads((AUDIT / "github" / (s["gh"].replace("/", "--") + ".json")).read_text(encoding="utf8"))
        records[s["id"]] = rec
    retired = {r["github_id"] for r in json.loads((ROOT / "data/retired.json").read_text(encoding="utf8"))["repos"]}
    batch4s = ROOT / f"curation/descripciones-4s/47-expansion-{args.batch}.json"
    four = json.loads(batch4s.read_text(encoding="utf8")) if batch4s.exists() else None
    added, problems = [], []
    by_id = {r["id"]: r for r in compact["repos"]}
    for s in specs:
        rid = s["id"]
        if rid not in records:
            continue
        row = records[rid]
        if row["status"] != "new":
            problems.append(f"{rid}: estado {row['status']} ({row.get('catalog_id') or row.get('error')})")
            continue
        meta, source = row["metadata"], row["readme"]
        if meta["full_name"].lower() != s["gh"].lower():
            problems.append(f"{rid}: el repo canónico es {meta['full_name']} (spec {s['gh']})")
        if meta.get("archived"):
            problems.append(f"{rid}: archivado")
        if meta["id"] in retired:
            problems.append(f"{rid}: en data/retired.json")
        text = base64.b64decode(source["content"]).decode("utf8", errors="replace")
        entry = {"id": rid, "kind": s["kind"], "cat": s["cat"], "sub": s["sub"], "one": s["one"]}
        for key, group in AI.items():
            (group.add if s.get("ai") == key else group.discard)(rid)
        if s.get("ready"):
            base.READY.add(rid)
        if s.get("cmd"):
            base.ENTRY_COMMANDS[rid] = s["cmd"]
        access = base.access_profile(entry, source, text)
        access["antigravity"] = "not_documented"
        access.update(s.get("access") or {})
        start = base.starting(entry, source, text, access, meta)
        if s.get("cmd") and s["cmd"] not in text:
            problems.append(f"{rid}: el comando de entrada no aparece en el README")
        if s.get("url"):
            start["entry_url"] = s["url"]
        if s.get("steps"):
            start["steps"] = s["steps"]
        category = next(c for c in compact["categories"] if c["num"] == s["cat"])
        assert s["sub"] in {x["key"] for x in category["subs"]}, rid
        lic = s.get("license") or (meta.get("license") or {}).get("spdx_id")
        repo = {"id": rid, "name": s["name"], "cat": s["cat"], "sub": s["sub"], "role": ROLE[s["kind"]],
                "exec": "hybrid" if access["api"] in {"optional", "required", "depends"} else "local",
                "setup": s.get("setup", "medium"), "mcp": s["kind"] == "mcp" or bool(s.get("mcp")),
                "prov": s.get("prov", []), "tags": s.get("tags", []), "stars": meta["stargazers_count"], "gh": meta["full_name"],
                "lib": False, "pick": False, "one": s["one"], "alt": [], "doc": f"human/fichas/{rid}.md",
                "github_id": meta["id"], "lang": meta.get("language"), "license": lic, "added_at": DATE, "github_checked": DATE,
                "goals": s.get("goals", []), "source_archived": False}
        repo["routes"] = access_routes({"access": access})
        files = [i["path"] for i in row["tree"].get("tree", []) if i.get("type") == "blob"]
        manifests = [p for p in files if p in {"pyproject.toml", "package.json", "Cargo.toml", "go.mod", "CMakeLists.txt", "pom.xml",
                                                "build.gradle", "composer.json", "Gemfile", "requirements.txt", "Dockerfile",
                                                "docker-compose.yml", "compose.yaml", "mix.exs", "setup.py"}]
        limits = "Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada."
        if s["cat"] == 16:
            limits += " Las pruebas activas requieren un alcance autorizado y un entorno adecuado."
        if s["cat"] == 14:
            limits += " No se verificó rentabilidad ni operación con fondos."
        if s.get("caveat"):
            limits += " " + s["caveat"]
        d = {"name": s["name"], "cat": s["cat"], "sub": s["sub"], "desc": s["one"], "how": s["how"],
             "install": "Sigue la instalación y el ejemplo mínimo en " + source["html_url"], "cases": [s["one"]],
             "stack": ", ".join([v for v in [meta.get("language"), *manifests] if v]),
             "choose_if": "buscas esta función: " + s["one"], "avoid_if": s.get("avoid") or AVOID[s["kind"]], "limits": limits,
             "combines_with": [], "alternatives": [], "repo": meta["html_url"], "homepage": meta.get("homepage"),
             "license": lic, "lang": meta.get("language"), "updated": DATE, "doc": f"human/fichas/{rid}.md",
             "access": access, "getting_started": start, "first_step": start["steps"][0],
             "sources": {"readme_blob_sha": source["sha"], "root_tree_sha": row["tree"]["sha"], "readme_url": source["html_url"],
                         "github_checked": DATE, "collection": "catalog-expansion-2026-11-16"}}
        d.update(review_fields(s, entry, access, source))
        compact["repos"].append(repo)
        detail["repos"][rid] = d
        by_id[rid] = repo
        added.append({"id": rid, "full_name": meta["full_name"], "github_id": meta["id"], "readme_blob_sha": source["sha"],
                      "stars": meta["stargazers_count"], "license": lic, "pushed_at": (meta.get("pushed_at") or "")[:10]})
        if four and rid in four["repos"] and args.apply:
            four["repos"][rid]["github"] = github_block(meta)
    # Grupos de alternativas declarados en el lote (simétricos, máximo 5 por repo).
    spec_doc = json.loads((SPECS / f"{args.batch}.json").read_text(encoding="utf8"))
    for group in spec_doc.get("alt_groups", []):
        for left in group:
            for right in group:
                if left == right or left not in by_id or right not in by_id:
                    continue
                alts = by_id[left].setdefault("alt", [])
                if right not in alts:
                    alts.append(right)
                detail["repos"][left]["alternatives"] = alts
    for cat in compact["categories"]:
        cat["count"] = sum(r["cat"] == cat["num"] and not r.get("alias_of") for r in compact["repos"])
    for goal in compact["discovery"]["goals"]:
        members = [r for r in compact["repos"] if goal["id"] in r.get("goals", []) or r["id"] in goal["starters"] + goal["guided"]]
        goal["categories"] = sorted({r["cat"] for r in members})
    total = sum(not r.get("alias_of") for r in compact["repos"])
    compact["meta"]["updated"] = DATE
    compact["meta"]["title"] = f"Índice IA — {total} repos curados de IA, automatización y herramientas"
    print({"batch": args.batch, "new": len(added), "total": total, "problems": problems, "apply": args.apply})
    if problems:
        sys.exit(1)
    if args.apply:
        (ROOT / "INDICE_IA.json").write_text(json.dumps(compact, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
        (ROOT / "INDICE_IA.detalle.json").write_text(json.dumps(detail, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
        if four:
            batch4s.write_text(json.dumps(four, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
        report = json.loads(REPORT.read_text(encoding="utf8")) if REPORT.exists() else {
            "checked_at": DATE, "source": "Propuesta aprobada por el propietario (190 candidatos, 2026-11-16).", "batches": {},
            "notes": ["No se instaló ni se ejecutó ningún proyecto del catálogo.",
                      "Identidades verificadas con la API de GitHub (id numérico, propietario, licencia, archivado)."]}
        report["batches"][args.batch] = added
        report["added_count"] = sum(len(v) for v in report["batches"].values())
        report["total_repositories"] = total
        REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf8")


if __name__ == "__main__":
    main()
