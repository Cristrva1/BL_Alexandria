[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › SDKs y frameworks para crear MCP

# 🧰 MCP Python SDK

> SDK oficial de Python para crear servidores y clientes del Model Context Protocol.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24.9k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

SDK oficial en Python del Model Context Protocol. Licencia MIT (el proyecto MCP está migrando a Apache-2.0). Es muy usado (~25k estrellas, v2.3.0).

## ¿Qué hace?

Permite crear servidores MCP que exponen herramientas, recursos y prompts a cualquier host, y clientes que se conectan a cualquier servidor. Incluye transportes estándar y la API de alto nivel heredada de FastMCP 1.0. La v2 trae cambios documentados en «What's new in v2».

## ¿Cómo lo hace?

Se instala con `uv add "mcp[cli]"` o `pip install "mcp[cli]"`; el extra `cli` añade los comandos `mcp dev`, `mcp run` y `mcp install`. La documentación está en py.sdk.modelcontextprotocol.io.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [MCP Inspector](mcp-inspector.md) | Probar el servidor durante el desarrollo; `mcp dev` lo usa. | Ejecuta `mcp dev servidor.py`. |
| [Pydantic AI](pydantic-ai.md) | Usar servidores MCP desde agentes Pydantic AI. (combinación por arquitectura) | Conecta el servidor como toolset MCP. |
| [Claude Code](claude-code.md) | Probar el servidor en un agente. (combinación por arquitectura) | Regístralo con `claude mcp add`. |
| [MCP for Beginners](mcp-for-beginners.md) | Combinación recíproca: MCP for Beginners lo enlaza como «SDK oficial usado en los ejemplos de Python». | Orden indicado desde MCP for Beginners: Instala `mcp[cli]` para seguir las lecciones de Python. |

**Notas:** Alternativas (elige una): fastmcp.

Estado en GitHub: activo · último push 2026-11-05 · última versión publicada v2.3.0 (2026-10-02) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md) · [2](https://py.sdk.modelcontextprotocol.io/get-started/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El SDK no necesita API de IA; el agente cliente y las herramientas externas mantienen sus costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La documentación revisada usa MCPServer y ofrece migración v2; no confundas este SDK con FastMCP independiente |
| Coste | Sin pago a un modelo en la ruta básica. El SDK no necesita API de IA; el agente cliente y las herramientas externas mantienen sus costes |
| Equipo | Preparación según la ruta elegida. Python 3.11+; uv; directorio de proyecto |

La documentación revisada usa MCPServer y ofrece migración v2; no confundas este SDK con FastMCP independiente

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.11+
- uv
- directorio de proyecto

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
uv add "mcp[cli]"      # or: pip install "mcp[cli]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MCP Python SDK para mi objetivo y necesito pasos guiados. Lee https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Implementa el servidor add del ejemplo y comprueba su esquema con Inspector.

**Qué comprobar:** Una llamada con dos enteros devuelve su suma.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Conectar una función Python a MCP
- Servir un recurso de texto desde una aplicación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Conectar una función Python a MCP; Servir un recurso de texto desde una aplicación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La documentación revisada usa MCPServer y ofrece migración v2; no confundas este SDK con FastMCP independiente

## Stack y modelos

- **Stack:** Python 3.11+; uv; directorio de proyecto
- **Etiquetas:** `mcp` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [FastMCP](fastmcp.md) | 28.5k | La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. |

## Enlaces

- 🐙 GitHub: [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)
- 🌐 Web: <https://py.sdk.modelcontextprotocol.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
