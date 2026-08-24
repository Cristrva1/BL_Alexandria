# Plan A — Cerrar el análisis: unificar lógica, arreglar CLI y commitear el mapa

> **Para el Grok de la conversación NUEVA:** este archivo es tu contrato. Léelo entero. No improvises alcance. Ejecuta tarea por tarea. REQUIRED: `subagent-driven-development` (recomendado) o `executing-plans`. Pasos con `- [ ]`.

**Prompt de arranque (pegarlo como primer mensaje de la conversación nueva):**

```text
Ejecuta Plan.a.md de la raíz de BL_Alexandria, entero, tarea por tarea.

Antes de tocar código lee:
1. Plan.a.md (este contrato)
2. docs/superpowers/specs/2026-08-23-bl-alexandria-mapa-completo.md (mapa del análisis)
3. AGENTS.md (protocolo de la biblioteca; no lo trates como código)

Restricciones duras:
- No corras `enrich --auto-merge` ni `scripts/recurate_all.py`.
- No reescribas el cuerpo editorial de Guia.md ni guias/*.md.
- No borres dependencias de pyproject.toml.
- No empaquetes los 185 repos con repomix.
- No implementes LLM ni cablees crawl4ai al CLI.
- No implementes scan/guide --changed-only de verdad; solo sé honesto en el help.
- Tests con uv run pytest -v. Commits frecuentes en español, un commit por tarea.
- Tras unificar install_mode SÍ puedes correr `uv run repo-intelligence guide build` y `menu export` para regenerar human/*, Catalogo.md y menu_portable/. Eso pisa salidas generadas; no pisa el cuerpo de Guia.md.
```

**Goal:** Dejar el hub coherente con el mapa del 2026-08-23: una sola función de `install_mode`, `auto` que no finja Codex, `--id` de enrich que funcione, stubs que no mientan, conteos alineados, y el mapa commiteado.

**Architecture:** Extraer `install_mode` / `decision` a `src/repo_intelligence/core/install_mode.py`, alimentado por `config/repo_policy.yaml` (listas de ids). `recommend`, `build_scan` y `guides/render` importan esa función. El fallback `auto → codex` pasa a `auto` (sin boost de herramienta). `enrich` recibe `ids`. `decide` usa `analysis/decisions.py`. `conflicts` se deriva de pares `alt`. `score` y `report daily` escriben números reales de los índices. Al final, `guide build` + `menu export` propagan modos a salidas generadas.

**Tech Stack:** Python 3.11+ (local 3.13), Typer CLI `repo-intelligence`, pytest, uv, JSON/YAML locales. Windows / PowerShell.

## Global Constraints

- Idioma de commits y comentarios nuevos: español, concreto, sin slop.
- TDD en cada tarea de código: test que falla → código mínimo → test verde → commit.
- Un commit por tarea. Estilo del repo: mensaje en español, descriptivo (no hace falta `feat:`).
- Fuente de verdad curada: `INDICE_IA.json` + `INDICE_IA.detalle.json`. No pises `choose_if` / `avoid_if` / `desc` buenos con templates de enrich.
- `guide build` no debe reescribir el cuerpo de `Guia.md` (ya hay tests). Tras tus cambios esos tests tienen que seguir pasando.
- `uv run pytest -v` debe quedar en 11 passed más los tests nuevos de este plan, todos verdes.
- No mutar `../Repositorios_Prueba`.
- Worktree: si empiezas feature work, usa worktree / rama `fix/coherencia-post-analisis`, no commits sueltos en main sin rama. Si el usuario está en main y pide explícitamente trabajar ahí, respeta al usuario.

---

## Qué ya está hecho (no lo repitas)

El análisis exhaustivo ya existió. Entregable:

- `docs/superpowers/specs/2026-08-23-bl-alexandria-mapa-completo.md` (untracked al escribir este plan: `?? docs/`)

Hallazgos que **este plan sí cierra** (mapa §14, ítems 1–8, 12 parcial):

| # | Hallazgo | Acción en este plan |
|---|---|---|
| 1 | `recommend` no lee `INDICE_IA.json` | **No cambiar eso.** Es diseño. Documentado. Scan se genera desde compact. |
| 2 | Tres `_install_mode` distintos | Unificar. Tarea 3. |
| 3 | `n8n.alt` vacío | Poner alternativas reales. Tarea 6. |
| 4 | `auto` cae a `codex` | `auto` queda `auto` (sin boost). Tarea 4. |
| 5 | Config huérfana | Cablear `repo_policy.yaml` para modos de **repos**. Tarea 3. El resto de YAML se documenta, no se inventa runtime. |
| 6 | `enrich --id` se ignora | Pasarlo a `run_enrich_for_new`. Tarea 5. |
| 7 | `choose_if` basura auto | **Fuera de alcance** (es `PLAN_ENRIQUECER_GUIAS.md`). |
| 8 | Conteos 177/156/185/186 | Alinear docs y `categories[].count`. Tarea 6–7. Extra `ui-shadcn`: Tarea 6. |
| 9 | Cuerpo editorial vs generador | No unificar a la fuerza. `guide build` regenera `human/*` sí. |
| 10 | `data/packed/` vacío | Fuera de alcance (no correras 185 repomix). |
| 11 | Deps no usadas | Fuera de alcance (no las borres). |
| 12 | Stubs `score`/`conflicts`/`decide`/`report daily` | Hacerlos honestos y útiles. Tarea 8. |
| 13 | Coverage whatsapp no marca n8n | No hace falta si n8n entra por domain boost. No tocar scoring de tags masivo. |

---

## Mapa de archivos (descomposición)

| Ruta | Responsabilidad |
|---|---|
| Create: `src/repo_intelligence/core/install_mode.py` | Única función `install_mode(repo) -> str` y `decision(repo) -> str`. Carga listas de `config/repo_policy.yaml`. |
| Create: `tests/test_install_mode.py` | Contratos: n8n→docker_local, skill→reference_only, heavy→deferred, yaml override. |
| Modify: `config/repo_policy.yaml` | Añadir `repo_install_modes` con las listas que hoy están hardcodeadas en `recommend._install_mode`. |
| Modify: `src/repo_intelligence/analysis/recommend.py` | Importar `install_mode`; `_detect_effective_tool("auto")` → `"auto"`. |
| Modify: `src/repo_intelligence/indexes/build_scan.py` | Dejar de definir `_install_mode` / `_decision` locales. |
| Modify: `src/repo_intelligence/guides/render.py` | Igual. |
| Modify: `src/repo_intelligence/analysis/curation.py` | `run_enrich_for_new(..., ids=None)`. |
| Modify: `src/repo_intelligence/cli.py` | Pasar `ids` a enrich; help honesto de `--changed-only`; stubs reales. |
| Modify: `src/repo_intelligence/analysis/decisions.py` | Ampliar `INITIAL_DECISIONS` si hace falta para `decide`. |
| Modify: `tests/test_recommend.py` | Fallback auto; WhatsApp sin herramienta no mete catálogo Codex. |
| Modify: `INDICE_IA.json` | `n8n.alt`, `categories[].count`, `meta.title` conteos, `agent_tools` en skills de `model_guidance`. |
| Modify: `AGENTS.md` | Conteos 185/186 en vez de ~177. |
| Modify: `README.md` | Una línea: `auto` sin mención de herramienta no asume Codex. |
| Regenerar: `human/*`, `Catalogo.md`, `ai_index/REPOS.detail.json`, `menu_portable/` | `guide build` + `menu export` **después** de unificar modos. |
| Commit inicial: `docs/superpowers/specs/2026-08-23-bl-alexandria-mapa-completo.md`, `Plan.a.md` | Documentación del análisis + este plan. |

---

### Task 1: Commitear mapa y este plan

**Files:**
- Add: `docs/superpowers/specs/2026-08-23-bl-alexandria-mapa-completo.md`
- Add: `Plan.a.md`

**Interfaces:**
- Consumes: nada de código
- Produces: commit de documentación en la rama de trabajo

- [ ] **Step 1: Crear rama** (si no existe)

```powershell
git checkout -b fix/coherencia-post-analisis
```

Expected: estás en `fix/coherencia-post-analisis`. Si el usuario insistió en `main`, trabaja en main y anótalo.

- [ ] **Step 2: Verificar que el mapa existe y no está vacío**

```powershell
Get-Item docs\superpowers\specs\2026-08-23-bl-alexandria-mapa-completo.md, Plan.a.md | Select-Object Name, Length
```

Expected: ambos files, tamaño > 1 KB.

- [ ] **Step 3: Commit solo docs**

```powershell
git add docs/superpowers/specs/2026-08-23-bl-alexandria-mapa-completo.md Plan.a.md
git commit -m "Documenta el mapa completo de BL_Alexandria y el plan de coherencia"
```

No añadas `human/`, JSON ni código en este commit.

---

### Task 2: Tests de `install_mode` (red) — TDD

**Files:**
- Create: `tests/test_install_mode.py`
- Test: `tests/test_install_mode.py`

**Interfaces:**
- Consumes: nada aún (el import fallará)
- Produces: contrato que Task 3 debe cumplir:

```python
from repo_intelligence.core.install_mode import install_mode, decision

def install_mode(repo: dict) -> str: ...
def decision(repo: dict) -> str: ...
# valores: global | local_project | docker_local | reference_only | deferred
# decision: use_now | defer | reference
# use_now <=> install_mode in {global, local_project, docker_local}
```

- [ ] **Step 1: Escribir tests que fallan**

Crear `tests/test_install_mode.py`:

```python
from pathlib import Path

from repo_intelligence.core.install_mode import decision, install_mode


def test_n8n_is_docker_local() -> None:
    assert install_mode({"id": "n8n", "role": "platform", "setup": "medium"}) == "docker_local"
    assert decision({"id": "n8n", "role": "platform", "setup": "medium"}) == "use_now"


def test_evolution_api_is_docker_local() -> None:
    assert install_mode({"id": "evolution-api", "role": "app", "setup": "medium"}) == "docker_local"


def test_skill_is_reference_only() -> None:
    assert install_mode({"id": "n8n-skills", "role": "skill", "setup": "easy"}) == "reference_only"
    assert decision({"id": "n8n-skills", "role": "skill"}) == "reference"


def test_repomix_is_global() -> None:
    assert install_mode({"id": "repomix", "role": "app", "setup": "easy"}) == "global"
    assert decision({"id": "repomix"}) == "use_now"


def test_markitdown_is_local_project() -> None:
    assert install_mode({"id": "markitdown", "role": "library", "setup": "easy"}) == "local_project"


def test_litellm_is_local_project() -> None:
    assert install_mode({"id": "litellm", "role": "runtime", "setup": "medium"}) == "local_project"


def test_heavy_is_deferred() -> None:
    assert install_mode({"id": "comfyui", "role": "platform", "setup": "heavy"}) == "deferred"
    assert decision({"id": "comfyui", "role": "platform", "setup": "heavy"}) == "defer"


def test_unknown_library_is_reference_only() -> None:
    assert install_mode({"id": "loguru", "role": "library", "setup": "easy"}) == "reference_only"


def test_id_list_wins_over_heavy() -> None:
    # n8n is medium in the index; if someone marks setup heavy, docker_local still wins
    assert install_mode({"id": "n8n", "role": "platform", "setup": "heavy"}) == "docker_local"
```

- [ ] **Step 2: Correr para ver el rojo**

```powershell
uv run pytest tests/test_install_mode.py -v
```

Expected: FAIL — `ModuleNotFoundError` o `ImportError` de `repo_intelligence.core.install_mode`.

- [ ] **Step 3: No implementes aún.** Commit de tests si quieres separar, o pasa directo a Task 3 en el mismo commit si el repo no suele commitear tests rojos solos. Preferido: un commit “test rojo + implementación” de Task 3. No dejes `main`/rama con tests rotos.

---

### Task 3: Una sola `install_mode` cableada a `repo_policy.yaml`

**Files:**
- Create: `src/repo_intelligence/core/install_mode.py`
- Modify: `config/repo_policy.yaml` (añadir bloque `repo_install_modes` al final; no borres `rules` ni `install_modes` existentes de tools)
- Modify: `src/repo_intelligence/analysis/recommend.py` — borrar `def _install_mode` local; usar `from repo_intelligence.core.install_mode import install_mode as _install_mode` (así el resto del archivo no cambia de nombre)
- Modify: `src/repo_intelligence/indexes/build_scan.py` — igual
- Modify: `src/repo_intelligence/guides/render.py` — igual para `_install_mode` y `_decision`
- Test: `tests/test_install_mode.py`

**Interfaces:**
- Consumes: contrato de Task 2
- Produces: `install_mode(repo: dict) -> str`, `decision(repo: dict) -> str`

Listas canónicas (copiar **verbatim** a YAML; son las de `recommend.py` líneas 708–715, que son el comportamiento de producto de las superguías):

```yaml
repo_install_modes:
  global:
    - repomix
    - gitnexus
  local_project:
    - markitdown
    - crawl4ai
    - litellm
  docker_local:
    - n8n
    - langfuse
    - evolution-api
    - chatwoot
    - novu
    - mautic
    - listmonk
    - posthog
    - metabase
```

- [ ] **Step 1: Implementar `core/install_mode.py`**

```python
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

_DEFAULTS = {
    "global": ["repomix", "gitnexus"],
    "local_project": ["markitdown", "crawl4ai", "litellm"],
    "docker_local": [
        "n8n",
        "langfuse",
        "evolution-api",
        "chatwoot",
        "novu",
        "mautic",
        "listmonk",
        "posthog",
        "metabase",
    ],
}


def _project_root() -> Path:
    # core/install_mode.py -> core -> repo_intelligence -> src -> project root
    return Path(__file__).resolve().parents[3]


@lru_cache(maxsize=1)
def _mode_sets() -> dict[str, set[str]]:
    path = _project_root() / "config" / "repo_policy.yaml"
    raw: dict[str, Any] = {}
    if path.exists():
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    block = raw.get("repo_install_modes") or _DEFAULTS
    return {
        "global": set(block.get("global") or _DEFAULTS["global"]),
        "local_project": set(block.get("local_project") or _DEFAULTS["local_project"]),
        "docker_local": set(block.get("docker_local") or _DEFAULTS["docker_local"]),
    }


def install_mode(repo: dict[str, Any] | None) -> str:
    repo = repo or {}
    repo_id = repo.get("id") or ""
    role = repo.get("role")
    modes = _mode_sets()
    if repo_id in modes["global"]:
        return "global"
    if repo_id in modes["local_project"]:
        return "local_project"
    if repo_id in modes["docker_local"]:
        return "docker_local"
    if role in {"skill", "directory"}:
        return "reference_only"
    if repo.get("setup") == "heavy":
        return "deferred"
    return repo.get("install_mode") or "reference_only"


def decision(repo: dict[str, Any] | None) -> str:
    mode = install_mode(repo)
    if mode in {"global", "local_project", "docker_local"}:
        return "use_now"
    if mode == "deferred":
        return "defer"
    return "reference"
```

Notas:
- `parents[3]` asume `src/repo_intelligence/core/install_mode.py`. Verifícalo con `Path(__file__).resolve().parts`.
- `REPO_GUIDANCE` de recommend fuerza `reference_only` en 9 skills. Esas ids ya son `role=skill|directory`, así que el resultado coincide. **No** dupliques REPO_GUIDANCE aquí.
- Cache `lru_cache`: en tests que toquen el YAML, llama `_mode_sets.cache_clear()` si añades un test de override. El test suite de Task 2 no lo necesita.

- [ ] **Step 2: Añadir el bloque YAML** al final de `config/repo_policy.yaml` (el bloque `repo_install_modes` de arriba). Deja `install_modes:` viejo (tools) intacto.

- [ ] **Step 3: Sustituir las tres copias**

En `recommend.py`, `build_scan.py`, `render.py`:
1. Importar.
2. Borrar las funciones locales `_install_mode` y, en scan/render, `_decision`.
3. Alias para no reescribir 20 llamadas:

```python
from repo_intelligence.core.install_mode import decision as _decision
from repo_intelligence.core.install_mode import install_mode as _install_mode
```

`build_scan._install_mode` recibía `meta: dict` — sigue siendo dict. OK.

Ojo: `recommend.py` tiene `from repo.get("install_mode")` en el fallback viejo; la función nueva ya lo hace.

- [ ] **Step 4: Tests**

```powershell
uv run pytest tests/test_install_mode.py tests/test_recommend.py tests/test_render_guide.py tests/test_discover.py -v
```

Expected: ALL PASS. El test de Claude Code diario no depende de install_mode de n8n.

- [ ] **Step 5: Commit**

```powershell
git add src/repo_intelligence/core/install_mode.py src/repo_intelligence/analysis/recommend.py src/repo_intelligence/indexes/build_scan.py src/repo_intelligence/guides/render.py config/repo_policy.yaml tests/test_install_mode.py
git commit -m "Unifica install_mode en un solo modulo alimentado por repo_policy.yaml"
```

---

### Task 4: `auto` no asume Codex

**Files:**
- Modify: `src/repo_intelligence/analysis/recommend.py` función `_detect_effective_tool` (hoy líneas 738–757)
- Modify: `tests/test_recommend.py`
- Modify: `README.md` (una frase en la sección de `--tool`)

**Interfaces:**
- Consumes: `_detect_effective_tool(project: str, requested_tool: str) -> str`
- Produces: si el brief no nombra herramienta y `requested_tool=="auto"`, retorno `"auto"`. `BUILD_TOOL_REPOS.get("auto", {})` es vacío → sin boost de catálogo Codex.

Comportamiento actual a reemplazar:

```python
    if tool == "auto":
        return "codex"
```

Por:

```python
    if tool == "auto":
        return "auto"
```

El resto de aliases (`claude` → `claude-code`, texto “claude code” en el brief, etc.) **no se toca**. El test `test_recommend_infers_claude_code_and_filters_generic_code` sigue pasando porque el brief dice “Claude Code”.

- [ ] **Step 1: Test nuevo que falla con el código viejo**

Añadir en `tests/test_recommend.py`:

```python
def test_auto_without_tool_phrase_does_not_assume_codex(tmp_path: Path) -> None:
    ai_index = tmp_path / "ai_index"
    ai_index.mkdir()
    write_json(
        ai_index / "REPOS.scan.json",
        {
            "repos": [
                _repo("evolution-api", role="app", tags=["whatsapp", "automation"]),
                _repo("n8n", role="platform", tags=["automation"]),
                _repo("awesome-agent-skills", role="directory", tags=["skills"]),
            ]
        },
    )
    write_json(
        ai_index / "REPOS.detail.json",
        {
            "repos": [
                {"id": "evolution-api", "desc": "api de whatsapp"},
                {"id": "n8n", "desc": "automatizacion de flujos"},
                {"id": "awesome-agent-skills", "desc": "catalogo de skills"},
            ]
        },
    )
    write_json(ai_index / "WINNERS.json", {})

    result = recommend(
        tmp_path,
        "bot de WhatsApp con IA para responder clientes y guardar leads",
        max_repos=5,
        build_tool="auto",
    )
    ids = [repo["id"] for repo in result["recommended_repos"]]
    assert result["requested_tool"] == "auto"
    assert result["build_tool"] == "auto"
    assert "awesome-agent-skills" not in ids
    assert "evolution-api" in ids
```

Ajusta `_repo` si hace falta para que evolution-api tenga id correcto (el helper ya pone `id`). Domain boost de whatsapp está en `DOMAIN_BOOSTS` y usa el texto “whatsapp”.

- [ ] **Step 2: Correr el test, debe FALLAR** con `build_tool == "codex"` o `awesome-agent-skills` en ids.

```powershell
uv run pytest tests/test_recommend.py::test_auto_without_tool_phrase_does_not_assume_codex -v
```

- [ ] **Step 3: Cambiar el `return "codex"` de `_detect_effective_tool` a `return "auto"`.**

- [ ] **Step 4: Suite recommend completa**

```powershell
uv run pytest tests/test_recommend.py -v
```

Expected: PASS incluyendo el test viejo de Claude Code.

- [ ] **Step 5: README** — en la lista de valores de `--tool`, aclara: si pones `auto` y el brief no nombra herramienta, no se asume Codex; no hay boost de catálogo de skills.

- [ ] **Step 6: Commit**

```powershell
git add src/repo_intelligence/analysis/recommend.py tests/test_recommend.py README.md
git commit -m "Deja de asumir Codex cuando --tool es auto y el brief no nombra herramienta"
```

---

### Task 5: `enrich --id` de verdad

**Files:**
- Modify: `src/repo_intelligence/analysis/curation.py` — `run_enrich_for_new`
- Modify: `src/repo_intelligence/cli.py` — `enrich()`
- Create: `tests/test_enrich_ids.py`

**Interfaces:**
- Consumes: `run_enrich_for_new(project_root, only_new=True, auto_merge=False, force_analyze=False)`
- Produces:

```python
def run_enrich_for_new(
    project_root: Path,
    only_new: bool = True,
    auto_merge: bool = False,
    force_analyze: bool = False,
    ids: list[str] | None = None,
) -> dict[str, Any]:
```

Si `ids` no es None/vacío, `targets` = esos ids que existan en el registry (aunque `only_new` sea True). Mismo patrón que `analyze`.

- [ ] **Step 1: Test**

`tests/test_enrich_ids.py` no debe lanzar analyze pesado. Extrae la resolución de targets a una función pura si hace falta, para testearla sin clones:

En `curation.py` añade:

```python
def resolve_enrich_targets(
    registry_ids: list[str],
    curated_ids: set[str],
    only_new: bool,
    ids: list[str] | None,
) -> list[str]:
    if ids:
        wanted = [i for i in ids if i in registry_ids]
        return wanted
    if only_new:
        return [i for i in registry_ids if i not in curated_ids]
    return list(registry_ids)
```

`run_enrich_for_new` y `get_new_repo_ids` usan eso. Test:

```python
from repo_intelligence.analysis.curation import resolve_enrich_targets

def test_ids_override_only_new() -> None:
    registry = ["n8n", "chatwoot", "nuevo"]
    curated = {"n8n", "chatwoot"}
    assert resolve_enrich_targets(registry, curated, only_new=True, ids=["n8n"]) == ["n8n"]

def test_only_new_without_ids() -> None:
    registry = ["n8n", "nuevo"]
    curated = {"n8n"}
    assert resolve_enrich_targets(registry, curated, only_new=True, ids=None) == ["nuevo"]
```

- [ ] **Step 2: pytest rojo, implementar, pytest verde.**

- [ ] **Step 3: CLI**

```python
    res = curation_mod.run_enrich_for_new(
        paths.project_root,
        only_new=new,
        auto_merge=auto_merge,
        force_analyze=force,
        ids=ids,
    )
```

- [ ] **Step 4: Commit**

```powershell
git add src/repo_intelligence/analysis/curation.py src/repo_intelligence/cli.py tests/test_enrich_ids.py
git commit -m "Hace que enrich --id filtre de verdad"
```

---

### Task 6: Datos compactos — alts, `ui-shadcn`, `agent_tools`, counts de categoría

**Files:**
- Modify: `INDICE_IA.json` (cirugía JSON, no reformat masivo innecesario)
- No `enrich --auto-merge`

**Reglas:**
- `n8n.alt`: `["activepieces", "huginn"]` (existen en compact; coincide con CONFLICTS y AGENTS.md).
- `activepieces.alt`: incluye `n8n` si no está (simétrico).
- Extra `ui-shadcn` en detalle y no en compact: inspecciona `INDICE_IA.json` id `ui` y detalle `ui-shadcn`. Si `ui` es el shadcn: o bien (a) copias el detalle de `ui-shadcn` a `ui` y borras `ui-shadcn` del dict detalle, o (b) añades compact `ui-shadcn` con los campos de `ui` y dejas el alias. Elige **una** y documenta en el commit. No dejes 186 vs 185.
- Recalcula `categories[].count` con un script de una vez:

```powershell
uv run python -c "
import json
from collections import Counter
from pathlib import Path
p = Path('INDICE_IA.json')
c = json.loads(p.read_text(encoding='utf-8'))
counts = Counter(r.get('cat') for r in c['repos'])
for cat in c['categories']:
    cat['count'] = counts.get(cat['num'], 0)
    print(cat['num'], cat['title'], cat['count'])
print('cat0', counts.get(0))
p.write_text(json.dumps(c, ensure_ascii=False, indent=2) + chr(10), encoding='utf-8')
"
```

Expected: las 13 categorías suman los compactos con cat 1–13. El `tools` cat 0 no entra en esas 13.

- `meta.title` / `meta` de compact: actualiza “156/171/177” a **185 curados** (y el extra de detalle si aún existe).
- `agent_tools`: para cada id de `model_guidance.tools.*.best_fit_repos`, pon `"agent_tools": ["claude-code"]` etc. Un repo puede estar en varios tools (lista). No inventes tools para el resto.

- [ ] **Step 1: Hacer los edits JSON.** Verificar con python que `len(repos)==185`, detalle ids ⊇ compact ids, y `detalle - compact` es `[]` o el alias que elegiste, documentado.

- [ ] **Step 2: Commit**

```powershell
git add INDICE_IA.json INDICE_IA.detalle.json
git commit -m "Alinea alts, conteos de categoria y agent_tools del indice compacto"
```

Si no tocaste detalle, no lo añadas.

---

### Task 7: AGENTS.md y README — conteos

**Files:**
- Modify: `AGENTS.md` (línea de “~177 repositorios curados (171+ detectados)” → **185 curados** compactos; si detalle difiere, dilo)
- Modify: `README.md` solo si aún habla de 156/177

No reescribas el protocolo de lectura. Solo cifras y, si aplica, la nota de `--tool auto` (si no la pusiste en Task 4).

- [ ] **Step 1: Grep**

```powershell
uv run python -c "from pathlib import Path
for p in Path('.').glob('*.md'):
    t=p.read_text(encoding='utf-8')
    if any(x in t for x in ['156','171','177','~177']):
        print(p)
"
```

Corrige AGENTS.md / README.md. **No** masajees `PLAN_ENRIQUECER_GUIAS.md` ni `PLAN_EXTRACCION_READMES.md` (son históricos). **No** cambies `tools_check/check_guias.py` `EXPECTED_TOTAL = 156`: vigila fichas editoriales `**Repo:**` de `guias/`, no el JSON.

- [ ] **Step 2: Commit**

```powershell
git add AGENTS.md README.md
git commit -m "Actualiza conteos de la biblioteca en AGENTS.md y README"
```

---

### Task 8: Stubs honestos (`decide`, `conflicts`, `score`, `report daily`)

**Files:**
- Modify: `src/repo_intelligence/cli.py`
- Modify: `src/repo_intelligence/analysis/decisions.py` si hace falta exportar un writer
- Create: `tests/test_cli_reports.py` (usar `tmp_path` + monkeypatch de CWD o pasar paths; si el CLI siempre usa `ProjectPaths.load()` de cwd, testea las funciones extraídas, no Typer)

No construyas un motor de scoring nuevo. Haz que los comandos **lean datos reales** y no hardcodeen un timestamp vacío.

#### `decide`

Usar `INITIAL_DECISIONS` de `analysis/decisions.py`. Si `--project-type` no está en el dict, error Typer claro. Escribir el mismo markdown pero desde el dict (winner, support_tools, avoid_now, reason).

#### `conflicts`

Generar lista desde compact: para cada repo con `alt`, un conflicto `functional_overlap` con `repo_a=id`, `repo_b=alt[0]`, `recommendation=elegir uno`. Dedup de pares no dirigidos. Si no hay alts, el archivo queda `"conflicts": []`, no el n8n hardcodeado (n8n ya tendrá alt tras Task 6).

#### `score`

Leer `REPOS.scan.json` y `config/scoring_rules.yaml`. Escribir JSON:

```python
{
  "generated_at": ...,
  "status": "v1_scan_summary",
  "rule_file": "config/scoring_rules.yaml",
  "counts": {"repos": N, "by_install_mode": {...}, "by_decision": {...}, "by_role": {...}},
  "weights_declared": <weights del yaml>,
  "note": "Estas weights no alimentan recommend(); recommend usa constantes en analysis/recommend.py."
}
```

#### `report daily`

Markdown con fecha, N compactos, N scan, N detalle, N drafts, packed vacío o no, y “comandos stub ya no están vacíos”.

#### `--changed-only`

En `scan` y `guide build`, el mensaje ya dice que V1 regenera todo. Deja el flag. Añade en el help de Typer: `"Accepted for compatibility; V1 always rebuilds."`

- [ ] **Step 1: Extrae writers testeables** (p. ej. `build_conflicts(repos) -> dict`) en `analysis/decisions.py` o `analysis/reports.py` nuevo si cli.py se hincha. Preferí `analysis/reports.py` si `decisions.py` se queda corto.

- [ ] **Step 2: Tests** de `build_conflicts` con dos repos que se apuntan por `alt` → un solo par. Test de `decide` dict desconocido.

- [ ] **Step 3: Cablear CLI. pytest -v verde.**

- [ ] **Step 4: Commit**

```powershell
git add src/repo_intelligence/cli.py src/repo_intelligence/analysis/decisions.py src/repo_intelligence/analysis/reports.py tests/test_cli_reports.py
git commit -m "Hace que score, conflicts, decide y report daily usen datos reales"
```

(Omite `reports.py` del add si no lo creaste.)

---

### Task 9: Regenerar salidas generadas

**Files (todos pisados por comandos, no a mano):**
- `Catalogo.md`, `human/**`, `ai_index/REPOS.detail.json`, `ai_index/REPOS.scan.json` (si corres discover/scan; **no hace falta discover** si no cambió la biblioteca)
- `menu_portable/**`

**No pises a mano** `Guia.md` cuerpo. `guide build` solo toca status/apéndice.

- [ ] **Step 1: Tests antes**

```powershell
uv run pytest -v
```

Expected: ALL PASS.

- [ ] **Step 2: guide build**

```powershell
uv run repo-intelligence guide build
```

Expected: imprime counts. `human/fichas/n8n.md` ahora debe decir `docker_local` / USAR AHORA (porque `_human_decision` usa `decision()` unificado y docker_local → `use_now`).

Verifica:

```powershell
uv run python -c "
from pathlib import Path
t = Path('human/fichas/n8n.md').read_text(encoding='utf-8')
assert 'docker_local' in t or 'USAR AHORA' in t, t[:400]
print('n8n ficha ok')
"
```

Si `USAR AHORA` no aparece, debug `_human_decision` / `_install_mode` en render (deben ser los imports nuevos).

- [ ] **Step 3: menu export**

```powershell
uv run repo-intelligence menu export
```

- [ ] **Step 4: pytest otra vez** (render tests usan tmp_path; no deberían romper). 

- [ ] **Step 5: Commit de artefactos generados**

```powershell
git add Catalogo.md human ai_index/REPOS.detail.json menu_portable
git commit -m "Regenera catalogos humanos y menu portable con install_mode unificado"
```

Si `guide build` tocó solo el bloque STATUS de `Guia.md`, inclúyelo. Si tocó cuerpo editorial, **STOP** y revierte ese archivo (`git checkout -- Guia.md`) salvo el bloque STATUS.

---

### Task 10: Verificación final y mapa actualizado

**Files:**
- Modify: `docs/superpowers/specs/2026-08-23-bl-alexandria-mapa-completo.md` — añade al final una sección `## 15. Estado tras Plan A` con fecha, tests, y qué quedó fuera.

- [ ] **Step 1: Suite + doctor**

```powershell
uv run pytest -v
uv run repo-intelligence doctor
```

Expected: tests 100% pass. Doctor sigue OK.

- [ ] **Step 2: Comprobar que no hay tres `_install_mode`**

```powershell
uv run python -c "
from pathlib import Path
hits=[]
for p in Path('src').rglob('*.py'):
    t=p.read_text(encoding='utf-8')
    if 'def _install_mode' in t or 'def install_mode' in t:
        hits.append(str(p))
print('\n'.join(hits))
"
```

Expected: solo `src/repo_intelligence/core/install_mode.py` define la función. Los otros importan.

- [ ] **Step 3: Sección 15 del mapa** (10–20 líneas, hechos, no marketing).

- [ ] **Step 4: Commit**

```powershell
git add docs/superpowers/specs/2026-08-23-bl-alexandria-mapa-completo.md
git commit -m "Registra en el mapa el estado tras unificar install_mode y el CLI"
```

- [ ] **Step 5: No abras PR a menos que el usuario lo pida.** Resume en el chat: rama, commits, qué cambió n8n/WhatsApp/`auto`, qué quedó fuera.

---

## Fuera de alcance (si lo haces, estás fuera de contrato)

- `enrich --auto-merge` / `scripts/recurate_all.py`
- Reescribir `guias/*.md` o el cuerpo de `Guia.md`
- Borrar duckdb/pandas/networkx/orjson/GitPython/etc. de `pyproject.toml`
- `repomix` sobre la biblioteca
- Implementar `src/repo_intelligence/llm/`
- Cablear `crawl4ai_docs` a un comando CLI
- Scan incremental real (`--changed-only`)
- Cambiar `recommend` para que lea `INDICE_IA.json` en vez del scan
- Aplicar `recipes[]` dentro de `recommend()` (es otro producto)
- Arreglar todos los `choose_if: "quieres …"` (otro plan)

---

## Orden de lectura mínimo para el agente nuevo

1. `Plan.a.md` (contrato)
2. `docs/superpowers/specs/2026-08-23-bl-alexandria-mapa-completo.md` §§3, 7, 10, 12, 14
3. `src/repo_intelligence/cli.py` (superficie)
4. `src/repo_intelligence/analysis/recommend.py` `_install_mode` y `_detect_effective_tool`
5. `tests/test_recommend.py` (anclas que no puedes romper)

Luego Task 1.

---

## Criterio de hecho

El plan está hecho cuando:

1. `uv run pytest -v` pasa (viejos + nuevos).
2. `install_mode({"id":"n8n","role":"platform","setup":"medium"}) == "docker_local"` desde core, scan y render.
3. Brief WhatsApp sin herramienta → `build_tool == "auto"` y no aparece `awesome-agent-skills` por default Codex.
4. `enrich --id n8n` no re-enriquece toda la biblioteca (targets = `[n8n]`). No hace falta ejecutarlo contra clones si el test de `resolve_enrich_targets` lo cubre; **no** uses `--auto-merge`.
5. Compact y detalle tienen el mismo conjunto de ids (salvo decisión documentada).
6. `AGENTS.md` no dice 177.
7. Stubs escriben datos derivados, no placeholders.
8. Hay commits en la rama, incluido el mapa.
)
