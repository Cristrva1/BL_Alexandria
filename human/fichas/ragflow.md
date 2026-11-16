[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📎 RAGFlow

> Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 94.2k | Apache-2.0 | Go | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 82/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor RAG (generación aumentada por recuperación) de código abierto (Apache 2.0) de InfiniFlow, que fusiona RAG con capacidades de agente. Muy activo: la versión 1.0.0 salió el 6 de noviembre de 2026 y el código principal está ahora en Go; tiene servicio en la nube opcional.

## ¿Qué hace?

Extrae conocimiento de documentos no estructurados con formatos complejos mediante comprensión profunda de documentos y troceado por plantillas explicables, con citas para reducir alucinaciones. Desde 2026 añade «compilación de conocimiento» (wikis, grafos, árboles, PageIndex, mapas mentales, líneas de tiempo y skills por documento o conjunto), RAG agéntico con cuatro niveles de razonamiento, ingesta de sitios web por sitemap y de Google BigQuery con sincronización incremental.

## ¿Cómo lo hace?

Se despliega con Docker Compose (Docker ≥ 24.0.0, Compose ≥ v2.26.1) y una configuración inicial recomendada de 4 núcleos, 16 GB de RAM y 50 GB de disco; usa MySQL por defecto y un motor de documentos Elasticsearch o Infinity (con Elasticsearch hay que subir `vm.max_map_count` a 262144). La interfaz se sirve en el puerto 80. Desde código requiere Go 1.27, Clang 20, LLD 20 y CMake ≥ 4.0. Admite modelos locales según su guía.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | La guía oficial explica cómo usar modelos locales de Ollama como LLM y embeddings. | Ollama accesible desde los contenedores (no uses localhost); después añade el proveedor en RAGFlow. |
| [activepieces](activepieces.md) | Automatizar la carga de documentos o consultar bases de conocimiento a través de su API HTTP (combinación por arquitectura). | Crea una clave de API en RAGFlow y úsala desde la pieza HTTP de Activepieces. |
| [langfuse](langfuse.md) | Observar las llamadas a LLM de los flujos (combinación por arquitectura; [DATO NO VERIFICADO: integración nativa]). | Langfuse en marcha con claves de proyecto antes de configurarlo. |
| [PaddleOCR](paddleocr.md) | Combinación recíproca: PaddleOCR lo enlaza como «El README cita RAGFlow entre los proyectos que lo integran». | Orden indicado desde PaddleOCR: Revisa en RAGFlow qué versión de PaddleOCR usa antes de mezclar instalaciones. |

**Notas:** Alternativas (elige una): dify, lightrag. El puerto 80 puede chocar con otros servicios web del mismo servidor.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.0.0 (2026-11-06) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/infiniflow/ragflow/blob/main/README.md) · [2](https://ragflow.io/docs/dev/deploy_local_llm) · [3](https://ragflow.io/docs/dev/http_api_reference)</sub>

## Ver similares

Grupo **RAG con grafos e índices de conocimiento**: RAGFlow ocupa la posición 1 de 4 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **RAGFlow** (esta ficha) ⭐ recomendado | 82 | Si quieres un motor de RAG completo con comprensión profunda de documentos e interfaz. |
| 2 | [LightRAG](lightrag.md) | 66 | Si quieres RAG con grafo de conocimiento ligero y rápido de indexar. |
| 3 | [PageIndex](pageindex.md) | 60 | Si quieres RAG sin vectores que razona sobre la tabla de contenidos de documentos largos. |
| 4 | [graphrag](graphrag.md) | 54 | Si necesitas la metodología GraphRAG de Microsoft para preguntas globales sobre un corpus. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. LLM, embeddings y reranker se configuran por separado; modelos locales necesitan recursos adicionales; APIs remotas tienen consumo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Los mínimos del servidor no incluyen necesariamente ejecutar los modelos; prueba pocos documentos antes de ampliar |
| Coste | El coste depende del proveedor o la ruta. LLM, embeddings y reranker se configuran por separado; modelos locales necesitan recursos adicionales; APIs remotas tienen consumo |
| Equipo | Preparación según la ruta elegida. Docker; configuración inicial orientativa 4 CPU,16 GB RAM,50 GB disco; modelos |

Los mínimos del servidor no incluyen necesariamente ejecutar los modelos; prueba pocos documentos antes de ampliar

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- configuración inicial orientativa 4 CPU,16 GB RAM,50 GB disco
- modelos

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker compose -f docker-compose.yml up -d
```

Comando copiado literalmente de el README (sección «🚀 Start up the server»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/infiniflow/ragflow/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar RAGFlow para mi objetivo y necesito pasos guiados. Lee https://github.com/infiniflow/ragflow/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Indexa un PDF propio corto y pregunta por un dato identificable con cita.

**Qué comprobar:** La respuesta permite abrir el fragmento y comprobar su procedencia.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar manuales de una organización
- Combinar documentos en una base de conocimiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar manuales de una organización; Combinar documentos en una base de conocimiento | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los mínimos del servidor no incluyen necesariamente ejecutar los modelos; prueba pocos documentos antes de ampliar

## Stack y modelos

- **Stack:** Docker; configuración inicial orientativa 4 CPU,16 GB RAM,50 GB disco; modelos
- **Etiquetas:** `rag` `docs` `agents` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [dify](dify.md) | 161k | Plataforma integral para construir apps de IA con backend y UI listos. |
| [LightRAG](lightrag.md) | 40.7k | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. |

## Enlaces

- 🐙 GitHub: [infiniflow/ragflow](https://github.com/infiniflow/ragflow)
- 🌐 Web: <https://ragflow.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/infiniflow/ragflow/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
