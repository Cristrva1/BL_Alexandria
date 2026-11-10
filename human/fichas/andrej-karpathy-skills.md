[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧠 andrej-karpathy-skills

> Guía de 4 principios inspirada en Andrej Karpathy para que tu agente de código responda útil y sin relleno.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 232k | — | — | 2026-04-20 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Ajusta el comportamiento de tu asistente con principios claros, sin atarte a una herramienta concreta.

## Por qué destaca

Condensa una filosofía conocida en reglas cortas y portables entre herramientas, lo que la hace fácil de adoptar sin atarse a un asistente concreto. Su origen en ideas de Karpathy le da peso frente a listas genéricas de "buenas prácticas".

## Cómo funciona

Se carga como `CLAUDE.md`/instrucciones de sistema que el asistente lee al inicio de la sesión y aplica a cada respuesta. No ejecuta código: es pura directriz de estilo y foco.

## Instalación rápida

Clona el repo y copia el `CLAUDE.md` (o su contenido) en tu proyecto o en el directorio de configuración del asistente; no requiere dependencias ni claves.

## Casos de uso

- Mejorar señal/ruido del asistente
- Base de buenas prácticas diarias
- Punto de partida para tu propio `CLAUDE.md`

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres respuestas más útiles ya, sin curar prompts largos | buscas skills ejecutables con scripts concretos |

## Stack y modelos

- **Stack:** Markdown (`CLAUDE.md`)
- **Modelos / API:** Claude Code, Cursor, Gemini CLI (agnóstico vía instrucciones de sistema).
- **Etiquetas:** `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Awesome Claude Code](awesome-claude-code.md) | 57.7k | Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías. |
| [Context-Engineering](context-engineering.md) | 9.3k | Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso. |

## Enlaces

- 🐙 GitHub: [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
