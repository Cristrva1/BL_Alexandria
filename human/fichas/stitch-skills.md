[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎯 Stitch Skills

> Colección de skills de agente para trabajar con el servidor MCP de Google Stitch.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.9k | Apache-2.0 | TypeScript | 2026-06-24 |

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

Skills en el estándar abierto Agent Skills que enseñan a Claude Code, Codex o Gemini CLI a diseñar con Stitch.

## Por qué destaca

Oficial de Google Labs y compatible con varios agentes.

## Cómo funciona

Carpetas SKILL.md que el agente carga para usar las herramientas MCP de Stitch.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/google-labs-code/stitch-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Stitch Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/google-labs-code/stitch-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Diseñar pantallas desde el agente
- Iterar UI con Stitch
- Pasar diseños a código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas Stitch con un agente de código | no usas Stitch |

## Stack y modelos

- **Stack:** TypeScript, Markdown
- **Etiquetas:** `skills` `design` `ui`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Stitch SDK](stitch-sdk.md) | 1.9k | SDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y capturas por código. |
| [Gemini CLI](gemini-cli.md) | 109k | Agente de IA open source de Google que lleva Gemini a tu terminal, con cuota gratuita generosa. |

## Enlaces

- 🐙 GitHub: [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)
- 🌐 Web: <https://stitch.withgoogle.com/docs/mcp/setup>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/google-labs-code/stitch-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
