[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Agentes de voz en tiempo real

# 📞 Pipecat

> Framework open source para agentes de voz y apps multimodales en tiempo real.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.3k | BSD-2-Clause | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Encadena STT, LLM y TTS con interrupciones y baja latencia, y conecta con teléfono, WebRTC o WhatsApp.

## Por qué destaca

Muy flexible, con decenas de proveedores de voz y transporte.

## Cómo funciona

Pipelines de frames procesan audio y texto en streaming entre servicios.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install pipecat-ai
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/pipecat-ai/pipecat/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Pipecat para mi objetivo y necesito pasos guiados. Lee https://github.com/pipecat-ai/pipecat/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Agente telefónico de atención
- Asistente de voz en web
- Tutor por voz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| construyes un agente de voz en Python | quieres infraestructura WebRTC gestionada; mira `livekit-agents` |

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `audio` `agents` `stt` `tts` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Kokoro](kokoro.md) | 10.1k | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |
| [whisper.cpp](whisper-cpp.md) | 55.2k | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LiveKit Agents](livekit-agents.md) | 15.2k | Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. |

## Enlaces

- 🐙 GitHub: [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat)
- 🌐 Web: <https://pipecat.ai>
- 🧪 Receta: [Agente de voz en tiempo real](../playbooks/agente-de-voz.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/pipecat-ai/pipecat/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
