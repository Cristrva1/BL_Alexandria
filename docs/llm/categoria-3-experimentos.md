# Alexandría para agentes · Simulación, evolución y debate entre modelos

Categoría 3 «Construir agentes y coordinar equipos de IA» › subcategoría `experimentos`. 5 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=3&sub=experimentos · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `mirofish` | Motor de inteligencia colectiva/predicción que construye mundos digitales con… | 3 Avanzado | 64 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `openevolve` | Agente de codificación evolutivo que optimiza algoritmos por simulación… | 3 Avanzado | 53 | Apache-2.0 (OSI permisiva) | sin grupo |
| `llm-council` | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. | 2 Intermedio | 40 | — (sin licencia detectada) | sin grupo |
| `jev-fraud` | Demostración de clasificación con modelos y servicios de IA para estudiar un… | 2 Intermedio | 36 | MIT (OSI permisiva) | sin grupo |
| `hermes-agent-self-evolution` | Herramientas para optimizar skills, prompts y código de Hermes Agent mediante… | 2 Intermedio | 34 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### MiroFish (`mirofish`)

- **Repo:** https://github.com/666ghj/MiroFish · AGPL-3.0 · nivel 3 · 64/100
- **Qué es:** Motor de 'inteligencia colectiva' (AGPL-3.0) de 666ghj para predecir escenarios simulando sociedades de agentes. Su motor de simulación es OASIS, de CAMEL-AI.
- **Cuándo elegirlo:** Casos: Explorar reacciones hipotéticas a un anuncio; Comparar escenarios narrativos antes de investigar datos reales.
- **Requisitos:** nivel 3: preparación pesada, varios servicios con Docker Compose, requiere clave de API; Docker o Node 18+ y Python 3.11–3.12; clave LLM; Zep Cloud; hardware prerequisites; API de IA: sí; Docker o Node 18+ y Python 3.11–3.12; clave LLM; Zep Cloud.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/666ghj/MiroFish/blob/main/README.md

  ```bash
  # 1. Configure environment variables (same as source deployment)
  cp .env.example .env

  # 2. Pull image and start
  docker compose up -d
  ```
- **Primera prueba propuesta (no ejecutada):** Carga un escenario ficticio y realiza una simulación corta con menos de 40 rondas Éxito: Puedes inspeccionar los agentes simulados y el informe del escenario
- **Combina con:** `graphiti` [6/memoria], `litellm` [23/serving], `ollama` [8/motores], `pythia` [10/osint]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. Combinación anterior con openevolve eliminada: sin relación técnica documentada. Son simulaciones generadas, no predicciones validadas del mercado ni evidencia de cómo actuarán personas reales.

### openevolve (`openevolve`)

- **Repo:** https://github.com/algorithmicsuperintelligence/openevolve · Apache-2.0 · nivel 3 · 53/100
- **Qué es:** Implementación open source (Apache-2.0) de AlphaEvolve de Google DeepMind, mantenida por algorithmicsuperintelligence. Es activa (v0.4.1) y el README lista artículos científicos que la han usado para obtener nuevos resultados.
- **Cuándo elegirlo:** Casos: Optimizar una función medible; Buscar mejores reglas de ordenación.
- **Requisitos:** nivel 3: preparación pesada; Python 3.10+; evaluador de calidad; API o CLI compatible autenticado; hardware prerequisites; API de IA: depends; Python 3.10+; evaluador de calidad; API o CLI compatible autenticado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/algorithmicsuperintelligence/openevolve/blob/main/README.md

  ```bash
  git clone https://github.com/algorithmicsuperintelligence/openevolve.git
  cd openevolve
  pip install -e .
  ```
- **Primera prueba propuesta (no ejecutada):** Prueba la minimización de una función con pocas iteraciones y revisa cada candidato Éxito: El evaluador permite comparar la puntuación inicial y la final
- **Combina con:** `ollama` [8/motores], `vllm` [23/serving], `litellm` [23/serving]
- **Riesgos y avisos:** Sin alternativas declaradas. Combinación anterior con llm-council eliminada: sin relación técnica. Es una implementación independiente de AlphaEvolve; una puntuación mejor solo vale para el evaluador definido.

### llm-council (`llm-council`)

- **Repo:** https://github.com/karpathy/llm-council · — · nivel 2 · 40/100
- **Qué es:** Experimento personal de Andrej Karpathy, 'vibe coded' en un sábado según el propio README. El autor avisa de que no lo mantendrá ni lo soportará. No tiene archivo de licencia, así que legalmente no hay permiso de reutilización explícito, y…
- **Cuándo elegirlo:** Casos: Comparar explicaciones de un concepto; Revisar opciones para una decisión técnica.
- **Requisitos:** nivel 2: preparación media, requiere clave de API; Python y uv; Node.js; clave OpenRouter; hardware prerequisites; API de IA: sí; Python y uv; Node.js; clave OpenRouter.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/karpathy/llm-council/blob/master/README.md

  ```bash
  uv sync

  cd frontend
  npm install
  cd ..
  ```
- **Primera prueba propuesta (no ejecutada):** Envía una pregunta acotada y compara las respuestas y las revisiones entre modelos Éxito: Se distinguen propuestas iniciales, evaluaciones y síntesis final
- **Combina con:** `litellm` [23/serving], `ollama` [8/motores], `promptfoo` [23/observabilidad]
- **Riesgos y avisos:** Sin alternativas declaradas. Sin licencia: no reutilices el código en proyectos distribuidos sin permiso. Una mayoría de modelos puede compartir el mismo error; comprueba las afirmaciones con fuentes.

### jev-fraud (`jev-fraud`)

- **Repo:** https://github.com/Nutlope/jev-fraud · MIT · nivel 2 · 36/100
- **Qué es:** Demo open source (MIT) de @Nutlope que muestra una cascada de modelos para detectar fraude en emails. Es un proyecto de ejemplo, no una herramienta mantenida: tiene ~17 estrellas y su último push es de septiembre de 2026.
- **Cuándo elegirlo:** Casos: Estudiar clasificación con escalado de casos inciertos; Comparar confianza y aciertos sobre un conjunto ficticio.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node.js y npm; claves Together y AI Gateway solo para ejecución nueva; hardware prerequisites; API de IA: opcional; Node.js y npm; claves Together y AI Gateway solo para ejecución nueva.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Nutlope/jev-fraud/blob/main/README.md

  ```sh
  git clone https://github.com/Nutlope/jev-fraud.git
     cd jev-fraud
     npm install
     cp .env.example .env.local

  npm run dev -- --port 3017
  ```
- **Primera prueba propuesta (no ejecutada):** Abre la aplicación y usa primero 10s replay sobre la grabación incluida Éxito: Ves la demostración grabada sin lanzar una clasificación nueva
- **Combina con:** `vercel-ai` [3/ts], `promptfoo` [23/observabilidad], `ui` [9/componentes]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Jev (typesafe.ai) y Kimi K3 son modelos comerciales; resultados no verificados de forma independiente. Es una demo sobre una muestra pequeña; sus resultados no validan un detector de fraude en producción.

### hermes-agent-self-evolution (`hermes-agent-self-evolution`)

- **Repo:** https://github.com/NousResearch/hermes-agent-self-evolution · — · nivel 2 · 34/100
- **Qué es:** Herramienta de Nous Research para mejorar automáticamente Hermes Agent mediante evolución de prompts con DSPy y GEPA. El repositorio no tiene archivo LICENSE: la mención 'MIT licensed' del README parece referirse a GEPA [DATO NO…
- **Cuándo elegirlo:** Casos: Refinar una skill de revisión de código; Comparar instrucciones con fallos observados.
- **Requisitos:** nivel 2: preparación media, requiere programar con él, requiere clave de API; Python; checkout de Hermes Agent; credenciales del optimizador; casos de evaluación; hardware prerequisites; API de IA: sí; Python; checkout de Hermes Agent; credenciales del optimizador; casos de evaluación.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/NousResearch/hermes-agent-self-evolution/blob/main/README.md

  ```bash
  # Install
  git clone https://github.com/NousResearch/hermes-agent-self-evolution.git
  cd hermes-agent-self-evolution
  pip install -e ".[dev]"
  ```
- **Primera prueba propuesta (no ejecutada):** Optimiza una skill pequeña con datos sintéticos y compara el candidato antes de aceptarlo Éxito: Puedes revisar diferencias y puntuaciones manteniendo la versión inicial
- **Combina con:** `hermes-agent` [21/asistentes], `dspy` [3/py], `claude-code` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Sin archivo de licencia en el repositorio. Solo la evolución de skills figura implementada; herramientas, prompts del sistema, código y bucle continuo son fases previstas; lee sesiones Claude Code como….

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-3-experimentos.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Simulación, evolución y debate entre modelos», lee `docs/alexandria/categoria-3-experimentos.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-3-experimentos.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
