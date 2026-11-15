[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 🧮 pgvector

> Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.7k | NOASSERTION | C | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere modelo; PostgreSQL, hosting y generación de embeddings son recursos separados |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una extensión de PostgreSQL; las instrucciones Windows con nmake requieren el entorno de compilación correspondiente |
| Coste | Sin pago a un modelo en la ruta básica. No requiere modelo; PostgreSQL, hosting y generación de embeddings son recursos separados |
| Equipo | Preparación según la ruta elegida. PostgreSQL; permisos de extensión; paquete o compilación adecuados al sistema |

Es una extensión de PostgreSQL; las instrucciones Windows con nmake requieren el entorno de compilación correspondiente

## Qué puedes hacer con él

Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales.

## Por qué destaca

Usos propuestos: Buscar similitud junto a datos SQL; Filtrar resultados vectoriales por columnas del negocio.

## Cómo funciona

Es una extensión de PostgreSQL; las instrucciones Windows con nmake requieren el entorno de compilación correspondiente

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- PostgreSQL
- permisos de extensión
- paquete o compilación adecuados al sistema

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/pgvector/pgvector/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar pgvector para mi objetivo y necesito pasos guiados. Lee https://github.com/pgvector/pgvector/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Habilita la extensión en una base de prueba y compara tres vectores junto a sus filas.

**Qué comprobar:** La consulta devuelve la fila más cercana usando la distancia elegida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Buscar similitud junto a datos SQL
- Filtrar resultados vectoriales por columnas del negocio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Buscar similitud junto a datos SQL; Filtrar resultados vectoriales por columnas del negocio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una extensión de PostgreSQL; las instrucciones Windows con nmake requieren el entorno de compilación correspondiente

## Stack y modelos

- **Stack:** PostgreSQL; permisos de extensión; paquete o compilación adecuados al sistema
- **Etiquetas:** `vector-db` `postgres` `rag`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| [Chroma](chroma.md) | 29.7k | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. |

## Enlaces

- 🐙 GitHub: [pgvector/pgvector](https://github.com/pgvector/pgvector)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pgvector/pgvector/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
