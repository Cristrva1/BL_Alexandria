[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ OBS Studio

> App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 79.6k | GPL-2.0 | C | 2026-11-10 |

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

OBS Studio captura, compone, codifica, graba y transmite video en Windows, macOS y Linux. Combinas en escenas la pantalla, ventanas, webcam, navegador y archivos multimedia, mezclas el audio con filtros y emites a YouTube, Twitch u otro servicio RTMP, o grabas a disco.

## Por qué destaca

Es el estándar libre para streaming y grabación de pantalla, con codificación por hardware (NVENC, AMF, QuickSync, Apple VT), cámara virtual, plugins y control remoto por WebSocket incluido.

## Cómo funciona

Su núcleo en C/C++ (libobs) compone en GPU las fuentes de cada escena y codifica con x264, FFmpeg o encoders de hardware. Se automatiza con scripts Lua o Python y con el protocolo obs-websocket.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y una fuente de imagen o sonido que quieras grabar.

1. Abre la web oficial de OBS y elige la descarga para tu sistema.
2. Sigue la guía del proyecto para añadir una fuente de captura y revisar la entrada de audio.
3. Graba unos segundos sin transmitir y reproduce el archivo para comprobar imagen y sonido.

[Instrucciones originales de instalación](https://github.com/obsproject/obs-studio/blob/master/README.rst)

[Abrir la web o descarga indicada por el autor](https://obsproject.com)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OBS Studio para mi objetivo y necesito pasos guiados. Lee https://github.com/obsproject/obs-studio/blob/master/README.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Grabar tutoriales y demos de producto con la webcam superpuesta
- Transmitir en directo a YouTube o Twitch con varias escenas
- Grabar clases o reuniones para transcribirlas después

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas grabar pantalla o transmitir en directo combinando varias fuentes en escenas | lo que necesitas es montar o recortar el video ya grabado; usa `opencut` o `lossless-cut` |

**Limitaciones:** No es un editor: graba y emite, pero el montaje posterior requiere otra herramienta.

## Stack y modelos

- **Stack:** C, C++, Qt, FFmpeg
- **Etiquetas:** `video` `audio` `ui` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LosslessCut](lossless-cut.md) | 46k | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. |
| [OpenCut](opencut.md) | 98.4k | Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. |
| [faster-whisper](faster-whisper.md) | 26.8k | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenScreen](openscreen.md) | 40k | App de escritorio para grabar demos de producto con zoom automático, webcam y subtítulos, alternativa libre a Screen Studio. |

## Enlaces

- 🐙 GitHub: [obsproject/obs-studio](https://github.com/obsproject/obs-studio)
- 🌐 Web: <https://obsproject.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/obsproject/obs-studio/blob/master/README.rst)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
