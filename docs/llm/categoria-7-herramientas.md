# Alexandría para agentes · CLIs y SDKs de desarrollo

Categoría 7 «Entender código y comprobar su calidad» › subcategoría `herramientas`. 5 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=7&sub=herramientas · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `lazygit` | Interfaz de terminal sencilla para git: preparar fragmentos o líneas, rebase… | 1 Básico | 71 | MIT (OSI permisiva) | sin grupo |
| `cli` | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la… | 1 Básico | 70 | MIT (OSI permisiva) | sin grupo |
| `openai-python` | SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes… | 2 Intermedio | 68 | Apache-2.0 (OSI permisiva) | sin grupo |
| `fzf` | Buscador difuso de línea de comandos y kit de interfaces de terminal para… | 1 Básico | 61 | MIT (OSI permisiva) | sin grupo |
| `ripgrep` | Búsqueda recursiva de texto por expresiones regulares muy rápida que respeta… | 1 Básico | 53 | Unlicense (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### lazygit (`lazygit`)

- **Repo:** https://github.com/jesseduffield/lazygit · MIT · nivel 1 · 71/100
- **Qué es:** Interfaz de terminal para git de código abierto (MIT) creada por Jesse Duffield y mantenida con la comunidad y patrocinadores. Muy popular y activa.
- **Cuándo elegirlo:** Casos: revisar y preparar por partes los cambios que hizo un agente antes de confirmarlos; hacer rebases interactivos y deshacer operaciones sin recordar comandos.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install lazygit` — fuente: https://github.com/jesseduffield/lazygit/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala lazygit y ábrelo en un repositorio de prueba con cambios sin confirmar. Éxito: Puedes preparar una sola línea y crear el commit desde la interfaz.
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `aider` [20/terminal]
- **Riesgos y avisos:** Lazygit ejecuta comandos git reales: las operaciones destructivas (reset, force push) siguen siendo destructivas.

### GitHub CLI (`cli`)

- **Repo:** https://github.com/cli/cli · MIT · nivel 1 · 70/100
- **Qué es:** GitHub CLI (`gh`), la herramienta oficial de GitHub para la terminal. Licencia MIT. Es madura y muy activa (~47k estrellas, v2.104.0).
- **Cuándo elegirlo:** Casos: Consultar issues desde terminal; Revisar ejecuciones de Actions.
- **Requisitos:** nivel 1: preparación sencilla; Binario gh oficial; cuenta GitHub para operaciones autenticadas; hardware prerequisites; API de IA: no; Binario gh oficial; cuenta GitHub para operaciones autenticadas.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/cli/cli.git gh-cli` — fuente: https://github.com/cli/cli/blob/trunk/docs/install_source.md
- **Primera prueba propuesta (no ejecutada):** Autentica tu cuenta y consulta el estado de una pull request de un repositorio de prueba Éxito: Ves el estado que coincide con la interfaz de GitHub
- **Combina con:** `claude-code` [20/terminal], `github-mcp-server` [5/servidores], `activepieces` [1/motores], `antigravity-awesome-skills` [2/catalogos], `awesome-copilot` [2/catalogos]
- **Riesgos y avisos:** Sin alternativas declaradas. Limita los scopes del token que uses con agentes. Instala gh antes de instalar su skill opcional; los comandos que escriben o publican afectan la cuenta autenticada.

### openai-python (`openai-python`)

- **Repo:** https://github.com/openai/openai-python · Apache-2.0 · nivel 2 · 68/100
- **Qué es:** SDK oficial de OpenAI para Python. Licencia Apache-2.0. Es madura y muy activa (~32k estrellas, v3.51.0) y se genera a partir de la especificación OpenAPI de OpenAI.
- **Cuándo elegirlo:** Casos: Integrar respuestas de IA en una app Python; Procesar audio o imágenes desde código.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él, requiere clave de API; Python 3.10+; entorno virtual; clave de proyecto API; hardware prerequisites; API de IA: sí; Python 3.10+; entorno virtual; clave de proyecto API.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/openai/openai-python/blob/main/README.md

  ```sh
  # install from PyPI
  pip install openai
  ```
- **Primera prueba propuesta (no ejecutada):** Envía una petición breve de ejemplo y revisa respuesta y uso informado Éxito: Obtienes la salida del endpoint y puedes localizar el consumo del proyecto
- **Combina con:** `litellm` [23/serving], `vllm` [23/serving], `langchain` [3/py], `openai-agents-python` [3/py], `openai-cookbook` [19/guias]
- **Riesgos y avisos:** Sin alternativas declaradas. Es un cliente oficial de API, no un plugin de Codex; base_url configurable no confirma todas las funciones de servidores locales.

### fzf (`fzf`)

- **Repo:** https://github.com/junegunn/fzf · MIT · nivel 1 · 61/100
- **Qué es:** Buscador difuso de propósito general de código abierto (MIT) creado y mantenido por Junegunn Choi desde 2013. Muy maduro y extendido.
- **Cuándo elegirlo:** Casos: buscar archivos y comandos del historial al instante en la terminal; construir menús interactivos en scripts de shell.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Gemfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install fzf` — fuente: https://github.com/junegunn/fzf/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala fzf, activa la integración de tu shell y pulsa CTRL-T para elegir un archivo. Éxito: El selector filtra miles de archivos al escribir y pega la ruta elegida en la línea de comandos.
- **Combina con:** `ripgrep`, `claude-code` [20/terminal], `codex` [20/terminal]
- **Riesgos y avisos:** Es una herramienta de uso diario: no requiere servidor ni configuración para empezar.

### ripgrep (`ripgrep`)

- **Repo:** https://github.com/BurntSushi/ripgrep · Unlicense · nivel 1 · 53/100
- **Qué es:** Herramienta de búsqueda de código abierto con doble licencia MIT o Unlicense, creada por Andrew Gallant (BurntSushi). Muy madura; la usan editores como VS Code y muchos agentes de código.
- **Cuándo elegirlo:** Casos: localizar todas las apariciones de una función en un repositorio grande; buscar texto en miles de archivos de logs o notas en segundos.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install ripgrep` — fuente: https://github.com/BurntSushi/ripgrep/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala ripgrep y ejecuta `rg` con un patrón en un repositorio. Éxito: Obtienes las coincidencias con archivo y línea, sin resultados de carpetas ignoradas.
- **Combina con:** `fzf`, `claude-code` [20/terminal], `opencode` [20/terminal]
- **Riesgos y avisos:** Es la herramienta de búsqueda que asumen muchos agentes de terminal; conviene tenerla instalada.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-7-herramientas.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «CLIs y SDKs de desarrollo», lee `docs/alexandria/categoria-7-herramientas.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-7-herramientas.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
