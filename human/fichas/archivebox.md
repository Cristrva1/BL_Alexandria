[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# 🔍 ArchiveBox

> Archivador web auto-hospedado que guarda páginas en HTML, PDF, capturas y medios.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 29k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Qué es

Le das URLs, marcadores o historial y guarda copias completas para siempre. Útil para investigación y preservación de fuentes.

## Por qué destaca

Guarda cada página en varios formatos abiertos que siguen legibles sin la app.

## Cómo funciona

Usa Chrome headless, wget, yt-dlp y otras herramientas para capturar cada URL en carpetas con índice.

## Instalación rápida

`docker run -it -v $PWD:/data archivebox/archivebox init --setup`.

## Casos de uso

- Archivar fuentes de una investigación
- Respaldar marcadores
- Guardar evidencia de páginas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres conservar copias fieles de páginas web | solo necesitas el texto para un LLM; mira `jina-reader` |

## Stack y modelos

- **Stack:** Python, Django, Docker
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `scraping` `data` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [yt-dlp](yt-dlp.md) | 207k | Descargador de audio y video por línea de comandos compatible con miles de sitios. |

## Enlaces

- 🐙 GitHub: [ArchiveBox/ArchiveBox](https://github.com/ArchiveBox/ArchiveBox)
- 🌐 Web: <https://archivebox.io>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
