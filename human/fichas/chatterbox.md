[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Síntesis y clonación de voz

# 🗣️ Chatterbox

> Modelo de texto a voz open source de Resemble AI con clonación de voz y control de emoción.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.8k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Clona una voz con unos segundos de audio y ajusta la expresividad. Multilingüe y con marca de agua.

## Por qué destaca

Calidad comparable a servicios comerciales con licencia MIT.

## Cómo funciona

Modelo basado en Llama que genera tokens de voz condicionados por una referencia.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install chatterbox-tts
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/resemble-ai/chatterbox/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Chatterbox para mi objetivo y necesito pasos guiados. Lee https://github.com/resemble-ai/chatterbox/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Voz de marca para videos
- Doblaje con clonación
- Agentes de voz expresivos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres clonar voces con calidad alta y licencia libre | necesitas algo muy ligero en CPU; mira `kokoro` |

## Stack y modelos

- **Stack:** Python, PyTorch
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pipecat](pipecat.md) | 17.3k | Framework open source para agentes de voz y apps multimodales en tiempo real. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Fish Speech](fish-speech.md) | 33.7k | Sistema de texto a voz open source de alta calidad con clonación de voz multilingüe. |
| [GPT-SoVITS](gpt-sovits.md) | 65.1k | Clonación de voz y TTS con solo un minuto de audio, con interfaz web para entrenar. |
| [Kokoro](kokoro.md) | 10.1k | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |
| [LuxTTS](luxtts.md) | 5.6k | Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. |

## Enlaces

- 🐙 GitHub: [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox)
- 🌐 Web: <https://resemble-ai.github.io/chatterbox_demopage/>
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/resemble-ai/chatterbox/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
