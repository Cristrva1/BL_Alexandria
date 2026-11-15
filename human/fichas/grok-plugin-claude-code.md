[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧠 grok-plugin-claude-code

> Plugin de terceros para delegar tareas de Claude Code a Grok CLI mediante comandos y un agente auxiliar.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30 | MIT | JavaScript | 2026-11-14 |

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

Plugin de terceros para delegar tareas de Claude Code a Grok CLI mediante comandos y un agente auxiliar. Envuelve el modo no interactivo de Grok CLI para ejecutar encargos y recuperar sus resultados.

## Por qué destaca

Usas Claude Code y quieres consultar Grok dentro de ese flujo.

## Cómo funciona

Envuelve el modo no interactivo de Grok CLI para ejecutar encargos y recuperar sus resultados.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/zachdunn/grok-plugin-claude-code/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar grok-plugin-claude-code para mi objetivo y necesito pasos guiados. Lee https://github.com/zachdunn/grok-plugin-claude-code/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Usas Claude Code y quieres consultar Grok dentro de ese flujo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas Claude Code y quieres consultar Grok dentro de ese flujo | no utilizas un agente o flujo compatible con estas instrucciones |

**Limitaciones:** Requiere Grok CLI y su autenticación; no es el plugin oficial de Codex.

## Stack y modelos

- **Stack:** JavaScript
- **Etiquetas:** `metodologia` `ai-agents` `claude-code` `grok` `grok-cli` `plugin` `xai` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [zachdunn/grok-plugin-claude-code](https://github.com/zachdunn/grok-plugin-claude-code)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/zachdunn/grok-plugin-claude-code/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
