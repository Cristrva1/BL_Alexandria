[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Redes sociales y descarga de medios

# 🖥️ gallery-dl

> Programa de línea de comandos para descargar galerías y colecciones de imágenes de muchos sitios, con nombres de archivo configurables.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 20.5k | GPL-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Herramienta de línea de comandos de código abierto (GPL-2.0) creada por Mike Fährmann y mantenida durante años. El README anuncia que el desarrollo activo se ha trasladado a Codeberg; GitHub sigue recibiendo cambios.

## ¿Qué hace?

Descarga galerías, colecciones y publicaciones de cientos de sitios de alojamiento de imágenes y redes (lista de sitios soportados en la documentación), con opciones de filtrado, autenticación, archivo de descargas previas y plantillas de nombres de archivo.

## ¿Cómo lo hace?

Requiere Python 3.8+ y Requests; opcionalmente yt-dlp o youtube-dl para vídeos HLS/DASH y FFmpeg para convertir animaciones Ugoira. Se instala con pip, Homebrew, ejecutables o Docker, y se configura con un archivo JSON.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [yt-dlp](yt-dlp.md) | gallery-dl usa yt-dlp de forma opcional para descargas de vídeo HLS/DASH e integración ytdl. | Instala yt-dlp en el mismo entorno; después activa la integración en la configuración. |
| [FFmpeg](ffmpeg.md) | FFmpeg es la dependencia opcional para convertir animaciones Ugoira de Pixiv. | Instala FFmpeg en el PATH; después configura el postprocesador correspondiente. |
| [Real-ESRGAN](real-esrgan.md) | Las imágenes descargadas pueden escalarse en lote con Real-ESRGAN antes de usarlas (combinación por arquitectura). | Descarga primero con gallery-dl; después procesa la carpeta con Real-ESRGAN. |

**Notas:** Repositorio canónico de desarrollo: Codeberg (mikf/gallery-dl); GitHub se mantiene como espejo con actividad.

Estado en Codeberg: activo · última actividad 2026-11-15 · última versión publicada v1.32.20 (2026-11-14) · licencia declarada GPL-2.0 (consultado el 2026-11-16).

Copia antigua en GitHub: activo · último push 2026-11-14 · última versión publicada v1.32.20 (2026-11-14) · licencia declarada GPL-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mikf/gallery-dl/blob/master/README.rst) · [2](https://codeberg.org/mikf/gallery-dl)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
brew install gallery-dl
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/mikf/gallery-dl/blob/master/README.rst)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar gallery-dl para mi objetivo y necesito pasos guiados. Lee https://github.com/mikf/gallery-dl/blob/master/README.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala gallery-dl (pip, Homebrew o binario) y descarga una galería pública pequeña a una carpeta de prueba..

**Qué comprobar:** Las imágenes quedan en disco con la estructura de carpetas y nombres configurada..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- archivar una colección propia de imágenes con metadatos y nombres ordenados
- descargar un conjunto de imágenes públicas para un dataset con permiso de uso

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: archivar una colección propia de imágenes con metadatos y nombres ordenados; descargar un conjunto de imágenes públicas para un dataset con permiso de uso | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Descargar contenido ajeno puede vulnerar términos de servicio o derechos de autor.

## Stack y modelos

- **Stack:** Python, Dockerfile, pyproject.toml, requirements.txt, setup.py
- **Etiquetas:** `scraping` `python` `image` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [mikf/gallery-dl](https://github.com/mikf/gallery-dl)
- 🌐 Web: <https://discord.gg/rSzQwRvGnE>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mikf/gallery-dl/blob/master/README.rst)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
