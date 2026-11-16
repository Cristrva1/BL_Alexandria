[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Procesamiento y limpieza de audio

# 📚 pyannote.audio

> Kit de PyTorch para diarización de hablantes (quién habla y cuándo) con modelos preentrenados y un servicio premium opcional.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.8k | MIT | Jupyter Notebook | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Kit de diarización de hablantes en Python sobre PyTorch (organización pyannote; pyannoteAI ofrece el servicio premium). Licencia MIT para el código; los modelos se publican en Hugging Face con condiciones propias. Versión 4.0.7 (junio de 2026), ~11k estrellas.

## ¿Qué hace?

Determina quién habla y cuándo: detección de actividad de voz, cambio de hablante, habla solapada y embeddings de hablante. Ofrece el pipeline abierto `community-1` (mejor que el 3.1 en conteo y asignación) y acceso integrado al pipeline premium `precision-2` de pyannoteAI.

## ¿Cómo lo hace?

Se instala con `uv add pyannote.audio` o `pip install pyannote.audio` (Python 3.11 o superior) y necesita ffmpeg para decodificar audio (torchcodec). Para `community-1` hay que aceptar las condiciones del modelo en Hugging Face y usar un token; se ejecuta en local, en CPU o GPU. `precision-2` se ejecuta en servidores de pyannoteAI con su clave de API. La telemetría es opcional (`PYANNOTE_METRICS_ENABLED`). Permite entrenamiento multi-GPU con PyTorch Lightning.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [whisperX](whisperx.md) | WhisperX usa pyannote-audio para la diarización y añade etiquetas de hablante a la transcripción. | Acepta las condiciones de pyannote en Hugging Face y pasa el token a WhisperX. |
| [PyTorch](pytorch.md) | pyannote.audio está construido sobre PyTorch; la elección de CUDA o CPU sigue la instalación de PyTorch. | Instala primero la variante de PyTorch adecuada a tu GPU. |
| [faster-whisper](faster-whisper.md) | Transcribir con faster-whisper y asignar después los segmentos a los hablantes de pyannote. (combinación por arquitectura) | Ejecuta la diarización y la transcripción por separado y cruza las marcas de tiempo. |
| [FFmpeg](ffmpeg.md) | Requisito documentado: torchcodec usa ffmpeg para decodificar el audio. | Instala ffmpeg antes del paquete. |
| [sherpa-onnx](sherpa-onnx.md) | Combinación recíproca: sherpa-onnx lo enlaza como «La diarización de sherpa-onnx usa el modelo de segmentación de pyannote exportado a ONNX junto a un modelo de embeddings de hablante». | Orden indicado desde sherpa-onnx: Descarga el modelo de segmentación de pyannote para sherpa-onnx; después ejecuta la diarización. |

**Notas:** Diarizar personas tiene implicaciones de privacidad: informa a los participantes. Las cifras del README (DER, velocidad en H100) son del autor.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada 4.0.7 (2026-06-30) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pyannote/pyannote-audio/blob/main/README.md) · [2](https://hf.co/pyannote/speaker-diarization-community-1)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. community-1 corre localmente con un token de Hugging Face; precision-2 corre en los servidores de pyannoteAI con su propia clave. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Los pipelines abiertos se ejecutan localmente en CPU o GPU tras aceptar sus condiciones en Hugging Face. |
| Coste | El coste depende del proveedor o la ruta. La ruta local no paga por uso; pyannoteAI ofrece créditos gratuitos y después cobra. La telemetría es opcional (PYANNOTE_METRICS_ENABLED). |
| Equipo | Memoria y GPU según el modelo. Python 3.11 o superior y ffmpeg; GPU recomendable para audio largo. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Instala ffmpeg y el paquete; acepta las condiciones de pyannote/speaker-diarization-community-1 en Hugging Face y crea un token.
2. Ejecuta el pipeline sobre un audio corto, en GPU si la tienes.
3. Revisa los segmentos por hablante antes de combinarlos con una transcripción.

**Entrada documentada (consulta la sintaxis original):**

```
pip install pyannote.audio
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/pyannote/pyannote-audio/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar pyannote.audio para mi objetivo y necesito pasos guiados. Lee https://github.com/pyannote/pyannote-audio/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta community-1 sobre un audio corto con dos voces de prueba.

**Qué comprobar:** Los segmentos alternan entre dos hablantes con marcas de tiempo coherentes.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Separar por hablante la grabación de una reunión
- Añadir hablantes a una transcripción

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Separar por hablante la grabación de una reunión; Añadir hablantes a una transcripción | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Jupyter Notebook, pyproject.toml
- **Etiquetas:** `audio` `diarization` `pytorch` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [pyannote/pyannote-audio](https://github.com/pyannote/pyannote-audio)
- 🌐 Web: <https://www.pyannote.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pyannote/pyannote-audio/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
