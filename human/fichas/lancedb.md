[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 📚 LanceDB

> Base de datos vectorial embebida sobre el formato columnar Lance: búsqueda vectorial, de texto completo y SQL sin servidor que mantener.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.9k | Apache-2.0 | Rust | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de recuperación embebida de código abierto (Apache-2.0) de LanceDB Inc., con nube y edición empresarial aparte. Activa y en crecimiento.

## ¿Qué hace?

Almacena, indexa y busca petabytes de datos multimodales y vectores: búsqueda vectorial, de texto completo y SQL, filtros, versionado automático sin copia y construcción de índices con GPU. Se integra con LangChain, LlamaIndex, Pandas, Polars, DuckDB y más.

## ¿Cómo lo hace?

El motor está escrito en Rust sobre el formato columnar Lance; se usa como biblioteca embebida desde Python, TypeScript o Rust, y guarda datos en disco local o S3/GCS. No requiere servidor.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [langchain](langchain.md) | LanceDB documenta su integración como almacén vectorial de LangChain. | Instala lancedb; después crea el almacén LanceDB en LangChain. |
| [LlamaIndex](llama-index.md) | LanceDB documenta su integración con LlamaIndex para indexar documentos. | Instala lancedb y la integración de LlamaIndex; después crea el índice. |
| [DuckDB](duckdb.md) | LanceDB enumera DuckDB entre sus integraciones para consultar tablas Lance con SQL. | Crea la tabla en LanceDB; después consúltala desde DuckDB. |
| [Polars](polars.md) | LanceDB enumera Polars entre sus integraciones de datos para leer resultados como DataFrames. | Instala polars; después convierte las consultas a DataFrames de Polars. |

**Notas:** Alternativas (elige una): chroma.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.41.0 (2026-10-29) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/lancedb/lancedb/blob/main/README.md) · [2](https://docs.lancedb.com/integrations/ai/langchain)</sub>

## Ver similares

Grupo **Bases y librerías vectoriales**: LanceDB ocupa la posición 4 de 7 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Milvus](milvus.md) ⭐ recomendado | 77 | Si necesitas escala de miles de millones de vectores y despliegue distribuido. |
| 2 | [Qdrant](qdrant.md) | 65 | Si buscas un servidor vectorial rápido en Rust con filtros ricos y buena experiencia local. |
| 3 | [Chroma](chroma.md) | 63 | Si quieres empezar en minutos con una base vectorial embebida para prototipos de RAG. |
| 4 | **LanceDB** (esta ficha) | 62 | Si quieres una base vectorial embebida sobre archivos, sin servidor. |
| 5 | [pgvector](pgvector.md) | 59 | Si ya usas PostgreSQL y quieres vectores en la misma base. |
| 6 | [Weaviate](weaviate.md) | 59 | Si quieres búsqueda híbrida (vectorial + palabras) y módulos de vectorización integrados. |
| 7 | [Faiss](faiss.md) | 56 | Si necesitas una librería de búsqueda de similitud dentro de tu código, en CPU o GPU. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/lancedb/lancedb/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LanceDB para mi objetivo y necesito pasos guiados. Lee https://github.com/lancedb/lancedb/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala el SDK de Python, crea una tabla con vectores de ejemplo y lanza una búsqueda..

**Qué comprobar:** La búsqueda devuelve los vecinos más cercanos y la tabla queda guardada en una carpeta local..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- añadir búsqueda vectorial a una app local sin desplegar un servidor
- gestionar datos multimodales y sus embeddings con versiones para entrenamiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: añadir búsqueda vectorial a una app local sin desplegar un servidor; gestionar datos multimodales y sus embeddings con versiones para entrenamiento | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Rust, Cargo.toml, docker-compose.yml
- **Etiquetas:** `vector-db` `rag` `rust` `library`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Chroma](chroma.md) | 29.7k | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. |

## Enlaces

- 🐙 GitHub: [lancedb/lancedb](https://github.com/lancedb/lancedb)
- 🌐 Web: <https://lancedb.com/docs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/lancedb/lancedb/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
