[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Chats, modelos locales y espacios privados

Motores locales, chats y workspaces. Tener la interfaz en tu equipo no garantiza que el modelo sea local: comprueba su backend y los requisitos de cada ficha.

26 repos · 4 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Ollama](../fichas/ollama.md) | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. | API de IA opcional |
| [Open WebUI](../fichas/open-webui.md) | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. | API de IA opcional |
| [Jan](../fichas/jan.md) | Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. | API de IA opcional |
| [AnythingLLM](../fichas/anything-llm.md) | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. | API de IA opcional |
| [SurfSense](../fichas/surfsense.md) | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. | Depende de la ruta elegida |

## Secciones

- [Motores para correr modelos en local](#motores-para-correr-modelos-en-local) — 10 repos
- [Interfaces de chat auto-hospedadas](#interfaces-de-chat-auto-hospedadas) — 7 repos
- [Workspaces privados y segundos cerebros](#workspaces-privados-y-segundos-cerebros) — 5 repos
- [NotebookLM: alternativas y clientes](#notebooklm-alternativas-y-clientes) — 4 repos

## Motores para correr modelos en local

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Ollama](../fichas/ollama.md) | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. | Tu objetivo encaja con estos ejemplos: Probar un LLM local; Conectar un modelo local a Codex CLI | API de IA opcional |
| [llama.cpp](../fichas/llama-cpp.md) | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. | Tu objetivo encaja con estos ejemplos: Servir un modelo en CPU; Comparar cuantizaciones de un mismo modelo | Sin clave propia de API de IA en la ruta básica |
| [LocalAI](../fichas/localai.md) | Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria. | Tu objetivo encaja con estos ejemplos: Ofrecer una API local a una aplicación; Probar texto o voz con distintos backends | Sin clave propia de API de IA en la ruta básica |
| [exo](../fichas/exo.md) | Ejecuta modelos grandes repartiéndolos entre varios equipos de tu casa u oficina. | Tu objetivo encaja con estos ejemplos: Compartir memoria entre equipos compatibles; Experimentar con inferencia distribuida local | Sin clave propia de API de IA en la ruta básica |
| [airllm](../fichas/airllm.md) | Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes. | Tu objetivo encaja con estos ejemplos: Estudiar inferencia por carga de capas; Probar un modelo que supera la VRAM disponible | Sin clave propia de API de IA en la ruta básica |
| [llmfit](../fichas/llmfit.md) | Inspector de hardware que estima qué modelos de lenguaje y cuantizaciones caben en tu CPU, RAM y GPU. | Tu objetivo encaja con estos ejemplos: Elegir un modelo antes de descargarlo; Comparar requisitos de dos cuantizaciones | Sin clave propia de API de IA en la ruta básica |
| [llamafile](../fichas/llamafile.md) | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. | Tu objetivo encaja con estos ejemplos: Distribuir una demo local de un LLM; Probar inferencia sin montar un servidor complejo | Sin clave propia de API de IA en la ruta básica |
| [FreeToken](../fichas/freetoken.md) | Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del proyecto. | Tu objetivo encaja con estos ejemplos: Experimentar con inferencia de modelos MoE; Evaluar un backend de aceleración local | Sin clave propia de API de IA en la ruta básica |
| [transformers.js](../fichas/transformers-js.md) | Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript. | Tu objetivo encaja con estos ejemplos: Clasificar texto en el navegador; Procesar audio o imágenes sin servidor de modelos externo | Sin clave propia de API de IA en la ruta básica |
| [magnitude](../fichas/magnitude.md) | Motor de inferencia local que adapta su ejecución al hardware y ofrece conexiones para agentes y aplicaciones. | Tu objetivo encaja con estos ejemplos: Servir un modelo local a Codex; Comparar backends de inferencia en tu equipo | Sin clave propia de API de IA en la ruta básica |

## Interfaces de chat auto-hospedadas

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Open WebUI](../fichas/open-webui.md) | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. | Tu objetivo encaja con estos ejemplos: Unificar chats de modelos locales; Crear una interfaz compartida para un equipo | API de IA opcional |
| [Jan](../fichas/jan.md) | Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. | Tu objetivo encaja con estos ejemplos: Conversar con un modelo privado; Comparar un modelo local con una API | API de IA opcional |
| [LobeHub](../fichas/lobehub.md) | Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. | Tu objetivo encaja con estos ejemplos: Organizar agentes para tareas de equipo; Conectar un agente de código a un espacio de trabajo | Depende de la ruta elegida |
| [Cherry Studio](../fichas/cherry-studio.md) | App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad. | Tu objetivo encaja con estos ejemplos: Comparar respuestas de varios modelos; Organizar una base documental de prueba | API de IA opcional |
| [Text Generation WebUI](../fichas/textgen.md) | App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic. | Tu objetivo encaja con estos ejemplos: Probar modelos GGUF sin una API remota; Servir un endpoint local para otra app | Sin clave propia de API de IA en la ruta básica |
| [LibreChat](../fichas/librechat.md) | Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada. | Tu objetivo encaja con estos ejemplos: Unificar proveedores en una interfaz; Crear asistentes con herramientas y archivos | API de IA opcional |
| [chatbox](../fichas/chatbox.md) | Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común. | Tu objetivo encaja con estos ejemplos: Conversar con varios proveedores; Probar un modelo local desde escritorio | API de IA opcional |

## Workspaces privados y segundos cerebros

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [AnythingLLM](../fichas/anything-llm.md) | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. | Tu objetivo encaja con estos ejemplos: Consultar documentación propia; Separar bases de conocimiento por proyecto | API de IA opcional |
| [odysseus](../fichas/odysseus.md) | Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. | Tu objetivo encaja con estos ejemplos: Organizar notas y tareas con IA; Comparar respuestas de modelos desde un workspace | Depende de la ruta elegida |
| [PrivateGPT](../fichas/private-gpt.md) | Capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP. | Tu objetivo encaja con estos ejemplos: Construir una API privada sobre documentos; Usar un modelo local como backend de programación | Depende de la ruta elegida |
| [Khoj](../fichas/khoj.md) | Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones. | Tu objetivo encaja con estos ejemplos: Consultar notas desde Obsidian; Crear un asistente de investigación personal | Depende de la ruta elegida |
| [Hermes Desktop](../fichas/hermes-desktop.md) | App de escritorio que envuelve al agente Hermes en una interfaz nativa. | Tu objetivo encaja con estos ejemplos: Usar Hermes desde una interfaz de escritorio; Consultar una instancia remota de Hermes | Depende de la ruta elegida |

## NotebookLM: alternativas y clientes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [SurfSense](../fichas/surfsense.md) | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. | Tu objetivo encaja con estos ejemplos: Revisar un contrato de prueba con comentarios; Extraer datos de un archivo Excel ficticio | Depende de la ruta elegida |
| [open-notebook](../fichas/open-notebook.md) | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. | Tu objetivo encaja con estos ejemplos: Estudiar documentos en una libreta; Generar un resumen o audio sobre material propio | Depende de la ruta elegida |
| [notebooklm-py](../fichas/notebooklm-py.md) | API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código. | Tu objetivo encaja con estos ejemplos: Automatizar consultas documentales; Exportar mapas o resúmenes propios | Sin clave propia de API de IA en la ruta básica |
| [notebooklm-mcp-cli](../fichas/notebooklm-mcp-cli.md) | CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP. | Tu objetivo encaja con estos ejemplos: Administrar fuentes desde un agente; Exportar contenido generado por NotebookLM | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md) — Preparar chat, documentos y memoria con rutas locales, comprobando por separado modelos, herramientas y conexiones externas.
- [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md) — Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
