[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Redes sociales y descarga de medios

# 🐦 snscrape

> Scraper de redes sociales (Twitter/X, Reddit, Telegram, Instagram, etc.) que recolecta posts y perfiles sin necesidad de APIs oficiales ni claves.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 5.5k | GPL-3.0 | Python | 2023-11-15 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Resuelve la recolección histórica de datos sociales cuando las APIs de pago no son viables o no existen.

## Por qué destaca

Referencia clásica para datasets sociales históricos sin pagar API, con CLI y librería Python en el mismo paquete. Su fiabilidad depende de los cambios y restricciones de cada plataforma, pero sigue siendo el punto de partida habitual para investigación de medios sociales.

## Cómo funciona

Raspa los endpoints y páginas públicas de cada red, devolviendo los resultados como objetos o JSON desde CLI o como librería, con soporte de rangos de fechas y paginación.

## Instalación rápida

`pip install snscrape` (o desde el repo para la versión de desarrollo, que suele ir por delante de PyPI). Algunas redes requieren sesión o cookies para funcionar.

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
- **Modelos / API:** N/A.
- **Etiquetas:** `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [instaloader](instaloader.md) | 13.8k | Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Agent-Reach](agent-reach.md) | 111k | CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube, GitHub y más sin pagar APIs. |

## Enlaces

- 🐙 GitHub: [JustAnotherArchivist/snscrape](https://github.com/JustAnotherArchivist/snscrape)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
