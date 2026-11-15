[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🕸️ mcp-neo4j

> Conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con soporte de despliegue en cloud.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 989 | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta. |
| Coste | Consumo del agente que ya utilizas. El modelo se consume en el cliente. Los servicios que la herramienta consulta pueden tener cuentas o tarifas propias. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

Puede conectarse a un cliente con soporte MCP, incluido Claude Code o Codex. Debes configurar el servidor y sus permisos.

## Qué puedes hacer con él

Resuelve el acceso natural a grafos desde un LLM: el asistente consulta y escribe Cypher sin que tú escribas el glue a mano.

## Por qué destaca

Lo mantiene el equipo Field GenAI de Neo4j Labs y viene contenedorizado y listo para HTTP, lo que facilita llevar grafos a producción con IA. Al ser oficial, sigue el ritmo de las versiones de Neo4j y del propio protocolo MCP.

## Cómo funciona

Expone consultas Cypher y operaciones sobre el grafo (lectura/escritura, esquema) como tools MCP que el cliente invoca mediante el protocolo, devolviendo resultados estructurados al LLM.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible.
- Las credenciales del servicio conectado, si las pide el servidor.

1. Instala o configura el servidor según su README.
2. Añade su comando o URL en la configuración MCP de tu cliente.
3. Comprueba que aparecen las herramientas antes de asignar una tarea.

[Instrucciones originales de instalación](https://github.com/neo4j-contrib/mcp-neo4j/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mcp-neo4j para mi objetivo y necesito pasos guiados. Lee https://github.com/neo4j-contrib/mcp-neo4j/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Consultar/escribir grafos Neo4j desde un asistente
- Backends de conocimiento basados en grafo
- Exploración de datos relacionales por lenguaje natural

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas Neo4j con IA y quieres que el asistente hable Cypher | no trabajas con grafos o tu base es relacional pura |

## Stack y modelos

- **Stack:** Python, Docker
- **Etiquetas:** `mcp` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |
| [awesome-mcp-servers](awesome-mcp-servers.md) | 97.7k | Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. |

## Enlaces

- 🐙 GitHub: [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)
- 🌐 Web: <https://neo4j.com/developer/genai-ecosystem/model-context-protocol-mcp/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/neo4j-contrib/mcp-neo4j/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
