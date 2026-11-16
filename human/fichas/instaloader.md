[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Redes sociales y descarga de medios

# 📸 instaloader

> Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.9k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta Python para descargar fotos, vídeos y metadatos de Instagram. Licencia MIT. Es madura (~14k estrellas, v4.16) y muestra un patrocinador de APIs sociales.

## ¿Qué hace?

Descarga perfiles públicos y privados (si inicias sesión y tienes acceso), hashtags, historias, destacados, reels, publicaciones etiquetadas y guardadas, con comentarios, geoetiquetas y textos. Actualiza descargas de forma incremental (`--fast-update`) y detecta cambios de nombre de perfil. También sirve como librería Python.

## ¿Cómo lo hace?

Se instala con `pip install instaloader` y se usa con `instaloader <perfil> [--stories] [--login USUARIO]`. Instagram limita las peticiones y puede bloquear cuentas que descargan mucho.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ArchiveBox](archivebox.md) | Archivar también las publicaciones en formatos de archivo web. (combinación por arquitectura) | Pasa las URLs de las publicaciones a ArchiveBox. |
| [whisper](whisper.md) | Transcribir el audio de los reels descargados. (combinación por arquitectura) | Extrae el audio y transcríbelo con Whisper. |
| [yt-dlp](yt-dlp.md) | Descargador alternativo para vídeos sueltos de otros sitios. (combinación por arquitectura) | Usa cada uno para lo que cubre mejor. |

**Notas:** Sin alternativas declaradas. Respeta los términos de uso de cada plataforma y la privacidad de las personas. Descargar contenido de otras personas puede vulnerar su privacidad.

Estado en GitHub: activo · último push 2026-11-01 · última versión publicada v4.16 (2026-10-26) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/instaloader/instaloader/blob/master/README.rst) · [2](https://instaloader.github.io/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa un modelo ni requiere API de IA; la cuenta y la plataforma imponen límites |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Contenido privado exige acceso autorizado; que el código no cobre no garantiza que Instagram permita todas las operaciones |
| Coste | Sin pago a un modelo en la ruta básica. No usa un modelo ni requiere API de IA; la cuenta y la plataforma imponen límites |
| Equipo | Preparación según la ruta elegida. Python; espacio en disco; sesión propia para contenido que la requiera |

Contenido privado exige acceso autorizado; que el código no cobre no garantiza que Instagram permita todas las operaciones

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- espacio en disco
- sesión propia para contenido que la requiera

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (shell):**

```
pip3 install instaloader
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/instaloader/instaloader/blob/master/README.rst)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar instaloader para mi objetivo y necesito pasos guiados. Lee https://github.com/instaloader/instaloader/blob/master/README.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga una publicación propia y compara archivo, descripción y metadatos.

**Qué comprobar:** La carpeta contiene los medios y datos esperados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Respaldar publicaciones propias
- Actualizar una colección autorizada sin repetir todo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Respaldar publicaciones propias; Actualizar una colección autorizada sin repetir todo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Contenido privado exige acceso autorizado; que el código no cobre no garantiza que Instagram permita todas las operaciones

## Stack y modelos

- **Stack:** Python; espacio en disco; sesión propia para contenido que la requiera
- **Etiquetas:** `vision` `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [instaloader/instaloader](https://github.com/instaloader/instaloader)
- 🌐 Web: <https://instaloader.github.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/instaloader/instaloader/blob/master/README.rst)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
