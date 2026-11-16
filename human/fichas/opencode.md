[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 👨‍💻 OpenCode

> Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 227k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

OpenCode, agente de programación open source para la terminal, de Anomaly (organización anomalyco). Licencia MIT. Es uno de los repos más populares del catálogo (~227k estrellas, v1.19.5).

## ¿Qué hace?

Funciona como agente en una TUI, en una app de escritorio (beta) o mediante servidor y SDK. Se conecta a muchos proveedores de modelos, incluidos los locales. Integra LSP, MCP, plugins, skills y agentes configurables (por ejemplo, modos de planificación y construcción).

## ¿Cómo lo hace?

Se instala con `curl -fsSL https://opencode.ai/v2/install | bash`, `npm i -g @opencode/cli`, Homebrew (tap propio o fórmula oficial), Nix o el cask de escritorio. Los proveedores y modelos se configuran en `opencode.json` o desde la TUI.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor local documentado. | Configura Ollama como proveedor en OpenCode. |
| [litellm](litellm.md) | Usar el proxy LiteLLM como proveedor compatible con OpenAI. (combinación por arquitectura) | Añade el proxy como proveedor personalizado. |
| [opencode-manager](opencode-manager.md) | Interfaz web autoalojada para gestionar sesiones de OpenCode. | Instala OpenCode y luego opencode-manager. |
| [T3 Code](t3code.md) | Controlar OpenCode desde web o móvil. | Instala T3 Code con OpenCode presente. |

**Notas:** Alternativas (elige una): claude-code, codex, goose, gemini-cli, aider.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.19.5 (2026-10-28) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/anomalyco/opencode/blob/dev/README.md) · [2](https://opencode.ai/docs/providers/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Admite proveedores por API, ChatGPT Plus o Pro mediante su adaptador y modelos locales con Ollama, LM Studio o vLLM |
| Claude Code | Integración no documentada |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El paquete actual es @opencode/cli; no confundir con el antiguo opencode-ai archivado; la integración ChatGPT no convierte el proyecto en un cliente oficial de Codex |
| Coste | El coste depende del proveedor o la ruta. Admite proveedores por API, ChatGPT Plus o Pro mediante su adaptador y modelos locales con Ollama, LM Studio o vLLM |
| Equipo | Preparación según la ruta elegida. Node para npm; repositorio de prueba; cuenta de proveedor o Ollama |

El paquete actual es @opencode/cli; no confundir con el antiguo opencode-ai archivado; la integración ChatGPT no convierte el proyecto en un cliente oficial de Codex

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node para npm
- repositorio de prueba
- cuenta de proveedor o Ollama

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm i -g @opencode/cli@latest      # or bun/pnpm/yarn
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/anomalyco/opencode/blob/dev/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenCode para mi objetivo y necesito pasos guiados. Lee https://github.com/anomalyco/opencode/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una copia de un proyecto en modo plan y pide que explique su estructura.

**Qué comprobar:** Obtienes una explicación contrastable antes de permitir ediciones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comprender un repositorio nuevo
- Planificar una corrección pequeña

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comprender un repositorio nuevo; Planificar una corrección pequeña | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El paquete actual es @opencode/cli; no confundir con el antiguo opencode-ai archivado; la integración ChatGPT no convierte el proyecto en un cliente oficial de Codex

## Stack y modelos

- **Stack:** Node para npm; repositorio de prueba; cuenta de proveedor o Ollama
- **Etiquetas:** `coding-agent` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |
| [goose](goose.md) | 56.6k | Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. |
| [Gemini CLI](gemini-cli.md) | 109k | CLI de Google orientado actualmente a Code Assist empresarial; el README remite el acceso individual a Antigravity CLI. |
| [Aider](aider.md) | 50.1k | Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos. |

## Enlaces

- 🐙 GitHub: [anomalyco/opencode](https://github.com/anomalyco/opencode)
- 🌐 Web: <https://opencode.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/anomalyco/opencode/blob/dev/README.md)
- [Fuente 2](https://opencode.ai/docs/providers/)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
