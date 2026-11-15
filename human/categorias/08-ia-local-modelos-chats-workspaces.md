[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Chats, modelos locales y espacios privados

Motores locales, chats y workspaces. Tener la interfaz en tu equipo no garantiza que el modelo sea local: comprueba su backend y los requisitos de cada ficha.

28 repos · 4 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Ollama](../fichas/ollama.md) | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. | Sin API de IA en la ruta básica |
| [Open WebUI](../fichas/open-webui.md) | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. | API de IA opcional |
| [Jan](../fichas/jan.md) | Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. | API de IA opcional |
| [AnythingLLM](../fichas/anything-llm.md) | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. | API de IA opcional |
| [SurfSense](../fichas/surfsense.md) | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. | Depende de la ruta elegida |

## Secciones

- [Motores para correr modelos en local](#motores-para-correr-modelos-en-local) — 10 repos
- [Interfaces de chat auto-hospedadas](#interfaces-de-chat-auto-hospedadas) — 7 repos
- [Workspaces privados y segundos cerebros](#workspaces-privados-y-segundos-cerebros) — 7 repos
- [NotebookLM: alternativas y clientes](#notebooklm-alternativas-y-clientes) — 4 repos

## Motores para correr modelos en local

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Ollama](../fichas/ollama.md) | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. | quieres modelos locales funcionando en minutos | Sin API de IA en la ruta básica |
| [llama.cpp](../fichas/llama-cpp.md) | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. | quieres el máximo control y rendimiento local | Sin API de IA en la ruta básica |
| [LocalAI](../fichas/localai.md) | Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria. | quieres una API tipo OpenAI local para varias modalidades | Sin API de IA en la ruta básica |
| [exo](../fichas/exo.md) | Ejecuta modelos grandes repartiéndolos entre varios equipos de tu casa u oficina. | tienes varios equipos y quieres correr un modelo grande | Sin API de IA en la ruta básica |
| [airllm](../fichas/airllm.md) | Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes. | buscas esta función: Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes. | Sin API de IA en la ruta básica |
| [llmfit](../fichas/llmfit.md) | Herramienta para evaluar y medir el "fit" y la calidad de LLMs en una tarea concreta, orientada a comparar modelos con datos. | necesitas elegir modelo con datos y reproducibilidad | Sin API de IA en la ruta básica |
| [llamafile](../fichas/llamafile.md) | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. | quieres repartir un modelo que funcione con doble clic | Sin API de IA en la ruta básica |
| [FreeToken](../fichas/freetoken.md) | Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del proyecto. | buscas esta función: Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del proyecto. | Sin API de IA en la ruta básica |
| [transformers.js](../fichas/transformers-js.md) | Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript. | quieres ejecutar un modelo compatible dentro del navegador | Sin API de IA en la ruta básica |
| [magnitude](../fichas/magnitude.md) | Motor de inferencia local que adapta su ejecución al hardware y ofrece conexiones para agentes y aplicaciones. | buscas esta función: Motor de inferencia local que adapta su ejecución al hardware y ofrece conexiones para agentes y aplicaciones. | Sin API de IA en la ruta básica |

## Interfaces de chat auto-hospedadas

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Open WebUI](../fichas/open-webui.md) | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. | necesitas un ChatGPT privado para tu equipo | API de IA opcional |
| [Jan](../fichas/jan.md) | Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. | quieres un ChatGPT local en tu escritorio | API de IA opcional |
| [LobeHub](../fichas/lobehub.md) | Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. | quieres un chat bonito y extensible con agentes | Depende de la ruta elegida |
| [Cherry Studio](../fichas/cherry-studio.md) | App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad. | quieres una app de escritorio multi-proveedor completa | API de IA opcional |
| [Text Generation WebUI](../fichas/textgen.md) | App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic. | quieres experimentar con muchos backends locales | Sin API de IA en la ruta básica |
| [LibreChat](../fichas/librechat.md) | Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada. | quieres todos los proveedores en un chat con SSO | API de IA opcional |
| [chatbox](../fichas/chatbox.md) | Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común. | quieres un cliente de escritorio que conecte varios modelos | API de IA opcional |

## Workspaces privados y segundos cerebros

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [AnythingLLM](../fichas/anything-llm.md) | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. | quieres RAG privado sin programar | API de IA opcional |
| [odysseus](../fichas/odysseus.md) | Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. | quieres operación privada todo-en-uno y aceptas operar la infra | Depende de la ruta elegida |
| [PrivateGPT](../fichas/private-gpt.md) | Capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP. | construyes un producto de IA que no puede enviar datos fuera | API de IA opcional |
| [Khoj](../fichas/khoj.md) | Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones. | quieres un asistente sobre tus notas personales | Depende de la ruta elegida |
| [server](../fichas/nextcloud-server.md) | Servidor de Nextcloud para almacenar y compartir archivos, contactos y calendarios en infraestructura propia. | necesitas una plataforma autoalojada para documentos y colaboración | Sin API de IA en la ruta básica |
| [Hermes Desktop](../fichas/hermes-desktop.md) | App de escritorio que envuelve al agente Hermes en una interfaz nativa. | usas Hermes Agent y prefieres una app de escritorio | Depende de la ruta elegida |
| [muse-spark](../fichas/muse-spark.md) | Proyecto de terceros que se presenta como un estudio de IA de escritorio; su afiliación y funciones no están verificadas. | solo deseas revisar su procedencia y código antes de evaluar el proyecto | API: por confirmar |

## NotebookLM: alternativas y clientes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [SurfSense](../fichas/surfsense.md) | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. | quieres un NotebookLM propio y con más fuentes | Depende de la ruta elegida |
| [open-notebook](../fichas/open-notebook.md) | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. | quieres NotebookLM privado y sin cuotas | API de IA opcional |
| [notebooklm-py](../fichas/notebooklm-py.md) | API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código. | automatizas el NotebookLM real y aceptas el riesgo de API no oficial | Sin API de IA en la ruta básica |
| [notebooklm-mcp-cli](../fichas/notebooklm-mcp-cli.md) | CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP. | integras NotebookLM con tu asistente MCP | Sin API de IA en la ruta básica |

## Recetas relacionadas

- [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md) — Tener chat, documentos y memoria de IA en tu propia máquina, sin enviar datos a terceros.
- [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md) — Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
