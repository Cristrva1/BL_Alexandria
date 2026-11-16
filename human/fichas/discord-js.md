[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › Chatbots y asistentes conversacionales

# 📚 discord.js

> Módulo Node.js de referencia para interactuar con la API de Discord y crear bots, con paquetes para voz, REST y gateway.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.8k | Apache-2.0 | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 71/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (Apache-2.0) mantenida por la comunidad discord.js. Muy madura; sigue las versiones de la API de Discord.

## ¿Qué hace?

Permite crear bots que reaccionan a eventos, comandos de barra, botones y modales, gestionan canales y roles, y usan voz, con cobertura casi completa de la API de Discord y caché configurable.

## ¿Cómo lo hace?

Escrito en TypeScript para Node.js; se instala con npm, yarn, pnpm o bun. Requiere un token de bot del portal de desarrolladores de Discord.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [AI SDK (Vercel)](vercel-ai.md) | El AI SDK de Vercel puede generar las respuestas de un bot de discord.js con el modelo que elijas (combinación por arquitectura). | Crea el bot; después llama al AI SDK desde el manejador de comandos. |
| [Ollama](ollama.md) | Un bot de discord.js puede consultar un modelo local de Ollama para responder en el servidor (combinación por arquitectura). | Ollama en marcha; después llama a su API desde el bot. |
| [coolify](coolify.md) | Un bot de discord.js se puede desplegar en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con volúmenes persistentes. |

**Notas:** Respeta los términos de desarrolladores de Discord y los límites de tasa.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 14.28.1 (2026-11-03) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/discordjs/discord.js/blob/main/README.md) · [2](https://discord.js.org/)</sub>

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

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/discordjs/discord.js/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar discord.js para mi objetivo y necesito pasos guiados. Lee https://github.com/discordjs/discord.js/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `npm install discord.js`, crea una aplicación en el portal de desarrolladores de Discord y ejecuta un bot que responda a un comando..

**Qué comprobar:** El bot aparece en línea y responde al comando en tu servidor de pruebas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- crear un bot de Discord con comandos de barra para tu comunidad
- conectar un asistente de IA a un servidor de Discord

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: crear un bot de Discord con comandos de barra para tu comunidad; conectar un asistente de IA a un servidor de Discord | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `chatbots` `javascript` `library` `discord`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [discordjs/discord.js](https://github.com/discordjs/discord.js)
- 🌐 Web: <https://discord.js.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/discordjs/discord.js/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
