[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Alojamiento y backend

# ⚙️ Caddy

> Servidor web y proxy inverso extensible con HTTPS automático por defecto, configurable con Caddyfile o JSON y API.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 79.1k | Apache-2.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Servidor web de código abierto (Apache-2.0) creado por Matt Holt y patrocinado por empresas. Muy maduro.

## ¿Qué hace?

Sirve sitios y hace de proxy inverso con HTTPS automático (incluidos certificados internos y renovación), HTTP/3, balanceo de carga, compresión, plantillas y servidor de archivos, ampliable con módulos.

## ¿Cómo lo hace?

Escrito en Go; un único binario para cualquier plataforma, paquetes o Docker. Se configura con Caddyfile, JSON nativo o su API REST; los plugins se compilan con xcaddy.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [coolify](coolify.md) | Coolify permite usar Caddy como proxy en lugar de Traefik. | Instala Coolify; después cambia el proxy del servidor a Caddy en la configuración. |
| [Uptime Kuma](uptime-kuma.md) | Uptime Kuma vigila los sitios que publica Caddy (combinación por arquitectura). | Publica el sitio con Caddy; después añade el monitor. |
| [Headscale](headscale.md) | La documentación de Headscale incluye la configuración para ejecutarlo detrás de Caddy. | Headscale en local; después añade el bloque reverse_proxy en Caddy. |
| [frp](frp.md) | Combinación recíproca: frp lo enlaza como «Caddy puede poner HTTPS automático delante de los servicios HTTP expuestos con frp en el VPS (combinación por arquitectura)». | Orden indicado desde frp: frps en el VPS; después configura Caddy como proxy hacia el puerto de frp. |
| [Synapse](synapse.md) | Combinación recíproca: Synapse lo enlaza como «Caddy sirve como proxy inverso con TLS y delegación .well-known para Synapse (combinación por arquitectura)». | Orden indicado desde Synapse: Synapse en local; después configura reverse_proxy en Caddy. |
| [WireGuard Easy](wg-easy.md) | Combinación recíproca: WireGuard Easy lo enlaza como «Caddy publica la interfaz web de wg-easy con HTTPS (combinación por arquitectura)». | Orden indicado desde WireGuard Easy: wg-easy en local; después configura reverse_proxy en Caddy. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (3). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[authentik](authentik.md) · [Keycloak](keycloak.md) · [OWASP CRS](coreruleset.md)

**Notas:** Alternativas (elige una): traefik.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v2.11.9 (2026-11-05) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/caddyserver/caddy/blob/master/README.md) · [2](https://caddyserver.com/docs/) · [3](https://coolify.io/docs/knowledge-base/server/proxies)</sub>

## Ver similares

Grupo **Proxies inversos con HTTPS automático**: Caddy ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Caddy** (esta ficha) ⭐ recomendado | 70 | Si buscas esto: servidor web y proxy inverso extensible con HTTPS automático por defecto, configurable con Caddyfile o JSON y API. |
| 2 | [Traefik Proxy](traefik.md) | 70 | Si buscas esto: proxy inverso y balanceador de carga dinámico para contenedores y microservicios que se configura automáticamente desde Docker, Kubernetes y otros. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/caddyserver/caddy/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Caddy para mi objetivo y necesito pasos guiados. Lee https://github.com/caddyserver/caddy/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Caddy y ejecuta `caddy reverse-proxy --from localhost:8443 --to localhost:8080` sobre un servicio local..

**Qué comprobar:** Caddy sirve el servicio por HTTPS con un certificado local automático..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- publicar tus servicios autoalojados con HTTPS sin gestionar certificados
- servir una web estática o hacer de proxy inverso con pocas líneas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: publicar tus servicios autoalojados con HTTPS sin gestionar certificados; servir una web estática o hacer de proxy inverso con pocas líneas | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Go, go.mod
- **Etiquetas:** `web` `go` `self-hosted` `server`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Traefik Proxy](traefik.md) | 65.6k | Proxy inverso y balanceador de carga dinámico para contenedores y microservicios que se configura automáticamente desde Docker, Kubernetes y otros. |

## Enlaces

- 🐙 GitHub: [caddyserver/caddy](https://github.com/caddyserver/caddy)
- 🌐 Web: <https://caddyserver.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/caddyserver/caddy/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
