[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Generar y editar imágenes con IA

Interfaces y modelos de generación, recorte, restauración y ampliación. Distingue la aplicación, sus modelos y el coste o equipo para generar cada imagen.

10 repos · 3 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [ComfyUI](../fichas/comfyui.md) | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. | API de IA opcional |
| [FLUX.2](../fichas/flux2.md) | Código oficial de inferencia de los modelos abiertos FLUX.2 de Black Forest Labs para generar y editar imágenes, con variantes rápidas para GPU domésticas. | API de IA opcional |
| [rembg](../fichas/rembg.md) | Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. | API de IA opcional |

## Secciones

- [Interfaces para generar imágenes](#interfaces-para-generar-imágenes) — 3 repos
- [Modelos, librerías y control](#modelos-librerías-y-control) — 2 repos
- [Restauración, upscaling y edición](#restauración-upscaling-y-edición) — 5 repos

## Interfaces para generar imágenes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [ComfyUI](../fichas/comfyui.md) | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. | Tu objetivo encaja con estos ejemplos: Crear un pipeline reproducible de imagen; Comparar dos ajustes del mismo modelo | API de IA opcional |
| [InvokeAI](../fichas/invokeai.md) | Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables. | Tu objetivo encaja con estos ejemplos: Retocar una ilustración por regiones; Organizar variantes de una producción visual | Sin clave propia de API de IA en la ruta básica |
| [Krita AI Diffusion](../fichas/krita-ai-diffusion.md) | Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting. | Tu objetivo encaja con estos ejemplos: Completar un fondo en una ilustración; Usar un boceto para guiar una imagen | API de IA opcional |

## Modelos, librerías y control

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [FLUX.2](../fichas/flux2.md) | Código oficial de inferencia de los modelos abiertos FLUX.2 de Black Forest Labs para generar y editar imágenes, con variantes rápidas para GPU domésticas. | Tu objetivo encaja con estos ejemplos: Generar imágenes de producto en tu propia GPU; Editar una foto combinando varias imágenes de referencia | API de IA opcional |
| [diffusers](../fichas/diffusers.md) | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. | Tu objetivo encaja con estos ejemplos: Integrar generación de imágenes en Python; Experimentar con modelos de video o audio compatibles | Sin clave propia de API de IA en la ruta básica |

## Restauración, upscaling y edición

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [rembg](../fichas/rembg.md) | Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. | Tu objetivo encaja con estos ejemplos: Preparar una foto de producto; Crear un recorte para una composición | API de IA opcional |
| [Upscayl](../fichas/upscayl.md) | Aplicación de escritorio libre para ampliar y mejorar imágenes con IA (Real-ESRGAN sobre NCNN Vulkan) en Linux, macOS y Windows. | Tu objetivo encaja con estos ejemplos: ampliar fotos antiguas o de baja resolución para imprimirlas; escalar en lote una carpeta de imágenes para una web | Sin clave propia de API de IA en la ruta básica |
| [Real-ESRGAN](../fichas/real-esrgan.md) | Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible generación de detalles nuevos. | Tu objetivo encaja con estos ejemplos: Preparar una ilustración para mayor tamaño; Mejorar visualmente una copia de material de baja resolución | Sin clave propia de API de IA en la ruta básica |
| [CodeFormer](../fichas/codeformer.md) | Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas. | Tu objetivo encaja con estos ejemplos: Experimentar con restauración de una fotografía; Comparar restauradores sobre material propio | Sin clave propia de API de IA en la ruta básica |
| [chaiNNer](../fichas/chainner.md) | Interfaz por nodos para encadenar procesamiento de imágenes con IA y clásico: escalado, restauración, conversión y lotes, en Windows, macOS y Linux. | Tu objetivo encaja con estos ejemplos: escalar y restaurar lotes de imágenes con varios modelos en cadena; crear flujos repetibles de conversión y retoque de imágenes | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md) — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
