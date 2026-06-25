from __future__ import annotations

"""
Curation / enrichment logic for making repo additions integral and complete.

When a new repo is discovered:
- analyze step uses runners (repomix, markitdown...) to produce artifacts in data/packed and data/extracted.
- enrich/draft step builds a rich profile and proposes full compact + detalle entries.

Heuristics + extracted content are used to fill:
- cat, role, exec, setup, tags, one, alt
- desc, stack, choose_if, avoid_if, combines, etc.

This makes "add repo -> full technical + theoretical ficha" automatic and high quality.
"""

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from repo_intelligence.core.io import read_json, read_yaml, write_json
from repo_intelligence.core.paths import ProjectPaths
from repo_intelligence.extract.manifests import detect_manifests, has_docker, infer_primary_language
from repo_intelligence.extract.readme import (
    extract_features,
    extract_install_hints,
    extract_intro_and_desc,
    guess_tech_stack,
    read_readme_text,
    short_summary,
)
from repo_intelligence.tools import gitnexus_runner, markitdown_runner, repomix_runner

# Strong keyword signals for category inference (extend as library grows)
CATEGORY_KEYWORDS: dict[int, list[str]] = {
    1: ["whatsapp", "evolution", "n8n", "chatwoot", "crm", "automation", "email", "notif", "mautic", "listmonk", "novu", "huginn", "activepieces"],
    2: ["skill", "prompt", "prompts", "awesome-agent", "karpathy", "context", "humanizer", "stop-slop", "marketingskills", "taste-skill", "ui-ux", "prompt-master"],
    3: ["agent", "framework", "orchestrat", "crew", "langchain", "langgraph", "dify", "flowise", "autogen", "ag2", "openhands", "deer", "gpt-researcher", "nemo-agent"],
    4: ["scrape", "crawl", "firecrawl", "crawl4ai", "playwright", "browser", "instaloader", "snscrape", "scrapy", "llm-scraper", "scrapegraph", "research", "archive"],
    5: ["mcp", "server", "public-apis", "connect", "neo4j"],
    6: ["mem0", "memory", "langfuse", "litellm", "observab", "loguru", "headroom", "sandbox", "agentmemory", "mempalace"],
    7: ["codegraph", "gitnexus", "graph", "repomix", "deepseek", "nanogpt", "how-to-train", "cosmos", "data-science", "awesome-bigdata", "openai-python", "llmc"],
    8: ["notebook", "odysseus", "ecc", "open-notebook", "workspace", "local-ai"],
    9: ["design", "ui", "frontend", "tailwind", "heroui", "shadcn", "penpot", "plasmic", "open-design", "gsap", "motion", "three", "magicui", "impeccable", "react-three"],
    10: ["analytics", "posthog", "metabase", "dash", "echarts", "uplot", "streamlit", "dataviz"],
    11: ["comfy", "stable-diffusion", "fooocus", "invoke", "diffusers", "controlnet", "gfpgan", "esrgan", "liveportrait", "deep-live", "face", "flux", "generative", "image", "vision"],
    12: ["whisper", "tts", "supertonic", "voxcpm", "moviepy", "remotion", "lossless", "opencut", "openscreen", "video", "audio", "voice", "hyperframes", "videofy"],
    13: ["markitdown", "ppt", "pdf", "reveal", "document", "present"],
}

ROLE_HINTS = {
    "platform": ["server", "full", "self-host", "docker-compose", "web app", "dashboard"],
    "runtime": ["engine", "runner", "core", "framework"],
    "library": ["sdk", "client", "python package", "lib", "npm package"],
    "skill": ["skill", "prompt pack", "template", "cheatsheet"],
    "directory": ["awesome", "list of", "curated", "collection"],
    "app": ["app", "desktop", "cli tool", "ui tool"],
}

EXEC_HINTS = {
    "local": ["local", "self host", "run locally", "uv run", "python -m"],
    "cloud": ["api", "hosted", "saas", "openai", "anthropic"],
    "hybrid": ["hybrid", "local or", "docker or api"],
}

SETUP_HINTS = {
    "easy": ["pip install", "npm i", "one command", "uv add"],
    "medium": ["docker", "config", "env", "compose"],
    "heavy": ["gpu", "large model", "whisper", "comfy", "training", "graphrag"],
}


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def _load_existing_indices(project_root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    compact = read_json(project_root / "INDICE_IA.json", {})
    detalle = read_json(project_root / "INDICE_IA.detalle.json", {})
    return compact, detalle


def get_new_repo_ids(project_root: Path | str) -> list[str]:
    """Return ids present in registry/scan but missing from curated INDICE."""
    root = Path(project_root)
    registry = read_yaml(root / "registry" / "repos.yaml", {"repos": []})
    compact = read_json(root / "INDICE_IA.json", {})
    curated = {r["id"] for r in compact.get("repos", [])}
    all_ids = [r.get("id") or _norm(r.get("name", "")) for r in registry.get("repos", [])]
    return [iid for iid in all_ids if iid and iid not in curated]


def ensure_analyzed(paths: ProjectPaths, repo_id: str, repo_path: Path, force: bool = False) -> dict[str, Any]:
    """Run heavy analysis tools for a repo. Returns paths to artifacts. Graceful on missing tools."""
    packed_dir = paths.packed_dir
    extracted_dir = paths.extracted_dir
    packed_dir.mkdir(parents=True, exist_ok=True)
    extracted_dir.mkdir(parents=True, exist_ok=True)

    packed_file = packed_dir / f"{repo_id}.xml"
    extracted_readme = extracted_dir / repo_id / "readme.md"
    extracted_readme.parent.mkdir(parents=True, exist_ok=True)

    results: dict[str, Any] = {
        "packed": str(packed_file),
        "readme_extracted": str(extracted_readme),
        "ran": [],
        "light_only": False,
    }

    from shutil import which
    has_repomix = which("repomix") is not None
    has_markit = which("markitdown") is not None

    # Repomix pack (code + structure overview) - skip if not present or not forced for speed
    if (has_repomix and (force or not packed_file.exists() or packed_file.stat().st_size < 200)):
        try:
            code = repomix_runner.pack_repo(repo_path, packed_file)
            results["ran"].append("repomix")
            results["repomix_code"] = code
        except Exception as e:
            results["repomix_error"] = str(e)
    else:
        results["light_only"] = True

    # Markitdown on the README
    readme = None
    from repo_intelligence.extract.readme import find_readme
    rm = find_readme(repo_path)
    if rm and has_markit:
        try:
            code = markitdown_runner.convert_to_markdown(rm, extracted_readme)
            results["ran"].append("markitdown")
            results["markitdown_code"] = code
            readme = extracted_readme
        except Exception as e:
            results["markitdown_error"] = str(e)
            readme = rm
    else:
        readme = rm
        if not has_markit:
            results["light_only"] = True

    # Gitnexus optional
    if which("gitnexus"):
        try:
            code = gitnexus_runner.analyze_repo(repo_path)
            results["ran"].append("gitnexus")
        except Exception:
            pass

    results["readme_source"] = str(readme) if readme else None
    return results


def _clean_text(t: str) -> str:
    t = re.sub(r"<[^>]+>", " ", t or "")
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:600]

def build_profile(repo_record: dict[str, Any], paths: ProjectPaths) -> dict[str, Any]:
    """Aggregate all available signals into a rich profile for drafting."""
    rid = repo_record.get("id") or _norm(repo_record.get("name", ""))
    repo_path = Path(repo_record.get("path", ""))

    readme_path = Path(repo_record["readme"]) if repo_record.get("readme") else None
    manifests = repo_record.get("manifests", []) or [str(p) for p in detect_manifests(repo_path)]

    # Prefer the full extracted README from data/extracted/ (no truncation) over the raw one
    extracted_readme = paths.extracted_dir / rid / "readme.md"
    if extracted_readme.exists():
        try:
            raw_readme = extracted_readme.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            raw_readme = read_readme_text(readme_path)
    else:
        raw_readme = read_readme_text(readme_path)
    intro = extract_intro_and_desc(raw_readme)
    features = extract_features(raw_readme)
    stack = guess_tech_stack(raw_readme, manifests)
    stack_lang = infer_primary_language(manifests)
    if stack_lang and stack_lang not in stack:
        stack.insert(0, stack_lang)
    if has_docker(manifests) and "docker" not in stack:
        stack.append("docker")

    install_hints = extract_install_hints(raw_readme)
    one = short_summary(readme_path) or _clean_text(intro.get("desc", ""))[:220]

    # Try to enrich with packed content if present
    packed = paths.packed_dir / f"{rid}.xml"
    packed_snippet = ""
    if packed.exists():
        try:
            packed_snippet = packed.read_text(encoding="utf-8", errors="ignore")[:6000]
        except Exception:
            pass

    # Basic remote url
    remotes = repo_record.get("remotes", [])
    repo_url = next((r for r in remotes if "github.com" in r), remotes[0] if remotes else "")

    return {
        "id": rid,
        "name": repo_record.get("name", rid),
        "path": str(repo_path),
        "repo_url": repo_url,
        "manifests": manifests,
        "intro": intro,
        "features": features,
        "stack": stack,
        "one": one,
        "install_hints": install_hints,
        "packed_snippet": packed_snippet,
        "raw_readme_head": raw_readme[:1500] if raw_readme else "",
    }


def infer_category(profile: dict[str, Any]) -> int | None:
    text = " ".join([
        profile.get("id", ""),
        profile.get("name", ""),
        profile.get("one", ""),
        profile.get("intro", {}).get("desc", ""),
        " ".join(profile.get("features", [])),
        " ".join(profile.get("stack", [])),
        profile.get("raw_readme_head", "")[:2000],
    ]).lower()

    scores: dict[int, int] = {}
    for cat, kws in CATEGORY_KEYWORDS.items():
        score = sum(1 for kw in kws if kw in text)
        if score > 0:
            scores[cat] = score
    if not scores:
        return None
    # prefer highest, tie-break lower numbers (more common cats first)
    return max(scores.items(), key=lambda x: (x[1], -x[0]))[0]


def infer_role_exec_setup(profile: dict[str, Any]) -> tuple[str, str, str]:
    text = " ".join([
        profile.get("id", ""), profile.get("name", ""), profile.get("one", ""),
        " ".join(profile.get("features", [])),
        profile.get("raw_readme_head", "")[:1500]
    ]).lower()
    stack = " ".join(profile.get("stack", [])).lower()
    manifests = " ".join(profile.get("manifests", "")).lower()

    role = "library"
    for r, hints in ROLE_HINTS.items():
        if any(h in text or h in stack for h in hints):
            role = r
            break
    if "awesome" in profile.get("id", "") or "list" in text:
        role = "directory"
    if any(k in text for k in ["skill", "prompt"]):
        role = "skill"

    exec_ = "local"
    for e, hints in EXEC_HINTS.items():
        if any(h in text for h in hints):
            exec_ = e
    if "api" in text or "hosted" in text:
        exec_ = "cloud" if exec_ == "local" else "hybrid"

    setup = "medium"
    for s, hints in SETUP_HINTS.items():
        if any(h in text or h in stack for h in hints):
            setup = s
    if "docker" in manifests or "docker" in stack:
        setup = "medium" if setup == "easy" else setup
    if profile.get("id") in {"repomix", "gitnexus", "markitdown"}:
        setup = "easy"

    return role, exec_, setup


def infer_tags(profile: dict[str, Any], cat: int | None) -> list[str]:
    tags: set[str] = set()
    text = (profile.get("one", "") + " " + " ".join(profile.get("stack", []))).lower()
    idn = profile.get("id", "").lower()

    base = ["automation"] if cat in (1, 3) else []
    if "mcp" in idn or "mcp" in text:
        tags.add("mcp")
    if any(x in text for x in ["agent", "orchestr"]):
        tags.add("agents")
    if any(x in text for x in ["image", "diffusion", "stable", "flux"]):
        tags.add("vision")
    if any(x in text for x in ["audio", "voice", "tts", "whisper", "video"]):
        tags.add("multimedia")
    if "scrap" in idn or "crawl" in text:
        tags.add("scraping")
    if "ui" in idn or "design" in text or "frontend" in text:
        tags.add("frontend")
    if "skill" in idn or "prompt" in text:
        tags.add("skills")
    tags.update(base)
    # from stack
    for s in profile.get("stack", []):
        tags.add(s.lower().replace("/", "-"))
    return sorted(list(tags))[:8]


def build_draft_entries(profile: dict[str, Any], existing_compact: dict[str, Any], existing_det: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    """Produce compact + detalle dicts ready for merge into INDICE files."""
    rid = profile["id"]
    cat = infer_category(profile) or 0
    role, exec_, setup = infer_role_exec_setup(profile)
    tags = infer_tags(profile, cat)
    one = profile.get("one", "")[:280]
    desc = _clean_text(profile.get("intro", {}).get("desc", one))[:520]
    stack_str = ", ".join(profile.get("stack", [])) or "See repo"

    # Simple combines: look at existing that share tags or cat (very rough)
    combines: list[str] = []
    for other_id, other in existing_det.items():
        if other_id == rid:
            continue
        ocat = other.get("cat")
        if ocat == cat and len(combines) < 3:
            combines.append(other_id)

    # choose/avoid templates (sanitized)
    raw_choose = profile.get("intro", {}).get("title", "") or profile.get("one", "") or "necesitas las capacidades que ofrece este repo"
    # strip obvious markdown/html
    clean = re.sub(r"<[^>]+>|```|\[.*?\]\(.*?\)|^\s*#{1,6}\s*", "", raw_choose).strip()
    if len(clean) < 8:
        clean = profile.get("one", "")[:80] or "las capacidades descritas en el proyecto"
    choose_if = f"quieres {clean[:90].lower()}"
    avoid_if = "ya tienes una herramienta equivalente o no encaja con tu stack actual"

    if cat == 5:
        choose_if = "necesitas exponer herramientas o contexto a agentes vía MCP"
        avoid_if = "prefieres conexiones directas sin protocolo estándar"
    if cat in (11, 12):
        avoid_if = "el caso no requiere generación multimedia o ya usas alternativas dedicadas"

    compact = {
        "id": rid,
        "name": profile.get("name", rid),
        "cat": cat,
        "role": role,
        "exec": exec_,
        "setup": setup,
        "mcp": "mcp" in tags,
        "prov": [],
        "tags": tags,
        "one": one,
        "alt": [],
        "doc": f"human/fichas/{rid}.md",
    }

    detalle = {
        "name": profile.get("name", rid),
        "cat": cat,
        "desc": desc,
        "stack": stack_str,
        "choose_if": choose_if,
        "avoid_if": avoid_if,
        "combines_with": combines[:4],
        "alternatives": [],
        "repo": profile.get("repo_url", ""),
        "doc": f"human/fichas/{rid}.md",
    }

    # Add review marker
    compact["_auto"] = True
    detalle["_auto"] = True
    detalle["_generated_at"] = datetime.now(timezone.utc).isoformat()

    return compact, detalle


def save_draft(project_root: Path, rid: str, compact: dict, detalle: dict, profile: dict) -> Path:
    drafts_dir = project_root / "data" / "drafts"
    drafts_dir.mkdir(parents=True, exist_ok=True)
    draft_path = drafts_dir / f"{rid}.json"
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "profile": {k: v for k, v in profile.items() if k not in ("raw_readme_head", "packed_snippet")},
        "compact": compact,
        "detalle": detalle,
    }
    write_json(draft_path, payload)
    return draft_path


def merge_into_indices(project_root: Path, rid: str, compact: dict[str, Any], detalle: dict[str, Any]) -> None:
    """Merge (or overwrite) the drafted entries into the canonical INDICE files.

    Preserves existing non-empty values when the new draft has empty ones
    (prevents regression on fields like 'one', 'desc', 'tags').
    """
    idx_path = project_root / "INDICE_IA.json"
    det_path = project_root / "INDICE_IA.detalle.json"

    idx = read_json(idx_path, {})
    det = read_json(det_path, {})

    # Find existing compact entry to preserve non-empty fields
    repos = idx.setdefault("repos", [])
    existing_compact = next((r for r in repos if r.get("id") == rid), {})

    clean_compact = {k: v for k, v in compact.items() if not k.startswith("_")}
    # Preserve existing non-empty values for key fields when new draft is empty
    for field in ("one", "tags", "alt", "prov"):
        new_val = clean_compact.get(field)
        old_val = existing_compact.get(field)
        if (not new_val or (isinstance(new_val, list) and not new_val)) and old_val:
            clean_compact[field] = old_val

    idx["repos"] = [r for r in repos if r.get("id") != rid]
    idx["repos"].append(clean_compact)

    det_repos = det.setdefault("repos", {})
    existing_det = det_repos.get(rid, {})
    clean_det = {k: v for k, v in detalle.items() if not k.startswith("_")}
    # Preserve existing non-empty values for key detail fields
    for field in ("desc", "choose_if", "avoid_if", "combines_with", "stack"):
        new_val = clean_det.get(field)
        old_val = existing_det.get(field)
        if (not new_val or (isinstance(new_val, list) and not new_val)) and old_val:
            clean_det[field] = old_val
    det_repos[rid] = clean_det

    # keep sorted-ish
    idx["repos"].sort(key=lambda r: (r.get("cat", 99), r.get("id", "")))

    write_json(idx_path, idx)
    write_json(det_path, det)


def run_enrich_for_new(
    project_root: Path,
    only_new: bool = True,
    auto_merge: bool = False,
    force_analyze: bool = False,
) -> dict[str, Any]:
    """High level entry: analyze + draft + optional merge for new repos."""
    paths = ProjectPaths.load(project_root)
    registry = read_yaml(paths.registry_file, {"repos": []})
    records = {r["id"]: r for r in registry.get("repos", [])}

    targets = get_new_repo_ids(project_root) if only_new else list(records.keys())

    compact_idx, det_idx = _load_existing_indices(project_root)

    results = {"analyzed": [], "drafted": [], "merged": []}

    for rid in targets:
        rec = records.get(rid)
        if not rec:
            continue
        repo_path = Path(rec["path"])

        # 1. analyze (heavy)
        analysis = ensure_analyzed(paths, rid, repo_path, force=force_analyze)
        results["analyzed"].append(rid)

        # 2. profile
        profile = build_profile(rec, paths)

        # 3. draft
        c_entry, d_entry = build_draft_entries(profile, compact_idx, det_idx.get("repos", {}))
        draft_path = save_draft(project_root, rid, c_entry, d_entry, profile)
        results["drafted"].append({"id": rid, "draft": str(draft_path)})

        # 4. optional merge (makes it part of curated immediately)
        if auto_merge:
            merge_into_indices(project_root, rid, c_entry, d_entry)
            results["merged"].append(rid)

    return results
