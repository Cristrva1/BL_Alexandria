# Alexandría para agentes · Aprender LLMs desde cero

Categoría 19 «Aprender IA y escribir mejores prompts» › subcategoría `aprender`. 9 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=19&sub=aprender · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `llms-from-scratch` | Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en… | 1 Básico | 71 | Apache-2.0 (OSI permisiva) | recomendado |
| `ml-for-beginners` | Curso gratuito de Microsoft de 12 semanas y 26 lecciones de machine learning… | 1 Básico | 67 | MIT (OSI permisiva) | sin grupo |
| `nanochat` | Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de… | 2 Intermedio | 62 | MIT (OSI permisiva) | sin grupo |
| `annotated-dl-papers` | Más de 60 implementaciones sencillas en PyTorch de papers de deep learning con… | 1 Básico | 59 | MIT (OSI permisiva) | sin grupo |
| `train-llm-from-scratch` | Tutorial y código de PyTorch para construir y entrenar un modelo de lenguaje… | 1 Básico | 59 | MIT (OSI permisiva) | sin grupo |
| `awesome-machine-learning` | Directorio de frameworks, bibliotecas y recursos de machine learning organizado… | 1 Básico | 55 | CC0-1.0 (texto incompleto en LICENSE) (OSI permisiva) | sin grupo |
| `llm-course` | Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender… | 1 Básico | 53 | Apache-2.0 (OSI permisiva) | alternativa |
| `llm.c` | Implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin… | 3 Avanzado | 49 | MIT (OSI permisiva) | sin grupo |
| `how-to-train-your-gpt` | Guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material… | 1 Básico | 45 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### LLMs from Scratch (`llms-from-scratch`)

- **Repo:** https://github.com/rasbt/LLMs-from-scratch · Apache-2.0 · nivel 1 · 71/100 · recomendado en «Aprender LLM desde cero»
- **Qué es:** Repositorio oficial del código del libro 'Build a Large Language Model (From Scratch)' de Sebastian Raschka (Manning). El LICENSE es Apache-2.0, aunque GitHub lo marca NOASSERTION.
- **Cuándo elegirlo:** Casos: Aprender cómo funciona un Transformer; Estudiar ajuste de instrucciones.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python; entorno PyTorch; nociones de programación; equipo según capítulo; hardware prerequisites; API de IA: opcional; Python; entorno PyTorch; nociones de programación; equipo según capítulo.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git` — fuente: https://github.com/rasbt/LLMs-from-scratch/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el capítulo de tokenización con una frase corta antes de entrenar una red Éxito: Puedes ver la conversión de texto a tokens y explicarla
- **Combina con:** `pytorch` [24/entrenamiento], `nanochat`, `transformers` [24/entrenamiento], `llm.c`, `annotated-dl-papers`
- **Alternativas:** `llm-course`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): llm-course. Requiere base de Python; la instalación está en setup y la evaluación por API no es obligatoria para todo el libro.

### ML for Beginners (`ml-for-beginners`)

- **Repo:** https://github.com/microsoft/ML-For-Beginners · MIT · nivel 1 · 67/100
- **Qué es:** Currículo educativo de código abierto (MIT) de Microsoft (serie «for Beginners»). Muy popular; mantenimiento continuo con traducciones automáticas.
- **Cuándo elegirlo:** Casos: aprender regresión, clasificación y clustering desde cero; preparar un temario de ML clásico para una clase.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Jupyter Notebook, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/microsoft/ML-For-Beginners.git` — fuente: https://github.com/microsoft/ML-For-Beginners/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repositorio con la descarga dispersa del README (sin traducciones) y abre la primera lección en Jupyter. Éxito: El cuaderno se ejecuta y muestra el primer modelo de regresión.
- **Combina con:** `jupyterlab` [25/datos], `marimo` [25/datos], `llm-course`, `scikit-learn` [24/entrenamiento]
- **Riesgos y avisos:** No cubre deep learning; para ese tema Microsoft remite a otros cursos de la serie.

### nanochat (`nanochat`)

- **Repo:** https://github.com/karpathy/nanochat · MIT · nivel 2 · 62/100
- **Qué es:** Arnés experimental mínimo (MIT) de Andrej Karpathy para entrenar LLMs de principio a fin en un solo nodo de GPU. Es experimental pero muy seguido (~61k estrellas); último push en septiembre de 2026. Sucede conceptualmente a nanoGPT.
- **Cuándo elegirlo:** Casos: Estudiar una cadena de entrenamiento a chat; Reproducir un experimento con presupuesto delimitado.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; uv; Python; CPU o GPU según ruta; presupuesto de cómputo; hardware prerequisites; API de IA: no; uv; Python; CPU o GPU según ruta; presupuesto de cómputo.
- **Instalación (documentada en la fuente; no ejecutada):** `uv sync --extra cpu    # (or) Use for CPU-only / MPS` — fuente: https://github.com/karpathy/nanochat/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Prepara la ruta CPU para estudiar el código y lee speedrun antes de contratar un nodo GPU Éxito: Distingues la instalación de dependencias del entrenamiento completo
- **Combina con:** `pytorch` [24/entrenamiento], `llms-from-scratch`, `llm.c`, `autoresearch` [21/research], `how-to-train-your-gpt`, `train-llm-from-scratch`
- **Riesgos y avisos:** Sin alternativas declaradas. Coste real: alquilar 8×H100 durante horas. El lema de cien dólares depende del benchmark, hardware y tarifas del autor; no es el coste garantizado de cualquier entrenamiento ni una configuración de….

### labml.ai Annotated Paper Implementations (`annotated-dl-papers`)

- **Repo:** https://github.com/labmlai/annotated_deep_learning_paper_implementations · MIT · nivel 1 · 59/100
- **Qué es:** Colección educativa de código abierto (MIT) de labml.ai (Varuna Jayasiri y colaboradores). Muy popular; se añaden implementaciones con frecuencia.
- **Cuándo elegirlo:** Casos: entender un mecanismo como la atención o RoPE leyendo código comentado; reutilizar una implementación de referencia como punto de partida para experimentos.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python, requirements.txt, setup.py; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install labml-nn` — fuente: https://github.com/labmlai/annotated_deep_learning_paper_implementations/blob/master/readme.md
- **Primera prueba propuesta (no ejecutada):** Abre en nn.labml.ai la implementación de atención multi-cabeza y lee el código con sus notas. Éxito: Ves el código de PyTorch con la explicación de cada paso al lado.
- **Combina con:** `pytorch` [24/entrenamiento], `claude-code` [20/terminal], `llms-from-scratch`
- **Riesgos y avisos:** Son implementaciones didácticas, no optimizadas para producción.

### train-llm-from-scratch (`train-llm-from-scratch`)

- **Repo:** https://github.com/FareedKhan-dev/train-llm-from-scratch · MIT · nivel 1 · 59/100
- **Qué es:** Tutorial y código (MIT) de @FareedKhan-dev para entrenar un modelo de lenguaje desde cero en PyTorch puro. Empezó como tutorial de preentrenamiento y hoy cubre hasta modelos alineados de estilo razonador.
- **Cuándo elegirlo:** Casos: Comprender la preparación de un corpus; Explorar un entrenamiento pequeño controlado.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python y PyTorch; datos pequeños; CPU o GPU según escala; hardware prerequisites; API de IA: no; Python y PyTorch; datos pequeños; CPU o GPU según escala.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/main/README.md

  ```bash
  git clone https://github.com/FareedKhan-dev/train-llm-from-scratch.git
  cd train-llm-from-scratch
  pip install -e .
  ```
- **Primera prueba propuesta (no ejecutada):** Instala el paquete en un entorno de prueba y estudia la configuración de un entrenamiento mínimo Éxito: Puedes identificar tamaño del modelo, datos y salida de checkpoints
- **Combina con:** `pytorch` [24/entrenamiento], `trl` [24/entrenamiento], `nanochat`
- **Riesgos y avisos:** Sin alternativas declaradas. Los extras train, ui, docs y all son alternativas; empezar por un corpus pequeño evita confundir la demostración con entrenar un modelo grande.

### awesome-machine-learning (`awesome-machine-learning`)

- **Repo:** https://github.com/josephmisiti/awesome-machine-learning · CC0-1.0 (texto incompleto en LICENSE) · nivel 1 · 55/100
- **Qué es:** Lista curada clásica de frameworks, bibliotecas y software de machine learning organizada por lenguaje, mantenida por Joseph Misiti e inspirada en awesome-php. GitHub marca su licencia como NOASSERTION.
- **Cuándo elegirlo:** Casos: Descubrir bibliotecas de clasificación; Encontrar herramientas de visión por lenguaje.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; lenguaje y problema de interés; hardware prerequisites; API de IA: no; Navegador; lenguaje y problema de interés.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/josephmisiti/awesome-machine-learning/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Busca dos bibliotecas del lenguaje que conoces y abre sus fuentes para comparar mantenimiento y requisitos Éxito: Obtienes una pequeña lista de candidatos con función diferenciada
- **Combina con:** `pytorch` [24/entrenamiento], `transformers` [24/entrenamiento], `llm-course`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. No se instala la lista ni se hereda la compatibilidad de todos los proyectos enlazados.

### LLM Course (`llm-course`)

- **Repo:** https://github.com/mlabonne/llm-course · Apache-2.0 · nivel 1 · 53/100 · alternativa en «Aprender LLM desde cero»
- **Qué es:** Curso gratuito (Apache-2.0) de Maxime Labonne para aprender LLMs, con rutas de estudio y notebooks de Colab. Es muy popular (~85k estrellas). El autor coescribió el libro 'LLM Engineer's Handbook' basado en este curso.
- **Cuándo elegirlo:** Casos: Crear un plan de aprendizaje de LLM; Estudiar cuantización GGUF.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; Python y cómputo al practicar; hardware prerequisites; API de IA: opcional; Navegador; Python y cómputo al practicar.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/mlabonne/llm-course/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Recorre la ruta de fundamentos y elige el notebook de cuantización solo después de revisar sus requisitos Éxito: Puedes ubicar la diferencia entre entrenar, cuantizar y servir un modelo
- **Combina con:** `unsloth` [24/entrenamiento], `trl` [24/entrenamiento], `pytorch` [24/entrenamiento], `awesome-machine-learning`, `ml-for-beginners`
- **Alternativas:** `llms-from-scratch`, `generative-ai-for-beginners`
- **Riesgos y avisos:** Alternativas (elige una): llms-from-scratch, generative-ai-for-beginners. Combinación anterior con llama-factory eliminada: el curso no lo usa (y es…. Es un mapa de aprendizaje con recursos externos y prácticas locales; no existe una instalación única para toda la ruta.

### llm.c (`llm.c`)

- **Repo:** https://github.com/karpathy/llm.c · MIT · nivel 3 · 49/100
- **Qué es:** Implementación de entrenamiento de LLMs en C/CUDA puro (MIT) de Andrej Karpathy, sin PyTorch ni Python. Es un proyecto educativo y de investigación de rendimiento, poco activo: el último push es de junio de 2025.
- **Cuándo elegirlo:** Casos: Estudiar entrenamiento sin un framework pesado; Comparar una implementación C con PyTorch.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él, necesita GPU; Compilador C; Python para preparación; CUDA y GPU para las rutas aceleradas; hardware prerequisites; API de IA: no; Compilador C; Python para preparación; CUDA y GPU para las rutas aceleradas.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/karpathy/llm.c/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Lee el ejemplo GPT-2 y localiza las operaciones de forward y backward antes de compilar Éxito: Puedes relacionar las operaciones matemáticas con el código C
- **Combina con:** `nanochat`, `llms-from-scratch`, `pytorch` [24/entrenamiento]
- **Riesgos y avisos:** Sin alternativas declaradas. Mantenimiento bajo desde 2025. Es un proyecto técnico de entrenamiento; no es una app de chat lista para personas sin programación.

### how-to-train-your-gpt (`how-to-train-your-gpt`)

- **Repo:** https://github.com/raiyanyahya/how-to-train-your-gpt · MIT · nivel 1 · 45/100
- **Qué es:** Libro de texto interactivo (MIT) de @raiyanyahya para construir, entrenar y ejecutar un modelo de lenguaje moderno desde cero. El autor declara que lo escribió para aprender y que usó IA para entender y verificar conceptos, así que…
- **Cuándo elegirlo:** Casos: Aprender tokenización paso a paso; Comprender atención con ejemplos pequeños.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python; Jupyter; entorno PyTorch; equipo adecuado al experimento; hardware prerequisites; API de IA: no; Python; Jupyter; entorno PyTorch; equipo adecuado al experimento.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/raiyanyahya/how-to-train-your-gpt/blob/master/README.md

  ```bash
  # Install everything you need
  pip install jupyter tiktoken torch numpy datasets matplotlib --index-url https://download.pytorch.org/whl/cpu

  # Start with chapter 2 (tokenization)
  jupyter notebook notebooks/02_tokenization.ipynb
  ```
- **Primera prueba propuesta (no ejecutada):** Abre el notebook de tokenización y procesa una frase antes de pasar a entrenamiento Éxito: Puedes inspeccionar tokens y reconstrucción del texto
- **Combina con:** `nanochat`, `pytorch` [24/entrenamiento], `marimo` [25/datos]
- **Riesgos y avisos:** Sin alternativas declaradas. Material escrito con ayuda de IA según su autor: verifica las afirmaciones técnicas. Empieza por el capítulo de setup; los comandos del README ofrecen alternativas y no deben concatenarse como si todas fueran obligatorias.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-19-aprender.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Aprender LLMs desde cero», lee `docs/alexandria/categoria-19-aprender.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-19-aprender.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
