[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Video programático y con agentes

# 🎞️ Remotion Agent Skills

> Skills oficiales de Remotion para que tu agente de código cree videos con React.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.1k | — | TypeScript | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

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

Enseñan al agente las buenas prácticas de Remotion: composiciones, animaciones, audio y render.

## Por qué destaca

Oficiales del equipo de Remotion.

## Cómo funciona

Carpetas SKILL.md que el agente carga al trabajar en proyectos Remotion.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

**Comando de entrada documentado:**

```shell
npx skills add remotion-dev/skills
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/remotion-dev/skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Remotion Agent Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/remotion-dev/skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Generar videos con Claude Code
- Animaciones de datos
- Plantillas de video

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| haces videos con Remotion y un agente | no usas Remotion |

## Stack y modelos

- **Stack:** TypeScript, Markdown
- **Etiquetas:** `video` `skills`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [remotion](remotion.md) | 73.2k | Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. |
| [Remotion Superpowers](remotion-superpowers.md) | 168 | Plugin que convierte Remotion en un estudio de video para Claude Code, Codex o Gemini CLI. |

## Enlaces

- 🐙 GitHub: [remotion-dev/skills](https://github.com/remotion-dev/skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/remotion-dev/skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
