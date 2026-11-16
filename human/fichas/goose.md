[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 👨‍💻 goose

> Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 56.6k | Apache-2.0 | Rust | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

goose, agente de IA open source de propósito general (escritorio, CLI y API) escrito en Rust, ahora bajo la organización aaif-goose y con métricas de salud de la Linux Foundation. Licencia Apache-2.0. Es muy activo (~57k estrellas, v1.59.1).

## ¿Qué hace?

Sirve para programar, investigar, escribir, automatizar o analizar datos. Funciona con más de 15 proveedores (Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock…) o con suscripciones existentes, y se extiende con servidores MCP.

## ¿Cómo lo hace?

Hay app nativa para macOS, Linux y Windows, CLI y API para integrarlo. La documentación está en goose-docs.ai.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor local soportado. | Configura Ollama en los proveedores de goose. |
| [Playwright MCP](playwright-mcp.md) | Extensión MCP para controlar el navegador. (combinación por arquitectura) | Añade el MCP como extensión. |
| [GitHub MCP Server](github-mcp-server.md) | Extensión MCP para GitHub. (combinación por arquitectura) | Añade el servidor como extensión. |

**Notas:** Alternativas (elige una): opencode, claude-code, open-interpreter.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.59.1 (2026-11-14) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/aaif-goose/goose/blob/main/README.md) · [2](https://goose-docs.ai)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Documenta API, modelos locales Ollama y agentes ACP con cuentas Claude, ChatGPT o Gemini; aplican límites del servicio elegido |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Los proveedores y extensiones tienen requisitos diferentes; la integración ACP no incluye créditos ni garantiza todas las funciones de cada agente |
| Coste | El coste depende del proveedor o la ruta. Documenta API, modelos locales Ollama y agentes ACP con cuentas Claude, ChatGPT o Gemini; aplican límites del servicio elegido |
| Equipo | Preparación según la ruta elegida. CLI o app; proveedor o agente ACP autenticado; proyecto de prueba |

Los proveedores y extensiones tienen requisitos diferentes; la integración ACP no incluye créditos ni garantiza todas las funciones de cada agente

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- CLI o app
- proveedor o agente ACP autenticado
- proyecto de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://goose-docs.ai/docs/getting-started/installation)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar goose para mi objetivo y necesito pasos guiados. Lee https://goose-docs.ai/docs/getting-started/installation. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un proveedor y solicita resumir una carpeta pequeña antes de añadir extensiones.

**Qué comprobar:** Puedes reconocer herramientas y contexto usados en la respuesta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Automatizar una tarea de desarrollo
- Comparar agentes conectados por ACP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Automatizar una tarea de desarrollo; Comparar agentes conectados por ACP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los proveedores y extensiones tienen requisitos diferentes; la integración ACP no incluye créditos ni garantiza todas las funciones de cada agente

## Stack y modelos

- **Stack:** CLI o app; proveedor o agente ACP autenticado; proyecto de prueba
- **Etiquetas:** `coding-agent` `agents` `mcp` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Open Interpreter](open-interpreter.md) | 68.9k | Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos. |

## Enlaces

- 🐙 GitHub: [aaif-goose/goose](https://github.com/aaif-goose/goose)
- 🌐 Web: <https://goose-docs.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/aaif-goose/goose/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
