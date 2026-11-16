[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# ⚙️ Meilisearch

> Motor de búsqueda rápido en Rust con texto completo, búsqueda semántica e híbrida, facetas, tolerancia a erratas y API sencilla.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 59.9k | MIT | Rust | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor de búsqueda de código abierto de Meili SAS. La Community Edition es MIT; la Enterprise Edition añade sharding y otras funciones bajo licencia comercial o Business Source License 1.1. Proyecto muy popular y maduro con nube gestionada.

## ¿Qué hace?

Ofrece búsqueda de texto completo, semántica e híbrida con tolerancia a erratas, facetas, filtros, ordenación, geobúsqueda, sinónimos y multi-tenencia, con respuestas de pocos milisegundos. Según el README funciona con LangChain y MCP para casos de IA.

## ¿Cómo lo hace?

Escrito en Rust; se instala con Docker, `curl -L https://install.meilisearch.com | sh`, paquetes o la nube. Se usa por API REST con SDK oficiales; la búsqueda semántica se activa configurando embedders.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Meilisearch admite Ollama como fuente de embeddings para la búsqueda semántica e híbrida en local. | Ollama con un modelo de embeddings; después configura el embedder de Ollama en el índice. |
| [langchain](langchain.md) | El README indica que Meilisearch funciona con LangChain como almacén para búsqueda y recuperación. | Meilisearch en marcha con una clave; después usa su integración en LangChain. |
| [firecrawl](firecrawl.md) | Firecrawl extrae páginas en Markdown o JSON que se pueden indexar en Meilisearch para buscar en un sitio (combinación por arquitectura). | Rastrea con Firecrawl; después sube los documentos al índice de Meilisearch. |

**Notas:** Revisa la licencia antes de usar funciones Enterprise en producción.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v1.56.2 (2026-11-09) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/meilisearch/meilisearch/blob/main/README.md) · [2](https://www.meilisearch.com/docs/reference/api/settings)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica y las funciones de IA se configuran por separado; activar un proveedor puede añadir credenciales y consumo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | El coste depende del proveedor o la ruta. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/meilisearch/meilisearch/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Meilisearch para mi objetivo y necesito pasos guiados. Lee https://github.com/meilisearch/meilisearch/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca Meilisearch con Docker o el script de instalación, sube un JSON de ejemplo y busca con una errata..

**Qué comprobar:** La búsqueda devuelve los documentos correctos en milisegundos pese a la errata..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- añadir búsqueda instantánea con facetas a una web o aplicación
- combinar búsqueda por palabras y semántica como capa de recuperación para RAG

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: añadir búsqueda instantánea con facetas a una web o aplicación; combinar búsqueda por palabras y semántica como capa de recuperación para RAG | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. La Community Edition es MIT; la Enterprise (sharding y otras funciones) usa licencia comercial o BUSL-1.1 y solo permite uso no productivo sin acuerdo.

## Stack y modelos

- **Stack:** Rust, Cargo.toml, Dockerfile
- **Etiquetas:** `rag` `search` `rust` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [meilisearch/meilisearch](https://github.com/meilisearch/meilisearch)
- 🌐 Web: <https://www.meilisearch.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/meilisearch/meilisearch/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
