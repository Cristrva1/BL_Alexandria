[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 🖥️ Qwen Code

> Agente de código de terminal del equipo Qwen, multiprotocolo (OpenAI, Anthropic, Gemini, Qwen o modelos locales), con skills, subagentes y MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.6k | Apache-2.0 | TypeScript | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Agente de código de código abierto (Apache-2.0) del equipo Qwen de Alibaba, derivado de Gemini CLI. Muy activo.

## ¿Qué hace?

Trabaja en el repositorio desde la terminal, la app de escritorio o el editor: lee y edita archivos, ejecuta comandos, usa memoria automática, skills, subagentes y MCP, y ofrece funciones experimentales como equipos de agentes y un daemon (`qwen serve`) sobre ACP.

## ¿Cómo lo hace?

Se instala con npm (Node.js) y se configura con el proveedor de modelos; cambia de proveedor en ejecución. Se integra con VS Code, Zed y JetBrains y con clientes de chat.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Zed](zed.md) | Qwen Code documenta su integración con Zed como agente externo. | Instala Qwen Code; después configúralo como agente en Zed. |
| [Ollama](ollama.md) | Qwen Code admite modelos locales servidos por Ollama. | Ollama con un modelo de código; después configúralo como proveedor. |
| [vLLM](vllm.md) | vLLM puede servir un modelo Qwen local que Qwen Code consume por API compatible. | Lanza vLLM; después apunta Qwen Code a su endpoint. |
| [OpenClaw](openclaw.md) | El README enlaza Qwen Code Claw (openclaw/acpx) para que otros agentes deleguen tareas de código en Qwen Code por ACP. | Instala Qwen Code; después configura acpx en OpenClaw. |

**Notas:** Alternativas (elige una): gemini-cli, del que deriva.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada sdk-typescript-v0.1.34 (2026-11-15) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/QwenLM/qwen-code/blob/main/README.md) · [2](https://qwenlm.github.io/qwen-code-docs/en/users/overview) · [3](https://qwenlm.github.io/qwen-code-docs/en/users/integration-zed/)</sub>

## Ver similares

Grupo **Agentes de programación en terminal**: Qwen Code ocupa la posición 4 de 9 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OpenCode](opencode.md) ⭐ recomendado | 82 | Si quieres un agente de terminal independiente del proveedor, con TUI cuidada y muchos modelos. |
| 2 | [Codex CLI](codex.md) | 71 | Si tienes ChatGPT Plus/Pro o API de OpenAI y quieres un agente de terminal abierto en Rust con sandbox. |
| 3 | [Gemini CLI](gemini-cli.md) | 65 | Si trabajas con Google Code Assist empresarial; para uso individual Google remite a Antigravity CLI. |
| 4 | **Qwen Code** (esta ficha) | 64 | Si quieres un agente de terminal que hable con varios protocolos (OpenAI, Anthropic, Gemini) o con modelos locales. |
| 5 | [goose](goose.md) | 62 | Si quieres un agente local extensible por MCP, con app de escritorio además de la CLI. |
| 6 | [Claude Code](claude-code.md) | 58 | Si usas Claude (Pro/Max o API) y quieres el agente de terminal más maduro con skills, hooks y subagentes. |
| 7 | [MiMo-Code](mimo-code.md) | 50 | Si quieres probar el agente de Xiaomi MiMo con memoria persistente. |
| 8 | [Aider](aider.md) | 49 | Si prefieres pair programming por git: cambios pequeños, commits automáticos y cualquier modelo. |
| 9 | [Antigravity CLI](antigravity-cli.md) | 27 | Si usas Antigravity de Google y quieres su agente desde la terminal. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
npm install -g @qwen-code/qwen-code@latest
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/QwenLM/qwen-code/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Qwen Code para mi objetivo y necesito pasos guiados. Lee https://github.com/QwenLM/qwen-code/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `npm install -g @qwen-code/qwen-code@latest`, configura un proveedor y pídele que resuma tu repositorio..

**Qué comprobar:** El agente lee el código y devuelve un resumen con los módulos principales..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- pedir desde la terminal cambios y pruebas en un repositorio
- usar un modelo local o de Qwen como agente de código sin depender de un único proveedor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: pedir desde la terminal cambios y pruebas en un repositorio; usar un modelo local o de Qwen como agente de código sin depender de un único proveedor | necesitas una herramienta estable y auditada para datos sensibles |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, package.json
- **Etiquetas:** `coding` `agent` `cli` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Gemini CLI](gemini-cli.md) | 109k | CLI de Google orientado actualmente a Code Assist empresarial; el README remite el acceso individual a Antigravity CLI. |

## Enlaces

- 🐙 GitHub: [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)
- 🌐 Web: <https://qwenlm.github.io/qwen-code-docs/en/users/overview>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/QwenLM/qwen-code/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
