[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Redes sociales y descarga de medios

# 🖥️ spotDL

> CLI que toma listas y canciones de Spotify, busca coincidencias en YouTube y las descarga con carátula, letras y metadatos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.8k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Descargador de música de línea de comandos de código abierto (MIT) mantenido por la comunidad spotDL; versión 4 estable y activa.

## ¿Qué hace?

Encuentra en YouTube las canciones de listas, álbumes o pistas de Spotify y las descarga con carátula, letras y metadatos. Ofrece modos de sincronización de listas, servidor web y varios formatos de salida.

## ¿Cómo lo hace?

Escrito en Python; se instala con `pip install spotdl`, ejecutables publicados, Termux o Docker. Requiere FFmpeg (puede descargarlo con su propia opción) y usa yt-dlp para la descarga del audio.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | spotDL necesita FFmpeg para convertir el audio descargado; documenta su instalación. | Instala FFmpeg o usa la opción de descarga de spotDL; después descarga canciones. |
| [yt-dlp](yt-dlp.md) | spotDL usa yt-dlp para descargar el audio encontrado en YouTube. | Se instala como dependencia; mantenlo actualizado si fallan las descargas. |
| [syncthing](syncthing.md) | Syncthing puede sincronizar la carpeta de música descargada entre tus dispositivos (combinación por arquitectura). | Descarga con spotDL en una carpeta; después compártela con Syncthing. |

**Notas:** La coincidencia en YouTube no siempre es exacta: revisa versiones en vivo o remezclas.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v4.6.0 (2026-10-26) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/spotDL/spotify-downloader/blob/master/README.md) · [2](https://spotdl.readthedocs.io/en/latest/)</sub>

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
pip install spotdl
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/spotDL/spotify-downloader/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar spotDL para mi objetivo y necesito pasos guiados. Lee https://github.com/spotDL/spotify-downloader/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install spotdl`, prepara FFmpeg y descarga una canción con su URL..

**Qué comprobar:** El archivo de audio queda en la carpeta con título, artista y carátula incrustados..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- conservar una copia local de listas de reproducción propias
- etiquetar automáticamente archivos de audio con metadatos de Spotify

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: conservar una copia local de listas de reproducción propias; etiquetar automáticamente archivos de audio con metadatos de Spotify | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Puede infringir derechos de autor y los términos de Spotify y YouTube; úsalo solo con contenido que tengas derecho a descargar.

## Stack y modelos

- **Stack:** Python, Dockerfile, docker-compose.yml, pyproject.toml
- **Etiquetas:** `audio` `python` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [spotDL/spotify-downloader](https://github.com/spotDL/spotify-downloader)
- 🌐 Web: <https://spotdl.readthedocs.io/en/latest/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/spotDL/spotify-downloader/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
