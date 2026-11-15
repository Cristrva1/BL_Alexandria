[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 Wan2.2

> Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.7k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

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

Wan2.2 publica pesos y código de inferencia de varios modelos de video: texto a video e imagen a video de 14B (MoE), un modelo híbrido de 5B que genera 720p a 24 fps en una RTX 4090, video guiado por voz (S2V) y animación o sustitución de personajes (Animate). Es la base de muchos flujos de ComfyUI y Diffusers.

## Por qué destaca

Combina calidad cercana a modelos cerrados con licencia Apache 2.0 y un ecosistema amplio: integración oficial en ComfyUI y Diffusers, y herramientas de la comunidad para GPU con poca memoria.

## Cómo funciona

Modelo de difusión con Mixture-of-Experts que reparte el denoising entre expertos según el paso, más un VAE de alta compresión (16x16x4) en el modelo 5B. El prompt se puede ampliar con un LLM Qwen local o por API.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Wan2.2 para mi objetivo y necesito pasos guiados. Lee https://github.com/Wan-Video/Wan2.2/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Generar clips 720p desde un prompt para anuncios o reels
- Animar la foto de un producto o personaje con imagen a video
- Crear el video de una persona hablando a partir de un audio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres el modelo de video abierto de referencia, con licencia permisiva, y tienes una GPU de 24 GB o más | tu GPU tiene menos de 24 GB o prefieres no trabajar con scripts; usa `wan2gp` o `comfyui` con modelos cuantizados |

**Limitaciones:** Los modelos de 14B piden unos 80 GB de VRAM sin offload, y el de 5B al menos 24 GB.

## Stack y modelos

- **Stack:** Python, PyTorch, FlashAttention, Diffusers
- **Etiquetas:** `video` `inference` `local` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 147k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |
| [diffusers](diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. |
| [Real-ESRGAN](real-esrgan.md) | 37.5k | Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. |
| [CosyVoice](cosyvoice.md) | 24.4k | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [HunyuanVideo](hunyuanvideo.md) | 12.8k | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. |
| [LTX-Video](ltx-video.md) | 11.4k | Modelos abiertos de Lightricks (v0.9.x) para generar video desde texto o imagen, rápidos en GPU de consumo; hoy en modo legado. |

## Enlaces

- 🐙 GitHub: [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2)
- 🌐 Web: <https://wan.video>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
