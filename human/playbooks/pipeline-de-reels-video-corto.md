[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)

# 🎬 Pipeline de Reels / video corto

> **Objetivo:** Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.

## Empieza con una versión pequeña

Propuesta editorial; no es una integración ejecutada ni una lista completa de dependencias.

**Piezas iniciales:** [Kokoro](../fichas/kokoro.md), [remotion](../fichas/remotion.md), [FFmpeg](../fichas/ffmpeg.md)

**Prepara:** Un guion de 20 segundos y dos imágenes propias

**Primera prueba propuesta:** Sintetiza la voz, monta una escena sencilla y exporta un clip

**Qué comprobar:** El archivo reproduce imagen y voz con la duración esperada

WhisperX hace falta si partes de audio; generar imágenes y restaurarlas son ampliaciones, no requisitos de todo video

**Otras rutas, no piezas que debas sumar:** [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md)

## Orden propuesto para preparar las piezas

```mermaid
flowchart LR
  kokoro["Kokoro"] --> remotion["remotion"]
  remotion["remotion"] --> ffmpeg["FFmpeg"]
```

## 🧩 Piezas

| # | Repo | Papel en la receta | ⭐ | Instalación |
|---:|---|---|---:|---|
| 1 | [whisperX](../fichas/whisperx.md) | Transcribe y alinea palabra por palabra para los subtítulos | 25.3k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 2 | [Kokoro](../fichas/kokoro.md) | Genera una voz en off con una voz e idioma compatibles | 10.1k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |
| 3 | [ComfyUI](../fichas/comfyui.md) | Genera imágenes o b-roll con modelos de difusión | 147k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 4 | [Real-ESRGAN](../fichas/real-esrgan.md) | Escala y limpia las imágenes antes del montaje | 37.5k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 5 | [remotion](../fichas/remotion.md) | Ensambla el video con plantillas en React | 73.2k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 6 | [FFmpeg](../fichas/ffmpeg.md) | Render final, formatos y compresión | 67.3k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |
| 7 | [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md) | Atajo todo-en-uno: tema → video corto automático | 144k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |

## 🔌 Cómo se conecta

Flujo propuesto: WhisperX prepara subtítulos; Kokoro sintetiza narración; ComfyUI genera visuales; Remotion compone y FFmpeg exporta. Comprueba los datos,la duración y la licencia de cada recurso. MoneyPrinterTurbo es otra aplicación con su configuración y costes propios.

## 🚫 Cuándo NO usar esta receta

Si solo necesitas cortar un video existente,no necesitas generar voces o imágenes. Kokoro,ComfyUI y los demás modelos tienen requisitos de equipo distintos; si eliges servicios remotos,revisa sus tarifas. Chatterbox queda como archivo de investigación y no como voz inicial recomendada.

## 🔁 Variantes

- En lugar de [whisperX](../fichas/whisperx.md): [NeMo Speech](../fichas/nemo.md)
- En lugar de [Kokoro](../fichas/kokoro.md): [LuxTTS](../fichas/luxtts.md), [edge-tts](../fichas/edge-tts.md)
- En lugar de [ComfyUI](../fichas/comfyui.md): [WanGP](../fichas/wan2gp.md), [Stable Diffusion WebUI Forge](../fichas/sd-webui-forge.md)
- En lugar de [remotion](../fichas/remotion.md): [MoviePy](../fichas/moviepy.md), [HyperFrames](../fichas/hyperframes.md)
- En lugar de [MoneyPrinterTurbo](../fichas/moneyprinterturbo.md): [OpenMontage](../fichas/openmontage.md), [videofy_minimal](../fichas/videofy-minimal.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
