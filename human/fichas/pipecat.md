[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Agentes de voz en tiempo real

# 📞 Pipecat

> Framework open source para agentes de voz y apps multimodales en tiempo real.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.3k | BSD-2-Clause | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## ¿Qué es?

Pipecat, framework open source en Python para agentes de voz y multimodales en tiempo real, creado por Daily. Licencia BSD-2-Clause. Es maduro y muy activo (~17k estrellas, v1.16.0).

## ¿Qué hace?

Construye agentes de voz individuales o sistemas multiagente con pipelines de STT, LLM y TTS, turnos de conversación, interrupciones y transporte en tiempo real. Tiene integraciones con decenas de servicios, entre ellos Whisper, Kokoro, Fish, Piper, XTTS, NVIDIA y Ollama, y transportes como Daily, LiveKit, WebSocket y telefonía.

## ¿Cómo lo hace?

Funciona con Python 3.11–3.14 (3.15 aún no, por onnxruntime) y se instala con `pip install pipecat-ai[...]` o `pipecat init quickstart`. Daily ofrece soporte enterprise.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Kokoro](kokoro.md) | Servicio TTS integrado. | Instala el extra correspondiente. |
| [whisper.cpp](whisper-cpp.md) | STT local. (combinación por arquitectura) | Usa un servicio STT local. |
| [Ollama](ollama.md) | Servicio LLM integrado. | Configura el servicio Ollama. |
| [NeMo Speech](nemo.md) | Servicios NVIDIA integrados. | Configura el servicio NVIDIA. |
| [ElevenLabs (SDK de Python)](elevenlabs-python.md) | Pipecat incluye servicios de ElevenLabs para TTS y STT; usan la misma cuenta y clave que el SDK. | Configura `ELEVENLABS_API_KEY` y el extra de ElevenLabs. |

**Notas:** Alternativas (elige una): livekit-agents, dograh.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.16.0 (2026-11-12) · licencia declarada BSD-2-Clause (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pipecat-ai/pipecat/blob/main/README.md) · [2](https://docs.pipecat.ai/getting-started/quickstart)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Cada servicio tiene costes propios; documenta Whisper, Ollama y Piper locales además de proveedores Cloud |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Depende del recurso o la configuración |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | Modelos locales documentados. Tiene skills específicos de Claude Code; un agente que genera el código no aporta automáticamente el runtime ni créditos de telefonía o voz |
| Coste | El coste depende del proveedor o la ruta. Cada servicio tiene costes propios; documenta Whisper, Ollama y Piper locales además de proveedores Cloud |
| Equipo | Preparación según la ruta elegida. uv; proveedores STT, LLM y TTS; micrófono; transporte local o remoto |

Tiene skills específicos de Claude Code; un agente que genera el código no aporta automáticamente el runtime ni créditos de telefonía o voz

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv
- proveedores STT, LLM y TTS
- micrófono
- transporte local o remoto

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv tool install "pipecat-ai[cli]"
pipecat init
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/pipecat-ai/pipecat/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Pipecat para mi objetivo y necesito pasos guiados. Lee https://github.com/pipecat-ai/pipecat/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una prueba local de una pregunta y comprueba transcripción, respuesta y audio por separado.

**Qué comprobar:** Puedes localizar en qué etapa falla la conversación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar un agente de voz
- Comparar combinaciones STT/LLM/TTS

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar un agente de voz; Comparar combinaciones STT/LLM/TTS | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Tiene skills específicos de Claude Code; un agente que genera el código no aporta automáticamente el runtime ni créditos de telefonía o voz

## Stack y modelos

- **Stack:** uv; proveedores STT, LLM y TTS; micrófono; transporte local o remoto
- **Etiquetas:** `audio` `agents` `stt` `tts` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LiveKit Agents](livekit-agents.md) | 15.2k | Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. |
| [dograh](dograh.md) | 6.1k | Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables. |

## Enlaces

- 🐙 GitHub: [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat)
- 🌐 Web: <https://pipecat.ai>
- 🧪 Receta: [Agente de voz en tiempo real](../playbooks/agente-de-voz.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pipecat-ai/pipecat/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
