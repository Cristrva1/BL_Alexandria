[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 🧮 Faiss

> Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 41.7k | MIT | C++ | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa un LLM ni cobra una API; la variante GPU necesita hardware y dependencias propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una biblioteca de índices, no una base con panel, autenticación y persistencia automática de una aplicación |
| Coste | Sin pago a un modelo en la ruta básica. No usa un LLM ni cobra una API; la variante GPU necesita hardware y dependencias propias |
| Equipo | Preparación según la ruta elegida. Paquete CPU o GPU compatible con tu sistema; vectores en memoria |

Es una biblioteca de índices, no una base con panel, autenticación y persistencia automática de una aplicación

## Qué puedes hacer con él

Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU.

## Por qué destaca

Usos propuestos: Comparar embeddings de imágenes; Experimentar con índices y compresión.

## Cómo funciona

Es una biblioteca de índices, no una base con panel, autenticación y persistencia automática de una aplicación

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Paquete CPU o GPU compatible con tu sistema
- vectores en memoria

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/facebookresearch/faiss/blob/main/INSTALL.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Faiss para mi objetivo y necesito pasos guiados. Lee https://github.com/facebookresearch/faiss/blob/main/INSTALL.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Construye un índice con cinco vectores y consulta el más cercano a uno conocido.

**Qué comprobar:** El resultado coincide con el vecino calculado para la muestra.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comparar embeddings de imágenes
- Experimentar con índices y compresión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comparar embeddings de imágenes; Experimentar con índices y compresión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una biblioteca de índices, no una base con panel, autenticación y persistencia automática de una aplicación

## Stack y modelos

- **Stack:** Paquete CPU o GPU compatible con tu sistema; vectores en memoria
- **Etiquetas:** `vector-db` `python` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Transformers](transformers.md) | 169k | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| [Chroma](chroma.md) | 29.7k | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. |

## Enlaces

- 🐙 GitHub: [facebookresearch/faiss](https://github.com/facebookresearch/faiss)
- 🌐 Web: <https://faiss.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/facebookresearch/faiss/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
