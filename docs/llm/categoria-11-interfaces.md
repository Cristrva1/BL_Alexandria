# Alexandría para agentes · Interfaces para generar imágenes

Categoría 11 «Generar y editar imágenes con IA» › subcategoría `interfaces`. 3 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=11&sub=interfaces · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `comfyui` | Motor local para crear pipelines de generación de imagen y video con IA… | 3 Avanzado | 82 | GPL-3.0 (OSI copyleft) | sin grupo |
| `invokeai` | Suite profesional y unificada para Stable Diffusion que combina una UI web… | 3 Avanzado | 73 | Apache-2.0 (OSI permisiva) | recomendado |
| `krita-ai-diffusion` | Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y… | 2 Intermedio | 55 | GPL-3.0 (OSI copyleft) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### ComfyUI (`comfyui`)

- **Repo:** https://github.com/Comfy-Org/ComfyUI · GPL-3.0 · nivel 3 · 82/100
- **Qué es:** ComfyUI, motor modular de creación con IA basado en grafos de nodos, mantenido por Comfy Org. Licencia GPL-3.0. Es uno de los proyectos de IA generativa más populares (~147k estrellas, v0.45.0).
- **Cuándo elegirlo:** Casos: Crear un pipeline reproducible de imagen; Comparar dos ajustes del mismo modelo.
- **Requisitos:** nivel 3: preparación pesada; Python o distribución elegida; modelo; RAM y GPU según workflow; hardware prerequisites; API de IA: opcional; Python o distribución elegida; modelo; RAM y GPU según workflow.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Comfy-Org/ComfyUI/blob/master/README.md

  ```bash
  pip install comfy-cli
  comfy install
  ```
- **Primera prueba propuesta (no ejecutada):** Carga un workflow mínimo y conecta modelo, prompt, sampler y guardado Éxito: Obtienes una imagen y puedes identificar los nodos que la produjeron
- **Combina con:** `flux2` [11/modelos], `krita-ai-diffusion`, `real-esrgan` [11/edicion], `hunyuanvideo-1-5` [12/generativo]
- **Alternativas:** `wan2gp`
- **Riesgos y avisos:** Alternativas (elige una): wan2gp. Revisa los nodos personalizados antes de instalarlos: ejecutan código arbitrario. El modo offline desactiva nodos API opcionales; importar un workflow puede exigir modelos o nodos adicionales.

### InvokeAI (`invokeai`)

- **Repo:** https://github.com/invoke-ai/InvokeAI · Apache-2.0 · nivel 3 · 73/100 · recomendado en «Interfaces de creación de imágenes»
- **Qué es:** Invoke (InvokeAI), suite creativa de IA para medios visuales, de Invoke AI. Licencia Apache-2.0. Es madura (~29k estrellas, v6.14.4).
- **Cuándo elegirlo:** Casos: Retocar una ilustración por regiones; Organizar variantes de una producción visual.
- **Requisitos:** nivel 3: preparación pesada; Launcher o instalación oficial; modelo admitido; hardware según checkpoint; hardware prerequisites; API de IA: no; Launcher o instalación oficial; modelo admitido; hardware según checkpoint.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/invoke-ai/InvokeAI/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre un canvas, genera una zona pequeña y conserva la imagen original en otra capa Éxito: Puedes comparar la zona editada y sus parámetros
- **Combina con:** `diffusers` [11/modelos], `flux2` [11/modelos], `real-esrgan` [11/edicion]
- **Alternativas:** `krita-ai-diffusion`
- **Riesgos y avisos:** Alternativas (elige una): krita-ai-diffusion. La interfaz y sus modelos se preparan por separado; comienza con la instalación recomendada y un único modelo.

### Krita AI Diffusion (`krita-ai-diffusion`)

- **Repo:** https://github.com/Acly/krita-ai-diffusion · GPL-3.0 · nivel 2 · 55/100 · alternativa en «Interfaces de creación de imágenes»
- **Qué es:** Generative AI for Krita, plugin para usar IA generativa dentro de Krita, de @Acly (Interstice). Licencia GPL-3.0. Es maduro (~11k estrellas, v1.53.0).
- **Cuándo elegirlo:** Casos: Completar un fondo en una ilustración; Usar un boceto para guiar una imagen.
- **Requisitos:** nivel 2: preparación media; Krita compatible; plugin; servidor local o Cloud; GPU recomendada para local; hardware prerequisites; API de IA: opcional; Krita compatible; plugin; servidor local o Cloud; GPU recomendada para local.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.interstice.cloud/installation
- **Primera prueba propuesta (no ejecutada):** Selecciona una región de una imagen propia y genera una modificación en otra capa Éxito: Puedes aceptar o descartar la capa manteniendo el original
- **Combina con:** `comfyui`, `flux2` [11/modelos], `real-esrgan` [11/edicion]
- **Alternativas:** `invokeai`
- **Riesgos y avisos:** Alternativas (elige una): invokeai. El autor recomienda al menos 6 GB VRAM NVIDIA para local; CPU es posible pero muy lenta; revisa soporte del backend de tu GPU.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-11-interfaces.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Interfaces para generar imágenes», lee `docs/alexandria/categoria-11-interfaces.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-11-interfaces.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
