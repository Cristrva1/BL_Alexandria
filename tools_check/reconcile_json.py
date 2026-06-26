#!/usr/bin/env python3
"""Reconcilia INDICE_IA.detalle.json e INDICE_IA.json con el contenido enriquecido de guias/*.md.

Para cada ficha de repo en las guias, extrae:
  - 'Qué es' → desc (si el actual es ruidoso/inglés/roto)
  - 'Elige si' → choose_if (sin prefijo 'quieres ')
  - 'Evita si' → avoid_if
  - 'Combina con' → combines_with (lista de ids)
  - corrige cat si difiere

Uso: python tools_check/reconcile_json.py [--dry-run]
"""
from __future__ import annotations
import json, re, sys, io, pathlib

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
GUIDE_DIR = ROOT / "guias"
DETALLE = ROOT / "INDICE_IA.detalle.json"
COMPACT = ROOT / "INDICE_IA.json"

DRY = "--dry-run" in sys.argv


def parse_fichas(text: str) -> dict[str, dict]:
    """Extrae fichas de repo de un texto markdown. Retorna {repo_id: {fields}}."""
    fichas = {}
    # Split por headers ###
    lines = text.split("\n")
    blocks = []
    current_title = None
    current_lines = []
    for line in lines:
        if line.startswith("### ") and "Escaneo rápido" not in line and "¿Cuál elegir" not in line and "Leyenda de badges" not in line:
            if current_title is not None:
                blocks.append((current_title, "\n".join(current_lines)))
            current_title = line.replace("### ", "").strip()
            current_lines = []
        elif current_title is not None:
            current_lines.append(line)
    if current_title is not None:
        blocks.append((current_title, "\n".join(current_lines)))

    for title, block in blocks:
        if "**Repo:**" not in block:
            continue
        # Extract fields
        fields = {}
        # Qué es
        m = re.search(r"\*\*Qué es:\*\*\s*(.+?)(?=\n\*\*|\n###|\Z)", block, re.S)
        if m:
            fields["que_es"] = m.group(1).strip()
        # Elige si / Evita si (often on same line separated by —)
        m = re.search(r"\*\*Elige si:\*\*\s*(.+?)(?=\n\*\*|\n###|\Z)", block, re.S)
        if m:
            elige = m.group(1).strip()
            # Split on — if Evita si is inline
            if "— **Evita si:**" in elige:
                parts = elige.split("— **Evita si:**", 1)
                fields["elige_si"] = parts[0].strip()
                fields["evita_si"] = parts[1].strip()
            else:
                fields["elige_si"] = elige
        else:
            m2 = re.search(r"\*\*Elige si:\*\*\s*(.+)", block)
            if m2:
                fields["elige_si"] = m2.group(1).strip()
        # Evita si (separate line)
        if "evita_si" not in fields:
            m = re.search(r"\*\*Evita si:\*\*\s*(.+?)(?=\n\*\*|\n###|\Z)", block, re.S)
            if m:
                fields["evita_si"] = m.group(1).strip()
        # Combina con
        m = re.search(r"\*\*Combina con:\*\*\s*(.+?)(?=\n\*\*|\n###|\Z)", block, re.S)
        if m:
            combines_text = m.group(1).strip()
            # Extract repo ids from [text](#-anchor) links
            ids = re.findall(r"\[([^\]]+)\]\(#-[^)]+\)", combines_text)
            # Clean: remove "receta" references
            ids = [i.strip() for i in ids if "receta" not in i.lower()]
            fields["combines_with"] = ids
        # Repo URL
        m = re.search(r"\*\*Repo:\*\*\s*\[GitHub\]\(([^)]+)\)", block)
        if m:
            fields["repo_url"] = m.group(1).strip()

        # Generate repo_id from title (lowercase, hyphens, sin emoji)
        clean_title = re.sub(r"[^\w\s\.-]", "", title, flags=re.UNICODE).strip()
        rid = clean_title.lower().replace(" ", "-").replace("(", "").replace(")", "")
        # Normalize some known mappings
        fichas[rid] = {"title": title, **fields}

    return fichas


def normalize_id(rid: str) -> str:
    """Normalize repo id to match JSON keys."""
    rid = rid.lower().strip()
    # Known mappings
    mappings = {
        "ui-ux-pro-max-skill": "ui-ux-pro-max-skill",
        "taste-skill": "taste-skill",
        "skills-emil": "skills_emil",
        "skillspector": "skillspector",
        "openwa": "openwa",
        "whatsapp-agentkit": "whatsapp-agentkit",
        "twenty-main": "twenty-main",
        "context-engineering": "context-engineering",
        "agent-toolkit": "agent-toolkit",
        "n8n-skills": "n8n-skills",
        "n8n-io": "n8n_io",
        "n8n_io": "n8n_io",
        "deep-live-cam": "deep-live-cam",
        "face-recognition": "face_recognition",
        "open-generative-ai": "open-generative-ai",
        "real-esrgan": "real-esrgan",
        "sd-webui-controlnet": "sd-webui-controlnet",
        "comfyui-ipadapter-plus": "comfyui-ipadapter-plus",
        "comfyui_ipadapter_plus": "comfyui-ipadapter-plus",
        "react-three-fiber": "react-three-fiber",
        "ui-shadcn": "ui",
        "ui-(shadcn)": "ui",
        "data-science-ipython-notebooks": "data-science-ipython-notebooks",
        "how-to-train-your-gpt": "how-to-train-your-gpt",
        "deepseek-coder": "deepseek-coder",
        "gpt-researcher": "gpt-researcher",
        "llm-council": "llm-council",
        "awesome-langgraph": "awesome-langgraph",
        "notebooklm-py": "notebooklm-py",
        "notebooklm-mcp-cli": "notebooklm-mcp-cli",
        "open-notebook": "open-notebook",
        "youtube2webpage": "youtube2webpage",
        "videofy-minimal": "videofy_minimal",
        "videofy_minimal": "videofy-minimal",
        "face_recognition": "face-recognition",
        "face-recognition": "face-recognition",
        "n8n_io": "n8n-io",
        "n8n-io": "n8n-io",
        "nanoGPT": "nanogpt",
        "nanogpt": "nanogpt",
        "skills_emil": "skills-emil",
        "skills-emil": "skills-emil",
        "lossless-cut": "lossless-cut",
        "faster-whisper": "faster-whisper",
        "scrapegraph-ai": "scrapegraph-ai",
        "crawlee-python": "crawlee-python",
        "nemo-agent-toolkit": "nemo-agent-toolkit",
        "hermes-agent": "hermes-agent",
        "deer-flow": "deer-flow",
        "openevolve": "openevolve",
        "codegraph": "codegraph",
        "gitnexus": "gitnexus",
        "graphify": "graphify",
        "graphrag": "graphrag",
        "nanogpt": "nanogpt",
        "nanochat": "nanochat",
        "llm.c": "llm.c",
        "openai-python": "openai-python",
        "awesome-bigdata": "awesome-bigdata",
        "awesome-dataviz": "awesome-dataviz",
        "awesome-mcp-servers": "awesome-mcp-servers",
        "awesome-claude-code": "awesome-claude-code",
        "awesome-agent-skills": "awesome-agent-skills",
        "antigravity-awesome-skills": "antigravity-awesome-skills",
        "claude-plugins-official": "claude-plugins-official",
        "agents-towards-production": "agents-towards-production",
        "agency-agents": "agency-agents",
        "geo-seo-claude": "geo-seo-claude",
        "prompt-master": "prompt-master",
        "andrej-karpathy-skills": "andrej-karpathy-skills",
        "marketingskills": "marketingskills",
        "markitdown": "markitdown",
        "ppt-master": "ppt-master",
        "pdfcraft": "pdfcraft",
        "reveal.js": "reveal.js",
        "three.js": "three.js",
        "normalize.css": "normalize.css",
        "motion": "motion",
        "gsap": "gsap",
        "swr": "swr",
        "echarts": "echarts",
        "uplot": "uplot",
        "streamlit": "streamlit",
        "posthog": "posthog",
        "metabase": "metabase",
        "dash": "dash",
        "tailwindcss": "tailwindcss",
        "magicui": "magicui",
        "heroui": "heroui",
        "plasmic": "plasmic",
        "penpot": "penpot",
        "open-design": "open-design",
        "design.md": "design.md",
        "impeccable": "impeccable",
        "ecc": "ecc",
        "odysseus": "odysseus",
        "mem0": "mem0",
        "agentmemory": "agentmemory",
        "mempalace": "mempalace",
        "turbovec": "turbovec",
        "litellm": "litellm",
        "langfuse": "langfuse",
        "llmfit": "llmfit",
        "headroom": "headroom",
        "sandbox": "sandbox",
        "loguru": "loguru",
        "mcp": "mcp",
        "mcp-use": "mcp-use",
        "mcp-neo4j": "mcp-neo4j",
        "n8n-mcp": "n8n-mcp",
        "public-apis": "public-apis",
        "servers": "servers",
        "firecrawl": "firecrawl",
        "crawl4ai": "crawl4ai",
        "scrapy": "scrapy",
        "crawlee": "crawlee",
        "scrapling": "scrapling",
        "scrapely": "scrapely",
        "llm-scraper": "llm-scraper",
        "playwright": "playwright",
        "playwright-cli": "playwright-cli",
        "browser-use": "browser-use",
        "instaloader": "instaloader",
        "snscrape": "snscrape",
        "ag2": "ag2",
        "crewai": "crewai",
        "langchain": "langchain",
        "langflow": "langflow",
        "dify": "dify",
        "flowise": "flowise",
        "openhands": "openhands",
        "ruflo": "ruflo",
        "multica": "multica",
        "mirofish": "mirofish",
        "evolution-api": "evolution-api",
        "activepieces": "activepieces",
        "n8n": "n8n",
        "huginn": "huginn",
        "mautic": "mautic",
        "chatwoot": "chatwoot",
        "listmonk": "listmonk",
        "novu": "novu",
        "invokeai": "invokeai",
        "diffusers": "diffusers",
        "controlnet": "controlnet",
        "gfpgan": "gfpgan",
        "liveportrait": "liveportrait",
        "fluxer": "fluxer",
        "comfyui": "comfyui",
        "stable-diffusion-webui": "stable-diffusion-webui",
        "fooocus": "fooocus",
        "whisper": "whisper",
        "whisperx": "whisperx",
        "supertonic": "supertonic",
        "voxcpm": "voxcpm",
        "tts": "tts",
        "omnivoice-studio": "omnivoice-studio",
        "moviepy": "moviepy",
        "remotion": "remotion",
        "opencut": "opencut",
        "openscreen": "openscreen",
        "hyperframes": "hyperframes",
        "cosmos": "cosmos",
    }
    return mappings.get(rid, rid)


def main() -> int:
    # Parse all fichas from guias
    all_fichas = {}
    for f in sorted(GUIDE_DIR.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        fichas = parse_fichas(text)
        for rid, data in fichas.items():
            nid = normalize_id(rid)
            all_fichas[nid] = data

    print(f"Fichas parsed from guias: {len(all_fichas)}")

    # Load JSON
    detalle = json.loads(DETALLE.read_text(encoding="utf-8"))
    compact = json.loads(COMPACT.read_text(encoding="utf-8"))

    changes = 0
    matched = 0

    for rid, ficha in all_fichas.items():
        if rid not in detalle["repos"]:
            continue
        matched += 1
        r = detalle["repos"][rid]
        changed = False

        # Fix choose_if if broken
        old_cif = r.get("choose_if", "")
        if "elige_si" in ficha:
            new_cif = ficha["elige_si"]
            # Remove trailing — or extra text
            new_cif = new_cif.split("—")[0].strip() if "—" in new_cif and "Evita" not in new_cif else new_cif
            if old_cif.startswith("quieres ") or "---" in old_cif or old_cif != new_cif:
                if old_cif != new_cif and new_cif:
                    r["choose_if"] = new_cif
                    changed = True

        # Fix avoid_if if generic
        old_aif = r.get("avoid_if", "")
        if "evita_si" in ficha:
            new_aif = ficha["evita_si"]
            if old_aif == "ya tienes una herramienta equivalente o no encaja con tu stack actual" or old_aif != new_aif:
                if old_aif != new_aif and new_aif:
                    r["avoid_if"] = new_aif
                    changed = True

        # Fix combines_with if empty or different
        if "combines_with" in ficha and ficha["combines_with"]:
            new_cw = [normalize_id(c) for c in ficha["combines_with"]]
            old_cw = r.get("combines_with", [])
            if not old_cw or set(new_cw) - set(old_cw):
                r["combines_with"] = new_cw
                changed = True

        # Fix repo URL if empty
        if not r.get("repo", "") and "repo_url" in ficha:
            r["repo"] = ficha["repo_url"]
            changed = True

        # Fix cat for openwa
        if rid == "openwa" and r.get("cat") != 1:
            r["cat"] = 1
            changed = True

        if changed:
            changes += 1

    print(f"Matched to JSON: {matched}")
    print(f"Repos changed: {changes}")

    if DRY:
        print("\n[DRY RUN] No changes written.")
        return 0

    DETALLE.write_text(json.dumps(detalle, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"INDICE_IA.detalle.json updated.")

    # Update compact index 'one' field for repos whose desc changed
    compact_repos = compact.get("repos", [])
    if isinstance(compact_repos, list):
        for cr in compact_repos:
            rid = cr.get("id", "")
            if rid in detalle["repos"]:
                dr = detalle["repos"][rid]
                # Update 'one' if it was empty or very short
                one = cr.get("one", "")
                if not one or len(one) < 15:
                    desc = dr.get("desc", "")
                    if desc:
                        cr["one"] = desc[:120]
                # Fix cat
                if rid == "openwa":
                    cr["cat"] = 1
        COMPACT.write_text(json.dumps(compact, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"INDICE_IA.json updated.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
