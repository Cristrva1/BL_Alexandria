[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Redes sociales y descarga de medios

# 📱 yt-dlp

> Descargador de audio y video por línea de comandos compatible con miles de sitios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 208k | Unlicense | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 80/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Descargador de audio y vídeo por línea de comandos con soporte para miles de sitios, fork de youtube-dl. El código del repositorio es Unlicense, pero los ejecutables publicados incluyen código GPLv3+ o ISC. Es muy maduro y activo (~208k estrellas, 2026.10.26).

## ¿Qué hace?

Descarga vídeos, audio, listas, subtítulos y metadatos, con selección avanzada de formatos, posprocesado, integración con SponsorBlock y plantillas de nombres. Se mantiene al día con los cambios de los sitios mediante versiones frecuentes. También se usa como librería Python.

## ¿Cómo lo hace?

Se instala con los binarios oficiales, `pip install -U "yt-dlp[default]"` o gestores de paquetes. Usa FFmpeg para unir formatos y convertir. Algunos sitios necesitan cookies o un runtime de JavaScript.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Dependencia recomendada para fusionar y convertir formatos. | Instala FFmpeg antes de usar yt-dlp. |
| [whisperX](whisperx.md) | Transcribir el audio descargado. (combinación por arquitectura) | Descarga con `-x` y pasa el audio a WhisperX. |
| [Fabric](fabric.md) | Extraer transcripciones de YouTube y resumirlas con patrones de Fabric. (combinación por arquitectura) | Instala yt-dlp y usa las utilidades de YouTube de Fabric. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (9). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[AI-Youtube-Shorts-Generator](ai-youtube-shorts-generator.md) · [ArchiveBox](archivebox.md) · [Concat](concat.md) · [gallery-dl](gallery-dl.md) · [instaloader](instaloader.md) · [LosslessCut](lossless-cut.md) · [obsidian-second-brain](obsidian-second-brain.md) · [spotDL](spotdl.md) · [VideoLingo](videolingo.md)

**Notas:** Sin alternativas declaradas. Descargar contenido protegido puede infringir derechos de autor o términos de uso.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 2026.10.26 (2026-10-26) · licencia declarada Unlicense (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/yt-dlp/yt-dlp/blob/master/README.md) · [2](https://github.com/yt-dlp/yt-dlp/wiki/Installation)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere IA; acceso al contenido y servicios externos pueden tener sus propios costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El comando nightly del README instala versiones preliminares; empieza con la ruta estable y respeta permisos de uso |
| Coste | Sin pago a un modelo en la ruta básica. No requiere IA; acceso al contenido y servicios externos pueden tener sus propios costes |
| Equipo | Preparación según la ruta elegida. Binario oficial o Python compatible; FFmpeg para unir y convertir medios |

El comando nightly del README instala versiones preliminares; empieza con la ruta estable y respeta permisos de uso

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario oficial o Python compatible
- FFmpeg para unir y convertir medios

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
pip install "yt-dlp[default,curl-cffi]"
```

Comando copiado literalmente de el README (sección «Impersonation»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/yt-dlp/yt-dlp/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar yt-dlp para mi objetivo y necesito pasos guiados. Lee https://github.com/yt-dlp/yt-dlp/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Consulta formatos de un video propio y descarga una versión que puedas reproducir.

**Qué comprobar:** El archivo conserva audio y video y se abre en un reproductor.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Respaldar videos propios
- Obtener medios permitidos para edición

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Respaldar videos propios; Obtener medios permitidos para edición | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El comando nightly del README instala versiones preliminares; empieza con la ruta estable y respeta permisos de uso

## Stack y modelos

- **Stack:** Binario oficial o Python compatible; FFmpeg para unir y convertir medios
- **Etiquetas:** `video` `audio` `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)
- 🌐 Web: <https://discord.gg/H5MNcFW63r>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/yt-dlp/yt-dlp/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
