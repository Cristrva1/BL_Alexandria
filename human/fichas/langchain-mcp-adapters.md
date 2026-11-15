[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › SDKs y frameworks para crear MCP

# 🧰 LangChain MCP Adapters

> Puente que convierte herramientas de servidores MCP en herramientas de LangChain y LangGraph.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.6k | MIT | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

> ⚠️ Archivado en GitHub: ya no recibe cambios.

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El adaptador no requiere modelo; los ejemplos con agentes usan el proveedor configurado y pueden consumir API |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El autor ha trasladado el desarrollo a langchain[mcp] bajo langchain.mcp; revisa la migración antes de iniciar algo nuevo |
| Coste | El coste depende del proveedor o la ruta. El adaptador no requiere modelo; los ejemplos con agentes usan el proveedor configurado y pueden consumir API |
| Equipo | Preparación según la ruta elegida. Python; servidor MCP; modelo solo para un agente LLM |

El autor ha trasladado el desarrollo a langchain[mcp] bajo langchain.mcp; revisa la migración antes de iniciar algo nuevo

## Qué puedes hacer con él

Puente que convierte herramientas de servidores MCP en herramientas de LangChain y LangGraph.

## Por qué destaca

Usos propuestos: Reutilizar herramientas MCP en LangGraph; Conectar dos servidores a un agente propio.

## Cómo funciona

El autor ha trasladado el desarrollo a langchain[mcp] bajo langchain.mcp; revisa la migración antes de iniciar algo nuevo

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- servidor MCP
- modelo solo para un agente LLM

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install langchain-mcp-adapters
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/langchain-ai/langchain-mcp-adapters/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LangChain MCP Adapters para mi objetivo y necesito pasos guiados. Lee https://github.com/langchain-ai/langchain-mcp-adapters/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga una herramienta add de un servidor MCP y llámala como herramienta LangChain.

**Qué comprobar:** Los argumentos y el resultado se conservan al cruzar el adaptador.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Reutilizar herramientas MCP en LangGraph
- Conectar dos servidores a un agente propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Reutilizar herramientas MCP en LangGraph; Conectar dos servidores a un agente propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El autor ha trasladado el desarrollo a langchain[mcp] bajo langchain.mcp; revisa la migración antes de iniciar algo nuevo

## Stack y modelos

- **Stack:** Python; servidor MCP; modelo solo para un agente LLM
- **Etiquetas:** `mcp` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangGraph](langgraph.md) | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mcp-use](mcp-use.md) | 11k | Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. |

## Enlaces

- 🐙 GitHub: [langchain-ai/langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)
- 🌐 Web: <https://docs.langchain.com/oss/python/langchain/mcp>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langchain-ai/langchain-mcp-adapters/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
