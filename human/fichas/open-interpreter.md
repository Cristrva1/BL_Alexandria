[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de código (terminal e IDE)

# 👨‍💻 Open Interpreter

> Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 68.9k | Apache-2.0 | Rust | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Qué es

Ejecuta código y comandos en tu máquina para cumplir tareas descritas en lenguaje natural. Su versión actual se enfoca en modelos abiertos.

## Por qué destaca

Proyecto pionero que popularizó dejar que un LLM ejecute código en tu equipo.

## Cómo funciona

El modelo genera código o comandos que se ejecutan localmente y su salida vuelve al bucle de conversación.

## Instalación rápida

Sigue la instalación del README (binario de releases o instalador del proyecto).

## Casos de uso

- Automatizar tareas de archivos y datos
- Agente con modelos abiertos baratos
- Prototipos de análisis de datos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un agente que ejecute código usando modelos abiertos | buscas un agente maduro para repos grandes; mira `opencode` |

**Limitaciones:** Ejecuta código en tu máquina: úsalo con aprobación o en un entorno aislado.

## Stack y modelos

- **Stack:** Rust, Python
- **Modelos / API:** Modelos abiertos (Kimi, GLM) y locales; compatible con APIs tipo OpenAI.
- **Etiquetas:** `coding-agent` `local` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [E2B](e2b.md) | 14.8k | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenCode](opencode.md) | 226k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |
| [goose](goose.md) | 56.4k | Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. |

## Enlaces

- 🐙 GitHub: [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter)
- 🌐 Web: <http://openinterpreter.com/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
