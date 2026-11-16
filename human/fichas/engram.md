[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 Engram

> Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.2k | MIT | Go | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Memoria persistente para agentes de código de Gentleman-Programming, de código abierto (MIT) y financiada por donaciones, sin funciones de pago. Muy activa (v3.7.2) y parte del ecosistema Gentle-AI.

## ¿Qué hace?

Da a tu agente una memoria única entre sesiones, local o en la nube, independiente del agente. Tiene 14 destinos de configuración (Claude Code, Pi, OpenCode, Gemini CLI, Codex, Antigravity, Windsurf, Qwen Code, Kiro, Cursor, VS Code Copilot, Kilo Code, Kimi Code, CommandCode) además de cualquier agente compatible con MCP. Permite compartir memoria por Git Sync y replicarla opcionalmente con Engram Cloud.

## ¿Cómo lo hace?

Un único binario en Go sin dependencias, con SQLite y búsqueda de texto completo FTS5, expuesto mediante CLI, API HTTP, MCP (stdio) y una TUI interactiva. Los datos se guardan en `~/.engram` (configurable con `ENGRAM_DATA_DIR`); la base SQLite local es la fuente de verdad y Git Sync exporta fragmentos comprimidos para otras máquinas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Destino de configuración soportado vía MCP. | Instala el binario y ejecuta la configuración para Claude Code. |
| [OpenCode](opencode.md) | Destino de configuración soportado. | Igual que arriba. |
| [Gemini CLI](gemini-cli.md) | Destino de configuración soportado. | Igual que arriba. |
| [DeepSeek Harness (DSH)](deepseek-harness.md) | La guía oficial de DSH incluye una configuración de referencia para conectar Engram como memoria MCP vía `dsh-mcp-client`. | Instala Engram con la versión fijada en la guía de DSH y activa la overlay. |

**Notas:** Alternativas (elige una): claude-mem, agentmemory.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v3.7.2 (2026-11-14) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Gentleman-Programming/engram/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. SQLite y FTS5 no requieren LLM ni API; el agente que interpreta los recuerdos mantiene sus costes |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. MCP no equivale por sí solo a captura automática; Codex añade requisitos de capacidad y sesión que debes revisar en la guía |
| Coste | Sin pago a un modelo en la ruta básica. SQLite y FTS5 no requieren LLM ni API; el agente que interpreta los recuerdos mantiene sus costes |
| Equipo | Preparación según la ruta elegida. Binario oficial o Go; cliente MCP; directorio de memoria de prueba |

MCP no equivale por sí solo a captura automática; Codex añade requisitos de capacidad y sesión que debes revisar en la guía

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario oficial o Go
- cliente MCP
- directorio de memoria de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Gentleman-Programming/engram/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Engram para mi objetivo y necesito pasos guiados. Lee https://github.com/Gentleman-Programming/engram/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Guarda una decisión con su razón y recupérala por palabras clave.

**Qué comprobar:** El registro aparece con contenido y contexto que puedes inspeccionar.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Recordar decisiones técnicas
- Hacer una entrega de contexto entre sesiones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Recordar decisiones técnicas; Hacer una entrega de contexto entre sesiones | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP no equivale por sí solo a captura automática; Codex añade requisitos de capacidad y sesión que debes revisar en la guía

## Stack y modelos

- **Stack:** Binario oficial o Go; cliente MCP; directorio de memoria de prueba
- **Etiquetas:** `memory` `mcp` `coding-agent` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [claude-mem](claude-mem.md) | 117k | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. |
| [agentmemory](agentmemory.md) | 30.4k | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. |

## Enlaces

- 🐙 GitHub: [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)
- 🌐 Web: <https://engram.gentlemanprogramming.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Gentleman-Programming/engram/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
