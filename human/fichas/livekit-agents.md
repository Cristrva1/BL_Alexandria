[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Agentes de voz en tiempo real

# 📞 LiveKit Agents

> Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.2k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

LiveKit Agents, framework para agentes de voz y vídeo en tiempo real sobre la infraestructura WebRTC de LiveKit. Licencia Apache-2.0; sus modelos de detección de turno usan la «LiveKit Model License». Es activo (~15k estrellas, 1.8.12).

## ¿Qué hace?

Crea participantes programables que escuchan, hablan y ven en salas LiveKit, con plugins de STT, LLM y TTS, detección de turnos, herramientas y telefonía. Hay SDK en Python y Node.js (AgentsJS).

## ¿Cómo lo hace?

Se instala con `pip install "livekit-agents[openai,deepgram,cartesia]"` (u otros plugins) y requiere un servidor LiveKit, autoalojado o LiveKit Cloud.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Kokoro](kokoro.md) | TTS local vía endpoint compatible. (combinación por arquitectura) | Expón Kokoro y configúralo como TTS. |
| [Ollama](ollama.md) | LLM local vía plugin compatible con OpenAI. (combinación por arquitectura) | Apunta el plugin al endpoint de Ollama. |
| [whisper.cpp](whisper-cpp.md) | STT local. (combinación por arquitectura) | Expón el servidor y úsalo como STT. |

**Notas:** Alternativas (elige una): pipecat.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada livekit-agents@1.8.12 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/livekit/agents/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Modelos, STT, TTS, transporte y Cloud se costean por separado; Ollama es una ruta LLM local documentada |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. El MCP del README consulta documentación para desarrollar y no controla automáticamente tus agentes; usar Ollama no vuelve locales todos los componentes de audio o transporte |
| Coste | El coste depende del proveedor o la ruta. Modelos, STT, TTS, transporte y Cloud se costean por separado; Ollama es una ruta LLM local documentada |
| Equipo | Preparación según la ruta elegida. Python; LiveKit; proveedores o modelos locales; micrófono de prueba |

El MCP del README consulta documentación para desarrollar y no controla automáticamente tus agentes; usar Ollama no vuelve locales todos los componentes de audio o transporte

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- LiveKit
- proveedores o modelos locales
- micrófono de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install "livekit-agents[openai,deepgram,cartesia]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/livekit/agents/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LiveKit Agents para mi objetivo y necesito pasos guiados. Lee https://github.com/livekit/agents/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa terminal mode para una conversación breve y revisa cada etapa antes de añadir telefonía.

**Qué comprobar:** Puedes comprobar audio de entrada, modelo y respuesta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir un asistente de voz
- Evaluar conversación en tiempo real

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir un asistente de voz; Evaluar conversación en tiempo real | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP del README consulta documentación para desarrollar y no controla automáticamente tus agentes; usar Ollama no vuelve locales todos los componentes de audio o transporte

## Stack y modelos

- **Stack:** Python; LiveKit; proveedores o modelos locales; micrófono de prueba
- **Etiquetas:** `audio` `agents` `video` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pipecat](pipecat.md) | 17.3k | Framework open source para agentes de voz y apps multimodales en tiempo real. |

## Enlaces

- 🐙 GitHub: [livekit/agents](https://github.com/livekit/agents)
- 🌐 Web: <https://docs.livekit.io/agents>
- 🧪 Receta: [Agente de voz en tiempo real](../playbooks/agente-de-voz.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/livekit/agents/blob/main/README.md)
- [Fuente 2](https://docs.livekit.io/agents/models/llm/plugins/ollama/)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
