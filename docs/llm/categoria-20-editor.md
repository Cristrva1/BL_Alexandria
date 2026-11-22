# Alexandría para agentes · Editores y extensiones de código

Categoría 20 «Programar con agentes de código» › subcategoría `editor`. 5 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=20&sub=editor · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `cline` | Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con… | 1 Básico | 66 | Apache-2.0 (OSI permisiva) | recomendado |
| `zed` | Editor de código de alto rendimiento y multijugador, de los creadores de Atom y… | 1 Básico | 64 | GPL-3.0 (Apache-2.0 en componentes marcados) (OSI permisiva) | sin grupo |
| `openidea` | Entorno de desarrollo con editor, depurador, Git y herramientas para trabajar… | 1 Básico | 63 | Apache-2.0 (OSI permisiva) | sin grupo |
| `kilocode` | Agente de código abierto para VS Code, JetBrains y la terminal, con más de 500… | 2 Intermedio | 60 | MIT (OSI permisiva) | alternativa |
| `opencursor` | Extensión abierta de VS Code con chat de agente, búsqueda semántica… | 2 Intermedio | 48 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Cline (`cline`)

- **Repo:** https://github.com/cline/cline · Apache-2.0 · nivel 1 · 66/100 · recomendado en «Agentes de código en el editor»
- **Qué es:** Cline, agente de programación open source para IDE, terminal y escritorio, de Cline Bot Inc. Licencia Apache-2.0. Es muy activo (~72k estrellas, v4.1.26).
- **Cuándo elegirlo:** Casos: Explicar un error de código; Comparar una propuesta antes de editar.
- **Requisitos:** nivel 1: preparación sencilla; Node para CLI o editor compatible; proveedor o Ollama; proyecto de prueba; hardware prerequisites; API de IA: opcional; Node para CLI o editor compatible; proveedor o Ollama; proyecto de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npm i -g cline` — fuente: https://github.com/cline/cline/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Usa Plan mode para pedir un diagnóstico de un archivo antes de pasar a Act Éxito: Puedes revisar el plan y los permisos solicitados
- **Combina con:** `ollama` [8/motores], `context7` [5/servidores], `playwright-mcp` [5/servidores], `omniroute` [23/serving], `awesome-mcp-clients` [5/directorios]
- **Alternativas:** `kilocode`, `aider`
- **Riesgos y avisos:** Alternativas (elige una): aider. Cline es su propio agente; soportar modelos Claude u OpenAI no equivale a usar una suscripción de Claude Code o Codex.

### Zed (`zed`)

- **Repo:** https://github.com/zed-industries/zed · GPL-3.0 (Apache-2.0 en componentes marcados) · nivel 1 · 64/100
- **Qué es:** Editor de código abierto de Zed Industries. El código es principalmente GPL-3.0-or-later con componentes Apache-2.0 donde se indica. Muy activo; ofrece planes de pago para su IA alojada.
- **Cuándo elegirlo:** Casos: editar código con un editor rápido y colaborar en tiempo real; usar Claude Code, Gemini CLI o Codex dentro del editor por ACP.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install --cask zed` — fuente: https://github.com/zed-industries/zed/blob/main/docs/src/installation.md
- **Primera prueba propuesta (no ejecutada):** Descarga Zed para tu sistema, abre un proyecto y configura un agente externo como Gemini CLI. Éxito: El agente responde en el panel de Zed y propone cambios en el proyecto.
- **Combina con:** `claude-code` [20/terminal], `gemini-cli` [20/terminal], `codex` [20/terminal], `qwen-code` [20/terminal]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. No hay otro editor completo en el catálogo; cline y kilocode son extensiones para VS Code.

### openidea (`openidea`)

- **Repo:** https://github.com/l0ng-ai/openidea · Apache-2.0 · nivel 1 · 63/100
- **Qué es:** OpenIDEA, IDE nativo con núcleo en Rust que reproduce la forma de trabajar de IntelliJ IDEA, de l0ng-ai. Licencia Apache-2.0; no está afiliado a JetBrains. Es muy reciente (creado en octubre de 2026) y ya tiene ~9k estrellas.
- **Cuándo elegirlo:** Casos: Explorar código con atajos tipo IntelliJ; Probar un editor nativo con plugins.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador para tu sistema; proyecto pequeño; hardware prerequisites; API de IA: no; Instalador para tu sistema; proyecto pequeño.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/l0ng-ai/openidea/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre un proyecto de ejemplo y usa buscar en todo para localizar una función Éxito: Puedes navegar al archivo y reconocer sus referencias
- **Combina con:** `opencode` [20/terminal], `claude-code` [20/terminal], `aider` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Proyecto muy joven: conviene vigilar su madurez. Es un IDE independiente en Rust y la API de plugins está en preview; los benchmarks del autor no son una garantía de igual rendimiento en tu equipo.

### Kilo Code (`kilocode`)

- **Repo:** https://github.com/Kilo-Org/kilocode · MIT · nivel 2 · 60/100 · alternativa en «Agentes de código en el editor»
- **Qué es:** Agente de código de código abierto (MIT) de Kilo Code, Inc., con servicio en la nube y pasarela de modelos de pago por uso. Muy activo. La extensión nació a partir de Roo Code y Cline; según el README, la CLI actual es un fork de OpenCode.
- **Cuándo elegirlo:** Casos: delegar en el editor una tarea de refactorización con revisión de cambios; usar el mismo agente en VS Code y en la terminal con distintos modelos. Evítalo si necesitas una herramienta estable y auditada para datos sensibles.
- **Requisitos:** nivel 2: preparación sencilla, requiere clave de API; TypeScript, package.json; API de IA: sí.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install -g @kilocode/cli` — fuente: https://github.com/Kilo-Org/kilocode/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala la extensión desde el VS Code Marketplace, conecta un modelo y pídele que explique un archivo de tu proyecto. Éxito: El agente responde y propone cambios que puedes aceptar o rechazar.
- **Combina con:** `context7` [5/servidores], `playwright-mcp` [5/servidores], `github-mcp-server` [5/servidores]
- **Alternativas:** `cline`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): cline. Revisa los cambios antes de aceptarlos y controla el gasto en la pasarela.

### OpenCursor (`opencursor`)

- **Repo:** https://github.com/PawanOsman/OpenCursor · MIT · nivel 2 · 48/100
- **Qué es:** OpenCursor, extensión open source de VS Code con agente de programación, de @PawanOsman. Licencia MIT. Tiene ~6k estrellas (0.2.1).
- **Cuándo elegirlo:** Casos: Trabajar con un agente dentro de VS Code; Comparar inferencia local con cuenta remota.
- **Requisitos:** nivel 2: preparación media; VS Code; extensión o VSIX; cuenta, API u Ollama/llama.cpp; proyecto de prueba; hardware prerequisites; API de IA: opcional; VS Code; extensión o VSIX; cuenta, API u Ollama/llama.cpp; proyecto de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/PawanOsman/OpenCursor.git` — fuente: https://github.com/PawanOsman/OpenCursor/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala la extensión y usa un modelo local o cuenta para explicar un archivo antes de permitir comandos Éxito: Puedes revisar contexto enviado, modelo y diff propuesto
- **Combina con:** `ollama` [8/motores], `llama-cpp` [8/motores], `context7` [5/servidores]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. No está relacionado con Cursor (producto comercial) pese al nombre. Es una extensión independiente; las rutas de cuenta no la convierten en producto oficial de esos proveedores y los servicios de embeddings pueden ser distintos….

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-20-editor.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Editores y extensiones de código», lee `docs/alexandria/categoria-20-editor.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-20-editor.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
