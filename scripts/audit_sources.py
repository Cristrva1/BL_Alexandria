"""Cache primary README evidence for editorial review without installing repositories.

Run from the hub with ``uv run python scripts/audit_sources.py``. This does not
promote keyword matches to verified pricing or subscription compatibility.
"""
from __future__ import annotations

import argparse
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess


def collect(root: Path, repo: dict, refresh: bool = False) -> dict:
    folder = root / "data" / "extracted" / repo["id"]
    folder.mkdir(parents=True, exist_ok=True)
    cache = folder / "access-review.json"
    if cache.exists() and not refresh:
        return json.loads(cache.read_text(encoding="utf-8"))
    result = subprocess.run(
        ["gh", "api", f"repos/{repo['gh']}/readme"],
        capture_output=True, encoding="utf-8", timeout=60, check=False,
    )
    now = datetime.now(timezone.utc).isoformat()
    if result.returncode:
        record = {"id": repo["id"], "gh": repo["gh"], "checked_at": now,
                  "error": result.stderr.strip(), "evidence": []}
    else:
        data = json.loads(result.stdout)
        text = base64.b64decode(data.get("content") or "").decode("utf-8", errors="replace")
        (folder / "readme.md").write_text(text, encoding="utf-8")
        lines = text.splitlines()
        pattern = re.compile(r"api[ _-]?key|subscription|oauth|claude code|codex|ollama|localhost:11434|llama\.cpp|billing|pricing|pip install|npm install|npx |docker compose|cuda|vram", re.I)
        evidence = []
        for index, line in enumerate(lines):
            if pattern.search(line) and len(line) < 1800:
                evidence.append({"line": index + 1, "text": "\n".join(lines[max(0, index-1):index+2])[:1400]})
        record = {"id": repo["id"], "gh": repo["gh"], "checked_at": now,
                  "url": data.get("html_url"), "blob_sha": data.get("sha"),
                  "path": data.get("path"), "evidence": evidence, "error": None}
    cache.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--id", action="append", dest="ids")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    compact = json.loads((root / "INDICE_IA.json").read_text(encoding="utf-8"))
    repos = [r for r in compact["repos"] if r.get("gh") and not r.get("alias_of") and r.get("repository_host", "github") == "github"]
    if args.ids:
        unknown = set(args.ids) - {r["id"] for r in repos}
        if unknown:
            parser.error("Unknown public repository ids: " + ", ".join(sorted(unknown)))
        repos = [r for r in repos if r["id"] in args.ids]
    records = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(collect, root, repo, args.refresh): repo["id"] for repo in repos}
        for future in as_completed(futures):
            try:
                records.append(future.result())
            except Exception as exc:
                records.append({"id": futures[future], "error": str(exc), "evidence": []})
            if len(records) % 40 == 0:
                print(f"Reviewed sources: {len(records)}/{len(repos)}", flush=True)
    output = root / "data" / "reports" / "access-source-audit.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    previous = json.loads(output.read_text(encoding="utf-8")) if args.ids and output.exists() else []
    by_id = {record["id"]: record for record in previous}
    by_id.update({record["id"]: record for record in records})
    output.write_text(json.dumps(sorted(by_id.values(), key=lambda r: r["id"]), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    failures = [r["id"] for r in records if r.get("error")]
    print(f"Sources cached: {len(records)}; unavailable: {failures}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
