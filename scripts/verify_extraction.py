"""Verify that README extraction and re-curation are complete before deleting clones."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    root = Path.cwd()
    errors: list[str] = []
    warnings: list[str] = []
    ok: list[str] = []

    # 1. INDICE_IA.json has >= 185 repos (177 original - 6 duplicates + 11 missing + 3 new = 185)
    indice = json.load(open(root / "INDICE_IA.json", encoding="utf-8"))
    repos = indice.get("repos", [])
    total = len(repos)
    if total >= 185:
        ok.append(f"INDICE_IA.json tiene {total} repos (>=185 esperado)")
    else:
        errors.append(f"INDICE_IA.json solo tiene {total} repos (esperado >=185)")

    # 2. No repo with empty 'one' (except 'tools' which has no README)
    empty_one = [r["id"] for r in repos if not r.get("one") or len(r.get("one", "").strip()) < 10]
    empty_one = [r for r in empty_one if r != "tools"]
    if not empty_one:
        ok.append("Todos los repos tienen 'one' poblado (excepto 'tools')")
    else:
        warnings.append(f"Repos con 'one' vacio: {empty_one}")

    # 3. No repo with cat=0 (except 'tools')
    cat0 = [r["id"] for r in repos if r.get("cat") == 0 and r["id"] != "tools"]
    if not cat0:
        ok.append("Todos los repos tienen categoria asignada (excepto 'tools')")
    else:
        warnings.append(f"Repos con cat=0: {cat0}")

    # 4. REPOS.detail.json has choose_if, avoid_if, stack, desc in all repos
    detail = json.load(open(root / "ai_index" / "REPOS.detail.json", encoding="utf-8"))
    det_repos = detail.get("repos", [])
    no_choose = [r["id"] for r in det_repos if not r.get("choose_if") and r["id"] != "tools"]
    no_avoid = [r["id"] for r in det_repos if not r.get("avoid_if") and r["id"] != "tools"]
    no_stack = [r["id"] for r in det_repos if not r.get("stack") and r["id"] != "tools"]
    no_desc = [r["id"] for r in det_repos if not r.get("desc") or len(r.get("desc", "").strip()) < 20]
    no_desc = [r for r in no_desc if r != "tools"]
    if not no_choose:
        ok.append("Todos los repos tienen choose_if")
    else:
        warnings.append(f"Sin choose_if: {no_choose}")
    if not no_avoid:
        ok.append("Todos los repos tienen avoid_if")
    else:
        warnings.append(f"Sin avoid_if: {no_avoid}")
    if not no_stack:
        ok.append("Todos los repos tienen stack")
    else:
        warnings.append(f"Sin stack: {no_stack}")
    if not no_desc:
        ok.append("Todos los repos tienen desc")
    else:
        warnings.append(f"Sin desc: {no_desc}")

    # 5. data/extracted/MANIFEST.json covers all repos
    manifest_path = root / "data" / "extracted" / "MANIFEST.json"
    if manifest_path.exists():
        manifest = json.load(open(manifest_path, encoding="utf-8"))
        manifest_ids = {m["id"] for m in manifest}
        indice_ids = {r["id"] for r in repos}
        missing_from_manifest = indice_ids - manifest_ids
        if not missing_from_manifest:
            ok.append(f"MANIFEST.json cubre todos los {len(manifest)} repos")
        else:
            errors.append(f"MANIFEST.json no cubre: {missing_from_manifest}")
    else:
        errors.append("MANIFEST.json no existe")

    # 6. data/readmes_backup.zip exists
    backup = root / "data" / "readmes_backup.zip"
    if backup.exists() and backup.stat().st_size > 100000:
        size_mb = backup.stat().st_size / (1024 * 1024)
        ok.append(f"readmes_backup.zip existe ({size_mb:.1f} MB)")
    else:
        errors.append("readmes_backup.zip no existe o es demasiado pequeno")

    # 7. data/extracted/ has a folder for each repo
    extracted_dir = root / "data" / "extracted"
    extracted_dirs = {d.name for d in extracted_dir.iterdir() if d.is_dir()}
    missing_extracted = indice_ids - extracted_dirs
    if not missing_extracted:
        ok.append(f"data/extracted/ tiene {len(extracted_dirs)} carpetas")
    else:
        errors.append(f"Carpetas faltantes en data/extracted/: {missing_extracted}")

    # Report
    print("=" * 60)
    print("VERIFICACION DE EXTRACCION COMPLETA")
    print("=" * 60)
    print()
    if ok:
        print(f"OK ({len(ok)}):")
        for item in ok:
            print(f"  [OK] {item}")
    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for item in warnings:
            print(f"  [WARN] {item}")
    if errors:
        print(f"\nERRORES ({len(errors)}):")
        for item in errors:
            print(f"  [ERROR] {item}")

    print()
    if errors:
        print(f"RESULTADO: FALLA ({len(errors)} errores, {len(warnings)} warnings)")
        return 1
    elif warnings:
        print(f"RESULTADO: OK CON WARNINGS ({len(warnings)} warnings)")
        return 0
    else:
        print(f"RESULTADO: TODO OK ({len(ok)} checks verdes)")
        return 0


if __name__ == "__main__":
    sys.exit(main())
