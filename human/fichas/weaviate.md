[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# ⚙️ Weaviate

> Base de datos vectorial nativa de la nube que guarda objetos y vectores, con búsqueda híbrida, filtros, RAG y vectorización integrada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17k | BSD-3-Clause | Go | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Base de datos vectorial de código abierto de Weaviate B.V. La mayor parte del repositorio es BSD-3-Clause; los archivos de `wl/` pertenecen a la edición Enterprise y requieren clave de licencia. Proyecto maduro con nube gestionada aparte.

## ¿Qué hace?

Almacena objetos junto a sus vectores y combina búsqueda por similitud con filtros por palabra clave y propiedades, búsqueda híbrida, RAG y reordenación. Puede vectorizar automáticamente al importar mediante modelos integrados o aceptar vectores precalculados; escala con replicación y fragmentación.

## ¿Cómo lo hace?

Escrito en Go; se despliega con Docker (`docker compose up -d`), Kubernetes o Weaviate Cloud. Expone REST, GraphQL y gRPC con clientes oficiales (`pip install -U weaviate-client`, TypeScript, Go, Java). Publica además skills para agentes (`npx skills add weaviate/agent-skills`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [langchain](langchain.md) | LangChain mantiene una integración de almacén vectorial para Weaviate (langchain-weaviate). | Weaviate en marcha; después instala langchain-weaviate y crea el almacén. |
| [LlamaIndex](llama-index.md) | LlamaIndex incluye WeaviateVectorStore para indexar y consultar documentos en Weaviate. | Weaviate en marcha; después instala la integración de LlamaIndex. |
| [Ollama](ollama.md) | Weaviate tiene módulos de vectorización y generación con Ollama para trabajar con modelos locales. | Ollama con un modelo de embeddings; después habilita el módulo de Ollama en Weaviate. |
| [Claude Code](claude-code.md) | Weaviate publica skills de agente que se instalan con `npx skills add weaviate/agent-skills` para trabajar con la base desde agentes de código. | Weaviate accesible; después añade las skills al agente. |

**Notas:** Alternativas (elige una): qdrant, milvus.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.40.5 (2026-11-10) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/weaviate/weaviate/blob/main/README.md) · [2](https://docs.weaviate.io/weaviate/model-providers) · [3](https://docs.weaviate.io/deploy/enterprise)</sub>

## Ver similares

Grupo **Bases y librerías vectoriales**: Weaviate ocupa la posición 6 de 7 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Milvus](milvus.md) ⭐ recomendado | 77 | Si necesitas escala de miles de millones de vectores y despliegue distribuido. |
| 2 | [Qdrant](qdrant.md) | 65 | Si buscas un servidor vectorial rápido en Rust con filtros ricos y buena experiencia local. |
| 3 | [Chroma](chroma.md) | 63 | Si quieres empezar en minutos con una base vectorial embebida para prototipos de RAG. |
| 4 | [LanceDB](lancedb.md) | 62 | Si quieres una base vectorial embebida sobre archivos, sin servidor. |
| 5 | [pgvector](pgvector.md) | 59 | Si ya usas PostgreSQL y quieres vectores en la misma base. |
| 6 | **Weaviate** (esta ficha) | 59 | Si quieres búsqueda híbrida (vectorial + palabras) y módulos de vectorización integrados. |
| 7 | [Faiss](faiss.md) | 56 | Si necesitas una librería de búsqueda de similitud dentro de tu código, en CPU o GPU. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (bash):**

```
pip install -U weaviate-client
```

Comando copiado literalmente de el README (sección «Getting started»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/weaviate/weaviate/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Weaviate para mi objetivo y necesito pasos guiados. Lee https://github.com/weaviate/weaviate/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca Weaviate con el Docker Compose del quickstart local, crea una colección y busca con el cliente de Python..

**Qué comprobar:** La consulta híbrida devuelve objetos ordenados por relevancia con sus propiedades..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- montar la búsqueda semántica con filtros de un catálogo o base documental
- servir la recuperación de un sistema RAG con búsqueda híbrida

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: montar la búsqueda semántica con filtros de un catálogo o base documental; servir la recuperación de un sistema RAG con búsqueda híbrida | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. La mayor parte es BSD-3-Clause, pero el código de la carpeta wl/ (edición Enterprise) solo se publica para revisión y requiere licencia.

## Stack y modelos

- **Stack:** Go, Dockerfile, docker-compose.yml, go.mod, pyproject.toml
- **Etiquetas:** `vector-db` `rag` `go` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| [Milvus](milvus.md) | 46.7k | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. |

## Enlaces

- 🐙 GitHub: [weaviate/weaviate](https://github.com/weaviate/weaviate)
- 🌐 Web: <https://weaviate.io/developers/weaviate/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/weaviate/weaviate/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
