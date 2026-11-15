[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧭 BMAD Method

> Metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 55.4k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Organiza el trabajo con IA en roles y documentos (brief, PRD, arquitectura, historias) que el agente de código sigue paso a paso. Útil para proyectos medianos donde los prompts sueltos se pierden.

## Por qué destaca

Muy adoptado en la comunidad; da estructura de equipo ágil a un agente de código.

## Cómo funciona

Instala agentes y flujos en tu proyecto; cada rol produce artefactos que alimentan al siguiente.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar BMAD Method para mi objetivo y necesito pasos guiados. Lee https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Pasar de idea a PRD y arquitectura
- Dividir un proyecto en historias
- Mantener contexto en proyectos largos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un proceso completo de producto a código con agentes | prefieres algo ligero centrado en especificaciones; mira `spec-kit` |

## Stack y modelos

- **Stack:** Markdown, Node.js
- **Etiquetas:** `coding-agent` `skills` `agents`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Spec Kit](spec-kit.md) | 150k | Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. |

## Enlaces

- 🐙 GitHub: [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
