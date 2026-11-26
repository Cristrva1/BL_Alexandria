# Alexandría para agentes · Agentes para issues y tareas de ingeniería

Categoría 20 «Programar con agentes de código» › subcategoría `ingenieria`. 3 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=20&sub=ingenieria · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `openhands` | Agent Canvas: centro de sesiones autoalojado para OpenHands, Claude Code, Codex… | 2 Intermedio | 74 | MIT (OSI permisiva) | recomendado |
| `open-swe` | Robin, fábrica de cambios sobre Deep Agents que despliega con Managed Deep… | 2 Intermedio | 61 | MIT (OSI permisiva) | alternativa |
| `mini-swe-agent` | Agente de ingeniería de software mínimo (unas 100 líneas) del equipo de… | 1 Básico | 52 | MIT (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### OpenHands (`openhands`)

- **Repo:** https://github.com/OpenHands/OpenHands · MIT · nivel 2 · 74/100 · recomendado en «Agentes que resuelven issues de software»
- **Qué es:** OpenHands, cuyo repo principal es ahora Agent Canvas, centro de control autoalojado para agentes de programación y automatizaciones. Licencia MIT. Es muy activo (~94k estrellas, v1.40.0).
- **Cuándo elegirlo:** Casos: Centralizar sesiones de agentes; Preparar una automatización de ingeniería.
- **Requisitos:** nivel 2: preparación media; Node 24 o posterior; uv; repositorio de prueba; agente autenticado; Docker según backend; hardware prerequisites; API de IA: opcional; Node 24 o posterior; uv; repositorio de prueba; agente autenticado; Docker según backend.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/OpenHands/OpenHands/blob/main/README.md

  ```sh
  npm install -g @openhands/agent-canvas
  agent-canvas
  ```
- **Primera prueba propuesta (no ejecutada):** Arranca Agent Canvas y crea una sesión que solo examine un proyecto de ejemplo Éxito: Puedes reconocer agente, backend y permisos de la sesión
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `sandbox` [22/infra], `ecc` [2/metodologia], `swe-bench` [7/calidad]
- **Alternativas:** `open-swe`, `mini-swe-agent`
- **Riesgos y avisos:** Alternativas (elige una): open-swe. El README actual presenta Agent Canvas con OpenHands, Claude Code, Codex y agentes ACP; la receta de Docker limita el puerto al equipo local.

### Open SWE (`open-swe`)

- **Repo:** https://github.com/langchain-ai/open-swe · MIT · nivel 2 · 61/100 · alternativa en «Agentes que resuelven issues de software»
- **Qué es:** Robin (repo open-swe), «fábrica de software» open source de LangChain construida sobre Deep Agents. El código propio es MIT y `vendor/` no está cubierto.
- **Cuándo elegirlo:** Casos: Diseñar una fábrica interna de cambios; Estudiar un agente asíncrono con revisión.
- **Requisitos:** nivel 2: preparación media, requiere clave de API; Managed Deep Agents para despliegue actual; repositorio y permisos de prueba; servicios integrados; hardware prerequisites; API de IA: sí; Managed Deep Agents para despliegue actual; repositorio y permisos de prueba; servicios integrados.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install --cask langchain-ai/tap/open-swe-desktop` — fuente: https://github.com/langchain-ai/open-swe/blob/main/docs/INSTALLATION.md
- **Primera prueba propuesta (no ejecutada):** Lee el flujo de issue a PR y prueba un issue ficticio sin habilitar entregas automáticas Éxito: Puedes inspeccionar planificación, sandbox y validación por separado
- **Combina con:** `deepagents` [3/py], `langgraph` [3/py], `e2b` [22/infra]
- **Alternativas:** `openhands`, `mini-swe-agent`
- **Riesgos y avisos:** Alternativas (elige una): openhands. Fuerte dependencia de servicios de LangSmith. El proyecto se presenta actualmente como Robin construido sobre Deep Agents; MIT cubre su código y no concede acceso a todos los servicios.

### mini-swe-agent (`mini-swe-agent`)

- **Repo:** https://github.com/SWE-agent/mini-swe-agent · MIT · nivel 1 · 52/100 · alternativa en «Agentes que resuelven issues de software»
- **Qué es:** Agente de código abierto (MIT) de los autores de SWE-bench y SWE-agent (Princeton y Stanford), que lo presentan como sucesor del SWE-agent original. Activo.
- **Cuándo elegirlo:** Casos: resolver issues de un repositorio de forma autónoma en un contenedor; usar un agente simple como base para investigación o benchmarks. Evítalo si necesitas una herramienta estable y auditada para datos sensibles.
- **Requisitos:** nivel 1: preparación sencilla; Python, pyproject.toml; hardware model_dependent; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install uv && uvx mini-swe-agent` — fuente: https://github.com/SWE-agent/mini-swe-agent/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta `pip install uv && uvx mini-swe-agent` con una clave de modelo y pídele una tarea pequeña en un repositorio de prueba. Éxito: El agente ejecuta comandos bash y propone el cambio.
- **Combina con:** `litellm` [23/serving], `ollama` [8/motores], `vllm` [23/serving]
- **Alternativas:** `openhands`, `open-swe`
- **Riesgos y avisos:** Alternativas (elige una): openhands. Ejecuta el agente en un contenedor para aislar los comandos.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-20-ingenieria.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Agentes para issues y tareas de ingeniería», lee `docs/alexandria/categoria-20-ingenieria.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-20-ingenieria.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
