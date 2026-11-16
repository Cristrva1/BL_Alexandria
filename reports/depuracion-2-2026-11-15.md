# Segunda depuración

Aplicada el 15 de noviembre de 2026 con aprobación expresa («eliminar y reemplazar»). Se retiraron **9 repos** y se añadieron **3 fichas nuevas** revisadas: de 644 a 638 fichas públicas. Los retiros quedan en `data/retired.json` junto con los 35 de la primera depuración.

## Método

Más profundo que la primera pasada:

1. Estado en vivo en GitHub de los 643 repos con fuente en GitHub: archivado, renombrado, fork, último commit de la rama principal y última versión publicada.
2. README completo (no solo el inicio) con patrones ampliados: modo mantenimiento, «solo correcciones», soporte limitado, proyecto movido, sucesor, fin de vida, búsqueda de mantenedores. Cada coincidencia se revisó a mano.
3. Repos más nuevos de la misma organización con el mismo nombre y número de versión mayor (por ejemplo, `sam2` → `sam3`).
4. README que se declaran sucesores o forks de otro repo del catálogo: ninguno.

Resultado: ningún repo archivado nuevo (solo `pdfding`, ya enlazado a Codeberg), ninguno renombrado, y 28 sin commits en el último año, la mayoría librerías terminadas.

## A. Sin mantenimiento según sus autores (3)

| Repo | Evidencia | Sustituto en el catálogo |
|---|---|---|
| `fooocus` | README: soporte limitado solo con correcciones de errores; no adoptará modelos nuevos como FLUX. Último commit sep 2025 | `comfyui`, `invokeai` |
| `comfyui-ipadapter-plus` | Su autor lo dejó en «solo mantenimiento» en abr 2025; sin commits desde entonces | `comfyui` |
| `rasa` | README: Rasa Open Source en modo mantenimiento; su desarrollo sigue en productos comerciales (Hello Rasa, CALM) | `botpress` |

## B. Sustituidos por una versión nueva del mismo autor (3)

| Repo | Sin commits desde | Versión nueva (no está en el catálogo) |
|---|---|---|
| `sam2` | dic 2024 | `facebookresearch/sam3` (SAM 3, activo en nov 2026) |
| `flux` | jul 2025 | `black-forest-labs/flux2` (FLUX.2, nov 2025) |
| `deepseek-coder` | 2023, solo mantenimiento menor | `deepseek-ai/DeepSeek-V3` (modelo general actual con capacidad de código) |

Si solo se eliminan, el catálogo queda sin modelo de segmentación tipo SAM, sin FLUX y sin un repo de DeepSeek (AGENTS.md lo usa como referencia del modelo). Por eso se propone reemplazarlos con una ficha nueva revisada de cada versión.

## C. Inactivos más de 17 meses, con sustituto claro (3)

| Repo | Último commit | Sustituto |
|---|---|---|
| `sd-webui-forge` | jun 2025 | `comfyui` (Forge depende de AUTOMATIC1111, ya retirado) |
| `melotts` | dic 2024 | `kokoro`, `fish-speech` |
| `scrapydweb` | feb 2025 | `scrapy`, `crawl4ai` |

## Fichas nuevas

Cada una se escribió a partir del README oficial (SHA verificado contra el contenido) y la estructura raíz del repositorio. No se instalaron ni ejecutaron.

| Ficha | Repositorio | Sustituye a | Puntos clave de la ficha |
|---|---|---|---|
| `sam3` | `facebookresearch/sam3` | `sam2` | Segmentación por concepto con texto; GPU con CUDA 12.6+; pesos con acceso aprobado en Hugging Face; licencia SAM |
| `flux2` | `black-forest-labs/flux2` | `flux` | klein 4B con Apache 2.0 y unos 8 GB de VRAM; klein 9B y [dev] con licencia no comercial; API de BFL opcional |
| `deepseek-v3` | `deepseek-ai/DeepSeek-V3` | `deepseek-coder` | API de pago compatible con OpenAI; ruta local solo con servidores de varias GPU; código MIT y pesos con licencia de modelo que permite uso comercial |

Las nuevas fichas heredan las selecciones editoriales (`sam3` y `flux2`), objetivos, combinaciones y referencias de las que sustituyen; `deepseek-v3` pasa a ser el repo de referencia de DeepSeek en AGENTS.md. En el registro de retirados, `segment-anything` apunta ahora a `sam3`. Dos pruebas que usaban `fooocus` como ejemplo usan `comfyui` y la comparación `comfyui`/`wan2gp`.

## Revisados y conservados

- `graphrag`: modo mantenimiento, pero sigue recibiendo correcciones (último commit nov 2026).
- `defending-code-reference-harness`: implementación de referencia publicada en ago 2026; se publicó sin mantenimiento a propósito.
- `pdfmathtranslate`: la versión 1 sigue activa (commit de nov 2026); la 2.0 vive en `PDFMathTranslate-next`.
- `hunyuanvideo`: activo (oct 2026); la 1.5 es una variante ligera, no un reemplazo.
- Librerías estables o de referencia sin commits recientes: `audiocraft`, `rnnoise`, `rubberband`, `llm.c`, `kokoro`, `mmpose`, `storm`, `pandas-ai`, `12-factor-agents`, más los 8 conservados en la primera depuración.
