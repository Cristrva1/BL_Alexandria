"""Apply the reviewed 2026-11-14 access migration to the canonical indices.

This is an editorial migration, not an inference engine. Explicit repository
sets define the scope of each claim; missing proof stays unconfirmed. Re-run the
source audit and review these sets before using a newer date.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
from repo_intelligence.core.access import access_routes


def ids(text: str) -> set[str]:
    return set(text.split())


NO_AI = ids("""
huginn node-red windmill kestra n8n activepieces trigger-dev whatsapp-web-js openwa baileys fluxer
evolution-api waha odoo twenty-main erpnext chatwoot novu listmonk mautic nocodb tooljet appsmith
budibase cal.diy whatsmeow compai-crm typebot
scrapling scrapy crawlee crawlee-python scrapely playwright puppeteer selenium lightpanda searxng
changedetection archivebox yt-dlp instaloader snscrape agent-browser camofox-browser scrapydweb
fastmcp mcp-typescript-sdk mcp-python-sdk mcp-inspector mcp-use langchain-mcp-adapters
masterdnsvpn qdrant milvus faiss chroma pgvector turbovec loguru langfuse mlflow opik phoenix
rtk headroom repomix tree-sitter semgrep ast-grep codegraph codebase-memory-mcp gitnexus cli
duckdb marimo polars llmfit nextcloud-server
ui ant-design mui react-bits swr heroui lucide magicui radix-primitives daisyui tailwindcss normalize.css
three.js animejs motion react-three-fiber gsap excalidraw penpot tldraw plasmic
umami posthog plausible matomo superset grafana metabase redash recharts d3 chart-js echarts uplot
gradio streamlit dash osiris label-studio opencv supervision face-recognition
ffmpeg moviepy opencut obs-studio lossless-cut openscreen hyperframes manim remotion manim-community
pandoc pdf-inspector youtube2webpage ocrmypdf tesseract stirling-pdf pdfcraft pdfding slidev reveal.js
marp mermaid agent-desktop nodeterm agent-protocol sandbox
chartanalyst stocks-analyst intellitrader open-sol-bot crypto-trader binance-trader qlib machine-learning-for-trading
""")
LOCAL_MODELS = ids("""
self-hosted-ai-starter-kit cline goose llama-index deepagents smolagents pydantic-ai ag2 semantic-kernel
metagpt mercury-agent local-deep-research open-deep-research openclaude
crawl4ai scrapegraph-ai llm-scraper skyvern vane
cognee graphiti supermemory agentmemory ragflow litellm backdoor
vllm sglang tensorrt-llm unsloth transformers pytorch llama-factory peft trl
llms-from-scratch nanogpt nanochat llm.c how-to-train-your-gpt timesfm deepseek-coder cosmos nemotron
bionemo-recipes tensorflow train-llm-from-scratch warp
ollama llama-cpp localai exo llamafile open-webui jan cherry-studio textgen librechat anything-llm
private-gpt open-notebook chatbox transformers.js pythia
stable-diffusion-webui comfyui fooocus invokeai sd-webui-forge krita-ai-diffusion flux diffusers
controlnet sd-webui-controlnet comfyui-ipadapter-plus rembg gfpgan real-esrgan codeformer
deep-live-cam facefusion insightface liveportrait ultralytics sam2 segment-anything
whisper-cpp whisper faster-whisper whisperx nemo kokoro omnivoice-studio gpt-sovits vibevoice tts
voxcpm rvc fish-speech chatterbox index-tts cosyvoice supertonic luxtts wan2-2 hunyuanvideo ltx-video
wan2gp audiocraft ace-step-1.5 docling mineru marker paddleocr unlimited-ocr olmocr
""")
PROVIDER_CHOICE = ids("""
opencode openhands cline open-interpreter goose aider continue swe-agent open-swe langgraph langchain
autogen crewai llama-index agno dspy deepagents openai-agents-python smolagents haystack adk-python
pydantic-ai ag2 langgraph-supervisor-py mastra semantic-kernel vercel-ai agent-framework langgraphjs
sim dify langflow flowise openclaw hermes-agent ruflo deeptutor multica mercury-agent deer-flow
storm gpt-researcher nemo-agent-toolkit mirofish openevolve hermes-agent-self-evolution langchain4j
local-deep-research metagpt mimo-code open-deep-research openclaude opencode-legacy opencursor paperclip
rasa mem0 cognee graphiti supermemory agentmemory letta ragflow lightrag pageindex graphrag litellm
promptfoo deepeval ragas guardrails backdoor fabric lobehub odysseus khoj hermes-desktop surfsense
copilotkit screenshot-to-code openui assistant-ui onlook wrenai pandas-ai
daily-stock-analysis autohedge chartanalyst dexter finceptterminal intellitrader machine-learning-for-trading
open-sol-bot qlib quantharness stocks-analyst tradingagents
pipecat livekit-agents videolingo moneyprinterturbo ai-youtube-shorts-generator short-video-factory
pdfmathtranslate unstructured presenton
""")
API_REQUIRED = ids("""
whatsapp-agentkit arcads-claude-code social-media-research-skills skillspector
computer-use-preview llm-council e2b social-media-agent openai-python open-generative-ai videofy-minimal stitch-sdk
""")
MCP_SERVERS = ids("""
n8n-mcp context7 playwright-mcp chrome-devtools-mcp github-mcp-server blender-mcp serena
figma-context-mcp mcp-neo4j annas-mcp browser-harness codebase-memory-mcp davinci-resolve-mcp
""")
SUBSCRIPTIONS = {
    "t3code": ("claude_code", "codex"), "goose": ("claude_code", "codex"),
    "multica": ("claude_code", "codex"), "ruflo": ("claude_code", "codex"),
    "paperclip": ("claude_code", "codex"), "opencursor": ("claude_code", "codex"),
    "fabric": ("codex",), "openclaude": ("codex",), "pageindex": ("claude_code",),
    "claude-mem": ("claude_code", "codex"),
}
HOST_OVERRIDES = {
    "graphify": ("claude_code", "codex"), "codegraph": ("claude_code", "codex"),
    "gitnexus": ("claude_code", "codex"), "mempalace": ("claude_code",),
    "engram": ("claude_code", "codex"), "headroom": ("claude_code", "codex"),
    "rtk": ("claude_code",), "autoresearch": ("claude_code", "codex"),
    "ppt-master": ("claude_code", "codex"),
}
OPTIONAL_AI = ids("""
n8n activepieces windmill kestra trigger-dev typebot compai-crm twenty-main chatwoot tooljet appsmith
budibase crawl4ai changedetection archivebox headroom rtk graphify langfuse mlflow opik phoenix
markitdown marker docling open-design
""")
LOCAL_OR_REMOTE = ids("jan cherry-studio chatbox open-webui librechat anything-llm private-gpt open-notebook")
SPECIAL_NOTES = {
    "videofy-minimal": "El flujo documentado usa OPENAI_API_KEY y ELEVENLABS_API_KEY. La interfaz local no elimina esas llamadas remotas.",
    "open-generative-ai": "La aplicación utiliza MuAPI para generar medios. El código abierto no incluye el consumo de ese servicio.",
    "arcads-claude-code": "La skill funciona dentro del agente, pero las generaciones consumen la API de Arcads; la suscripción del agente no paga Arcads.",
    "social-media-research-skills": "El modelo lo aporta tu agente; las consultas de datos requieren acceso a ScrapeCreators por separado.",
    "skillspector": "El escaneo con LLM documenta proveedores con API key. Una propuesta de añadir Ollama no demuestra soporte local implementado.",
    "e2b": "La clave E2B_API_KEY da acceso al servicio de sandboxes, con sus propios límites y tarifas; el modelo se configura aparte.",
    "whatsapp-agentkit": "La plantilla pide una clave de Anthropic para el bot. Usar Claude Code para construirlo no sustituye la autenticación del bot.",
    "computer-use-preview": "Este repositorio demuestra computer use con Gemini y requiere su API key; el nombre no implica una integración de OpenAI.",
    "codex-plugin-cc": "Claude Code aloja el plugin y Codex utiliza su propia cuenta o API key. Cada sesión conserva los límites de su proveedor.",
    "pageindex": "El proyecto documenta usar Claude Code con una suscripción o una API key. La modalidad cloud de PageIndex tiene requisitos propios.",
    "fabric": "El proyecto documenta un backend de OAuth de Codex; es una integración del proyecto, no una garantía general para otras apps.",
    "notebooklm-py": "Cliente no oficial que reutiliza una sesión de Google/NotebookLM. No es un modelo local ni una API oficial incluida por Claude o Codex.",
    "notebooklm-mcp-cli": "Conecta un cliente MCP con una sesión de NotebookLM. El acceso y los límites los determina Google, además del agente que invoque las herramientas.",
    "edge-tts": "Usa un servicio de voz de Microsoft en línea. No pide una API key en su uso documentado, pero no funciona sin conexión ni garantiza disponibilidad futura.",
    "annas-mcp": "El proyecto documenta requisitos de acceso a la API de Anna's Archive; no asumir acceso ilimitado por conectar un cliente MCP.",
    "context7": "El cliente MCP usa su propio modelo. Context7 recomienda una API key y aplica límites o planes al servicio de documentación.",
    "figma-context-mcp": "Requiere credenciales y acceso al archivo de Figma. La clave de Figma no es una clave de un LLM.",
    "github-mcp-server": "Requiere autenticación y permisos de GitHub. La IA que decide las acciones pertenece al cliente MCP.",
    "blender-mcp": "Controlar Blender y generar modelos en servicios externos son rutas distintas: los proveedores de generación pueden cobrar.",
    "davinci-resolve-mcp": "Necesita DaVinci Resolve instalado y su API de scripting; algunas funciones dependen de la edición de Resolve.",
    "palmier-pro": "Las versiones actuales distribuyen binarios propietarios; el código abierto conservado es histórico. Las funciones de IA pueden tener servicios adicionales.",
    "remotion": "El renderizado de React no requiere una API de IA. Revisar la licencia de Remotion para el tamaño del equipo y el uso comercial.",
    "self-hosted-ai-starter-kit": "La receta incluye Ollama y servicios locales. Las integraciones añadidas a n8n pueden introducir cuentas o APIs externas.",
    "stitch-sdk": "La ruta documentada necesita STITCH_API_KEY del servicio de Google. Verificar sus cuotas y condiciones; la sesión de Claude Code o Codex no sustituye esa credencial.",
    "compai-crm": "El README permite prescindir de fuentes externas de investigación. Confirmar por separado el agente y proveedor que ejecutará las tareas.",
}

# Editorially selected entry commands. A README mention by itself is insufficient:
# it may be a prerequisite, sponsor, example, deprecated method or a test command.
COMMANDS = {
    "claude-code":"winget install Anthropic.ClaudeCode", "codex":"npm install -g @openai/codex",
    "gemini-cli":"npx @google/gemini-cli", "t3code":"npx t3@latest",
    "cline":"npm i -g cline", "langgraph":"pip install -U langgraph", "langchain":"uv add langchain",
    "llama-index":"pip install llama-index", "dspy":"pip install dspy", "deepagents":"uv add deepagents",
    "openai-agents-python":"pip install openai-agents", "haystack":"pip install haystack-ai",
    "adk-python":"pip install google-adk", "ag2":"pip install ag2",
    "langgraph-supervisor-py":"pip install langgraph-supervisor", "mastra":"npm create mastra@latest",
    "semantic-kernel":"pip install semantic-kernel", "vercel-ai":"npm install ai",
    "agent-framework":"pip install agent-framework", "langgraphjs":"npm install @langchain/langgraph @langchain/core",
    "flowise":"npm install -g flowise", "langflow":"pip install langflow",
    "openclaw":"npm install -g openclaw@latest", "ruflo":"npm install -g ruflo@latest",
    "gpt-researcher":"pip install gpt-researcher", "composio":"pip install composio",
    "e2b":"pip install e2b-code-interpreter", "nemo-agent-toolkit":"pip install nvidia-nat",
    "openevolve":"pip install openevolve", "firecrawl":"pip install firecrawl",
    "scrapling":"pip install scrapling", "crawl4ai":"pip install crawl4ai", "scrapy":"pip install scrapy",
    "crawlee":"npx crawlee create", "scrapely":"pip install scrapely", "scrapegraph-ai":"pip install scrapegraphai",
    "puppeteer":"npm i puppeteer", "skyvern":"pip install skyvern", "archivebox":"pip install archivebox",
    "fastmcp":"uv add fastmcp", "mcp-python-sdk":"pip install \"mcp[cli]\"",
    "mcp-inspector":"npx @modelcontextprotocol/inspector", "langchain-mcp-adapters":"pip install langchain-mcp-adapters",
    "playwright-mcp":"npx @playwright/mcp@latest", "blender-mcp":"uvx blender-mcp",
    "mem0":"pip install mem0ai", "cognee":"pip install cognee", "graphiti":"pip install graphiti-core",
    "chroma":"pip install chromadb", "vllm":"pip install vllm", "loguru":"pip install loguru",
    "opik":"pip install opik", "deepeval":"pip install -U deepeval", "ragas":"pip install ragas",
    "phoenix":"pip install arize-phoenix", "repomix":"npx repomix", "graphify":"pipx install graphify",
    "gitnexus":"npm install -g gitnexus", "semgrep":"pip install semgrep", "peft":"pip install peft",
    "trl":"pip install trl", "openai-python":"pip install openai", "marimo":"pip install marimo",
    "polars":"pip install polars", "llmfit":"uv tool install -U llmfit", "open-webui":"pip install open-webui",
    "ant-design":"npm install antd", "heroui":"npm install @heroui/styles @heroui/react",
    "normalize.css":"npm install --save normalize.css", "motion":"npm install motion", "gsap":"npm install gsap",
    "tldraw":"npm i tldraw", "assistant-ui":"npx assistant-ui@latest init",
    "stitch-sdk":"npm install @google/stitch-sdk", "impeccable":"npx impeccable",
    "wrenai":"pip install wrenai", "pandas-ai":"pip install pandasai", "gradio":"pip install --upgrade gradio",
    "streamlit":"pip install streamlit", "ultralytics":"pip install ultralytics", "supervision":"pip install supervision",
    "label-studio":"pip install label-studio", "whisper":"pip install -U openai-whisper",
    "faster-whisper":"pip install faster-whisper", "whisperx":"pip install whisperx", "kokoro":"pip install kokoro",
    "tts":"pip install TTS", "voxcpm":"pip install voxcpm", "chatterbox":"pip install chatterbox-tts",
    "supertonic":"pip install supertonic", "pipecat":"pip install pipecat-ai", "moviepy":"pip install moviepy",
    "hyperframes":"npx hyperframes init my-video", "skills-remotion":"npx skills add remotion-dev/skills",
    "manim":"pip install manimgl", "remotion":"npx create-video@latest", "docling":"pip install docling",
    "markitdown":"pip install markitdown", "marker":"pip install marker-pdf", "pdf-inspector":"pip install pdf-inspector",
    "unstructured":"pip install \"unstructured[all-docs]\"", "olmocr":"pip install olmocr",
    "pdfmathtranslate":"pip install pdf2zh", "ppt-master":"npx skills add hugohe3/ppt-master",
    "autoskills":"npx autoskills", "social-media-research-skills":"npx skills add ScrapeCreators/social-media-research-skills",
    "superclaude-framework":"pipx install superclaude", "agent-desktop":"npm install -g agent-desktop",
    "local-deep-research":"pip install local-deep-research", "metagpt":"pip install --upgrade metagpt",
    "openclaude":"npm install -g @twigpine/openclaude@latest", "agent-browser":"npm install -g agent-browser",
    "scrapydweb":"pip install scrapydweb", "rtk":"winget install rtk-ai.rtk", "tensorflow":"pip install tensorflow",
    "warp":"pip install warp-lang", "transformers.js":"npm i @huggingface/transformers", "edge-tts":"pip install edge-tts",
    "whatsapp-web-js":"npm install whatsapp-web.js", "marketingskills":"npx skills add coreyhaines31/marketingskills",
    "taste-skill":"npx skills add https://github.com/Leonxlnx/taste-skill --skill \"design-taste-frontend\"",
}

START = {
    "codex": (["Una cuenta con acceso a Codex o una API key; Node.js y npm si utilizas el comando mostrado."], ["Instala Codex CLI o elige una distribución oficial para tu sistema.", "Abre Codex y elige sesión de ChatGPT o autenticación con API key; comprueba cuál está activa.", "Abre una carpeta de prueba y pide una tarea pequeña antes de ampliar los permisos o la automatización."]),
    "claude-code": (["Un sistema compatible y acceso a Claude Code mediante plan o API, según la ruta elegida."], ["Sigue el instalador oficial para tu sistema; el comando mostrado corresponde a Windows.", "Ejecuta Claude Code y autentícate con el plan o con la cuenta de API que quieras consumir.", "Abre un proyecto de prueba y comprueba el método de acceso antes de trabajar con tareas largas."]),
    "n8n": (["n8n Cloud o un entorno para el despliegue propio indicado en su documentación."], ["Elige servicio gestionado o despliegue propio; son instalaciones y costes diferentes.", "Crea un primer workflow con un disparador y una acción sin IA.", "Añade un nodo de modelo solo si lo necesitas y configura su proveedor o el backend local correspondiente."]),
    "self-hosted-ai-starter-kit": (["Docker y recursos para los contenedores y el modelo que elijas."], ["Abre la configuración de Docker Compose y el perfil de CPU o GPU del README.", "Prepara las variables del ejemplo y descarga un modelo compatible en Ollama.", "Comprueba un flujo mínimo de n8n y sus conexiones antes de añadir servicios externos."]),
    "ollama": (["Equipo compatible con el modelo elegido y espacio para sus pesos."], ["Instala el motor de Ollama para tu sistema desde la fuente oficial.", "Elige un modelo que quepa en la memoria del equipo y sigue su descarga y primer chat.", "Conecta una interfaz como Open WebUI solo cuando hayas comprobado la inferencia local del motor."]),
    "open-webui": (["Python o Docker según la instalación elegida, y un proveedor o motor de modelos."], ["Elige la instalación con paquete o contenedor que documenta el README.", "Configura un backend, por ejemplo un motor local compatible o un proveedor remoto.", "Prueba una conversación y confirma dónde se ejecuta el modelo antes de cargar documentos."]),
    "jan": (["Sistema operativo y memoria compatibles con la distribución y el modelo."], ["Descarga la aplicación para tu sistema desde su fuente oficial.", "Configura un modelo local compatible o una conexión remota, según la ruta que quieras usar.", "Prueba una conversación pequeña y revisa dónde se guardan los datos y qué backend está activo."]),
    "docling": (["Un entorno Python con las dependencias indicadas por el proyecto."], ["Instala la biblioteca en el entorno de tu proyecto.", "Ejecuta la conversión de un PDF o documento pequeño siguiendo el ejemplo del README.", "Revisa el texto, tablas y orden de lectura del resultado antes de procesar un lote."]),
    "whisper-cpp": (["Compilador o binario compatible, y un modelo Whisper de la variante seleccionada."], ["Elige el binario o la compilación para tu sistema según el README.", "Prepara un modelo y un audio de muestra en los formatos del ejemplo.", "Ejecuta la transcripción y mide calidad y tiempo en tu propio equipo."]),
    "faster-whisper": (["Python y las dependencias de CPU o GPU correspondientes a la ruta elegida."], ["Instala la biblioteca en un entorno aislado.", "Selecciona modelo, dispositivo y precisión siguiendo el ejemplo del README.", "Transcribe un audio corto y revisa el texto y el consumo de memoria antes de procesar material largo."]),
    "kokoro": (["Python, los pesos y las dependencias de audio e idioma de la variante elegida."], ["Instala la biblioteca y prepara las dependencias que indica su README.", "Elige idioma y voz de los ejemplos disponibles.", "Sintetiza un texto breve y escucha el resultado antes de generar una narración completa."]),
    "edge-tts": (["Python y conexión a internet."], ["Instala edge-tts en un entorno Python o mediante la ruta de CLI del README.", "Elige una voz disponible en el servicio.", "Sintetiza un texto de prueba y guarda el audio; recuerda que esta ruta llama a un servicio en línea."]),
    "remotion": (["Node.js y el gestor de paquetes indicado por el proyecto."], ["Crea un proyecto de video con el comando documentado.", "Abre una composición sencilla y ajusta el contenido y la duración.", "Prueba el renderizado local y revisa la licencia antes de una integración comercial o un servicio de render."]),
    "ppt-master": (["Un agente compatible y el entorno Python de la ruta documentada."], ["Añade la skill o abre las instrucciones del proyecto en tu agente.", "Entrega un documento fuente y especifica audiencia, contenido y formato de la presentación.", "Genera un PPTX editable y ábrelo para revisar contenido y diseño. Las generaciones externas de imágenes se configuran por separado."]),
    "agent-browser": (["Una distribución compatible de la CLI y su navegador."], ["Instala la CLI siguiendo la ruta del README.", "Prepara el navegador que utiliza la distribución instalada.", "Abre una página de prueba, toma un snapshot y comprueba una acción sobre una referencia de elemento."]),
    "n8n-mcp": (["Un cliente MCP; una instancia de n8n y sus permisos solo si quieres administrarla."], ["Elige el servidor gestionado o la instalación local según el README.", "Añade su URL o comando a la configuración MCP del cliente.", "Comprueba una consulta de documentación. Configura por separado la instancia y credenciales de n8n para operaciones sobre workflows."]),
    "context7": (["Un cliente MCP y el acceso a Context7 que requiera la ruta elegida."], ["Elige el servidor remoto o la configuración documentada para tu cliente.", "Configura la API key recomendada y comprueba los límites de tu plan si la necesitas.", "Consulta la documentación de una librería concreta y verifica que la respuesta corresponde a su versión."]),
    "comfyui": (["Python o una distribución preparada, modelos compatibles y hardware suficiente."], ["Elige la distribución para tu sistema y la ruta de CPU o GPU del README.", "Prepara los pesos y el workflow de ejemplo correspondiente.", "Genera una imagen pequeña y comprueba memoria, resultado y licencias de los modelos antes de ampliar el flujo."]),
}

READY_APPS=ids("jan chatbox cherry-studio lossless-cut obs-studio openscreen pdfcraft excalidraw opencut hermes-desktop")
ENTRY_URLS={
    "jan":"https://jan.ai/", "chatbox":"https://chatboxai.app/", "cherry-studio":"https://cherryai.com/download",
    "lossless-cut":"https://github.com/mifi/lossless-cut/releases", "obs-studio":"https://obsproject.com",
    "openscreen":"https://github.com/siddharthvaddem/openscreen/releases", "pdfcraft":"https://pdfcraft.devtoolcafe.com/en/",
    "excalidraw":"https://excalidraw.com", "opencut":"https://opencut.app", "hermes-desktop":"https://hermesone.org",
}
START.update({
    "chatbox": (["Un sistema compatible y una ruta de acceso a un modelo."], ["Abre las descargas oficiales y elige el instalador para tu sistema.", "Inicia la aplicación y elige el servicio de Chatbox, una API propia o la conexión local que documente la configuración.", "Envía un mensaje breve y confirma qué proveedor y cuenta se están consumiendo."]),
    "cherry-studio": (["Un sistema compatible y el proveedor o modelo que vayas a configurar."], ["Abre la descarga de escritorio indicada por el autor e instala la versión de tu sistema.", "Sigue la guía de inicio para añadir un proveedor; comprueba por separado API, modelos descargados y permisos.", "Prueba una conversación pequeña antes de activar conectores o importar documentos."]),
    "lossless-cut": (["Un archivo de video de prueba y una distribución compatible con tu sistema."], ["Elige la descarga oficial para tu sistema; el README distingue las tiendas de pago y los ejecutables gratuitos de GitHub.", "Abre una copia de un video y marca el comienzo y final del fragmento que quieres conservar.", "Exporta un fragmento y comprueba imagen, sonido y puntos de corte antes de trabajar con el original."]),
    "obs-studio": (["Un sistema compatible y una fuente de imagen o sonido que quieras grabar."], ["Abre la web oficial de OBS y elige la descarga para tu sistema.", "Sigue la guía del proyecto para añadir una fuente de captura y revisar la entrada de audio.", "Graba unos segundos sin transmitir y reproduce el archivo para comprobar imagen y sonido."]),
    "openscreen": (["Una distribución para tu sistema y los permisos de captura que pida la aplicación."], ["Abre Releases y elige el instalador correspondiente a tu sistema; el README también documenta gestores de paquetes.", "Configura una captura pequeña y comprueba qué permisos de pantalla y audio necesita.", "Graba unos segundos, revisa la edición y exporta una muestra antes de una grabación larga."]),
    "pdfcraft": (["Un navegador compatible y un PDF de prueba."], ["Abre la web enlazada por el README para probar la interfaz sin desplegar el código.", "Elige una operación sencilla, por ejemplo combinar o dividir archivos, y utiliza documentos de prueba.", "Descarga y abre el resultado. El despliegue propio con Node o Docker es una ruta distinta que requiere preparación técnica."]),
    "excalidraw": (["Un navegador y una idea de diagrama."], ["Abre excalidraw.com, la aplicación web enlazada por el proyecto.", "Dibuja unas formas y añade etiquetas para probar el editor.", "Exporta una imagen o guarda el dibujo. Instalar el paquete npm solo hace falta si vas a integrarlo en una aplicación propia."]),
    "opencut": (["Un navegador y un clip pequeño de prueba."], ["Abre opencut.app para probar la versión clásica; el README indica que este repositorio está en reescritura.", "Usa un clip de prueba para comprobar el flujo de edición disponible en esa versión.", "Revisa la exportación y sus límites. Preparar el nuevo código desde fuente es una ruta de desarrollo diferente."]),
    "hermes-desktop": (["Un sistema compatible y el proveedor que usará Hermes Agent."], ["Abre las descargas de Hermes One indicadas por el proyecto y revisa compatibilidad y procedencia de la distribución.", "Sigue el asistente para instalar o conectar Hermes y elegir el proveedor; la interfaz no incluye automáticamente acceso a los modelos.", "Prueba una conversación y una herramienta sencilla antes de habilitar conectores, tareas periódicas o datos reales."]),
})


def profile(repo: dict, detail: dict, source: dict, text: str) -> dict:
    rid = repo["id"]
    role = repo.get("role")
    reference = role == "directory"
    access = {
        "mode": "reference" if reference else "agent_extension" if role == "skill" else "software",
        "api": "depends", "local_model": "not_documented", "claude_code": "not_documented",
        "codex": "not_documented", "cost": "choice", "hardware": "unknown",
        "scope": "Ruta básica del proyecto; las funciones opcionales se revisan aparte.",
        "api_note": "El proveedor y la función elegidos determinan si hacen falta credenciales de IA.",
        "subscription_note": "El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.",
        "local_note": "No se confirma un backend local solo porque la aplicación se instale en tu equipo.",
        "cost_note": "Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.",
        "hardware_note": "Consultar los requisitos del README y de los componentes que actives.",
        "checked_at": "2026-11-14", "review": "documented", "sources": [source["url"]],
        "source_blob_sha": source["blob_sha"],
    }
    if reference:
        access.update(api="not_required", local_model="not_applicable", cost="no_model_fee", hardware="ordinary",
                      scope="Leer el material y elegir ejemplos; ejecutar un ejemplo es una decisión posterior.",
                      api_note="Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.",
                      local_note="Leer una referencia no ejecuta un modelo.",
                      cost_note="La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.")
    if rid in NO_AI:
        access.update(api="not_required", local_model="not_applicable", cost="no_model_fee", hardware="ordinary",
                      api_note="La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.",
                      local_note="La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.",
                      cost_note="Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.")
    if rid in PROVIDER_CHOICE and rid not in NO_AI:
        access.update(api="depends", local_model="not_documented", cost="choice", hardware="model_dependent",
                      api_note="Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.",
                      hardware_note="Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.")
    if rid in LOCAL_MODELS:
        access.update(local_model="supported", hardware="model_dependent",
                      local_note="La ruta local está documentada; hay que instalar o descargar un modelo compatible.",
                      hardware_note="El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.")
        if rid not in PROVIDER_CHOICE:
            access.update(api="not_required", cost="no_model_fee",
                          api_note="La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.",
                          cost_note="No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.")
    if rid in OPTIONAL_AI:
        access.update(api="optional", cost="choice",
                      api_note="La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.")
    if rid in LOCAL_OR_REMOTE:
        access.update(api="optional",cost="choice",
                      api_note="Puedes elegir la ruta local documentada o configurar un proveedor remoto; la ruta remota puede requerir API key o acceso propio.",
                      cost_note="La inferencia local consume recursos de tu equipo. Los proveedores remotos y servicios del cliente tienen sus propios planes y tarifas.")
    if role == "skill":
        access.update(api="not_required", cost="host_plan", hardware="ordinary", local_model="not_applicable",
                      api_note="Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales.",
                      subscription_note="Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.",
                      cost_note="No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación.",
                      local_note="Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión.")
        if "claude code" in text.lower() or "claude-code" in (repo.get("agent_tools") or []):
            access["claude_code"] = "host"
        if re.search(r"\bcodex\b", text, re.I) or "codex" in (repo.get("agent_tools") or []):
            access["codex"] = "host"
    if rid in API_REQUIRED:
        access.update(api="required", cost="usage_based", local_model="not_documented",
                      api_note="La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.",
                      cost_note="Revisar el plan, créditos, cuotas y facturación del proveedor antes de ejecutar.")
    if rid in {"e2b", "social-media-research-skills"}:
        access.update(api="not_required", cost="usage_based",
                      api_note="La clave exigida es de un servicio externo. No es una API de un modelo de lenguaje; el agente o aplicación que use sus datos tiene su propio acceso a IA.")
    if rid in MCP_SERVERS:
        access.update(mode="agent_extension", api="not_required", cost="host_plan", local_model="not_applicable",
                      claude_code="connector", codex="connector",
                      api_note="El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios.",
                      subscription_note="Puede conectarse a un cliente con soporte MCP, incluido Claude Code o Codex. Debes configurar el servidor y sus permisos.",
                      local_note="Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta.",
                      cost_note="El modelo se consume en el cliente. Los servicios que la herramienta consulta pueden tener cuentas o tarifas propias.")
    for client in HOST_OVERRIDES.get(rid, ()):
        access[client] = "host"
    if rid in HOST_OVERRIDES and rid not in {"graphify", "headroom", "rtk", "codegraph", "gitnexus"}:
        access.update(api="not_required", cost="host_plan")
    for client in SUBSCRIPTIONS.get(rid, ()):
        access[client] = "project_integration"
    if rid in SUBSCRIPTIONS:
        access.update(api="optional", cost="choice",
                      subscription_note="El README documenta una integración con las sesiones de los agentes indicados. Configurar esa ruta y comprobar sus límites; otras rutas pueden facturar por API.")
    if rid in {"codex", "claude-code"}:
        client = "codex" if rid == "codex" else "claude_code"
        official = "https://learn.chatgpt.com/docs/auth" if rid == "codex" else "https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan"
        access.update(api="optional", cost="choice", hardware="ordinary", **{client: "native"},
                      subscription_note="La sesión oficial del plan y una API key son rutas de autenticación distintas. Elegir una y consultar los límites del plan.",
                      api_note="Puede utilizarse con sesión del plan compatible o con API key; no son la misma facturación.")
        access["sources"].append(official)
    if rid in {"notebooklm-py", "notebooklm-mcp-cli", "edge-tts"}:
        access.update(api="not_required", cost="choice", local_model="not_documented", hardware="ordinary",
                      api_note="La ruta documentada usa un servicio en línea mediante sesión o acceso propio; no implica ejecución local del modelo.")
    if rid in {"annas-mcp", "context7", "figma-context-mcp", "github-mcp-server", "blender-mcp"}:
        access["cost"] = "choice"
    if rid in {"codex-chatgpt-web"}:
        access.update(api="unconfirmed", cost="unconfirmed", local_model="unconfirmed", review="pending",
                      api_note="No se da por verificada la autenticación o el coste real de esta integración de terceros.",
                      subscription_note="Consultar la procedencia, el método de sesión y la documentación actual antes de introducir credenciales.")
    if rid in SPECIAL_NOTES:
        access["cost_note"] = SPECIAL_NOTES[rid]
    other={
        "gemini-cli":"El README documenta acceso con una cuenta de Google mediante OAuth y rutas con API key. Consultar las cuotas del método elegido.",
        "hermes-agent":"El proyecto documenta una suscripción propia de Nous Portal además de otros proveedores; los servicios incluidos y sus límites pertenecen a ese plan.",
        "goose":"El README también documenta proveedores ACP para utilizar acceso de Gemini, además de APIs y modelos locales.",
        "t3code":"El README lista otros agentes y adaptadores ACP. T3 Code coordina esos agentes; cada uno conserva su autenticación y sus límites.",
        "mimo-code":"El README documenta acceso al proveedor Xiaomi MiMo con OAuth o configuración del proveedor. No equivale a usar un plan de Claude o Codex.",
        "open-design":"El servicio ofrece sus propios planes y rutas de API. Consultar las condiciones de OpenDesign por separado del plan del agente que lo conecte.",
    }
    if rid in other:access['other_access']=other[rid]
    if rid in {"chartanalyst", "stocks-analyst", "intellitrader", "open-sol-bot", "crypto-trader", "binance-trader", "qlib", "machine-learning-for-trading"}:
        access["cost_note"] = "La ruta básica no exige un LLM. Exchanges, brokers, datos de mercado y ejecución real pueden requerir cuentas, tarifas o fondos; los ejemplos no acreditan rentabilidad."
    return access


def onboarding(repo: dict, detail: dict, source: dict, text: str, access: dict) -> dict:
    role=repo.get("role")
    kind="reference" if role=="directory" else "skill" if role=="skill" else "mcp" if repo['id'] in MCP_SERVERS else "source"
    prerequisites=[]
    if kind=="skill":
        prerequisites=["Un agente compatible y acceso activo a su modelo."]
        steps=["Elige el agente indicado en Acceso y costes.", "Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.", "Prueba una tarea pequeña y revisa si activa conectores externos."]
    elif kind=="reference":
        steps=["Abre el material original y elige un capítulo o ejemplo.", "Revisa los requisitos de ese ejemplo antes de instalar dependencias.", "Usa las alternativas y recetas para situarlo dentro de tu proyecto."]
    elif kind=="mcp":
        prerequisites=["Un cliente MCP compatible.","Las credenciales del servicio conectado, si las pide el servidor."]
        steps=["Instala o configura el servidor según su README.","Añade su comando o URL en la configuración MCP de tu cliente.","Comprueba que aparecen las herramientas antes de asignar una tarea."]
    else:
        steps=["Elige la ruta del README: paquete, aplicación o despliegue desde fuente.","Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.","Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto."]
    if repo['id'] in START:
        prerequisites,steps=START[repo['id']]
    candidate=COMMANDS.get(repo['id'], '')
    command=candidate if candidate and candidate in text else ''
    if kind=="reference": command=""
    if repo.get("status")=="unverified": command="";kind="review"
    audience = "ready_app" if repo['id'] in READY_APPS else "agent" if kind in {'skill','mcp'} else "reading" if kind=='reference' else "developer" if role=='library' else "setup"
    entry_url=ENTRY_URLS.get(repo['id'], '')
    if entry_url and entry_url not in text:raise ValueError(f"Entry URL missing from source: {repo['id']}")
    return {"kind":kind,"audience":audience,"entry_url":entry_url,"prerequisites":prerequisites,"steps":steps,"command":command,
            "command_status":"documented" if command else "readme","source":source["url"],
            "note":"Comando presente en el README revisado; no es una prueba de instalación." if command else "Consulta la ruta exacta en la fuente. No se adivina el nombre del paquete ni se presenta clonar como una instalación completa.",
            "checked_at":"2026-11-14"}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--apply",action="store_true");args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    compact=json.loads((root/'INDICE_IA.json').read_text(encoding='utf8'))
    detail=json.loads((root/'INDICE_IA.detalle.json').read_text(encoding='utf8'))
    audit={r['id']:r for r in json.loads((root/'data/reports/access-source-audit.json').read_text(encoding='utf8'))}
    counts=Counter()
    for repo in compact['repos']:
        if not repo.get('gh') or repo.get('alias_of'):continue
        rid=repo['id'];d=detail['repos'][rid];source=audit[rid]
        if source.get('error'):raise RuntimeError(f"Source unavailable: {rid}")
        text=(root/'data/extracted'/rid/'readme.md').read_text(encoding='utf8')
        a=profile(repo,d,source,text);d['access']=a;d['getting_started']=onboarding(repo,d,source,text,a)
        repo['routes']=access_routes(d)
        counts[a['api']]+=1
    compact['meta']['access_checked']='2026-11-14'
    compact['meta']['fields']['access']='Acceso por ruta en INDICE_IA.detalle.json: API de IA, modelos locales, clientes, coste, equipo y fuentes.'
    if args.apply:
        for name,data in [('INDICE_IA.json',compact),('INDICE_IA.detalle.json',detail)]:
            (root/name).write_text(json.dumps(data,ensure_ascii=False,indent=1)+'\n',encoding='utf8')
    print('Access profiles:',dict(counts),'applied:',args.apply)


if __name__=='__main__':main()
