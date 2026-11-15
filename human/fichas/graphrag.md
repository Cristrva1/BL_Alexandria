[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 🔗 graphrag

> Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 36.6k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

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

## Qué puedes hacer con él

Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud.

## Por qué destaca

Usos propuestos: Estudiar relaciones de un corpus; Comparar búsqueda local y resumen global.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [graphify](graphify.md) | 148k | CLI y skill que convierten código y documentos en un grafo consultable; el código se analiza localmente con AST y la extracción semántica tiene rutas separadas. |
| [mcp-neo4j](mcp-neo4j.md) | 989 | Servidores experimentales de Neo4j Labs para consultar grafos, memoria y recursos Aura desde clientes MCP. |
| [turbovec](turbovec.md) | 17.5k | Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida. |

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
