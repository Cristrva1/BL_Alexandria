# 🤖 AGENTS.md — Punto de entrada para agentes de IA

Esta biblioteca contiene **156 repositorios** de IA y automatización, ya analizados, comparados y clasificados. Este archivo te dice cómo elegir los repos correctos **gastando el mínimo de tokens**. Léelo entero (es corto); luego abre solo lo que necesites.

---

## ⚡ TL;DR — protocolo de selección (en orden)

0. **Si el usuario ya describió un proyecto concreto**, genera primero su superguía:
   `uv run repo-intelligence recommend --tool <herramienta> --project "<descripcion>" --max-repos 7`.
   Luego lee `ai_index/SUPERGUIAS/<proyecto>.md` o `ai_index/CONTEXT_PACKS/latest.md`. Esa guía ya trae finalistas, orden, instalación y cautelas.
1. **Lee `INDICE_IA.json`** (índice compacto, 1 línea por repo). Es la única lectura obligatoria. No abras los `.md` todavía.
2. **Filtra candidatos** por `cat` (categoría), `tags`, `role`, `exec`, `setup`, `prov` (proveedor LLM) y palabras de `one` (resumen de una línea).
3. **Desempata** entre repos parecidos con el campo `alt` (alternativas): si ya elegiste uno, **descarta sus `alt`** — cumplen la misma función, no necesitas dos.
4. **Combina** con `recipes` (stacks completos ya probados) si el proyecto necesita un flujo end-to-end, no una pieza suelta.
5. **Considera la herramienta del usuario** (Antigravity, Codex, Claude Code, Grok, Deepseek) con `model_guidance` y el campo opcional `agent_tools`. Ver regla abajo.
6. **Solo para los finalistas (<8 repos)**: abre `INDICE_IA.detalle.json` por `id`, o la ficha humana en el campo `doc` (`guia/NN-*.md#ancla`). Ahí está stack, instalación, "elige si / evita si" y "combina con".

> Coste: pasos 1-5 ≈ un solo archivo (~20k tokens). No leas `Guia.md` (es el documento monolítico viejo) ni las 13 fichas completas salvo que hayas reducido la lista.

---

## 🗺️ Archivos de esta biblioteca

| Archivo | Para qué | Cuándo leerlo |
|---|---|---|
| **`AGENTS.md`** (este) | Instrucciones de navegación | Primero, siempre |
| **`INDICE_IA.json`** | Índice **compacto** (scan): id, cat, tags, role, exec, setup, prov, resumen, alternativas | Para preseleccionar (lectura principal) |
| **`INDICE_IA.detalle.json`** | Detalle por `id`: desc completa, stack, choose_if, avoid_if, combines_with | Solo para finalistas |
| **`ai_index/SUPERGUIAS/*.md`** | Superguías generadas por proyecto: finalistas, por qué, cómo, orden, global/local/Docker/referencia | Primero si ya hay una descripción de proyecto |
| **`ai_index/CONTEXT_PACKS/latest.md`** | Alias de la última superguía generada | Para continuar la última recomendación |
| **`guia/NN-*.md`** | Ficha **humana** completa por categoría (13 archivos) | Lectura humana o detalle máximo |
| **`guia/README.md`** | Mapa de categorías + leyenda + recetas (versión humana) | Navegación humana |
| **`Catalogo.md`** | Tabla plana de los 156 repos (instalación + API) | Referencia rápida tabular |

---

## 🧠 Regla clave: herramienta de código ≠ modelo en ejecución

Separa **dos** decisiones que se confunden:

- **(a) El agente/IDE con el que CONSTRUYES** — Antigravity, Codex, Claude Code, Grok, Deepseek-coder. Solo importa para los repos de tipo **`skill`/`directory`** (catálogos de skills, plugins, playbooks). Ahí mira `agent_tools`.
- **(b) El LLM que tu APP llama EN EJECUCIÓN** — campo `prov` (`openai`/`anthropic`/`google`/`mcp`/`local`). **La mayoría de repos runtime son agnósticos**: el proveedor se configura por variables de entorno. No descartes un repo runtime por la herramienta de código del usuario.

**Resumen por herramienta** (detalle en `model_guidance` del JSON):

| Herramienta | Repos específicos que le sirven |
|---|---|
| **Claude Code** | `claude-plugins-official`, `awesome-claude-code`, `superpowers`, `skills`, `agent-toolkit`, `n8n-skills`, `geo-seo-claude`, `agency-agents` |
| **Antigravity** | `antigravity-awesome-skills` (nativo), `awesome-agent-skills`, `prompt-master` |
| **Codex** | `antigravity-awesome-skills`, `awesome-agent-skills`, `marketingskills`, `taste-skill` (catálogos cross-tool) |
| **Grok** | Ninguno específico — úsalo como proveedor LLM; los repos runtime lo aceptan vía API |
| **Deepseek** | `deepseek-coder` (es el modelo); el resto es agnóstico vía proveedor compatible OpenAI |

---

## 📂 Categorías (156 repos)

| # | Categoría | Repos | Archivo |
|---|---|---|---|
| 1 | Automatización, Mensajería & CRM | 12 | `guia/01-automatizacion-mensajeria-crm.md` |
| 2 | Skills, Prompts & Guías de Agente | 21 | `guia/02-skills-prompts-guias-de-agente.md` |
| 3 | Frameworks & Orquestación de Agentes | 18 | `guia/03-frameworks-orquestacion-de-agentes.md` |
| 4 | Scraping, Búsqueda & Research Web | 14 | `guia/04-scraping-busqueda-research-web.md` |
| 5 | MCP & Conectividad | 7 | `guia/05-mcp-conectividad.md` |
| 6 | Memoria, LLM Ops & Observabilidad | 10 | `guia/06-memoria-llm-ops-observabilidad.md` |
| 7 | Inteligencia de Código, Datos & Entrenamiento | 13 | `guia/07-inteligencia-de-codigo-datos-entrenamiento.md` |
| 8 | Workspaces de IA Local & Notebooks | 5 | `guia/08-workspaces-de-ia-local-notebooks.md` |
| 9 | Diseño, UI & Frontend | 15 | `guia/09-diseno-ui-frontend.md` |
| 10 | Analítica & Visualización | 7 | `guia/10-analitica-visualizacion.md` |
| 11 | Generación de Imagen & Visión | 15 | `guia/11-generacion-de-imagen-vision.md` |
| 12 | Audio, Voz & Video | 15 | `guia/12-audio-voz-video.md` |
| 13 | Documentos & Presentaciones | 4 | `guia/13-documentos-presentaciones.md` |

---

## 🔗 Recetas (stacks end-to-end listos)

Cuando el usuario describe un **producto** (no una pieza), busca primero la receta y parte de ahí (detalle completo en `recipes` del JSON):

1. **Bot de WhatsApp con IA** → evolution-api + n8n (+ n8n-mcp, n8n-skills) + chatwoot + novu
2. **Pipeline de Reels / video corto** → whisperX + supertonic/TTS + ComfyUI/Fooocus + Real-ESRGAN + moviepy/remotion + lossless-cut
3. **Agente de research profundo** → gpt-researcher/deer-flow + firecrawl/crawl4ai + browser-use + markitdown + langfuse
4. **Workspace privado local soberano** → odysseus + open-notebook + ECC + mem0
5. **Análisis de repos grandes** → codegraph + graphify/graphrag + GitNexus
6. **Marketing de agencia** → marketingskills + agency-agents + mautic + listmonk + posthog/metabase
7. **Web app moderna con IA** → open-design/plasmic + tailwindcss + heroui/ui + GSAP/motion/three.js + swr + echarts/uPlot
8. **Construir una app/servidor MCP** → mcp-use + mcp + servers + awesome-mcp-servers
9. **Documentos → presentaciones** → markitdown + ppt-master/reveal.js

---

## 🏷️ Leyenda de campos (índice)

- **`exec`**: `local` 🏠 · `cloud` ☁️ · `hybrid` 🔀
- **`role`**: `platform` (plataforma) · `runtime` (motor) · `library` (lib/SDK) · `skill` (skill/prompt) · `directory` (catálogo) · `app` (app/UI)
- **`setup`**: `easy` 🟢 · `medium` 🟡 · `heavy` 🔴 (GPU/infra)
- **`mcp`**: `true` si expone/consume Model Context Protocol
- **`prov`**: APIs/LLM declarados. `[]` = no declarado (NO implica incompatibilidad)
- **`alt`**: repos sustitutos (elige uno) · **`combines_with`** (en detalle): repos complementarios (úsalos juntos)

---

## 🔧 Mantenimiento (para humanos)

La **fuente de verdad** son los `guia/NN-*.md`. Para enriquecer: edita la ficha en su `.md` (respeta el formato de campos `**Qué es:** / **Stack:** / **Elige si:** …`) y regenera los índices:

```bash
python tools/regenerar_indice.py
```

Eso reconstruye `INDICE_IA.json` y `INDICE_IA.detalle.json` desde los `.md`.
