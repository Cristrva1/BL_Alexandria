[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 📐 design.md

> Formato para describir una identidad visual a agentes de código con tokens YAML y prosa.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28.9k | Apache-2.0 | TypeScript | 2026-06-24 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

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

Resuelve la inconsistencia de marca cuando varias personas o agentes tocan la UI.

## Por qué destaca

Propuesta de Google Labs que aporta no solo los valores sino el "por qué" y cómo aplicarlos, algo que un simple archivo de tokens no transmite. Al ser un formato declarativo, funciona con cualquier agente que lea Markdown.

## Cómo funciona

Archivo Markdown/YAML que el agente lee como contexto persistente, combinando tokens de diseño (color, tipografía, espaciado) con guías en prosa sobre cuándo usarlos.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/google-labs-code/design.md/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar design.md para mi objetivo y necesito pasos guiados. Lee https://github.com/google-labs-code/design.md/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Dar al agente un sistema de diseño persistente
- Mantener coherencia de marca entre varios contribuyentes
- Onboarding rápido de estilo para nuevos agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres consistencia de marca con IA y usas agentes para UI | no usas agentes para generar código de UI |

## Stack y modelos

- **Stack:** Markdown/YAML
- **Etiquetas:** `skills` `design` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [impeccable](impeccable.md) | 110k | Guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio. |

## Enlaces

- 🐙 GitHub: [google-labs-code/design.md](https://github.com/google-labs-code/design.md)
- 🌐 Web: <https://stitch.withgoogle.com/docs/design-md/specification>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/google-labs-code/design.md/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
