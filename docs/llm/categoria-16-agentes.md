# Alexandría para agentes · Análisis y pruebas con agentes

Categoría 16 «Analizar software y comprobar su seguridad» › subcategoría `agentes`. 5 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=16&sub=agentes · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `rea` | Herramientas e instrucciones para estudiar el comportamiento y la estructura de… | 2 Intermedio | 75 | MIT (OSI permisiva) | sin grupo |
| `strix` | Agente de pruebas de seguridad para aplicaciones, con rutas de API, modelos… | 2 Intermedio | 72 | Apache-2.0 (OSI permisiva) | recomendado |
| `shannon` | Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y… | 2 Intermedio | 62 | AGPL-3.0 (OSI copyleft) | alternativa |
| `garak` | Escáner de vulnerabilidades de LLM de NVIDIA: prueba jailbreaks, inyección de… | 2 Intermedio | 61 | Apache-2.0 (OSI permisiva) | sin grupo |
| `craft-anything` | Herramientas para estudiar cómo funciona una aplicación y ayudar a construir… | 2 Intermedio | 60 | Apache-2.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### rea (`rea`)

- **Repo:** https://github.com/morluto/rea · MIT · nivel 2 · 75/100
- **Qué es:** REA, un servidor MCP para hacer ingeniería inversa con agentes, desde el comportamiento de una aplicación hasta binarios nativos, de @morluto. Licencia MIT.
- **Cuándo elegirlo:** Casos: Entender estructura de una app propia; Comparar dos versiones de un formato de laboratorio.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Node y npm; agente; herramientas nativas solo según formato; programa propio; hardware prerequisites; API de IA: no; Node y npm; agente; herramientas nativas solo según formato; programa propio.
- **Instalación (documentada en la fuente; no ejecutada):** `npx rea-agents setup` — fuente: https://github.com/morluto/rea/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Analiza estáticamente un pequeño proyecto JavaScript propio y revisa el informe y sus rutas de archivos Éxito: Puedes contrastar cada elemento con el código del proyecto
- **Combina con:** `claude-code` [20/terminal], `ghidra` [16/reversing], `jadx` [16/reversing], `codex` [20/terminal], `awesome-ai-reverse-engineering` [16/referencias], `awesome-reverse-engineering` [16/referencias]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Sin alternativas declaradas. Revisa qué escribe el setup en la configuración de tu agente. Úsalo solo con software propio o con autorización escrita. Los backends tienen requisitos distintos; el setup propone cambios de cliente y conserva copias; no todos los formatos funcionan solo con Node.

### strix (`strix`)

- **Repo:** https://github.com/usestrix/strix · Apache-2.0 · nivel 2 · 72/100 · recomendado en «Pentesting autónomo con agentes»
- **Qué es:** Herramienta open source de pentesting con agentes de IA autónomos, de usestrix. Licencia Apache-2.0. Es muy activa (~76k estrellas, v1.7.1); el README distingue la versión open source de otras opciones en strix.ai.
- **Cuándo elegirlo:** Casos: Estudiar una revisión de seguridad en laboratorio; Integrar un escaneo autorizado en CI de prueba.
- **Requisitos:** nivel 2: preparación media; Docker activo; modelo con herramientas; objetivo de laboratorio autorizado; hardware prerequisites; API de IA: depends; Docker activo; modelo con herramientas; objetivo de laboratorio autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -sSL https://strix.ai/install | bash` — fuente: https://github.com/usestrix/strix/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Delimita una app propia desechable y revisa proveedor y modo antes de una evaluación pequeña Éxito: Los hallazgos quedan asociados al alcance y evidencias que puedes revisar
- **Combina con:** `ollama` [8/motores], `github-mcp-server` [5/servidores], `semgrep` [16/defensa], `defending-code-reference-harness` [16/skills]
- **Alternativas:** `shannon`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Alternativa (elige una): shannon. Úsalo solo contra sistemas propios o con autorización escrita. Las skills ayudan a operar Strix; la ruta de suscripción ChatGPT es distinta de cargar una skill en Codex; no se hereda el coste entre ambas.

### shannon (`shannon`)

- **Repo:** https://github.com/KeygraphHQ/shannon · AGPL-3.0 · nivel 2 · 62/100 · alternativa en «Pentesting autónomo con agentes»
- **Qué es:** Pentester autónomo con IA para aplicaciones web y APIs, de Keygraph. Licencia AGPL-3.0. Es muy activo (~52k estrellas, v3.5.1).
- **Cuándo elegirlo:** Casos: Evaluar una app propia en un laboratorio; Comparar evidencias y veredictos de una prueba autorizada.
- **Requisitos:** nivel 2: preparación media; Node; dependencias de la guía; objetivo autorizado de laboratorio; código; proveedor o modelo local; hardware prerequisites; API de IA: depends; Node; dependencias de la guía; objetivo autorizado de laboratorio; código; proveedor o modelo local.
- **Instalación (documentada en la fuente; no ejecutada):** `npx @keygraph/shannon@latest` — fuente: https://github.com/KeygraphHQ/shannon/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Configura primero un objetivo desechable propio y revisa alcance, credenciales y límites antes de iniciar un análisis Éxito: Puedes identificar exactamente qué se analizaría y dónde se guardarían hallazgos y costes
- **Combina con:** `ollama` [8/motores], `semgrep` [16/defensa], `mitmproxy` [16/pruebas]
- **Alternativas:** `strix`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativa (elige una): strix. Úsalo solo contra sistemas propios o con autorización escrita. Nunca en producción. La versión actual no soporta suscripciones Claude Code; esa ruta corresponde a 1.9.0 anterior y no se anuncia como soporte actual.

### garak (`garak`)

- **Repo:** https://github.com/NVIDIA/garak · Apache-2.0 · nivel 2 · 61/100
- **Qué es:** Kit de red teaming y evaluación de IA generativa de código abierto (Apache-2.0), creado por Leon Derczynski y mantenido bajo la organización NVIDIA. Activo y con artículo académico asociado.
- **Cuándo elegirlo:** Casos: auditar un chatbot propio frente a inyección de prompts y jailbreaks antes de publicarlo; comparar la robustez de varios modelos locales con las mismas sondas.
- **Requisitos:** nivel 2: preparación media; Python, pyproject.toml, requirements.txt; hardware model_dependent; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install -U garak` — fuente: https://github.com/NVIDIA/garak/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `python -m pip install -U garak` y ejecuta una sonda sencilla contra un modelo pequeño de Hugging Face o local. Éxito: Obtienes un informe con el porcentaje de fallos por sonda y un registro JSONL.
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `promptfoo` [23/observabilidad]
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Las tasas de fallo dependen de la versión de las sondas; fija la versión para comparar resultados.

### craft-anything (`craft-anything`)

- **Repo:** https://github.com/storytold/craft-anything · Apache-2.0 · nivel 2 · 60/100
- **Qué es:** Motor open source en Rust para estudiar cómo funciona un sitio web, una app o un juego y que un agente construya una versión propia en «sala limpia», del equipo ArtCraft (storytold). Licencia dual MIT o Apache-2.0.
- **Cuándo elegirlo:** Casos: Comprender una implementación propia existente; Comparar comportamiento antes de una reimplementación.
- **Requisitos:** nivel 2: preparación media; Rust >=1.97 para compilar; dependencias del sistema; agente o proveedor; app propia de prueba; hardware prerequisites; API de IA: depends; Rust >=1.97 para compilar; dependencias del sistema; agente o proveedor; app propia de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/storytold/craft-anything/blob/main/README.md

  ```sh
  git clone https://github.com/storytold/craft-anything && cd craft-anything
  cargo run --release -p craft-anything                # the desktop app
  cargo install --path apps/craft-anything-cli         # the CLI, as `craft-anything-cli`
  craft-anything-cli doctor                            # checks the install, coding agents and engines
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta doctor y prueba una consulta de análisis sobre una app pequeña propia antes de pedir reconstrucción Éxito: Puedes identificar motores disponibles, proveedor y capacidades verificadas
- **Combina con:** `claude-code` [20/terminal], `ghidra` [16/reversing], `rea`
- **Riesgos y avisos:** Uso dual: solo contra sistemas propios o con autorización. Sin alternativas declaradas. Clonar el diseño o el código de terceros puede infringir derechos de autor, marcas o términos de servicio: úsalo solo con…. El autor dice que existe adaptador Codex pero no está probado en una instalación real; MCP y análisis no certifican esa ruta de reconstrucción.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-16-agentes.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Análisis y pruebas con agentes», lee `docs/alexandria/categoria-16-agentes.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-16-agentes.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
