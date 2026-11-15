[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Transcripción (voz a texto)

# ⚡ faster-whisper

> Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.8k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

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

Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. Puede reducir requisitos frente a otras implementaciones; mide calidad y rendimiento con tu propio audio.

## Por qué destaca

Es la versión preferida en producción por su relación velocidad/calidad y su bajo consumo; muy adoptada en pipelines y servidores de transcripción (WhisperX la usa internamente).

## Cómo funciona

Carga modelos Whisper compatibles y permite configurar dispositivo y precisión de inferencia.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y las dependencias de CPU o GPU correspondientes a la ruta elegida.

1. Instala la biblioteca en un entorno aislado.
2. Selecciona modelo, dispositivo y precisión siguiendo el ejemplo del README.
3. Transcribe un audio corto y revisa el texto y el consumo de memoria antes de procesar material largo.

**Comando de entrada documentado:**

```shell
pip install faster-whisper
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/SYSTRAN/faster-whisper/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar faster-whisper para mi objetivo y necesito pasos guiados. Lee https://github.com/SYSTRAN/faster-whisper/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Procesar lotes de audio/video con menos latencia
- Transcripción en producción/servidor
- Reducir coste de GPU manteniendo calidad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| el rendimiento, la memoria o el coste de GPU importan | necesitas alineación/diarización (whisperX) o te basta el CLI oficial |

## Stack y modelos

- **Stack:** Python, CTranslate2
- **Etiquetas:** `stt` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisperX](whisperx.md) | 25.3k | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper.cpp](whisper-cpp.md) | 55.2k | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. |

## Enlaces

- 🐙 GitHub: [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- 🧪 Receta: [Agente de voz en tiempo real](../playbooks/agente-de-voz.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/SYSTRAN/faster-whisper/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
