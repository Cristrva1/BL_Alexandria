[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 👨‍💻 Gemini CLI

> CLI de Google orientado actualmente a Code Assist empresarial; el README remite el acceso individual a Antigravity CLI.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 109k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Puntuación de calidad** 65/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Gemini CLI, agente de terminal de Google. Licencia Apache-2.0. Tiene ~109k estrellas (v0.68.0), pero su README indica que desde el 18 de junio de 2026 está orientado solo a licencias Gemini Code Assist Standard/Enterprise y Code Assist for GitHub.

## ¿Qué hace?

Ofrece un agente con herramientas de archivos, shell, búsqueda web y MCP en la terminal. El acceso gratuito individual y los planes Google AI Pro/Ultra se trasladaron a Antigravity CLI, y el README advierte que no está optimizado para Gemini 4 ni sirve para hacer benchmarks.

## ¿Cómo lo hace?

Se ejecuta con `npx @google/gemini-cli` o se instala con `npm install -g @google/gemini-cli` o `brew install gemini-cli` (canales stable, preview y nightly). Requiere una licencia empresarial de Code Assist.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Stitch Skills](stitch-skills.md) | Skills de diseño de Google para agentes. (combinación por arquitectura) | Añade las skills al agente. |
| [Context7](context7.md) | Documentación de librerías vía MCP. (combinación por arquitectura) | Configura el MCP de Context7 en `settings.json`. |
| [Google MCP](mcp.md) | Servidores MCP oficiales de Google Cloud. (combinación por arquitectura) | Añade los endpoints MCP a la configuración. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (18). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Agent Skills (Addy Osmani)](agent-skills.md) · [agentmemory](agentmemory.md) · [Awesome Agent Skills](awesome-agent-skills.md) · [Browser Harness](browser-harness.md) · [Chrome DevTools MCP](chrome-devtools-mcp.md) · [ECC](ecc.md) · [Engram](engram.md) · [gemini-skills](gemini-skills.md) · [i-have-adhd](i-have-adhd.md) · [logo-design-skill](logo-design-skill.md) · [MCP Toolbox for Databases](mcp-toolbox.md) · [notebooklm-mcp-cli](notebooklm-mcp-cli.md) · [rtk](rtk.md) · [skills](google-skills.md) · [Spec Kit](spec-kit.md) · [superpowers](superpowers.md) · [The Agency (agency-agents)](agency-agents.md) · [Zed](zed.md)

**Notas:** Alternativas (elige una): claude-code, codex, opencode, antigravity-cli. Para uso individual, Google remite a Antigravity CLI (antigravity-cli).

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.68.0 (2026-11-10) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google-gemini/gemini-cli/blob/main/README.md) · [2](https://antigravity.google/product/antigravity-cli)</sub>

## Ver similares

Grupo **Agentes de programación en terminal**: Gemini CLI ocupa la posición 3 de 9 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OpenCode](opencode.md) ⭐ recomendado | 82 | Si quieres un agente de terminal independiente del proveedor, con TUI cuidada y muchos modelos. |
| 2 | [Codex CLI](codex.md) | 71 | Si tienes ChatGPT Plus/Pro o API de OpenAI y quieres un agente de terminal abierto en Rust con sandbox. |
| 3 | **Gemini CLI** (esta ficha) | 65 | Si trabajas con Google Code Assist empresarial; para uso individual Google remite a Antigravity CLI. |
| 4 | [Qwen Code](qwen-code.md) | 64 | Si quieres un agente de terminal que hable con varios protocolos (OpenAI, Anthropic, Gemini) o con modelos locales. |
| 5 | [goose](goose.md) | 62 | Si quieres un agente local extensible por MCP, con app de escritorio además de la CLI. |
| 6 | [Claude Code](claude-code.md) | 58 | Si usas Claude (Pro/Max o API) y quieres el agente de terminal más maduro con skills, hooks y subagentes. |
| 7 | [MiMo-Code](mimo-code.md) | 50 | Si quieres probar el agente de Xiaomi MiMo con memoria persistente. |
| 8 | [Aider](aider.md) | 49 | Si prefieres pair programming por git: cambios pequeños, commits automáticos y cualquier modelo. |
| 9 | [Antigravity CLI](antigravity-cli.md) | 27 | Si usas Antigravity de Google y quieres su agente desde la terminal. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El README actual lo destina a Code Assist Standard o Enterprise y rutas API o Vertex heredadas; no promete cuota individual gratuita |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Referencia para la herramienta; no es una integración |
| Modelos locales | Modelo local no documentado. El acceso individual y Google AI Pro o Ultra se remiten a Antigravity CLI, un producto separado; sustituye la descripción antigua de cuota gratuita |
| Coste | El coste depende del proveedor o la ruta. El README actual lo destina a Code Assist Standard o Enterprise y rutas API o Vertex heredadas; no promete cuota individual gratuita |
| Equipo | Preparación según la ruta elegida. Node; acceso empresarial Code Assist o credenciales admitidas; proyecto de prueba |

El acceso individual y Google AI Pro o Ultra se remiten a Antigravity CLI, un producto separado; sustituye la descripción antigua de cuota gratuita

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- acceso empresarial Code Assist o credenciales admitidas
- proyecto de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Using npx (no installation required)
npx @google/gemini-cli
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google-gemini/gemini-cli/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Gemini CLI para mi objetivo y necesito pasos guiados. Lee https://github.com/google-gemini/gemini-cli/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee primero el aviso de acceso y comprueba si corresponde este CLI empresarial o Antigravity CLI.

**Qué comprobar:** Puedes elegir el producto de Google apropiado antes de instalar.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar un agente empresarial de Google
- Planificar una migración de CLI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar un agente empresarial de Google; Planificar una migración de CLI | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El acceso individual y Google AI Pro o Ultra se remiten a Antigravity CLI, un producto separado; sustituye la descripción antigua de cuota gratuita

## Stack y modelos

- **Stack:** Node; acceso empresarial Code Assist o credenciales admitidas; proyecto de prueba
- **Etiquetas:** `coding-agent` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |
| [Antigravity CLI](antigravity-cli.md) | 2.8k | Agente de programación de Google para la terminal (agy), con subagentes, MCP y skills; se distribuye en binarios, sin código fuente. |
| [Qwen Code](qwen-code.md) | 30.6k | Agente de código de terminal del equipo Qwen, multiprotocolo (OpenAI, Anthropic, Gemini, Qwen o modelos locales), con skills, subagentes y MCP. |

## Enlaces

- 🐙 GitHub: [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- 🌐 Web: <https://geminicli.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-gemini/gemini-cli/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
