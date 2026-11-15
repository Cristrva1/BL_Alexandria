[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ LosslessCut

> App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 46k | GPL-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

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

LosslessCut es una interfaz gráfica sobre FFmpeg para recortar y fusionar archivos de video y audio sin recompresión. Sirve para descartar gigas de material de cámara, GoPro o dron, extraer o reemplazar pistas, cambiar de contenedor (MKV a MP4) y editar metadatos o capítulos, en Windows, macOS y Linux.

## Por qué destaca

Al copiar los streams en vez de recodificar, los cortes son casi instantáneos y sin pérdida incluso en archivos enormes. Detecta escenas, silencios y fotogramas negros, y ofrece CLI y API HTTP para automatizarlo.

## Cómo funciona

App Electron con React que reproduce con el motor HTML5 de Chromium (o con FFmpeg para formatos no soportados) y exporta desde el archivo original con FFmpeg en modo copia de stream, sin tocar los fotogramas.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un archivo de video de prueba y una distribución compatible con tu sistema.

1. Elige la descarga oficial para tu sistema; el README distingue las tiendas de pago y los ejecutables gratuitos de GitHub.
2. Abre una copia de un video y marca el comienzo y final del fragmento que quieres conservar.
3. Exporta un fragmento y comprueba imagen, sonido y puntos de corte antes de trabajar con el original.

[Instrucciones originales de instalación](https://github.com/mifi/lossless-cut/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/mifi/lossless-cut/releases)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LosslessCut para mi objetivo y necesito pasos guiados. Lee https://github.com/mifi/lossless-cut/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Recortar horas de grabación de cámara o dron en segundos
- Extraer o reemplazar pistas de audio y subtítulos
- Dividir por escenas o silencios antes de editar un reel

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas recortar o unir material rápido y sin recomprimir, con interfaz gráfica | necesitas efectos, transiciones o un montaje con capas; mira `opencut` o, por código, `moviepy` |

**Limitaciones:** Sin recodificar, los cortes solo caen exactos en fotogramas clave, así que el punto de corte puede desplazarse unos fotogramas.

## Stack y modelos

- **Stack:** TypeScript, Electron, React, FFmpeg
- **Etiquetas:** `video` `audio` `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [yt-dlp](yt-dlp.md) | 208k | Descargador de audio y video por línea de comandos compatible con miles de sitios. |
| [whisperX](whisperx.md) | 25.3k | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. |
| [MoviePy](moviepy.md) | 15.2k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Enlaces

- 🐙 GitHub: [mifi/lossless-cut](https://github.com/mifi/lossless-cut)
- 🌐 Web: <https://losslesscut.app/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/mifi/lossless-cut/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
