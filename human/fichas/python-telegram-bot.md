[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › Chatbots y asistentes conversacionales

# 📚 python-telegram-bot

> Biblioteca Python asíncrona de referencia para crear bots de Telegram, con cobertura completa de la Bot API y utilidades de alto nivel.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29.6k | LGPL-3.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Biblioteca de código abierto (LGPL-3.0 según su README; la API de GitHub la marca como GPL-3.0) mantenida por voluntarios. Muy madura; sigue de cerca cada versión de la Bot API.

## ¿Qué hace?

Ofrece una interfaz Python completa a la Bot API de Telegram y un framework con manejadores de comandos y mensajes, conversaciones por estados, teclados, pagos, webhooks, persistencia y JobQueue para tareas programadas.

## ¿Cómo lo hace?

Se instala con pip (extras opcionales como `[job-queue]`, `[webhooks]`, `[socks]`); desde la v20 está construida sobre asyncio. Requiere un token de BotFather.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Un bot de python-telegram-bot puede reenviar mensajes a un modelo local servido por Ollama y devolver la respuesta (combinación por arquitectura). | Ollama en marcha; después llama a su API desde el manejador de mensajes. |
| [LangGraph](langgraph.md) | Un grafo de LangGraph puede actuar como cerebro de un bot de Telegram construido con esta biblioteca (combinación por arquitectura). | Construye el agente en LangGraph; después invócalo desde el manejador del bot. |
| [coolify](coolify.md) | Un bot de python-telegram-bot se puede desplegar en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con volúmenes persistentes. |

**Notas:** Para bots con IA ya listos, revisa también openclaw o hermes-agent, que integran Telegram como canal.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v22.8 (2026-06-12) · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/README.rst) · [2](https://docs.python-telegram-bot.org/)</sub>

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

**Entrada documentada (consulta la sintaxis original):**

```
pip install python-telegram-bot --upgrade
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/README.rst)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar python-telegram-bot para mi objetivo y necesito pasos guiados. Lee https://github.com/python-telegram-bot/python-telegram-bot/blob/master/README.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install python-telegram-bot --upgrade`, crea un token con BotFather y ejecuta el ejemplo echobot..

**Qué comprobar:** El bot responde en Telegram repitiendo tus mensajes..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- crear un bot de Telegram que responda comandos y envíe avisos
- conectar un modelo de lenguaje a un chat de Telegram

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: crear un bot de Telegram que responda comandos y envíe avisos; conectar un modelo de lenguaje a un chat de Telegram | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `chatbots` `python` `library` `telegram`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [python-telegram-bot/python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- 🌐 Web: <https://python-telegram-bot.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/README.rst)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
