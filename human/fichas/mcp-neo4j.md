[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🕸️ mcp-neo4j

> Servidores experimentales de Neo4j Labs para consultar grafos, memoria y recursos Aura desde clientes MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 989 | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El conector no necesita modelo propio; Neo4j Aura, base local y agente tienen costes distintos |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Son servidores Neo4j Labs experimentales sin SLA del equipo de producto; el producto oficial Neo4j MCP es otro repositorio |
| Coste | El coste depende del proveedor o la ruta. El conector no necesita modelo propio; Neo4j Aura, base local y agente tienen costes distintos |
| Equipo | Preparación según la ruta elegida. Neo4j; credenciales; APOC para inspección de esquema; servidor elegido |

Son servidores Neo4j Labs experimentales sin SLA del equipo de producto; el producto oficial Neo4j MCP es otro repositorio

## Qué puedes hacer con él

Colección del programa Neo4j Labs, mantenida por el equipo Field GenAI, con servidores para Cypher, memoria, modelado y Aura. Los autores advierten que no tiene SLA ni garantías de compatibilidad del equipo de producto y enlazan un repositorio distinto para el servidor oficial de producto.

## Por qué destaca

Usos propuestos: Consultar relaciones en un grafo; Estudiar memoria de entidades entre sesiones.

## Cómo funciona

Son servidores Neo4j Labs experimentales sin SLA del equipo de producto; el producto oficial Neo4j MCP es otro repositorio

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Neo4j
- credenciales
- APOC para inspección de esquema
- servidor elegido

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/neo4j-contrib/mcp-neo4j/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mcp-neo4j para mi objetivo y necesito pasos guiados. Lee https://github.com/neo4j-contrib/mcp-neo4j/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Consulta el esquema de un grafo ficticio y revisa una consulta Cypher de lectura.

**Qué comprobar:** Obtienes etiquetas y relaciones que coinciden con la base de prueba.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar relaciones en un grafo
- Estudiar memoria de entidades entre sesiones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar relaciones en un grafo; Estudiar memoria de entidades entre sesiones | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Son servidores Neo4j Labs experimentales sin SLA del equipo de producto; el producto oficial Neo4j MCP es otro repositorio

## Stack y modelos

- **Stack:** Neo4j; credenciales; APOC para inspección de esquema; servidor elegido
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

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/neo4j-contrib/mcp-neo4j/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
