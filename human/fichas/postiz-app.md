[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › Email, marketing y notificaciones

# ⚙️ postiz-app

> Plataforma para preparar, programar y gestionar publicaciones en redes sociales, con integraciones y funciones de IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 41.6k | AGPL-3.0 | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado · **MCP** 🔌 sí

## ¿Qué es?

Plataforma de gestión de redes sociales para programar, automatizar y analizar contenido, de gitroomhq. La edición autoalojada es de código abierto (AGPL-3.0) sin funciones limitadas por licencia, y existe Postiz Cloud gestionado.

## ¿Qué hace?

Programa publicaciones en Instagram, YouTube, Dribbble, LinkedIn, Reddit, TikTok, Facebook, Pinterest, Threads, X, Slack, Discord, Mastodon y Bluesky, con analítica y un copiloto de IA para textos, imágenes y videos. Ofrece API pública, SDK de Node.js, nodo personalizado para n8n, integración con Make.com y un servidor MCP para agentes como Claude Code, Codex o Cursor.

## ¿Cómo lo hace?

Monorepo en TypeScript con Next.js (React), NestJS, Temporal para flujos y Prisma con PostgreSQL por defecto. En autoalojamiento debes configurar PostgreSQL, Redis, almacenamiento y variables de entorno, y crear tus propias apps de desarrollador en cada red (la aprobación de Meta, YouTube o TikTok puede tardar semanas). Se despliega con Docker, Coolify, Railway o cualquier VPS; la IA requiere tus propias claves de OpenAI u otros proveedores.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [n8n](n8n.md) | Nodo personalizado oficial de n8n para publicar desde flujos (por ejemplo, al aprobar un contenido). | Postiz primero con clave de API pública; después instala el nodo en n8n. |
| [Claude Code](claude-code.md) | Servidor MCP de Postiz para que un agente programe y gestione publicaciones. | Postiz con canales conectados; luego registra el MCP en el agente. |
| [coolify](coolify.md) | Ruta de despliegue citada en el README. | Coolify en el servidor; prepara PostgreSQL, Redis y almacenamiento antes del primer arranque. |

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v2.26.0 (2026-11-13) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/gitroomhq/postiz-app/blob/main/README.md) · [2](https://docs.postiz.com/public-api)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Cloud incluye cuotas de AI por plan; self-hosting usa claves propias y recursos; redes pueden exigir aprobaciones y permisos adicionales |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. MCP y CLI están incluidos por ambas rutas; clonar el código no obtiene automáticamente credenciales aprobadas de cada red |
| Coste | El coste depende del proveedor o la ruta. Cloud incluye cuotas de AI por plan; self-hosting usa claves propias y recursos; redes pueden exigir aprobaciones y permisos adicionales |
| Equipo | Preparación según la ruta elegida. Cuenta Cloud o self-host con PostgreSQL y Redis; apps de plataforma; modelos solo para AI |

MCP y CLI están incluidos por ambas rutas; clonar el código no obtiene automáticamente credenciales aprobadas de cada red

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta Cloud o self-host con PostgreSQL y Redis
- apps de plataforma
- modelos solo para AI

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.postiz.com/quickstart)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar postiz-app para mi objetivo y necesito pasos guiados. Lee https://docs.postiz.com/quickstart. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prepara una publicación ficticia en borrador y revisa preview, canal y horario sin programarla.

**Qué comprobar:** Puedes comprobar contenido y cuenta de destino antes de publicar.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar un calendario de contenido
- Evaluar generación asistida de borradores

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar un calendario de contenido; Evaluar generación asistida de borradores | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP y CLI están incluidos por ambas rutas; clonar el código no obtiene automáticamente credenciales aprobadas de cada red

## Stack y modelos

- **Stack:** Cuenta Cloud o self-host con PostgreSQL y Redis; apps de plataforma; modelos solo para AI
- **Etiquetas:** `marketing` `server` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app)
- 🌐 Web: <https://postiz.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/gitroomhq/postiz-app/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
