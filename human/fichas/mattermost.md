[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › Comunidades,chat y llamadas

# ⚙️ Mattermost

> Plataforma de colaboración autoalojada y open core, alternativa a Slack: chat, automatización de flujos, llamadas, pantalla compartida e integración con IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.6k | AGPL-3.0 / Apache-2.0 (herramientas) + Enterprise | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 71/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de colaboración open core de Mattermost, Inc. El código fuente se licencia bajo AGPL-3.0 o licencia comercial; los binarios oficiales, bajo MIT; hay ediciones de pago. Muy madura.

## ¿Qué hace?

Ofrece canales, mensajes directos, hilos, búsqueda, automatización de flujos, llamadas y pantalla compartida, integración con IA e integraciones mediante APIs, webhooks, comandos de barra, apps y plugins.

## ¿Cómo lo hace?

Servidor en Go con frontend React y PostgreSQL; se despliega con Docker, paquetes de Ubuntu, tarball o Kubernetes. Clientes de escritorio y móviles.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Los webhooks entrantes de Mattermost permiten enviar avisos desde flujos de Activepieces (combinación por arquitectura). | Crea un webhook entrante en Mattermost; después úsalo en Activepieces. |
| [Ollama](ollama.md) | Las funciones de IA de Mattermost o un bot propio pueden apuntar a un modelo local servido por Ollama (combinación por arquitectura). | Ollama en marcha; después configura el endpoint en la integración de IA. |
| [coolify](coolify.md) | Mattermost se puede desplegar en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con volúmenes persistentes. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Element Web](element-web.md)

**Notas:** Alternativas (elige una): rocket-chat.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v12.1.0 (2026-11-05) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mattermost/mattermost/blob/master/README.md) · [2](https://github.com/mattermost/mattermost/blob/master/LICENSE.txt) · [3](https://docs.mattermost.com/guides/deployment.html)</sub>

## Ver similares

Grupo **Chat de equipo auto-hospedado**: Mattermost ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Rocket.Chat](rocket-chat.md) ⭐ recomendado | 75 | Si buscas esto: plataforma de comunicación autoalojable para equipos y atención al cliente, con chat, llamadas, federación, omnicanal y marketplace de apps. |
| 2 | **Mattermost** (esta ficha) | 71 | Si buscas esto: plataforma de colaboración autoalojada y open core, alternativa a Slack: chat, automatización de flujos, llamadas, pantalla compartida e integración con IA. |
| 3 | [Zulip](zulip.md) | 63 | Si buscas esto: chat de equipo open source con hilos por tema: combina lo mejor del email y del chat para trabajo remoto. |

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/mattermost/mattermost/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Mattermost para mi objetivo y necesito pasos guiados. Lee https://github.com/mattermost/mattermost/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Mattermost con Docker siguiendo la guía oficial, crea un equipo y un canal y añade un webhook entrante..

**Qué comprobar:** Los mensajes enviados al webhook aparecen en el canal..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- montar un chat de equipo privado en tu infraestructura
- integrar alertas de CI o monitorización en canales del equipo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: montar un chat de equipo privado en tu infraestructura; integrar alertas de CI o monitorización en canales del equipo | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Open core: el código fuente es AGPL-3.0 (herramientas de administración Apache-2.0) y las funciones Enterprise requieren licencia comercial.

## Stack y modelos

- **Stack:** TypeScript
- **Etiquetas:** `chat` `self-hosted` `go` `server`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Rocket.Chat](rocket-chat.md) | 46.5k | Plataforma de comunicación autoalojable para equipos y atención al cliente, con chat, llamadas, federación, omnicanal y marketplace de apps. |
| [Zulip](zulip.md) | 26.2k | Chat de equipo open source con hilos por tema: combina lo mejor del email y del chat para trabajo remoto. |

## Enlaces

- 🐙 GitHub: [mattermost/mattermost](https://github.com/mattermost/mattermost)
- 🌐 Web: <https://mattermost.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mattermost/mattermost/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
