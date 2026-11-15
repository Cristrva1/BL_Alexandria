[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Interfaces para generar imágenes

# 🖼️ Stable Diffusion WebUI Forge

> Versión optimizada de la WebUI de Stable Diffusion, más rápida y con menos memoria.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.1k | AGPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

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

Mantiene la interfaz de AUTOMATIC1111 con mejoras de rendimiento y soporte de modelos nuevos como FLUX.

## Por qué destaca

Mejor rendimiento en GPUs modestas con la interfaz conocida.

## Cómo funciona

Backend reescrito para gestión de memoria y nuevos samplers sobre la WebUI de Gradio.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Stable Diffusion WebUI Forge para mi objetivo y necesito pasos guiados. Lee https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Generar imágenes en GPUs de 6-8 GB
- Probar FLUX con interfaz clásica
- Flujos con extensiones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres la WebUI clásica pero más rápida | prefieres flujos por nodos; mira `comfyui` |

**Limitaciones:** Licencia AGPL-3.0; actualizaciones irregulares.

## Stack y modelos

- **Stack:** Python, Gradio, PyTorch
- **Etiquetas:** `image` `local` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ControlNet](controlnet.md) | 34.2k | Modelos que guían la generación de imágenes con poses, bordes, profundidad o segmentación. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [stable-diffusion-webui](stable-diffusion-webui.md) | 165k | Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. |
| [ComfyUI](comfyui.md) | 147k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Enlaces

- 🐙 GitHub: [lllyasviel/stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
