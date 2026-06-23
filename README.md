# Repo Intelligence Hub

Repo Intelligence Hub ayuda a una persona a decidir que repositorios de una biblioteca de IA debe usar para construir un proyecto concreto.

El caso de uso principal es simple: llegas con una idea, dices con que herramienta la vas a construir, y el sistema te recomienda que instalar, que leer, que diferir y en que orden avanzar.

```powershell
uv run repo-intelligence recommend --tool codex --project "bot de WhatsApp con IA para responder clientes y guardar leads" --max-repos 7
```

## Explorar la biblioteca sin instalar nada

Si solo quieres ver que repos contiene la biblioteca, no hace falta leer este README entero ni abrir repos completos:

| Quiero ver... | Abrir |
|---|---|
| Catalogo completo de repos | [Catalogo.md](Catalogo.md) |
| Guia humana navegable | [human/README.md](human/README.md) |
| Repos por categoria | [human/categorias/](human/categorias/) |
| Fichas individuales | [human/fichas/](human/fichas/) |
| Comparativas entre alternativas | [human/comparativas/](human/comparativas/) |
| Playbooks o recetas end-to-end | [human/playbooks/](human/playbooks/) |
| Indice compacto para IA | [ai_index/REPOS.scan.json](ai_index/REPOS.scan.json) |

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
uv run repo-intelligence recommend --tool codex --project "quiero hacer un bot de WhatsApp con IA para responder clientes, guardar leads y escalar a humano" --max-repos 7
```

Herramientas aceptadas en `--tool`:

```txt
codex
claude-code
antigravity
grok-build
open-code
```

El resultado se imprime en terminal y tambien genera el archivo mas importante para cualquier IA:

```txt
ai_index/CONTEXT_PACKS/latest.md
```

Ese archivo es el paquete de contexto optimizado. Puedes decirle a cualquier chat/agente:

```txt
Lee ai_index/CONTEXT_PACKS/latest.md. Con eso decide que repos instalar, en que modo y en que orden. No leas repos completos salvo finalistas.
```

Tambien puedes compartir solo ese archivo con otra IA si no quieres darle toda la biblioteca.

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
uv run repo-intelligence report daily
```

`pull --safe` usa red porque ejecuta Git contra los remotos. Los demas comandos son locales.

## Estado actual frente a los 2 objetivos

| Objetivo | Estado | Notas |
|---|---|---|
| Usuario describe proyecto y herramienta de construccion | Cubierto | `recommend --tool ... --project ...` genera recomendaciones y contexto IA. |
| Elegir repos por funcion real | Cubierto inicial | Usa `REPOS.scan`, `REPOS.detail`, tags, recetas y boosts por herramienta. |
| Decidir global/local/Docker/referencia/diferido | Cubierto inicial | Cada recomendacion trae `install_mode`. |
| Explicar orden de instalacion | Cubierto inicial | `latest.md` separa global/local/Docker/referencia/diferido y da el orden operativo. |
| Generar comandos exactos por repo finalista | Parcial | El sistema aun no extrae automaticamente el comando preciso desde cada README actualizado. |
| Instalar automaticamente repos elegidos | No automatico | Por seguridad, el sistema recomienda; la instalacion se ejecuta despues conscientemente. |
| Actualizar biblioteca local | Cubierto | `pull --safe`, `discover`, `snapshot`. |
| Regenerar catalogos/guias/fichas/playbooks | Cubierto | `guide build` genera salidas humanas e indices IA. |
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
uv run repo-intelligence recommend --tool claude-code --project "Quiero crear un sistema para analizar campañas de Meta Ads, scrapear datos publicos de competencia, generar reportes ejecutivos y automatizar envios por email" --max-repos 7
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

Archivo generado:

```txt
ai_index/CONTEXT_PACKS/latest.md
```

Prompt recomendado:

```txt
Lee ai_index/CONTEXT_PACKS/latest.md. Usa solo los repos recomendados como finalistas. Indica que instalar global, local y Docker. No instales catalogos completos de skills. No leas repos completos salvo que el contexto diga que son finalistas.
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

### Bot de WhatsApp con IA

```powershell
uv run repo-intelligence recommend --tool codex --project "bot de WhatsApp con IA para responder clientes, guardar leads y escalar a humano" --max-repos 7
```

Salida esperada: `evolution-api`, `n8n`, `chatwoot`, `n8n-mcp`, `n8n-skills`, alternativas y diferidos.

### Sistema MCP para Codex

```powershell
uv run repo-intelligence recommend --tool codex --project "sistema MCP para conectar archivos locales y herramientas a Codex" --max-repos 5
```

Salida esperada: repos MCP, servidores, catálogos y herramientas de conectividad.

### Pipeline de Reels

```powershell
uv run repo-intelligence recommend --tool antigravity --project "pipeline de reels con transcripcion, voz, subtitulos y render de video" --max-repos 7
```

Salida esperada: `whisperX`, `supertonic` o `TTS`, `moviepy` o `remotion`, y herramientas de video.

### Web app moderna con IA

```powershell
uv run repo-intelligence recommend --tool open-code --project "web app moderna con IA, dashboard, graficas y frontend pulido" --max-repos 7
```

Salida esperada: frontend/UI, datos, graficas, skills de diseño y librerías de apoyo.

## Indices optimizados para IA

Lectura minima, en este orden:

1. `ai_index/CONTEXT_PACKS/latest.md` si ya existe una descripcion de proyecto.
2. `ai_index/WINNERS.json` para decisiones base por funcion.
3. `ai_index/ROUTER.json` para saber que leer primero y que evitar.
4. `ai_index/REPOS.scan.json` para explorar la biblioteca con bajo costo.
5. `ai_index/REPOS.detail.json` solo para finalistas.
6. `human/fichas/<repo>.md` solo para repos candidatos.

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
