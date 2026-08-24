# Mapa de BL_Alexandria (Repo Intelligence Hub)

Paquete: `repo-intelligence-hub` 0.1.0 (`pyproject.toml`). CLI: `repo-intelligence` → `repo_intelligence.cli:app`. Python ≥3.11 (el entorno local corre 3.13).

Este documento es el mapa persistente del análisis. No se recorrieron las 191 fichas humanas ni los clones de `../Repositorios_Prueba` archivo por archivo. El contrato de fichas se tomó de `guides/render.py:_render_cards` y de `human/fichas/n8n.md`. El algoritmo de recomendación se tomó de `analysis/recommend.py` entero y de `tests/test_recommend.py`. Conteos verificados el 2026-08-23.

---

## 1. Propósito

Repo Intelligence Hub decide **qué repositorios de una biblioteca local de IA** usar para un proyecto concreto, y **mantiene índices compactos** para humanos y agentes.

El usuario llega con una idea y (opcionalmente) la herramienta con la que construye (Codex, Claude Code, Antigravity, Grok Build, Open Code). El sistema responde: qué instalar, en qué modo, en qué orden, qué leer solo, qué diferir. No instala nada por sí solo.

La biblioteca de clones vive en `../Repositorios_Prueba` (`config/paths.yaml` → `repo_library`). Este repo (`BL_Alexandria`) es el hub de inteligencia, no los clones.

V1 es **determinista y local**. No llama a OpenAI/Anthropic/Gemini/Grok. `src/repo_intelligence/llm/__init__.py` está vacío. `crawl4ai` existe como runner de red pero **no está cableado** al CLI.

---

## 2. Qué no es

- No es un orquestador multiagente ni un runtime de LLM.
- No instala repos, skills ni Docker de forma automática.
- `Guia_IDE.md` no es el catálogo: es un ensayo que separa modelo ≠ agente de código ≠ superficie ≠ ecosistema.
- `guias/*.md` y el cuerpo de `Guia.md` no son la fuente de verdad del motor: son catálogo editorial humano.
- No es un SaaS. Toda decisión de `recommend` sale de JSON local.

---

## 3. Fuentes de verdad vs salidas generadas

Hay **tres capas** que a veces se tratan como una sola.

### Fuente de verdad curada (se edita a mano o vía `enrich --auto-merge`)

| Archivo | Forma | Conteos 2026-08-23 |
|---|---|---|
| `INDICE_IA.json` | lista `repos[]` | 185 |
| `INDICE_IA.detalle.json` | dict `repos.<id>` | 186 (extra: `ui-shadcn`) |

Campos compactos reales: `id`, `name`, `cat`, `role`, `exec`, `setup`, `mcp`, `prov`, `tags`, `one`, `alt`, `doc`. El `meta.fields` documenta `agent_tools`; **cero repos** lo tienen.

Campos detalle reales: `name`, `cat`, `desc`, `stack`, `choose_if`, `avoid_if`, `combines_with`, `alternatives`, `repo`, `doc`. Algunos tienen `models_note`.

### Inventario descubierto

| Archivo | Generado por | Conteos |
|---|---|---|
| `registry/repos.yaml` | `discover` | 185 (`generated_at` 2026-06-25) |
| `ai_index/REPOS.scan.json` | `discover` / `scan` via `build_scan_index` | 185, lista |
| `data/snapshots/snapshot_*.json` | `snapshot` | dump de `RepoRecord` |
| `data/extracted/<id>/readme.md` | `analyze` o `scripts/extract_all_readmes.py` | 185 carpetas, 184 README, 1 `NO_README.txt` (`tools`) |
| `data/extracted/MANIFEST.json` | script de extracción | 185 entradas |
| `data/packed/` | `analyze` / repomix | **vacío** |
| `data/drafts/<id>.json` | `enrich` | 185 |

### Salidas generadas

| Archivo | Generado por |
|---|---|
| `ai_index/REPOS.detail.json` | `guide build` (`_render_detail_index`) — **lista**, 186 |
| `Catalogo.md`, `human/catalogo.md` | `guide build` |
| `human/README.md`, `human/categorias/`, `human/fichas/` (191), `human/comparativas/` (61), `human/playbooks/` (9), `human/usar-ahora.md`, `human/diferir.md`, `human/descartar.md`, `human/guia-generada.md` | `guide build` |
| `Guia.md` (conteos + apéndice) | `guide build` **no reescribe el cuerpo** si detecta el título rico |
| `menu_portable/` | `menu export` |
| `ai_index/SUPERGUIAS/<slug>.md`, `ai_index/CONTEXT_PACKS/latest.md`, `data/decisions/<slug>.json` | `recommend` / `context build` |

### Editorial híbrido (fuera del generador principal)

| Archivo | Origen |
|---|---|
| `Guia.md` cuerpo | manual; `guide build` solo actualiza `<!-- BL_ALEXANDRIA_STATUS -->` y el apéndice `<!-- BL_ALEXANDRIA_AUTO_APPEND_* -->` |
| `guias/guia1.md` … `guia5.md` | split manual de `Guia.md`; **`render_all` no los toca** |
| `AGENTS.md`, `README.md`, `Guia_IDE.md`, `PLAN_*.md`, `proyecto.md` | manual |

`tools_check/mirror_to_guia.py` espeja `guias/` → `Guia.md`. `tools_check/reconcile_json.py` empuja prosa de `guias/` hacia `INDICE_IA*.json`. `tools_check/check_guias.py` espera **156** fichas `**Repo:**` — cifra del catálogo editorial, no del índice JSON (185).

### Markdown por familia (inventario)

Raíz: 8 `.md`. `human/fichas` 191, `human/comparativas` 61, `human/categorias` 13, `human/playbooks` 9, `guias` 5, `menu_portable/REPO_MENU_cats` 13, `ai_index/SUPERGUIAS` 3, más ~184 README extraídos.

Dos contratos de “ficha”:

- Editorial (`Guia.md` / `guias/`): Qué es, Por qué destaca, Cómo funciona, Instalación, Casos, Stack, Elige si / Evita si, Combina con, Repo.
- Generada (`human/fichas/`): Decision, Para que sirve, Que problema resuelve, Por que tiene valor, Cuando usarlo / NO, Tipo de instalacion, Stack, Instalacion detectada, Combina, Compite, Riesgos, Ideas, Veredicto.

---

## 4. Workflow A — recommend

```text
brief (--project y/o --project-file)
  -> recommend()
       lee  ai_index/REPOS.scan.json
            ai_index/REPOS.detail.json   (lista)
            ai_index/WINNERS.json
       NO lee INDICE_IA.json
  -> score_repo por cada repo del scan (descarta score <= 0)
  -> ordena por (score, mode_priority)
  -> _dedupe_alternatives (bloquea alt/alternatives)
  -> _ensure_capability_coverage (puede sustituir un finalista)
  -> _enrich_recommendation (REPO_GUIDANCE o defaults)
  -> escribe data/decisions/<slug>.json
            ai_index/SUPERGUIAS/<slug>.md
            ai_index/CONTEXT_PACKS/latest.md   (misma prosa)
```

`context build` es el mismo camino con default `max_repos=3` y query vacía → texto “general repository intelligence project”.

Si `build_tool=auto` y el brief no nombra herramienta, `_detect_effective_tool` **cae a `codex`**. Si el texto contiene “claude” / “claude code”, gana `claude-code` aunque `--tool` diga otra cosa: **el texto del proyecto manda**.

### Ejemplo real en disco

`data/decisions/bot-de-whatsapp-con-ia-para-responder-clientes.json` (brief sin herramienta, `requested_tool: auto`):

| id | score | install_mode |
|---|---:|---|
| evolution-api | 17 | docker_local |
| n8n | 12 | docker_local |
| whatsapp-agentkit | 11 | reference_only |
| chatwoot | 10 | docker_local |
| awesome-agent-skills | 10 | reference_only |

`awesome-agent-skills` entra por el default `codex` (`BUILD_TOOL_REPOS["codex"]` +10), no porque el brief pida un catálogo de skills. La receta documentada en `AGENTS.md` / `recipes` (evolution-api, n8n, n8n-mcp, n8n-skills, chatwoot, novu) **no se aplica como receta**: `recommend` no lee `recipes`. Solo hay boosts de dominio (`DOMAIN_BOOSTS["whatsapp"]`).

---

## 5. Workflow B — mantenimiento de biblioteca

Documentado en `README.md` y `AGENTS.md`. Código real:

```text
clones en ../Repositorios_Prueba   (un nivel, cada subcarpeta)
  doctor          paths + which(git,gh,node,npm,pnpm,uv,docker,repomix,gitnexus,markitdown)
  pull --safe     git pull --ff-only; skip dirty / no-git; --no-safe error V1
  discover        registry/repos.yaml + REPOS.scan.json
  snapshot        data/snapshots/snapshot_<UTC>.json
  scan            rebuild scan (flag --changed-only ignorado)
  analyze --new   data/packed/<id>.xml + data/extracted/<id>/readme.md
  enrich --new [--auto-merge]   data/drafts/<id>.json  [+ INDICE_IA*.json]
  guide build     human/*, Catalogo.md, REPOS.detail.json, conteos Guia.md
  menu export     menu_portable/
  score / conflicts / decide / report daily     STUBS
```

Al agregar un repo nuevo el flujo integral es: clonar → `discover` → `analyze --new` → `enrich --new --auto-merge` → revisar JSON → `guide build` → `menu export`.

`PLAN_ENRIQUECER_GUIAS.md` avisa: **no** correr `enrich --auto-merge` después de editar JSON/guías a mano; regeneraría `choose_if`/`avoid_if` desde drafts.

Doctor en esta máquina (2026-08-23): todo OK, incluida la biblioteca en `C:\Users\criss\Desktop\Claude\Repositorios_Prueba`.

---

## 6. CLI completo

Entrada: `src/repo_intelligence/cli.py`. 15 comandos. Sin subcomandos ocultos.

| Comando | Función | Escribe | Red | Stub |
|---|---|---|---|---|
| `doctor` | `doctor` | nada | no | no |
| `discover [--base]` | `discover` | `registry/repos.yaml`, `REPOS.scan.json` | no | no |
| `snapshot` | `snapshot` | `data/snapshots/snapshot_*.json` | no | no |
| `pull --safe` | `pull` | working trees git | sí | `--no-safe` rechazado |
| `scan [--changed-only]` | `scan` | `REPOS.scan.json` | no | flag ignorado |
| `score` | `score` | `data/reports/score.json` | no | **sí** `v1_placeholder` |
| `conflicts` | `conflicts` | `ai_index/CONFLICTS.json` | no | **sí** n8n vs activepieces |
| `decide --project-type` | `decide` | `data/decisions/<type>.md` | no | **sí** hardcode |
| `recommend -p/--project-file/--tool/--max-repos` | `recommend_project` | decisions json + 2 md | no | no |
| `guide build [--changed-only]` | `guide_build` | human/*, Catalogo, detail, Guia conteos | no | flag ignorado |
| `menu export -o` | `menu_export` | `menu_portable/` | no | no |
| `context build` | `context_build` | igual que recommend | no | no |
| `report daily` | `report_daily` | `data/reports/daily.md` | no | **sí** |
| `analyze [--new --id --force]` | `analyze` | packed + extracted | tools locales | no |
| `enrich [--new --id --auto-merge --force]` | `enrich` | drafts [+ INDICE] | no | `--id` **se declara y no se pasa** a `run_enrich_for_new` |

Helpers: `_load_project_text` concatena `--project` y archivo (error si ambos vacíos); `_now` ISO UTC; `_first_line` para tablas Rich.

---

## 7. Algoritmo de scoring

Archivo: `src/repo_intelligence/analysis/recommend.py`. `config/scoring_rules.yaml` **no alimenta** este código.

### `score_repo` (sin early-exit; el corte `score <= 0` es en `recommend`)

Haystack normalizado: `id name role one tags desc choose_if stack`.

| Orden | Término | Puntos |
|---|---|---|
| 1 | Overlap de tokens (≥4 chars, sin stopwords) | `min(len, 8)` |
| 2 | Tag del repo cuya sinonimia aparece en el brief (`TAG_SYNONYMS`) | +8 por tag |
| 3 | `role` skill/directory y el brief contiene codex/claude/antigravity/skill(s) | +5 |
| 4 | MCP en repo y “mcp” en el brief | +8 |
| 5 | `BUILD_TOOL_REPOS[effective_tool][id]` | 0–10 |
| 6 | `DOMAIN_BOOSTS` si tokens del brief cruzan keywords del dominio | suma (p. ej. whatsapp→evolution-api +16) |
| 7 | `INTENT_BOOSTS` | hasta +30 (superpowers en agent_ide_optimization); −10 si skill condicional sin términos |
| 8 | `_should_suppress_for_intent` | −18 |
| 9 | install_mode deferred −4; local_project/global +2 | |

Dominios con receta dura: whatsapp, mcp, research, video, frontend, marketing, documents.

Herramientas: claude-code, codex, antigravity, open-code. `grok-build` y `grok` tienen mapas **vacíos**.

Intenciones (solo dos): `agent_ide_optimization` (herramienta nombrada + señal de optimizar/skills/plugins/…) y `claude_code_daily` (hace falta la frase “claude code”). Con esas intenciones, repos que no están en `REPO_GUIDANCE` / allowlist / cat 2 skill|directory se penalizan −18. Eso es lo que el test usa para echar `awesome-bigdata`.

### Post-score

1. `_dedupe_alternatives`: si entra A, bloquea `alt` y `alternatives` de A.
2. `_infer_required_capabilities` desde `TAG_SYNONYMS` + señales extra (RAG, CRM, dashboard, 24/7, multiagente).
3. `_effective_max_repos` puede subir el tope a 6 u 8 si hay muchas capacidades fuertes; nunca lo baja.
4. `_ensure_capability_coverage`: si una capacidad fuerte no está cubierta, añade o **sustituye** al finalista más barato. Protegidos: `superpowers`, `agent-toolkit`, `claude-plugins-official`.
5. `_enrich_recommendation`: 9 repos tienen prosa custom (`REPO_GUIDANCE`). El resto usa `_default_*`.

Ancla de tests: brief “Quiero optimizar y ultralizar Claude Code para uso diario”, `max_repos=7`, `auto` → ids exactos `superpowers, agent-toolkit, claude-plugins-official, awesome-claude-code, skillspector, context-engineering, prompt-master`.

### Tres `_install_mode` distintos (desajuste)

| Módulo | docker_local n8n/evolution-api/… | litellm | REPO_GUIDANCE | fallback |
|---|---|---|---|---|
| `recommend._install_mode` | sí | local_project | sí | campo del repo o reference_only |
| `build_scan._install_mode` | no | no | no | siempre reference_only |
| `guides/render._install_mode` | no | no | no | siempre reference_only |

Por eso `Catalogo.md` y `human/fichas/n8n.md` marcan n8n como `reference_only` / REFERENCIA, mientras `recommend` lo pone `docker_local`. Scan: 157 reference_only, 24 deferred, 2 local_project (`markitdown`, `crawl4ai`), 2 global (`repomix`, `gitnexus`).

---

## 8. Pipeline analyze → enrich → guide → menu

### Extract

`extract/readme.py`: busca `README.md/.rst/.markdown/.html/.txt` y fallback case-insensitive. `read_readme_text` default **50000** chars (el plan `PLAN_EXTRACCION_READMES.md` habla de 8000; eso ya se cambió). Extrae título+desc, features, stack heurístico, hints de install.

`extract/manifests.py`: `package.json`, `pyproject.toml`, `requirements.txt`, `setup.py`, `uv.lock`, locks npm/pnpm, docker-compose, Dockerfile. Solo raíz del clone.

### Runners (`tools/`)

| Runner | Artefacto | Red | Guardia |
|---|---|---|---|
| `repomix_runner.pack_repo` | `data/packed/<id>.xml` | no | `which` en `ensure_analyzed` |
| `markitdown_runner.convert_to_markdown` | `data/extracted/<id>/readme.md` | no | fallback: copia raw |
| `gitnexus_runner.analyze_repo` | escribe **dentro del clone** (`gitnexus analyze .`) | no | `which`; excepciones tragadas |
| `crawl4ai_docs.crawl_url` | string in-memory | **sí** | no usado por CLI |

Hoy `data/packed/` está vacío: analyze se ha corrido en modo light o repomix no produjo archivos persistidos en el hub.

### Curation (`analysis/curation.py`)

1. `get_new_repo_ids` — registry minus compact.
2. `ensure_analyzed` — tools si existen.
3. `build_profile` — prefiere README completo de `data/extracted/`.
4. `infer_category` — 13 cubos de keywords; empate favorece número de cat más bajo.
5. `infer_role_exec_setup` — defaults `library / local / medium`.
6. `infer_tags` — máximo 8.
7. `build_draft_entries` — compact + detalle. `choose_if` template `"quieres {title}"`; `avoid_if` genérico. `combines_with` = hasta 3 ids de la misma cat. Marca `_auto`.
8. `save_draft` → `data/drafts/<id>.json`.
9. `merge_into_indices` — preserva `one/tags/alt/prov/desc/choose_if/avoid_if/combines_with/stack` si el draft viene vacío.

`analysis/decisions.py` (`INITIAL_DECISIONS`) **no lo importa el CLI** `decide`.

### `guide build` (`guides/render.py`)

Lee compact + detalle + scan + registry + drafts. Emite el árbol `human/` y `REPOS.detail.json`.

`Guia.md`: si el archivo existe y contiene `# 🌌 Catálogo de Repositorios de IA & Automatización`, no se sustituye por la guía simple (`human/guia-generada.md`). Solo cambia el conteo y, si faltan repos sin heading `###` ni link a ficha, añade el apéndice automático. Tests en `tests/test_render_guide.py` fijan esa no-destrucción (menciones e hipervínculos internos **no** cuentan como ficha).

`guias/*.md` no se escriben aquí.

Comparativas: un archivo por par no dirigido de `compact.alt`. n8n tiene `alt: []`, así que **no** hay `n8n-vs-activepieces.md`; sí hay `n8n-io-vs-n8n.md`. El conflicto n8n/activepieces vive solo en el stub `CONFLICTS.json`.

Playbooks: un md por `recipes[]` de compact.

### `menu export` (`menu/export.py`)

Lee **`INDICE_IA.json` + `INDICE_IA.detalle.json`** (no el scan). `derive_install` infiere comando y confianza `+` / `~` / `?` según role/exec/stack. Escribe `REPO_MENU.md`, `REPO_MENU_cats/01-*.md`…, `REPO_MENU_DATA.json`. El protocolo de 5+1 pasos vive en el propio menú.

---

## 9. Modelos y esquemas JSON

### Pydantic (`core/models.py`)

- `RepoRecord`: id, name, path, is_git, head, branch, dirty, remotes, readme, manifests, install_mode. Lo usa discover/snapshot/scan.
- `ScanRepo`: id, name, role, exec, setup, tags, one, install_mode, decision, alt, path.

`recommend` **no usa Pydantic**: trabaja dicts.

### Compact vs detalle vs scan vs detail operativo

| | compact | detalle curado | scan | detail operativo |
|---|---|---|---|---|
| Archivo | `INDICE_IA.json` | `INDICE_IA.detalle.json` | `ai_index/REPOS.scan.json` | `ai_index/REPOS.detail.json` |
| `repos` | lista 185 | **dict** 186 | lista 185 | **lista** 186 |
| Quién lo lee | agentes humanos, guide, menu, scan-match, enrich | guide, menu, enrich | **recommend**, guide merge | **recommend** |

`recommend` indexa detail operativo con `{item["id"]: item for item in detail["repos"]}` — exige lista.

Recetas compactas (9): `id`, `title`, `goal`, `repos`, `how` (a menudo `null`). `categories[]`: `num`, `title`, `file`, `count`. Los `count` del JSON de categorías **están desfasados** respecto al Counter real (p. ej. cat 1 declara 12 y hay 17 compactos).

`WINNERS.json`: cinco tipos de problema (library management, context packaging, structure analysis, document conversion, web docs). Lo usa recommend para `global_tools` extra y `avoid_by_default`.

`ROUTER.json`: qué leer primero según intención (recommend / decidir / analizar finalista / extraer docs). No lo ejecuta el código; es protocolo para agentes.

IDs compactos vs scan: conjuntos iguales (185). Extra en detalle: `ui-shadcn` (alias; `SCAN_ALIASES = {"ui": "ui-shadcn"}` en render). Compact `cat: 0`: solo `tools` (`one` vacío).

Roles compactos: library 47, platform 41, skill 41, runtime 25, directory 21, app 10. Exec: local 97, hybrid 77, cloud 11. Setup: medium 136, heavy 37, easy 12. `mcp: true` en 9.

---

## 10. Config cableada vs config huérfana

`ProjectPaths.load()` solo lee `config/paths.yaml`. `INDICE_IA.json` **no** está en `ProjectPaths`; guide/curation/scan/menu lo hardcodean como `project_root / "INDICE_IA.json"`.

| Archivo | En `src/` |
|---|---|
| `config/paths.yaml` | **usado** (`core/paths.py`) |
| `config/scoring_rules.yaml` | mencionado como string en el stub `score`; **nunca se carga** |
| `config/repo_policy.yaml` | **huérfano** |
| `config/project_types.yaml` | **huérfano** (el runtime usa `WINNERS.json`) |
| `config/install_allowlist.yaml` | **huérfano** |
| `config/ignore_patterns.yaml` | **huérfano** (`discover` no filtra hijos) |
| `registry/external_tools.yaml` | **huérfano** (tools globales hardcodeadas en `recommend._global_tools_for_project`) |

`discover_repos` recorre **solo el primer nivel** de `repo_library`, incluye carpetas no-git, no aplica ignore_patterns.

IO: `core/io.py` usa `json` stdlib + `yaml`. No orjson.

---

## 11. Tests y huecos

`uv run pytest -v` → **11 passed** (2026-08-23, 0.74s).

| Área | Tests |
|---|---|
| `discover_repos` | 1 (directorio vacío) |
| `recommend` | 5 (inferencia Claude Code, alias `--tool claude`, capabilities, max_repos, paths públicos) |
| `_update_rich_root_guide` | 5 (no pisar cuerpo, apéndice, conteos, menciones, links) |
| resto del CLI | **ninguno** |

No hay tests de analyze, enrich, menu export, pull, scan, doctor, ni de los stubs.

`scripts/`:

- `extract_all_readmes.py` — copia README completo + `MANIFEST.json` (ya corrido: 185).
- `recurate_all.py` — `run_enrich_for_new(only_new=False, auto_merge=True)`. Mutante.
- `verify_extraction.py` — umbral ≥185, campos, zip de backup.

`tools_check/check_guias.py` `EXPECTED_TOTAL = 156` no coincide con 185 compactos: vigila el catálogo editorial, no el índice.

Infra: `infra/n8n/docker-compose.yml` (puerto 5678) y `infra/litellm/config.yaml` (`repo-cheap` / `repo-strong`) son semillas. El CLI no las levanta; `recommend` solo dice “preparar en `infra/`”.

---

## 12. Stubs y deuda V1

Stubs de CLI: `score`, `conflicts`, `decide`, `report daily`.

Flags aceptados y no implementados: `scan --changed-only`, `guide build --changed-only`. `enrich --id` se parsea y se ignora.

Paquete `llm/` vacío.

`crawl4ai_docs` no tiene comando CLI.

Gitnexus no deja artefactos en `data/`.

`data/packed/` vacío pese a que `doctor` ve `repomix` OK.

Dependencias declaradas y **no importadas** en `src/`: duckdb, sqlalchemy, networkx, pandas, jinja2, rapidfuzz, loguru, orjson, unidiff, GitPython, python-dotenv, requests. Git se llama por `subprocess`, no GitPython. `markitdown` se llama por CLI.

`PLAN_EXTRACCION_READMES.md` y `PLAN_ENRIQUECER_GUIAS.md` describen un estado anterior (177 en índice, 21 extracted, 156 fichas JSON, 11 clones huérfanos, `one` vacío en 7 repos, `.rst` no detectado). Hoy: 185/186, 185 extracted, `find_readme` incluye `.rst`, `one` vacío solo en `tools`. Los planes siguen siendo útiles como historial, no como foto actual.

---

## 13. Cómo debe leer este repo un agente (protocolo confirmado)

Para **usar la biblioteca** (elegir repos de un brief):

1. `uv run repo-intelligence recommend --project "…" --max-repos 7` (o `--project-file`).
2. Leer `ai_index/SUPERGUIAS/<slug>.md` o `ai_index/CONTEXT_PACKS/latest.md`.
3. No leer `Guia.md` ni clones salvo finalistas.

Para **navegar a mano** sin recommend (lo que dice `AGENTS.md`):

1. `INDICE_IA.json` (único obligatorio).
2. Filtrar `cat/tags/role/exec/setup/prov/one`.
3. Desempatar con `alt`.
4. Combinar con `recipes` si es un producto.
5. Herramienta de construcción ≠ `prov` del runtime.
6. Detalle solo para <8 finalistas: `INDICE_IA.detalle.json` o `human/fichas/<id>.md`.

Ojo: el protocolo de `AGENTS.md` y el motor `recommend` **no leen el mismo índice**. Si scan y compact divergen, un agente que siga AGENTS.md y el CLI pueden discrepar. Hoy los ids coinciden (185).

Para **cambiar el hub** (código de este repo): este mapa + `src/repo_intelligence/cli.py` + el módulo citado. No regenerar catálogos a menos que el usuario lo pida.

Reglas de producto (README): no instalar todos los repos; no instalar catálogos enteros de skills; no multiagente si bastan scripts/índices; no Repomix sobre toda la biblioteca; no leer repos completos salvo finalistas; diferir heavy.

---

## 14. Hallazgos (desajustes, no propuestas de feature)

1. **`recommend` no lee `INDICE_IA.json`.** Lee `ai_index/REPOS.scan.json` + `REPOS.detail.json` + `WINNERS.json`. Tampoco aplica `recipes`; solo `DOMAIN_BOOSTS` y scoring.
2. **Tres funciones `_install_mode`.** Solo `recommend` asigna `docker_local` a n8n/evolution-api/chatwoot/novu/mautic/listmonk/posthog/metabase/langfuse. Catalogo y fichas humanas dicen `reference_only`.
3. **`n8n.alt` está vacío** en compact, así que no hay comparativa n8n vs activepieces generada. El solape vive en el stub `CONFLICTS.json` y en la prosa de `AGENTS.md`.
4. **Default de herramienta `auto` → `codex`.** Un brief de WhatsApp sin “Codex” en el texto mete `awesome-agent-skills` por boost de herramienta, no por dominio.
5. **Config de política no gobierna el runtime.** `scoring_rules`, `repo_policy`, `install_allowlist`, `ignore_patterns`, `project_types`, `external_tools` no se cargan.
6. **`enrich --id` no filtra.** `analyze --id` sí. `run_enrich_for_new` solo entiende `only_new`.
7. **`choose_if`/`avoid_if` auto** siguen el template de `build_draft_entries` (“quieres …”, “ya tienes una herramienta equivalente…”). `menu/export.py:_clean_field` ya los oculta en el menú portable; las fichas humanas los muestran.
8. **Conteos rotos entre documentos.** AGENTS.md ~177; compact 185; detalle 186 (`ui-shadcn`); categorías JSON `count` desfasado; `check_guias.py` 156; `human/README.md` 185 documentados / 186 curados en `Guia.md`.
9. **Cuerpo editorial vs generador.** `Guia.md`/`guias/` son otra fuente. `guide build` no las reescribe. Hay dos mundos de fichas.
10. **Packed nunca corrido en el hub** (`data/packed/` vacío) aunque `repomix` está en PATH. Analyze actual es light: README extraído, sin pack XML.
11. **Deps de “plataforma de datos” no usadas** (duckdb, pandas, networkx, sqlalchemy, jinja2, rapidfuzz, orjson, GitPython). V1 es YAML+JSON+heurística.
12. **`crawl4ai` y `llm/` son capacidad reservada**, no producto.
13. En la traza WhatsApp, `capability_coverage.whatsapp` lista `evolution-api` y `whatsapp-agentkit`; n8n entra por domain boost, no porque `_repo_capabilities` lo marque whatsapp (el tag de n8n es `automation`, no `whatsapp`).

### Traza “n8n entra a la biblioteca” (estado en disco)

1. Clone: `C:\Users\criss\Desktop\Claude\Repositorios_Prueba\n8n` (registry).
2. `discover` → id `n8n` en `registry/repos.yaml`.
3. `build_scan_index` matchea compact → scan con `install_mode: reference_only`.
4. README en `data/extracted/n8n/readme.md`. **No** hay `data/packed/n8n.xml`.
5. Draft `data/drafts/n8n.json`. Compact+detalle curados.
6. `guide build` → `human/fichas/n8n.md` (REFERENCIA / reference_only), fila en `Catalogo.md`, playbook WhatsApp, comparativa solo vs `n8n-io`.
7. `menu export` → línea en `REPO_MENU.md`; `derive_install` vería role platform + docker → `git clone && docker compose up -d` con `~`.
8. `recommend` sobreescribe el modo a `docker_local` al puntuar.

### Traza “bot de WhatsApp con Codex”

Si el brief **nombra Codex**, `BUILD_TOOL_REPOS["codex"]` empuja catálogos cross-tool. Si no lo nombra y `--tool auto`, el efecto es el mismo porque auto→codex. Domain whatsapp empuja evolution-api/n8n/chatwoot/whatsapp-agentkit. Dedupe no actúa: esos ids no se declaran `alt` entre sí. Receta 1 de AGENTS.md coincide en espíritu (evolution-api + n8n + chatwoot) y se desvía en n8n-mcp/n8n-skills/novu vs whatsapp-agentkit/awesome-agent-skills.

---

*Análisis de solo lectura. Único archivo nuevo: este mapa. Tests: 11/11. Doctor: OK. No se ejecutó `discover` / `guide build` / `enrich` / `recommend` sobre el árbol vivo.*
