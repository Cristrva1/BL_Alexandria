[🏠 Inicio](../README.md) › [🧠 Mejorar tu agente: skills y prompts](../categorias/02-skills-prompts-gu-as-de-agente.md) › Prompts y prompt engineering

# 🎯 prompt-master

> Skill que ayuda a redactar prompts precisos para cualquier herramienta de IA, buscando el mejor resultado sin desperdiciar tokens.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16k | MIT | — | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Te ayuda a escribir mejores prompts con meta-prompting reutilizable, como una capa por encima de cualquier IA.

## Por qué destaca

Es transversal a casi cualquier IA (texto, imagen, video, código), lo que la hace útil como capa de "meta-prompting" reutilizable. Su foco en acertar al primer intento reduce iteraciones y coste.

## Cómo funciona

La skill guía al asistente para clarificar la intención y construir el prompt óptimo, conservando contexto y memoria entre iteraciones. Aplica plantillas y criterios según el tipo de salida buscada (texto, imagen, código).

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/nidhinjs/prompt-master/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar prompt-master para mi objetivo y necesito pasos guiados. Lee https://github.com/nidhinjs/prompt-master/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Acertar el prompt al primer intento
- Retención de contexto y memoria entre iteraciones
- Meta-prompting para imagen y video

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres dejar de re-promptear y acertar antes | ya tienes prompts afinados y estables |

## Stack y modelos

- **Stack:** Markdown/skill
- **Etiquetas:** `skills` `prompts`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [andrej-karpathy-skills](andrej-karpathy-skills.md) | 233k | Guía de 4 principios inspirada en Andrej Karpathy para que tu agente de código responda útil y sin relleno. |

## Enlaces

- 🐙 GitHub: [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/nidhinjs/prompt-master/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
