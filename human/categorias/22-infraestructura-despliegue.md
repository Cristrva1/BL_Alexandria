[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Infraestructura, despliegue y herramientas para agentes

Sandboxes, herramientas de ejecución, backend y alojamiento. Son piezas de infraestructura: separa el coste del servidor, los servicios conectados y las llamadas al modelo.

26 repos · 4 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Composio](../fichas/composio.md) | Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales. | Sin clave propia de API de IA en la ruta básica |
| [E2B](../fichas/e2b.md) | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Infraestructura: sandboxes, herramientas y protocolos](#infraestructura-sandboxes-herramientas-y-protocolos) — 10 repos
- [Dominios y recursos de infraestructura](#dominios-y-recursos-de-infraestructura) — 2 repos
- [Redes y transporte](#redes-y-transporte) — 5 repos
- [Alojamiento y backend](#alojamiento-y-backend) — 9 repos

## Infraestructura: sandboxes, herramientas y protocolos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Composio](../fichas/composio.md) | Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales. | Tu objetivo encaja con estos ejemplos: Conectar un agente a un CRM; Explorar herramientas de consulta de un servicio | Sin clave propia de API de IA en la ruta básica |
| [E2B](../fichas/e2b.md) | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. | Tu objetivo encaja con estos ejemplos: Ejecutar código aislado de una app; Preparar un entorno temporal para un agente | Sin clave propia de API de IA en la ruta básica |
| [claude-task-master](../fichas/claude-task-master.md) | Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP. | Tu objetivo encaja con estos ejemplos: Descomponer un proyecto web; Revisar orden y dependencias de tareas | API de IA opcional |
| [agent-desktop](../fichas/agent-desktop.md) | CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio. | Tu objetivo encaja con estos ejemplos: Inspeccionar una app de escritorio propia; Preparar una prueba de interfaz | Sin clave propia de API de IA en la ruta básica |
| [NemoClaw](../fichas/nemoclaw.md) | Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. | Tu objetivo encaja con estos ejemplos: Estudiar aislamiento para OpenClaw; Comparar políticas de ejecución de agentes | Depende de la ruta elegida |
| [sandbox](../fichas/sandbox.md) | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. | Tu objetivo encaja con estos ejemplos: Probar herramientas de un agente en un contenedor; Consultar una interfaz de navegador aislada | Sin clave propia de API de IA en la ruta básica |
| [Gemini Computer Use (preview)](../fichas/computer-use-preview.md) | Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. | Tu objetivo encaja con estos ejemplos: Estudiar automatización visual de navegador; Evaluar tareas de formularios ficticios | API de IA necesaria |
| [shepherd](../fichas/shepherd.md) | Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos. | Tu objetivo encaja con estos ejemplos: Estudiar reproducción de ejecuciones; Comparar una traza con un resultado final | API de IA opcional |
| [nodeterm](../fichas/nodeterm.md) | Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto. | Tu objetivo encaja con estos ejemplos: Organizar varias sesiones de código; Asociar sesiones con worktrees | API de IA opcional |
| [Agent Protocol](../fichas/agent-protocol.md) | Especificación de LangChain para exponer cualquier agente con una API estándar de ejecuciones, hilos y estado. | Tu objetivo encaja con estos ejemplos: Diseñar una API de agentes; Comparar protocolos antes de implementar | Sin clave propia de API de IA en la ruta básica |

## Dominios y recursos de infraestructura

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [FreeDomain](../fichas/freedomain.md) | Recursos de registro de dominios y aprendizaje práctico de DNS publicados por DigitalPlat. | Tu objetivo encaja con estos ejemplos: Aprender DNS; Evaluar un dominio para un proyecto personal | Sin clave propia de API de IA en la ruta básica |
| [free-for-dev](../fichas/free-for-dev.md) | Directorio de servicios de infraestructura y desarrollo que ofrecen planes o niveles gratuitos. | Tu objetivo encaja con estos ejemplos: Encontrar infraestructura para una demo; Comparar niveles gratuitos | Sin clave propia de API de IA en la ruta básica |

## Redes y transporte

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [frp](../fichas/frp.md) | Proxy inverso rápido para exponer servidores locales detrás de NAT o cortafuegos a internet, con TCP, UDP, HTTP, HTTPS y modo P2P. | Tu objetivo encaja con estos ejemplos: acceder por SSH a un equipo de casa detrás de NAT; publicar temporalmente un servicio web local usando tu propio VPS | Sin clave propia de API de IA en la ruta básica |
| [Headscale](../fichas/headscale.md) | Implementación abierta y autoalojada del servidor de control de Tailscale para crear tu propia red privada WireGuard con los clientes oficiales. | Tu objetivo encaja con estos ejemplos: conectar tus equipos y servidores en una red privada sin depender del servicio de Tailscale; dar acceso remoto a una red doméstica o de laboratorio | Sin clave propia de API de IA en la ruta básica |
| [NetBird](../fichas/netbird.md) | Red privada superpuesta basada en WireGuard con SSO, MFA y control de acceso granular, autoalojable o en la nube. | Tu objetivo encaja con estos ejemplos: conectar servidores y equipos remotos sin abrir puertos; dar acceso a la red interna con SSO y políticas por grupo | Sin clave propia de API de IA en la ruta básica |
| [WireGuard Easy](../fichas/wg-easy.md) | La forma más sencilla de ejecutar WireGuard VPN con interfaz web para gestionar clientes, códigos QR, estadísticas y 2FA. | Tu objetivo encaja con estos ejemplos: montar una VPN para acceder a tu red de casa desde el móvil; gestionar clientes de WireGuard sin editar archivos a mano | Sin clave propia de API de IA en la ruta básica |
| [MasterDnsVPN](../fichas/masterdnsvpn.md) | Implementación en Go de un túnel que transporta tráfico TCP mediante consultas y respuestas DNS. | Tu objetivo encaja con estos ejemplos: Estudiar transporte sobre DNS; Probar conectividad en un laboratorio | Sin clave propia de API de IA en la ruta básica |

## Alojamiento y backend

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [supabase](../fichas/supabase.md) | Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones. | Tu objetivo encaja con estos ejemplos: Preparar un backend para una web; Conectar un agente a un esquema de prueba | Sin clave propia de API de IA en la ruta básica |
| [Uptime Kuma](../fichas/uptime-kuma.md) | Monitor de disponibilidad autoalojado y fácil de usar: comprueba webs y servicios, envía alertas a más de 90 canales y publica páginas de estado. | Tu objetivo encaja con estos ejemplos: recibir un aviso en Telegram cuando tu web o servidor cae; publicar una página de estado de tus servicios | Sin clave propia de API de IA en la ruta básica |
| [Caddy](../fichas/caddy.md) | Servidor web y proxy inverso extensible con HTTPS automático por defecto, configurable con Caddyfile o JSON y API. | Tu objetivo encaja con estos ejemplos: publicar tus servicios autoalojados con HTTPS sin gestionar certificados; servir una web estática o hacer de proxy inverso con pocas líneas | Sin clave propia de API de IA en la ruta básica |
| [coolify](../fichas/coolify.md) | Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios. | Tu objetivo encaja con estos ejemplos: Alojar una demo web; Administrar despliegues en servidor propio | Sin clave propia de API de IA en la ruta básica |
| [Traefik Proxy](../fichas/traefik.md) | Proxy inverso y balanceador de carga dinámico para contenedores y microservicios que se configura automáticamente desde Docker, Kubernetes y otros. | Tu objetivo encaja con estos ejemplos: publicar contenedores Docker con dominios y HTTPS mediante etiquetas; balancear tráfico entre servicios en Kubernetes | Sin clave propia de API de IA en la ruta básica |
| [Appwrite](../fichas/appwrite.md) | Plataforma de backend abierta orientada a agentes y desarrolladores: autenticación, bases de datos, almacenamiento, funciones, mensajería, tiempo real y hosting, con MCP. | Tu objetivo encaja con estos ejemplos: dar backend completo a una app web o móvil sin escribir servidor; dejar que un agente de código opere un proyecto de backend vía MCP | Sin clave propia de API de IA en la ruta básica |
| [Portainer CE](../fichas/portainer.md) | Interfaz web ligera para gestionar contenedores en Docker, Swarm, Podman, Kubernetes y ACI (Community Edition). | Tu objetivo encaja con estos ejemplos: administrar los contenedores de tu homelab desde el navegador; desplegar stacks de Docker Compose con interfaz gráfica | Sin clave propia de API de IA en la ruta básica |
| [Dokploy](../fichas/dokploy.md) | Plataforma como servicio autoalojada, alternativa a Vercel, Netlify y Heroku, para desplegar aplicaciones y bases de datos con Docker y Traefik. | Tu objetivo encaja con estos ejemplos: desplegar tus aplicaciones y bases de datos en un VPS propio con interfaz web; levantar con un clic plantillas como Plausible o Cal.com | Sin clave propia de API de IA en la ruta básica |
| [CasaOS](../fichas/casaos.md) | Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos. | Tu objetivo encaja con estos ejemplos: Organizar servicios domésticos; Explorar un servidor personal | Sin clave propia de API de IA en la ruta básica |

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
