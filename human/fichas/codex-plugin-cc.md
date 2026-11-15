[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧠 codex-plugin-cc

> Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y tareas delegadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 35.1k | Apache-2.0 | JavaScript | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. Claude Code aloja el plugin y Codex utiliza su propia cuenta o API key. Cada sesión conserva los límites de su proveedor. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y tareas delegadas. Añade comandos de revisión y delegación y conecta Claude Code con el runtime de Codex.

## Por qué destaca

Quieres revisar código con Codex dentro de tu flujo de Claude Code.

## Cómo funciona

Añade comandos de revisión y delegación y conecta Claude Code con el runtime de Codex.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/openai/codex-plugin-cc/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar codex-plugin-cc para mi objetivo y necesito pasos guiados. Lee https://github.com/openai/codex-plugin-cc/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Quieres revisar código con Codex dentro de tu flujo de Claude Code

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres revisar código con Codex dentro de tu flujo de Claude Code | no utilizas un agente o flujo compatible con estas instrucciones |

**Limitaciones:** Requiere acceso a Codex y consume los límites o la facturación de la cuenta configurada.

## Stack y modelos

- **Stack:** JavaScript, Node.js
- **Etiquetas:** `metodologia` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/openai/codex-plugin-cc/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
