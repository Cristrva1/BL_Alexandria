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
    "code": {"codigo", "repositorio", "analizar codigo", "codebase"},
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
    "uso",
    "code",
    "claude",
    "diario",
    "diaria",
    "optimizar",
    "ultralizar",
    "ultra",
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

INTENT_BOOSTS = {
    "agent_ide_optimization": {
        "superpowers": 30,
        "agent-toolkit": 27,
        "claude-plugins-official": 25,
        "awesome-claude-code": 24,
        "skillspector": 18,
        "context-engineering": 16,
        "prompt-master": 14,
        "awesome-agent-skills": 10,
        "antigravity-awesome-skills": 6,
    },
    "claude_code_daily": {
        "superpowers": 24,
        "agent-toolkit": 24,
        "claude-plugins-official": 22,
        "awesome-claude-code": 22,
        "skillspector": 16,
        "context-engineering": 12,
        "prompt-master": 10,
        "n8n-skills": 4,
        "geo-seo-claude": 3,
        "agency-agents": 3,
    },
}


CONDITIONAL_SKILLS = {
    "n8n-skills": {"n8n", "automatizacion", "automation", "workflow", "flujos"},
    "geo-seo-claude": {"seo", "geo", "search", "busqueda", "marketing", "contenido"},
    "agency-agents": {"agencia", "agency", "clientes", "marketing", "ventas"},
    "marketingskills": {"marketing", "copy", "seo", "ads", "growth", "campanas"},
    "taste-skill": {"frontend", "ui", "interfaz", "diseño", "diseno", "react", "web"},
}


REPO_GUIDANCE = {
    "superpowers": {
        "stack_role": "Base metodologica para trabajar todos los dias con agentes.",
        "why": "Conviene cuando el objetivo es mejorar el flujo completo de Claude Code: no es una skill suelta, sino una forma de obligar al agente a usar instrucciones, habilidades y pasos de trabajo reutilizables.",
        "how": "Funciona como una capa de instrucciones y skills composables. El valor esta en adoptar el metodo y copiar/activar solo las piezas que cambian tu rutina: planificacion, ejecucion, revision y memoria de decisiones.",
        "install": [
            "Revisar el repositorio local y sus carpetas `.claude-plugin`, `.codex-plugin`, `skills`, `hooks` y `scripts`.",
            "Para Claude Code, empezar por la variante de plugin/skills de Claude y probarla en un proyecto desechable.",
            "Copiar o instalar solo el metodo y las skills que realmente vayas a usar; no mezclarlo de golpe con todos los catalogos.",
        ],
        "human": "Usalo como columna vertebral: primero adopta el metodo, luego agrega herramientas especializadas.",
        "ai": "Si este repo esta seleccionado, tratalo como la capa de proceso. Lee su README y la carpeta de skills/plugin relevante antes de instalar otras skills.",
        "order": 1,
        "install_mode": "reference_only",
        "caution": "Puede solaparse con agent-toolkit; si hay conflicto de instrucciones, deja superpowers como regla superior y agent-toolkit como caja de herramientas.",
    },
    "agent-toolkit": {
        "stack_role": "Caja de herramientas para productividad diaria en Claude Code.",
        "why": "Aporta skills, comandos y agentes practicos para desarrollo, documentacion y planificacion. Es ideal cuando quieres mejoras visibles sin diseñar todo un sistema desde cero.",
        "how": "Funciona como piezas copiables: comandos, agentes y skills que se agregan al entorno del asistente para tareas recurrentes.",
        "install": [
            "Inspeccionar `skills`, `commands` y `agents`.",
            "Elegir 3 a 5 piezas de uso diario y copiarlas al proyecto o perfil de Claude Code segun su formato.",
            "Probar cada pieza con una tarea real antes de instalar mas.",
        ],
        "human": "Instalalo despues de definir el metodo base; evita activar todo el pack en una sola pasada.",
        "ai": "Usa agent-toolkit como biblioteca de acciones concretas. No lo conviertas en autoridad si superpowers tambien fue elegido.",
        "order": 2,
        "install_mode": "reference_only",
        "caution": "No lo uses como sustituto de una arquitectura de contexto; complementa a superpowers.",
    },
    "claude-plugins-official": {
        "stack_role": "Canal oficial de plugins/extensiones para Claude Code.",
        "why": "Debe estar arriba cuando el usuario trabaja en Claude Code porque ofrece el camino mas confiable para extensiones oficiales antes de ir a repos comunitarios.",
        "how": "Funciona como repositorio de plugins. En Claude Code se instalan plugins seleccionados desde el propio entorno, despues de revisar permisos y archivos que modifican.",
        "install": [
            "Abrir el README del repositorio local y revisar la lista de plugins.",
            "Instalar solo plugins finalistas desde Claude Code con `/plugin install <plugin>@claude-plugins-official` cuando aplique.",
            "Leer permisos, comandos y archivos que cada plugin agrega antes de activarlo.",
        ],
        "human": "Empieza aqui si quieres extensiones confiables de Claude Code; no instales todos los plugins.",
        "ai": "Antes de sugerir un plugin oficial, explica que problema resuelve, que permisos requiere y como revertirlo.",
        "order": 3,
        "install_mode": "reference_only",
        "caution": "Un plugin puede ejecutar herramientas o modificar contexto; tratarlo como software, no como texto inocuo.",
    },
    "awesome-claude-code": {
        "stack_role": "Mapa curado del ecosistema Claude Code.",
        "why": "Sirve para descubrir scripts, hooks, slash commands, agentes y extensiones especificas de Claude Code sin leer decenas de repos al azar.",
        "how": "No es una dependencia. Es una guia de seleccion: primero filtra por necesidad, luego instala el recurso externo concreto.",
        "install": [
            "No instalarlo como dependencia del proyecto.",
            "Usarlo como indice para encontrar hooks, comandos o agentes concretos.",
            "Abrir solo los recursos finalistas y validar mantenimiento, permisos y compatibilidad.",
        ],
        "human": "Usalo para explorar, no para copiar todo.",
        "ai": "Lee este repo como catalogo. Selecciona maximo 2 o 3 recursos externos por iteracion.",
        "order": 4,
        "install_mode": "reference_only",
        "caution": "Al ser catalogo, puede llevarte a instalar demasiado. Mantenerlo como referencia.",
    },
    "skillspector": {
        "stack_role": "Filtro de seguridad para skills externas.",
        "why": "Si vas a instalar skills comunitarias, necesitas revisar riesgos antes de copiarlas al entorno del agente.",
        "how": "Analiza archivos de skills buscando patrones sospechosos, instrucciones peligrosas o comportamientos no deseados.",
        "install": [
            "Usarlo antes de instalar skills de catalogos grandes o repos desconocidos.",
            "Ejecutarlo contra la carpeta de la skill finalista, no contra toda la biblioteca.",
            "Revisar hallazgos manualmente antes de copiar la skill al perfil global.",
        ],
        "human": "Ponlo como paso de auditoria cuando la skill no venga de una fuente plenamente confiable.",
        "ai": "No instales skills externas sin mencionar si pasaron por revision o por que se consideran confiables.",
        "order": 5,
        "install_mode": "reference_only",
        "caution": "No reemplaza lectura humana; reduce riesgo y ruido.",
    },
    "context-engineering": {
        "stack_role": "Guia para diseñar contexto compacto y reutilizable.",
        "why": "Ayuda a que Claude Code, Codex u otro agente no dependan de prompts enormes ni lecturas repetidas.",
        "how": "Funciona como material de diseño: enseña a decidir que entra al contexto, que queda como referencia y como mantener instrucciones pequeñas.",
        "install": [
            "No instalar como dependencia.",
            "Leer las secciones aplicables a contexto, ejemplos y plantillas.",
            "Convertir las mejores ideas en `AGENTS.md`, context packs o guias del proyecto.",
        ],
        "human": "Usalo para mejorar tus instrucciones base y reducir gasto de tokens.",
        "ai": "Extrae principios, no copies el curso entero. Aplica solo a archivos de contexto del proyecto.",
        "order": 6,
        "install_mode": "reference_only",
        "caution": "Es formacion y referencia; no soluciona por si solo la instalacion de skills.",
    },
    "prompt-master": {
        "stack_role": "Mejora de prompts y briefs antes de ejecutar agentes.",
        "why": "Aporta una capa ligera para transformar ideas vagas en instrucciones accionables, util cuando el usuario quiere mejores resultados diarios.",
        "how": "Funciona como skill de redaccion/critica de prompts. Reduce reintentos y ambiguedad.",
        "install": [
            "Revisar la skill y adaptarla al estilo del agente que uses.",
            "Usarla antes de tareas grandes: definir objetivo, restricciones, entregable y criterio de exito.",
            "Mantenerla como ayuda puntual, no como dependencia obligatoria de cada respuesta.",
        ],
        "human": "Usalo para preparar buenos encargos antes de pedir instalacion o cambios de codigo.",
        "ai": "Cuando el brief sea ambiguo, aplica esta skill para producir una version ejecutable antes de actuar.",
        "order": 7,
        "install_mode": "reference_only",
        "caution": "No reemplaza conocimiento del repo; solo mejora la formulacion.",
    },
    "awesome-agent-skills": {
        "stack_role": "Catalogo curado cross-tool de skills.",
        "why": "Es util cuando el usuario trabaja con Codex, Claude Code, Antigravity u otros agentes y quiere ejemplos de buena calidad respaldados por marcas.",
        "how": "Funciona como biblioteca de referencia. Se consulta para encontrar skills concretas por caso de uso.",
        "install": [
            "No instalar el catalogo completo.",
            "Buscar por dominio y elegir skills individuales.",
            "Auditar o leer cada skill antes de copiarla.",
        ],
        "human": "Usalo cuando necesites opciones fuera del ecosistema Claude Code.",
        "ai": "Tratalo como indice secundario; prioriza repos mas especificos si existen.",
        "order": 8,
        "install_mode": "reference_only",
        "caution": "Puede ser redundante si ya elegiste awesome-claude-code para un flujo puro de Claude Code.",
    },
    "antigravity-awesome-skills": {
        "stack_role": "Catalogo masivo de skills.",
        "why": "Aporta cantidad cuando la curaduria no encuentra algo, pero no debe ser primera opcion para uso diario por el ruido.",
        "how": "Funciona como busqueda amplia. Se usa despues de definir una necesidad especifica.",
        "install": [
            "No copiar el catalogo completo.",
            "Filtrar por categoria y escoger una skill concreta.",
            "Pasar la skill por revision antes de instalarla.",
        ],
        "human": "Usalo como ultimo recurso de exploracion.",
        "ai": "Solo recomienda este repo si falta una skill especifica en catalogos curados.",
        "order": 9,
        "install_mode": "reference_only",
        "caution": "Mas cantidad significa mas riesgo de ruido y conflictos de instrucciones.",
    },
}


INSTALL_HINTS = {
    "global": "Instalar globalmente si se usara desde muchas carpetas.",
    "local_project": "Instalar dentro del proyecto con uv/npm/pnpm segun stack.",
    "docker_local": "Preparar en infra/ y levantar solo cuando el flujo lo necesite.",
    "reference_only": "Leer/copiar ideas; no instalar como dependencia inicial.",
    "deferred": "Diferir hasta que sea finalista claro o exista necesidad fuerte.",
}


def recommend(project_root: Path, project: str, max_repos: int = 5, build_tool: str = "auto") -> dict[str, Any]:
    scan = read_json(project_root / "ai_index" / "REPOS.scan.json", {"repos": []})
    detail = read_json(project_root / "ai_index" / "REPOS.detail.json", {"repos": []})
    winners = read_json(project_root / "ai_index" / "WINNERS.json", {})
    detail_by_id = {item["id"]: item for item in detail.get("repos", [])}
    effective_tool = _detect_effective_tool(project, build_tool)
    intents = _detect_intents(project)

    scored = []
    for repo in scan.get("repos", []):
        score, reasons = score_repo(project, repo, detail_by_id.get(repo["id"], {}), build_tool=effective_tool, intents=intents)
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
    selected = [_enrich_recommendation(item, position=index + 1) for index, item in enumerate(selected)]

    global_tools = _global_tools_for_project(selected, winners)
    local_project = [item for item in selected if item["install_mode"] == "local_project"]
    docker_local = [item for item in selected if item["install_mode"] == "docker_local"]
    reference_only = [item for item in selected if item["install_mode"] == "reference_only"]
    deferred = [item for item in selected if item["install_mode"] == "deferred"]

    safe_name = _slug(project)[:80] or "project"
    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project": project,
        "requested_tool": _norm_tool(build_tool),
        "build_tool": effective_tool,
        "detected_intents": sorted(intents),
        "superguide_file": f"ai_index/SUPERGUIAS/{safe_name}.md",
        "latest_superguide_file": "ai_index/CONTEXT_PACKS/latest.md",
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

    write_json(project_root / "data" / "decisions" / f"{safe_name}.json", result)
    write_superguide(project_root, result, safe_name=safe_name)
    return result


def write_superguide(project_root: Path, result: dict[str, Any], safe_name: str | None = None) -> Path:
    safe_name = safe_name or _slug(result.get("project", ""))[:80] or "project"
    text = _render_superguide(result)
    superguide = project_root / "ai_index" / "SUPERGUIAS" / f"{safe_name}.md"
    latest = project_root / "ai_index" / "CONTEXT_PACKS" / "latest.md"
    superguide.parent.mkdir(parents=True, exist_ok=True)
    latest.parent.mkdir(parents=True, exist_ok=True)
    superguide.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    return superguide


def write_context_pack(project_root: Path, result: dict[str, Any]) -> Path:
    return write_superguide(project_root, result)


def _render_superguide(result: dict[str, Any]) -> str:
    lines = [
        "# Super Guia Practica Del Proyecto",
        "",
        f"Generado: {result['generated_at']}",
        "",
        "## Proyecto",
        "",
        result["project"],
        "",
        "## Herramienta detectada para construir",
        "",
        result.get("build_tool", "codex"),
        "",
        "## Diagnostico",
        "",
        f"- Pista indicada en `--tool`: `{result.get('requested_tool', 'auto')}`",
        f"- Herramienta tomada del planteamiento: `{result.get('build_tool', '')}`",
        f"- Intenciones detectadas: {', '.join(result.get('detected_intents', [])) or 'general'}",
        "- Regla aplicada: la herramienta con la que construyes no siempre es el proveedor LLM de la app. Si el texto menciona Claude Code, se prioriza su ecosistema aunque el comando se haya ejecutado desde Codex.",
        f"- Archivo estable de esta recomendacion: `{result.get('superguide_file', '')}`",
        f"- Alias siempre actualizado: `{result.get('latest_superguide_file', 'ai_index/CONTEXT_PACKS/latest.md')}`",
        "",
        "## Indices que cualquier IA debe leer primero",
        "",
    ]
    lines.extend(f"- `{path}`" for path in result["read_first_for_any_ai"])
    lines.extend(
        [
            "",
            "## Veredicto Rapido",
            "",
            "Estos son los finalistas para este proyecto concreto. No instales catalogos completos: instala o copia piezas concretas despues de leer la seccion de cada repo.",
            "",
            "| Orden | Repo | Papel en el stack | Instalacion | Por que entra | Cuidado |",
            "|---:|---|---|---|---|---|",
        ]
    )
    for repo in result["recommended_repos"]:
        lines.append(
            "| "
            f"{repo.get('order', '')} | `{repo['id']}` | {repo.get('stack_role', '')} | `{repo['install_mode']}` | "
            f"{_sentence(repo.get('expert_reason') or ', '.join(repo.get('reasons', [])))} | {_sentence(repo.get('caution', ''))} |"
        )
    lines.extend(["", "## Herramientas globales sugeridas", ""])
    for tool in result["global_tools"]:
        lines.append(f"- `{tool['id']}`: {tool['reason']}")
    lines.extend(["", "## Orden recomendado de instalacion", ""])
    lines.extend(
        [
            "1. Instalar/verificar herramientas globales.",
            "2. Crear la carpeta del proyecto real.",
            "3. Leer esta guia completa antes de tocar repos externos.",
            "4. Instalar dependencias `local_project` dentro de ese proyecto.",
            "5. Preparar servicios `docker_local` en `infra/`, sin levantarlos hasta que el flujo lo necesite.",
            "6. Leer/copiar solo lo necesario de `reference_only`; en skills, elegir piezas concretas.",
            "7. Dejar `deferred` fuera de la primera version.",
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
                f"- orden: `{repo.get('order', '')}`",
                f"- ruta local: `{_repo_path(repo)}`",
                f"- papel en el stack: {repo.get('stack_role', '')}",
                f"- por que se recomienda: {repo.get('expert_reason') or ', '.join(repo.get('reasons', []))}",
                f"- como funciona: {repo.get('how_it_works', '')}",
                f"- resumen: {repo.get('desc') or repo.get('one') or ''}",
                f"- cuidado: {repo.get('caution', 'ninguno especial')}",
                f"- combinar con: {', '.join(repo.get('combines_with', [])) or 'ninguno declarado'}",
                f"- alternativas: {', '.join(repo.get('alternatives') or repo.get('alt', [])) or 'ninguna declarada'}",
                "",
                "#### Instalacion / uso",
                "",
            ]
        )
        lines.extend(f"{idx}. {step}" for idx, step in enumerate(repo.get("install_steps", []), start=1))
        lines.extend(
            [
                "",
                "#### Instrucciones para humano",
                "",
                repo.get("human_instructions", ""),
                "",
                "#### Instrucciones para IA instaladora",
                "",
                repo.get("ai_instructions", ""),
                "",
            ]
        )
    lines.extend(["## No instalar por defecto", ""])
    for item in result["avoid_by_default"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## Instrucciones Para El Humano",
            "",
            "1. Usa esta guia como lista de compra del proyecto, no como catalogo general.",
            "2. Instala primero lo global, despues lo local, luego Docker, y al final copia piezas de referencia.",
            "3. Si un repo esta marcado como `reference_only`, no lo instales completo: copia solo la skill, prompt, comando, hook o plantilla concreta que necesites.",
            "4. Si dos repos compiten, elige uno. Si se complementan, respeta el orden de esta guia.",
            "5. Guarda esta superguia dentro de la documentacion del proyecto real si vas a delegar la instalacion a otra IA.",
            "",
            "## Prompt Para El Agente Instalador",
            "",
            "```txt",
            "Lee esta superguia completa. Fue generada para un proyecto concreto; no la sustituyas por una lectura masiva de la biblioteca.",
            "Usa solo los repos finalistas y respeta el orden.",
            "Antes de instalar, separa: global, local del proyecto, Docker local, referencia y diferido.",
            "Para repos de tipo skill/directory, no copies catalogos completos: elige piezas concretas, explica por que, revisa permisos y evita instrucciones duplicadas.",
            "Si necesitas abrir mas contexto, abre primero REPOS.detail.json por id y despues la ficha humana del repo finalista. No leas repos completos salvo que vayas a instalar ese repo.",
            "Antes de ejecutar cambios, reporta el plan de instalacion con comandos o acciones concretas para cada grupo.",
            "```",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def _append_install_group(lines: list[str], repos: list[dict[str, Any]]) -> None:
    if not repos:
        lines.append("- Ninguno.")
        return
    for repo in repos:
        lines.append(f"- `{repo['id']}`: {repo.get('install_hint', '')} Ruta: `{_repo_path(repo)}`")


def score_repo(
    project: str,
    repo: dict[str, Any],
    detail: dict[str, Any],
    build_tool: str = "auto",
    intents: set[str] | None = None,
) -> tuple[int, list[str]]:
    text = _norm_text(project)
    intents = intents or _detect_intents(project)
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

    intent_score = _intent_boost(intents, text, repo)
    if intent_score:
        score += intent_score
        reasons.append(f"encaja con intencion detectada (+{intent_score})")

    if _should_suppress_for_intent(intents, text, repo):
        score -= 18
        reasons.append("penalizado: coincide solo por ruido, no por funcion real")

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
    if repo_id in REPO_GUIDANCE:
        return REPO_GUIDANCE[repo_id].get("install_mode", "reference_only")
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


def _detect_effective_tool(project: str, requested_tool: str) -> str:
    text = _norm_text(project)
    if _has_phrase(text, "claude code") or _has_phrase(text, "claude"):
        return "claude-code"
    if _has_phrase(text, "grok build"):
        return "grok-build"
    if _has_phrase(text, "open code") or _has_phrase(text, "opencode"):
        return "open-code"
    if _has_phrase(text, "antigravity"):
        return "antigravity"
    if _has_phrase(text, "codex"):
        return "codex"
    tool = _norm_tool(requested_tool)
    if tool == "claude":
        return "claude-code"
    if tool == "opencode":
        return "open-code"
    if tool == "auto":
        return "codex"
    return tool


def _detect_intents(project: str) -> set[str]:
    text = _norm_text(project)
    intents: set[str] = set()
    if any(_has_phrase(text, phrase) for phrase in ["claude code", "codex", "antigravity", "open code", "opencode"]):
        if any(_has_phrase(text, phrase) for phrase in ["optimizar", "ultralizar", "uso diario", "productividad", "mejorar", "skills", "plugins", "hooks", "commands", "comandos"]):
            intents.add("agent_ide_optimization")
    if _has_phrase(text, "claude code"):
        intents.add("claude_code_daily")
    return intents


def _intent_boost(intents: set[str], text: str, repo: dict[str, Any]) -> int:
    repo_id = repo.get("id", "")
    boost = sum(INTENT_BOOSTS.get(intent, {}).get(repo_id, 0) for intent in intents)
    conditional_terms = CONDITIONAL_SKILLS.get(repo_id)
    if conditional_terms and not any(_has_phrase(text, _norm_text(term)) for term in conditional_terms):
        boost -= 10
    return boost


def _should_suppress_for_intent(intents: set[str], text: str, repo: dict[str, Any]) -> bool:
    if not {"agent_ide_optimization", "claude_code_daily"} & intents:
        return False
    repo_id = repo.get("id", "")
    if repo_id in REPO_GUIDANCE:
        return False
    if repo_id in {"skills", "andrej-karpathy-skills", "headroom"}:
        return False
    if repo_id in CONDITIONAL_SKILLS:
        return not any(_has_phrase(text, _norm_text(term)) for term in CONDITIONAL_SKILLS[repo_id])
    if repo.get("cat") == 2 and repo.get("role") in {"skill", "directory"}:
        return False
    return True


def _enrich_recommendation(repo: dict[str, Any], position: int) -> dict[str, Any]:
    guidance = REPO_GUIDANCE.get(repo.get("id", ""), {})
    enriched = dict(repo)
    enriched["order"] = guidance.get("order", position)
    enriched["stack_role"] = guidance.get("stack_role") or _default_stack_role(repo)
    enriched["expert_reason"] = guidance.get("why") or _default_reason(repo)
    enriched["how_it_works"] = guidance.get("how") or _default_how(repo)
    enriched["install_steps"] = guidance.get("install") or _default_install_steps(repo)
    enriched["human_instructions"] = guidance.get("human") or _default_human_instruction(repo)
    enriched["ai_instructions"] = guidance.get("ai") or _default_ai_instruction(repo)
    enriched["caution"] = guidance.get("caution") or _default_caution(repo)
    return enriched


def _default_stack_role(repo: dict[str, Any]) -> str:
    role = repo.get("role", "reference")
    if role == "directory":
        return "Indice de referencia para elegir piezas concretas."
    if role == "skill":
        return "Skill o pack de instrucciones para el agente."
    if role == "platform":
        return "Plataforma base del producto."
    if role == "runtime":
        return "Motor de ejecucion dentro del proyecto."
    if role == "library":
        return "Libreria local del proyecto."
    return "Referencia o componente auxiliar."


def _default_reason(repo: dict[str, Any]) -> str:
    reasons = ", ".join(repo.get("reasons", []))
    summary = repo.get("desc") or repo.get("one") or ""
    if reasons and summary:
        return f"{summary} Relevancia detectada: {reasons}."
    return summary or reasons or "Seleccionado por coincidencia con el proyecto."


def _default_how(repo: dict[str, Any]) -> str:
    role = repo.get("role")
    if role in {"skill", "directory"}:
        return "Se usa como fuente de instrucciones, skills, prompts o ejemplos. Normalmente no se instala completo como dependencia."
    if repo.get("install_mode") == "docker_local":
        return "Se ejecuta como servicio local aislado, normalmente con Docker."
    if repo.get("install_mode") == "local_project":
        return "Se agrega como dependencia o herramienta dentro de la carpeta del proyecto."
    return "Se consulta como referencia hasta que el proyecto justifique instalarlo."


def _default_install_steps(repo: dict[str, Any]) -> list[str]:
    mode = repo.get("install_mode", "reference_only")
    if mode == "global":
        return [
            "Verificar si ya esta instalado en la maquina.",
            "Instalarlo globalmente solo si se usara desde varios proyectos.",
            "Probar el comando en una carpeta temporal antes de usarlo en el proyecto real.",
        ]
    if mode == "local_project":
        return [
            "Crear o abrir la carpeta del proyecto real.",
            "Instalar la dependencia con el gestor del stack del proyecto (`uv`, `npm`, `pnpm` o equivalente).",
            "Guardar configuracion y variables de entorno dentro del proyecto, no en la biblioteca.",
        ]
    if mode == "docker_local":
        return [
            "Crear una carpeta `infra/` dentro del proyecto real.",
            "Copiar solo los archivos de despliegue necesarios.",
            "Levantar el servicio cuando el flujo lo necesite y documentar puertos/volumenes.",
        ]
    if mode == "deferred":
        return [
            "No instalar en la primera version.",
            "Revisar de nuevo cuando exista una necesidad clara.",
        ]
    return [
        "Leer la ficha y el README del repo finalista.",
        "Copiar solo archivos, prompts, skills o ejemplos necesarios.",
        "Registrar que se copio y por que dentro de la documentacion del proyecto.",
    ]


def _default_human_instruction(repo: dict[str, Any]) -> str:
    mode = repo.get("install_mode", "reference_only")
    if mode == "reference_only":
        return "Usalo para decidir y copiar piezas concretas. Evita instalar o pegar todo el repositorio."
    return "Instalalo solo despues de confirmar que es finalista y que su funcion no esta cubierta por otro repo seleccionado."


def _default_ai_instruction(repo: dict[str, Any]) -> str:
    return (
        "Antes de actuar, explica la funcion exacta de este repo, su modo de instalacion y que archivos necesitas leer. "
        "No abras el repositorio completo salvo que sea indispensable para instalarlo."
    )


def _default_caution(repo: dict[str, Any]) -> str:
    avoid_if = repo.get("avoid_if")
    if avoid_if:
        return f"Evitar si {avoid_if}"
    if repo.get("role") in {"skill", "directory"}:
        return "Puede duplicar instrucciones de otros packs; instalar solo piezas concretas."
    if repo.get("setup") == "heavy":
        return "Puede requerir GPU o infraestructura pesada."
    return "Validar mantenimiento, permisos y solapamiento antes de instalar."


def _repo_path(repo: dict[str, Any]) -> str:
    return repo.get("local_path") or repo.get("path") or ""


def _sentence(value: str, limit: int = 180) -> str:
    text = " ".join((value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


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
