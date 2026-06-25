## Veredicto directo

No son lo mismo. Estás comparando **4 capas distintas** que muchas empresas venden mezcladas:

1. **Modelo**: GPT-5.5, Claude Opus 4.8, Gemini 3.1 Pro, etc.
2. **Agente de código**: Claude Code, Codex, Antigravity, Copilot Agent, Cursor Agent, Devin, OpenCode, Grok Build.
3. **Superficie de uso**: terminal, app de escritorio, VS Code, IDE completo, navegador/cloud.
4. **Ecosistema**: skills, MCP, plugins, hooks, worktrees, navegador, GitHub, Git, terminal, bases de datos, Figma, Slack, etc.

La confusión principal es esta: **usar GPT-5.5 en Copilot Chat no es lo mismo que usar Codex App; usar Opus 4.8 en Copilot no es lo mismo que usar Claude Code; usar Gemini en VS Code no es lo mismo que Antigravity**. El modelo puede ser parecido, pero el rendimiento real cambia por el “arnés” del agente: cómo lee archivos, cómo edita, cómo corre tests, cómo usa terminal, cómo maneja contexto, cómo crea ramas, cómo pide permisos y cómo verifica su propio trabajo.

---

## Corrección importante al 21 de junio de 2026

La opción “**Gemini Code Assist para VS Code con Google AI Ultra**” ya no debe tratarse como una opción principal para consumidor. Google anunció que desde el **18 de junio de 2026** Gemini Code Assist IDE extensions y Gemini CLI dejaron de servir requests para Gemini Code Assist for individuals, Google AI Pro y Google AI Ultra; la migración recomendada es hacia **Antigravity** y **Antigravity CLI**. ([Google for Developers][1])

Esto cambia bastante tu lista: con Google Ultra, lo fuerte ahora es **Antigravity 2.0 / Antigravity IDE / Antigravity CLI**, no la extensión clásica Gemini Code Assist para VS Code.

---

# 1. Mapa mental: desktop vs terminal vs VS Code vs IDE

| Superficie                                                 | Qué es realmente                                                                                                            | Ventaja principal                                                                                | Desventaja principal                                                                        | Cuándo usarla                                                                                         |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Terminal abierta en la carpeta del proyecto**            | El agente trabaja directamente sobre tu repo local, con shell, Git, tests y archivos reales.                                | Máximo control técnico; ideal para refactors, debugging, migraciones, Docker, scripts y pruebas. | Menos visual; más fácil ejecutar comandos peligrosos si no configuras permisos.             | Tu superficie base para trabajo serio de backend, full-stack, scraping, automatización, Docker, APIs. |
| **App de escritorio**                                      | Centro de mando para correr varias sesiones/agentes, revisar diffs, previews, worktrees, browser, terminal y tareas largas. | Mejor para trabajo paralelo y revisión visual.                                                   | Puede abstraer demasiado; necesitas disciplina con ramas/worktrees.                         | Cuando quieres “orquestar” varios agentes como si fueran juniors trabajando en paralelo.              |
| **Extensión de VS Code**                                   | Agente integrado al editor, con archivos abiertos, selección de código, inline diffs y contexto visual.                     | Menor fricción para editar, revisar y preguntar sobre código puntual.                            | Puede ser más limitada para tareas largas, paralelas o multi-repo que una app/CLI dedicada. | Ideal para revisar cambios, editar archivos puntuales, entender errores y usarlo junto al terminal.   |
| **IDE completo tipo Cursor / Antigravity / Devin Desktop** | Entorno construido alrededor de agentes, no solo editor.                                                                    | Une editor, chat, agentes, terminal, navegador, Git y contexto en una experiencia completa.      | Te puede encerrar en su flujo; duplicas costos si ya usas Claude Code/Codex/Copilot.        | Cuando quieres que el IDE sea el centro operativo de programación con IA.                             |
| **Chat web normal**                                        | Modelo conversacional con archivos subidos, conectores o contexto pegado.                                                   | Excelente para arquitectura, explicación, prompts, análisis, investigación y diseño.             | No siempre ve tu repo real ni corre tests locales.                                          | Planeación, documentación, análisis, arquitectura y decisiones antes de ejecutar en agente.           |

---

# 2. Tabla comparativa principal

| Herramienta                     | Mejor superficie                        | Cómo funciona                                                                                                                                                      | Paralelo / worktrees                                                                                                                  | Skills / MCP / plugins                                                                                                                                             | Navegador / investigación                                                                                                                           | Fortaleza real                                                                     | Cuidado principal                                                                                     |
| ------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Claude Code Max**             | Terminal + VS Code + Desktop            | Agente que lee repo, edita archivos, corre comandos e integra herramientas; existe en terminal, IDE, desktop y browser. ([Claude API Docs][2])                     | Muy fuerte. Puede trabajar con worktrees y sesiones paralelas; docs recomiendan worktrees para evitar choques. ([Claude API Docs][3]) | Muy fuerte: skills, subagents, hooks, plugins y MCP. ([Claude API Docs][4])                                                                                        | Fuerte si conectas Chrome/browser, MCP o SDK; en VS Code puede usar `@browser` para probar apps y leer consola. ([Claude API Docs][5])              | Calidad de razonamiento, refactors, debugging complejo, revisión crítica.          | Puede gastar límites rápido; Max es caro y aun así tiene límites.                                     |
| **OpenAI Codex Plus/Pro**       | Codex App + CLI + IDE extension         | Agente de OpenAI para escribir, revisar y shippear código; Codex App maneja threads en paralelo con worktrees, Git y automations. ([Desarrolladores de OpenAI][6]) | Muy fuerte en app/cloud; Windows app permite múltiples agentes, worktrees aislados y diffs revisables. ([OpenAI Help Center][7])      | Fuerte: skills en Codex, plugins, app mappings, MCP y subagents según superficie. ([IT Pro][8])                                                                    | Fuerte en app/cloud; Codex puede leer, editar y correr código, y Codex cloud trabaja en paralelo en entorno cloud. ([Desarrolladores de OpenAI][9]) | Rendimiento top en terminal coding con GPT-5.5; muy buen costo si ya pagas Plus.   | En Plus puedes topar límites; para uso intensivo serio quizá Pro/credits.                             |
| **Google Antigravity Ultra**    | Antigravity 2.0 + Antigravity IDE + CLI | Antigravity 2.0 es centro de mando standalone para agentes locales paralelos, tareas programadas y flujos multiagente. ([Google Codelabs][10])                     | Muy fuerte: enfoque multiagente y central command center.                                                                             | Fuerte: Antigravity se está consolidando como plataforma unificada; Code Assist/Gemini CLI consumidor migran hacia Antigravity. ([Google Cloud Documentation][11]) | Muy fuerte en flujos editor-terminal-browser; Google lo posiciona como plataforma agent-first.                                                      | Buen balance de velocidad, tooling, multimodalidad, navegador y ecosistema Google. | La extensión Gemini Code Assist consumer quedó deprecada; usa Antigravity.                            |
| **GitHub Copilot Pro**          | VS Code / GitHub / PRs                  | Copilot soporta múltiples modelos según plan y cliente; modelo disponible depende de plan y superficie. ([GitHub Docs][12])                                        | Medio-alto: Cloud agent y agent mode, pero menos “fleet manager” que Codex App, Claude Desktop, Cursor o Devin.                       | MCP y agent mode permiten workflows multi-step y conexión a herramientas externas. ([GitHub Docs][13])                                                             | Variable; fuerte dentro de GitHub, PRs, issues y VS Code.                                                                                           | Autocomplete, next edit suggestions, PR review, GitHub flow.                       | No sustituye siempre a Claude Code/Codex nativos; Copilot con Opus/GPT/Gemini usa el arnés de GitHub. |
| **Cursor**                      | IDE completo                            | IDE agent-first con agentes locales/cloud, paralelo, MCP, skills/hooks según plan.                                                                                 | Fuerte: Cursor 3 fue diseñado alrededor de agentes paralelos y cloud agents. ([Product Hunt][14])                                     | Fuerte: Cursor ofrece MCP, skills, hooks y cloud agents en planes pagos. ([Cursor][15])                                                                            | Bueno; integrado al flujo IDE.                                                                                                                      | Muy cómodo para programar todo el día sin salir del IDE.                           | Si ya usas Claude Code + Codex + VS Code, puede ser redundante.                                       |
| **Devin Desktop / ex Windsurf** | IDE/comando multiagente                 | Devin se posiciona como AI software engineer para equipos complejos; Devin Desktop/Windsurf va hacia command center. ([Devin][16])                                 | Fuerte para equipos y cloud agents.                                                                                                   | Interesante por ACP y agentes externos, según evolución de Devin Desktop.                                                                                          | Bueno para flujos end-to-end.                                                                                                                       | Equipos, multi-repo, tareas largas, tickets.                                       | Puede ser caro o excesivo para proyectos personales/pequeños.                                         |
| **OpenCode con API**            | Terminal / desktop / IDE                | Agente open source para terminal, IDE o desktop; permite varios proveedores y sesiones paralelas. ([OpenCode][17])                                                 | Bueno: multi-session y proveedores múltiples.                                                                                         | Flexible: depende de configuración, MCP y proveedor.                                                                                                               | Variable.                                                                                                                                           | Control, costo, portabilidad, evitar lock-in.                                      | Requiere más setup y criterio técnico.                                                                |
| **Grok Build / Grok terminal**  | Terminal                                | xAI lanzó Grok Build como beta temprana para SuperGrok y X Premium Plus; corre desde terminal. ([xAI][18])                                                         | Todavía temprano.                                                                                                                     | Menos maduro públicamente que Claude/Codex/Antigravity/Cursor.                                                                                                     | Variable.                                                                                                                                           | Experimental, potencialmente rápido/barato.                                        | No lo usaría como herramienta principal de producción todavía.                                        |

---

# 3. Anthropic Claude Code Max

## Qué es

Claude Code es un **agente de programación** que puede leer tu codebase, editar archivos, correr comandos e integrarse con tus herramientas. Anthropic lo ofrece en terminal, IDE, desktop app y browser. ([Claude API Docs][2])

La suscripción **Claude Max** te da más uso que Pro; Anthropic muestra opciones de 5x o 20x más uso que Pro en su página de precios. ([Claude][19])

## Claude Code en terminal

Esta es, para mí, la versión más seria para programar.

Cuando abres la terminal de Windows en la carpeta del proyecto, el agente trabaja sobre el repo real. Puede leer estructura, editar archivos, ejecutar tests, correr builds, usar Git, revisar errores de consola y seguir instrucciones persistentes tipo `CLAUDE.md`. Anthropic documenta que Claude Code usa `CLAUDE.md` y memoria automática para cargar instrucciones del proyecto en cada sesión. ([Claude API Docs][20])

**Ventajas:**

* Mejor para proyectos reales, no snippets.
* Ideal para debugging, migraciones, refactors, scripts, Docker, backend, scraping.
* Puedes controlar permisos.
* Se integra bien con Git y worktrees.
* Es más fácil auditar qué cambió.

**Desventajas:**

* Es menos visual.
* Si no usas ramas, puede modificar demasiado.
* Necesitas aprender comandos, permisos, contexto y reglas.

## Claude Code app de escritorio

No la vería como “otro Claude distinto”, sino como **otra superficie** del mismo ecosistema. Su valor está en manejar sesiones, revisar, ver diffs, previews, tareas y posiblemente flujos más visuales. Claude Code también documenta integraciones de desktop, browser, Chrome, computer use, sesiones remotas y superficies múltiples. ([Claude API Docs][20])

**Dónde brilla:**

* Tareas paralelas.
* Revisión visual.
* UI/frontend.
* Supervisar varios agentes.
* Menos fricción que tener 4 terminales abiertas.

## Extensión Claude Code para VS Code

La extensión sirve para usar Claude dentro del editor, con archivos abiertos, diffs y referencias de código. Anthropic documenta la integración de Claude Code en VS Code y la capacidad de conectar Chrome para probar apps, revisar consola y automatizar flujos de navegador sin salir del editor. ([Claude API Docs][5])

**Mi uso recomendado:**

* Terminal para que haga el trabajo fuerte.
* VS Code extension para revisar, preguntar, ajustar y aprobar.
* Desktop cuando quieras correr varias líneas de trabajo al mismo tiempo.

## Skills, MCP, subagents, plugins

Claude Code es probablemente el ecosistema más maduro en **context engineering** y extensibilidad. Tiene:

* **Skills**: instrucciones/procedimientos reutilizables para tareas específicas. ([Claude API Docs][4])
* **MCP**: conecta Claude con herramientas, APIs, bases de datos y sistemas externos. ([Claude API Docs][21])
* **Subagents**: agentes especializados para separar investigación, testing, seguridad, documentación, frontend, backend, etc. ([Claude API Docs][22])
* **Hooks**: comandos o endpoints que se ejecutan en eventos del ciclo de Claude Code. ([Claude API Docs][23])
* **Plugins**: empaquetan skills, agents, hooks y MCP servers. ([Claude API Docs][24])

**Conclusión Claude:** para trabajo complejo, de alta calidad y con criterio, Claude Code Max sigue siendo de las mejores apuestas. Lo usaría como tu “arquitecto/programador senior” principal.

---

# 4. OpenAI Codex Plus / Pro

## Qué es

Codex es el agente de código de OpenAI. OpenAI lo define como un agente que ayuda a escribir, revisar y shippear código; está incluido en planes elegibles de ChatGPT, con límites según plan. ([OpenAI Help Center][25])

La página de Codex Pricing muestra **Plus a 20 USD/mes** con Codex en web, CLI, IDE extension e iOS, acceso a modelos recientes como GPT-5.5, GPT-5.4 y GPT-5.4 mini, y posibilidad de extender uso con créditos. ([Desarrolladores de OpenAI][26])

## Codex App de escritorio Windows

Codex App es un **command center** para trabajar con threads de Codex en paralelo, con worktrees, automations y Git. ([Desarrolladores de OpenAI][6])

OpenAI también indica que la app de Windows permite correr múltiples agentes en paralelo, con worktrees aislados y diffs revisables que pueden editarse, descartarse o convertirse en pull request. ([OpenAI Help Center][7])

**Ventajas:**

* Excelente para trabajo paralelo.
* Muy buena integración con Git.
* Mejor que chat normal para tareas largas.
* GPT-5.5 tiene rendimiento muy fuerte en benchmarks de terminal/coding.
* Plus tiene muy buena relación costo/beneficio.

**Desventajas:**

* Plus puede ser limitado si programas muchas horas.
* Puede ser más “ejecutor” que “crítico” si no le pides plan y revisión.
* Debes cuidar permisos y ramas, igual que con Claude.

## Codex en terminal

Codex CLI corre localmente en tu computadora. El repositorio oficial indica que Codex CLI es un agente de programación local y muestra instalación para Windows vía PowerShell. ([GitHub][27])

**Uso recomendado:**

* Abres terminal en la carpeta del proyecto.
* Le pides primero plan, luego implementación.
* Lo obligas a correr tests.
* Revisas diff.
* Commit.

En rendimiento puro de terminal, Codex con GPT-5.5 está muy fuerte. En Terminal-Bench 2.1, la entrada **Codex CLI + GPT-5.5** aparece con **83.4% ± 2.2**, por encima de Claude Code Opus 4.8 en ese benchmark específico. ([Terminal-Bench][28])

## Extensión Codex para VS Code

La extensión es útil para el flujo normal dentro del editor, pero para trabajo largo preferiría **Codex App o Codex CLI**. La extensión te da contexto local y menor fricción, pero la app/CLI suele ser mejor cuando quieres tareas de varios archivos, tests, ramas y agentes en paralelo.

## Skills, plugins, subagents

OpenAI ya está empujando **Skills en Codex**: paquetes de instrucciones, recursos y scripts opcionales para que Codex ejecute workflows de forma más confiable. ([IT Pro][8])

Además, Codex cloud puede trabajar en paralelo en entorno cloud, lo cual lo separa de un simple chat de programación. ([Desarrolladores de OpenAI][9])

**Conclusión Codex:** si ya pagas ChatGPT Plus, Codex es probablemente el mejor “no-brainer” costo/beneficio. Para trabajo intensivo, Codex App + CLI es una combinación muy potente.

---

# 5. Google Gemini Ultra / Antigravity

## Qué cambió

Antes tenía sentido pensar en:

* Gemini Code Assist VS Code.
* Gemini CLI.
* Antigravity IDE.

Pero Google está consolidando en **Antigravity**. La documentación de deprecación indica que Gemini Code Assist IDE extensions y Gemini CLI dejaron de servir requests para individuos, Google AI Pro y Google AI Ultra desde el 18 de junio de 2026. ([Google for Developers][1])

Google también dice en release notes que están unificando herramientas en una plataforma multiagente llamada Antigravity, con Antigravity CLI disponible. ([Google Cloud Documentation][11])

## Antigravity 2.0 app de escritorio

Antigravity 2.0 es el centro de mando. Google lo describe como una app standalone para macOS, Linux y Windows que sirve para manejar múltiples agentes locales en paralelo, tareas programadas y más. ([Google Codelabs][10])

**Ventajas:**

* Enfoque nativo multiagente.
* Buen puente entre editor, terminal y navegador.
* Fuerte en flujos visuales/multimodales.
* Muy interesante si ya pagas Google AI Ultra.
* Google AI Ultra ofrece cuotas 5x o 20x en Gemini y Antigravity frente a Pro, según plan. ([Soporte de Google][29])

## Antigravity IDE

El IDE es la experiencia más cercana a Cursor/Devin/Windsurf: editor + agentes + navegador + terminal + contexto. Es más cómodo si quieres un entorno completo, no solo un CLI.

## Antigravity en terminal

La CLI de Antigravity es el reemplazo lógico de Gemini CLI para usuarios consumidor. El matiz importante: Google dice que la transición a Antigravity/CLI es parte de la unificación; no trates Gemini CLI clásico como herramienta estable de largo plazo para Ultra consumer. ([Google Cloud Documentation][11])

## Benchmarks Gemini

Google reporta que **Gemini 3.5 Flash** logra **76.2% en Terminal-Bench 2.1** y **83.6% en MCP Atlas**, superando a Gemini 3.1 Pro en benchmarks agentic/coding según su blog. ([blog.google][30])

En Terminal-Bench 2.1, el leaderboard muestra **Gemini CLI + Gemini 3.1 Pro** con **70.7% ± 2.9** y **Terminus 2 + Gemini 3.1 Pro** con **70.3% ± 2.9**. ([Terminal-Bench][28])

**Conclusión Google:** Antigravity es serio y está creciendo rápido. Pero hoy no lo pondría como tu única herramienta principal si tu prioridad es máxima confiabilidad en repos complejos. Sí lo usaría si quieres un entorno multiagente con fuerte integración navegador/multimodal/Google.

---

# 6. GitHub Copilot Pro con modelos GPT-5.5, Opus 4.8 o Gemini 3.1 Pro

## Qué es realmente

Copilot no es solo “un modelo”. Es el arnés de GitHub dentro de VS Code, GitHub.com, PRs, issues y su propio agent mode. GitHub documenta que Copilot soporta múltiples modelos y que la disponibilidad depende del plan y del cliente donde lo uses. ([GitHub Docs][12])

La documentación de modelos de GitHub incluye modelos como GPT-5.5, variantes Codex, Claude Opus/Sonnet y Gemini, según plan/superficie. ([GitHub Docs][31])

## Dónde brilla Copilot

Copilot Pro es muy bueno para:

* Autocomplete.
* Next edit suggestions.
* Chat dentro de VS Code.
* Explicar errores rápidos.
* PR review.
* GitHub Issues / PRs / repo workflow.
* Cambios medianos dentro del IDE.

La página de planes de GitHub Copilot Pro menciona completions ilimitadas, next edit suggestions, acceso a Cloud agent, code review, selección de modelo y créditos mensuales. ([GitHub][32])

## Dónde no lo confundiría

No asumiría que:

* “Copilot con GPT-5.5” = Codex App.
* “Copilot con Opus 4.8” = Claude Code Max.
* “Copilot con Gemini” = Antigravity.

El modelo puede ser similar, pero el agente no es el mismo. Cambian permisos, herramientas, contexto, memoria, flujo de Git, uso de terminal, worktrees y autonomía.

**Conclusión Copilot:** yo lo conservaría como herramienta diaria dentro de VS Code, pero no lo usaría como reemplazo total de Claude Code o Codex si quieres programación agéntica pesada.

---

# 7. Cursor, Devin/Windsurf, OpenCode, Grok Build

## Cursor

Cursor 3 se posiciona como un workspace agent-first con agentes locales/cloud y ejecución paralela. La información pública de Cursor 3 destaca agentes en una sola barra lateral, agentes locales/cloud y ejecución desde desktop, mobile, web, Slack, GitHub y Linear. ([Product Hunt][14])

**Cuándo vale la pena:**

* Quieres vivir dentro de un IDE agent-first.
* Prefieres una experiencia pulida a configurar CLIs.
* Quieres agentes cloud y locales desde un solo lugar.
* No quieres pensar tanto en terminal.

**Cuándo no:**

* Ya usas VS Code + Claude Code + Codex App.
* Quieres evitar otro pago.
* Prefieres control total por terminal.

## Devin Desktop / ex Windsurf

Devin se vende como AI software engineer para equipos complejos y proyectos multi-repo. ([Devin][16])

Este tipo de herramienta tiene sentido cuando tienes:

* Tickets definidos.
* Repos grandes.
* Flujos de PR.
* Equipos.
* Necesidad de delegar tareas largas.
* Mucha coordinación.

Para tu caso, si estás construyendo herramientas PropTech, scraping, automatizaciones y productos internos, Devin puede ser interesante, pero no lo metería antes de dominar Claude/Codex.

## OpenCode con API

OpenCode es muy atractivo si quieres independencia. Se define como un agente open source que ayuda a escribir código en terminal, IDE o desktop, con LSP, multi-session y soporte de cuentas/proveedores como GitHub Copilot y ChatGPT Plus/Pro. ([OpenCode][17])

**Ventaja:** control, multi-proveedor, menos lock-in.

**Desventaja:** más configuración, más responsabilidad técnica, menos “producto terminado” que Claude/Codex/Cursor.

## Grok Build / Grok terminal

xAI lanzó Grok Build como beta temprana para SuperGrok y X Premium Plus: un agente/CLI de código para ingeniería profesional y tareas complejas desde terminal. ([xAI][18])

Lo pondría en categoría **experimental**. Úsalo para pruebas, no como columna vertebral de producción todavía.

---

# 8. Benchmarks: lectura honesta

Primero, advertencia: los benchmarks de coding son útiles, pero no equivalen directamente a “esta app es mejor”. Miden combinaciones de **modelo + agente + scaffold + herramientas + permisos + tiempo + tests**. OpenAI incluso dejó de recomendar SWE-bench Verified para medir frontier coding porque lo considera contaminado y recomienda SWE-bench Pro. ([OpenAI][33])

SWE-Bench Pro fue diseñado para tareas más realistas, largas y empresariales; el paper lo describe como 1,865 problemas de 41 repos activos y tareas que pueden requerir horas o días a un ingeniero profesional. ([arXiv][34])

## Tabla de rendimiento relevante

| Modelo / agente                   |             Benchmark | Resultado reportado | Lectura práctica                                                                                                                |
| --------------------------------- | --------------------: | ------------------: | ------------------------------------------------------------------------------------------------------------------------------- |
| **Codex CLI + GPT-5.5**           |    Terminal-Bench 2.1 |     **83.4% ± 2.2** | Muy fuerte para tareas de terminal, shell, repo y ejecución local. ([Terminal-Bench][28])                                       |
| **Claude Code + Claude Opus 4.8** |    Terminal-Bench 2.1 |     **78.9% ± 2.5** | Muy fuerte; quizá menos alto que Codex CLI en este benchmark, pero excelente en razonamiento y revisión. ([Terminal-Bench][28]) |
| **Terminus 2 + GPT-5.5**          |    Terminal-Bench 2.1 |     **78.2% ± 2.4** | GPT-5.5 es fuerte incluso fuera del arnés Codex CLI. ([Terminal-Bench][28])                                                     |
| **Gemini CLI + Gemini 3.1 Pro**   |    Terminal-Bench 2.1 |     **70.7% ± 2.9** | Sólido, pero debajo de Codex/Claude Code en este leaderboard. ([Terminal-Bench][28])                                            |
| **GPT-5.5**                       |    Terminal-Bench 2.0 |           **82.7%** | OpenAI lo presenta como su modelo agentic coding más potente hasta ese lanzamiento. ([OpenAI][35])                              |
| **GPT-5.5**                       | SWE-Bench Pro público |           **58.6%** | Muy fuerte, aunque OpenAI muestra Claude Opus 4.7 arriba en esa tabla específica. ([OpenAI][35])                                |
| **Claude Opus 4.7**               | SWE-Bench Pro público |           **64.3%** | En la tabla de OpenAI aparece arriba de GPT-5.5 en SWE-Bench Pro público. ([OpenAI][35])                                        |
| **Gemini 3.5 Flash**              |    Terminal-Bench 2.1 |           **76.2%** | Google lo reporta como su modelo Gemini más fuerte en agentic/coding frente a Gemini 3.1 Pro. ([blog.google][30])               |
| **Gemini 3.5 Flash**              |             MCP Atlas |           **83.6%** | Muy fuerte en uso de herramientas/MCP según Google. ([blog.google][30])                                                         |

## Lectura real de benchmarks

* **Para terminal y ejecución local:** Codex CLI + GPT-5.5 aparece muy fuerte.
* **Para refactor complejo, criterio, revisión y “no me hagas basura”:** Claude Code con Opus sigue siendo de primera línea.
* **Para uso de herramientas/MCP/multimodal/browser:** Gemini/Antigravity puede volverse muy competitivo, especialmente con Gemini 3.5 Flash.
* **Para VS Code diario:** Copilot gana por fricción baja, no necesariamente por ser el agente más autónomo.
* **Para IDE agent-first:** Cursor/Devin compiten por experiencia integrada, no solo por modelo.

---

# 9. Recomendación práctica para ti

## Stack racional, sin volverte loco

Para tu perfil —Windows, Python, scraping, automatizaciones, apps web, IA local, PropTech, documentos, CRMs, dashboards— yo usaría esto:

### Opción principal recomendada

| Rol                                  | Herramienta                              | Por qué                                                                                                                             |
| ------------------------------------ | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Agente senior principal**          | **Claude Code Max en terminal**          | Mejor para arquitectura, refactors, debugging difícil, revisión crítica y mantener calidad.                                         |
| **Agente ejecutor/paralelo**         | **Codex App + Codex CLI con Plus o Pro** | Excelente para correr tareas en paralelo, implementar features, arreglar bugs y aprovechar GPT-5.5.                                 |
| **Editor diario**                    | **VS Code + Copilot Pro**                | Autocomplete, next edit, chat rápido, PRs, menor fricción.                                                                          |
| **Exploración Google/multimodal**    | **Antigravity 2.0 si ya pagas Ultra**    | Útil para agentes paralelos, navegador, flujos visuales y ecosistema Google. No uses Gemini Code Assist consumer clásico como base. |
| **Open source / API / experimentos** | **OpenCode**                             | Para controlar proveedor, costos y evitar lock-in.                                                                                  |

## Lo que NO haría

No pagaría al mismo tiempo por:

* Claude Max.
* ChatGPT Pro.
* Google Ultra.
* Copilot Pro+.
* Cursor.
* Devin.
* Grok.
* APIs varias.

Eso te va a generar ruido, no productividad.

Primero domina **2 herramientas fuertes**:

1. **Claude Code** para calidad.
2. **Codex** para ejecución/paralelo.

Luego añade **Copilot Pro** si realmente trabajas todo el día en VS Code.

---

# 10. Flujo de trabajo recomendado

## Para una tarea seria

1. **Plan en chat o Claude/Codex sin editar archivos**

   * “Analiza el repo y dame plan. No modifiques nada.”
2. **Crear rama o worktree**

   * `git checkout -b feature/x`
   * o worktree separado.
3. **Pedir implementación mínima**

   * “Implementa solo lo necesario. No refactorices fuera del alcance.”
4. **Obligar tests**

   * “Corre tests/lint/build y corrige.”
5. **Revisión por otro agente**

   * Codex implementa, Claude revisa.
   * O Claude implementa, Codex revisa.
6. **Diff humano**

   * Revisas cambios críticos.
7. **Commit**

   * Mensaje claro.
8. **Documentar aprendizaje**

   * Actualizar `AGENTS.md`, `CLAUDE.md` o reglas del repo.

## Regla clave

Nunca le digas a un agente:

> “Arregla todo el proyecto.”

Mejor:

> “Encuentra la causa raíz de este error. Propón 2 soluciones. Elige la menos invasiva. Implementa solo esa. Corre tests. Resume cambios y riesgos.”

---

# 11. Mi ranking por caso de uso

| Caso de uso                            | Mejor opción                                                                      |
| -------------------------------------- | --------------------------------------------------------------------------------- |
| Refactor grande de backend             | **Claude Code terminal**                                                          |
| Implementar feature completa con tests | **Codex App / Codex CLI**                                                         |
| Arreglar bugs complejos                | **Claude Code + Codex en revisión cruzada**                                       |
| Autocomplete diario                    | **GitHub Copilot Pro**                                                            |
| Frontend visual con navegador          | **Claude Code con Chrome / Antigravity / Cursor**                                 |
| Multiagente paralelo                   | **Codex App, Claude Desktop, Antigravity 2.0, Cursor 3 o Devin**                  |
| Control de costos/API                  | **OpenCode**                                                                      |
| Experimentación nueva                  | **Grok Build**                                                                    |
| Investigación profunda web             | **ChatGPT / Claude / Gemini web**, luego pasar especificación al agente de código |
| Proyecto empresarial multi-repo        | **Devin / Cursor / Codex cloud**, según presupuesto                               |

---

# 12. Decisión final

Para no volverte loco:

## Quédate con este esquema

**Base de programación seria:**

* **VS Code**
* **Git**
* **Claude Code en terminal**
* **Codex App/CLI**
* **Copilot Pro solo para autocomplete y edición rápida**

**Opcional:**

* **Antigravity** si ya pagas Google Ultra.
* **OpenCode** si quieres jugar con APIs/modelos/local.
* **Cursor o Devin**, pero solo si decides que tu IDE completo será agent-first.

## Mi elección concreta para ti

Si tuviera que elegir por prioridad:

1. **Claude Code Max** como herramienta premium de razonamiento y calidad.
2. **Codex Plus/Pro** como herramienta de ejecución, paralelo y costo/beneficio.
3. **Copilot Pro** para VS Code diario.
4. **Antigravity Ultra** solo si el ecosistema Google/multimodal/browser te da valor adicional.
5. **OpenCode** como laboratorio técnico.
6. **Grok Build** como experimento, no base.

La combinación más equilibrada sería:

> **Claude Code Max + Codex Plus + VS Code con Copilot Pro**

Y la regla operativa sería:

> **Claude piensa/revisa; Codex ejecuta/paraleliza; Copilot acelera edición diaria; tú decides arquitectura, alcance y aprobación final.**
