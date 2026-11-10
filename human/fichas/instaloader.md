[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Redes sociales y descarga de medios

# 📸 instaloader

> Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 13.8k | MIT | Python | 2026-11-01 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Resuelve el archivado masivo de Instagram sin recurrir a APIs oficiales de pago ni herramientas manuales.

## Por qué destaca

Utilidad veterana y muy usada para archivar Instagram, con CLI lista para usar y soporte de descargas incrementales y sesiones logueadas. Su madurez y mantenimiento continuo la convierten en la opción de facto para este caso concreto.

## Cómo funciona

Consulta los endpoints públicos de Instagram (o autenticados con sesión) y guarda los medios con su metadata en JSON, respetando la estructura del perfil y permitiendo reanudar descargas sin duplicar.

## Instalación rápida

`pip install instaloader`; se usa como CLI (`instaloader perfil`) o importando el módulo. Para contenido privado o límites altos hace falta iniciar sesión con una cuenta de Instagram.

## Casos de uso

- Archivar contenido de perfiles
- Datasets de medios sociales
- Backups incrementales de stories y posts de un creador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas datos de Instagram de forma fiable | quieres varias redes a la vez (snscrape) o el contenido requiere API oficial por ToS |

**Limitaciones:** Depende del frontend no oficial de Instagram, así que cambios en la app o el endurecimiento de sus ToS pueden romperlo; el uso masoso puede derivar en bloqueos de cuenta.

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** N/A.
- **Etiquetas:** `vision` `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [snscrape](snscrape.md) | 5.5k | Scraper de redes sociales (Twitter/X, Reddit, Telegram, Instagram, etc.) que recolecta posts y perfiles sin necesidad de APIs oficiales ni claves. |

## Enlaces

- 🐙 GitHub: [instaloader/instaloader](https://github.com/instaloader/instaloader)
- 🌐 Web: <https://instaloader.github.io/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
