[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 WanGP

> App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| — | — | — | — | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado · **MCP** 🔌 sí

> ⚠️ El repositorio original ya no está disponible en GitHub; se conserva el clon local.

## Qué es

WanGP, antes Wan2GP, es una interfaz web para ejecutar en tu GPU decenas de modelos generativos abiertos: video (Wan 2.1/2.2, LTX-2, Hunyuan Video), imagen (Flux, Qwen Image), voz y música (Chatterbox, Index TTS, Ace Step) y 3D. Añade cola de trabajos, LoRAs, galerías y un asistente local, Deepy, que planifica y lanza las generaciones por ti.

## Por qué destaca

Está pensado para quien no tiene una GPU de 80 GB: gestiona memoria y cuantización (int8, fp8, GGUF, NV FP4) para correr modelos con 4-8 GB de VRAM, también en GTX 10XX y AMD, y añade los modelos nuevos casi en cuanto salen.

## Cómo funciona

App Python con interfaz Gradio que descarga los pesos adecuados a tu hardware y aplica offloading con su librería mmgp. Ofrece modo headless por línea de comandos, API propia e interfaz MCP para agentes externos.

## Instalación rápida

Ejecuta `scripts/install.sh` (o `scripts\install.bat` en Windows), o bien `git clone https://github.com/deepbeepmeep/Wan2GP.git`, entorno conda con Python 3.11, PyTorch con CUDA y `pip install -r requirements.txt`; arranca con `python wgp.py`.

## Casos de uso

- Generar video con Wan o LTX en una GPU de 8-12 GB
- Probar modelos nuevos de imagen, voz o música en una sola interfaz
- Lanzar lotes de generación sin supervisión en modo headless

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres generar video e imagen con modelos abiertos en una GPU de consumo sin montar flujos a mano | prefieres construir flujos por nodos con control fino (`comfyui`) o tienes una GPU grande y quieres el código oficial (`wan2-2`) |

**Limitaciones:** Su licencia propia (WanGP Community License) permite el uso gratuito, también en empresas, pero prohíbe venderlo, integrarlo en productos de pago u ofrecerlo como SaaS sin licencia comercial.

## Stack y modelos

- **Stack:** Python, PyTorch, Gradio, Diffusers, mmgp
- **Modelos / API:** Modelos abiertos en local (Wan, LTX, Hunyuan, Flux, Qwen Image, Chatterbox, Index TTS, entre otros); no necesita API externa.
- **Etiquetas:** `video` `image` `tts` `local` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [MoviePy](moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |
| [LosslessCut](lossless-cut.md) | 45.9k | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 146k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Enlaces

- 🐙 GitHub: [deepbeepmeep/Wan2GP](https://github.com/deepbeepmeep/Wan2GP)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
