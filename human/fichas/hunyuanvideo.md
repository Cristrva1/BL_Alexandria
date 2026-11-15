[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 HunyuanVideo

> Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.8k | NOASSERTION | Python | 2026-11-10 |

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

HunyuanVideo publica los pesos, la definición en PyTorch y el código de inferencia de un modelo de texto a video de más de 13.000 millones de parámetros, que genera clips de unos 5 segundos (129 fotogramas) en 540p o 720p. Las variantes de imagen a video, avatares guiados por audio y personalización viven en repos aparte.

## Por qué destaca

Al publicarse fue el modelo de video abierto más grande, con calidad comparable a modelos cerrados en evaluaciones humanas. Tiene soporte nativo en ComfyUI y Diffusers, pesos FP8 y versiones cuantizadas de la comunidad.

## Cómo funciona

Transformer de difusión que trabaja en un espacio latente comprimido por un VAE causal 3D; el prompt se codifica con un LLM multimodal en lugar de CLIP o T5. Admite inferencia paralela en varias GPU con xDiT.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar HunyuanVideo para mi objetivo y necesito pasos guiados. Lee https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Generar planos cinematográficos a partir de un prompt
- Crear b-roll para videos sin rodar ni comprar material de stock
- Investigar o ajustar modelos de video con pesos abiertos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tienes una GPU de 60-80 GB o varias GPU y quieres un modelo de texto a video abierto de alta calidad | trabajas con GPU de consumo; prueba `ltx-video`, `wan2-2` o `wan2gp`, o la versión 1.5, más eficiente |

**Limitaciones:** Necesita entre 45 y 60 GB de VRAM, y su licencia Tencent Hunyuan Community excluye la UE, el Reino Unido y Corea del Sur.

## Stack y modelos

- **Stack:** Python, PyTorch, Diffusers, FlashAttention, xDiT
- **Etiquetas:** `video` `inference` `local` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 147k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |
| [diffusers](diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. |
| [Real-ESRGAN](real-esrgan.md) | 37.5k | Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Wan2.2](wan2-2.md) | 18.7k | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. |
| [LTX-Video](ltx-video.md) | 11.4k | Modelos abiertos de Lightricks (v0.9.x) para generar video desde texto o imagen, rápidos en GPU de consumo; hoy en modo legado. |

## Enlaces

- 🐙 GitHub: [Tencent-Hunyuan/HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo)
- 🌐 Web: <https://aivideo.hunyuan.tencent.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
