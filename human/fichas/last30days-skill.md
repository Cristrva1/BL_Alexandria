[🏠 Inicio](../README.md) › [🕷️ Buscar y extraer información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# 🔍 last30days

> Skill para agentes que investiga un tema en Reddit, X, YouTube, HN, Polymarket y la web de los últimos 30 días.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 67.7k | MIT | Python | 2026-06-24 |

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

Busca lo que la gente está diciendo ahora sobre un tema y lo resume con fuentes. Prioriza señales reales como votos, likes y apuestas.

## Por qué destaca

Da a tu agente un pulso actual del tema, no solo resultados de buscador.

## Cómo funciona

Lanza búsquedas en varias plataformas, puntúa resultados por interacción y sintetiza un resumen citado.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/mvanhorn/last30days-skill/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar last30days para mi objetivo y necesito pasos guiados. Lee https://github.com/mvanhorn/last30days-skill/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Tendencias recientes de un producto
- Opinión de la comunidad sobre una herramienta
- Ideas de contenido actuales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres saber qué se dice ahora sobre un tema | necesitas un informe académico; mira `storm` |

**Limitaciones:** Algunas fuentes requieren claves de API.

## Stack y modelos

- **Stack:** Python, Markdown
- **Etiquetas:** `research` `skills` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Agent-Reach](agent-reach.md) | 112k | CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube, GitHub y más sin pagar APIs. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [social-media-research-skills](social-media-research-skills.md) | 6.5k | Skills para investigar publicaciones, comentarios, competidores y anuncios en redes mediante ScrapeCreators. |

## Enlaces

- 🐙 GitHub: [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/mvanhorn/last30days-skill/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
