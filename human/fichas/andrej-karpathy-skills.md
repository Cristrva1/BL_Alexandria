[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧠 andrej-karpathy-skills

> Guía de 4 principios inspirada en Andrej Karpathy para que tu agente de código responda útil y sin relleno.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 233k | — | — | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Ajusta el comportamiento de tu asistente con principios claros, sin atarte a una herramienta concreta.

## Por qué destaca

Condensa una filosofía conocida en reglas cortas y portables entre herramientas, lo que la hace fácil de adoptar sin atarse a un asistente concreto. Su origen en ideas de Karpathy le da peso frente a listas genéricas de "buenas prácticas".

## Cómo funciona

Se carga como `CLAUDE.md`/instrucciones de sistema que el asistente lee al inicio de la sesión y aplica a cada respuesta. No ejecuta código: es pura directriz de estilo y foco.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar andrej-karpathy-skills para mi objetivo y necesito pasos guiados. Lee https://github.com/multica-ai/andrej-karpathy-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Awesome Claude Code](awesome-claude-code.md) | 58k | Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías. |
| [Context-Engineering](context-engineering.md) | 9.3k | Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso. |

## Enlaces

- 🐙 GitHub: [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
