# Plan: Extracción completa de READMEs antes de borrar Repositorios_Prueba

**Objetivo:** Garantizar que toda la información útil de los 182 repos clonados en `../Repositorios_Prueba` quede persistente en `BL_Alexandria` antes de eliminar la carpeta de clones.

**Alcance:** Completo (READMEs + repos missing + re-curación + backup), sin repomix.

---

## Contexto y hallazgos previos

| Métrica | Valor |
|---|---|
| Repos clonados | 182 |
| Repos en INDICE_IA.json | 177 |
| Repos en REPOS.detail.json | 177 |
| Carpetas en data/extracted/ | 21 (solo 18 con readme.md) |
| Archivos en data/packed/ | 0 (repomix nunca corrido) |
| Drafts en data/drafts/ | 21 |

### Gaps detectados

1. **11 repos clonados NO están en el índice**: `FFmpeg`, `OpenMontage`, `browser-harness`, `codebase-memory-mcp`, `daily_stock_analysis`, `last30days-skill`, `ponytail`, `skills_remotion`, `stitch-sdk`, `stitch-skills`, `video-use`
2. **133 READMEs > 8000 chars** fueron truncados por `read_readme_text(max_chars=8000)` durante la curación. El más grande: `awesome-mcp-servers` con 1M chars.
3. **3 READMEs en formato .rst** (`instaloader`, `scrapely`, `scrapy`) no son detectados por `find_readme` (solo busca `.md`, `.txt`).
4. **7 repos con `one` vacío**: `tools`, `appsmith`, `budibase`, `llm.c`, `design.md`, `three.js`, `ui`
5. **5 repos sin `combines_with`** en REPOS.detail.json
6. **1 repo sin README**: `tools`

---

## Fases del plan

### Fase 1: Fix find_readme para detectar .rst

**Archivo:** `src/repo_intelligence/extract/readme.py`

**Cambio:** Ampliar `README_NAMES` para incluir `README.rst`, `readme.rst`, `README.markdown`, `README.html`.

**Validación:**
```powershell
cd BL_Alexandria
uv run python -c "from repo_intelligence.extract.readme import find_readme; from pathlib import Path; print(find_readme(Path('../Repositorios_Prueba/instaloader')))"
```
Debe devolver la ruta al `README.rst`.

---

### Fase 2: Extraer README completo de los 182 repos a data/extracted/

**Problema actual:** `read_readme_text` lee solo 8000 chars. `ensure_analyzed` corre markitdown solo si está instalado y guarda el resultado en `data/extracted/{id}/readme.md`, pero solo se hizo para 21 repos.

**Solución:** Crear un script `scripts/extract_all_readmes.py` que:

1. Itere sobre los 182 repos en `../Repositorios_Prueba`
2. Para cada repo:
   - Encuentre el README con `find_readme` (ya fixeado para .rst)
   - Si es `.md`: copie el contenido completo a `data/extracted/{id}/readme.md`
   - Si es `.rst` u otro formato: intente markitdown si está disponible, sino copie el raw
   - Si no hay README: registre en `data/extracted/{id}/NO_README.txt`
3. Genere un manifiesto `data/extracted/MANIFEST.json` con:
   - `id`, `source_path`, `source_format`, `chars`, `extracted_chars`, `truncated` (bool)

**Criterio de completitud:** Los 182 repos deben tener una carpeta en `data/extracted/` con el README completo (o el flag NO_README).

**Validación:**
```powershell
uv run python scripts/extract_all_readmes.py
# Verificar:
uv run python -c "import json; m=json.load(open('data/extracted/MANIFEST.json')); print(f'Total: {len(m)}, con README: {sum(1 for r in m if not r[\"no_readme\"])}')"
```

---

### Fase 3: Descubrir y procesar los 11 repos missing

Los 11 repos que están clonados pero no en el índice necesitan pasar por el pipeline completo.

**Pasos:**
1. `uv run repo-intelligence discover` — para que el scan los detecte
2. `uv run repo-intelligence analyze --new` — extrae README + manifests
3. `uv run repo-intelligence enrich --new --auto-merge` — genera drafts y los mergea a los índices

**Validación:**
```powershell
uv run python -c "import json; d=json.load(open('INDICE_IA.json',encoding='utf-8')); ids={r['id'] for r in d['repos']}; missing=['ffmpeg','openmontage','browser-harness','codebase-memory-mcp','daily_stock_analysis','last30days-skill','ponytail','skills_remotion','stitch-sdk','stitch-skills','video-use']; print('Faltan:', [m for m in missing if m not in ids])"
```
La lista debe estar vacía o contener solo los que genuinamente no tienen README útil.

---

### Fase 4: Re-curar con texto completo de READMEs

**Problema:** La curación original usó `read_readme_text(max_chars=8000)`. Para 133 repos, la inferencia de cat, role, stack, features, desc, choose_if, avoid_if se hizo con texto truncado.

**Solución:** Modificar `build_profile` en `curation.py` para que, si existe `data/extracted/{id}/readme.md`, lea el texto completo de ahí en lugar del raw truncado.

**Cambios:**
1. En `build_profile`, antes de `read_readme_text(readme_path)`:
   - Verificar si `paths.extracted_dir / rid / "readme.md"` existe
   - Si existe, leerlo completo (sin límite de 8000 chars)
   - Si no, fallback a `read_readme_text(readme_path)` con el límite actual
2. Aumentar `max_chars` de `read_readme_text` de 8000 a 50000 como segundo nivel de fallback

**Re-curación:**
```powershell
# Forzar re-enriquecimiento de todos los repos con el texto completo
uv run repo-intelligence enrich --all --auto-merge
```

> Nota: si `enrich` no tiene flag `--all`, se necesita agregar o usar `analyze --force` + `enrich --new --auto-merge` para todos.

**Validación:**
- Comparar `INDICE_IA.json` antes/después: los campos `one`, `tags`, `cat` de los 133 repos truncados pueden cambiar
- Verificar que los 7 repos con `one` vacío ahora tengan contenido
- Verificar que los 5 repos sin `combines_with` ahora tengan

---

### Fase 5: Backup permanente de READMEs

Crear un archivo único que sirva como referencia permanente después de borrar los clones.

**Salida:** `data/readmes_backup.tar.gz` (o `.zip` en Windows) con:
- Todos los READMEs extraídos en `data/extracted/`
- El `MANIFEST.json`
- El `registry/repos.yaml` actualizado

**Script:** `scripts/backup_readmes.py` o comando directo:
```powershell
Compress-Archive -Path data/extracted/*, registry/repos.yaml -DestinationPath data/readmes_backup.zip -Force
```

**Validación:**
```powershell
# Verificar que el backup contiene los 182 repos
uv run python -c "import zipfile; z=zipfile.ZipFile('data/readmes_backup.zip'); dirs={n.split('/')[0] for n in z.namelist()}; print(f'Carpetas en backup: {len(dirs)}')"
```

---

### Fase 6: Regenerar guías y verificar completitud

```powershell
uv run repo-intelligence guide build
```

Esto regenera: `Catalogo.md`, `Guia.md`, `human/*`, `INDICE_IA.json`, `INDICE_IA.detalle.json`, `ai_index/REPOS.*`.

**Verificación de completitud:**

```powershell
uv run python scripts/verify_extraction.py
```

Script que verifica:
1. `INDICE_IA.json` tiene >= 177 repos (idealmente 188 = 177 + 11)
2. Ningún repo tiene `one` vacío (excepto `tools` que no tiene README)
3. Ningún repo tiene `cat=0` (excepto `tools`)
4. `REPOS.detail.json` tiene `choose_if`, `avoid_if`, `stack`, `desc` en todos los repos
5. `data/extracted/MANIFEST.json` cubre los 182 repos
6. `data/readmes_backup.zip` existe y tiene tamaño razonable

---

### Fase 7: Validación final pre-borrado

**Checklist manual de aprobación:**

- [ ] `INDICE_IA.json` tiene los 11 repos que faltaban (o los que no tienen README útil están documentados)
- [ ] `data/extracted/` tiene 182 carpetas (o 181 + 1 NO_README)
- [ ] `data/extracted/MANIFEST.json` lista los 182 repos con `chars` y `truncated`
- [ ] `data/readmes_backup.zip` existe y pesa > 1MB
- [ ] `Guia.md`, `Catalogo.md`, `human/*` regenerados sin errores
- [ ] `uv run repo-intelligence recommend --project "bot de WhatsApp con IA" --max-repos 5` funciona correctamente
- [ ] Git commit de todos los cambios

**Solo después de marcar todos los checkboxes:** borrar `../Repositorios_Prueba`.

---

## Archivos a crear/modificar

| Archivo | Acción |
|---|---|
| `src/repo_intelligence/extract/readme.py` | Modificar: ampliar `README_NAMES` con `.rst`, `.markdown`, `.html` |
| `src/repo_intelligence/analysis/curation.py` | Modificar: `build_profile` lee de `data/extracted/` si existe |
| `src/repo_intelligence/extract/readme.py` | Modificar: `read_readme_text` aumentar `max_chars` a 50000 |
| `scripts/extract_all_readmes.py` | Crear: script de extracción masiva |
| `scripts/verify_extraction.py` | Crear: script de verificación de completitud |
| `data/extracted/MANIFEST.json` | Generado por el script de extracción |
| `data/readmes_backup.zip` | Generado por el script de backup |

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Re-curación cambia metadatos que ya estaban buenos | Hacer backup de `INDICE_IA.json` y `INDICE_IA.detalle.json` antes de re-curar |
| Algunos de los 11 repos missing no tienen README | Documentarlos en `data/extracted/MANIFEST.json` con `no_readme: true` |
| markitdown falla en algunos formatos | Fallback a copia raw del archivo |
| `enrich --all` no existe como flag | Usar `analyze --force` + `enrich --new --auto-merge` o agregar el flag |

## Orden de ejecución

```
Fase 1 (fix .rst) → Fase 2 (extraer 182 READMEs) → Fase 3 (procesar 11 missing)
→ Fase 4 (re-curar) → Fase 5 (backup) → Fase 6 (regenerar + verificar)
→ Fase 7 (validación final) → borrar Repositorios_Prueba
```

## Tiempo estimado

- Fases 1-2: extracción de READMEs (I/O bound, ~5-10 min)
- Fase 3: pipeline de 11 repos (~5 min)
- Fase 4: re-curación de 177 repos (~10-15 min)
- Fases 5-7: backup + verificación (~5 min)
