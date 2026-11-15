[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

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
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige LLM; infraestructura y generación de vectores se presupuestan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. pymilvus es el cliente y no toda la infraestructura del servidor; elige explícitamente el modo antes de instalar |
| Coste | Sin pago a un modelo en la ruta básica. No exige LLM; infraestructura y generación de vectores se presupuestan aparte |
| Equipo | Preparación según la ruta elegida. Python para cliente; servidor o modo local según guía; vectores de prueba |

pymilvus es el cliente y no toda la infraestructura del servidor; elige explícitamente el modo antes de instalar

## Qué puedes hacer con él

Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores.

## Por qué destaca

Usos propuestos: Buscar productos por similitud; Indexar embeddings a gran escala.

## Cómo funciona

pymilvus es el cliente y no toda la infraestructura del servidor; elige explícitamente el modo antes de instalar

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python para cliente
- servidor o modo local según guía
- vectores de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/milvus-io/milvus/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Milvus para mi objetivo y necesito pasos guiados. Lee https://github.com/milvus-io/milvus/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una colección, inserta tres vectores y busca uno cercano.

**Qué comprobar:** Puedes contrastar el vecino y los metadatos devueltos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Buscar productos por similitud
- Indexar embeddings a gran escala

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Buscar productos por similitud; Indexar embeddings a gran escala | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** pymilvus es el cliente y no toda la infraestructura del servidor; elige explícitamente el modo antes de instalar

## Stack y modelos

- **Stack:** Python para cliente; servidor o modo local según guía; vectores de prueba
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

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/milvus-io/milvus/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
