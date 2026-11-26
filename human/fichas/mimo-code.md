[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 🕸️ MiMo-Code

> Asistente de código de Xiaomi MiMo para la terminal con herramientas de archivos, comandos, Git y memoria persistente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.8k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 50/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

MiMoCode, asistente de programación para terminal de Xiaomi MiMo, construido como fork de OpenCode. Licencia MIT. Tiene ~14k estrellas (v0.1.17).

## ¿Qué hace?

Mantiene las capacidades de OpenCode (múltiples proveedores, TUI, LSP, MCP, plugins) y añade memoria persistente, gestión inteligente de contexto, orquestación de subagentes, bucles autónomos guiados por objetivos y checkpoints automáticos. Incluye búsqueda web con Exa o Tavily.

## ¿Cómo lo hace?

Se instala con `curl -fsSL https://mimo.xiaomi.com/install | bash` o PowerShell. Admite cualquier proveedor de LLM y puede usar opcionalmente skills de `.opencode/skills`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [headroom](headroom.md) | Comprimir el contexto en sesiones largas. (combinación por arquitectura) | Envuelve el agente con Headroom si es compatible. |
| [rtk](rtk.md) | Reducir la salida de comandos. (combinación por arquitectura) | Configura los hooks de rtk si son compatibles. |
| [Context7](context7.md) | MiMo Code admite servidores MCP remotos en su configuración `mcp` (el README muestra Exa y Tavily); Context7 aporta documentación actualizada de librerías. (combinación por arquitectura) | Añade Context7 como servidor MCP remoto en la configuración. |

**Notas:** Alternativa (elige una): opencode.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.1.17 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/XiaomiMiMo/MiMo-Code/blob/main/README.md)</sub>

## Ver similares

Grupo **Agentes de programación en terminal**: MiMo-Code ocupa la posición 7 de 9 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OpenCode](opencode.md) ⭐ recomendado | 82 | Si quieres un agente de terminal independiente del proveedor, con TUI cuidada y muchos modelos. |
| 2 | [Codex CLI](codex.md) | 68 | Si tienes ChatGPT Plus/Pro o API de OpenAI y quieres un agente de terminal abierto en Rust con sandbox. |
| 3 | [Gemini CLI](gemini-cli.md) | 65 | Si trabajas con Google Code Assist empresarial; para uso individual Google remite a Antigravity CLI. |
| 4 | [Qwen Code](qwen-code.md) | 64 | Si quieres un agente de terminal que hable con varios protocolos (OpenAI, Anthropic, Gemini) o con modelos locales. |
| 5 | [goose](goose.md) | 62 | Si quieres un agente local extensible por MCP, con app de escritorio además de la CLI. |
| 6 | [Claude Code](claude-code.md) | 58 | Si usas Claude (Pro/Max o API) y quieres el agente de terminal más maduro con skills, hooks y subagentes. |
| 7 | **MiMo-Code** (esta ficha) | 50 | Si quieres probar el agente de Xiaomi MiMo con memoria persistente. |
| 8 | [Aider](aider.md) | 49 | Si prefieres pair programming por git: cambios pequeños, commits automáticos y cualquier modelo. |
| 9 | [Antigravity CLI](antigravity-cli.md) | 24 | Si usas Antigravity de Google y quieres su agente desde la terminal. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Documenta MiMo OAuth, Codex Plus o Pro e importación de autenticación Claude Code además de API; los términos y límites dependen de cada servicio |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Son adaptadores de terceros y la importación de credenciales no demuestra autorización universal del proveedor; no se confirma una ruta local en este README |
| Coste | El coste depende del proveedor o la ruta. Documenta MiMo OAuth, Codex Plus o Pro e importación de autenticación Claude Code además de API; los términos y límites dependen de cada servicio |
| Equipo | Preparación según la ruta elegida. Terminal; cuenta o proveedor admitido; carpeta de prueba |

Son adaptadores de terceros y la importación de credenciales no demuestra autorización universal del proveedor; no se confirma una ruta local en este README

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Terminal
- cuenta o proveedor admitido
- carpeta de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/XiaomiMiMo/MiMo-Code/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MiMo-Code para mi objetivo y necesito pasos guiados. Lee https://github.com/XiaomiMiMo/MiMo-Code/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el primer inicio y comprueba proveedor y modelo antes de pedir explicar un archivo.

**Qué comprobar:** Puedes identificar la ruta de autenticación y revisar la respuesta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un asistente de terminal
- Estudiar memoria y herramientas del proyecto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un asistente de terminal; Estudiar memoria y herramientas del proyecto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Son adaptadores de terceros y la importación de credenciales no demuestra autorización universal del proveedor; no se confirma una ruta local en este README

## Stack y modelos

- **Stack:** Terminal; cuenta o proveedor admitido; carpeta de prueba
- **Etiquetas:** `coding` `ai` `ai-agents` `cli` `mimo` `mimo-code` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |

## Enlaces

- 🐙 GitHub: [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)
- 🌐 Web: <https://mimo.xiaomi.com/mimocode>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/XiaomiMiMo/MiMo-Code/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
