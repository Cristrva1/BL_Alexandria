"""Extract GitHub references from a saved DOCX and prepare a read-only source audit.

The document stays local. Review and curate the resulting candidates before
editing the canonical indices; a shared name is never enough to merge projects.
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
from urllib.parse import unquote, urlparse
from xml.etree import ElementTree as ET
from zipfile import ZipFile

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}


def repository_name(url: str) -> str | None:
    parsed = urlparse(url)
    if parsed.scheme not in {"https", "http"} or parsed.hostname not in {"github.com", "www.github.com"}:
        return None
    parts = unquote(parsed.path).strip("/").split("/")
    if len(parts) < 2 or parts[0].lower() in {"topics", "collections", "settings", "search", "orgs", "marketplace"}:
        return None
    owner, name = parts[:2]
    name = name.removesuffix(".git").rstrip(".,;:")
    if not re.fullmatch(r"[A-Za-z0-9_-]+", owner) or not re.fullmatch(r"[A-Za-z0-9_.-]+", name):
        return None
    return owner + "/" + name


def extract_docx(path: Path) -> dict:
    with ZipFile(path) as archive:
        links = []
        for filename in archive.namelist():
            if filename.endswith(".rels"):
                links += [node.get("Target", "") for node in ET.fromstring(archive.read(filename))]
        rels = {node.get("Id"): node.get("Target", "") for node in ET.fromstring(archive.read("word/_rels/document.xml.rels"))}
        body = ET.fromstring(archive.read("word/document.xml")).find("w:body", NS)
    def text(element):
        return "".join(node.text or "" for node in element.iter("{" + NS["w"] + "}t"))
    # Word stores some URLs as ordinary text, outside relationship targets.
    paragraphs = "\n".join(text(paragraph) for paragraph in body.iter("{" + NS["w"] + "}p"))
    links += re.findall(r"https?://(?:www\.)?github\.com/[^\s<>\"'()[\]]+", paragraphs, re.I)
    directory, unresolved = [], []
    active, category = False, ""
    for element in body:
        value = text(element)
        if element.tag.endswith("}p"):
            if value == "Directorio de repositorios": active = True
            elif value == "Biblioteca de prompts": active = False
            elif active and value.startswith("Repositorios:"): category = value
        elif active and element.tag.endswith("}tbl"):
            for row in element.findall("w:tr", NS)[1:]:
                targets = [rels.get(link.get("{" + NS["r"] + "}id"), "") for link in row.findall(".//w:hyperlink", NS)]
                names = sorted({name for target in targets if (name := repository_name(target))})
                cells = [text(cell) for cell in row.findall("w:tc", NS)]
                record = {"category": category, "names": names, "cells": cells}
                (directory if names else unresolved).append(record)
    names = {}
    for link in links:
        name = repository_name(link)
        if name: names.setdefault(name.lower(), name)
    return {"repositories": sorted(names.values(), key=str.casefold), "directory": directory, "unresolved": unresolved}


def github(path: str) -> dict:
    result = subprocess.run(["gh", "api", path], capture_output=True, text=True, encoding="utf-8", timeout=60)
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    return json.loads(result.stdout)


def inspect_repository(name: str, known_ids: dict, folder: Path) -> dict:
    cache = folder / (name.replace("/", "--") + ".json")
    if cache.exists(): return json.loads(cache.read_text(encoding="utf-8"))
    result = {"requested": name, "checked_at": datetime.now(timezone.utc).isoformat()}
    try:
        metadata = github("repos/" + name)
        result["metadata"] = metadata
        if metadata.get("private"):
            result["status"] = "private"
        elif str(metadata["id"]) in known_ids:
            result.update(status="existing", catalog_id=known_ids[str(metadata["id"])])
        else:
            result["status"] = "new"
            try: result["readme"] = github("repos/" + metadata["full_name"] + "/readme")
            except RuntimeError as error: result["readme_error"] = str(error)
            result["tree"] = github("repos/" + metadata["full_name"] + "/git/trees/" + metadata["default_branch"])
    except Exception as error:
        result.update(status="unavailable", error=str(error))
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path)
    parser.add_argument("--output", type=Path, default=Path("data/reports/document-import-20261114"))
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument("--verified-reference", action="append", default=[], help="Additional repository resolved from an unlinked named resource")
    args = parser.parse_args()
    extracted = extract_docx(args.document)
    extracted["repositories"] = sorted(set(extracted["repositories"] + args.verified_reference), key=str.casefold)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "source-extraction.json").write_text(json.dumps(extracted, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"References: {len(extracted['repositories'])}; directory rows with links: {len(extracted['directory'])}; unresolved rows: {len(extracted['unresolved'])}", flush=True)
    if not args.fetch: return
    compact = json.loads(Path("INDICE_IA.json").read_text(encoding="utf-8"))
    known = {str(repo["github_id"]): repo["id"] for repo in compact["repos"] if repo.get("github_id") and not repo.get("alias_of")}
    records = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(inspect_repository, name, known, args.output / "github") for name in extracted["repositories"]]
        for future in as_completed(futures):
            records.append(future.result())
            if len(records) % 20 == 0: print(f"Verified: {len(records)}/{len(futures)}", flush=True)
    records.sort(key=lambda row: row["requested"].lower())
    (args.output / "repositories.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from collections import Counter
    print(dict(Counter(row["status"] for row in records)))
    for row in records:
        if row["status"] == "unavailable": print(row["requested"], row["error"])


if __name__ == "__main__": main()
