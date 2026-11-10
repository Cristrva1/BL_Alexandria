[🏠 Inicio](../README.md) › [🔌 MCP & Conectividad](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🕸️ mcp-neo4j

> Conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con soporte de despliegue en cloud.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 989 | MIT | Python | 2026-09-09 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Qué es

Resuelve el acceso natural a grafos desde un LLM: el asistente consulta y escribe Cypher sin que tú escribas el glue a mano.

## Por qué destaca

Lo mantiene el equipo Field GenAI de Neo4j Labs y viene contenedorizado y listo para HTTP, lo que facilita llevar grafos a producción con IA. Al ser oficial, sigue el ritmo de las versiones de Neo4j y del propio protocolo MCP.

## Cómo funciona

Expone consultas Cypher y operaciones sobre el grafo (lectura/escritura, esquema) como tools MCP que el cliente invoca mediante el protocolo, devolviendo resultados estructurados al LLM.

## Instalación rápida

`pip install mcp-neo4j-cypher` (o imagen Docker) y registrar el servidor en la config del cliente MCP. Requiere una instancia Neo4j accesible (local o Aura cloud) con credenciales.

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
- **Modelos / API:** Clientes MCP (Claude, Cursor, etc.); Neo4j como backend.
- **Etiquetas:** `mcp` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |
| [awesome-mcp-servers](awesome-mcp-servers.md) | 97.6k | Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. |

## Enlaces

- 🐙 GitHub: [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j)
- 🌐 Web: <https://neo4j.com/developer/genai-ecosystem/model-context-protocol-mcp/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
