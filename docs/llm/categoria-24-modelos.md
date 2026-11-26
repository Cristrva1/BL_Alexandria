# Alexandría para agentes · Modelos abiertos y fundacionales

Categoría 24 «Modelos abiertos y entrenamiento» › subcategoría `modelos`. 7 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=24&sub=modelos · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `timesfm` | Modelos preentrenados de Google para pronóstico de series temporales; las… | 2 Intermedio | 70 | Apache-2.0 (OSI permisiva) | sin grupo |
| `laya` | Motor de decisiones que clasifica texto o selecciona opciones mediante modelos… | 3 Avanzado | 69 | Apache-2.0 (OSI permisiva) | sin grupo |
| `deepseek-v3` | Modelo de lenguaje abierto de DeepSeek (671B parámetros, MoE) para chat, código… | 3 Avanzado | 67 | MIT (OSI permisiva) | sin grupo |
| `cosmos` | Plataforma de "world foundation models" de NVIDIA para IA física y embodiment… | 3 Avanzado | 61 | OpenMDW-1.1 (OSI permisiva) | sin grupo |
| `gemma` | Biblioteca oficial de Google DeepMind para usar y ajustar los modelos de pesos… | 3 Avanzado | 53 | Apache-2.0 (OSI permisiva) | sin grupo |
| `nemotron` | Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron… | 1 Básico | 46 | Apache-2.0 (OSI permisiva) | sin grupo |
| `kimi-k2-7-code` | Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos… | 3 Avanzado | 34 | Modified MIT; revisar condiciones (source-available) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### TimesFM (`timesfm`)

- **Repo:** https://github.com/google-research/timesfm · Apache-2.0 · nivel 2 · 70/100
- **Qué es:** TimesFM, modelo fundacional preentrenado de Google Research para pronóstico de series temporales (artículo en ICML 2024). El código es Apache-2.0 y la licencia de los pesos cambia por versión.
- **Cuándo elegirlo:** Casos: Estudiar demanda con series temporales; Comparar un baseline de pronóstico.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; serie numérica ordenada; backend PyTorch o MLX; pesos permitidos; hardware prerequisites; API de IA: opcional; Python; serie numérica ordenada; backend PyTorch o MLX; pesos permitidos.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/google-research/timesfm/blob/master/README.md

  ```shell
  # Install TimesFM with PyTorch
  pip install timesfm[torch]
  ```
- **Primera prueba propuesta (no ejecutada):** Pronostica un tramo reservado de una serie de ejemplo y compáralo con datos que no diste al modelo Éxito: Puedes medir error fuera de la muestra
- **Combina con:** `polars` [25/datos], `duckdb` [25/datos], `pytorch` [24/entrenamiento]
- **Riesgos y avisos:** Sin alternativas declaradas. Código y pesos hasta 2.5 son Apache; pesos 3.0 autoalojados no permiten uso comercial o productivo, que sí se ofrece mediante servicios Google autorizados.

### laya (`laya`)

- **Repo:** https://github.com/NandhaKishorM/laya · Apache-2.0 · nivel 3 · 69/100
- **Qué es:** laya, motor de decisión multilingüe no autoregresivo de @NandhaKishorM, con preprint asociado («From Laya to Vega»). Licencia Apache-2.0. Es muy reciente (septiembre de 2026, v0.4.34) y ya tiene ~36k estrellas, una cifra inusual…
- **Cuándo elegirlo:** Casos: Clasificar consultas por intención; Elegir una opción estructurada.
- **Requisitos:** nivel 3: preparación pesada; Python 3.10+; pesos del checkpoint para inferencia real; memoria del modelo; hardware prerequisites; API de IA: no; Python 3.10+; pesos del checkpoint para inferencia real; memoria del modelo.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install laya` — fuente: https://github.com/NandhaKishorM/laya/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Prueba una decisión entre categorías de soporte y comprueba si usas routing offline o inferencia con pesos Éxito: Puedes distinguir una regla de enrutamiento de una predicción del modelo
- **Combina con:** `langgraph` [3/py], `llama-index` [3/py], `crewai` [3/py]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Recuento de estrellas inusual para su edad. Ofrece MCP stdio opcional; el ejemplo offline sin descarga es routing y no demuestra que se haya cargado un modelo; las probabilidades requieren evaluación….

### DeepSeek-V3 (`deepseek-v3`)

- **Repo:** https://github.com/deepseek-ai/DeepSeek-V3 · MIT · nivel 3 · 67/100
- **Qué es:** DeepSeek-V3, modelo de lenguaje MoE de DeepSeek con 671B parámetros totales y 37B activos por token. El código es MIT y los pesos usan un Model Agreement propio.
- **Cuándo elegirlo:** Casos: Conectar un modelo abierto potente a un agente mediante la API de DeepSeek; Estudiar cómo se sirve un modelo MoE grande con vLLM o SGLang. Evítalo si Quieres correr un modelo en un equipo doméstico; elige un modelo pequeño con Ollama y revisa los límites antes de elegirlo.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; API: cuenta en platform.deepseek.com; local: servidor con varias GPU y un motor como SGLang o vLLM; hardware gpu; API de IA: opcional; cuenta en la plataforma de DeepSeek para la API; o un servidor con varias GPU para la ruta local; un motor de inferencia como SGLang o vLLM.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/deepseek-ai/DeepSeek-V3.git` — fuente: https://github.com/deepseek-ai/DeepSeek-V3/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Envía una petición de prueba a la API de DeepSeek desde un cliente compatible con OpenAI y pide completar una función corta Éxito: Recibes la respuesta y ves en tu panel el consumo de esa llamada
- **Combina con:** `sglang` [23/serving], `vllm` [23/serving], `litellm` [23/serving], `tensorrt-llm` [23/serving]
- **Riesgos y avisos:** Sin alternativas declaradas. Repo histórico: conviene evaluar las versiones más nuevas de DeepSeek. No cabe en un equipo doméstico: la demo oficial usa dos nodos de 8 GPU. No es un IDE ni una integración nativa con Claude Code, Codex o Antigravity.

### cosmos (`cosmos`)

- **Repo:** https://github.com/NVIDIA/cosmos · OpenMDW-1.1 · nivel 3 · 61/100
- **Qué es:** NVIDIA Cosmos, plataforma de modelos fundacionales de mundo (world foundation models) para IA física: robótica, vehículos autónomos, industria y más. Código y modelos con licencia OpenMDW-1.1 (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Explorar datos sintéticos para robótica; Estudiar generación de escenas físicas.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; GPU compatible; entorno de la receta; acceso aprobado a pesos restringidos; token HF de lectura; hardware prerequisites; API de IA: opcional; GPU compatible; entorno de la receta; acceso aprobado a pesos restringidos; token HF de lectura.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/NVIDIA/cosmos/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Consulta una demo o ejecuta una receta pequeña y compara el video con su condicionamiento Éxito: Puedes reconocer entrada, modelo y salida generada
- **Combina con:** `diffusers` [11/modelos], `pytorch` [24/entrenamiento], `nemotron`, `warp` [26/simulacion]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Autenticarse en Hugging Face no concede por sí solo acceso al repositorio gated de Guardrail; las escenas generadas no prueban fidelidad física ni aptitud para….

### Gemma (biblioteca JAX) (`gemma`)

- **Repo:** https://github.com/google-deepmind/gemma · Apache-2.0 · nivel 3 · 53/100
- **Qué es:** Biblioteca de código abierto (Apache-2.0) de Google DeepMind para la familia Gemma. Activa, con documentación en gemma-llm.readthedocs.io.
- **Cuándo elegirlo:** Casos: chatear con un modelo Gemma en Python con JAX; ajustar Gemma con LoRA en GPU o TPU.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él, necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install gemma` — fuente: https://github.com/google-deepmind/gemma/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala JAX para tu hardware y después `pip install gemma`; ejecuta el ejemplo de muestreo con un checkpoint pequeño. Éxito: El modelo responde al prompt de ejemplo.
- **Combina con:** `jax` [24/entrenamiento], `jupyterlab` [25/datos], `lm-eval-harness` [23/observabilidad]
- **Riesgos y avisos:** Para usar Gemma en PyTorch o con Ollama, hay rutas alternativas fuera de esta biblioteca.

### Nemotron (NVIDIA) (`nemotron`)

- **Repo:** https://github.com/NVIDIA-NeMo/Nemotron · Apache-2.0 · nivel 1 · 46/100
- **Qué es:** Repositorio para desarrolladores de NVIDIA Nemotron, familia de modelos abiertos para IA agéntica: recetas de entrenamiento, guías de despliegue y ejemplos. Licencia Apache-2.0 (los pesos tienen sus propias licencias).
- **Cuándo elegirlo:** Casos: Explorar modelos abiertos de NVIDIA; Preparar un pipeline guiado de adaptación.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; modelo o receta elegida; GPU según tarea; Claude Code solo para plugin; hardware prerequisites; API de IA: opcional; Navegador; modelo o receta elegida; GPU según tarea; Claude Code solo para plugin.
- **Instalación (documentada en la fuente; no ejecutada):** `/plugin marketplace add NVIDIA-NeMo/Nemotron` — fuente: https://github.com/NVIDIA-NeMo/Nemotron/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige una receta y usa su guía para identificar datos, checkpoint y recursos antes de ejecutarla Éxito: Puedes diferenciar entrenamiento, adaptación e inferencia
- **Combina con:** `vllm` [23/serving], `nemoclaw` [22/infra], `claude-code` [20/terminal], `nemo` [29/stt], `cosmos`
- **Riesgos y avisos:** Sin alternativas declaradas. Es un centro de recursos con modelos y recetas distintas; el plugin nemotron-customize es para Claude Code y no implica compatibilidad automática de toda receta.

### Kimi K2.7 Code (`kimi-k2-7-code`)

- **Repo:** https://huggingface.co/moonshotai/Kimi-K2.7-Code · Modified MIT; revisar condiciones · nivel 3 · 34/100
- **Qué es:** Kimi K2.7 Code, modelo de pesos abiertos de Moonshot AI orientado a programación agéntica, construido sobre Kimi K2.6. Se publica en Hugging Face (moonshotai/Kimi-K2.7-Code), no en GitHub.
- **Cuándo elegirlo:** Casos: Comparar generación de código; Estudiar uso de herramientas con un modelo abierto.
- **Requisitos:** nivel 3: preparación pesada; Servicio Moonshot o infraestructura de inferencia adecuada; licencia Modified MIT; proyecto de prueba; hardware prerequisites; API de IA: opcional; Servicio Moonshot o infraestructura de inferencia adecuada; licencia Modified MIT; proyecto de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://huggingface.co/moonshotai/Kimi-K2.7-Code/blob/74797c9c62378b951a1f6fcf5c4631024e9b8bef/README.md
- **Primera prueba propuesta (no ejecutada):** Revisa la guía de despliegue o API y evalúa una función pequeña con tests conocidos Éxito: Puedes identificar modelo, proveedor y resultado comprobado
- **Combina con:** `vllm` [23/serving], `sglang` [23/serving], `opencode` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Sin repo de GitHub: la fuente canónica es la model card de Hugging Face. Es una ficha de pesos en Hugging Face, no un repositorio Git ni el CLI Kimi; mencionar Codex o Claude en benchmarks no prueba integración con esos planes.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-24-modelos.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Modelos abiertos y fundacionales», lee `docs/alexandria/categoria-24-modelos.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-24-modelos.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
