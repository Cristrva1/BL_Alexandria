[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Transcripción (voz a texto)

# 🎯 whisperX

> Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.3k | BSD-2-Clause | Python | 2026-06-23 |

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

Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. Las etapas, modelos y credenciales requeridos cambian según las funciones que actives.

## Por qué destaca

Es la opción de referencia cuando los timings finos y el "quién habla" importan, muy usada para subtítulos de reels y entrevistas; combina tres componentes probados en un solo pipeline.

## Cómo funciona

Combina reconocimiento de voz, alineación y componentes de diarización configurables.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install whisperx
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/m-bain/whisperX/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar whisperX para mi objetivo y necesito pasos guiados. Lee https://github.com/m-bain/whisperX/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Subtítulos bien ajustados para reels/entrevistas
- Separar hablantes en podcasts
- Exportar SRT/VTT con timings de palabra

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas subtítulos precisos o diarización | te basta texto plano (whisper) o no quieres gestionar tokens de HF |

## Stack y modelos

- **Stack:** Python, faster-whisper, wav2vec2, pyannote
- **Etiquetas:** `stt` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper](whisper.md) | 113k | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. |
| [MoviePy](moviepy.md) | 15.2k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [NVIDIA NeMo Speech](nemo.md) | 18.8k | Framework de NVIDIA para entrenar y usar modelos de voz: reconocimiento, síntesis y más. |

## Enlaces

- 🐙 GitHub: [m-bain/whisperX](https://github.com/m-bain/whisperX)
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/m-bain/whisperX/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
