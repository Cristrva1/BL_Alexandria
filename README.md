# Repo Intelligence Hub

Repo Intelligence Hub ayuda a una persona a decidir que repositorios de una biblioteca de IA debe usar para construir un proyecto concreto.

La biblioteca curada tiene **212 repositorios** en `INDICE_IA.json` (el mismo conjunto en `INDICE_IA.detalle.json`). En disco hay **208 clones git** en `../Repositorios_Prueba`, más tres carpetas locales (`guia`, `tools`, `twenty-main`) y el alias `n8n-io`. El caso de uso principal es simple: llegas con una idea, dices con que herramienta la vas a construir, y el sistema te recomienda que instalar, que leer, que diferir y en que orden avanzar. Si no nombras herramienta y `--tool` queda en `auto`, no se asume Codex.

```powershell
uv run repo-intelligence recommend --project "bot de WhatsApp con IA para responder clientes y guardar leads. Lo voy a construir con Codex." --max-repos 7
```

## Explorar la biblioteca sin instalar nada

Si solo quieres ver que repos contiene la biblioteca, no hace falta leer este README entero ni abrir repos completos:

| Quiero ver... | Abrir |
|---|---|
| Catalogo completo de repos | [Catalogo.md](Catalogo.md) |
| Guia monolitica completa | [Guia.md](Guia.md) |
| Guia humana navegable | [human/README.md](human/README.md) |
| Repos por categoria | [human/categorias/](human/categorias/) |
| Fichas individuales | [human/fichas/](human/fichas/) |
| Comparativas entre alternativas | [human/comparativas/](human/comparativas/) |
| Playbooks o recetas end-to-end | [human/playbooks/](human/playbooks/) |
| Indice compacto para IA | [ai_index/REPOS.scan.json](ai_index/REPOS.scan.json) |
| Menu portable para otro proyecto | [menu_portable/](menu_portable/) |

El README explica como usar el sistema. El catalogo y las guias viven en archivos separados para que GitHub sea navegable sin convertir esta portada en un documento enorme.

## Rutas locales

Por defecto, el proyecto espera una biblioteca de repos clonados en una carpeta local hermana:

```txt
../Repositorios_Prueba
```

El proyecto se ejecuta desde la carpeta donde clonaste este repositorio:

```txt
BL_Alexandria
```

Si lo clonas en otra maquina, cambia esas rutas en:

```txt
config/paths.yaml
```

## Menu portable para otro proyecto

El comando `menu export` genera un paquete autocontenido y optimizado para tokens que puedes copiar a la raiz de un proyecto NUEVO. Una IA lee ese paquete y decide que repos instalar sin visitar la web ni abrir READMEs completos.

```powershell
uv run repo-intelligence menu export
```

Salida:

```txt
menu_portable/
    REPO_MENU.md            <- ENTRY POINT. La IA lee solo esto para preseleccionar.
    REPO_MENU_cats/         <- detalle por categoria (abrir solo para finalistas)
        01-*.md ... 13-*.md
    REPO_MENU_DATA.json     <- espejo machine-readable (opcional)
```

Como lo usa la IA (el protocolo esta dentro del propio `REPO_MENU.md`):

1. Lee `REPO_MENU.md` y filtra candidatos por categoria, `role`, `exec`, `setup` y la descripcion de una linea por repo.
2. Desempata con `alt`/alternativas: si ya eligio un repo, descarta sus alternativas.
3. Combina con `recipes` si el proyecto es un flujo end-to-end.
4. Solo para finalistas (<8): abre el archivo de su categoria en `REPO_MENU_cats/` para ver desc completa, `choose_if`, `avoid_if`, `combines_with` y el comando de instalacion derivado.
5. Instala con el comando marcado por confianza: `+` seguro, `~` verificar nombre de paquete, `?` solo clone + README.

Para copiarlo directamente a otro proyecto:

```powershell
uv run repo-intelligence menu export -o ../mi_nuevo_proyecto/menu_portable
```

Y en el `AGENTS.md` o system prompt de ese proyecto:

```txt
Antes de elegir dependencias, lee menu_portable/REPO_MENU.md y sigue su protocolo.
```

Regenera el paquete cada vez que agregues o cure repos nuevos (`discover` + `analyze` + `enrich` + `guide build` + `menu export`).

## Las 2 partes del proyecto

### 1. Decidir que instalar para un proyecto nuevo

Esta es la parte prioritaria.

Un usuario llega con una idea, por ejemplo:

```txt
Quiero hacer un bot de WhatsApp con IA para responder clientes, guardar leads y escalar a humano. Lo voy a construir con Codex.
```

El sistema debe responder:

- Que repositorios conviene usar.
- Cuales instalar globalmente.
- Cuales instalar dentro del proyecto.
- Cuales levantar con Docker.
- Cuales solo leer como referencia.
- Cuales diferir o evitar.
- En que orden instalarlos.
- Que indices debe leer Codex, Claude Code, Antigravity, Grok Build u Open Code para no gastar tokens de mas.

Comando principal:

```powershell
uv run repo-intelligence recommend --project "quiero hacer un bot de WhatsApp con IA para responder clientes, guardar leads y escalar a humano. Lo voy a construir con Codex." --max-repos 7
```

`--tool` es opcional y por defecto vale `auto`. El sistema intenta tomar la herramienta desde la redaccion del proyecto. Si pones `auto` y el brief no nombra herramienta, no se asume Codex y no hay boost de catalogo de skills. Si quieres dar una pista manual, estas son las opciones aceptadas:

```txt
auto
codex
claude
claude-code
antigravity
grok-build
open-code
```

El resultado se imprime en terminal y tambien genera una super guia practica especifica para ese proyecto:

```txt
ai_index/SUPERGUIAS/<nombre-del-proyecto>.md
```

Tambien actualiza este alias con la ultima recomendacion:

```txt
ai_index/CONTEXT_PACKS/latest.md
```

La super guia generada es el archivo mas importante para cualquier IA. Incluye diagnostico de intencion, herramienta efectiva inferida, finalistas, por que entra cada repo, como funciona, orden de instalacion, si va global/local/Docker/referencia, cautelas, instrucciones para humano e instrucciones para una IA instaladora. Puedes decirle a cualquier chat/agente:

```txt
Lee ai_index/CONTEXT_PACKS/latest.md. Con eso decide que repos instalar, en que modo y en que orden. No leas repos completos salvo finalistas.
```

Tambien puedes compartir el archivo de `ai_index/SUPERGUIAS/` con otra IA si no quieres darle toda la biblioteca ni perder recomendaciones anteriores.

Regla importante: la descripcion del proyecto manda. Si escribes "optimizar Claude Code", el sistema prioriza el ecosistema Claude Code aunque no pongas `--tool`.

### 2. Mantener y mejorar la biblioteca

Esta es la segunda parte.

Sirve para actualizar los repos clonados, detectar cambios, regenerar catalogos, fichas, comparativas, playbooks, guias e indices para humanos e IAs.

Flujo de mantenimiento:

```powershell
uv run repo-intelligence doctor
uv run repo-intelligence pull --safe
uv run repo-intelligence discover
uv run repo-intelligence snapshot
uv run repo-intelligence scan --changed-only
uv run repo-intelligence score
uv run repo-intelligence conflicts
uv run repo-intelligence decide --project-type repo_library_management
uv run repo-intelligence guide build
uv run repo-intelligence menu export
uv run repo-intelligence report daily
```

**Al agregar nuevos repositorios a la biblioteca (para que tengan toda la información técnica y teórica completa):**

```powershell
# 1. Descubrir
uv run repo-intelligence discover

# 2. Análisis profundo (repomix + markitdown + extracción)
uv run repo-intelligence analyze --new

# 3. Generar borradores ricos + incorporar (inferencia de cat, stack, choose/avoid, etc.)
uv run repo-intelligence enrich --new --auto-merge

# 4. Regenerar catálogos, fichas, Guia.md, human/* e índices
uv run repo-intelligence guide build

# 5. Regenerar el menú portable para otros proyectos
uv run repo-intelligence menu export
```

Ver también AGENTS.md → sección Mantenimiento para el flujo completo y recomendaciones de revisión de drafts en `data/drafts/`.

`pull --safe` usa red porque ejecuta Git contra los remotos. Los demas comandos son locales.

`scan --changed-only` y `guide build --changed-only` aceptan el flag por compatibilidad; V1 regenera todo. `score`, `conflicts`, `decide` y `report daily` leen los indices reales: `conflicts` sale de pares `alt`, `score` resume el scan, `decide` usa `analysis/decisions.py`. El modo de instalacion de cada repo (`global` / `local_project` / `docker_local` / `reference_only` / `deferred`) vive en un solo sitio: `src/repo_intelligence/core/install_mode.py`, alimentado por `config/repo_policy.yaml`.

## Estado actual frente a los 2 objetivos

| Objetivo | Estado | Notas |
|---|---|---|
| Usuario describe proyecto y herramienta de construccion | Cubierto | `recommend --project ...` o `recommend --project-file proyecto.md` genera una super guia practica por proyecto. |
| Elegir repos por funcion real | Cubierto | Usa `REPOS.scan`, `REPOS.detail`, tags, recetas, boosts por herramienta e intencion detectada. |
| Decidir global/local/Docker/referencia/diferido | Cubierto | Una sola `install_mode` (recommend, scan y fichas humanas) leida de `config/repo_policy.yaml`. |
| Explicar orden de instalacion | Cubierto | La super guia separa global/local/Docker/referencia/diferido y da el orden operativo. |
| Generar guia practica por repo finalista | Cubierto inicial | Incluye por que, como funciona, pasos, cautelas e instrucciones para humano/IA; algunos comandos exactos aun dependen del README finalista. |
| Inferir herramienta objetivo desde el texto | Cubierto | Si el brief nombra Claude Code/Codex/etc. gana el texto. Si `--tool auto` y el brief no nombra herramienta, queda `auto` (no se asume Codex). |
| Instalar automaticamente repos elegidos | No automatico | Por seguridad, el sistema recomienda; la instalacion se ejecuta despues conscientemente. |
| Actualizar biblioteca local | Cubierto | `pull --safe`, `discover`, `snapshot`. |
| Regenerar catalogos/guias/fichas/playbooks | Cubierto | `guide build` genera salidas humanas e indices IA. |
| Exportar menu portable para otro proyecto | Cubierto | `menu export` genera `menu_portable/` autocontenido con comandos de instalacion derivados. |
| Usar APIs de IA | No por defecto | La V1 es deterministica. |

## Instalacion del sistema

### Requisitos globales

Instala o verifica:

```powershell
git --version
gh --version
node --version
npm --version
pnpm --version
uv --version
docker --version
repomix --version
gitnexus --version
markitdown --help
```

Si falta algo, comandos sugeridos:

```powershell
winget install -e --id Git.Git
winget install -e --id GitHub.cli
winget install -e --id OpenJS.NodeJS.LTS
winget install -e --id Docker.DockerDesktop
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
npm install -g pnpm repomix gitnexus
uv tool install "markitdown[all]"
```

### Instalacion local del proyecto

Desde la carpeta donde clonaste este proyecto:

```powershell
cd BL_Alexandria
```

Instala con `uv`:

```powershell
uv sync --python 3.13
uv run crawl4ai-setup
uv run crawl4ai-doctor
```

Alternativa con `requirements.txt`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

Recomendado: usa `uv`, porque respeta `uv.lock` y reproduce mejor el entorno.

## Uso para una persona promedio

### Paso 1: Escribe tu idea

Mientras mas concreto, mejor:

```txt
Quiero crear un sistema para analizar campañas de Meta Ads, scrapear datos publicos de competencia, generar reportes ejecutivos y automatizar envios por email. Lo voy a construir con Claude Code.
```

### Paso 2: Ejecuta `recommend`

```powershell
uv run repo-intelligence recommend --project "Quiero crear un sistema para analizar campañas de Meta Ads, scrapear datos publicos de competencia, generar reportes ejecutivos y automatizar envios por email. Lo voy a construir con Claude Code." --max-repos 7
```

Si el planteamiento es largo, crea un archivo `proyecto.md` en la carpeta del sistema y escribe ahi todo el brief. Luego ejecuta:

```powershell
uv run repo-intelligence recommend --project-file proyecto.md --max-repos 7
```

Tambien puedes combinar una frase corta con el archivo:

```powershell
uv run repo-intelligence recommend --project "Prioriza instalacion local primero" --project-file proyecto.md --max-repos 7
```

### Paso 3: Lee el resultado

El sistema separa:

| Tipo | Que hacer |
|---|---|
| `global` | Instalar una vez para toda la maquina. |
| `local_project` | Instalar dentro del proyecto concreto. |
| `docker_local` | Preparar en `infra/` y levantar con Docker cuando toque. |
| `reference_only` | Leer/copiar ideas; no instalar completo. |
| `deferred` | No instalar en la primera version. |

### Paso 4: Dale el contexto a tu agente de IA

Archivos generados:

```txt
ai_index/SUPERGUIAS/<nombre-del-proyecto>.md
ai_index/CONTEXT_PACKS/latest.md
```

Prompt recomendado:

```txt
Lee la super guia generada en ai_index/SUPERGUIAS/ o, si estas trabajando con la ultima consulta, ai_index/CONTEXT_PACKS/latest.md. Usa solo los repos recomendados como finalistas. Indica que instalar global, local y Docker. No instales catalogos completos de skills. No leas repos completos salvo que el contexto diga que son finalistas.
```

### Paso 5: Instala en orden

Orden recomendado:

1. Herramientas globales: `git`, `gh`, `uv`, `pnpm`, `repomix`, `gitnexus`, `docker`.
2. Crear carpeta del proyecto real.
3. Instalar dependencias locales elegidas.
4. Copiar o referenciar repos `reference_only` solo si aportan prompts, skills, plantillas o ejemplos.
5. Preparar servicios `docker_local` en `infra/`.
6. Diferir todo lo marcado como `deferred`.

## Ejemplos

### Optimizar Claude Code para uso diario

```powershell
uv run repo-intelligence recommend --project "Quiero optimizar y ultralizar Claude Code para uso diario" --max-repos 7
```

Salida esperada: `superpowers`, `agent-toolkit`, `claude-plugins-official`, `awesome-claude-code`, `skillspector`, `context-engineering`, `prompt-master`. El sistema infiere `claude-code` porque aparece en la descripcion.

### Bot de WhatsApp con IA

```powershell
uv run repo-intelligence recommend --project "bot de WhatsApp con IA para responder clientes, guardar leads y escalar a humano. Lo voy a construir con Codex." --max-repos 7
```

Salida esperada: `evolution-api`, `n8n`, `chatwoot`, `n8n-mcp`, `n8n-skills`, alternativas y diferidos.

### Sistema MCP para Codex

```powershell
uv run repo-intelligence recommend --project "sistema MCP para conectar archivos locales y herramientas a Codex" --max-repos 5
```

Salida esperada: repos MCP, servidores, catálogos y herramientas de conectividad.

### Pipeline de Reels

```powershell
uv run repo-intelligence recommend --project "pipeline de reels con transcripcion, voz, subtitulos y render de video. Lo voy a construir con Antigravity." --max-repos 7
```

Salida esperada: `whisperX`, `supertonic` o `TTS`, `moviepy` o `remotion`, y herramientas de video.

### Web app moderna con IA

```powershell
uv run repo-intelligence recommend --project "web app moderna con IA, dashboard, graficas y frontend pulido. Lo voy a construir con Open Code." --max-repos 7
```

Salida esperada: frontend/UI, datos, graficas, skills de diseño y librerías de apoyo.

## Indices optimizados para IA

Lectura minima, en este orden:

1. `ai_index/SUPERGUIAS/<nombre-del-proyecto>.md` si ya existe una recomendacion para ese proyecto.
2. `ai_index/CONTEXT_PACKS/latest.md` si quieres la ultima recomendacion generada.
3. `menu_portable/REPO_MENU.md` si vas a trabajar en otro proyecto y quieres un menu autocontenido (ver seccion "Menu portable para otro proyecto").
4. `ai_index/WINNERS.json` para decisiones base por funcion.
5. `ai_index/ROUTER.json` para saber que leer primero y que evitar.
6. `ai_index/REPOS.scan.json` para explorar la biblioteca con bajo costo.
7. `ai_index/REPOS.detail.json` solo para finalistas.
8. `human/fichas/<repo>.md` solo para repos candidatos.

## Salidas humanas

| Ruta | Uso |
|---|---|
| `Catalogo.md` | Catalogo humano principal generado. |
| `human/catalogo.md` | Copia navegable del catalogo. |
| `human/fichas/` | Ficha individual por repo. |
| `human/categorias/` | Secciones por categoria. |
| `human/comparativas/` | Comparaciones entre alternativas. |
| `human/playbooks/` | Recetas end-to-end. |

## APIs y red

Por defecto, el sistema no llama a OpenAI, Anthropic, Gemini, Grok ni modelos remotos.

| Comando | Usa red/API | Motivo |
|---|---|---|
| `recommend` | No | Decide desde indices locales. |
| `context build` | No | Genera contexto desde indices locales. |
| `doctor` | No | Verifica entorno. |
| `discover` | No | Recorre carpetas locales. |
| `snapshot` | No | Lee estado Git local. |
| `scan` | No | Reconstruye indices locales. |
| `guide build` | No | Renderiza Markdown desde JSON local. |
| `menu export` | No | Genera el paquete portable desde indices locales. |
| `pull --safe` | Si | Contacta remotos Git. |
| `crawl4ai` runner | Si | Solo si se le da una URL. |
| `gh` | Si | Disponible para metadata GitHub futura, no usado automaticamente en V1. |

## Reglas

- No instalar todos los repos.
- No instalar catalogos completos de skills.
- No usar frameworks multiagente si el problema se resuelve con scripts, indices y reglas.
- No usar Repomix en toda la biblioteca; solo en finalistas.
- No leer repos completos salvo que sean finalistas.
- Diferir herramientas pesadas hasta que el proyecto lo justifique.
