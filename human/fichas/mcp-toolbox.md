[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🧩 MCP Toolbox for Databases

> Servidor MCP de Google para bases de datos: herramientas genéricas listas y un framework para definir consultas seguras para agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.9k | Apache-2.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Servidor MCP de código abierto (Apache-2.0) mantenido por Google (organización googleapis). El repositorio se llamaba genai-toolbox y se renombró a mcp-toolbox; publica versiones frecuentes y SDK oficiales.

## ¿Qué hace?

Conecta agentes, IDE y aplicaciones con bases de datos empresariales en dos modos: como servidor MCP listo con herramientas genéricas (explorar esquemas, consultar datos) para Gemini CLI, Antigravity, Claude Code, Codex u otros clientes, y como framework para definir herramientas específicas y seguras (consultas estructuradas, búsqueda semántica, NL2SQL) para agentes en producción. Soporta PostgreSQL, MySQL, BigQuery, AlloyDB, Spanner, ClickHouse, Elasticsearch y muchas más.

## ¿Cómo lo hace?

Escrito en Go; se instala con Homebrew (`brew install mcp-toolbox`), `go install`, binarios, Docker o `npx @toolbox-sdk/server --config tools.yaml`. Las fuentes y herramientas se declaran en `tools.yaml`; los SDK (`toolbox-core`, `toolbox-langchain`, `toolbox-llamaindex`, npm, Go y Java) cargan esas herramientas en frameworks de agentes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | El README documenta conectar Claude Code a las bases de datos mediante las herramientas genéricas del servidor MCP. | Arranca el servidor con tu tools.yaml; después añádelo como servidor MCP en Claude Code. |
| [Gemini CLI](gemini-cli.md) | Gemini CLI es uno de los clientes documentados para usar el servidor MCP de Toolbox. | Instala Gemini CLI; después configura Toolbox como servidor MCP. |
| [Codex CLI](codex.md) | Codex figura entre los clientes MCP que el README cita para hablar con las bases de datos. | Servidor Toolbox en marcha; después regístralo en la configuración MCP de Codex. |
| [langchain](langchain.md) | El paquete toolbox-langchain carga las herramientas definidas en Toolbox dentro de agentes de LangChain. | Servidor Toolbox primero; después `pip install toolbox-langchain` y carga el conjunto de herramientas. |
| [LlamaIndex](llama-index.md) | El paquete toolbox-llamaindex expone las mismas herramientas a agentes de LlamaIndex. | Servidor Toolbox primero; después `pip install toolbox-llamaindex`. |

**Notas:** Usa credenciales de solo lectura en las primeras pruebas: las herramientas genéricas pueden ejecutar SQL arbitrario.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v1.17.0 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/googleapis/mcp-toolbox/blob/main/README.md) · [2](https://mcp-toolbox.dev/documentation/introduction/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El servidor aporta herramientas a un cliente MCP; el cliente aporta el modelo. Revisar los servicios que usa cada herramienta. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Consumo del agente que ya utilizas. El modelo se consume en el cliente MCP. Programas, licencias y servicios conectados pueden tener requisitos y tarifas independientes. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

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
brew install mcp-toolbox
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/googleapis/mcp-toolbox/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MCP Toolbox for Databases para mi objetivo y necesito pasos guiados. Lee https://github.com/googleapis/mcp-toolbox/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prepara un tools.yaml contra una base de prueba, arranca el servidor y regístralo en tu cliente MCP..

**Qué comprobar:** El cliente lista las herramientas y una consulta de solo lectura devuelve filas de la base de prueba..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- consultar y explorar el esquema de una base PostgreSQL desde tu agente de código
- dar a un agente en producción consultas parametrizadas en lugar de SQL libre

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: consultar y explorar el esquema de una base PostgreSQL desde tu agente de código; dar a un agente en producción consultas parametrizadas en lugar de SQL libre | necesitas un producto autónomo y esta pieza requiere un cliente MCP |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Go, Dockerfile, go.mod
- **Etiquetas:** `mcp` `go` `data` `database`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox)
- 🌐 Web: <https://mcp-toolbox.dev/documentation/introduction/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/googleapis/mcp-toolbox/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
