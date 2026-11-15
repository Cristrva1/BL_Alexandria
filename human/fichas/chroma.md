[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 🧮 Chroma

> Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29.7k | Apache-2.0 | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ruta embebida del ejemplo no pide API; funciones de embeddings elegidas y Chroma Cloud pueden tener costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Distingue cliente embebido, servidor y Cloud; para guardar resultados entre reinicios configura persistencia |
| Coste | Sin pago a un modelo en la ruta básica. La ruta embebida del ejemplo no pide API; funciones de embeddings elegidas y Chroma Cloud pueden tener costes |
| Equipo | Preparación según la ruta elegida. Python; entorno virtual; dos documentos de prueba |

Distingue cliente embebido, servidor y Cloud; para guardar resultados entre reinicios configura persistencia

## Qué puedes hacer con él

Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local.

## Por qué destaca

Usos propuestos: Prototipar búsqueda semántica local; Filtrar fragmentos por metadatos.

## Cómo funciona

Distingue cliente embebido, servidor y Cloud; para guardar resultados entre reinicios configura persistencia

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- entorno virtual
- dos documentos de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
pip install chromadb # python client
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/chroma-core/chroma/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Chroma para mi objetivo y necesito pasos guiados. Lee https://github.com/chroma-core/chroma/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una colección con dos textos y consulta uno de sus temas.

**Qué comprobar:** Se devuelve el documento relacionado y su identificador.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar búsqueda semántica local
- Filtrar fragmentos por metadatos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar búsqueda semántica local; Filtrar fragmentos por metadatos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Distingue cliente embebido, servidor y Cloud; para guardar resultados entre reinicios configura persistencia

## Stack y modelos

- **Stack:** Python; entorno virtual; dos documentos de prueba
- **Etiquetas:** `vector-db` `rag` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| [pgvector](pgvector.md) | 23.7k | Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales. |
| [Milvus](milvus.md) | 46.7k | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. |
| [Faiss](faiss.md) | 41.7k | Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU. |

## Enlaces

- 🐙 GitHub: [chroma-core/chroma](https://github.com/chroma-core/chroma)
- 🌐 Web: <https://www.trychroma.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/chroma-core/chroma/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
