# Alexandría para agentes · Agentes de research autónomo

Categoría 21 «Asistentes e investigación con agentes» › subcategoría `research`. 5 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=21&sub=research · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `deer-flow` | Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con… | 2 Intermedio | 68 | MIT (OSI permisiva) | sin grupo |
| `gpt-researcher` | Agente autónomo que investiga en línea y consolida reportes citados y… | 2 Intermedio | 61 | Apache-2.0 (OSI permisiva) | recomendado |
| `storm` | Sistema de Stanford que investiga un tema en la web y escribe un informe largo… | 2 Intermedio | 60 | MIT (OSI permisiva) | alternativa |
| `local-deep-research` | Agente de investigación que combina buscadores, documentos y modelos locales o… | 2 Intermedio | 56 | MIT (OSI permisiva) | alternativa |
| `autoresearch` | Experimento para iterar sobre entrenamiento de nanochat con un agente de código… | 3 Avanzado | 45 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### deer-flow (`deer-flow`)

- **Repo:** https://github.com/bytedance/deer-flow · MIT · nivel 2 · 68/100
- **Qué es:** DeerFlow 2.0, «super agent harness» open source de ByteDance, construido sobre LangGraph y LangChain. Licencia MIT. Es una reescritura completa sin código compartido con la v1 (el framework Deep Research sigue en la rama 1.x), tiene ~85k…
- **Cuándo elegirlo:** Casos: Investigar un tema con fuentes; Coordinar una generación de informe.
- **Requisitos:** nivel 2: preparación media; Docker o entorno de desarrollo; modelo configurado; carpeta de prueba; hardware prerequisites; API de IA: depends; Docker o entorno de desarrollo; modelo configurado; carpeta de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/bytedance/deer-flow/blob/main/README.md

  ```bash
  git clone https://github.com/bytedance/deer-flow.git
  cd deer-flow
  make setup          # interactive wizard: writes config.yaml and .env (about 2 minutes)
  ```
- **Primera prueba propuesta (no ejecutada):** Completa setup y solicita un informe corto con fuentes antes de habilitar herramientas de escritura Éxito: Puedes contrastar las referencias y revisar las acciones del agente
- **Combina con:** `langgraph` [3/py], `firecrawl` [4/crawlers], `searxng` [4/busqueda], `sandbox` [22/infra]
- **Riesgos y avisos:** Sin alternativas declaradas; se solapa con gpt-researcher en el modo investigación (solo anotado). Documenta el skill claude-to-deerflow para controlar una instancia activa; pedir a Codex que instale el proyecto no demuestra una integración runtime con Codex.

### gpt-researcher (`gpt-researcher`)

- **Repo:** https://github.com/assafelovic/gpt-researcher · Apache-2.0 · nivel 2 · 61/100 · recomendado en «Agentes de investigación autónoma»
- **Qué es:** GPT Researcher, agente open source de investigación profunda en web y documentos locales, de @assafelovic. Licencia Apache-2.0. Es maduro (desde 2023, ~31k estrellas, v3.8.0).
- **Cuándo elegirlo:** Casos: Preparar un informe de mercado con fuentes; Investigar documentación técnica.
- **Requisitos:** nivel 2: preparación media; Python 3.11+; proveedor y buscador; cliente MCP solo si eliges esa ruta; hardware prerequisites; API de IA: opcional; Python 3.11+; proveedor y buscador; cliente MCP solo si eliges esa ruta.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install gpt-researcher` — fuente: https://github.com/assafelovic/gpt-researcher/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Haz una pregunta acotada y verifica dos fuentes antes de reutilizar el informe Éxito: Puedes recuperar contexto y enlaces que respaldan conclusiones
- **Combina con:** `claude-code` [20/terminal], `firecrawl` [4/crawlers], `ollama` [8/motores], `searxng` [4/busqueda]
- **Alternativas:** `storm`, `local-deep-research`, `vane`
- **Riesgos y avisos:** Alternativas (elige una): storm, vane, local-deep-research. Se quita browser-use de las combinaciones (no hay integración documentada). El MCP está ahora en gptr-mcp, proyecto compañero con stdio y transportes de red; el skill y el servidor de investigación requieren configuración propia.

### STORM (`storm`)

- **Repo:** https://github.com/stanford-oval/storm · MIT · nivel 2 · 60/100 · alternativa en «Agentes de investigación autónoma»
- **Qué es:** STORM y Co-STORM, sistemas de investigación de Stanford OVAL (artículos en NAACL y EMNLP 2024) que escriben informes tipo Wikipedia con citas. Licencia MIT. Tiene ~32k estrellas, pero sin cambios desde septiembre de 2025.
- **Cuándo elegirlo:** Casos: Preparar una revisión de un tema; Comparar perspectivas antes de escribir.
- **Requisitos:** nivel 2: preparación media, requiere clave de API; Conda y Python 3.11; modelo; credenciales del buscador configurado; hardware prerequisites; API de IA: sí; Conda y Python 3.11; modelo; credenciales del buscador configurado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/stanford-oval/storm/blob/main/README.md

  ```shell
  git clone https://github.com/stanford-oval/storm.git
      cd storm

  conda create -n storm python=3.11
     conda activate storm
     pip install -r requirements.txt
  ```
- **Primera prueba propuesta (no ejecutada):** Investiga un tema acotado y comprueba manualmente dos citas del borrador Éxito: Puedes rastrear las afirmaciones a sus fuentes
- **Combina con:** `litellm` [23/serving], `searxng` [4/busqueda], `qdrant` [6/vectores]
- **Alternativas:** `gpt-researcher`, `local-deep-research`
- **Riesgos y avisos:** Alternativas (elige una): gpt-researcher. Actividad baja. Las citas y el texto generado requieren revisión; una interfaz de modelo configurable no confirma una ruta local lista para usar.

### local-deep-research (`local-deep-research`)

- **Repo:** https://github.com/LearningCircuit/local-deep-research · MIT · nivel 2 · 56/100 · alternativa en «Agentes de investigación autónoma»
- **Qué es:** Local Deep Research, asistente de investigación agéntica que puede ejecutarse totalmente en local, de LearningCircuit. Licencia MIT. Tiene ~9.6k estrellas (v2.0.1); según su propio README, alcanza ~95% en SimpleQA con Qwen3.6-27B en una…
- **Cuándo elegirlo:** Casos: Consultar documentos privados; Preparar una revisión bibliográfica.
- **Requisitos:** nivel 2: preparación media; Modelo local o remoto; buscador; Python o Docker; equipo adecuado al modelo; hardware prerequisites; API de IA: opcional; Modelo local o remoto; buscador; Python o Docker; equipo adecuado al modelo.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install local-deep-research` — fuente: https://github.com/LearningCircuit/local-deep-research/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Investiga una pregunta pequeña con Ollama y SearXNG y abre las fuentes citadas Éxito: Puedes identificar buscador, modelo y evidencia utilizada
- **Combina con:** `ollama` [8/motores], `searxng` [4/busqueda], `llama-cpp` [8/motores]
- **Alternativas:** `gpt-researcher`, `storm`
- **Riesgos y avisos:** Alternativa (elige una): gpt-researcher. El MCP documentado usa stdio para uso local y carece de autenticación y límite de peticiones; el benchmark del autor no garantiza exactitud en cualquier tema.

### autoresearch (`autoresearch`)

- **Repo:** https://github.com/karpathy/autoresearch · — · nivel 3 · 45/100
- **Qué es:** autoresearch, experimento de @karpathy en el que un agente investiga de forma autónoma sobre el entrenamiento de nanochat con una sola GPU. Licencia MIT según el README, pero sin archivo LICENSE (GitHub no detecta licencia).
- **Cuándo elegirlo:** Casos: Estudiar optimización de entrenamiento; Aprender a registrar experimentos reproducibles.
- **Requisitos:** nivel 3: preparación media, necesita GPU; GPU NVIDIA; Python 3.10+; uv; agente y presupuesto de cómputo; hardware prerequisites; API de IA: no; GPU NVIDIA; Python 3.10+; uv; agente y presupuesto de cómputo.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/karpathy/autoresearch/blob/master/README.md

  ```bash
  # 2. Install dependencies
  uv sync
  ```
- **Primera prueba propuesta (no ejecutada):** Lee program.md y ejecuta primero un experimento manual pequeño antes de permitir iteraciones Éxito: Puedes comparar métrica y cambio concreto del experimento
- **Combina con:** `nanochat` [19/aprender], `claude-code` [20/terminal], `codex` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Se quitan gpt-researcher y crawl4ai: es investigación en entrenamiento de modelos, no en la web. Probado por el autor en H100 y no diseñado actualmente para CPU o MPS; no se traslada su sugerencia de desactivar permisos como requisito para principiantes.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-21-research.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Agentes de research autónomo», lee `docs/alexandria/categoria-21-research.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-21-research.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
