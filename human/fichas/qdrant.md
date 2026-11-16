[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 🧮 Qdrant

> Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 35.6k | Apache-2.0 | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## ¿Qué es?

Qdrant, motor de búsqueda vectorial y base de datos vectorial escrita en Rust, de Qdrant Solutions GmbH. Licencia Apache-2.0. Es madura (~36k estrellas, v1.20.x). También existe como servicio gestionado (Qdrant Cloud, con nivel gratuito).

## ¿Qué hace?

Guarda puntos (vectores con datos JSON asociados) y los busca por similitud aplicando filtros sobre esos datos. Admite vectores densos, dispersos y multivector, búsqueda híbrida con fusión RRF o DBSF, y sirve para RAG, búsqueda semántica, recomendaciones y clasificación.

## ¿Cómo lo hace?

Funciona como servidor (`docker run -p 6333:6333 qdrant/qdrant`) con API REST descrita en OpenAPI 3.0 y una interfaz gRPC, y tiene clientes oficiales en Python, JS/TS, Go, Rust, .NET y Java. Reduce memoria con cuantización y almacenamiento en disco, admite despliegue distribuido y existe Qdrant Edge para correr embebido. Por defecto arranca sin autenticación y abierto a todas las interfaces de red.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Docling](docling.md) | Prepara documentos en Markdown/JSON limpio antes de generar los embeddings que se guardan en Qdrant. | Independientes; Qdrant debe estar en marcha al indexar. |
| [activepieces](activepieces.md) | Activepieces tiene una pieza oficial `qdrant` para usar Qdrant en flujos. | Qdrant en marcha con sus credenciales; después añade la pieza `qdrant` en un flujo de Activepieces. |
| [LlamaIndex](llama-index.md) | Integración documentada como almacén vectorial de LlamaIndex. | Qdrant en marcha y cliente `qdrant-client` en el entorno Python. |
| [langchain](langchain.md) | Integración documentada como vector store de LangChain. | Igual que con LlamaIndex; elige un solo framework para no duplicar la lógica de RAG. |
| [crawl4ai](crawl4ai.md) | Ingesta de páginas web en Markdown fragmentado para indexar. (combinación por arquitectura) | Rastrea, genera embeddings e inserta en Qdrant. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (12). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[agentic-rag-for-dummies](agentic-rag-for-dummies.md) · [Agno](agno.md) · [AnythingLLM](anything-llm.md) · [CAMEL](camel.md) · [crawlee-python](crawlee-python.md) · [Haystack](haystack.md) · [langchain4j](langchain4j.md) · [mem0](mem0.md) · [STORM](storm.md) · [transformers.js](transformers-js.md) · [Unstructured](unstructured.md) · [Xberg (antes Kreuzberg)](xberg.md)

**Notas:** Alternativas (elige una): milvus, chroma, pgvector, faiss. Configura autenticación (API key) antes de exponer el puerto 6333.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.20.1 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/qdrant/qdrant/blob/master/README.md) · [2](https://qdrant.tech/documentation/data-management/docling/) · [3](https://qdrant.tech/documentation/frameworks/llama-index/) · [4](https://qdrant.tech/documentation/frameworks/langchain/) · [5](https://github.com/activepieces/activepieces/tree/main/packages/pieces/community/qdrant)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El servidor no requiere modelo; generar embeddings y Qdrant Cloud pueden costar aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La base vectorial almacena y busca; no genera por sí sola respuestas de un chatbot |
| Coste | Sin pago a un modelo en la ruta básica. El servidor no requiere modelo; generar embeddings y Qdrant Cloud pueden costar aparte |
| Equipo | Preparación según la ruta elegida. Docker; vectores y metadatos de prueba |

La base vectorial almacena y busca; no genera por sí sola respuestas de un chatbot

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- vectores y metadatos de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
docker run -p 6333:6333 qdrant/qdrant
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/qdrant/qdrant/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Qdrant para mi objetivo y necesito pasos guiados. Lee https://github.com/qdrant/qdrant/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inserta tres vectores pequeños con etiquetas y consulta el más parecido con un filtro.

**Qué comprobar:** La búsqueda devuelve el registro esperado y respeta el filtro.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Guardar embeddings de documentos
- Combinar similitud y filtros de metadatos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Guardar embeddings de documentos; Combinar similitud y filtros de metadatos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La base vectorial almacena y busca; no genera por sí sola respuestas de un chatbot

## Stack y modelos

- **Stack:** Docker; vectores y metadatos de prueba
- **Etiquetas:** `vector-db` `rag` `rust` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Milvus](milvus.md) | 46.7k | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. |
| [Chroma](chroma.md) | 29.7k | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. |
| [pgvector](pgvector.md) | 23.7k | Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales. |
| [Faiss](faiss.md) | 41.7k | Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU. |
| [Weaviate](weaviate.md) | 17k | Base de datos vectorial nativa de la nube que guarda objetos y vectores, con búsqueda híbrida, filtros, RAG y vectorización integrada. |

## Enlaces

- 🐙 GitHub: [qdrant/qdrant](https://github.com/qdrant/qdrant)
- 🌐 Web: <https://qdrant.tech>
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/qdrant/qdrant/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
