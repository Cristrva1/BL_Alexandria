[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Generar y editar imágenes con IA

Interfaces y modelos de generación, recorte, restauración y ampliación. Distingue la aplicación, sus modelos y el coste o equipo para generar cada imagen.

12 repos · 4 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [ComfyUI](../fichas/comfyui.md) | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. | API de IA opcional |
| [FLUX](../fichas/flux.md) | Repositorio oficial de inferencia de los modelos FLUX.1 de Black Forest Labs para generar imágenes. | API de IA opcional |
| [rembg](../fichas/rembg.md) | Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. | API de IA opcional |
| [Open-Generative-AI](../fichas/open-generative-ai.md) | Estudio de imagen y video con servicios remotos MuAPI y rutas locales de escritorio mediante sd.cpp o Wan2GP. | API de IA opcional |

## Secciones

- [Interfaces para generar imágenes](#interfaces-para-generar-imágenes) — 5 repos
- [Modelos, librerías y control](#modelos-librerías-y-control) — 3 repos
- [Restauración, upscaling y edición](#restauración-upscaling-y-edición) — 3 repos
- [Suites generativas todo-en-uno](#suites-generativas-todo-en-uno) — 1 repos

## Interfaces para generar imágenes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [ComfyUI](../fichas/comfyui.md) | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. | Tu objetivo encaja con estos ejemplos: Crear un pipeline reproducible de imagen; Comparar dos ajustes del mismo modelo | API de IA opcional |
| [Fooocus](../fichas/fooocus.md) | Herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes. | Tu objetivo encaja con estos ejemplos: Bocetar una imagen para una idea visual; Probar inpainting sin un grafo complejo | Sin clave propia de API de IA en la ruta básica |
| [InvokeAI](../fichas/invokeai.md) | Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables. | Tu objetivo encaja con estos ejemplos: Retocar una ilustración por regiones; Organizar variantes de una producción visual | Sin clave propia de API de IA en la ruta básica |
| [Stable Diffusion WebUI Forge](../fichas/sd-webui-forge.md) | Variante de Stable Diffusion WebUI que experimenta con gestión de recursos y optimización de inferencia; el rendimiento depende de la configuración. | Tu objetivo encaja con estos ejemplos: Probar un checkpoint con gestión de memoria distinta; Comparar variantes de WebUI en una máquina | Sin clave propia de API de IA en la ruta básica |
| [Krita AI Diffusion](../fichas/krita-ai-diffusion.md) | Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting. | Tu objetivo encaja con estos ejemplos: Completar un fondo en una ilustración; Usar un boceto para guiar una imagen | API de IA opcional |

## Modelos, librerías y control

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [FLUX](../fichas/flux.md) | Repositorio oficial de inferencia de los modelos FLUX.1 de Black Forest Labs para generar imágenes. | Tu objetivo encaja con estos ejemplos: Prototipar imagen con FLUX.1 schnell; Comparar un modelo de edición con otro de generación | API de IA opcional |
| [diffusers](../fichas/diffusers.md) | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. | Tu objetivo encaja con estos ejemplos: Integrar generación de imágenes en Python; Experimentar con modelos de video o audio compatibles | Sin clave propia de API de IA en la ruta básica |
| [ComfyUI_IPAdapter_plus](../fichas/comfyui-ipadapter-plus.md) | Conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una o varias imágenes de referencia para transferir estilo o identidad. | Tu objetivo encaja con estos ejemplos: Transferir un estilo desde una referencia propia; Mantener una dirección visual entre variantes | Sin clave propia de API de IA en la ruta básica |

## Restauración, upscaling y edición

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [rembg](../fichas/rembg.md) | Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. | Tu objetivo encaja con estos ejemplos: Preparar una foto de producto; Crear un recorte para una composición | API de IA opcional |
| [Real-ESRGAN](../fichas/real-esrgan.md) | Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible generación de detalles nuevos. | Tu objetivo encaja con estos ejemplos: Preparar una ilustración para mayor tamaño; Mejorar visualmente una copia de material de baja resolución | Sin clave propia de API de IA en la ruta básica |
| [CodeFormer](../fichas/codeformer.md) | Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas. | Tu objetivo encaja con estos ejemplos: Experimentar con restauración de una fotografía; Comparar restauradores sobre material propio | Sin clave propia de API de IA en la ruta básica |

## Suites generativas todo-en-uno

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Open-Generative-AI](../fichas/open-generative-ai.md) | Estudio de imagen y video con servicios remotos MuAPI y rutas locales de escritorio mediante sd.cpp o Wan2GP. | Tu objetivo encaja con estos ejemplos: Probar imagen local desde una interfaz; Comparar una ruta local con un servicio de video remoto | API de IA opcional |

## Recetas relacionadas

- [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md) — Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.
- [Marketing de agencia](../playbooks/marketing-de-agencia.md) — Operar campañas, contenido y email a escala con agentes y herramientas propias.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
