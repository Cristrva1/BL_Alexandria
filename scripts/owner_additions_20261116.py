"""Owner-requested catalog additions, 2026-11-16.

Dated editorial migration on the same path as document_curation_20261114.py:
``import_document_repos.inspect_repository`` audits each public GitHub identity
(metadata, README blob and root tree) into ignored data/reports/, and this script
turns the reviewed rows into complete compact + detail entries (category, section,
access, getting_started, routes, goals). The 4-section descriptions live in
curation/descripciones-4s/46-altas-del-propietario.json and are applied with
apply_descripciones_4s.py. Nothing catalogued is installed or executed.

    uv run python scripts/owner_additions_20261116.py --fetch   # audit via gh api
    uv run python scripts/owner_additions_20261116.py --apply   # write the indices
"""
from __future__ import annotations

import argparse
import base64
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import document_curation_20261114 as base  # noqa: E402
from import_document_repos import inspect_repository  # noqa: E402
from repo_intelligence.core.access import access_routes  # noqa: E402

DATE = "2026-11-16"
base.DATE = DATE
AUDIT = ROOT / "data/reports/owner-additions-20261116"

# GitHub identity | catalog id | category | section | kind | display name | plain-language function.
DATA = """
neo4j/mcp|neo4j-mcp|5|servidores|mcp|Neo4j MCP (oficial)|Servidor MCP oficial de Neo4j para que un asistente lea el esquema de un grafo y ejecute consultas Cypher de lectura o escritura.
deepseek-ai/deepseek-harness|deepseek-harness|20|terminal|agent|DeepSeek Harness (DSH)|Harness de agentes de DeepSeek en vista previa, con arquitectura de plugins, Web UI local y proveedores de modelos configurables.
TanStack/query|tanstack-query|9|componentes|library|TanStack Query|Biblioteca para obtener, cachear, sincronizar y actualizar datos del servidor en React, Vue, Solid, Svelte, Angular y otros frameworks.
google-antigravity/antigravity-cli|antigravity-cli|20|terminal|app|Antigravity CLI|Agente de programación de Google para la terminal (agy), con subagentes, MCP y skills; se distribuye en binarios, sin código fuente.
CopilotKit/OpenBot|openbot|21|asistentes|agent|OpenBot|Espacio autoalojable de CopilotKit para compañeros de IA con navegador propio, permisos, aprobaciones y auditoría, conectables por AG-UI.
Tencent-Hunyuan/HunyuanVideo-1.5|hunyuanvideo-1-5|12|generativo|model|HunyuanVideo 1.5|Modelo de video de Tencent de 8,3B parámetros que genera clips desde texto o imagen en 480p y 720p con GPU de 14 GB o más.
apache/iceberg|apache-iceberg|25|datos|library|Apache Iceberg|Formato abierto de tablas analíticas de la Apache Software Foundation; este repositorio es la implementación de referencia en Java.
delta-io/delta|delta-lake|25|datos|library|Delta Lake|Capa de almacenamiento con transacciones ACID sobre Parquet para montar un lakehouse con Spark, Flink, Trino y otros motores.
jupyterlab/jupyterlab|jupyterlab|25|datos|app|JupyterLab|Entorno web de Project Jupyter con notebooks, terminal, editor de texto y explorador de archivos, ampliable mediante extensiones.
pyannote/pyannote-audio|pyannote-audio|29|audio|library|pyannote.audio|Kit de PyTorch para diarización de hablantes (quién habla y cuándo) con modelos preentrenados y un servicio premium opcional.
elevenlabs/elevenlabs-python|elevenlabs-python|29|tts|library|ElevenLabs (SDK de Python)|SDK oficial de Python para la API de pago de ElevenLabs: voz sintética, clonación, transcripción, música y agentes de voz.
"""

SKIPPED = [
    {"requested": "microsoft/autogen", "reason": "Ya figura en data/retired.json (motivo «abandonado», 2026-11-15). Su README declara el proyecto archivado y sin correcciones de seguridad y remite a Microsoft Agent Framework, que ya está catalogado; reincorporarlo contradiría ese retiro."},
    {"requested": "browserbase (plataforma)", "reason": "Browserbase es un servicio de navegadores en la nube; su pieza abierta principal, browserbase/stagehand, ya está catalogada y su servidor MCP (browserbase/mcp-server-browserbase) está archivado."},
    {"requested": "elevenlabs/elevenlabs-mcp", "reason": "Archivado en GitHub; se cataloga en su lugar el SDK oficial de Python (elevenlabs/elevenlabs-python), activo."},
]

ENTRY_COMMANDS = {
    "neo4j-mcp": "pip install neo4j-mcp-server",
    "deepseek-harness": "npx @deepseek-ai/dsh web",
    "jupyterlab": "pip install jupyterlab",
    "pyannote-audio": "pip install pyannote.audio",
    "elevenlabs-python": "pip install elevenlabs",
}
ENTRY_URLS = {
    "tanstack-query": "https://tanstack.com/query/latest/docs/framework/react/overview",
    "antigravity-cli": "https://antigravity.google/docs/cli/overview",
    "apache-iceberg": "https://py.iceberg.apache.org/",
    "delta-lake": "https://docs.delta.io/latest/quick-start.html",
    "hunyuanvideo-1-5": "https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/checkpoints-download.md",
}
LICENSES = {"neo4j-mcp": "GPL-3.0", "hunyuanvideo-1-5": "Tencent Hunyuan Community License", "antigravity-cli": "Propietaria (sin licencia en el repositorio)"}
READY = {"jupyterlab", "openbot", "antigravity-cli"}
GOALS = {
    "neo4j-mcp": ["mcp"], "deepseek-harness": ["programar", "mcp"], "tanstack-query": ["web"],
    "antigravity-cli": ["programar", "mcp"], "openbot": ["investigar", "mcp"], "hunyuanvideo-1-5": ["video"],
    "apache-iceberg": ["datos"], "delta-lake": ["datos"], "jupyterlab": ["datos"],
    "pyannote-audio": ["voz"], "elevenlabs-python": ["narrar"],
}
SETUP = {"hunyuanvideo-1-5": "heavy", "openbot": "heavy", "apache-iceberg": "medium", "delta-lake": "medium",
         "jupyterlab": "easy", "elevenlabs-python": "easy", "tanstack-query": "easy", "antigravity-cli": "easy",
         "neo4j-mcp": "medium", "deepseek-harness": "medium", "pyannote-audio": "medium"}
PROV = {"deepseek-harness": ["deepseek", "anthropic", "openai", "local"], "openbot": ["openai", "anthropic", "google", "local"],
        "antigravity-cli": ["google"], "elevenlabs-python": ["elevenlabs"], "hunyuanvideo-1-5": ["local"], "pyannote-audio": ["local"]}
TAGS = {
    "neo4j-mcp": ["mcp", "graph", "neo4j", "cypher", "go"], "deepseek-harness": ["agents", "coding", "plugins", "typescript"],
    "tanstack-query": ["frontend", "data-fetching", "cache", "typescript"], "antigravity-cli": ["coding", "agents", "cli", "google"],
    "openbot": ["agents", "computer-use", "ag-ui", "mcp", "typescript"], "hunyuanvideo-1-5": ["video", "inference", "local", "python"],
    "apache-iceberg": ["data", "lakehouse", "table-format", "java"], "delta-lake": ["data", "lakehouse", "table-format", "scala"],
    "jupyterlab": ["notebooks", "data", "python", "typescript"], "pyannote-audio": ["audio", "diarization", "pytorch", "python"],
    "elevenlabs-python": ["tts", "voice", "api", "python"],
}
ROLE = {"mcp": "runtime", "agent": "app", "library": "library", "app": "app", "model": "runtime"}
HOW = {
    "neo4j-mcp": "Un cliente MCP llama sus herramientas get-schema, read-cypher, write-cypher y list-gds-procedures contra una instancia Neo4j que tú configuras.",
    "deepseek-harness": "Un servidor local en Node.js carga plugins sobre Cordis y sirve una Web UI; el modelo se configura por proveedor (DeepSeek, terceros o una API compatible propia).",
    "tanstack-query": "Tu aplicación declara consultas y mutaciones con claves de caché; la biblioteca gestiona caché, reintentos, refetch en segundo plano y estados de carga.",
    "antigravity-cli": "La TUI `agy` comparte el motor de agentes de Antigravity 2.0, inicia sesión con Google y ejecuta ediciones y comandos con tu permiso.",
    "openbot": "Un backend en contenedores (PostgreSQL, API y Bots) más CopilotKit Intelligence coordina agentes propios o externos vía AG-UI y herramientas MCP con políticas y auditoría.",
    "hunyuanvideo-1-5": "Un DiT de 8,3B parámetros con VAE causal 3D genera video a partir de texto o imagen; se ejecuta con PyTorch y CUDA o mediante ComfyUI y Diffusers.",
    "apache-iceberg": "Define una especificación de metadatos (snapshots, esquemas y particiones) sobre archivos Parquet, ORC o Avro que leen motores como Spark, Flink o Trino.",
    "delta-lake": "Mantiene un registro de transacciones junto a archivos Parquet para dar ACID, versiones y viaje en el tiempo a motores como Spark, Flink o Trino.",
    "jupyterlab": "Un servidor Jupyter local sirve la interfaz web; los kernels (Python u otros lenguajes) ejecutan las celdas de cada notebook.",
    "pyannote-audio": "Carga pipelines de PyTorch desde Hugging Face (con token y condiciones aceptadas) y devuelve segmentos etiquetados por hablante.",
    "elevenlabs-python": "Cliente HTTP generado con Fern que llama a la API de ElevenLabs con tu clave; el procesamiento ocurre en sus servidores.",
}


# Two illustrative scenarios and a proposed (not executed) first try per entry.
EXAMPLES = {
    "neo4j-mcp": (["Preguntar en lenguaje natural por el esquema de un grafo de prueba", "Consultar relaciones con Cypher de solo lectura desde el agente"],
                  "Conecta el servidor en modo solo lectura a una base Neo4j de prueba y pide al agente que describa su esquema", "El agente lista etiquetas y relaciones que coinciden con las de la base"),
    "deepseek-harness": (["Probar un harness de agentes extensible por plugins", "Comparar proveedores de modelos desde una misma Web UI"],
                         "Abre la Web UI en una VM o contenedor, configura un proveedor y pide un resumen de un archivo ficticio", "El resumen aparece y el registro de la sesión muestra el proveedor elegido"),
    "tanstack-query": (["Cachear y revalidar datos de una API en una app React", "Mostrar estados de carga y error sin estado global manual"],
                       "Envuelve una llamada a una API pública de prueba en una consulta y muestra sus estados", "Ves carga, datos y un refetch al volver a enfocar la ventana"),
    "antigravity-cli": (["Pedir cambios a un proyecto desde la terminal o por SSH", "Delegar tareas paralelas en subagentes"],
                        "Inicia agy en un proyecto de prueba y pide renombrar una función con su prueba", "El cambio aparece en el diff y pediste permiso antes de ejecutar comandos"),
    "openbot": (["Dar a un asistente un navegador propio con aprobaciones", "Conectar un agente existente por AG-UI a un espacio común"],
                "Instala la app de escritorio, configura un modelo y pide una búsqueda web que requiera aprobación", "La acción queda pendiente de tu aprobación y aparece en la auditoría"),
    "hunyuanvideo-1-5": (["Generar un clip corto desde texto con GPU de consumo", "Animar una imagen fija en 480p"],
                         "Genera un clip de pocos segundos en 480p con offloading activado", "El video se guarda y anotas tiempo y VRAM usados"),
    "apache-iceberg": (["Compartir una tabla analítica entre varios motores", "Consultar un snapshot anterior tras un cambio de esquema"],
                       "Crea una tabla Iceberg pequeña con PyIceberg, añade una columna y consulta el snapshot previo", "El snapshot anterior conserva el esquema original"),
    "delta-lake": (["Añadir transacciones y versiones a archivos Parquet", "Recuperar una versión anterior de una tabla"],
                   "Escribe una tabla Delta local, actualiza unas filas y lee la versión 0", "La versión 0 muestra los datos originales"),
    "jupyterlab": (["Analizar datos de muestra en un notebook", "Documentar un experimento con código y resultados"],
                   "Crea un notebook, carga un CSV ficticio y dibuja un gráfico simple", "El notebook guarda código, tabla y gráfico al reabrirlo"),
    "pyannote-audio": (["Separar por hablante la grabación de una reunión", "Añadir hablantes a una transcripción"],
                       "Ejecuta community-1 sobre un audio corto con dos voces de prueba", "Los segmentos alternan entre dos hablantes con marcas de tiempo coherentes"),
    "elevenlabs-python": (["Generar una locución para un video", "Prototipar un agente de voz conectado a la API"],
                          "Convierte una frase corta a voz con una voz predefinida", "Obtienes un MP3 reproducible y el consumo aparece en tu cuenta"),
}
MODELS = {
    "neo4j-mcp": "El modelo lo aporta el cliente MCP; el servidor solo habla con Neo4j",
    "deepseek-harness": "DeepSeek, Anthropic, OpenAI, Kimi, GLM o una API compatible propia",
    "tanstack-query": "No usa LLM ni API de IA",
    "antigravity-cli": "Modelos de Google según la cuenta o el proyecto de GCP",
    "openbot": "OpenAI, Claude, Gemini o un endpoint compatible con OpenAI, también local",
    "hunyuanvideo-1-5": "Pesos propios de Tencent en local; reescritura de prompts opcional con vLLM",
    "apache-iceberg": "No usa LLM ni API de IA",
    "delta-lake": "No usa LLM ni API de IA",
    "jupyterlab": "No usa LLM ni API de IA en la instalación básica",
    "pyannote-audio": "Modelos locales de Hugging Face o servicio premium de pyannoteAI",
    "elevenlabs-python": "Modelos de ElevenLabs en su nube, con clave de API",
}


def review_fields(rid, entry, access, source):
    scenarios, action, success = EXAMPLES[rid]
    return {
        "cases": scenarios, "why": "Usos propuestos: " + "; ".join(scenarios) + ".",
        "choose_if": "Tu objetivo encaja con estos ejemplos: " + "; ".join(scenarios),
        "models": MODELS[rid], "source_archived": False,
        "practical_examples": [{"scenario": s, "status": "illustrative"} for s in scenarios],
        "first_try": {"action": action, "success": success, "execution": "proposed_not_executed"},
        "editorial_review": {"status": "source_reviewed", "checked_at": DATE, "source": source["html_url"],
                             "source_blob_sha": source["sha"], "previous_category": [entry["cat"], entry["sub"]],
                             "category_verdict": "confirmed", "note": access.get("api_note", ""),
                             "checks": ["identity", "category", "examples", "installation_source", "api_costs",
                                        "claude_code", "codex", "antigravity", "local_model"],
                             "installation_tested": False},
    }


def rows():
    result = {}
    for line in DATA.strip().splitlines():
        name, rid, category, section, kind, display, one = line.split("|", 6)
        assert 60 <= len(one) <= 175, (name, len(one))
        result[name.lower()] = dict(name=name, id=rid, cat=int(category), sub=section, kind=kind, display=display, one=one)
    return result


def access_for(entry, source, text):
    kind = entry["kind"]
    a = base.access_profile({**entry, "kind": {"agent": "agent", "model": "model"}.get(kind, kind)}, source, text)
    rid = entry["id"]
    a["antigravity"] = "not_documented"
    if rid == "neo4j-mcp":
        a.update(antigravity="connector", hardware="prerequisites",
                 hardware_note="Necesitas una base Neo4j (local, Docker o Aura) y credenciales; GDS es opcional.",
                 cost_note="El modelo se consume en el cliente MCP. Neo4j Aura y las ediciones comerciales tienen sus propias condiciones; con ellas el servidor queda cubierto por esos contratos.")
    if rid == "deepseek-harness":
        a.update(mode="software", api="depends", cost="choice", local_model="supported", hardware="ordinary",
                 api_note="Necesita un proveedor: clave de DeepSeek, un proveedor de terceros incluido (Anthropic, OpenAI, Kimi, GLM) o una API propia compatible.",
                 local_note="La guía de proveedores admite una API personalizada para un servidor autoalojado; el harness no incluye modelos.",
                 cost_note="El consumo se paga al proveedor elegido. Un servidor local consume tu hardware.",
                 subscription_note="No documenta uso con sesiones de Claude Code o Codex; los plugins y servidores MCP se configuran dentro de DSH.",
                 hardware_note="Node.js para `npx`; pnpm para ejecutar desde el código. Preferible una VM o contenedor desechable según su aviso de seguridad.")
    if rid == "antigravity-cli":
        a.update(mode="software", api="not_required", cost="choice", local_model="not_documented", antigravity="native", hardware="ordinary",
                 api_note="Inicia sesión con una cuenta de Google (o un proyecto de GCP para empresa); no pide una clave de API propia en la ruta básica.",
                 subscription_note="Es la superficie de terminal de Google Antigravity y usa la cuenta y el plan de Google con que inicias sesión.",
                 cost_note="Los límites dependen de la cuenta y el plan de Google. Google recoge datos de interacción por defecto (desactivable en ajustes).",
                 local_note="No documenta modelos locales.")
    if rid == "openbot":
        a.update(mode="software", api="depends", cost="choice", local_model="supported", hardware="prerequisites",
                 claude_code="not_documented", codex="not_documented",
                 api_note="Elige OpenAI, Claude, Gemini o un endpoint compatible con OpenAI; el despliegue en Kubernetes de evaluación usa una clave de modelo.",
                 local_note="El README describe una operación totalmente local con OpenBot, Intelligence y un modelo compatible; las apps conectadas siguen usando internet.",
                 cost_note="La plantilla es MIT, pero CopilotKit Intelligence tiene licencia aparte: local gratuita para uso personal, prueba para Kubernetes y licencia de producción después.",
                 subscription_note="Los agentes externos se conectan por AG-UI (el repositorio trae ejemplos para LangGraph, Mastra, CrewAI, Agno, Pydantic AI, ADK y otros); no usa sesiones de Claude Code o Codex.",
                 hardware_note="Docker para PostgreSQL, la API y los Bots; Bun para ejecutar desde el código; Kubernetes y Helm para equipos.")
    if rid == "hunyuanvideo-1-5":
        a.update(api="optional", local_model="supported", hardware="gpu", cost="choice",
                 api_note="La reescritura de prompts usa un endpoint vLLM opcional; si no se configura, el pipeline genera sin reescritura remota.",
                 local_note="Inferencia local con pesos descargados de Hugging Face, sujeta a la Tencent Hunyuan Community License.",
                 hardware_note="GPU NVIDIA con CUDA y al menos 14 GB de VRAM con offloading; Linux y Python 3.10 o superior.",
                 cost_note="Sin pago por llamada en la ruta local; consume GPU. La licencia excluye la UE, el Reino Unido y Corea del Sur.")
    if rid == "pyannote-audio":
        a.update(api="optional", local_model="supported", hardware="model_dependent", cost="choice",
                 api_note="community-1 corre localmente con un token de Hugging Face; precision-2 corre en los servidores de pyannoteAI con su propia clave.",
                 local_note="Los pipelines abiertos se ejecutan localmente en CPU o GPU tras aceptar sus condiciones en Hugging Face.",
                 cost_note="La ruta local no paga por uso; pyannoteAI ofrece créditos gratuitos y después cobra. La telemetría es opcional (PYANNOTE_METRICS_ENABLED).",
                 hardware_note="Python 3.11 o superior y ffmpeg; GPU recomendable para audio largo.")
    if rid == "elevenlabs-python":
        a.update(api="required", cost="usage_based", local_model="not_applicable",
                 api_note="Toda llamada usa la API de ElevenLabs con tu ELEVENLABS_API_KEY.",
                 cost_note="Consumo por caracteres, minutos o créditos según el plan de ElevenLabs; el SDK es gratuito.",
                 local_note="No ejecuta modelos localmente: es un cliente de un servicio en la nube.",
                 hardware_note="Python 3.8 o superior y conexión a internet.")
    if rid in {"apache-iceberg", "delta-lake"}:
        a.update(hardware="prerequisites",
                 hardware_note="JVM (Java 17 o 21 para compilar Iceberg; Scala/sbt para Delta) o las bibliotecas de Python y Rust del ecosistema; un motor como Spark, Trino o DuckDB para consultar.")
    if rid == "jupyterlab":
        a.update(hardware="ordinary", hardware_note="Python con pip, conda o mamba; los kernels y extensiones añaden sus propias dependencias.",
                 cost_note="Sin coste de modelo. Las extensiones de IA (p. ej. Jupyter AI) se configuran aparte con sus proveedores.")
    if rid == "tanstack-query":
        a.update(hardware="ordinary", hardware_note="Un proyecto JavaScript o TypeScript con el adaptador de tu framework.")
    return a


def starting_for(entry, source, text, access, meta):
    kind = {"agent": "app", "model": "model"}.get(entry["kind"], entry["kind"])
    if entry["id"] in READY:
        base.READY.add(entry["id"])
    start = base.starting({**entry, "kind": kind}, source, text, access, meta)
    rid = entry["id"]
    command = ENTRY_COMMANDS.get(rid, "")
    if command and command not in text:
        command = ""
    start.update(command=command, command_status="documented" if command else "readme")
    if rid in ENTRY_URLS:
        start["entry_url"] = ENTRY_URLS[rid]
    custom = {
        "deepseek-harness": ["Lee SAFETY.md y prepara una VM, contenedor o carpeta de prueba: es una vista previa que ejecuta código generado por el modelo.",
                             "Inicia la Web UI con el comando de npm y configura un proveedor en Settings → Models.",
                             "Pide una tarea pequeña sobre archivos de prueba; añade plugins o servidores MCP uno por uno."],
        "antigravity-cli": ["Revisa la documentación oficial de la CLI y los términos de uso y datos de Google antes de instalar.",
                            "Instala la versión para tu sistema desde la guía oficial e inicia `agy` dentro de un proyecto de prueba.",
                            "Completa el inicio de sesión con Google y pide un cambio acotado; revisa los permisos que concede cada herramienta."],
        "openbot": ["Para probarlo solo, descarga la app de escritorio enlazada en el README; incluye el backend en Docker.",
                    "Elige el modelo (OpenAI, Claude, Gemini o un endpoint compatible) y revisa la licencia local de CopilotKit Intelligence.",
                    "Pide una tarea con aprobación activada y revisa la auditoría antes de conectar cuentas reales o un equipo."],
        "jupyterlab": ["Crea un entorno de Python e instala JupyterLab con pip, conda o mamba.",
                       "Ejecuta `jupyter lab` en una carpeta de prueba y crea un notebook.",
                       "Ejecuta unas celdas y guarda el notebook antes de instalar extensiones."],
        "hunyuanvideo-1-5": ["Confirma que tu país no está excluido por la licencia y que tienes Linux, CUDA y al menos 14 GB de VRAM.",
                             "Instala las dependencias y descarga los pesos según checkpoints-download.md; ComfyUI y Diffusers son rutas alternativas.",
                             "Genera un clip corto en 480p con offloading activado y mide tiempo y memoria antes de subir a 720p."],
        "apache-iceberg": ["Decide el motor (Spark, Flink, Trino, DuckDB) o la biblioteca (PyIceberg, iceberg-rust) con que vas a leer y escribir tablas.",
                           "Configura un catálogo y un almacenamiento de prueba según la documentación oficial.",
                           "Crea una tabla pequeña, haz un cambio de esquema y consulta un snapshot anterior."],
        "delta-lake": ["Sigue la guía rápida oficial con Spark (Scala, Java o Python) o usa delta-rs si no quieres JVM.",
                       "Escribe una tabla de prueba en un directorio local y lee su historial.",
                       "Prueba una actualización y una consulta de una versión anterior antes de usar almacenamiento en la nube."],
        "pyannote-audio": ["Instala ffmpeg y el paquete; acepta las condiciones de pyannote/speaker-diarization-community-1 en Hugging Face y crea un token.",
                           "Ejecuta el pipeline sobre un audio corto, en GPU si la tienes.",
                           "Revisa los segmentos por hablante antes de combinarlos con una transcripción."],
        "elevenlabs-python": ["Crea una clave en ElevenLabs y guárdala como ELEVENLABS_API_KEY fuera del repositorio.",
                              "Instala el paquete y convierte una frase corta con el ejemplo del README.",
                              "Revisa el consumo en tu cuenta antes de generar audio largo o clonar voces (con consentimiento)."],
    }
    if rid in custom:
        start["steps"] = custom[rid]
    return start


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    compact = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))
    curated = rows()
    if args.fetch:
        known = {str(r["github_id"]): r["id"] for r in compact["repos"] if r.get("github_id") and not r.get("alias_of")}
        records = [inspect_repository(row["name"], known, AUDIT / "github") for row in curated.values()]
        (AUDIT / "repositories.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    records = json.loads((AUDIT / "repositories.json").read_text(encoding="utf8"))
    candidates = {r["metadata"]["full_name"].lower(): r for r in records if r["status"] == "new"}
    assert set(candidates) == set(curated), (set(candidates) ^ set(curated))
    retired = {r["github_id"] for r in json.loads((ROOT / "data/retired.json").read_text(encoding="utf8"))["repos"]}
    existing = {r["id"] for r in compact["repos"]}
    added = []
    for name, row in candidates.items():
        meta, source = row["metadata"], row["readme"]
        entry = curated[name]
        rid = entry["id"]
        assert meta["id"] not in retired, rid
        if rid in existing:  # already applied; the migration is idempotent
            continue
        text = base64.b64decode(source["content"]).decode("utf8", errors="replace")
        access = access_for(entry, source, text)
        start = starting_for(entry, source, text, access, meta)
        category = next(c for c in compact["categories"] if c["num"] == entry["cat"])
        assert entry["sub"] in {s["key"] for s in category["subs"]}, rid
        lic = LICENSES.get(rid) or (meta.get("license") or {}).get("spdx_id")
        repo = {"id": rid, "name": entry["display"], "cat": entry["cat"], "sub": entry["sub"], "role": ROLE[entry["kind"]],
                "exec": "hybrid" if access["api"] in {"optional", "required", "depends"} or rid == "antigravity-cli" else "local",
                "setup": SETUP[rid], "mcp": entry["kind"] == "mcp" or rid in {"openbot", "deepseek-harness", "antigravity-cli"},
                "prov": PROV.get(rid, []), "tags": TAGS[rid], "stars": meta["stargazers_count"], "gh": meta["full_name"],
                "lib": False, "pick": False, "one": entry["one"], "alt": [], "doc": f"human/fichas/{rid}.md",
                "github_id": meta["id"], "lang": meta.get("language"), "license": lic, "added_at": DATE, "github_checked": DATE,
                "goals": GOALS[rid], "source_archived": bool(meta.get("archived"))}
        repo["routes"] = access_routes({"access": access})
        files = [i["path"] for i in row["tree"].get("tree", []) if i.get("type") == "blob"]
        manifests = [p for p in files if p in {"pyproject.toml", "package.json", "Cargo.toml", "go.mod", "build.gradle", "build.sbt", "requirements.txt", "Dockerfile", "docker-compose.yml"}]
        limits = "Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada."
        extra = {
            "deepseek-harness": " Vista previa con cambios incompatibles anunciados y sin auditoría de seguridad.",
            "antigravity-cli": " Producto propietario: el repositorio solo contiene README, changelog y ejemplos; la organización de GitHub no está verificada, pero el sitio oficial antigravity.google documenta la CLI.",
            "openbot": " CopilotKit Intelligence es un componente con licencia propia, necesario para ejecutar OpenBot.",
            "hunyuanvideo-1-5": " Licencia comunitaria de Tencent con exclusión territorial (UE, Reino Unido, Corea del Sur) y política de uso aceptable.",
            "neo4j-mcp": " GPL-3.0; con Aura o ediciones comerciales de Neo4j aplican sus contratos.",
            "elevenlabs-python": " Servicio de pago en la nube; clonar voces requiere consentimiento de la persona.",
        }
        limits += extra.get(rid, "")
        avoid = {"library": "buscas una aplicación lista y no quieres preparar un proyecto de código",
                 "mcp": "necesitas un producto autónomo y esta pieza requiere un cliente MCP y una base Neo4j",
                 "model": "no tienes una GPU NVIDIA con memoria suficiente o te afecta la exclusión territorial de la licencia",
                 "agent": "necesitas una herramienta estable y auditada para datos sensibles",
                 "app": "necesitas una instalación sin cuentas ni dependencias adicionales"}[entry["kind"]]
        d = {"name": repo["name"], "cat": repo["cat"], "sub": repo["sub"], "desc": entry["one"], "how": HOW[rid],
             "install": "Sigue la instalación y el ejemplo mínimo en " + source["html_url"], "cases": [entry["one"]],
             "stack": ", ".join([v for v in [meta.get("language"), *manifests] if v]),
             "choose_if": "buscas esta función: " + entry["one"], "avoid_if": avoid, "limits": limits,
             "combines_with": [], "alternatives": [], "repo": meta["html_url"], "homepage": meta.get("homepage"),
             "license": lic, "lang": meta.get("language"), "updated": DATE, "doc": f"human/fichas/{rid}.md",
             "access": access, "getting_started": start, "first_step": start["steps"][0],
             "sources": {"readme_blob_sha": source["sha"], "root_tree_sha": row["tree"]["sha"], "readme_url": source["html_url"],
                         "github_checked": DATE, "collection": "owner-additions-2026-11-16"}}
        d.update(review_fields(rid, entry, access, source))
        compact["repos"].append(repo)
        detail["repos"][rid] = d
        added.append({"id": rid, "full_name": meta["full_name"], "github_id": meta["id"], "readme_blob_sha": source["sha"]})
    for cat in compact["categories"]:
        cat["count"] = sum(r["cat"] == cat["num"] and not r.get("alias_of") for r in compact["repos"])
    public = [r for r in compact["repos"] if r.get("gh") and not r.get("alias_of")]
    compact["meta"]["updated"] = DATE
    total = sum(not r.get("alias_of") for r in compact["repos"])
    compact["meta"]["title"] = f"Índice IA — {total} repos curados de IA, automatización y herramientas"
    report = {"checked_at": DATE, "source": "Solicitud del propietario del catálogo (2026-11-16).", "added_count": len(added),
              "added": added, "skipped": SKIPPED, "total_public_repositories": len(public),
              "notes": ["No se instaló ni se ejecutó ningún proyecto del catálogo.",
                        "Identidades verificadas con la API de GitHub (id numérico, propietario, licencia, archivado)."]}
    print({"new": len(added), "public_total": len(public), "apply": args.apply})
    if args.apply:
        (ROOT / "INDICE_IA.json").write_text(json.dumps(compact, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
        (ROOT / "INDICE_IA.detalle.json").write_text(json.dumps(detail, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
        (ROOT / "reports/owner-additions-2026-11-16.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf8")


if __name__ == "__main__":
    main()
