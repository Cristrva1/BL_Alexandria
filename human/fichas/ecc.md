[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🌌 ECC

> Sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 300k | MIT | JavaScript | 2026-11-09 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Qué es

Actúa como capa intermedia entre el modelo y tu sistema, de modo que las acciones del agente pasan por un escudo antes de tocar el filesystem o la shell.

## Por qué destaca

Aporta una capa de seguridad de ejecución poco común en arneses de agentes, orientada a equipos que dan acceso real a su máquina a herramientas como Claude Code o Cursor. Su core en Rust y el soporte multi-agente lo diferencian de los runtimes puramente en Python.

## Cómo funciona

Intercepta y valida las acciones del agente (comandos bash, ficheros, red) mediante un core en Rust con hooks y memoria persistente, y solo las deja proseguir si cumplen la política definida.

## Instalación rápida

`git clone` del repo y compilación del core en Rust más dependencias en TS/Python/Go. Requiere toolchain de Rust y permisos para instalar hooks a nivel de sistema.

## Casos de uso

- Que Claude ejecute comandos bash sin poner en riesgo el sistema
- Memoria persistente y hooks entre sesiones
- Sandbox de agentes con auditoría de cada acción

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| ejecutas agentes con acceso real a tu máquina y necesitas contención | solo haces prompts de chat sin ejecución de código |

## Stack y modelos

- **Stack:** Rust (core), TypeScript, Python, Go
- **Modelos / API:** Claude Code, Cursor, Zed, Codex, Gemini, Copilot.
- **Etiquetas:** `automation` `skills` `javascript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenHands](openhands.md) | 93.1k | Plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). |
| [sandbox](sandbox.md) | 6.3k | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |
| [hermes-agent](hermes-agent.md) | 262k | Entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. |

## Enlaces

- 🐙 GitHub: [affaan-m/ECC](https://github.com/affaan-m/ECC)
- 🌐 Web: <https://ecc.tools>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
