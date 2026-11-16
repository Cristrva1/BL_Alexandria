[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 🔗 graphrag

> Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 36.6k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 54/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto de investigación de Microsoft Research (MIT) que usa grafos de conocimiento para construir el contexto de respuesta de un LLM. Publicado en julio de 2024; según su README está mayormente en modo mantenimiento: no acepta PR ni funciones nuevas, solo correcciones y actualizaciones de dependencias. No es un producto con soporte oficial.

## ¿Qué hace?

Es una canalización de datos que extrae información estructurada (entidades, relaciones, comunidades y sus resúmenes) de texto no estructurado con LLM y la usa para responder preguntas sobre datos privados, incluidas preguntas globales sobre todo el corpus. Incluye guía de ajuste de prompts, muy recomendada para obtener buenos resultados con datos propios.

## ¿Cómo lo hace?

Paquete Python con CLI (`graphrag init`, indexado y consulta) que llama a los modelos a través de LiteLLM, lo que da acceso a más de 100 proveedores siempre que soporten salida estructurada; se ha probado sobre todo con la serie GPT-4 de OpenAI. El indexado puede ser caro: la documentación pide empezar con poco. Entre versiones menores hay que volver a ejecutar `graphrag init --force` y los cuadernos de migración.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | GraphRAG usa LiteLLM como gestor de modelos según su documentación de configuración. | Define el proveedor y modelo en `settings.yaml`; si usas el proxy de LiteLLM, apunta allí la URL base. |
| [mcp-neo4j](mcp-neo4j.md) | Cargar en Neo4j las tablas de entidades y relaciones generadas y explorarlas con un agente (combinación por arquitectura). | Indexa primero; importa los Parquet resultantes a Neo4j y conecta el MCP con un usuario de solo lectura. |
| [Docling](docling.md) | Convertir PDF y otros formatos a texto antes del indexado, que espera texto, CSV o JSON (combinación por arquitectura). | Convierte primero y deja los archivos en la carpeta de entrada. |
| [graphify](graphify.md) | Combinación recíproca: graphify lo enlaza como «Llevar el análisis de grafos a corpus documentales grandes. (combinación por arquitectura)». | Orden indicado desde graphify: Usa Graphify para el código y GraphRAG para la documentación. |
| [Scrapegraph-ai](scrapegraph-ai.md) | Combinación recíproca: Scrapegraph-ai lo enlaza como «Construir un grafo de conocimiento con los datos extraídos. (combinación por arquitectura)». | Orden indicado desde Scrapegraph-ai: Exporta los resultados como documentos para GraphRAG. |
| [kotaemon](kotaemon.md) | Combinación recíproca: kotaemon lo enlaza como «kotaemon soporta GraphRAG de Microsoft y nano-GraphRAG para preguntas sobre relaciones entre documentos». | Orden indicado desde kotaemon: Instala graphrag o nano-graphrag según el README; después elige ese índice. |

**Notas:** Alternativas (elige una): graphiti, cognee, lightrag. Por su estado de mantenimiento, evalúa lightrag para proyectos nuevos.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.3.0 (2026-10-08) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/microsoft/graphrag/blob/main/README.md) · [2](https://microsoft.github.io/graphrag/get_started/) · [3](https://microsoft.github.io/graphrag/config/models/)</sub>

## Ver similares

Grupo **RAG con grafos e índices de conocimiento**: graphrag ocupa la posición 4 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [RAGFlow](ragflow.md) ⭐ recomendado | 82 | Si quieres un motor de RAG completo con comprensión profunda de documentos e interfaz. |
| 2 | [LightRAG](lightrag.md) | 66 | Si quieres RAG con grafo de conocimiento ligero y rápido de indexar. |
| 3 | [PageIndex](pageindex.md) | 60 | Si quieres RAG sin vectores que razona sobre la tabla de contenidos de documentos largos. |
| 4 | **graphrag** (esta ficha) | 54 | Si necesitas la metodología GraphRAG de Microsoft para preguntas globales sobre un corpus. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La indexación usa LLM y puede ser costosa antes de la primera consulta; calcula un lote pequeño |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Proyecto de investigación en mantenimiento: el autor no prevé nuevas funciones ni nuevas PRs, aunque mantiene correcciones y dependencias |
| Coste | El coste depende del proveedor o la ruta. La indexación usa LLM y puede ser costosa antes de la primera consulta; calcula un lote pequeño |
| Equipo | Preparación según la ruta elegida. Python según guía; modelo y embeddings; corpus pequeño; presupuesto de indexación |

Proyecto de investigación en mantenimiento: el autor no prevé nuevas funciones ni nuevas PRs, aunque mantiene correcciones y dependencias

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python según guía
- modelo y embeddings
- corpus pequeño
- presupuesto de indexación

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://microsoft.github.io/graphrag/get_started/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar graphrag para mi objetivo y necesito pasos guiados. Lee https://microsoft.github.io/graphrag/get_started/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Indexa unos textos ficticios y pregunta por un tema que conecte varios de ellos.

**Qué comprobar:** Puedes revisar entidades, comunidades y fuentes de la respuesta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar relaciones de un corpus
- Comparar búsqueda local y resumen global

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar relaciones de un corpus; Comparar búsqueda local y resumen global | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Proyecto de investigación en mantenimiento: el autor no prevé nuevas funciones ni nuevas PRs, aunque mantiene correcciones y dependencias

## Stack y modelos

- **Stack:** Python según guía; modelo y embeddings; corpus pequeño; presupuesto de indexación
- **Etiquetas:** `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Graphiti](graphiti.md) | 32.8k | Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes. |
| [cognee](cognee.md) | 33.3k | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. |
| [LightRAG](lightrag.md) | 40.7k | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. |

## Enlaces

- 🐙 GitHub: [microsoft/graphrag](https://github.com/microsoft/graphrag)
- 🌐 Web: <https://microsoft.github.io/graphrag/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/graphrag/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
