[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 👨‍💻 Claude Code

> Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 156k | — | TypeScript | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Claude Code, agente de programación de Anthropic para la terminal, el IDE y la web. Es software propietario: el repo contiene documentación, plugins y seguimiento de issues, y el uso se rige por los Términos Comerciales de Anthropic (GitHub no detecta licencia). Es muy activo (~156k estrellas, v2.1.325).

## ¿Qué hace?

Entiende la base de código, ejecuta tareas rutinarias, explica código y gestiona flujos de git mediante lenguaje natural. Se amplía con skills, plugins, hooks, subagentes y servidores MCP, y tiene SDK para automatización.

## ¿Cómo lo hace?

Se instala con el instalador nativo o `brew install --cask claude-code`; la instalación por npm está obsoleta. Requiere una cuenta de Anthropic (suscripción o API).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [superpowers](superpowers.md) | Biblioteca de skills y flujos para Claude Code. | Instala el plugin desde su marketplace. |
| [Anthropic Skills](anthropic-skills.md) | Skills oficiales de Anthropic. | Añade el marketplace de skills. |
| [claude-mem](claude-mem.md) | Memoria persistente entre sesiones. | Instala el plugin claude-mem. |
| [Context7](context7.md) | Documentación actualizada de librerías vía MCP. | Añade el servidor MCP de Context7. |

**Notas:** Alternativas (elige una): codex, gemini-cli, opencode, goose, antigravity-cli. No es open source.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v2.1.325 (2026-11-13) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/anthropics/claude-code/blob/main/README.md) · [2](https://code.claude.com/docs/en/overview)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El cliente oficial admite suscripción o cuenta Console según ruta; Ollama documenta modelos locales y nube separada |
| Claude Code | Acceso oficial con sesión del plan |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local procede de la integración de Ollama y necesita modelos compatibles con herramientas; las funciones y el acceso no son idénticos a Claude alojado |
| Coste | El coste depende del proveedor o la ruta. El cliente oficial admite suscripción o cuenta Console según ruta; Ollama documenta modelos locales y nube separada |
| Equipo | Preparación según la ruta elegida. Equipo compatible; terminal; cuenta de Claude o proveedor elegido; carpeta de prueba |

La ruta local procede de la integración de Ollama y necesita modelos compatibles con herramientas; las funciones y el acceso no son idénticos a Claude alojado

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Equipo compatible
- terminal
- cuenta de Claude o proveedor elegido
- carpeta de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (powershell):**

```
winget install Anthropic.ClaudeCode
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/anthropics/claude-code/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Claude Code para mi objetivo y necesito pasos guiados. Lee https://github.com/anthropics/claude-code/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala el CLI para tu sistema, comprueba la versión y pide explicar un archivo sin modificarlo.

**Qué comprobar:** Puedes revisar el archivo citado y la configuración de acceso.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Entender código sin editar
- Preparar una propuesta de corrección

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Entender código sin editar; Preparar una propuesta de corrección | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La ruta local procede de la integración de Ollama y necesita modelos compatibles con herramientas; las funciones y el acceso no son idénticos a Claude alojado

## Stack y modelos

- **Stack:** Equipo compatible; terminal; cuenta de Claude o proveedor elegido; carpeta de prueba
- **Etiquetas:** `coding-agent` `agents` `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |
| [Gemini CLI](gemini-cli.md) | 109k | CLI de Google orientado actualmente a Code Assist empresarial; el README remite el acceso individual a Antigravity CLI. |
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |
| [goose](goose.md) | 56.6k | Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. |
| [Antigravity CLI](antigravity-cli.md) | 2.8k | Agente de programación de Google para la terminal (agy), con subagentes, MCP y skills; se distribuye en binarios, sin código fuente. |

## Enlaces

- 🐙 GitHub: [anthropics/claude-code](https://github.com/anthropics/claude-code)
- 🌐 Web: <https://code.claude.com/docs/en/overview>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/anthropics/claude-code/blob/main/README.md)
- [Fuente 2](https://code.claude.com/docs/en/overview)
- [Fuente 3](https://docs.ollama.com/integrations/claude-code)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
