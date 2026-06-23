from __future__ import annotations

import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from repo_intelligence.core.io import read_json, write_json


TAG_SYNONYMS = {
    "whatsapp": {"whatsapp", "wa", "mensajeria", "mensaje", "chat"},
    "automation": {"automatizacion", "automation", "workflow", "flujo", "n8n", "zapier", "crm"},
    "agents": {"agente", "agentes", "agent", "agents", "multiagente"},
    "mcp": {"mcp", "model context protocol", "servidor mcp", "herramientas"},
    "scraping": {"scraping", "scraper", "crawler", "crawl", "extraer", "web", "research"},
    "research": {"research", "investigacion", "buscar", "citar", "informe"},
    "llmops": {"llmops", "observabilidad", "trazas", "costos", "evaluacion"},
    "memory": {"memoria", "memory", "persistencia"},
    "ui": {"ui", "frontend", "web app", "interfaz", "diseño", "diseno", "react"},
    "dataviz": {"dashboard", "grafica", "graficos", "analytics", "analitica", "bi", "metricas"},
    "image": {"imagen", "image", "foto", "generacion visual", "vision"},
    "audio": {"audio", "voz", "voice", "tts", "stt", "transcripcion"},
    "video": {"video", "reels", "shorts", "subtitulos", "edicion"},
    "docs": {"documento", "documentos", "pdf", "ppt", "presentacion", "markdown"},
    "code": {"codigo", "code", "repos", "repositorio", "analizar codigo"},
    "local": {"local", "privado", "offline", "self-host", "soberano"},
    "email": {"email", "correo", "newsletter"},
    "notifications": {"notificaciones", "notification", "push"},
}

STOPWORDS = {
    "quiero",
    "crear",
    "para",
    "con",
    "sin",
    "que",
    "una",
    "uno",
    "unos",
    "unas",
    "este",
    "esta",
    "estos",
    "estas",
    "hacer",
    "sistema",
    "proyecto",
    "app",
    "aplicacion",
    "herramienta",
    "necesito",
    "usar",
    "tener",
}

DOMAIN_BOOSTS = {
    "whatsapp": {
        "keywords": {"whatsapp", "clientes", "leads", "humano", "mensajes", "soporte", "ventas"},
        "repos": {
            "evolution-api": 16,
            "n8n": 12,
            "chatwoot": 10,
            "whatsapp-agentkit": 10,
            "n8n-mcp": 8,
            "n8n-skills": 8,
            "novu": 5,
            "openwa": 5,
        },
    },
    "mcp": {
        "keywords": {"mcp", "model", "context", "protocol", "servidor", "herramientas", "conectar"},
        "repos": {"mcp": 14, "servers": 12, "mcp-use": 10, "awesome-mcp-servers": 8, "github-mcp-server": 7, "n8n-mcp": 6},
    },
    "research": {
        "keywords": {"research", "investigacion", "buscar", "citar", "informe", "web"},
        "repos": {"gpt-researcher": 14, "deer-flow": 10, "crawl4ai": 9, "firecrawl": 7, "browser-use": 6, "markitdown": 5},
    },
    "video": {
        "keywords": {"reels", "shorts", "video", "subtitulos", "voz", "transcripcion"},
        "repos": {"whisperx": 12, "supertonic": 10, "tts": 8, "moviepy": 8, "remotion": 8, "lossless-cut": 6},
    },
    "frontend": {
        "keywords": {"frontend", "interfaz", "ui", "dashboard", "react", "web", "graficas"},
        "repos": {"tailwindcss": 10, "heroui": 9, "swr": 8, "echarts": 8, "uplot": 7, "taste-skill": 7, "threejs": 6},
    },
    "marketing": {
        "keywords": {"marketing", "campanas", "ads", "seo", "growth", "newsletter", "email"},
        "repos": {"marketingskills": 12, "agency-agents": 10, "mautic": 8, "listmonk": 8, "posthog": 7, "metabase": 7},
    },
    "documents": {
        "keywords": {"documentos", "pdf", "word", "ppt", "presentacion", "markdown"},
        "repos": {"markitdown": 12, "ppt-master": 9, "revealjs": 7, "pdfcraft": 6},
    },
}

BUILD_TOOL_REPOS = {
    "claude-code": {
        "claude-plugins-official": 10,
        "awesome-claude-code": 10,
        "superpowers": 9,
        "skills": 8,
        "agent-toolkit": 8,
        "n8n-skills": 7,
        "geo-seo-claude": 7,
        "agency-agents": 7,
    },
    "codex": {
        "awesome-agent-skills": 10,
        "antigravity-awesome-skills": 8,
        "marketingskills": 7,
        "taste-skill": 7,
    },
    "antigravity": {
        "antigravity-awesome-skills": 10,
        "awesome-agent-skills": 8,
        "prompt-master": 6,
    },
    "grok-build": {},
    "grok": {},
    "open-code": {
        "awesome-agent-skills": 8,
        "antigravity-awesome-skills": 7,
        "prompt-master": 6,
    },
    "opencode": {
        "awesome-agent-skills": 8,
        "antigravity-awesome-skills": 7,
        "prompt-master": 6,
    },
}


INSTALL_HINTS = {
    "global": "Instalar globalmente si se usara desde muchas carpetas.",
    "local_project": "Instalar dentro del proyecto con uv/npm/pnpm segun stack.",
    "docker_local": "Preparar en infra/ y levantar solo cuando el flujo lo necesite.",
    "reference_only": "Leer/copiar ideas; no instalar como dependencia inicial.",
    "deferred": "Diferir hasta que sea finalista claro o exista necesidad fuerte.",
}


def recommend(project_root: Path, project: str, max_repos: int = 5, build_tool: str = "codex") -> dict[str, Any]:
    scan = read_json(project_root / "ai_index" / "REPOS.scan.json", {"repos": []})
    detail = read_json(project_root / "ai_index" / "REPOS.detail.json", {"repos": []})
    winners = read_json(project_root / "ai_index" / "WINNERS.json", {})
    detail_by_id = {item["id"]: item for item in detail.get("repos", [])}

    scored = []
    for repo in scan.get("repos", []):
        score, reasons = score_repo(project, repo, detail_by_id.get(repo["id"], {}), build_tool=build_tool)
        if score <= 0:
            continue
        enriched = {**repo, **detail_by_id.get(repo["id"], {})}
        enriched["score"] = score
        enriched["reasons"] = reasons
        enriched["install_mode"] = _install_mode(enriched)
        enriched["install_hint"] = INSTALL_HINTS.get(enriched["install_mode"], "")
        scored.append(enriched)

    scored.sort(key=lambda item: (item["score"], _mode_priority(item["install_mode"])), reverse=True)
    selected = _dedupe_alternatives(scored, max_repos)

    global_tools = _global_tools_for_project(selected, winners)
    local_project = [item for item in selected if item["install_mode"] == "local_project"]
    docker_local = [item for item in selected if item["install_mode"] == "docker_local"]
    reference_only = [item for item in selected if item["install_mode"] == "reference_only"]
    deferred = [item for item in selected if item["install_mode"] == "deferred"]

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project": project,
        "build_tool": build_tool,
        "read_first_for_any_ai": [
            "ai_index/WINNERS.json",
            "ai_index/ROUTER.json",
            "ai_index/REPOS.scan.json",
            "ai_index/REPOS.detail.json only for finalists",
            "human/fichas/<repo>.md only for chosen finalists",
        ],
        "global_tools": global_tools,
        "recommended_repos": selected,
        "local_project": local_project,
        "docker_local": docker_local,
        "reference_only": reference_only,
        "deferred": deferred,
        "avoid_by_default": _avoid_by_default(winners),
    }

    safe_name = _slug(project)[:80] or "project"
    write_json(project_root / "data" / "decisions" / f"{safe_name}.json", result)
    write_context_pack(project_root, result)
    return result


def write_context_pack(project_root: Path, result: dict[str, Any]) -> Path:
    lines = [
        "# Context Pack Para IA",
        "",
        f"Generado: {result['generated_at']}",
        "",
        "## Proyecto",
        "",
        result["project"],
        "",
        "## Herramienta con la que se construira",
        "",
        result.get("build_tool", "codex"),
        "",
        "## Indices que cualquier IA debe leer primero",
        "",
    ]
    lines.extend(f"- `{path}`" for path in result["read_first_for_any_ai"])
    lines.extend(["", "## Herramientas globales sugeridas", ""])
    for tool in result["global_tools"]:
        lines.append(f"- `{tool['id']}`: {tool['reason']}")
    lines.extend(["", "## Orden recomendado de instalacion", ""])
    lines.extend(
        [
            "1. Instalar/verificar herramientas globales.",
            "2. Crear la carpeta del proyecto real.",
            "3. Instalar dependencias `local_project` dentro de ese proyecto.",
            "4. Preparar servicios `docker_local` en `infra/`, sin levantarlos hasta que el flujo lo necesite.",
            "5. Leer/copiar solo lo necesario de `reference_only`.",
            "6. Dejar `deferred` fuera de la primera version.",
            "",
            "### Global",
        ]
    )
    for tool in result["global_tools"]:
        lines.append(f"- `{tool['id']}`")
    lines.extend(["", "### Local del proyecto", ""])
    _append_install_group(lines, result["local_project"])
    lines.extend(["", "### Docker local", ""])
    _append_install_group(lines, result["docker_local"])
    lines.extend(["", "### Solo referencia", ""])
    _append_install_group(lines, result["reference_only"])
    lines.extend(["", "### Diferir", ""])
    _append_install_group(lines, result["deferred"])
    lines.extend(["", "## Repos recomendados", ""])
    for repo in result["recommended_repos"]:
        lines.extend(
            [
                f"### {repo['name']}",
                "",
                f"- id: `{repo['id']}`",
                f"- score: `{repo['score']}`",
                f"- instalacion: `{repo['install_mode']}`",
                f"- ruta local: `{repo.get('path', '')}`",
                f"- motivo: {', '.join(repo.get('reasons', []))}",
                f"- resumen: {repo.get('desc') or repo.get('one') or ''}",
                f"- combinar con: {', '.join(repo.get('combines_with', [])) or 'ninguno declarado'}",
                f"- alternativas: {', '.join(repo.get('alternatives') or repo.get('alt', [])) or 'ninguna declarada'}",
                "",
            ]
        )
    lines.extend(["## No instalar por defecto", ""])
    for item in result["avoid_by_default"]:
        lines.append(f"- `{item}`")

    output = project_root / "ai_index" / "CONTEXT_PACKS" / "latest.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output


def _append_install_group(lines: list[str], repos: list[dict[str, Any]]) -> None:
    if not repos:
        lines.append("- Ninguno.")
        return
    for repo in repos:
        lines.append(f"- `{repo['id']}`: {repo.get('install_hint', '')} Ruta: `{repo.get('path', '')}`")


def score_repo(project: str, repo: dict[str, Any], detail: dict[str, Any], build_tool: str = "codex") -> tuple[int, list[str]]:
    text = _norm_text(project)
    haystack = _norm_text(
        " ".join(
            [
                repo.get("id", ""),
                repo.get("name", ""),
                repo.get("role") or "",
                repo.get("one") or "",
                " ".join(repo.get("tags", [])),
                detail.get("desc") or "",
                detail.get("choose_if") or "",
                detail.get("stack") or "",
            ]
        )
    )
    score = 0
    reasons: list[str] = []

    project_tokens = set(_tokens(text))
    repo_tokens = set(_tokens(haystack))
    overlap = project_tokens & repo_tokens
    if overlap:
        points = min(len(overlap), 8)
        score += points
        reasons.append(f"coincide en palabras clave: {', '.join(sorted(list(overlap))[:5])}")

    for tag in repo.get("tags", []):
        synonyms = TAG_SYNONYMS.get(tag, {tag})
        if any(_has_phrase(text, _norm_text(word)) for word in synonyms):
            score += 8
            reasons.append(f"tag relevante: {tag}")

    if repo.get("role") in {"skill", "directory"} and any(word in text for word in ["codex", "claude", "antigravity", "skill", "skills"]):
        score += 5
        reasons.append("util para agente/IDE")

    if repo.get("mcp") or "mcp" in repo.get("tags", []) or "mcp" in haystack:
        if "mcp" in text:
            score += 8
            reasons.append("relacionado con MCP")

    tool_boost = BUILD_TOOL_REPOS.get(_norm_tool(build_tool), {}).get(repo.get("id", ""), 0)
    if tool_boost:
        score += tool_boost
        reasons.append(f"encaja con herramienta de construccion: {build_tool} (+{tool_boost})")

    domain_score = _domain_boost(text, repo.get("id", ""))
    if domain_score:
        score += domain_score
        reasons.append(f"encaja con receta de dominio (+{domain_score})")

    install_mode = _install_mode(repo)
    if install_mode == "deferred":
        score -= 4
    elif install_mode in {"local_project", "global"}:
        score += 2

    return score, reasons


def _dedupe_alternatives(scored: list[dict[str, Any]], max_repos: int) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    blocked: set[str] = set()
    for repo in scored:
        repo_id = repo["id"]
        if _norm_id(repo_id) in blocked:
            continue
        selected.append(repo)
        for alt in repo.get("alt", []) + repo.get("alternatives", []):
            blocked.add(_norm_id(alt))
        if len(selected) >= max_repos:
            break
    return selected


def _global_tools_for_project(selected: list[dict[str, Any]], winners: dict[str, Any]) -> list[dict[str, str]]:
    tools = [
        {"id": "git", "reason": "actualizar y versionar repos"},
        {"id": "gh", "reason": "metadata de GitHub cuando haga falta"},
        {"id": "uv", "reason": "entorno Python local reproducible"},
        {"id": "pnpm", "reason": "proyectos Node/TypeScript"},
    ]
    selected_ids = {item["id"] for item in selected}
    if {"repomix", "gitnexus"} & selected_ids or "repo_structure_analysis" in winners:
        tools.extend(
            [
                {"id": "repomix", "reason": "empaquetar contexto amplio de finalistas"},
                {"id": "gitnexus", "reason": "analisis estructural de repos grandes"},
            ]
        )
    if "markitdown" in selected_ids:
        tools.append({"id": "markitdown", "reason": "conversion de documentos a Markdown"})
    if any(item.get("setup") == "heavy" or item["install_mode"] == "docker_local" for item in selected):
        tools.append({"id": "docker", "reason": "servicios pesados aislados"})
    return _unique_tools(tools)


def _avoid_by_default(winners: dict[str, Any]) -> list[str]:
    avoid: list[str] = []
    for value in winners.values():
        if isinstance(value, dict):
            avoid.extend(value.get("avoid_now", []))
            avoid.extend(value.get("defer", []))
    return sorted(set(avoid))


def _install_mode(repo: dict[str, Any]) -> str:
    repo_id = repo.get("id", "")
    role = repo.get("role")
    if repo_id in {"repomix", "gitnexus"}:
        return "global"
    if repo_id in {"markitdown", "crawl4ai"}:
        return "local_project"
    if repo_id in {"n8n", "langfuse", "evolution-api", "chatwoot", "novu", "mautic", "listmonk", "posthog", "metabase"}:
        return "docker_local"
    if repo_id in {"litellm"}:
        return "local_project"
    if role in {"skill", "directory"}:
        return "reference_only"
    if repo.get("setup") == "heavy":
        return "deferred"
    return repo.get("install_mode") or "reference_only"


def _mode_priority(mode: str) -> int:
    return {"local_project": 5, "global": 4, "docker_local": 3, "reference_only": 2, "deferred": 1}.get(mode, 0)


def _unique_tools(tools: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[str] = set()
    result: list[dict[str, str]] = []
    for tool in tools:
        if tool["id"] in seen:
            continue
        seen.add(tool["id"])
        result.append(tool)
    return result


def _tokens(text: str) -> list[str]:
    return [
        token
        for token in re.findall(r"[a-z0-9áéíóúñü]+", text.lower())
        if len(token) >= 4 and _norm_text(token) not in STOPWORDS
    ]


def _norm_text(value: str) -> str:
    return (
        value.lower()
        .replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("ñ", "n")
        .replace("ü", "u")
    )


def _norm_id(value: str) -> str:
    return value.lower().replace("_", "-").replace(".", "-")


def _slug(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")


def _norm_tool(value: str) -> str:
    return value.lower().strip().replace("_", "-").replace(" ", "-")


def _has_phrase(text: str, phrase: str) -> bool:
    if not phrase:
        return False
    if " " in phrase:
        return phrase in text
    return bool(re.search(rf"\b{re.escape(phrase)}\b", text))


def _domain_boost(text: str, repo_id: str) -> int:
    tokens = set(_tokens(text))
    boost = 0
    for domain in DOMAIN_BOOSTS.values():
        if tokens & {_norm_text(keyword) for keyword in domain["keywords"]}:
            boost += domain["repos"].get(repo_id, 0)
    return boost
