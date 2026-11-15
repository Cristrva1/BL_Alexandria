[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Agentes de voz en tiempo real

# 📞 LiveKit Agents

> Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.2k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

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

## Qué puedes hacer con él

Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit.

## Por qué destaca

Usos propuestos: Construir un asistente de voz; Evaluar conversación en tiempo real.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Kokoro](kokoro.md) | 10.1k | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |

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
