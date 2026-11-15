[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 📄 Youtube2Webpage

> Script en Perl que genera una página web legible a partir de un video de YouTube, intercalando la transcripción de subtítulos con capturas de pantalla del momento citado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.5k | MIT | JavaScript | 2026-06-23 |

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

Convierte una charla en un artículo navegable con contexto visual.

## Por qué destaca

Automatiza el paso de charla a artículo combinando texto e imágenes sincronizadas; es una utilidad de nicho y poco conocida, pero efectiva para su propósito.

## Cómo funciona

Usa yt-dlp para descargar video y subtítulos y ffmpeg para extraer fotogramas en los timestamps relevantes, ensamblando todo en una página HTML estática con texto e imágenes alineadas.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/obra/Youtube2Webpage/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Youtube2Webpage para mi objetivo y necesito pasos guiados. Lee https://github.com/obra/Youtube2Webpage/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `docs` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper](whisper.md) | 113k | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. |

## Enlaces

- 🐙 GitHub: [obra/Youtube2Webpage](https://github.com/obra/Youtube2Webpage)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/obra/Youtube2Webpage/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
