# Alexandría para agentes · CLIs y SDKs de desarrollo

Categoría 7 «Entender código y comprobar su calidad» › subcategoría `herramientas`. 11 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
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
| `openai-python` | SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes… | 2 Intermedio | 75 | Apache-2.0 (OSI permisiva) | sin grupo |
| `cli` | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la… | 1 Básico | 74 | MIT (OSI permisiva) | sin grupo |
| `lazygit` | Interfaz de terminal sencilla para git: preparar fragmentos o líneas, rebase… | 1 Básico | 71 | MIT (OSI permisiva) | sin grupo |
| `fzf` | Buscador difuso de línea de comandos y kit de interfaces de terminal para… | 1 Básico | 67 | MIT (OSI permisiva) | sin grupo |
| `pake` | Convierte una página web o una carpeta con tu web estática en una app de… | 2 Intermedio | 60 | GPL-3.0 (open-core) | sin grupo |
| `requests-cache` | Guarda respuestas de solicitudes Python para reutilizarlas cuando sean válidas… | 2 Intermedio | 59 | BSD-2-Clause (OSI permisiva) | sin grupo |
| `apscheduler` | Programa funciones Python para un horario, un intervalo o una fecha concreta… | 2 Intermedio | 57 | MIT (OSI permisiva) | sin grupo |
| `npkill` | Muestra cuánto espacio ocupan carpetas generadas por herramientas de desarrollo… | 1 Básico | 56 | MIT (OSI permisiva) | sin grupo |
| `hishel` | Añade caché a peticiones HTTP de Python con políticas de expiración y… | 2 Intermedio | 53 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `ripgrep` | Búsqueda recursiva de texto por expresiones regulares muy rápida que respeta… | 1 Básico | 52 | Unlicense (OSI permisiva) | sin grupo |
| `pybreaker` | Protege una integración Python con un interruptor que pausa llamadas tras… | 2 Intermedio | 44 | BSD-3-Clause (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### openai-python (`openai-python`)

- **Repo:** https://github.com/openai/openai-python · Apache-2.0 · nivel 2 · 75/100
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

### GitHub CLI (`cli`)

- **Repo:** https://github.com/cli/cli · MIT · nivel 1 · 74/100
- **Qué es:** GitHub CLI (`gh`), la herramienta oficial de GitHub para la terminal. Licencia MIT. Es madura y muy activa (~47k estrellas, v2.104.0).
- **Cuándo elegirlo:** Casos: Consultar issues desde terminal; Revisar ejecuciones de Actions.
- **Requisitos:** nivel 1: preparación sencilla; Binario gh oficial; cuenta GitHub para operaciones autenticadas; hardware prerequisites; API de IA: no; Binario gh oficial; cuenta GitHub para operaciones autenticadas.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/cli/cli.git gh-cli` — fuente: https://github.com/cli/cli/blob/trunk/docs/install_source.md
- **Primera prueba propuesta (no ejecutada):** Autentica tu cuenta y consulta el estado de una pull request de un repositorio de prueba Éxito: Ves el estado que coincide con la interfaz de GitHub
- **Combina con:** `claude-code` [20/terminal], `github-mcp-server` [5/servidores], `activepieces` [1/motores], `antigravity-awesome-skills` [2/catalogos], `awesome-copilot` [2/catalogos]
- **Riesgos y avisos:** Sin alternativas declaradas. Limita los scopes del token que uses con agentes. Instala gh antes de instalar su skill opcional; los comandos que escriben o publican afectan la cuenta autenticada.

### lazygit (`lazygit`)

- **Repo:** https://github.com/jesseduffield/lazygit · MIT · nivel 1 · 71/100
- **Qué es:** Interfaz de terminal para git de código abierto (MIT) creada por Jesse Duffield y mantenida con la comunidad y patrocinadores. Muy popular y activa.
- **Cuándo elegirlo:** Casos: revisar y preparar por partes los cambios que hizo un agente antes de confirmarlos; hacer rebases interactivos y deshacer operaciones sin recordar comandos.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install lazygit` — fuente: https://github.com/jesseduffield/lazygit/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala lazygit y ábrelo en un repositorio de prueba con cambios sin confirmar. Éxito: Puedes preparar una sola línea y crear el commit desde la interfaz.
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `aider` [20/terminal]
- **Riesgos y avisos:** Lazygit ejecuta comandos git reales: las operaciones destructivas (reset, force push) siguen siendo destructivas.

### fzf (`fzf`)

- **Repo:** https://github.com/junegunn/fzf · MIT · nivel 1 · 67/100
- **Qué es:** Buscador difuso de propósito general de código abierto (MIT) creado y mantenido por Junegunn Choi desde 2013. Muy maduro y extendido.
- **Cuándo elegirlo:** Casos: buscar archivos y comandos del historial al instante en la terminal; construir menús interactivos en scripts de shell.
- **Requisitos:** nivel 1: preparación sencilla; Go, Dockerfile, Gemfile, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install fzf` — fuente: https://github.com/junegunn/fzf/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala fzf, activa la integración de tu shell y pulsa CTRL-T para elegir un archivo. Éxito: El selector filtra miles de archivos al escribir y pega la ruta elegida en la línea de comandos.
- **Combina con:** `ripgrep`, `claude-code` [20/terminal], `codex` [20/terminal]
- **Riesgos y avisos:** Es una herramienta de uso diario: no requiere servidor ni configuración para empezar.

### Pake (`pake`)

- **Repo:** https://github.com/tw93/Pake · GPL-3.0 · nivel 2 · 60/100
- **Qué es:** Herramienta de línea de comandos que empaqueta páginas web como apps de escritorio.
- **Cuándo elegirlo:** Casos: Convertir una página de inicio propia en una app con icono y ventana propios; Empaquetar la carpeta dist de una presentación o herramienta web estática para usarla sin abrir el navegador. Evítalo si no quieres instalar Node.js, Rust y herramientas de compilación, o necesitas que la app acceda a funciones del sistema más allá de mostrar la web.
- **Requisitos:** nivel 2: preparación media; Rust, Dockerfile, package.json; hardware prerequisites; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/tw93/Pake/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea hola.html con un título y un párrafo propios y ejecuta pake ./hola.html --name HolaPake Éxito: En la carpeta aparece un instalador (.dmg, .msi, .deb o AppImage). Instálalo y abre HolaPake: la ventana muestra tu…
- **Combina con:** `slidev` [31/slides], `tailwindcss` [9/estilos], `excalidraw` [9/diseno]

### Requests Cache (`requests-cache`)

- **Repo:** https://github.com/requests-cache/requests-cache · BSD-2-Clause · nivel 2 · 59/100
- **Qué es:** Guarda respuestas de solicitudes Python para reutilizarlas cuando sean válidas y reducir viajes repetidos a un servicio HTTP.
- **Cuándo elegirlo:** Casos: Evitar repetir la descarga de una lista pública durante pruebas.; Medir cuántas veces una tarea de ejemplo vuelve a consultar el servidor.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, docker-compose.yml, pyproject.toml; API de IA: no; Python y una aplicación que use requests; SQLite disponible para un ejemplo local..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://requests-cache.readthedocs.io/
- **Primera prueba propuesta (no ejecutada):** Configura una sesión de caché en un ejemplo con dos lecturas de la misma página de prueba. Éxito: La primera lectura consulta el servidor y la siguiente puede reutilizar la respuesta guardada.
- **Riesgos y avisos:** Expira la caché según los datos y evita almacenar respuestas con credenciales o información privada.

### APScheduler (`apscheduler`)

- **Repo:** https://github.com/agronholm/apscheduler · MIT · nivel 2 · 57/100
- **Qué es:** Programa funciones Python para un horario, un intervalo o una fecha concreta dentro de una aplicación propia.
- **Cuándo elegirlo:** Casos: Actualizar un dato local cada minuto.; Programar un recordatorio interno una vez al día.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, docker-compose.yml, pyproject.toml; API de IA: no; Python y una versión estable 3.x conforme a su guía..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://apscheduler.readthedocs.io/en/3.x/userguide.html
- **Primera prueba propuesta (no ejecutada):** Sigue la guía 3.x y programa una función de prueba que imprima la hora. Éxito: La función se ejecuta en el intervalo elegido y deja una marca visible.
- **Riesgos y avisos:** Haz la primera prueba solo con el almacén en memoria. GHSA-2r6w-vc63-g3hx afecta a los almacenes persistentes de 3.x y no indica parche; las preversiones….

### npkill (`npkill`)

- **Repo:** https://github.com/voidcosmos/npkill · MIT · nivel 1 · 56/100
- **Qué es:** Muestra cuánto espacio ocupan carpetas generadas por herramientas de desarrollo y permite revisarlas antes de eliminar residuos.
- **Cuándo elegirlo:** Casos: Medir el tamaño de node_modules en un proyecto de ejemplo.; Revisar sin borrar los residuos de un directorio de pruebas.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, package.json; API de IA: no; Node.js/npm para la distribución oficial y una carpeta de prueba sin datos importantes..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://npkill.js.org
- **Primera prueba propuesta (no ejecutada):** Usa el modo documentado de simulación dentro de la carpeta de prueba, sin confirmar eliminaciones. Éxito: Ves una lista de candidatos y los archivos del ejemplo siguen presentes.
- **Riesgos y avisos:** Una eliminación real puede ser irreversible. Verifica la ruta y el modo antes de confirmar; no barrer todo el disco para la primera prueba.

### Hishel (`hishel`)

- **Repo:** https://github.com/karpetrosyan/hishel · BSD-3-Clause · nivel 2 · 53/100
- **Qué es:** Añade caché a peticiones HTTP de Python con políticas de expiración y adaptadores de almacenamiento reutilizables.
- **Cuándo elegirlo:** Casos: Evitar pedir varias veces un catálogo público de prueba.; Probar una política de expiración con respuestas de un servidor local.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, package.json, pyproject.toml; API de IA: no; Python y el cliente HTTP soportado por el adaptador elegido..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://hishel.com
- **Primera prueba propuesta (no ejecutada):** Crea dos consultas iguales al ejemplo de prueba usando el adaptador de la guía. Éxito: La segunda consulta se sirve de la caché cuando las reglas lo permiten.
- **Riesgos y avisos:** No compartas una caché que contenga respuestas privadas entre usuarios. El tráfico remoto conserva sus propias cuotas.

### ripgrep (`ripgrep`)

- **Repo:** https://github.com/BurntSushi/ripgrep · Unlicense · nivel 1 · 52/100
- **Qué es:** Herramienta de búsqueda de código abierto con doble licencia MIT o Unlicense, creada por Andrew Gallant (BurntSushi). Muy madura; la usan editores como VS Code y muchos agentes de código.
- **Cuándo elegirlo:** Casos: localizar todas las apariciones de una función en un repositorio grande; buscar texto en miles de archivos de logs o notas en segundos.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install ripgrep` — fuente: https://github.com/BurntSushi/ripgrep/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala ripgrep y ejecuta `rg` con un patrón en un repositorio. Éxito: Obtienes las coincidencias con archivo y línea, sin resultados de carpetas ignoradas.
- **Combina con:** `fzf`, `claude-code` [20/terminal], `opencode` [20/terminal]
- **Riesgos y avisos:** Es la herramienta de búsqueda que asumen muchos agentes de terminal; conviene tenerla instalada.

### PyBreaker (`pybreaker`)

- **Repo:** https://github.com/danielfm/pybreaker · BSD-3-Clause · nivel 2 · 44/100
- **Qué es:** Protege una integración Python con un interruptor que pausa llamadas tras varios fallos y después permite comprobar si volvió el servicio.
- **Cuándo elegirlo:** Casos: Evitar que una integración lenta bloquee todos los trabajos.; Probar cómo se recupera un cliente tras una caída ficticia.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno Python con una función ficticia que pueda fallar..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/danielfm/pybreaker/blob/2b0b965fcfc7705ca9a776c614ea6cb3ec3fe783/README.rst
- **Primera prueba propuesta (no ejecutada):** Configura un ejemplo con una función local que falle repetidamente. Éxito: El interruptor abre y deja de invocar la función hasta el periodo de recuperación.
- **Riesgos y avisos:** Redis es opcional para guardar el estado compartido; no sirve por sí solo para reintentos ni para definir tiempos de espera.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-7-herramientas.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «CLIs y SDKs de desarrollo», lee `docs/alexandria/categoria-7-herramientas.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-7-herramientas.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
