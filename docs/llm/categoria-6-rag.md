# Alexandría para agentes · RAG y motores de conocimiento

Categoría 6 «Memoria, RAG y búsqueda de conocimiento» › subcategoría `rag`. 10 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=6&sub=rag · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `ragflow` | Motor de RAG con comprensión profunda de documentos, citas y agentes… | 3 Avanzado | 82 | Apache-2.0 (OSI permisiva) | recomendado |
| `onyx` | Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con… | 2 Intermedio | 70 | MIT + Onyx Enterprise License (ee/) (open-core) | sin grupo |
| `lightrag` | RAG simple y rápido que combina grafo de conocimiento y vectores, de la… | 2 Intermedio | 66 | MIT (OSI permisiva) | alternativa |
| `kotaemon` | Interfaz RAG limpia y personalizable para chatear con documentos, con modelos… | 2 Intermedio | 61 | Apache-2.0 (OSI permisiva) | sin grupo |
| `pageindex` | Índice de documentos para RAG sin vectores, basado en razonamiento sobre una… | 2 Intermedio | 60 | MIT (OSI permisiva) | alternativa |
| `meilisearch` | Motor de búsqueda rápido en Rust con texto completo, búsqueda semántica e… | 1 Básico | 58 | MIT (source-available) | sin grupo |
| `txtai` | Framework de IA todo en uno para búsqueda semántica, RAG, pipelines con LLM… | 2 Intermedio | 58 | Apache-2.0 (OSI permisiva) | sin grupo |
| `graphrag` | Sistema de RAG de Microsoft que recupera información sobre un grafo de… | 2 Intermedio | 55 | MIT (OSI permisiva) | alternativa |
| `chonkie` | Divide textos largos en fragmentos para indexarlos o recuperarlos, con… | 2 Intermedio | 51 | MIT (OSI permisiva) | sin grupo |
| `agentic-rag-for-dummies` | Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta… | 2 Intermedio | 47 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### RAGFlow (`ragflow`)

- **Repo:** https://github.com/infiniflow/ragflow · Apache-2.0 · nivel 3 · 82/100 · recomendado en «RAG con grafos e índices de conocimiento»
- **Qué es:** Motor RAG (generación aumentada por recuperación) de código abierto (Apache 2.0) de InfiniFlow, que fusiona RAG con capacidades de agente. Muy activo: la versión 1.0.0 salió el 6 de noviembre de 2026 y el código principal está ahora en Go…
- **Cuándo elegirlo:** Casos: Consultar manuales de una organización; Combinar documentos en una base de conocimiento.
- **Requisitos:** nivel 3: preparación pesada, varios servicios con Docker Compose; Docker; configuración inicial orientativa 4 CPU,16 GB RAM,50 GB disco; modelos; hardware prerequisites; API de IA: depends; Docker; configuración inicial orientativa 4 CPU,16 GB RAM,50 GB disco; modelos.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose -f docker-compose.yml up -d` — fuente: https://github.com/infiniflow/ragflow/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Indexa un PDF propio corto y pregunta por un dato identificable con cita Éxito: La respuesta permite abrir el fragmento y comprobar su procedencia
- **Combina con:** `ollama` [8/motores], `activepieces` [1/motores], `langfuse` [23/observabilidad], `paddleocr` [13/ocr]
- **Alternativas:** `lightrag`, `pageindex`, `graphrag`, `dify`
- **Riesgos y avisos:** Alternativas (elige una): dify, lightrag. El puerto 80 puede chocar con otros servicios web del mismo servidor. Los mínimos del servidor no incluyen necesariamente ejecutar los modelos; prueba pocos documentos antes de ampliar.

### onyx (`onyx`)

- **Repo:** https://github.com/onyx-dot-app/onyx · MIT + Onyx Enterprise License (ee/) · nivel 2 · 70/100
- **Qué es:** Capa de conocimiento y contexto para equipos y agentes de IA de Onyx (antes Danswer). La Community Edition es MIT y la Enterprise Edition añade funciones para grandes organizaciones (GitHub marca la licencia como no estándar por esa…
- **Cuándo elegirlo:** Casos: Buscar conocimiento de equipo; Dar contexto organizacional a un agente de código.
- **Requisitos:** nivel 2: preparación media; Docker o ruta elegida; proveedor; fuente documental de prueba; hardware prerequisites; API de IA: depends; Docker o ruta elegida; proveedor; fuente documental de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `uv tool install onyx-cli && onyx-cli deploy install` — fuente: https://github.com/onyx-dot-app/onyx/blob/main/documentation/snippets/quickstart.mdx
- **Primera prueba propuesta (no ejecutada):** Conecta dos documentos de prueba y formula una consulta que exija una cita Éxito: La respuesta muestra fuentes accesibles para el usuario que consulta
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `searxng` [4/busqueda], `firecrawl` [4/crawlers]
- **Alternativas:** `anything-llm`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativa (elige una): anything-llm. Respeta los permisos de las fuentes; revisa qué conectores sincronizan datos sensibles. Lite es un chat ligero y no indexa documentos; para la prueba documental necesitas el despliegue completo.

### LightRAG (`lightrag`)

- **Repo:** https://github.com/HKUDS/LightRAG · MIT · nivel 2 · 66/100 · alternativa en «RAG con grafos e índices de conocimiento»
- **Qué es:** Sistema RAG «simple y rápido» basado en grafos de conocimiento, del laboratorio HKUDS (Universidad de Hong Kong). MIT y muy activo; la última etiqueta es una release candidate (v1.5.8rc1) y en 2026 absorbió el proyecto multimodal…
- **Cuándo elegirlo:** Casos: Consultar relaciones entre conceptos; Combinar búsqueda de grafos y vectores.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python y uv; LLM; embeddings; almacenamiento; configuración .env; hardware prerequisites; API de IA: depends; Python y uv; LLM; embeddings; almacenamiento; configuración .env.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/HKUDS/LightRAG/blob/main/README.md

  ```bash
  # Install LightRAG Server as a tool using uv (recommended)
  uv tool install "lightrag-hku[api]"
  ```
- **Primera prueba propuesta (no ejecutada):** Indexa un documento ficticio y compara una consulta sobre una entidad con otra sobre sus relaciones Éxito: Puedes inspeccionar los resultados y las relaciones recuperadas
- **Combina con:** `pgvector` [6/vectores], `ollama` [8/motores], `docling` [13/conversion], `langfuse` [23/observabilidad], `ragas` [23/observabilidad], `deeptutor` [21/asistentes]
- **Alternativas:** `ragflow`, `pageindex`, `graphrag`
- **Riesgos y avisos:** Alternativas (elige una): graphrag, ragflow, pageindex. `lightrag-server` escucha en 0.0.0.0 sin autenticación por defecto: actívala antes de usarlo en red. Configura HOST o autenticación antes de arrancar en red; conserva el mismo modelo de embeddings entre indexación y consulta.

### kotaemon (`kotaemon`)

- **Repo:** https://github.com/Cinnamon/kotaemon · Apache-2.0 · nivel 2 · 61/100
- **Qué es:** Herramienta RAG de código abierto (Apache-2.0) de Cinnamon AI, pensada tanto para usuarios finales como para desarrolladores. Popular, aunque el ritmo de cambios se ha reducido (último push en julio de 2026).
- **Cuándo elegirlo:** Casos: hacer preguntas con citas sobre una carpeta de PDF propios; comparar estrategias RAG clásicas y basadas en grafos sobre el mismo corpus.
- **Requisitos:** nivel 2: preparación media; Python, Dockerfile, pyproject.toml; hardware model_dependent; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Cinnamon/kotaemon/blob/main/README.md

  ```bash
  docker run -e GRADIO_SERVER_NAME=0.0.0.0 -e GRADIO_SERVER_PORT=7860 -v ./ktem_app_data:/app/ktem_app_data -p 7860:7860 -it --rm ghcr.io/cinnamon/kotaemon:main-full
  ```
- **Primera prueba propuesta (no ejecutada):** Arranca la imagen Docker main-lite (u ollama) del README, sube un PDF y haz una pregunta. Éxito: La respuesta incluye citas enlazadas a las páginas del documento.
- **Combina con:** `ollama` [8/motores], `lightrag`, `graphrag`, `docling` [13/conversion]
- **Riesgos y avisos:** Alternativas cercanas en el catálogo: anything-llm, open-notebook.

### PageIndex (`pageindex`)

- **Repo:** https://github.com/VectifyAI/PageIndex · MIT · nivel 2 · 60/100 · alternativa en «RAG con grafos e índices de conocimiento»
- **Qué es:** Sistema RAG «sin vectores» basado en razonamiento, de VectifyAI. La versión de código abierto es MIT (v0.7.0) y convive con productos en la nube: PageIndex Cloud, una API de búsqueda de páginas y una app de análisis de documentos.
- **Cuándo elegirlo:** Casos: Consultar informes largos por su estructura; Encontrar una sección de un contrato.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; documento de prueba; proveedor para modo local o cuenta Cloud; hardware prerequisites; API de IA: depends; Python; documento de prueba; proveedor para modo local o cuenta Cloud.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U pageindex` — fuente: https://github.com/VectifyAI/PageIndex/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Indexa un PDF con secciones y pregunta por un dato de una sección concreta Éxito: La recuperación señala la parte pertinente del documento
- **Combina con:** `claude-code` [20/terminal], `openai-agents-python` [3/py], `claude-agent-sdk-python` [3/py]
- **Alternativas:** `ragflow`, `lightrag`, `graphrag`
- **Riesgos y avisos:** Alternativa (elige una): lightrag. Cada consulta implica razonamiento del LLM: más latencia y coste por pregunta que una búsqueda vectorial. Sin base vectorial no significa sin modelo ni coste; su adaptador Claude es integración del proyecto y no una aprobación universal de planes.

### Meilisearch (`meilisearch`)

- **Repo:** https://github.com/meilisearch/meilisearch · MIT · nivel 1 · 58/100
- **Qué es:** Motor de búsqueda de código abierto de Meili SAS. La Community Edition es MIT; la Enterprise Edition añade sharding y otras funciones bajo licencia comercial o Business Source License 1.1. Proyecto muy popular y maduro con nube gestionada.
- **Cuándo elegirlo:** Casos: añadir búsqueda instantánea con facetas a una web o aplicación; combinar búsqueda por palabras y semántica como capa de recuperación para RAG.
- **Requisitos:** nivel 1: preparación sencilla; Rust, Cargo.toml, Dockerfile; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -it --rm -p 7700:7700 -v $(pwd)/meili_data:/meili_data getmeili/meilisearch:latest` — fuente: https://github.com/meilisearch/meilisearch/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca Meilisearch con Docker o el script de instalación, sube un JSON de ejemplo y busca con una errata. Éxito: La búsqueda devuelve los documentos correctos en milisegundos pese a la errata.
- **Combina con:** `ollama` [8/motores], `langchain` [3/py], `firecrawl` [4/crawlers]
- **Riesgos y avisos:** BSL (source-available): no es OSI; revisa usos comerciales y la fecha de cambio de licencia. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Revisa la licencia antes de usar funciones Enterprise en producción.

### txtai (`txtai`)

- **Repo:** https://github.com/neuml/txtai · Apache-2.0 · nivel 2 · 58/100
- **Qué es:** Framework de código abierto (Apache-2.0) de NeuML, mantenido de forma continua desde 2020. Requiere Python 3.11 o superior.
- **Cuándo elegirlo:** Casos: indexar documentos y hacer búsqueda semántica con SQL en local; montar un RAG o un grafo de conocimiento sin desplegar varios servicios.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml, setup.py; hardware model_dependent; API de IA: opcional; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install txtai` — fuente: https://github.com/neuml/txtai/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install txtai`, indexa unas frases y busca por significado. Éxito: La búsqueda devuelve las frases más parecidas aunque no compartan palabras.
- **Combina con:** `transformers` [24/entrenamiento], `litellm` [23/serving], `llama-cpp` [8/motores], `claude-code` [20/terminal]
- **Riesgos y avisos:** Alternativas cercanas en el catálogo: llama-index, haystack.

### graphrag (`graphrag`)

- **Repo:** https://github.com/microsoft/graphrag · MIT · nivel 2 · 55/100 · alternativa en «RAG con grafos e índices de conocimiento»
- **Qué es:** Proyecto de investigación de Microsoft Research (MIT) que usa grafos de conocimiento para construir el contexto de respuesta de un LLM. Publicado en julio de 2024; según su README está mayormente en modo mantenimiento: no acepta PR ni…
- **Cuándo elegirlo:** Casos: Estudiar relaciones de un corpus; Comparar búsqueda local y resumen global.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python según guía; modelo y embeddings; corpus pequeño; presupuesto de indexación; hardware prerequisites; API de IA: depends; Python según guía; modelo y embeddings; corpus pequeño; presupuesto de indexación.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install graphrag` — fuente: https://github.com/microsoft/graphrag/blob/main/docs/get_started.md
- **Primera prueba propuesta (no ejecutada):** Indexa unos textos ficticios y pregunta por un tema que conecte varios de ellos Éxito: Puedes revisar entidades, comunidades y fuentes de la respuesta
- **Combina con:** `litellm` [23/serving], `mcp-neo4j` [5/servidores], `docling` [13/conversion], `graphify` [7/codigo], `scrapegraph-ai` [4/llm], `kotaemon`
- **Alternativas:** `ragflow`, `lightrag`, `pageindex`, `graphiti`, `cognee`
- **Riesgos y avisos:** Alternativas (elige una): graphiti, cognee, lightrag. Por su estado de mantenimiento, evalúa lightrag para proyectos nuevos. Proyecto de investigación en mantenimiento: el autor no prevé nuevas funciones ni nuevas PRs, aunque mantiene correcciones y dependencias.

### Chonkie (`chonkie`)

- **Repo:** https://github.com/feyninc/chonkie · MIT · nivel 2 · 51/100
- **Qué es:** Divide textos largos en fragmentos para indexarlos o recuperarlos, con estrategias simples y opciones basadas en modelos.
- **Cuándo elegirlo:** Casos: Dividir un manual por bloques para una búsqueda posterior.; Comparar fragmentos por tamaño fijo con los de una estrategia semántica.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, Dockerfile, docker-compose.yml, pyproject.toml; API de IA: opcional; Entorno Python y un archivo de texto sintético..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.chonkie.ai
- **Primera prueba propuesta (no ejecutada):** Instala la variante básica y divide dos párrafos de prueba con una estrategia simple. Éxito: Obtienes fragmentos cuyo contenido y tamaño se pueden comprobar.
- **Riesgos y avisos:** El corte básico no necesita IA. Algunos fragmentadores, modelos o la API alojada tienen dependencias, credenciales y costes propios.

### agentic-rag-for-dummies (`agentic-rag-for-dummies`)

- **Repo:** https://github.com/GiovanniPasq/agentic-rag-for-dummies · MIT · nivel 2 · 47/100
- **Qué es:** Proyecto educativo de código abierto (MIT) de Giovanni Pasqualino que enseña a construir un sistema de RAG agéntico modular con LangGraph. Activo (v2.3.1), con cuaderno interactivo y proyecto ejecutable.
- **Cuándo elegirlo:** Casos: Aprender RAG por pasos; Comparar un pipeline local con otro proveedor.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; checkout; Ollama local; PDFs propios; Jupyter para notebook; hardware prerequisites; API de IA: depends; Python; checkout; Ollama local; PDFs propios; Jupyter para notebook.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -r requirements.txt` — fuente: https://github.com/GiovanniPasq/agentic-rag-for-dummies/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Coloca un PDF breve en docs y pregunta por un dato de una página concreta Éxito: Puedes ver documentos recuperados y aclarar una consulta ambigua
- **Combina con:** `langgraph` [3/py], `ollama` [8/motores], `qdrant` [6/vectores], `langfuse` [23/observabilidad], `ragas` [23/observabilidad]
- **Riesgos y avisos:** Es material de aprendizaje y referencia, no un producto para producción. No confundas instalar langchain-openai con completar todo el proyecto; revisa requisitos y la guía de ejecución de la app o notebook.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-6-rag.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «RAG y motores de conocimiento», lee `docs/alexandria/categoria-6-rag.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-6-rag.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
