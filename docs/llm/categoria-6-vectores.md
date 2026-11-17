# Alexandría para agentes · Bases vectoriales y búsqueda semántica

Categoría 6 «Memoria, RAG y búsqueda de conocimiento» › subcategoría `vectores`. 8 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=6&sub=vectores · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `milvus` | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de… | 3 Avanzado | 77 | Apache-2.0 (OSI permisiva) | recomendado |
| `qdrant` | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y… | 1 Básico | 65 | Apache-2.0 (OSI permisiva) | alternativa |
| `chroma` | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings… | 1 Básico | 63 | Apache-2.0 (OSI permisiva) | alternativa |
| `lancedb` | Base de datos vectorial embebida sobre el formato columnar Lance: búsqueda… | 2 Intermedio | 62 | Apache-2.0 (OSI permisiva) | alternativa |
| `pgvector` | Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos… | 2 Intermedio | 59 | PostgreSQL (OSI permisiva) | alternativa |
| `weaviate` | Base de datos vectorial nativa de la nube que guarda objetos y vectores, con… | 2 Intermedio | 59 | BSD-3-Clause (open-core) | alternativa |
| `faiss` | Librería de Meta para búsqueda de similitud y clustering de vectores densos, en… | 2 Intermedio | 56 | MIT (OSI permisiva) | alternativa |
| `turbovec` | Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant… | 2 Intermedio | 52 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Milvus (`milvus`)

- **Repo:** https://github.com/milvus-io/milvus · Apache-2.0 · nivel 3 · 77/100 · recomendado en «Bases y librerías vectoriales»
- **Qué es:** Base de datos vectorial de alto rendimiento y escalable, escrita en Go y C++, proyecto de la LF AI & Data Foundation bajo Apache 2.0. Madura y muy activa (v3.0.6), con versión gestionada en Zilliz Cloud.
- **Cuándo elegirlo:** Casos: Buscar productos por similitud; Indexar embeddings a gran escala.
- **Requisitos:** nivel 3: preparación pesada; Python para cliente; servidor o modo local según guía; vectores de prueba; hardware prerequisites; API de IA: no; Python para cliente; servidor o modo local según guía; vectores de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/milvus-io/milvus.git` — fuente: https://github.com/milvus-io/milvus/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una colección, inserta tres vectores y busca uno cercano Éxito: Puedes contrastar el vecino y los metadatos devueltos
- **Combina con:** `anything-llm` [8/workspaces], `lightrag` [6/rag], `llama-index` [3/py], `langchain4j` [3/ts]
- **Alternativas:** `qdrant`, `chroma`, `lancedb`, `pgvector`, `weaviate`, `faiss`
- **Riesgos y avisos:** Alternativas (elige una): qdrant, chroma, pgvector. Pymilvus es el cliente y no toda la infraestructura del servidor; elige explícitamente el modo antes de instalar.

### Qdrant (`qdrant`)

- **Repo:** https://github.com/qdrant/qdrant · Apache-2.0 · nivel 1 · 65/100 · alternativa en «Bases y librerías vectoriales»
- **Qué es:** Qdrant, motor de búsqueda vectorial y base de datos vectorial escrita en Rust, de Qdrant Solutions GmbH. Licencia Apache-2.0. Es madura (~36k estrellas, v1.20.x). También existe como servicio gestionado (Qdrant Cloud, con nivel gratuito).
- **Cuándo elegirlo:** Casos: Guardar embeddings de documentos; Combinar similitud y filtros de metadatos.
- **Requisitos:** nivel 1: preparación sencilla; Docker; vectores y metadatos de prueba; hardware prerequisites; API de IA: no; Docker; vectores y metadatos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -p 6333:6333 qdrant/qdrant` — fuente: https://github.com/qdrant/qdrant/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Inserta tres vectores pequeños con etiquetas y consulta el más parecido con un filtro Éxito: La búsqueda devuelve el registro esperado y respeta el filtro
- **Combina con:** `docling` [13/conversion], `activepieces` [1/motores], `llama-index` [3/py], `langchain` [3/py], `crawl4ai` [4/crawlers]
- **Alternativas:** `milvus`, `chroma`, `lancedb`, `pgvector`, `weaviate`, `faiss`
- **Riesgos y avisos:** Alternativas (elige una): milvus, chroma, pgvector, faiss. Configura autenticación (API key) antes de exponer el puerto 6333. La base vectorial almacena y busca; no genera por sí sola respuestas de un chatbot.

### Chroma (`chroma`)

- **Repo:** https://github.com/chroma-core/chroma · Apache-2.0 · nivel 1 · 63/100 · alternativa en «Bases y librerías vectoriales»
- **Qué es:** Infraestructura de datos de código abierto para IA (base de datos vectorial) de Chroma, con núcleo en Rust bajo Apache 2.0. Muy activa, publica versiones de PyPI y npm cada lunes; ofrece Chroma Cloud como servicio gestionado.
- **Cuándo elegirlo:** Casos: Prototipar búsqueda semántica local; Filtrar fragmentos por metadatos.
- **Requisitos:** nivel 1: preparación sencilla; Python; entorno virtual; dos documentos de prueba; hardware prerequisites; API de IA: no; Python; entorno virtual; dos documentos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install chromadb # python client` — fuente: https://github.com/chroma-core/chroma/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una colección con dos textos y consulta uno de sus temas Éxito: Se devuelve el documento relacionado y su identificador
- **Combina con:** `mempalace` [6/memoria], `anything-llm` [8/workspaces], `langchain` [3/py]
- **Alternativas:** `milvus`, `qdrant`, `lancedb`, `pgvector`, `weaviate`, `faiss`
- **Riesgos y avisos:** Alternativas (elige una): qdrant, pgvector, milvus, faiss. Distingue cliente embebido, servidor y Cloud; para guardar resultados entre reinicios configura persistencia.

### LanceDB (`lancedb`)

- **Repo:** https://github.com/lancedb/lancedb · Apache-2.0 · nivel 2 · 62/100 · alternativa en «Bases y librerías vectoriales»
- **Qué es:** Biblioteca de recuperación embebida de código abierto (Apache-2.0) de LanceDB Inc., con nube y edición empresarial aparte. Activa y en crecimiento.
- **Cuándo elegirlo:** Casos: añadir búsqueda vectorial a una app local sin desplegar un servidor; gestionar datos multimodales y sus embeddings con versiones para entrenamiento.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Rust, Cargo.toml, docker-compose.yml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install lancedb pandas` — fuente: https://github.com/lancedb/lancedb/blob/main/docs/web/quickstart.mdx
- **Primera prueba propuesta (no ejecutada):** Instala el SDK de Python, crea una tabla con vectores de ejemplo y lanza una búsqueda. Éxito: La búsqueda devuelve los vecinos más cercanos y la tabla queda guardada en una carpeta local.
- **Combina con:** `langchain` [3/py], `llama-index` [3/py], `duckdb` [25/datos], `polars` [25/datos]
- **Alternativas:** `milvus`, `qdrant`, `chroma`, `pgvector`, `weaviate`, `faiss`
- **Riesgos y avisos:** Alternativas (elige una): chroma.

### pgvector (`pgvector`)

- **Repo:** https://github.com/pgvector/pgvector · PostgreSQL · nivel 2 · 59/100 · alternativa en «Bases y librerías vectoriales»
- **Qué es:** Extensión de código abierto de PostgreSQL para búsqueda de similitud vectorial, de Andrew Kane. Se distribuye con una licencia de estilo PostgreSQL (GitHub la marca como no estándar); madura y activa (v0.8.7), sin releases en GitHub.
- **Cuándo elegirlo:** Casos: Buscar similitud junto a datos SQL; Filtrar resultados vectoriales por columnas del negocio.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; PostgreSQL; permisos de extensión; paquete o compilación adecuados al sistema; hardware prerequisites; API de IA: no; PostgreSQL; permisos de extensión; paquete o compilación adecuados al sistema.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install pgvector` — fuente: https://github.com/pgvector/pgvector/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Habilita la extensión en una base de prueba y compara tres vectores junto a sus filas Éxito: La consulta devuelve la fila más cercana usando la distancia elegida
- **Combina con:** `supabase` [22/infraestructura], `anything-llm` [8/workspaces], `librechat` [8/chats], `lightrag` [6/rag], `langchain4j` [3/ts]
- **Alternativas:** `milvus`, `qdrant`, `chroma`, `lancedb`, `weaviate`, `faiss`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): qdrant, chroma, milvus. Es una extensión de PostgreSQL; las instrucciones Windows con nmake requieren el entorno de compilación correspondiente.

### Weaviate (`weaviate`)

- **Repo:** https://github.com/weaviate/weaviate · BSD-3-Clause · nivel 2 · 59/100 · alternativa en «Bases y librerías vectoriales»
- **Qué es:** Base de datos vectorial de código abierto de Weaviate B.V. La mayor parte del repositorio es BSD-3-Clause; los archivos de `wl/` pertenecen a la edición Enterprise y requieren clave de licencia. Proyecto maduro con nube gestionada aparte.
- **Cuándo elegirlo:** Casos: montar la búsqueda semántica con filtros de un catálogo o base documental; servir la recuperación de un sistema RAG con búsqueda híbrida.
- **Requisitos:** nivel 2: preparación media; Go, Dockerfile, docker-compose.yml, go.mod, pyproject.toml; hardware model_dependent; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U weaviate-client` — fuente: https://github.com/weaviate/weaviate/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca Weaviate con el Docker Compose del quickstart local, crea una colección y busca con el cliente de Python. Éxito: La consulta híbrida devuelve objetos ordenados por relevancia con sus propiedades.
- **Combina con:** `langchain` [3/py], `llama-index` [3/py], `ollama` [8/motores], `claude-code` [20/terminal]
- **Alternativas:** `milvus`, `qdrant`, `chroma`, `lancedb`, `pgvector`, `faiss`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): qdrant, milvus.

### Faiss (`faiss`)

- **Repo:** https://github.com/facebookresearch/faiss · MIT · nivel 2 · 56/100 · alternativa en «Bases y librerías vectoriales»
- **Qué es:** Biblioteca de Meta (Facebook Research) para búsqueda de similitud y agrupamiento de vectores densos, escrita en C++ con interfaz Python. MIT, madura y activa (v1.16.0); es una biblioteca, no un servidor de base de datos.
- **Cuándo elegirlo:** Casos: Comparar embeddings de imágenes; Experimentar con índices y compresión.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Paquete CPU o GPU compatible con tu sistema; vectores en memoria; hardware prerequisites; API de IA: no; Paquete CPU o GPU compatible con tu sistema; vectores en memoria.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/facebookresearch/faiss/blob/main/INSTALL.md
- **Primera prueba propuesta (no ejecutada):** Construye un índice con cinco vectores y consulta el más cercano a uno conocido Éxito: El resultado coincide con el vecino calculado para la muestra
- **Combina con:** `langchain` [3/py], `llama-index` [3/py], `transformers` [24/entrenamiento]
- **Alternativas:** `milvus`, `qdrant`, `chroma`, `lancedb`, `pgvector`, `weaviate`
- **Riesgos y avisos:** Alternativas (elige una): qdrant, chroma. Al no ser servidor, no trae persistencia, filtros por metadatos ni control de acceso. Es una biblioteca de índices, no una base con panel, autenticación y persistencia automática de una aplicación.

### turbovec (`turbovec`)

- **Repo:** https://github.com/RyanCodrai/turbovec · MIT · nivel 2 · 52/100
- **Qué es:** Índice vectorial en proceso para Python y Rust de Ryan Codrai, MIT, basado en el método TurboQuant de Google Research. Reciente y sin releases formales en GitHub.
- **Cuándo elegirlo:** Casos: Explorar índices vectoriales embebidos; Reducir memoria de una búsqueda local.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; wheel compatible o Rust y maturin para compilar; embeddings de prueba; hardware prerequisites; API de IA: no; Python; wheel compatible o Rust y maturin para compilar; embeddings de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install turbovec` — fuente: https://github.com/RyanCodrai/turbovec/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Indexa un conjunto pequeño y compara vecinos antes y después de cuantizar Éxito: Puedes medir memoria, tiempo y coincidencia en tus propios datos
- **Combina con:** `langchain` [3/py], `llama-index` [3/py], `haystack` [3/py]
- **Riesgos y avisos:** Sus cifras de rendimiento son benchmarks del autor; no predicen el comportamiento de tu máquina o corpus.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-6-vectores.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Bases vectoriales y búsqueda semántica», lee `docs/alexandria/categoria-6-vectores.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-6-vectores.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
