# Depuración: repos anticuados o sustituidos

Aplicada el 15 de noviembre de 2026 con aprobación expresa de la lista. Se retiraron **35 repos** (de 679 a 644 fichas públicas). Cada uno queda registrado en `data/retired.json` con motivo, evidencia, último commit y sustitutos del catálogo.

## Método

- Estado en GitHub consultado en vivo el 15/11/2026: archivado, renombrado y fecha del último commit en la rama principal (no `pushed_at`, que cambia con cualquier rama).
- Avisos en README y descripción de las instantáneas de `data/reviews/679-20261114/` («deprecated», «no longer maintained», «superseded», «moved to», «maintenance mode»…), revisados a mano para descartar falsos positivos (opciones obsoletas, modos de solo lectura, etc.).
- Sustitutos buscados en el propio catálogo y en `alt`.
- Ningún candidato a eliminar aparece en recetas, técnicas o plantillas. `real-esrgan` sí está en la receta de Reels y se conserva.

## 1. Eliminar: archivados o abandonados por sus autores (16)

| Repo | Evidencia | Sustituto en el catálogo |
|---|---|---|
| `flowise` | Archivado en GitHub (ago 2026): «Flowise has been archived» | `langflow`, `dify`, `sim` |
| `langchain-mcp-adapters` | Archivado; el soporte MCP pasó a LangChain | `langchain` |
| `langgraph-supervisor-py` | Archivado; recomiendan el patrón supervisor con tools | `langgraph` |
| `open-deep-research` | Archivado (ago 2026) | `local-deep-research`, `gpt-researcher` |
| `opencode-legacy` | Archivado; el proyecto continuó como Crush | `opencode` |
| `openscreen` | Archivado (oct 2026); remite a un fork comunitario | `obs-studio` |
| `py-clob-client` | Archivado: «no longer functional» | `py-sdk` |
| `supertonic` | Archivado; desarrollo y soporte terminados | `kokoro` |
| `crypto-trader` | Archivado; último commit 2019; remite a ccxt | `ccxt` |
| `videopose3d` | Archivado; último commit 2020 | `mediapipe` |
| `autogen` | README: «archived and no longer maintained» | `agent-framework`, `ag2` |
| `chatterbox` | README: investigación retirada desde ago 2026, sin mantenimiento | `fish-speech`, `kokoro` |
| `continue` | README: repositorio sin mantenimiento activo y de solo lectura | `cline`, `aider` |
| `nemo-agent-toolkit` | README: deprecado en oct 2026, fin de vida a final de 2026 | — (NeMo Relay no está en el catálogo) |
| `tts` (Coqui) | Empresa cerrada; sin commits desde feb 2024 | `kokoro`, `fish-speech` |
| `nanogpt` | El autor lo declara «very old and deprecated» | `nanochat` |

## 2. Eliminar: sustituidos por otro proyecto o versión (11)

| Repo | Evidencia | Sustituto |
|---|---|---|
| `semantic-kernel` | README: Microsoft Agent Framework es su sucesor | `agent-framework` |
| `segment-anything` | Sin commits desde sep 2024; README remite a SAM 2 | `sam2` |
| `swe-agent` | README: mini-swe-agent lo ha sustituido | `openhands` (mini-swe-agent no está en el catálogo) |
| `ltx-video` | README: LTX-2.5 sustituye a LTX-Video | `wan2-2`, `hunyuanvideo` (LTX-2 no está en el catálogo) |
| `stable-diffusion-webui` | AUTOMATIC1111: sin cambios en la rama principal desde jul 2024 | `comfyui` |
| `controlnet` | Código original sin commits desde sep 2023; integrado en las interfaces actuales | `comfyui` |
| `sd-webui-controlnet` | Extensión de AUTOMATIC1111; sin commits desde jul 2024 | `comfyui` |
| `backtrader` | Sin commits desde abr 2023 | `nautilus-trader` |
| `snscrape` | Sin commits desde jun 2023; dejó de funcionar con X/Twitter | `agent-reach` |
| `scrapely` | Sin commits desde nov 2019 | `scrapy`, `crawl4ai` |
| `gfpgan` | Sin commits desde abr 2024 | `codeformer` |

## 3. Eliminar: sin actividad en años y poco valor actual (8)

| Repo | Último commit | Motivo |
|---|---|---|
| `stocks-analyst` | 2016-02 | 28 estrellas, código de 2016 |
| `chartanalyst` | 2016-07 | 21 estrellas, código de 2016 |
| `bigdata` | 2017-01 | Material de 2017 |
| `machinelearning` | 2017-07 | Apuntes de 2017 |
| `intellitrader` | 2018-07 | Bot de trading sin mantenimiento (riesgo al operar) |
| `data-science-ipython-notebooks` | 2019-02 | Cuadernos de 2019, versiones de librerías antiguas |
| `dataanalystportfolioprojects` | 2022-02 | Proyectos de portafolio personal, sin actualizar |
| `youtube2webpage` | 2023-12 | Script sin mantenimiento |

## 4. Conservar aunque sean antiguos (8)

| Repo | Último commit | Por qué conservarlo |
|---|---|---|
| `real-esrgan` | 2024-04 | Sigue siendo el estándar de ampliación; está en la receta de Reels |
| `normalize.css` | 2018-11 | Proyecto terminado y estable |
| `webgl-noise` | 2024-11 | Librería terminada |
| `zdog` | 2022-01 | Librería estable sin sustituto directo |
| `scenejs` | 2023-06 | Librería estable sin sustituto directo |
| `openpose` | 2024-08 | Referencia clásica de pose; muchos flujos lo siguen usando |
| `wham` | 2024-04 | Código de investigación aún citado |
| `prompt-eng-tutorial` | 2024-04 | Tutorial oficial de Anthropic; los principios siguen vigentes |

## 5. Actualizar en vez de eliminar (1)

| Repo | Situación | Acción |
|---|---|---|
| `pdfding` | GitHub archivado porque el proyecto se mudó a Codeberg; sigue activo | Cambiar la fuente a `codeberg.org/mrmn/PdfDing` |

## También revisados, sin cambios

En modo mantenimiento pero vigentes: `rasa`, `graphrag`. Poco activos (15 a 24 meses), sin aviso de abandono: `melotts`, `scrapydweb`, `rnnoise`, `rubberband`, `audiocraft`, `comfyui-ipadapter-plus`, `llm.c`, `sam2`, `sd-webui-forge`.

## Cambios aplicados

- Fichas retiradas de `INDICE_IA.json` e `INDICE_IA.detalle.json`; sus páginas en `human/fichas/` se eliminan al regenerar.
- Referencias limpiadas en `alt` (sigue siendo simétrico), `alternatives`, `combines_with`, arranques de áreas, temas de configuración de clientes, objetivos guiados y comparaciones.
- `comfyui` pasa a ser la selección editorial de «Interfaces para generar imágenes», en lugar de AUTOMATIC1111. `nautilus-trader` sustituye a `backtrader` entre los arranques del área de trading.
- Dos técnicas actualizadas: la de video menciona LTX-2 en lugar de LTX-Video, y la de backtesting propone NautilusTrader en lugar de Backtrader.
- `scripts/daily_stars.py` omite los repos de `data/retired.json`, aunque sigan con star.
- El registro histórico de la revisión de 679 fichas (`curation/review-679-2026-11-14/`, `reports/review-679-2026-11-14.json`) no se modifica. Las pruebas comprueban que lo retirado está documentado.

`pdfding` se actualizó después con aprobación: su ficha enlaza `codeberg.org/mrmn/PdfDing`, la revisión toma como fuente el README de Codeberg (SHA `5a397cd`) y deja de mostrarse como archivado. Conserva su identidad de GitHub para que la sincronización de stars no lo duplique.
