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
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve las preguntas que requieren conectar entidades dispersas en muchos documentos, donde el RAG clásico falla.

## Por qué destaca

Proyecto de Microsoft Research muy difundido que mejora las respuestas en preguntas que requieren conectar entidades dispersas en muchos documentos. Su enfoque de resumen por comunidades y recuperación local+global es un patrón de referencia en RAG avanzado.

## Cómo funciona

Un LLM extrae entidades y relaciones para construir el grafo, lo resume por comunidades con un LLM y luego responde combinando recuperación local (entidades concretas) y global (temas del corpus) con embeddings.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/microsoft/graphrag/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar graphrag para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/graphrag/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Preguntas complejas sobre un corpus
- Recuperación que entiende relaciones
- Análisis temático de colecciones grandes de documentos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto | un RAG simple basta o el coste de indexado con LLM es prohibitivo |

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [graphify](graphify.md) | 148k | Generador de grafos de conocimiento que mapea código, PDFs, imágenes y video en diagramas interactivos. |
| [mcp-neo4j](mcp-neo4j.md) | 989 | Conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con soporte de despliegue en cloud. |
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

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/microsoft/graphrag/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
