[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Agentes de voz en tiempo real

# 🖥️ dograh

> Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.1k | BSD-2-Clause | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

Dograh AI, plataforma open source y autoalojable para construir agentes de voz, alternativa a Vapi y Retell. Licencia BSD-2-Clause. Tiene ~6k estrellas y es activa (dograh-v1.51.0).

## ¿Qué hace?

Ofrece un constructor visual de flujos, pruebas rápidas, telefonía y la posibilidad de usar cualquier LLM, STT o TTS, o su propio stack. Los asistentes de código con IA pueden ayudar a diseñar los agentes.

## ¿Cómo lo hace?

Se autoaloja con un comando Docker. Por defecto el quickstart abre un túnel público de trycloudflare.com para los webhooks de telefonía y deja el registro abierto, algo a revisar en producción.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | LLM local. (combinación por arquitectura) | Configura un proveedor compatible. |
| [whisper.cpp](whisper-cpp.md) | STT autoalojado. (combinación por arquitectura) | Configura un STT propio. |
| [Kokoro](kokoro.md) | TTS autoalojado. (combinación por arquitectura) | Configura un TTS propio. |

**Notas:** Alternativas (elige una): pipecat, livekit-agents. Revisa el túnel público y el registro abierto por defecto.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada dograh-v1.51.0 (2026-11-04) · licencia declarada BSD-2-Clause (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/dograh-hq/dograh/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Autoalojamiento no incluye STT, TTS, LLM o telefonía; Cloud y proveedores tienen tarifas o cuotas propias |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. MCP permite consultar y guardar borradores desde clientes compatibles; los plugins Claude y Codex ayudan a configurar y no incluyen suscripciones de voz |
| Coste | El coste depende del proveedor o la ruta. Autoalojamiento no incluye STT, TTS, LLM o telefonía; Cloud y proveedores tienen tarifas o cuotas propias |
| Equipo | Preparación según la ruta elegida. Docker o entorno documentado; proveedores de voz/modelo; micrófono de prueba |

MCP permite consultar y guardar borradores desde clientes compatibles; los plugins Claude y Codex ayudan a configurar y no incluyen suscripciones de voz

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o entorno documentado
- proveedores de voz/modelo
- micrófono de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/dograh-hq/dograh/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dograh para mi objetivo y necesito pasos guiados. Lee https://github.com/dograh-hq/dograh/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un flujo de borrador y prueba una conversación local sin realizar llamadas telefónicas.

**Qué comprobar:** Puedes inspeccionar nodos, proveedores y transiciones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Diseñar un agente de voz
- Editar un workflow mediante MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Diseñar un agente de voz; Editar un workflow mediante MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP permite consultar y guardar borradores desde clientes compatibles; los plugins Claude y Codex ayudan a configurar y no incluyen suscripciones de voz

## Stack y modelos

- **Stack:** Docker o entorno documentado; proveedores de voz/modelo; micrófono de prueba
- **Etiquetas:** `voz-agentes` `agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pipecat](pipecat.md) | 17.3k | Framework open source para agentes de voz y apps multimodales en tiempo real. |
| [LiveKit Agents](livekit-agents.md) | 15.2k | Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. |
| [TEN Framework](ten-framework.md) | 11.2k | Framework para agentes de voz conversacionales en tiempo real, con grafo de extensiones (ASR, LLM, TTS, VAD, turnos), diseñador visual y ejemplos listos. |

## Enlaces

- 🐙 GitHub: [dograh-hq/dograh](https://github.com/dograh-hq/dograh)
- 🌐 Web: <https://app.dograh.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/dograh-hq/dograh/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
