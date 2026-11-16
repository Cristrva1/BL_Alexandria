[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Alojamiento y backend

# ⚙️ coolify

> Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 66.1k | Apache-2.0 | PHP | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 2 Intermedio — instalador de una línea; después hay que configurar dominios y despliegues · corregido a mano

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Coolify, plataforma autoalojada para desplegar aplicaciones, bases de datos y servicios en tus propios servidores, de coollabsio. Licencia Apache-2.0. Es muy popular (~66k estrellas), activa y financiada por patrocinios.

## ¿Qué hace?

Es una alternativa autoalojada a Heroku, Netlify y Vercel. Despliega desde GitHub, GitLab, Bitbucket o Gitea con Nixpacks, Railpack, Dockerfile, Compose o imágenes. Gestiona bases de datos, backups, SSL y dominios, con dashboard, API, CLI y MCP. Los recursos siguen funcionando si dejas de usarlo.

## ¿Cómo lo hace?

Se instala con `curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash` en un servidor compatible (VPS, bare metal, Raspberry Pi); solo necesita SSH hacia los servidores gestionados.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [supabase](supabase.md) | Autoalojar Supabase como servicio. (combinación por arquitectura) | Despliega Supabase desde Coolify. |
| [activepieces](activepieces.md) | Coolify trae plantillas de servicio oficiales para desplegar Activepieces (y también Windmill) con un clic. | Coolify primero; luego despliega la plantilla `activepieces`. |
| [Windmill](windmill.md) | Plantilla de servicio oficial de Coolify para Windmill. | Coolify primero; luego despliega la plantilla `windmill`. |
| [FreeDomain](freedomain.md) | Dominio gratuito para las apps. (combinación por arquitectura) | Apunta el DNS al servidor. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (55). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Actual Budget](actual.md) · [AppFlowy](appflowy.md) · [Appwrite](appwrite.md) · [audiobookshelf](audiobookshelf.md) · [Baserow](baserow.md) · [binance-trader](binance-trader.md) · [Caddy](caddy.md) · [Calibre-Web](calibre-web.md) · [CrowdSec](crowdsec.md) · [Dagger](dagger.md) · [discord.js](discord-js.md) · [Easy!Appointments](easyappointments.md) · [EspoCRM](espocrm.md) · [Firefly III](firefly-iii.md) · [fluxer](fluxer.md) · [free-for-dev](free-for-dev.md) · [FreeScout](freescout.md) · [FreshRSS](freshrss.md) · [Ghostfolio](ghostfolio.md) · [Grist](grist-core.md) · [huginn](huginn.md) · [Immich](immich.md) · [Jellyfin](jellyfin.md) · [karakeep](karakeep.md) · [Kavita](kavita.md) · [Mattermost](mattermost.md) · [Memos](memos.md) · [Miniflux](miniflux.md) · [NetBird](netbird.md) · [NocoDB](nocodb.md) · [open-seo](open-seo.md) · [open-sol-bot](open-sol-bot.md) · [opencode-manager](opencode-manager.md) · [pdfcraft](pdfcraft.md) · [PdfDing](pdfding.md) · [PhotoPrism](photoprism.md) · [Pi-hole](pi-hole.md) · [postiz-app](postiz-app.md) · [python-telegram-bot](python-telegram-bot.md) · [Reflex](reflex.md) · [Rocket.Chat](rocket-chat.md) · [RSSHub](rsshub.md) · [server](nextcloud-server.md) · [SonarQube Community Build](sonarqube.md) · [Synapse](synapse.md) · [syncthing](syncthing.md) · [Teable](teable.md) · [Traefik Proxy](traefik.md) · [Trilium Notes](trilium.md) · [Trivy](trivy.md) · [Uptime Kuma](uptime-kuma.md) · [vaultwarden](vaultwarden.md) · [wallabag](wallabag.md) · [whatsapp-agentkit](whatsapp-agentkit.md) · [Zammad](zammad.md)

**Notas:** Alternativa (elige una): casaos.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v4.7.5 (2026-11-10) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/coollabsio/coolify/blob/main/README.md) · [2](https://coolify.io/docs/installation) · [3](https://github.com/coollabsio/coolify/tree/main/templates/compose)</sub>

## Ver similares

Grupo **Paneles de auto-hospedaje y PaaS propios**: coolify ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **coolify** (esta ficha) ⭐ recomendado | 74 | Si buscas esto: plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios. |
| 2 | [Dokploy](dokploy.md) | 67 | Si buscas esto: plataforma como servicio autoalojada, alternativa a Vercel, Netlify y Heroku, para desplegar aplicaciones y bases de datos con Docker y Traefik. |
| 3 | [CasaOS](casaos.md) | 52 | Si buscas esto: entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Self-host abierto requiere servidores y mantenimiento; Cloud es un servicio de pago separado |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Un patrocinador que menciona Claude Code no acredita una integración del producto con ese agente |
| Coste | El coste depende del proveedor o la ruta. Self-host abierto requiere servidores y mantenimiento; Cloud es un servicio de pago separado |
| Equipo | Preparación según la ruta elegida. Servidor compatible; Docker; dominio opcional; aplicación de prueba |

Un patrocinador que menciona Claude Code no acredita una integración del producto con ese agente

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servidor compatible
- Docker
- dominio opcional
- aplicación de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://coolify.io/docs/installation)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar coolify para mi objetivo y necesito pasos guiados. Lee https://coolify.io/docs/installation. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega una página estática de prueba y revisa logs antes de añadir bases de datos reales.

**Qué comprobar:** Puedes abrir el sitio y reconocer su servicio y registros.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Alojar una demo web
- Administrar despliegues en servidor propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Alojar una demo web; Administrar despliegues en servidor propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Un patrocinador que menciona Claude Code no acredita una integración del producto con ese agente

## Stack y modelos

- **Stack:** Servidor compatible; Docker; dominio opcional; aplicación de prueba
- **Etiquetas:** `infraestructura` `server` `php`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [CasaOS](casaos.md) | 37.6k | Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos. |
| [Dokploy](dokploy.md) | 38.5k | Plataforma como servicio autoalojada, alternativa a Vercel, Netlify y Heroku, para desplegar aplicaciones y bases de datos con Docker y Traefik. |

## Enlaces

- 🐙 GitHub: [coollabsio/coolify](https://github.com/coollabsio/coolify)
- 🌐 Web: <https://coolify.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/coollabsio/coolify/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
