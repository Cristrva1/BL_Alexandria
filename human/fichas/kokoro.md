[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Síntesis y clonación de voz

# 🗣️ Kokoro

> Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.1k | Apache-2.0 | JavaScript | 2026-11-10 |

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

Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. Comprueba los idiomas, dependencias de audio y condiciones de la variante que utilices.

## Por qué destaca

Excelente relación calidad, tamaño y licencia.

## Cómo funciona

Un pipeline de síntesis transforma texto en audio usando los pesos y voces seleccionados.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python, los pesos y las dependencias de audio e idioma de la variante elegida.

1. Instala la biblioteca y prepara las dependencias que indica su README.
2. Elige idioma y voz de los ejemplos disponibles.
3. Sintetiza un texto breve y escucha el resultado antes de generar una narración completa.

**Comando de entrada documentado:**

```shell
pip install kokoro
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/hexgrad/kokoro/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Kokoro para mi objetivo y necesito pasos guiados. Lee https://github.com/hexgrad/kokoro/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Voz para agentes locales
- Narración de videos
- Audiolibros sencillos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres TTS ligero, rápido y con licencia permisiva | necesitas clonar voces; mira `chatterbox` |

## Stack y modelos

- **Stack:** Python, PyTorch, JavaScript
- **Etiquetas:** `tts` `audio` `local`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pipecat](pipecat.md) | 17.3k | Framework open source para agentes de voz y apps multimodales en tiempo real. |
| [whisper.cpp](whisper-cpp.md) | 55.2k | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Chatterbox](chatterbox.md) | 27.8k | Modelo de texto a voz open source de Resemble AI con clonación de voz y control de emoción. |
| [TTS](tts.md) | 46.2k | Toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz. |
| [LuxTTS](luxtts.md) | 5.6k | Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. |
| [edge-tts](edge-tts.md) | 12.5k | Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. |

## Enlaces

- 🐙 GitHub: [hexgrad/kokoro](https://github.com/hexgrad/kokoro)
- 🧪 Receta: [Agente de voz en tiempo real](../playbooks/agente-de-voz.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/hexgrad/kokoro/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
