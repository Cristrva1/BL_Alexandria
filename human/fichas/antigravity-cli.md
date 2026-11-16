[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 🖥️ Antigravity CLI

> Agente de programación de Google para la terminal (agy), con subagentes, MCP y skills; se distribuye en binarios, sin código fuente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.8k | Propietaria (sin licencia en el repositorio) | — | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 27/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

CLI oficial de Google Antigravity (`agy`), producto propietario. El repositorio google-antigravity/antigravity-cli solo contiene README, CHANGELOG, ejemplos y releases con binarios; no publica código fuente ni licencia. La organización de GitHub no está verificada, pero el sitio oficial antigravity.google enlaza la documentación y describe la CLI. Versión 1.5.9 (noviembre de 2026).

## ¿Qué hace?

Agente de programación en la terminal: entiende el código, edita varios archivos con tu permiso, ejecuta comandos, delega tareas en subagentes concurrentes y gestiona plugins, MCP, skills y hooks mediante comandos con barra. Está optimizado para teclado y sesiones SSH remotas y puede exportar sesiones a la app de escritorio Antigravity 2.0.

## ¿Cómo lo hace?

Se instala con los scripts oficiales de antigravity.google (macOS/Linux, PowerShell o CMD) o con los binarios de las releases, y se inicia con `agy`. Comparte el motor de agentes y los ajustes con Antigravity 2.0. Se autentica con el llavero del sistema o con Google Sign-In (en SSH imprime una URL); para empresa se conecta un proyecto de GCP. Por defecto Google recoge los datos de interacción para mejorar el producto (desactivable en ajustes).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [skills](google-skills.md) | El catálogo de skills de Google documenta la instalación en Antigravity CLI con `agy plugin install`. | Instala la CLI, inicia sesión y luego añade los plugins de skills necesarios. |
| [Agentic Awesome Skills (AAS)](antigravity-awesome-skills.md) | Su instalador lista Antigravity CLI (`antigravity-cli`) como destino de instalación de skills. | Instala solo las skills que vayas a usar para no sobrecargar el agente. |
| [Engram](engram.md) | Engram documenta una configuración para Antigravity como cliente MCP de memoria persistente. (combinación por arquitectura) | Instala Engram y registra su servidor MCP; comprueba que la guía aplica a la CLI. |
| [Context7](context7.md) | Context7 aporta documentación actualizada de bibliotecas como servidor MCP, configurable desde los comandos MCP de la CLI. (combinación por arquitectura) | Añade Context7 como servidor MCP tras el primer inicio de sesión. |

**Notas:** Alternativas (elige una): gemini-cli, claude-code, codex. Google remite a Antigravity CLI a las cuentas gratuitas y Google AI Pro/Ultra que antes usaban Gemini CLI. Producto cerrado: revisa los términos de uso y de datos.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada 1.5.9 (2026-11-14) · licencia declarada sin licencia (propietario) (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google-antigravity/antigravity-cli/blob/main/README.md) · [2](https://antigravity.google/product/antigravity-cli) · [3](https://antigravity.google/docs/cli/overview)</sub>

## Ver similares

Grupo **Agentes de programación en terminal**: Antigravity CLI ocupa la posición 9 de 9 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OpenCode](opencode.md) ⭐ recomendado | 82 | Si quieres un agente de terminal independiente del proveedor, con TUI cuidada y muchos modelos. |
| 2 | [Codex CLI](codex.md) | 71 | Si tienes ChatGPT Plus/Pro o API de OpenAI y quieres un agente de terminal abierto en Rust con sandbox. |
| 3 | [Gemini CLI](gemini-cli.md) | 65 | Si trabajas con Google Code Assist empresarial; para uso individual Google remite a Antigravity CLI. |
| 4 | [Qwen Code](qwen-code.md) | 64 | Si quieres un agente de terminal que hable con varios protocolos (OpenAI, Anthropic, Gemini) o con modelos locales. |
| 5 | [goose](goose.md) | 62 | Si quieres un agente local extensible por MCP, con app de escritorio además de la CLI. |
| 6 | [Claude Code](claude-code.md) | 58 | Si usas Claude (Pro/Max o API) y quieres el agente de terminal más maduro con skills, hooks y subagentes. |
| 7 | [MiMo-Code](mimo-code.md) | 50 | Si quieres probar el agente de Xiaomi MiMo con memoria persistente. |
| 8 | [Aider](aider.md) | 49 | Si prefieres pair programming por git: cambios pequeños, commits automáticos y cualquier modelo. |
| 9 | **Antigravity CLI** (esta ficha) | 27 | Si usas Antigravity de Google y quieres su agente desde la terminal. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Inicia sesión con una cuenta de Google (o un proyecto de GCP para empresa); no pide una clave de API propia en la ruta básica. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Acceso oficial con sesión del plan |
| Modelos locales | Modelo local no documentado. No documenta modelos locales. |
| Coste | El coste depende del proveedor o la ruta. Los límites dependen de la cuenta y el plan de Google. Google recoge datos de interacción por defecto (desactivable en ajustes). |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Es la superficie de terminal de Google Antigravity y usa la cuenta y el plan de Google con que inicias sesión.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y una copia de datos o archivos para la primera prueba.

1. Revisa la documentación oficial de la CLI y los términos de uso y datos de Google antes de instalar.
2. Instala la versión para tu sistema desde la guía oficial e inicia `agy` dentro de un proyecto de prueba.
3. Completa el inicio de sesión con Google y pide un cambio acotado; revisa los permisos que concede cada herramienta.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/google-antigravity/antigravity-cli/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://antigravity.google/docs/cli/overview)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Antigravity CLI para mi objetivo y necesito pasos guiados. Lee https://github.com/google-antigravity/antigravity-cli/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inicia agy en un proyecto de prueba y pide renombrar una función con su prueba.

**Qué comprobar:** El cambio aparece en el diff y pediste permiso antes de ejecutar comandos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Pedir cambios a un proyecto desde la terminal o por SSH
- Delegar tareas paralelas en subagentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Pedir cambios a un proyecto desde la terminal o por SSH; Delegar tareas paralelas en subagentes | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Producto propietario: el repositorio solo contiene README, changelog y ejemplos; la organización de GitHub no está verificada, pero el sitio oficial antigravity.google documenta la CLI.

## Stack y modelos

- **Etiquetas:** `coding` `agents` `cli` `google`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Gemini CLI](gemini-cli.md) | 109k | CLI de Google orientado actualmente a Code Assist empresarial; el README remite el acceso individual a Antigravity CLI. |
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |

## Enlaces

- 🐙 GitHub: [google-antigravity/antigravity-cli](https://github.com/google-antigravity/antigravity-cli)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-antigravity/antigravity-cli/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
