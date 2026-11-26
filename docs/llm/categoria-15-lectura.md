# Alexandría para agentes · Libros, podcasts y bibliotecas personales

Categoría 15 «Organizar notas, archivos y servicios personales» › subcategoría `lectura`. 4 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=15&sub=lectura · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `jellyfin` | Sistema multimedia libre para gestionar y transmitir películas, series, música… | 1 Básico | 75 | GPL-2.0 (OSI copyleft) | sin grupo |
| `kavita` | Servidor de lectura rápido y multiplataforma para manga, cómics y libros, con… | 1 Básico | 57 | GPL-3.0 (OSI copyleft) | recomendado |
| `audiobookshelf` | Servidor personal para organizar audiolibros y podcasts, escuchar contenido y… | 3 Avanzado | 53 | GPL-3.0 (OSI copyleft) | sin grupo |
| `calibre-web` | Aplicación web para explorar, leer y descargar libros electrónicos de una base… | 1 Básico | 42 | GPL-3.0 (OSI copyleft) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Jellyfin (`jellyfin`)

- **Repo:** https://github.com/jellyfin/jellyfin · GPL-2.0 · nivel 1 · 75/100
- **Qué es:** Sistema multimedia de código abierto (GPL-2.0) mantenido por voluntarios desde 2018, cuando nació como fork de Emby. Sin licencias premium ni funciones de pago; muy maduro.
- **Cuándo elegirlo:** Casos: organizar y ver tu videoteca en TV, móvil y navegador; compartir una biblioteca multimedia con la familia sin cuentas en la nube.
- **Requisitos:** nivel 1: preparación sencilla; C#; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/jellyfin/jellyfin.git` — fuente: https://github.com/jellyfin/jellyfin/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Jellyfin (paquete o Docker), añade una carpeta con vídeos y reprodúcelos desde el navegador. Éxito: La biblioteca muestra carátulas y metadatos y el vídeo se reproduce, transcodificado si hace falta.
- **Combina con:** `ffmpeg` [12/edicion], `handbrake` [12/edicion], `audiobookshelf`, `coolify` [22/infraestructura]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. No hay alternativa directa en el catálogo (Plex y Emby son propietarios); audiobookshelf cubre otro tipo de medios.

### Kavita (`kavita`)

- **Repo:** https://github.com/Kareadita/Kavita · GPL-3.0 · nivel 1 · 57/100 · recomendado en «Bibliotecas de libros y cómics»
- **Qué es:** Servidor de lectura de código abierto (GPL-3.0) del proyecto Kareadita, con funciones adicionales (Kavita+) para patrocinadores. Activo y multiplataforma.
- **Cuándo elegirlo:** Casos: leer tu colección de cómics o manga desde cualquier dispositivo; compartir una biblioteca de lectura con amigos o familia.
- **Requisitos:** nivel 1: preparación sencilla; C#, Dockerfile; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Kareadita/Kavita/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Kavita con Docker, añade una carpeta con un cómic o EPUB y ábrelo en el lector web. Éxito: El archivo aparece en la biblioteca con su portada y se puede leer en el navegador.
- **Combina con:** `syncthing` [15/archivos], `audiobookshelf`, `coolify` [22/infraestructura]
- **Alternativas:** `calibre-web`
- **Riesgos y avisos:** Alternativas (elige una): calibre-web.

### audiobookshelf (`audiobookshelf`)

- **Repo:** https://github.com/advplyr/audiobookshelf · GPL-3.0 · nivel 3 · 53/100
- **Qué es:** Servidor autoalojado de audiolibros y podcasts, creado por @advplyr. Licencia GPL-3.0. Es maduro y activo (~15k estrellas, v2.37.2), pero el README avisa que no se revisan PR del frontend en Vue porque se está reescribiendo en React.
- **Cuándo elegirlo:** Casos: Organizar audiolibros propios o autorizados; Gestionar una colección de podcasts.
- **Requisitos:** nivel 3: preparación pesada; Servidor o Docker; carpetas de audio; volumen persistente; WebSocket si usas proxy; hardware prerequisites; API de IA: no; Servidor o Docker; carpetas de audio; volumen persistente; WebSocket si usas proxy.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://audiobookshelf.org/docs/category/installation
- **Primera prueba propuesta (no ejecutada):** Añade una grabación propia, reproduce un minuto y comprueba el progreso guardado Éxito: Puedes retomar la reproducción desde otro dispositivo autorizado
- **Combina con:** `coolify` [22/infraestructura], `syncthing` [15/archivos], `activepieces` [1/motores], `jellyfin`, `kavita`
- **Riesgos y avisos:** Sin alternativas declaradas. Antes de contribuir al frontend, revisa el estado de la migración a React. Los comandos Docker y VS Code del README son para desarrollo; para usar el servidor sigue la guía de instalación.

### Calibre-Web (`calibre-web`)

- **Repo:** https://github.com/janeczku/calibre-web · GPL-3.0 · nivel 1 · 42/100 · alternativa en «Bibliotecas de libros y cómics»
- **Qué es:** Aplicación de código abierto (GPL-3.0) de janeczku, fork del proyecto library de mutschler. Madura y activa; requiere una base de datos de Calibre válida.
- **Cuándo elegirlo:** Casos: acceder a tu biblioteca de Calibre desde el móvil o el e-reader; compartir una biblioteca de libros con la familia con cuentas separadas.
- **Requisitos:** nivel 1: preparación sencilla; Fluent, pyproject.toml, requirements.txt; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install calibreweb` — fuente: https://github.com/janeczku/calibre-web/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install calibreweb`, apunta a una biblioteca de Calibre de prueba y abre un libro en el lector web. Éxito: El catálogo muestra los libros con portadas y el lector abre el EPUB.
- **Combina con:** `syncthing` [15/archivos], `pandoc` [13/conversion], `coolify` [22/infraestructura]
- **Alternativas:** `kavita`
- **Riesgos y avisos:** Alternativas (elige una): kavita.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-15-lectura.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Libros, podcasts y bibliotecas personales», lee `docs/alexandria/categoria-15-lectura.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-15-lectura.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
