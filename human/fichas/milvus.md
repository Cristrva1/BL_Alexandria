[🏠 Inicio](../README.md) › [🧬 Memoria, conocimiento y operación de IA](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 🧮 Milvus

> Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 46.7k | Apache-2.0 | Go | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Pensada para producción con grandes volúmenes, alta disponibilidad y varios tipos de índices. Tiene una versión ligera para empezar.

## Por qué destaca

Escala horizontal probada en empresas con volúmenes enormes.

## Cómo funciona

Arquitectura distribuida que separa almacenamiento y cómputo, con índices como HNSW, IVF y DiskANN.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/milvus-io/milvus/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Milvus para mi objetivo y necesito pasos guiados. Lee https://github.com/milvus-io/milvus/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Búsqueda semántica a gran escala
- Recomendaciones por similitud
- RAG con millones de documentos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| esperas volúmenes muy grandes de vectores | tu proyecto es pequeño; mira `chroma` o `qdrant` |

## Stack y modelos

- **Stack:** Go, C++, Kubernetes
- **Etiquetas:** `vector-db` `rag` `go` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| [Chroma](chroma.md) | 29.7k | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. |

## Enlaces

- 🐙 GitHub: [milvus-io/milvus](https://github.com/milvus-io/milvus)
- 🌐 Web: <https://milvus.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/milvus-io/milvus/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
