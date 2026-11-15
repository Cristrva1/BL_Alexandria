[🏠 Inicio](../README.md) › [📄 Documentos & Presentaciones](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 📄 Youtube2Webpage

> Script en Perl que genera una página web legible a partir de un video de YouTube, intercalando la transcripción de subtítulos con capturas de pantalla del momento citado.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 1.5k | MIT | JavaScript | 2023-12-01 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Convierte una charla en un artículo navegable con contexto visual.

## Por qué destaca

Automatiza el paso de charla a artículo combinando texto e imágenes sincronizadas; es una utilidad de nicho y poco conocida, pero efectiva para su propósito.

## Cómo funciona

Usa yt-dlp para descargar video y subtítulos y ffmpeg para extraer fotogramas en los timestamps relevantes, ensamblando todo en una página HTML estática con texto e imágenes alineadas.

## Instalación rápida

Clonar el repo y ejecutar el script Perl con yt-dlp y ffmpeg instalados en el sistema. Requiere Perl y los binarios mencionados.

## Casos de uso

- Convertir una charla en artículo legible
- Documentar video como texto+imágenes
- Archivar contenido de YouTube como página estática

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres video → artículo con transcripción y capturas | necesitas edición de video o el contenido no tiene subtítulos |

## Stack y modelos

- **Stack:** Perl, yt-dlp, ffmpeg
- **Modelos / API:** N/A.
- **Etiquetas:** `docs` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper](whisper.md) | 112k | Modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo. |

## Enlaces

- 🐙 GitHub: [obra/Youtube2Webpage](https://github.com/obra/Youtube2Webpage)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
