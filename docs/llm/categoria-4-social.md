# Alexandría para agentes · Redes sociales y descarga de medios

Categoría 4 «Buscar, extraer y monitorear información web» › subcategoría `social`. 4 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=4&sub=social · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `yt-dlp` | Descargador de audio y video por línea de comandos compatible con miles de… | 1 Básico | 80 | Unlicense (OSI permisiva) | sin grupo |
| `spotdl` | CLI que toma listas y canciones de Spotify, busca coincidencias en YouTube y… | 1 Básico | 64 | MIT (OSI permisiva) | sin grupo |
| `instaloader` | Herramienta y librería Python para descargar fotos, videos, stories, leyendas y… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `gallery-dl` | Programa de línea de comandos para descargar galerías y colecciones de imágenes… | 1 Básico | 53 | GPL-2.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### yt-dlp (`yt-dlp`)

- **Repo:** https://github.com/yt-dlp/yt-dlp · Unlicense · nivel 1 · 80/100
- **Qué es:** Descargador de audio y vídeo por línea de comandos con soporte para miles de sitios, fork de youtube-dl. El código del repositorio es Unlicense, pero los ejecutables publicados incluyen código GPLv3+ o ISC.
- **Cuándo elegirlo:** Casos: Respaldar videos propios; Obtener medios permitidos para edición.
- **Requisitos:** nivel 1: preparación sencilla; Binario oficial o Python compatible; FFmpeg para unir y convertir medios; hardware prerequisites; API de IA: no; Binario oficial o Python compatible; FFmpeg para unir y convertir medios.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install "yt-dlp[default,curl-cffi]"` — fuente: https://github.com/yt-dlp/yt-dlp/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Consulta formatos de un video propio y descarga una versión que puedas reproducir Éxito: El archivo conserva audio y video y se abre en un reproductor
- **Combina con:** `ffmpeg` [12/edicion], `whisperx` [29/stt], `fabric` [19/prompts]
- **Riesgos y avisos:** Sin alternativas declaradas. Descargar contenido protegido puede infringir derechos de autor o términos de uso. El comando nightly del README instala versiones preliminares; empieza con la ruta estable y respeta permisos de uso.

### spotDL (`spotdl`)

- **Repo:** https://github.com/spotDL/spotify-downloader · MIT · nivel 1 · 64/100
- **Qué es:** Descargador de música de línea de comandos de código abierto (MIT) mantenido por la comunidad spotDL; versión 4 estable y activa.
- **Cuándo elegirlo:** Casos: conservar una copia local de listas de reproducción propias; etiquetar automáticamente archivos de audio con metadatos de Spotify.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, docker-compose.yml, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install spotdl` — fuente: https://github.com/spotDL/spotify-downloader/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install spotdl`, prepara FFmpeg y descarga una canción con su URL. Éxito: El archivo de audio queda en la carpeta con título, artista y carátula incrustados.
- **Combina con:** `ffmpeg` [12/edicion], `yt-dlp`, `syncthing` [15/archivos]
- **Riesgos y avisos:** La coincidencia en YouTube no siempre es exacta: revisa versiones en vivo o remezclas.

### instaloader (`instaloader`)

- **Repo:** https://github.com/instaloader/instaloader · MIT · nivel 2 · 58/100
- **Qué es:** Herramienta Python para descargar fotos, vídeos y metadatos de Instagram. Licencia MIT. Es madura (~14k estrellas, v4.16) y muestra un patrocinador de APIs sociales.
- **Cuándo elegirlo:** Casos: Respaldar publicaciones propias; Actualizar una colección autorizada sin repetir todo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; espacio en disco; sesión propia para contenido que la requiera; hardware prerequisites; API de IA: no; Python; espacio en disco; sesión propia para contenido que la requiera.
- **Instalación (documentada en la fuente; no ejecutada):** `pip3 install instaloader` — fuente: https://github.com/instaloader/instaloader/blob/master/README.rst
- **Primera prueba propuesta (no ejecutada):** Descarga una publicación propia y compara archivo, descripción y metadatos Éxito: La carpeta contiene los medios y datos esperados
- **Combina con:** `archivebox` [4/busqueda], `whisper` [29/stt], `yt-dlp`
- **Riesgos y avisos:** Sin alternativas declaradas. Respeta los términos de uso de cada plataforma y la privacidad de las personas. Contenido privado exige acceso autorizado; que el código no cobre no garantiza que Instagram permita todas las operaciones.

### gallery-dl (`gallery-dl`)

- **Repo:** https://github.com/mikf/gallery-dl · GPL-2.0 · nivel 1 · 53/100
- **Qué es:** Herramienta de línea de comandos de código abierto (GPL-2.0) creada por Mike Fährmann y mantenida durante años. El README anuncia que el desarrollo activo se ha trasladado a Codeberg; GitHub sigue recibiendo cambios.
- **Cuándo elegirlo:** Casos: archivar una colección propia de imágenes con metadatos y nombres ordenados; descargar un conjunto de imágenes públicas para un dataset con permiso de uso.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, pyproject.toml, requirements.txt, setup.py; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install gallery-dl` — fuente: https://github.com/mikf/gallery-dl/blob/master/README.rst
- **Primera prueba propuesta (no ejecutada):** Instala gallery-dl (pip, Homebrew o binario) y descarga una galería pública pequeña a una carpeta de prueba. Éxito: Las imágenes quedan en disco con la estructura de carpetas y nombres configurada.
- **Combina con:** `yt-dlp`, `ffmpeg` [12/edicion], `real-esrgan` [11/edicion], `upscayl` [11/edicion]
- **Riesgos y avisos:** Repositorio canónico de desarrollo: Codeberg (mikf/gallery-dl); GitHub se mantiene como espejo con actividad.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-4-social.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Redes sociales y descarga de medios», lee `docs/alexandria/categoria-4-social.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-4-social.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
