[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › Comunidades,chat y llamadas

# ⚙️ Synapse

> Servidor doméstico de Matrix de referencia, mantenido por Element: chat federado, abierto e interoperable que puedes alojar tú mismo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.8k | AGPL-3.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

Implementación de servidor de Matrix de código abierto (AGPL-3.0, o licencia comercial de Element) mantenida por Element. Muy madura.

## ¿Qué hace?

Aloja cuentas y salas de Matrix con mensajería cifrada de extremo a extremo (en los clientes), federación con otros servidores, administración, módulos y puentes hacia otras redes mediante servicios de aplicación.

## ¿Cómo lo hace?

Escrito en Python y Rust; se instala con paquetes de Debian, Docker o pip. Para producción se recomienda PostgreSQL y un proxy inverso con TLS; expone métricas Prometheus.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Grafana](grafana.md) | La documentación de Synapse explica cómo exponer métricas Prometheus y ofrece un panel de Grafana. | Habilita las métricas; después importa el panel de Grafana. |
| [Caddy](caddy.md) | Caddy sirve como proxy inverso con TLS y delegación .well-known para Synapse (combinación por arquitectura). | Synapse en local; después configura reverse_proxy en Caddy. |
| [coolify](coolify.md) | Synapse se puede desplegar en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con volúmenes persistentes. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Element Web](element-web.md) · [Zulip](zulip.md)

**Notas:** Para despliegues sencillos, servidores Matrix más ligeros (no catalogados) pueden bastar.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v1.165.0 (2026-11-10) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/element-hq/synapse/blob/develop/README.rst) · [2](https://element-hq.github.io/synapse/latest/setup/installation.html) · [3](https://element-hq.github.io/synapse/latest/metrics-howto.html)</sub>

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

[Instrucciones originales de instalación](https://github.com/element-hq/synapse/blob/develop/README.rst)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Synapse para mi objetivo y necesito pasos guiados. Lee https://github.com/element-hq/synapse/blob/develop/README.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Synapse con paquetes o Docker siguiendo la guía oficial, crea un usuario y conéctate con un cliente Matrix..

**Qué comprobar:** Puedes chatear desde el cliente y unirte a salas de otros servidores federados..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- alojar tu propio servidor de chat federado para un grupo o comunidad
- conectar usuarios con otros servidores Matrix manteniendo tus datos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: alojar tu propio servidor de chat federado para un grupo o comunidad; conectar usuarios con otros servidores Matrix manteniendo tus datos | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, Cargo.toml, pyproject.toml
- **Etiquetas:** `chat` `python` `self-hosted` `server`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [element-hq/synapse](https://github.com/element-hq/synapse)
- 🌐 Web: <https://element-hq.github.io/synapse>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/element-hq/synapse/blob/develop/README.rst)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
