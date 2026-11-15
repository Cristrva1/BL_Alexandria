[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de código (terminal e IDE)

# 👨‍💻 Codex CLI

> Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 135k | Apache-2.0 | Rust | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Lee tu repositorio, propone y aplica cambios y ejecuta comandos dentro de un sandbox. Usa AGENTS.md para el contexto del proyecto y admite MCP.

## Por qué destaca

Open source, rápido y con sandbox del sistema operativo por defecto; se integra con ChatGPT y la nube de Codex.

## Cómo funciona

Un CLI en Rust conversa con modelos de OpenAI y ejecuta las herramientas en un sandbox con niveles de aprobación.

## Instalación rápida

`npm i -g @openai/codex` (o `brew install --cask codex`) y ejecuta `codex`.

## Casos de uso

- Corregir bugs desde la terminal
- Generar tests y refactors
- Tareas en paralelo con la nube de Codex

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas ChatGPT u OpenAI y quieres un agente abierto en terminal | trabajas con Claude como modelo principal; mira `claude-code` |

## Stack y modelos

- **Stack:** Rust, TypeScript
- **Modelos / API:** Modelos de OpenAI (GPT/Codex); admite otros proveedores compatibles.
- **Etiquetas:** `coding-agent` `agents` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Agent Skills (Addy Osmani)](agent-skills.md) | 115k | Colección de skills de ingeniería de producción para agentes de código, de Addy Osmani. |
| [Spec Kit](spec-kit.md) | 149k | Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. |
| [Context7](context7.md) | 64.5k | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Gemini CLI](gemini-cli.md) | 109k | Agente de IA open source de Google que lleva Gemini a tu terminal, con cuota gratuita generosa. |
| [OpenCode](opencode.md) | 226k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |

## Enlaces

- 🐙 GitHub: [openai/codex](https://github.com/openai/codex)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
