# Plan: Enriquecer y profundizar las guías (`guias/*.md`)

> **Para ejecutores agénticos:** este plan se ejecuta tarea por tarea. Los pasos usan checkboxes (`- [ ]`) para seguimiento. Cada tarea editorial termina con una verificación scriptable y un commit. Recomendado paralelizar por archivo con subagentes (ver "Ejecución").

**Objetivo:** Analizar a fondo los 5 documentos de `guias/` y enriquecer su redacción de forma moderada (~30–50% más texto) en **todas** las secciones —cabecera, tablas de escaneo, comparativas, recetas y las 156 fichas de repos— siendo más específico y técnico, sin inventar datos, y manteniendo sincronizadas la fuente de verdad JSON y el maestro `Guia.md`.

**Enfoque (decisión "Ambos"):**
1. **Editar directamente** los 5 `guias/*.md` (entregable principal).
2. **Espejar** las mismas ediciones de prosa en el maestro `Guia.md` (los `guias/*.md` son un split manual de `Guia.md`; su cuerpo editorial es idéntico y `guide build` no lo reescribe).
3. **Reconciliar la fuente de verdad** `INDICE_IA.json` + `INDICE_IA.detalle.json` (campos `one`, `desc`, `choose_if`, `avoid_if`, `combines_with`, `cat`) para que coincidan con el contenido ya enriquecido y arreglar inconsistencias; luego propagar con `uv run repo-intelligence guide build`.

**Fuentes permitidas para ganar especificidad** (en orden de preferencia):
- `INDICE_IA.detalle.json` (curado: `stack`, `choose_if`, `avoid_if`, `combines_with`, `repo`).
- READMEs locales extraídos en `data/extracted/<id>/readme.md` y, si hace falta, el clon en `../Repositorios_Prueba/<repo>`.
- Web (GitHub / docs oficiales) solo para precisar hechos verificables (lenguaje, dependencias, naturaleza del proyecto, estado/licencia). **Nunca** inventar métricas (stars, benchmarks) ni features no confirmadas.

**Stack/herramientas del proyecto:** Markdown (GitHub-flavored), Python + `uv` (CLI `repo-intelligence`), PowerShell para verificación. Sin tests automáticos: la "verificación" son checks scriptables de integridad (anclas, conteos, campos, columnas de tabla).

---

## Restricciones globales

Estas reglas aplican a **todas** las tareas editoriales:

- **Idioma:** español neutro, técnico y claro. Mantener el tono y los emojis de cabecera ya existentes.
- **Grado de crecimiento:** moderado, ~30–50% por campo. No duplicar el largo. Legibilidad por encima de volumen.
- **No inventar:** solo añadir detalles verificables desde JSON / README / web. Ante la duda, mantener lo genérico. No fabricar números.
- **Estructura de ficha:** conservar los 10 campos actuales en su orden actual; está permitido **añadir** campos opcionales nuevos (ver Contrato) solo donde aporten valor.
- **Integridad de enlaces:** todo enlace interno `[texto](#-ancla)` debe resolver a un encabezado `###` existente. No introducir anclas rotas. Las anclas se derivan del título en minúsculas, sin emoji, con espacios→`-` y signos eliminados (estilo GitHub).
- **Conteo invariante:** al terminar debe haber exactamente **156** fichas (`^\*\*Repo:\*\*`) en `guias/` y **156** en `Guia.md`. No borrar ni fusionar fichas.
- **Tablas:** mantener tablas Markdown válidas (cabecera + separador `|---|` + filas con igual número de columnas). Si se añade una columna, añadirla en cabecera, separador y **todas** las filas de esa tabla.
- **Anti-slop (skills `humanizer`/`stop-slop`):** sin muletillas de IA ("en el mundo de", "en resumen", "cabe destacar"), sin relleno de "regla de tres", uso comedido de rayas (—), nada de lenguaje promocional vacío. Frases concretas y específicas.
- **No tocar** los bloques HTML de estado `<!-- BL_ALEXANDRIA_STATUS -->` salvo en la tarea de cierre, y solo para corregir el conteo si procede.
- **Commits frecuentes:** un commit por tarea (por archivo de guía / por bloque), en español, formato del repo.

---

## Contexto y hallazgos

| Métrica | Valor |
|---|---|
| Archivos de guía | 5 (`guias/guia1.md` … `guia5.md`), ~208 KB total |
| Fichas de repo (`**Repo:**`) | 156 en `guias/` · 156 en `Guia.md` (idénticas) |
| Tablas "Escaneo rápido" + "¿Cuál elegir?" | 33 sub-secciones |
| Categorías | 13 (algunas cruzan el límite entre 2 archivos) |
| Recetas de integración | 9 (en `guia1.md`) |
| Fuente de verdad | `INDICE_IA.json` (compacto) + `INDICE_IA.detalle.json` (detalle por id, key `repos.<id>`) |
| READMEs locales | `data/extracted/<id>/readme.md` (presentes) + clones en `../Repositorios_Prueba` (184) |
| Maestro rico | `Guia.md` (mismo cuerpo que `guias/`; `guide build` solo actualiza conteos y apéndice, no reescribe el cuerpo) |
| Generados por `guide build` | `human/*`, `Catalogo.md`, conteos/apéndice de `Guia.md` — **NO** `guias/` |

**Inconsistencias detectadas a corregir en la Fase 7 (JSON):**
- `choose_if` auto-generados defectuosos en `INDICE_IA.detalle.json` (p. ej. `"quieres why twenty"`, `"quieres ---"`, `"quieres open-source rest api for whatsapp…"`).
- Categoría incorrecta: `openwa` está como `cat: 9` en el JSON pero vive en la categoría 1 en las guías.
- `avoid_if` repetido genérico (`"ya tienes una herramienta equivalente o no encaja con tu stack actual"`) en muchos repos.

**Advertencia operativa:** **No** ejecutar `enrich --auto-merge` tras este trabajo: regeneraría los campos curados desde `data/drafts/` y pisaría las mejoras del JSON. Editar `INDICE_IA*.json` directamente.

---

## Contrato de enriquecimiento (la "interfaz" que toda tarea aplica)

### A. Campos por ficha (conservar los 10, expandir cada uno con moderación)

| Campo | Estado actual | Acción de enriquecimiento |
|---|---|---|
| `Etiquetas` | badges (Ejecución/MCP/Rol/Setup) | Conservar tal cual. No tocar. |
| `Qué es` | ~1 frase | Llevar a 2 frases: qué es + qué primitiva/problema resuelve. Nombrar componentes/lenguajes reales del README. |
| `Por qué destaca` | ~1 frase | 2 frases: diferenciador + evidencia concreta (madurez, procedencia, adopción declarada). Sin números inventados. |
| `Cómo funciona` | ~1 frase | 2 frases con mecanismo/arquitectura concretos (datos del `stack` + README). |
| `Instalación` | comando(s) | Conservar comando(s) y añadir el prerrequisito real (GPU, clave de API, descarga de pesos, servicio dependiente). |
| `Casos` | 2 bullets | Conservar y, si aporta, añadir un 3.º caso concreto. |
| `Stack` / `Modelo/API` | a veces vago | Precisar lenguajes/frameworks/almacenes reales; en Modelo/API nombrar proveedores y aclarar "agnóstico vía variables de entorno" cuando aplique. |
| `Elige si` / `Evita si` | genérico | Afinar a criterios de decisión concretos; cruzar con la alternativa real. |
| `Combina con` | enlaces | Conservar y, si aporta, añadir 1 enlace relevante más (debe resolver a una ancla existente). |
| `Repo` | enlace | Conservar; verificar que la URL no esté vacía (algunos `repo` en JSON están vacíos). |

### B. Campos NUEVOS opcionales (permitidos; usar solo donde aporten valor, con etiqueta uniforme)

Limitar a estos dos para no inflar de forma desigual:
- **`Limitaciones:`** — restricciones reales: coste/GPU, fragilidad o ToS (scrapers como `snscrape`), duplicado (`n8n_io`), estado de mantenimiento, dependencia de credenciales.
- **`Madurez:`** — señal de madurez/licencia notable ("estándar de facto", "archivado", licencia) solo cuando sea verificable y relevante.

> Regla: si un campo nuevo no aporta algo concreto y verificable, **no** se añade. Mejor especificidad que relleno.

### C. Tablas

- **Cabecera global "Mapa de categorías" (`guia1`):** enriquecer la columna "Para qué" con 1–2 ejemplos concretos por categoría. Mantener 4 columnas.
- **"Escaneo rápido" (por categoría):** enriquecer el texto de las celdas para que sea específico. Donde la tabla **no** tenga ya columna de `Setup`, añadir columna `Setup` (🟢/🟡/🔴) tomada de la `Etiquetas` de cada ficha. Mantener consistencia dentro de cada tabla.
- **"¿Cuál elegir?":** afinar el texto de las celdas a criterios concretos. Donde falte la columna `Evítalo si…` (p. ej. la comparativa de MCP), añadirla.
- **Recetas (`guia1`):** ampliar cada receta con una línea de "Cuándo NO usar este stack" o un matiz de "Cómo encaja" donde sea corto; mantener los enlaces existentes intactos.

### D. Sincronización a `Guia.md` y al JSON

- Cada edición de prosa en `guias/guiaN.md` se aplica **idéntica** en `Guia.md` (el `old_string` es único e idéntico en ambos archivos).
- Tras enriquecer la prosa, en Fase 7 se vuelca a `INDICE_IA.detalle.json` (`desc` 1–2 frases en español alineadas con "Qué es"; `choose_if`/`avoid_if` espejo de "Elige si"/"Evita si"; `combines_with` alineado con "Combina con") y a `INDICE_IA.json` (`one`).

### E. Ejemplo trabajado (plantilla — antes/después)

**Ficha `twenty-main` — ANTES:**
```markdown
### 👥 twenty-main
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** CRM open-source orientado a desarrolladores, alternativa moderna y personalizable a Salesforce/HubSpot que modela tu negocio mediante objetos y campos propios.
**Por qué destaca:** es uno de los CRM open-source más populares y con mayor crecimiento en GitHub, valorado por su UI moderna y su enfoque versionable como código.
**Cómo funciona:** una arquitectura basada en metadatos define objetos, campos y relaciones sobre PostgreSQL, con backend NestJS y frontend React.
**Instalación:** vía `docker compose` con la imagen oficial, o clonando el repo y levantando los servicios con el stack Node/PostgreSQL.
**Casos:** pipelines de venta versionados como código · panel a medida con objetos/campos propios.
**Stack:** TypeScript, React, NestJS, PostgreSQL, Docker — **Modelo/API:** opcional (plugins Claude Code/Codex para consultar el CRM en lenguaje natural).
**Elige si:** quieres un CRM que se adapte 1:1 a tu negocio — **Evita si:** buscas algo plug-and-play sin self-host.
**Combina con:** [evolution-api](#-evolution-api) · [n8n](#-n8n)
**Repo:** [GitHub](https://github.com/twentyhq/twenty)
```

**Ficha `twenty-main` — DESPUÉS (objetivo, ~+40%, +1 campo `Limitaciones`):**
```markdown
### 👥 twenty-main
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** CRM open-source orientado a equipos técnicos, pensado como alternativa moderna a Salesforce/HubSpot que modelas con tus propios objetos, campos y relaciones. La premisa es tratar el CRM como una pieza más de tu stack: lo construyes, lo despliegas y lo versionas igual que el código.
**Por qué destaca:** combina una UI cuidada con un modelo de datos totalmente personalizable, lo que evita el "molde" rígido de los CRM SaaS. Su enfoque "construye tu propio CRM" y su comunidad activa lo han vuelto una de las opciones open-source de referencia para este caso.
**Cómo funciona:** una arquitectura dirigida por metadatos describe objetos, campos y relaciones que se materializan en PostgreSQL; el backend en NestJS expone una API (GraphQL/REST) que consume un frontend en React. Todo corre en contenedores para reproducir el entorno.
**Instalación:** la vía soportada es `docker compose` con la imagen oficial (levanta app, base de datos y worker); también puedes clonar el repo y arrancar los servicios con el stack Node/PostgreSQL para desarrollo. Requiere PostgreSQL y recursos no triviales (de ahí el setup 🔴).
**Casos:** pipelines de venta versionados como código · panel a medida con objetos/campos propios · base de datos de clientes integrada con tus automatizaciones.
**Stack:** TypeScript, React, NestJS, PostgreSQL, Docker — **Modelo/API:** no requiere LLM; opcionalmente, plugins de Claude Code/Codex permiten consultar el CRM en lenguaje natural.
**Elige si:** quieres un CRM que se adapte 1:1 a tu negocio y vivir en self-host — **Evita si:** buscas algo plug-and-play gestionado o no quieres operar PostgreSQL y Docker.
**Limitaciones:** self-host con setup pesado; necesitas mantener la base de datos y las actualizaciones tú mismo.
**Combina con:** [evolution-api](#-evolution-api) · [n8n](#-n8n)
**Repo:** [GitHub](https://github.com/twentyhq/twenty)
```

**Ejemplo de fila de "Escaneo rápido" con columna `Setup` añadida — ANTES:**
```markdown
| Repo | Qué es | Ejec. | Elige si… |
|---|---|---|---|
| [twenty-main](#-twenty-main) | CRM open-source tipo Salesforce | 🔀 | Quieres un CRM versionable como código |
```
**DESPUÉS:**
```markdown
| Repo | Qué es | Ejec. | Setup | Elige si… |
|---|---|---|---|---|
| [twenty-main](#-twenty-main) | CRM open-source y versionable tipo Salesforce | 🔀 | 🔴 | Quieres un CRM que modelas con tus propios objetos |
```

---

## Mapa de trabajo (qué hay en cada archivo)

| Archivo | Categorías | Fichas | Tablas (escaneo/comparativas) | Notas |
|---|---|---|---|---|
| `guia1.md` | Cabecera + Cat 1 (Automatización) + Cat 2 (Skills, parte 1/2) | 27 | Cat1: 1 escaneo + 2 comparativas · Cat2: 1 escaneo + 2 comparativas | Contiene cabecera global (leyenda, mapa, 9 recetas) + bloque estado |
| `guia2.md` | Cat 2 (resto) + Cat 3 (Frameworks) + Cat 4 (Scraping, parte 1/2) | 34 | Cat3: 1 escaneo + 2 comparativas · Cat4: 1 escaneo + 2 comparativas | Las tablas de Cat 2 viven en `guia1` |
| `guia3.md` | Cat 4 (resto) + Cat 5 (MCP) + Cat 6 (Memoria/LLM Ops) + Cat 7 (Código/Datos) | 34 | Cat5: 1+1 · Cat6: 1+1 · Cat7: 1+2 | Comparativa MCP sin `Evítalo si…` (añadir) |
| `guia4.md` | Cat 8 (Workspaces) + Cat 9 (Diseño/UI) + Cat 10 (Analítica) + Cat 11 (Imagen, parte 1/2) | 30 | Cat8: 1+1 · Cat9: 1+2 · Cat10: 1+1 · Cat11: 1+2 | — |
| `guia5.md` | Cat 11 (resto) + Cat 12 (Audio/Voz/Video) + Cat 13 (Documentos) | 31 | Cat12: 1+2 · Cat13: 1 escaneo | — |

> Cada categoría vive completa dentro de un solo archivo en cuanto a sus tablas (escaneo/comparativas viven donde empieza la categoría); solo las **fichas** de Cat 2, Cat 4 y Cat 11 continúan en el archivo siguiente. Por eso editar por archivo no genera conflictos: cada archivo es independiente.

---

## Fases y tareas

### Fase 0 — Preparación, baseline y script de verificación

**Files:**
- Crear: `tools_check/check_guias.ps1` (script de verificación reutilizable)
- Solo lectura: `guias/*.md`, `Guia.md`, `INDICE_IA.detalle.json`

- [ ] **Paso 1 — Baseline de conteos.** Ejecutar y guardar la salida:
```powershell
Get-ChildItem 'guias/*.md' | ForEach-Object { '{0}: {1} fichas' -f $_.Name, (Select-String -Path $_.FullName -Pattern '^\*\*Repo:\*\*').Count }
(Select-String -Path 'Guia.md' -Pattern '^\*\*Repo:\*\*').Count
```
Esperado: `guia1=27, guia2=34, guia3=34, guia4=30, guia5=31`; `Guia.md=156`.

- [ ] **Paso 2 — Crear el script de verificación** `tools_check/check_guias.ps1` que reporte: (a) nº de fichas por archivo, (b) anclas internas `(#-...)` que no tengan un `###` correspondiente, (c) fichas a las que les falte algún campo obligatorio (`Qué es`, `Por qué destaca`, `Cómo funciona`, `Instalación`, `Casos`, `Stack`, `Elige si`, `Combina con`, `Repo`), (d) filas de tabla con nº de columnas distinto a su cabecera.

```powershell
# tools_check/check_guias.ps1
param([string]$Dir = 'guias')
$files = Get-ChildItem "$Dir/*.md"
$headings = @(); foreach ($f in $files) { Get-Content $f.FullName | Where-Object { $_ -match '^### ' } | ForEach-Object {
  $t = ($_ -replace '^###\s+','').Trim()
  $slug = ($t.ToLower() -replace '[^\p{L}\p{Nd}\s-]','' -replace '\s+','-')
  $headings += '#-' + $slug.TrimStart('-') } }
$problems = 0
foreach ($f in $files) {
  $text = Get-Content $f.FullName -Raw
  [regex]::Matches($text,'\]\((#-[^)]+)\)') | ForEach-Object {
    $a = $_.Groups[1].Value
    if ($headings -notcontains $a) { Write-Output "ANCLA ROTA en $($f.Name): $a"; $problems++ } }
}
$total = ($files | ForEach-Object { (Select-String -Path $_.FullName -Pattern '^\*\*Repo:\*\*').Count } | Measure-Object -Sum).Sum
Write-Output "TOTAL fichas: $total (esperado 156)"
Write-Output "PROBLEMAS de ancla: $problems"
```

- [ ] **Paso 3 — Correr el script y verificar baseline limpio.**
Run: `pwsh tools_check/check_guias.ps1`
Esperado: `TOTAL fichas: 156`, `PROBLEMAS de ancla: 0` (si hay anclas rotas preexistentes, anotarlas para no contarlas como regresión).

- [ ] **Paso 4 — Commit.**
```bash
git add tools_check/check_guias.ps1
git commit -m "Agrega script de verificación de integridad de guías"
```

---

### Fase 1 — Cabecera global de `guia1.md` (leyenda, mapa de categorías, recetas) + espejo en `Guia.md`

**Files:**
- Modify: `guias/guia1.md` (líneas ~6–86: leyenda, Mapa de categorías, 9 recetas)
- Modify: `Guia.md` (mismas secciones, cuerpo idéntico)

**Interfaces / invariantes:** no cambiar las 13 filas del mapa ni los anchors de las recetas (`#-1-bot-de-whatsapp-con-ia`, etc.); las recetas son referenciadas por fichas vía "Combina con".

- [ ] **Paso 1 — Enriquecer la leyenda de badges** con una frase de contexto por dimensión (Ejecución/MCP/Rol/Setup), sin cambiar los símbolos.
- [ ] **Paso 2 — Ampliar la columna "Para qué" del Mapa de categorías** con 1–2 ejemplos concretos por categoría (mantener 4 columnas, 13 filas).
- [ ] **Paso 3 — Ampliar cada una de las 9 recetas** con un matiz de "Cómo encaja" o "Cuándo NO" (1 línea), conservando todos los enlaces `[repo](#-ancla)`.
- [ ] **Paso 4 — Aplicar los mismos 3 cambios en `Guia.md`** (mismo `old_string`→`new_string`).
- [ ] **Paso 5 — Verificar anclas.**
Run: `pwsh tools_check/check_guias.ps1`
Esperado: `PROBLEMAS de ancla: 0`, `TOTAL fichas: 156`.
- [ ] **Paso 6 — Commit.**
```bash
git add guias/guia1.md Guia.md
git commit -m "Enriquece cabecera, mapa de categorías y recetas de la guía"
```

---

### Fase 2 — `guia1.md` fichas: Cat 1 (Automatización, 12) + Cat 2 parte 1 (Skills, 15)

**Files:**
- Modify: `guias/guia1.md` (fichas + tablas de escaneo/comparativas de Cat 1 y Cat 2)
- Modify: `Guia.md` (espejo)

**Fichas Cat 1 (12):** `twenty-main`, `evolution-api`, `OpenWA`, `whatsapp-agentkit`, `activepieces`, `n8n`, `n8n_io`, `huginn`, `mautic`, `chatwoot`, `listmonk`, `novu`.
**Fichas Cat 2 parte 1 (15):** `andrej-karpathy-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`, `awesome-claude-code`, `superpowers`, `skills`, `claude-plugins-official`, `agents-towards-production`, `Context-Engineering`, `agent-toolkit`, `n8n-skills`, `marketingskills`, `agency-agents`, `geo-seo-claude`, `prompt-master`.

- [ ] **Paso 1 — Tablas de Cat 1.** Enriquecer celdas del "Escaneo rápido" (línea ~92) y de las 2 comparativas (Canal de WhatsApp, Plataforma de automatización); añadir columna `Setup` al escaneo. Aplicar también en `Guia.md`.
- [ ] **Paso 2 — Fichas Cat 1.** Para cada una de las 12 fichas: leer `data/extracted/<id>/readme.md` (y `INDICE_IA.detalle.json`), aplicar el **Contrato (sección A/B)**, y editar la ficha en `guias/guia1.md` **y** en `Guia.md`. Caso especial `n8n_io`: dejar claro que es duplicado de `n8n` y añadir `Limitaciones:` ("usa la ficha [n8n] en su lugar").
- [ ] **Paso 3 — Tablas de Cat 2.** Enriquecer "Escaneo rápido" (línea ~276) y las 2 comparativas (Catálogos vs. metodología; Anti-slop), añadir columna `Setup`. Espejo en `Guia.md`.
- [ ] **Paso 4 — Fichas Cat 2 parte 1.** Para cada una de las 15 fichas: aplicar el Contrato usando README + JSON; editar en ambos archivos.
- [ ] **Paso 5 — Verificar.**
Run: `pwsh tools_check/check_guias.ps1`
Esperado: `guia1` mantiene 27 fichas; `TOTAL fichas: 156`; `PROBLEMAS de ancla: 0`.
- [ ] **Paso 6 — Commit.**
```bash
git add guias/guia1.md Guia.md
git commit -m "Enriquece fichas y tablas de Automatización y Skills (parte 1)"
```

---

### Fase 3 — `guia2.md`: Cat 2 parte 2 (6) + Cat 3 (Frameworks, 18) + Cat 4 parte 1 (Scraping, 10)

**Files:**
- Modify: `guias/guia2.md`
- Modify: `Guia.md` (espejo)

**Fichas Cat 2 parte 2 (6):** `ui-ux-pro-max-skill`, `taste-skill`, `skills_emil`, `SkillSpector`, `humanizer`, `stop-slop`.
**Fichas Cat 3 (18):** `ag2`, `crewAI`, `langchain`, `langflow`, `dify`, `Flowise`, `OpenHands`, `deer-flow`, `NeMo-Agent-Toolkit`, `hermes-agent`, `openevolve`, `gpt-researcher`, `autoresearch`, `ruflo`, `multica`, `MiroFish`, `llm-council`, `awesome-LangGraph`.
**Fichas Cat 4 parte 1 (10):** `firecrawl`, `crawl4ai`, `scrapy`, `crawlee`, `crawlee-python`, `Scrapling`, `scrapely`, `llm-scraper`, `Scrapegraph-ai`, `playwright`.

- [ ] **Paso 1 — Fichas Cat 2 parte 2 (6).** Aplicar Contrato (README + JSON), editar en `guia2.md` y `Guia.md`. (Las tablas de Cat 2 ya se hicieron en Fase 2.)
- [ ] **Paso 2 — Tablas Cat 3.** Enriquecer "Escaneo rápido" (línea ~80) + comparativas (Frameworks de agentes; Low-code/visual), añadir `Setup`. Espejo en `Guia.md`.
- [ ] **Paso 3 — Fichas Cat 3 (18).** Aplicar Contrato a cada una; editar en ambos archivos. Para scrapers/agentes con dependencias notables, considerar `Limitaciones:` (p. ej. claves de API, sandbox).
- [ ] **Paso 4 — Tablas Cat 4.** Enriquecer "Escaneo rápido" (línea ~344) + comparativas (Crawling/scraping; Web estructurada con LLM), añadir `Setup`. Espejo.
- [ ] **Paso 5 — Fichas Cat 4 parte 1 (10).** Aplicar Contrato; añadir `Limitaciones:` a scrapers frágiles/ToS donde corresponda.
- [ ] **Paso 6 — Verificar.**
Run: `pwsh tools_check/check_guias.ps1` → `guia2` 34 fichas, total 156, anclas 0.
- [ ] **Paso 7 — Commit.**
```bash
git add guias/guia2.md Guia.md
git commit -m "Enriquece Skills (parte 2), Frameworks y Scraping (parte 1)"
```

---

### Fase 4 — `guia3.md`: Cat 4 parte 2 (4) + Cat 5 (MCP, 7) + Cat 6 (Memoria/LLM Ops, 10) + Cat 7 (Código/Datos, 13)

**Files:**
- Modify: `guias/guia3.md`
- Modify: `Guia.md` (espejo)

**Cat 4 parte 2 (4):** `playwright-cli`, `browser-use`, `instaloader`, `snscrape`.
**Cat 5 (7):** `mcp`, `mcp-use`, `servers`, `awesome-mcp-servers`, `mcp-neo4j`, `n8n-mcp`, `public-apis`.
**Cat 6 (10):** `mem0`, `agentmemory`, `mempalace`, `turbovec`, `litellm`, `langfuse`, `llmfit`, `headroom`, `sandbox`, `loguru`.
**Cat 7 (13):** `codegraph`, `graphify`, `graphrag`, `GitNexus`, `DeepSeek-Coder`, `nanoGPT`, `nanochat`, `llm.c`, `how-to-train-your-gpt`, `cosmos`, `data-science-ipython-notebooks`, `awesome-bigdata`, `openai-python`.

- [ ] **Paso 1 — Fichas Cat 4 parte 2 (4).** Aplicar Contrato; `snscrape`/`instaloader` → añadir `Limitaciones:` (fragilidad por cambios de plataforma / ToS).
- [ ] **Paso 2 — Tablas Cat 5.** Enriquecer "Escaneo rápido" (línea ~56) + comparativa "Crear vs. descubrir MCP" (línea ~68): **añadir columna `Evítalo si…`** (hoy solo tiene 2 columnas). Espejo en `Guia.md`.
- [ ] **Paso 3 — Fichas Cat 5 (7).** Aplicar Contrato.
- [ ] **Paso 4 — Tablas Cat 6.** Enriquecer escaneo (línea ~167) + comparativa "Memoria de agentes" (línea ~182), añadir `Setup`. Espejo.
- [ ] **Paso 5 — Fichas Cat 6 (10).** Aplicar Contrato.
- [ ] **Paso 6 — Tablas Cat 7.** Enriquecer escaneo (línea ~317) + 2 comparativas (Entender código vs. grafos; Entrenar desde cero), añadir `Setup`. Espejo.
- [ ] **Paso 7 — Fichas Cat 7 (13).** Aplicar Contrato; repos didácticos de entrenamiento → `Limitaciones:` (GPU/escala) cuando aplique.
- [ ] **Paso 8 — Verificar.** `pwsh tools_check/check_guias.ps1` → `guia3` 34, total 156, anclas 0.
- [ ] **Paso 9 — Commit.**
```bash
git add guias/guia3.md Guia.md
git commit -m "Enriquece Scraping (parte 2), MCP, Memoria/LLM Ops e Inteligencia de Código"
```

---

### Fase 5 — `guia4.md`: Cat 8 (Workspaces, 5) + Cat 9 (Diseño/UI, 15) + Cat 10 (Analítica, 7) + Cat 11 parte 1 (Imagen, 3)

**Files:**
- Modify: `guias/guia4.md`
- Modify: `Guia.md` (espejo)

**Cat 8 (5):** `ECC`, `odysseus`, `open-notebook`, `notebooklm-py`, `notebooklm-mcp-cli`.
**Cat 9 (15):** `open-design`, `penpot`, `plasmic`, `design.md`, `impeccable`, `tailwindcss`, `magicui`, `heroui`, `ui (shadcn)`, `normalize.css`, `GSAP`, `motion`, `three.js`, `react-three-fiber`, `swr`.
**Cat 10 (7):** `posthog`, `metabase`, `dash`, `echarts`, `uPlot`, `streamlit`, `awesome-dataviz`.
**Cat 11 parte 1 (3):** `ComfyUI`, `stable-diffusion-webui`, `Fooocus`.

- [ ] **Paso 1 — Tablas Cat 8.** Escaneo (línea ~8) + comparativa "Local privado vs. NotebookLM" (línea ~18), añadir `Setup`. Espejo.
- [ ] **Paso 2 — Fichas Cat 8 (5).** Aplicar Contrato; `notebooklm-py`/`notebooklm-mcp-cli` → `Limitaciones:` (API no oficial, depende de credenciales de Google).
- [ ] **Paso 3 — Tablas Cat 9.** Escaneo (línea ~92) + 2 comparativas (Diseño asistido vs. builder; Librerías de componentes), añadir `Setup`. Espejo.
- [ ] **Paso 4 — Fichas Cat 9 (15).** Aplicar Contrato.
- [ ] **Paso 5 — Tablas Cat 10.** Escaneo (línea ~316) + comparativa "Plataforma vs. librería" (línea ~328), añadir `Setup`. Espejo.
- [ ] **Paso 6 — Fichas Cat 10 (7).** Aplicar Contrato.
- [ ] **Paso 7 — Tablas Cat 11.** Escaneo (línea ~427) + 2 comparativas (Motor de generación; Control y restauración), añadir `Setup`. Espejo.
- [ ] **Paso 8 — Fichas Cat 11 parte 1 (3).** Aplicar Contrato; añadir `Limitaciones:` (GPU) donde aplique.
- [ ] **Paso 9 — Verificar.** `pwsh tools_check/check_guias.ps1` → `guia4` 30, total 156, anclas 0.
- [ ] **Paso 10 — Commit.**
```bash
git add guias/guia4.md Guia.md
git commit -m "Enriquece Workspaces, Diseño/UI, Analítica e Imagen (parte 1)"
```

---

### Fase 6 — `guia5.md`: Cat 11 parte 2 (Imagen, 12) + Cat 12 (Audio/Voz/Video, 15) + Cat 13 (Documentos, 4)

**Files:**
- Modify: `guias/guia5.md`
- Modify: `Guia.md` (espejo)

**Cat 11 parte 2 (12):** `InvokeAI`, `diffusers`, `ControlNet`, `sd-webui-controlnet`, `ComfyUI_IPAdapter_plus`, `GFPGAN`, `Real-ESRGAN`, `LivePortrait`, `Deep-Live-Cam`, `face_recognition`, `Open-Generative-AI`, `fluxer`.
**Cat 12 (15):** `whisper`, `faster-whisper`, `whisperX`, `supertonic`, `VoxCPM`, `TTS`, `OmniVoice-Studio`, `lossless-cut`, `moviepy`, `remotion`, `videofy_minimal`, `OpenCut`, `openscreen`, `Youtube2Webpage`, `hyperframes`.
**Cat 13 (4):** `markitdown`, `ppt-master`, `pdfcraft`, `reveal.js`.

- [ ] **Paso 1 — Fichas Cat 11 parte 2 (12).** Aplicar Contrato (las tablas de Cat 11 ya se hicieron en Fase 5); GPU/uso responsable (p. ej. `Deep-Live-Cam`, `face_recognition`) → `Limitaciones:` concreta.
- [ ] **Paso 2 — Tablas Cat 12.** Escaneo (línea ~152) + 2 comparativas (STT; TTS), añadir `Setup`. Espejo.
- [ ] **Paso 3 — Fichas Cat 12 (15).** Aplicar Contrato.
- [ ] **Paso 4 — Tablas Cat 13.** Escaneo (línea ~375) — enriquecer celdas (no hay comparativa). Espejo.
- [ ] **Paso 5 — Fichas Cat 13 (4).** Aplicar Contrato.
- [ ] **Paso 6 — Verificar.** `pwsh tools_check/check_guias.ps1` → `guia5` 31, total 156, anclas 0.
- [ ] **Paso 7 — Commit.**
```bash
git add guias/guia5.md Guia.md
git commit -m "Enriquece Imagen (parte 2), Audio/Voz/Video y Documentos"
```

---

### Fase 7 — Reconciliar la fuente de verdad JSON y propagar

**Files:**
- Modify: `INDICE_IA.detalle.json` (key `repos.<id>`: `desc`, `choose_if`, `avoid_if`, `combines_with`, `cat`)
- Modify: `INDICE_IA.json` (campo `one` por repo, y `cat` si aplica)
- Genera (no editar a mano): `human/*`, `Catalogo.md`, conteos de `Guia.md` vía `guide build`

- [ ] **Paso 1 — `choose_if`/`avoid_if` por repo.** Reemplazar los `choose_if` auto-generados defectuosos por el texto "Elige si" enriquecido (sin el prefijo "quieres ..."), y `avoid_if` por el "Evita si" concreto de cada ficha. Empezar por los rotos detectados (`twenty-main`, `evolution-api`, `openwa`, y todo el que contenga `"quieres ---"` o `"quieres why "` o `"quieres open-source"`).
- [ ] **Paso 2 — `desc` por repo.** Donde `desc` sea un fragmento crudo de README en inglés o esté mal cortado, sustituir por una descripción de 1–2 frases en español alineada con "Qué es". (Priorizar los más visibles; no es obligatorio reescribir los 156 si ya son correctos.)
- [ ] **Paso 3 — Arreglar categorías.** `openwa`: `cat: 9` → `cat: 1`. Revisar que `combines_with` de cada repo coincida con "Combina con" de su ficha (al menos no contradiga).
- [ ] **Paso 4 — `one` en el índice compacto.** Afinar el `one` (resumen de una línea) de los repos cuyo "Qué es" cambió, para que siga siendo el reflejo corto. Rellenar los `one` vacíos detectados previamente (`tools`, `appsmith`, `budibase`, `llm.c`, `design.md`, `three.js`, `ui`) si están en el índice.
- [ ] **Paso 5 — Validar JSON.**
```powershell
python -c "import json; json.load(open('INDICE_IA.json',encoding='utf-8')); json.load(open('INDICE_IA.detalle.json',encoding='utf-8')); print('JSON OK')"
```
Esperado: `JSON OK`.
- [ ] **Paso 6 — Propagar a generados.**
```powershell
uv run repo-intelligence guide build
```
- [ ] **Paso 7 — Verificar que `guide build` NO pisó el cuerpo enriquecido de `Guia.md`** (solo conteos/apéndice) ni tocó `guias/`:
```powershell
git diff --stat guias/ Guia.md
```
Esperado: `guias/` sin cambios por el build; en `Guia.md` solo cambios de conteo/apéndice si los hubiera.
- [ ] **Paso 8 — Commit.**
```bash
git add INDICE_IA.json INDICE_IA.detalle.json human/ Catalogo.md Guia.md
git commit -m "Reconcilia INDICE_IA con las guías enriquecidas y regenera derivados"
```

---

### Fase 8 — Verificación final y self-review

**Files:** solo lectura + posible corrección puntual del bloque de estado.

- [ ] **Paso 1 — Verificación scriptable completa.**
```powershell
pwsh tools_check/check_guias.ps1
```
Esperado: `TOTAL fichas: 156`, `PROBLEMAS de ancla: 0`, sin campos faltantes ni filas de tabla descuadradas.
- [ ] **Paso 2 — Diff de crecimiento.** Confirmar que el crecimiento por archivo está en el rango moderado (no x3):
```powershell
git diff --stat HEAD~7 -- guias/
```
Revisión humana: cada `guiaN.md` debería crecer aprox. +30–50% en bytes/líneas, no más.
- [ ] **Paso 3 — Self-review anti-slop.** Releer 5–10 fichas al azar contra las reglas `humanizer`/`stop-slop`: sin muletillas de IA, sin relleno, frases concretas. Corregir lo que chirríe.
- [ ] **Paso 4 — Coherencia de conteo de estado.** Si el bloque `<!-- BL_ALEXANDRIA_STATUS -->` quedó desalineado con 156, corregirlo en `guia1.md` y `Guia.md`.
- [ ] **Paso 5 — Commit final (si hubo correcciones).**
```bash
git add guias/ Guia.md
git commit -m "Pulido final y coherencia de conteos en las guías"
```

---

## Criterios de aceptación

- [ ] Las 5 guías y `Guia.md` mantienen **156** fichas; ninguna eliminada ni fusionada.
- [ ] Cada ficha conserva sus 10 campos; los campos nuevos (`Limitaciones`/`Madurez`) solo aparecen donde aportan algo concreto.
- [ ] Todas las tablas son válidas; las que recibieron columna `Setup`/`Evítalo si…` están completas en cabecera, separador y filas.
- [ ] `pwsh tools_check/check_guias.ps1` → 0 anclas rotas, 0 campos faltantes.
- [ ] `INDICE_IA.json` y `INDICE_IA.detalle.json` parsean; `choose_if`/`avoid_if` ya no contienen los patrones defectuosos; `openwa` en `cat 1`.
- [ ] `guide build` corre sin error y no pisa el cuerpo editorial de `Guia.md` ni `guias/`.
- [ ] Crecimiento por documento ~30–50% (moderado), redacción en español, sin slop.

## Riesgos y mitigaciones

- **Doble edición (guías + `Guia.md`) desincronizada.** Mitigación: usar el mismo `old_string`→`new_string` en ambos en el mismo paso; el verificador de conteo (156/156) detecta divergencias groseras.
- **Anclas rotas al reescribir títulos.** Mitigación: **no** cambiar los títulos `###` de las fichas (solo el cuerpo); `check_guias.ps1` valida anclas en cada fase.
- **`enrich --auto-merge` pisando el JSON.** Mitigación: documentado — no ejecutarlo; editar JSON directamente.
- **Inflar de más / slop.** Mitigación: grado moderado fijado en Restricciones; self-review anti-slop en Fase 8; `git diff --stat` para vigilar el tamaño.
- **Datos no verificables.** Mitigación: prohibido inventar; ante duda, mantener genérico.

## Self-review del plan (hecho)

- **Cobertura:** las 13 categorías, las 156 fichas, las 33 tablas, la cabecera y las 9 recetas están asignadas a una fase. ✓
- **Sin placeholders:** Contrato con ejemplo trabajado completo (antes/después) + reglas exactas por campo y tabla. ✓
- **Consistencia:** nombres de campos (`Qué es`, `Por qué destaca`, …) y de fichas tomados de los archivos reales; rutas exactas; comandos de verificación concretos. ✓

---

## Ejecución (handoff)

Plan guardado en `PLAN_ENRIQUECER_GUIAS.md`. Dos opciones:

1. **Subagentes en paralelo (recomendado para velocidad).** Las Fases 2–6 editan **archivos distintos** (`guia1`…`guia5`) y son independientes → un subagente por archivo, con `Guia.md` como punto de cuidado (las ediciones de espejo a `Guia.md` deben serializarse o asignarse a un solo agente para evitar conflictos de escritura sobre el mismo archivo). Las Fases 0, 1, 7 y 8 son secuenciales.
2. **Ejecución inline (más simple, sin conflictos).** Hacer las fases en orden 0→8 en esta sesión, con checkpoint de revisión tras cada fase.

> Nota sobre paralelismo: como cada Fase 2–6 también edita `Guia.md`, si se paralelizan habría escritura concurrente sobre `Guia.md`. Opción segura: en paralelo solo se editan los `guias/guiaN.md`; el espejo a `Guia.md` se aplica al final en una pasada secuencial (Fase 6.bis) reutilizando los mismos `old_string`→`new_string`.
