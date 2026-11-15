[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Asistentes e investigación con agentes

Asistentes personales, equipos de agentes e investigación con fuentes. Compara la tarea que completan, las herramientas que pueden usar y la revisión que necesitas hacer del resultado.

18 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [OpenClaw](../fichas/openclaw.md) | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. | API de IA opcional |
| [autoresearch](../fichas/autoresearch.md) | Experimento para iterar sobre entrenamiento de nanochat con un agente de código y una GPU NVIDIA. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Asistentes autónomos y equipos de agentes](#asistentes-autónomos-y-equipos-de-agentes) — 12 repos
- [Agentes de research autónomo](#agentes-de-research-autónomo) — 6 repos

## Asistentes autónomos y equipos de agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [OpenClaw](../fichas/openclaw.md) | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. | Tu objetivo encaja con estos ejemplos: Probar un asistente personal; Conectar un agente a un canal propio | API de IA opcional |
| [hermes-agent](../fichas/hermes-agent.md) | Asistente de Nous Research con memoria, skills y herramientas; usa proveedores remotos o endpoints locales configurados. | Tu objetivo encaja con estos ejemplos: Evaluar memoria de un asistente; Comparar un modelo local con Nous Portal | API de IA opcional |
| [paperclip](../fichas/paperclip.md) | Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo. | Tu objetivo encaja con estos ejemplos: Organizar tareas de varios agentes; Auditar una propuesta antes de aprobarla | API de IA opcional |
| [ruflo](../fichas/ruflo.md) | Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). | Tu objetivo encaja con estos ejemplos: Coordinar tareas de código; Estudiar memoria compartida entre agentes | API de IA opcional |
| [DeepTutor](../fichas/deeptutor.md) | Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus documentos. | Tu objetivo encaja con estos ejemplos: Estudiar un tema desde apuntes propios; Preparar preguntas de repaso | API de IA opcional |
| [multica](../fichas/multica.md) | Workspace para asignar y revisar trabajo de agentes de código mediante sus CLI y cuentas propias. | Tu objetivo encaja con estos ejemplos: Organizar trabajo entre agentes; Revisar entregas en un espacio compartido | API de IA opcional |
| [OpenDots](../fichas/opendots.md) | Interfaz abierta de asistentes persistentes que requiere CopilotKit Intelligence, alojado, evaluado localmente o con licencia. | Tu objetivo encaja con estos ejemplos: Probar un asistente persistente; Estudiar aprobación de acciones conectadas | API de IA necesaria |
| [Mercury Agent](../fichas/mercury-agent.md) | Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. | Tu objetivo encaja con estos ejemplos: Probar un asistente persistente; Estudiar presupuestos de tokens | API de IA opcional |
| [social-media-agent](../fichas/social-media-agent.md) | Agente de LangChain que convierte enlaces en publicaciones para redes sociales con revisión humana antes de publicarlas. | Tu objetivo encaja con estos ejemplos: Preparar una propuesta para LinkedIn; Convertir un artículo en un borrador corto | API de IA necesaria |
| [hello-halo](../fichas/hello-halo.md) | Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores API. | Tu objetivo encaja con estos ejemplos: Explorar un asistente de escritorio; Revisar tareas de código visualmente | API de IA opcional |
| [agentes-chat](../fichas/agentes-chat.md) | Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas. | Tu objetivo encaja con estos ejemplos: Evaluar un espacio de colaboración con agentes; Organizar consultas en canales | API de IA opcional |
| [fugu](../fichas/fugu.md) | Ejemplos y acceso a un sistema multiagente de Sakana que se consume como un servicio de modelos mediante API. | Tu objetivo encaja con estos ejemplos: Probar un sistema multiagente como proveedor; Comparar un flujo de código con Fugu | API de IA necesaria |

## Agentes de research autónomo

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [autoresearch](../fichas/autoresearch.md) | Experimento para iterar sobre entrenamiento de nanochat con un agente de código y una GPU NVIDIA. | Tu objetivo encaja con estos ejemplos: Estudiar optimización de entrenamiento; Aprender a registrar experimentos reproducibles | Sin clave propia de API de IA en la ruta básica |
| [deer-flow](../fichas/deer-flow.md) | Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. | Tu objetivo encaja con estos ejemplos: Investigar un tema con fuentes; Coordinar una generación de informe | Depende de la ruta elegida |
| [STORM](../fichas/storm.md) | Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia. | Tu objetivo encaja con estos ejemplos: Preparar una revisión de un tema; Comparar perspectivas antes de escribir | API de IA necesaria |
| [gpt-researcher](../fichas/gpt-researcher.md) | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. | Tu objetivo encaja con estos ejemplos: Preparar un informe de mercado con fuentes; Investigar documentación técnica | API de IA opcional |
| [open_deep_research](../fichas/open-deep-research.md) | Agente abierto de LangChain para investigación profunda configurable con distintos modelos, buscadores y servidores MCP. | Tu objetivo encaja con estos ejemplos: Estudiar investigación con LangGraph; Comparar configuraciones de búsqueda | API de IA opcional |
| [local-deep-research](../fichas/local-deep-research.md) | Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes. | Tu objetivo encaja con estos ejemplos: Consultar documentos privados; Preparar una revisión bibliográfica | API de IA opcional |

## Recetas relacionadas

- [Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
