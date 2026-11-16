[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📎 LightRAG

> RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.7k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Sistema RAG «simple y rápido» basado en grafos de conocimiento, del laboratorio HKUDS (Universidad de Hong Kong). MIT y muy activo; la última etiqueta es una release candidate (v1.5.8rc1) y en 2026 absorbió el proyecto multimodal RAG-Anything.

## ¿Qué hace?

Extrae entidades y relaciones de los documentos para construir un grafo y combina recuperación por grafo y por vectores, con reranker, citas, borrado de documentos con regeneración del grafo y procesamiento multimodal (tablas, imágenes, ecuaciones) vía MinerU o Docling. Ofrece cuatro estrategias de troceado, LLM distintos por rol (extracción, consulta, palabras clave, visión), una interfaz web para insertar, consultar y visualizar el grafo, evaluación con RAGAS y trazas con Langfuse.

## ¿Cómo lo hace?

Biblioteca y servidor Python (`pip install "lightrag-hku[api]"`, luego `lightrag-server`) con la WebUI precompilada. Por defecto guarda KV, vectores y grafo en archivos locales, solo apto para pruebas; para producción recomienda PostgreSQL, que cubre los cuatro tipos de almacenamiento, y admite MongoDB, OpenSearch, Neo4j, Milvus y otros. Un asistente despliega embeddings, reranker y almacenamiento con Docker. El modelo de embeddings debe fijarse antes de indexar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [pgvector](pgvector.md) | PostgreSQL (con pgvector para vectores) es el backend recomendado para producción. | PostgreSQL con pgvector primero; configúralo en `.env` antes de indexar. |
| [Ollama](ollama.md) | Modelos locales para extracción, consulta y embeddings. | Ollama primero; usa un modelo con contexto suficiente para la extracción del grafo. |
| [Docling](docling.md) | Servicio de análisis multimodal soportado tras la integración de RAG-Anything. | Arranca el servicio de Docling y apunta LightRAG a él. |
| [langfuse](langfuse.md) | Trazas integradas desde 2025. | Configura las claves de Langfuse en el entorno del servidor. |
| [Ragas](ragas.md) | Evaluación integrada; la API devuelve los contextos recuperados para medir precisión. | Después de tener datos indexados. |
| [DeepTutor](deeptutor.md) | Combinación recíproca: DeepTutor lo enlaza como «Integración nativa de modelos de rol LightRAG». | Orden indicado desde DeepTutor: Configura LightRAG desde ajustes. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (4). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[kotaemon](kotaemon.md) · [Milvus](milvus.md) · [MinerU](mineru.md) · [olmOCR](olmocr.md)

**Notas:** Alternativas (elige una): graphrag, ragflow, pageindex. `lightrag-server` escucha en 0.0.0.0 sin autenticación por defecto: actívala antes de usarlo en red.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.5.8rc1 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/HKUDS/LightRAG/blob/main/README.md)</sub>

## Ver similares

Grupo **RAG con grafos e índices de conocimiento**: LightRAG ocupa la posición 2 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [RAGFlow](ragflow.md) ⭐ recomendado | 82 | Si quieres un motor de RAG completo con comprensión profunda de documentos e interfaz. |
| 2 | **LightRAG** (esta ficha) | 66 | Si quieres RAG con grafo de conocimiento ligero y rápido de indexar. |
| 3 | [PageIndex](pageindex.md) | 60 | Si quieres RAG sin vectores que razona sobre la tabla de contenidos de documentos largos. |
| 4 | [graphrag](graphrag.md) | 54 | Si necesitas la metodología GraphRAG de Microsoft para preguntas globales sobre un corpus. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Indexar y responder pueden llamar varios modelos; admite configuración Ollama; el coste depende de roles, corpus y proveedor |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Configura HOST o autenticación antes de arrancar en red; conserva el mismo modelo de embeddings entre indexación y consulta |
| Coste | El coste depende del proveedor o la ruta. Indexar y responder pueden llamar varios modelos; admite configuración Ollama; el coste depende de roles, corpus y proveedor |
| Equipo | Preparación según la ruta elegida. Python y uv; LLM; embeddings; almacenamiento; configuración .env |

Configura HOST o autenticación antes de arrancar en red; conserva el mismo modelo de embeddings entre indexación y consulta

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- LLM
- embeddings
- almacenamiento
- configuración .env

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Install LightRAG Server as a tool using uv (recommended)
uv tool install "lightrag-hku[api]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/HKUDS/LightRAG/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LightRAG para mi objetivo y necesito pasos guiados. Lee https://github.com/HKUDS/LightRAG/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Indexa un documento ficticio y compara una consulta sobre una entidad con otra sobre sus relaciones.

**Qué comprobar:** Puedes inspeccionar los resultados y las relaciones recuperadas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar relaciones entre conceptos
- Combinar búsqueda de grafos y vectores

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar relaciones entre conceptos; Combinar búsqueda de grafos y vectores | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Configura HOST o autenticación antes de arrancar en red; conserva el mismo modelo de embeddings entre indexación y consulta

## Stack y modelos

- **Stack:** Python y uv; LLM; embeddings; almacenamiento; configuración .env
- **Etiquetas:** `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |
| [RAGFlow](ragflow.md) | 94.2k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. |
| [PageIndex](pageindex.md) | 40.4k | Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos. |

## Enlaces

- 🐙 GitHub: [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)
- 🌐 Web: <https://arxiv.org/abs/2410.05779>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/HKUDS/LightRAG/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
