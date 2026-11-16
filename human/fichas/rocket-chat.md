[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › Comunidades,chat y llamadas

# ⚙️ Rocket.Chat

> Plataforma de comunicación autoalojable para equipos y atención al cliente, con chat, llamadas, federación, omnicanal y marketplace de apps.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 46.5k | MIT + licencia Enterprise (ee/) | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Puntuación de calidad** 75/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de comunicación de Rocket.Chat Technologies. El núcleo es MIT y las carpetas ee/ tienen licencia Enterprise propia. Muy madura; usada por grandes organizaciones.

## ¿Qué hace?

Ofrece mensajería en tiempo real, hilos, llamadas de voz y vídeo, federación con otras redes, atención omnicanal a clientes, apps del marketplace o propias con Apps-Engine, integraciones, cifrado de extremo a extremo y cumplimiento normativo.

## ¿Cómo lo hace?

Escrito en TypeScript sobre Meteor y Node.js con MongoDB; se despliega con Docker, Podman o Kubernetes según la guía oficial. Clientes de escritorio y móviles aparte.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Los webhooks y la API REST de Rocket.Chat permiten automatizar avisos y flujos desde Activepieces (combinación por arquitectura). | Crea un webhook entrante en Rocket.Chat; después úsalo desde Activepieces. |
| [Ollama](ollama.md) | Un bot de Apps-Engine o una integración puede responder en Rocket.Chat con un modelo local de Ollama (combinación por arquitectura). | Ollama en marcha; después crea la integración que llame a su API. |
| [coolify](coolify.md) | Rocket.Chat se puede desplegar en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con volúmenes persistentes. |

**Notas:** Alternativas (elige una): mattermost.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 9.0.0 (2026-11-10) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/RocketChat/Rocket.Chat/blob/develop/README.md) · [2](https://docs.rocket.chat/docs/deploy-rocketchat)</sub>

## Ver similares

Grupo **Chat de equipo auto-hospedado**: Rocket.Chat ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Rocket.Chat** (esta ficha) ⭐ recomendado | 75 | Si buscas esto: plataforma de comunicación autoalojable para equipos y atención al cliente, con chat, llamadas, federación, omnicanal y marketplace de apps. |
| 2 | [Mattermost](mattermost.md) | 71 | Si buscas esto: plataforma de colaboración autoalojada y open core, alternativa a Slack: chat, automatización de flujos, llamadas, pantalla compartida e integración con IA. |
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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/RocketChat/Rocket.Chat/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Rocket.Chat para mi objetivo y necesito pasos guiados. Lee https://github.com/RocketChat/Rocket.Chat/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Rocket.Chat con Docker Compose siguiendo su guía, crea un espacio de trabajo y un canal..

**Qué comprobar:** Puedes chatear en el canal desde la web y la app móvil..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- sustituir Slack o Teams por un chat de equipo en tu servidor
- atender clientes de varios canales desde una bandeja compartida

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: sustituir Slack o Teams por un chat de equipo en tu servidor; atender clientes de varios canales desde una bandeja compartida | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Open core: el código de las carpetas ee/ tiene licencia comercial y algunas funciones requieren plan de pago.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `chat` `self-hosted` `typescript` `server`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Mattermost](mattermost.md) | 39.6k | Plataforma de colaboración autoalojada y open core, alternativa a Slack: chat, automatización de flujos, llamadas, pantalla compartida e integración con IA. |
| [Zulip](zulip.md) | 26.2k | Chat de equipo open source con hilos por tema: combina lo mejor del email y del chat para trabajo remoto. |

## Enlaces

- 🐙 GitHub: [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)
- 🌐 Web: <https://rocket.chat/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/RocketChat/Rocket.Chat/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
