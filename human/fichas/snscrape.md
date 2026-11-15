[🏠 Inicio](../README.md) › [🕷️ Buscar y extraer información web](../categorias/04-scraping-b-squeda-research-web.md) › Redes sociales y descarga de medios

# 🐦 snscrape

> Scraper de redes sociales (Twitter/X, Reddit, Telegram, Instagram, etc.) que recolecta posts y perfiles sin necesidad de APIs oficiales ni claves.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.5k | GPL-3.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve la recolección histórica de datos sociales cuando las APIs de pago no son viables o no existen.

## Por qué destaca

Referencia clásica para datasets sociales históricos sin pagar API, con CLI y librería Python en el mismo paquete. Su fiabilidad depende de los cambios y restricciones de cada plataforma, pero sigue siendo el punto de partida habitual para investigación de medios sociales.

## Cómo funciona

Raspa los endpoints y páginas públicas de cada red, devolviendo los resultados como objetos o JSON desde CLI o como librería, con soporte de rangos de fechas y paginación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/JustAnotherArchivist/snscrape/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar snscrape para mi objetivo y necesito pasos guiados. Lee https://github.com/JustAnotherArchivist/snscrape/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Recolectar posts/tweets para análisis
- Datasets sociales históricos
- Alimentar pipelines de investigación con datos públicos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| recolectas varias redes y no te sirve una API oficial | solo necesitas Instagram (instaloader) o la plataforma ya bloqueó el acceso no oficial |

**Limitaciones:** Muy sensible a cambios de frontend y bloqueos de cada plataforma (Twitter/X endureció el acceso); revisa los ToS antes de usarlo a escala, pues varias redes lo prohíben.

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [instaloader](instaloader.md) | 13.9k | Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Agent-Reach](agent-reach.md) | 112k | CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube, GitHub y más sin pagar APIs. |

## Enlaces

- 🐙 GitHub: [JustAnotherArchivist/snscrape](https://github.com/JustAnotherArchivist/snscrape)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/JustAnotherArchivist/snscrape/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
