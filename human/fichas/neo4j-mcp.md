[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🧩 Neo4j MCP (oficial)

> Servidor MCP oficial de Neo4j para que un asistente lea el esquema de un grafo y ejecute consultas Cypher de lectura o escritura.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 307 | GPL-3.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Servidor MCP oficial de Neo4j (organización neo4j, Neo4j Sweden AB), escrito en Go. Licencia GPL-3.0 según LICENSE.txt y NOTICE.txt (GitHub muestra NOASSERTION); si se usa con Aura o con las ediciones comerciales de Neo4j, pasa a regirse por esos contratos. Versión v2.1.1 (noviembre de 2026), ~300 estrellas, activo.

## ¿Qué hace?

Da a un asistente acceso estructurado a una base Neo4j: descubrir etiquetas, relaciones y propiedades (`get-schema`), ejecutar Cypher de solo lectura (`read-cypher`, validado con EXPLAIN), ejecutar escrituras (`write-cypher`, desactivable con `NEO4J_MCP_READ_ONLY=true`) y listar procedimientos de Graph Data Science.

## ¿Cómo lo hace?

Se instala con `pip install neo4j-mcp-server` (la documentación oficial cubre brew e instalación manual; el repositorio incluye un Dockerfile) y se registra como servidor stdio en el cliente MCP con las variables `NEO4J_MCP_URI`, `NEO4J_MCP_USERNAME`, `NEO4J_MCP_PASSWORD` y `NEO4J_MCP_DATABASE`. Requiere una instancia Neo4j accesible (local, Docker o Aura). El propio README advierte que procedimientos mal clasificados como de lectura pueden saltarse el control de solo lectura.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Cliente MCP de terminal; el README cita Claude, Cursor y VS Code como clientes compatibles. (combinación por arquitectura) | Prepara Neo4j, luego registra el servidor con `claude mcp add`. |
| [Codex CLI](codex.md) | Codex admite servidores MCP stdio en su configuración. (combinación por arquitectura) | Añade el servidor en la configuración MCP de Codex tras arrancar Neo4j. |
| [Graphiti](graphiti.md) | Graphiti guarda su grafo de contexto en Neo4j 5.26 (entre otros backends); este servidor permite inspeccionar y consultar ese mismo grafo con Cypher. (combinación por arquitectura) | Instala Neo4j, ejecuta Graphiti y después conecta el servidor MCP en modo solo lectura. |
| [cognee](cognee.md) | Cognee documenta Neo4j como almacén de grafos; el servidor MCP da al agente consultas Cypher directas sobre lo que Cognee construye. (combinación por arquitectura) | Configura Cognee con Neo4j y luego añade el servidor MCP. |

**Notas:** Alternativa (elige una): mcp-neo4j. Es el servidor oficial; mcp-neo4j son los servidores experimentales de Neo4j Labs. Activa `NEO4J_MCP_READ_ONLY` salvo que necesites escribir.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v2.1.1 (2026-11-11) · licencia declarada GPL-3.0 (GitHub: NOASSERTION) (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/neo4j/mcp/blob/main/README.md) · [2](https://github.com/neo4j/mcp/blob/main/NOTICE.txt) · [3](https://neo4j.com/docs/mcp/current/)</sub>

## Ver similares

Grupo **Servidores MCP de Neo4j**: Neo4j MCP (oficial) ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Neo4j MCP (oficial)** (esta ficha) ⭐ recomendado | 60 | Si buscas esto: servidor MCP oficial de Neo4j para que un asistente lea el esquema de un grafo y ejecute consultas Cypher de lectura o escritura. |
| 2 | [mcp-neo4j](mcp-neo4j.md) | 52 | Si buscas esto: servidores experimentales de Neo4j Labs para consultar grafos, memoria y recursos Aura desde clientes MCP. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El servidor aporta herramientas a un cliente MCP; el cliente aporta el modelo. Revisar los servicios que usa cada herramienta. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Consumo del agente que ya utilizas. El modelo se consume en el cliente MCP. Neo4j Aura y las ediciones comerciales tienen sus propias condiciones; con ellas el servidor queda cubierto por esos contratos. |
| Equipo | Preparación según la ruta elegida. Necesitas una base Neo4j (local, Docker o Aura) y credenciales; GDS es opcional. |

Configura este servidor en un cliente MCP compatible, incluido Claude Code o Codex. Sus servicios y permisos se preparan aparte.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible y el programa o servicio que va a controlar la herramienta.

1. Prepara el servidor y sus dependencias siguiendo la configuración del README.
2. Añade el comando o la URL en el cliente MCP y configura los permisos y credenciales de los servicios conectados.
3. Comprueba que aparecen sus herramientas y prueba una consulta pequeña antes de permitir modificaciones.

**Entrada documentada (consulta la sintaxis original):**

```
pip install neo4j-mcp-server
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/neo4j/mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Neo4j MCP (oficial) para mi objetivo y necesito pasos guiados. Lee https://github.com/neo4j/mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta el servidor en modo solo lectura a una base Neo4j de prueba y pide al agente que describa su esquema.

**Qué comprobar:** El agente lista etiquetas y relaciones que coinciden con las de la base.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preguntar en lenguaje natural por el esquema de un grafo de prueba
- Consultar relaciones con Cypher de solo lectura desde el agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preguntar en lenguaje natural por el esquema de un grafo de prueba; Consultar relaciones con Cypher de solo lectura desde el agente | necesitas un producto autónomo y esta pieza requiere un cliente MCP y una base Neo4j |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. GPL-3.0; con Aura o ediciones comerciales de Neo4j aplican sus contratos.

## Stack y modelos

- **Stack:** Go, Dockerfile, go.mod
- **Etiquetas:** `mcp` `graph` `neo4j` `cypher` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mcp-neo4j](mcp-neo4j.md) | 989 | Servidores experimentales de Neo4j Labs para consultar grafos, memoria y recursos Aura desde clientes MCP. |

## Enlaces

- 🐙 GitHub: [neo4j/mcp](https://github.com/neo4j/mcp)
- 🌐 Web: <https://neo4j.com/docs/mcp/current/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/neo4j/mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
