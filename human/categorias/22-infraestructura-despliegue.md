[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Infraestructura, despliegue y herramientas para agentes

Sandboxes, herramientas de ejecución, backend y alojamiento. Son piezas de infraestructura: separa el coste del servidor, los servicios conectados y las llamadas al modelo.

18 repos · 4 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Composio](../fichas/composio.md) | Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales. | Depende de la ruta elegida |
| [E2B](../fichas/e2b.md) | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. | Sin API de IA en la ruta básica |

## Secciones

- [Infraestructura: sandboxes, herramientas y protocolos](#infraestructura-sandboxes-herramientas-y-protocolos) — 12 repos
- [Dominios y recursos de infraestructura](#dominios-y-recursos-de-infraestructura) — 2 repos
- [Redes y transporte](#redes-y-transporte) — 1 repos
- [Alojamiento y backend](#alojamiento-y-backend) — 3 repos

## Infraestructura: sandboxes, herramientas y protocolos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Composio](../fichas/composio.md) | Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales. | tu agente necesita actuar en muchas apps SaaS | Depende de la ruta elegida |
| [E2B](../fichas/e2b.md) | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. | tu agente ejecuta código y necesitas aislarlo | Sin API de IA en la ruta básica |
| [claude-task-master](../fichas/claude-task-master.md) | Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP. | buscas esta función: Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP. | API de IA necesaria |
| [agent-desktop](../fichas/agent-desktop.md) | CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio. | necesitas automatizar aplicaciones nativas desde un agente | Sin API de IA en la ruta básica |
| [NemoClaw](../fichas/nemoclaw.md) | Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. | quieres correr agentes potentes con aislamiento corporativo | Depende de la ruta elegida |
| [codex-chatgpt-web](../fichas/codex-chatgpt-web.md) | Integración de terceros que conecta una sesión de ChatGPT Web con el selector de modelos y herramientas de Codex. | quieres estudiar una integración entre ChatGPT Web y Codex | API: por confirmar |
| [sandbox](../fichas/sandbox.md) | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. | quieres aislar la ejecución de agentes y reproducibilidad | Sin API de IA en la ruta básica |
| [Gemini Computer Use (preview)](../fichas/computer-use-preview.md) | Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. | quieres probar computer use con Gemini | API de IA necesaria |
| [NeMo-Agent-Toolkit](../fichas/nemo-agent-toolkit.md) | Toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo). | trabajas con infra NVIDIA o necesitas guardrails/eval empresarial | Depende de la ruta elegida |
| [shepherd](../fichas/shepherd.md) | Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos. | buscas esta función: Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos. | Sin API de IA en la ruta básica |
| [nodeterm](../fichas/nodeterm.md) | Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto. | gestionas muchas terminales o sesiones de agentes y prefieres una organización visual | Sin API de IA en la ruta básica |
| [Agent Protocol](../fichas/agent-protocol.md) | Especificación de LangChain para exponer cualquier agente con una API estándar de ejecuciones, hilos y estado. | diseñas una plataforma que sirve agentes de distintos frameworks | Sin API de IA en la ruta básica |

## Dominios y recursos de infraestructura

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [FreeDomain](../fichas/freedomain.md) | Recursos de registro de dominios y aprendizaje práctico de DNS publicados por DigitalPlat. | quieres aprender el flujo de dominios y DNS con sus recursos de referencia | Sin API de IA en la ruta básica |
| [free-for-dev](../fichas/free-for-dev.md) | Directorio de servicios de infraestructura y desarrollo que ofrecen planes o niveles gratuitos. | buscas servicios de desarrollo con un nivel gratuito disponible | Sin API de IA en la ruta básica |

## Redes y transporte

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [MasterDnsVPN](../fichas/masterdnsvpn.md) | Implementación en Go de un túnel que transporta tráfico TCP mediante consultas y respuestas DNS. | quieres estudiar transporte de red sobre DNS en un entorno de pruebas | Sin API de IA en la ruta básica |

## Alojamiento y backend

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [supabase](../fichas/supabase.md) | Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones. | buscas esta función: Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones. | Sin API de IA en la ruta básica |
| [coolify](../fichas/coolify.md) | Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios. | buscas esta función: Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios. | Sin API de IA en la ruta básica |
| [CasaOS](../fichas/casaos.md) | Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos. | buscas esta función: Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos. | Sin API de IA en la ruta básica |

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
