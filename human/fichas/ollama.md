[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 Ollama

> La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 187k | MIT | Go | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 85/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Ollama, motor para descargar y ejecutar modelos de lenguaje abiertos en tu equipo (macOS, Windows, Linux o Docker), de Ollama Inc. Licencia MIT. Es muy madura y popular (~187k estrellas, v0.40.x). Ofrece además modelos en su nube (Ollama Cloud), con cuenta y condiciones propias.

## ¿Qué hace?

Ejecuta modelos de su biblioteca, permite conversar con ellos (por ejemplo `ollama run gemma4`) y los sirve a otras aplicaciones. Con `ollama launch` conecta modelos a agentes como Claude Code, Codex, Copilot CLI, OpenCode u OpenClaw; así cambia el modelo del agente, pero no da acceso a modelos de Anthropic u OpenAI.

## ¿Cómo lo hace?

Está escrito en Go y declara llama.cpp como backend. Expone una API REST local en el puerto 11434 (por ejemplo `/api/chat`), es compatible con la API de OpenAI y tiene librerías oficiales para Python y JavaScript. Los modelos se importan y personalizan con un Modelfile. Los requisitos de RAM y GPU dependen del modelo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Open WebUI](open-webui.md) | Interfaz de chat tipo ChatGPT que se conecta a Ollama con `OLLAMA_BASE_URL`. | Ollama primero, o usa la imagen `:ollama` de Open WebUI que ya lo incluye; no instales los dos por separado si usas esa imagen. |
| [litellm](litellm.md) | LiteLLM trae los proveedores `ollama` y `ollama_chat` y pone los modelos locales detrás de la misma API compatible con OpenAI que los de la nube. | Ollama primero y luego declara sus modelos en la configuración de LiteLLM. |
| [crawl4ai](crawl4ai.md) | La extracción con LLM de Crawl4AI acepta modelos de Ollama (ejemplo `ollama/llama3.3`), así que puedes estructurar páginas sin API de pago. | Ollama con el modelo descargado antes de lanzar la extracción. |
| [Claude Code](claude-code.md) | `ollama launch claude` configura Claude Code para usar un modelo de Ollama. | Ollama primero con el modelo descargado; luego `ollama launch claude`. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (111). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[ag2](ag2.md) · [agentic-rag-for-dummies](agentic-rag-for-dummies.md) · [Agents Towards Production](agents-towards-production.md) · [AgentScope](agentscope.md) · [AI SDK (Vercel)](vercel-ai.md) · [ai-engineering-hub](ai-engineering-hub.md) · [Aider](aider.md) · [AnythingLLM](anything-llm.md) · [AppFlowy](appflowy.md) · [AutoGPT](autogpt.md) · [browser-use](browser-use.md) · [Budibase](budibase.md) · [CAMEL](camel.md) · [changedetection.io](changedetection.md) · [chatbox](chatbox.md) · [Cherry Studio](cherry-studio.md) · [Cline](cline.md) · [daily_stock_analysis](daily-stock-analysis.md) · [DeepSeek Harness (DSH)](deepseek-harness.md) · [DeepTutor](deeptutor.md) · [dexter](dexter.md) · [dify](dify.md) · [discord.js](discord-js.md) · [dograh](dograh.md) · [Fabric](fabric.md) · [FinceptTerminal](finceptterminal.md) · [fluxer](fluxer.md) · [garak](garak.md) · [goose](goose.md) · [gpt-researcher](gpt-researcher.md) · [Gradio](gradio.md) · [graphify](graphify.md) · [Haystack](haystack.md) · [Hermes Desktop](hermes-desktop.md) · [hermes-agent](hermes-agent.md) · [Home Assistant](home-assistant.md) · [huginn](huginn.md) · [Jan](jan.md) · [karakeep](karakeep.md) · [Kestra](kestra.md) · [Khoj](khoj.md) · [kotaemon](kotaemon.md) · [langchain4j](langchain4j.md) · [langchain](langchain.md) · [langflow](langflow.md) · [Letta](letta.md) · [LibreChat](librechat.md) · [LightRAG](lightrag.md) · [LiveKit Agents](livekit-agents.md) · [LlamaIndex](llama-index.md) · [llm-council](llm-council.md) · [llm-scraper](llm-scraper.md) · [llmfit](llmfit.md) · [LobeHub](lobehub.md) · [local-deep-research](local-deep-research.md) · [lumibot](lumibot.md) · [marimo](marimo.md) · [Mastra](mastra.md) · [Mattermost](mattermost.md) · [Meilisearch](meilisearch.md) · [Mercury Agent](mercury-agent.md) · [MetaGPT](metagpt.md) · [Microsoft Agent Framework](agent-framework.md) · [mini-swe-agent](mini-swe-agent.md) · [MiroFish](mirofish.md) · [MoneyPrinterTurbo](moneyprinterturbo.md) · [Nanobrowser](nanobrowser.md) · [Node-RED](node-red.md) · [odysseus](odysseus.md) · [OmniRoute](omniroute.md) · [onyx](onyx.md) · [Open Interpreter](open-interpreter.md) · [open-design](open-design.md) · [open-notebook](open-notebook.md) · [OpenClaw](openclaw.md) · [opencode-manager](opencode-manager.md) · [OpenCode](opencode.md) · [OpenCursor](opencursor.md) · [openevolve](openevolve.md) · [OpenLLMetry](openllmetry.md) · [OpenMAIC](openmaic.md) · [OpenViking](openviking.md) · [pdf-craft](pdf-craft.md) · [PDFMathTranslate](pdfmathtranslate.md) · [Phoenix](phoenix.md) · [Pipecat](pipecat.md) · [Presenton](presenton.md) · [PrivateGPT](private-gpt.md) · [Pydantic AI](pydantic-ai.md) · [Pythia](pythia.md) · [python-telegram-bot](python-telegram-bot.md) · [Qwen Code](qwen-code.md) · [RAGFlow](ragflow.md) · [Rocket.Chat](rocket-chat.md) · [Scrapegraph-ai](scrapegraph-ai.md) · [server](nextcloud-server.md) · [shannon](shannon.md) · [short-video-factory](short-video-factory.md) · [SillyTavern](sillytavern.md) · [Sim](sim.md) · [SiYuan](siyuan.md) · [Skyvern](skyvern.md) · [strix](strix.md) · [supermemory](supermemory.md) · [SurfSense](surfsense.md) · [TradingAgents](tradingagents.md) · [Unsloth](unsloth.md) · [Vane](vane.md) · [Weaviate](weaviate.md) · [whatsapp-web.js](whatsapp-web-js.md) · [whatsmeow](whatsmeow.md)

**Notas:** Alternativas (elige una): llama-cpp, localai, llamafile. Varios motores en la misma máquina compiten por GPU y memoria. Por defecto la API escucha solo en localhost: no la expongas sin autenticación.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.40.16 (2026-11-09) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ollama/ollama/blob/main/README.md) · [2](https://github.com/open-webui/open-webui/blob/main/README.md) · [3](https://docs.litellm.ai/docs/providers/ollama) · [4](https://github.com/unclecode/crawl4ai/blob/main/README.md)</sub>

## Ver similares

Grupo **Motores para correr LLM en local**: Ollama ocupa la posición 1 de 5 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Ollama** (esta ficha) ⭐ recomendado | 85 | Si quieres la forma más sencilla de descargar y servir modelos locales con API compatible. |
| 2 | [llama.cpp](llama-cpp.md) | 78 | Si necesitas el motor base con máximo control de cuantización, CPU/GPU y rendimiento. |
| 3 | [LocalAI](localai.md) | 72 | Si quieres un servidor compatible con OpenAI para texto, imagen y voz en un contenedor. |
| 4 | [llamafile](llamafile.md) | 53 | Si quieres distribuir un modelo como un solo ejecutable que funciona en cualquier sistema. |
| 5 | [KoboldCpp](koboldcpp.md) | 47 | Si quieres un ejecutable con interfaz para escritura creativa y rol sobre modelos GGUF. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Los modelos locales usan tu hardware; modelos Cloud y búsqueda web tienen autenticación y condiciones propias |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Las guías del autor documentan Claude Code y Codex CLI con backend Ollama; esto cambia el modelo y no aporta modelos Anthropic/OpenAI mediante su suscripción |
| Coste | El coste depende del proveedor o la ruta. Los modelos locales usan tu hardware; modelos Cloud y búsqueda web tienen autenticación y condiciones propias |
| Equipo | Preparación según la ruta elegida. Instalador oficial para tu sistema; RAM y disco adecuados al modelo |

Las guías del autor documentan Claude Code y Codex CLI con backend Ollama; esto cambia el modelo y no aporta modelos Anthropic/OpenAI mediante su suscripción

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador oficial para tu sistema
- RAM y disco adecuados al modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install ollama
```

Comando copiado literalmente de el README (sección «Python»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/ollama/ollama/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Ollama para mi objetivo y necesito pasos guiados. Lee https://github.com/ollama/ollama/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga un modelo pequeño y formula una pregunta antes de conectarlo a un agente.

**Qué comprobar:** Puedes identificar el modelo ejecutado y ver la respuesta en tu equipo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un LLM local
- Conectar un modelo local a Codex CLI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un LLM local; Conectar un modelo local a Codex CLI | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las guías del autor documentan Claude Code y Codex CLI con backend Ollama; esto cambia el modelo y no aporta modelos Anthropic/OpenAI mediante su suscripción

## Stack y modelos

- **Stack:** Instalador oficial para tu sistema; RAM y disco adecuados al modelo
- **Etiquetas:** `inference` `local` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [llama.cpp](llama-cpp.md) | 135k | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. |
| [LocalAI](localai.md) | 50.4k | Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria. |
| [llamafile](llamafile.md) | 26.6k | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. |

## Enlaces

- 🐙 GitHub: [ollama/ollama](https://github.com/ollama/ollama)
- 🌐 Web: <https://ollama.com>
- 🧪 Receta: [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md)
- 🧪 Receta: [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ollama/ollama/blob/main/README.md)
- [Fuente 2](https://docs.ollama.com/integrations/claude-code)
- [Fuente 3](https://docs.ollama.com/integrations/codex)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
