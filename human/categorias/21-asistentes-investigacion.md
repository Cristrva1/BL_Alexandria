[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Asistentes e investigación con agentes

Asistentes personales, equipos de agentes e investigación con fuentes. Compara la tarea que completan, las herramientas que pueden usar y la revisión que necesitas hacer del resultado.

18 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [OpenClaw](../fichas/openclaw.md) | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. | Depende de la ruta elegida |
| [autoresearch](../fichas/autoresearch.md) | Enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. | Sin API de IA en la ruta básica |

## Secciones

- [Asistentes autónomos y equipos de agentes](#asistentes-autónomos-y-equipos-de-agentes) — 12 repos
- [Agentes de research autónomo](#agentes-de-research-autónomo) — 6 repos

## Asistentes autónomos y equipos de agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [OpenClaw](../fichas/openclaw.md) | Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. | quieres un asistente personal que actúe por tus canales de chat | Depende de la ruta elegida |
| [hermes-agent](../fichas/hermes-agent.md) | Entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. | quieres agentes locales con UI y memoria persistente | Depende de la ruta elegida |
| [paperclip](../fichas/paperclip.md) | Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo. | necesitas coordinar varios agentes y seguir su trabajo en un panel | API de IA opcional |
| [ruflo](../fichas/ruflo.md) | Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). | orquestas muchos agentes a escala y quieres rendimiento | API de IA opcional |
| [DeepTutor](../fichas/deeptutor.md) | Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus documentos. | quieres un tutor con IA sobre tu propio material | Depende de la ruta elegida |
| [multica](../fichas/multica.md) | Plataforma para que humanos y agentes trabajen lado a lado ("tus próximas 10 contrataciones no serán humanas"). | mezclas trabajo humano y agentes en un mismo flujo | API de IA opcional |
| [OpenDots](../fichas/opendots.md) | Plataforma de asistentes de IA persistentes que coordinan conversaciones, llamadas y servicios conectados. | buscas esta función: Plataforma de asistentes de IA persistentes que coordinan conversaciones, llamadas y servicios conectados. | API de IA necesaria |
| [Mercury Agent](../fichas/mercury-agent.md) | Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. | quieres un asistente personal ligero con permisos claros | Depende de la ruta elegida |
| [social-media-agent](../fichas/social-media-agent.md) | Agente de LangChain que convierte enlaces en publicaciones para redes sociales con revisión humana antes de publicarlas. | quieres preparar publicaciones para X o LinkedIn con una etapa de aprobación | API de IA necesaria |
| [hello-halo](../fichas/hello-halo.md) | Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores API. | buscas esta función: Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores API. | API de IA opcional |
| [agentes-chat](../fichas/agentes-chat.md) | Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas. | buscas esta función: Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas. | API de IA opcional |
| [fugu](../fichas/fugu.md) | Ejemplos y acceso a un sistema multiagente de Sakana que se consume como un servicio de modelos mediante API. | buscas esta función: Ejemplos y acceso a un sistema multiagente de Sakana que se consume como un servicio de modelos mediante API. | API de IA necesaria |

## Agentes de research autónomo

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [autoresearch](../fichas/autoresearch.md) | Enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. | experimentas con research iterativo o quieres un punto de partida | Sin API de IA en la ruta básica |
| [deer-flow](../fichas/deer-flow.md) | Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. | quieres un orquestador completo y extensible | Depende de la ruta elegida |
| [STORM](../fichas/storm.md) | Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia. | necesitas informes largos y citados sobre un tema | Depende de la ruta elegida |
| [gpt-researcher](../fichas/gpt-researcher.md) | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. | necesitas research profundo citado | Depende de la ruta elegida |
| [open_deep_research](../fichas/open-deep-research.md) | Agente abierto de LangChain para investigación profunda configurable con distintos modelos, buscadores y servidores MCP. | quieres adaptar un agente de investigación construido con LangGraph | Depende de la ruta elegida |
| [local-deep-research](../fichas/local-deep-research.md) | Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes. | quieres investigar con un modelo local y conservar las fuentes consultadas | Depende de la ruta elegida |

## Recetas relacionadas

- [Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
