[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🖥️ OpenScreen

> App de escritorio para grabar demos de producto con zoom automático, webcam y subtítulos, alternativa libre a Screen Studio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

> ⚠️ Archivado en GitHub: ya no recibe cambios.

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

OpenScreen graba una ventana o la pantalla completa con micrófono y audio del sistema, y después te deja pulir la demo: zooms que siguen al cursor, webcam superpuesta, fondos, anotaciones, recorte y velocidad por tramo. Exporta a MP4 o GIF en varias proporciones. El proyecto original está archivado; su continuación activa es getopenscreen/openscreen.

## Por qué destaca

Cubre lo esencial de Screen Studio gratis y sin marcas de agua, también para uso comercial, y genera subtítulos automáticos en el propio equipo sin subir el audio.

## Cómo funciona

App Electron en TypeScript con render en PixiJS. En macOS y Windows captura con APIs nativas (ScreenCaptureKit, Windows Graphics Capture) y en Linux con la captura del navegador.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Una distribución para tu sistema y los permisos de captura que pida la aplicación.

1. Abre Releases y elige el instalador correspondiente a tu sistema; el README también documenta gestores de paquetes.
2. Configura una captura pequeña y comprueba qué permisos de pantalla y audio necesita.
3. Graba unos segundos, revisa la edición y exporta una muestra antes de una grabación larga.

[Instrucciones originales de instalación](https://github.com/siddharthvaddem/openscreen/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/siddharthvaddem/openscreen/releases)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenScreen para mi objetivo y necesito pasos guiados. Lee https://github.com/siddharthvaddem/openscreen/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Grabar demos de producto para X, Reddit o YouTube
- Hacer tutoriales con zoom que sigue al cursor
- Exportar GIFs cortos de una función para la documentación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres demos de pantalla pulidas con zoom automático sin pagar Screen Studio | necesitas un proyecto mantenido; usa su continuación getopenscreen/openscreen, o `obs-studio` para grabación y streaming generales |

**Limitaciones:** El repositorio está archivado y sin mantenimiento (el propio autor advierte que no es de calidad de producción); la continuación comunitaria es getopenscreen/openscreen.

## Stack y modelos

- **Stack:** TypeScript, Electron, PixiJS
- **Etiquetas:** `video` `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LosslessCut](lossless-cut.md) | 46k | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. |
| [OpenCut](opencut.md) | 98.4k | Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OBS Studio](obs-studio.md) | 79.6k | App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real. |

## Enlaces

- 🐙 GitHub: [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/siddharthvaddem/openscreen/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
