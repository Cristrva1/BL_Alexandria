[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Libros, podcasts y bibliotecas personales

# ⚙️ Jellyfin

> Sistema multimedia libre para gestionar y transmitir películas, series, música y libros desde tu servidor, alternativa a Plex y Emby.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 59.4k | GPL-2.0 | C# | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 75/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Sistema multimedia de código abierto (GPL-2.0) mantenido por voluntarios desde 2018, cuando nació como fork de Emby. Sin licencias premium ni funciones de pago; muy maduro.

## ¿Qué hace?

Gestiona y transmite películas, series, música, audiolibros, libros y TV en directo con grabación, desde un servidor propio a clientes web, móviles, TV y consolas, con usuarios, control parental, metadatos automáticos, subtítulos y transcodificación por hardware.

## ¿Cómo lo hace?

Servidor en C#/.NET; se instala con paquetes para Linux, Windows y macOS o con Docker. Necesita jellyfin-ffmpeg para transcodificar; la aceleración por hardware se configura según la GPU.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Jellyfin transcodifica con jellyfin-ffmpeg, su compilación de FFmpeg, que se instala junto al servidor. | Instala jellyfin-ffmpeg o usa la imagen Docker que lo incluye. |
| [HandBrake](handbrake.md) | Convertir la videoteca a formatos compatibles con HandBrake reduce la transcodificación en tiempo real de Jellyfin (combinación por arquitectura). | Convierte con HandBrake; después añade los archivos a la biblioteca. |
| [audiobookshelf](audiobookshelf.md) | Audiobookshelf se especializa en audiolibros y pódcasts y complementa a Jellyfin para películas y música (combinación por arquitectura). | Despliega ambos con bibliotecas separadas. |
| [coolify](coolify.md) | La imagen Docker de Jellyfin se puede desplegar desde Coolify con volúmenes de medios (combinación por arquitectura). | Coolify primero; después crea el servicio y monta las carpetas de medios. |

**Notas:** No hay alternativa directa en el catálogo (Plex y Emby son propietarios); audiobookshelf cubre otro tipo de medios.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v12.4 (2026-10-26) · licencia declarada GPL-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/jellyfin/jellyfin/blob/master/README.md) · [2](https://jellyfin.org/docs/)</sub>

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/jellyfin/jellyfin/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Jellyfin para mi objetivo y necesito pasos guiados. Lee https://github.com/jellyfin/jellyfin/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Jellyfin (paquete o Docker), añade una carpeta con vídeos y reprodúcelos desde el navegador..

**Qué comprobar:** La biblioteca muestra carátulas y metadatos y el vídeo se reproduce, transcodificado si hace falta..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- organizar y ver tu videoteca en TV, móvil y navegador
- compartir una biblioteca multimedia con la familia sin cuentas en la nube

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: organizar y ver tu videoteca en TV, móvil y navegador; compartir una biblioteca multimedia con la familia sin cuentas en la nube | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** C#
- **Etiquetas:** `self-hosted` `csharp` `video` `server`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin)
- 🌐 Web: <https://jellyfin.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jellyfin/jellyfin/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
