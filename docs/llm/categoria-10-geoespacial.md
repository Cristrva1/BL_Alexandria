# Alexandría para agentes · Fotogrametría y mapas desde imágenes

Categoría 10 «Dashboards, analítica y mapas» › subcategoría `geoespacial`. 7 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=10&sub=geoespacial · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `leaflet` | Biblioteca JavaScript ligera para mapas web interactivos: unos 40 kB, capas de… | 2 Intermedio | 70 | BSD-2-Clause (OSI permisiva) | recomendado |
| `maplibre` | Biblioteca abierta de mapas vectoriales interactivos en el navegador con… | 2 Intermedio | 67 | BSD-3-Clause (OSI permisiva) | alternativa |
| `kepler.gl` | Herramienta web de exploración visual de grandes datos geográficos sin código… | 1 Básico | 66 | MIT (OSI permisiva) | sin grupo |
| `deck.gl` | Framework de visualización en WebGL2/WebGPU para grandes conjuntos de datos… | 2 Intermedio | 65 | MIT (OSI permisiva) | sin grupo |
| `qgis` | Sistema de información geográfica libre y multiplataforma: gestión de datos… | 1 Básico | 61 | GPL-2.0 (OSI copyleft) | sin grupo |
| `webodm` | Interfaz para procesar fotografías aéreas y obtener mapas y modelos con el… | 3 Avanzado | 60 | AGPL-3.0 (OSI copyleft) | recomendado |
| `odm` | Herramientas para convertir fotografías aéreas en mapas, nubes de puntos… | 2 Intermedio | 58 | AGPL-3.0 (OSI copyleft) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Leaflet (`leaflet`)

- **Repo:** https://github.com/Leaflet/Leaflet · BSD-2-Clause · nivel 2 · 70/100 · recomendado en «Mapas web interactivos»
- **Qué es:** Biblioteca de código abierto (BSD-2-Clause) creada en 2010 por Volodymyr Agafonkin y mantenida por la comunidad Leaflet. La biblioteca de mapas web interactivos más extendida; muy madura.
- **Cuándo elegirlo:** Casos: añadir un mapa con marcadores y popups a una web; publicar datos GeoJSON propios sobre un mapa base de OpenStreetMap.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; JavaScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `npm install leaflet@beta` — fuente: https://github.com/Leaflet/Leaflet/blob/main/docs/install.md
- **Primera prueba propuesta (no ejecutada):** Crea una página HTML con Leaflet desde CDN, un mapa de OpenStreetMap y un marcador. Éxito: El mapa se desplaza y amplía y el marcador muestra su popup al hacer clic.
- **Combina con:** `webodm`, `qgis`, `claude-code` [20/terminal], `nicegui` [25/apps]
- **Alternativas:** `maplibre`
- **Riesgos y avisos:** Alternativas (elige una): maplibre (mapas vectoriales con WebGL).

### MapLibre GL JS (`maplibre`)

- **Repo:** https://github.com/maplibre/maplibre-gl-js · BSD-3-Clause · nivel 2 · 67/100 · alternativa en «Mapas web interactivos»
- **Qué es:** Biblioteca de código abierto (BSD-3-Clause) de la organización MapLibre, creada como fork de mapbox-gl-js cuando este pasó a una licencia no libre en diciembre de 2020. Madura y con amplio respaldo.
- **Cuándo elegirlo:** Casos: publicar mapas vectoriales con estilo propio sin depender de un proveedor; crear mapas 3D con edificios y terreno en una web.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; TypeScript, docker-compose.yml, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/maplibre/maplibre-gl-js/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una página con MapLibre desde unpkg y el estilo de demostración de MapLibre. Éxito: El mapa vectorial se carga, rota e inclina con el ratón.
- **Combina con:** `deck.gl`, `kepler.gl`, `qgis`
- **Alternativas:** `leaflet`
- **Riesgos y avisos:** Alternativas (elige una): leaflet.

### kepler.gl (`kepler.gl`)

- **Repo:** https://github.com/keplergl/kepler.gl · MIT · nivel 1 · 66/100
- **Qué es:** Aplicación de análisis geoespacial de código abierto (MIT), creada en Uber y hoy proyecto de la OpenJS Foundation dentro del ecosistema vis.gl. Activa.
- **Cuándo elegirlo:** Casos: explorar millones de viajes o eventos geolocalizados en el navegador; incrustar un explorador de mapas en una aplicación React o en un cuaderno.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install --save @kepler.gl/components maplibre-gl` — fuente: https://github.com/keplergl/kepler.gl/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre la demo de kepler.gl y carga un CSV con columnas de latitud y longitud. Éxito: El mapa crea capas automáticamente y permite filtrar por tiempo.
- **Combina con:** `deck.gl`, `maplibre`, `jupyterlab` [25/datos], `claude-code` [20/terminal]
- **Riesgos y avisos:** La demo procesa los datos en el navegador; revisa memoria con conjuntos muy grandes.

### deck.gl (`deck.gl`)

- **Repo:** https://github.com/visgl/deck.gl · MIT · nivel 2 · 65/100
- **Qué es:** Framework de visualización de código abierto (MIT) del grupo vis.gl de la OpenJS Foundation, creado originalmente en Uber. Maduro y activo.
- **Cuándo elegirlo:** Casos: visualizar millones de puntos geográficos con interacción fluida; crear mapas 3D de densidad o rutas en una web o cuaderno.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; TypeScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `npm install deck.gl` — fuente: https://github.com/visgl/deck.gl/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala `npm install deck.gl` o `pip install pydeck` y dibuja una capa de puntos con datos de ejemplo. Éxito: El mapa muestra los puntos y permite seleccionar uno con el ratón.
- **Combina con:** `maplibre`, `kepler.gl`, `superset` [10/bi], `jupyterlab` [25/datos], `panel` [25/apps]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Para mapas base comerciales revisa las condiciones y claves del proveedor.

### QGIS (`qgis`)

- **Repo:** https://github.com/qgis/QGIS · GPL-2.0 · nivel 1 · 61/100
- **Qué es:** SIG de escritorio de código abierto (GPL-2.0 o posterior) desarrollado por la comunidad QGIS y miembro de OSGeo. Muy maduro, con versiones LTR y regulares.
- **Cuándo elegirlo:** Casos: preparar y analizar capas geográficas para un estudio o mapa impreso; publicar servicios de mapas WMS/WFS con QGIS Server.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; C++, CMakeLists.txt, requirements.txt; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/qgis/QGIS.git` — fuente: https://github.com/qgis/QGIS/blob/master/INSTALL.md
- **Primera prueba propuesta (no ejecutada):** Instala QGIS, carga una capa GeoJSON y un mapa base, y exporta un mapa en PDF. Éxito: El PDF contiene el mapa con la capa estilizada, leyenda y escala.
- **Combina con:** `leaflet`, `maplibre`, `webodm`, `duckdb` [25/datos]
- **Riesgos y avisos:** Curva de aprendizaje alta para análisis avanzado; la documentación oficial y los tutoriales de la comunidad son amplios.

### WebODM (`webodm`)

- **Repo:** https://github.com/WebODM/WebODM · AGPL-3.0 · nivel 3 · 60/100 · recomendado en «Fotogrametría con drones»
- **Qué es:** WebODM, software de procesamiento de imágenes de drones con interfaz web, liderado por @pierotofy. Licencia AGPL-3.0. Es maduro (~4.3k estrellas, v4.0.1) y desde abril de 2026 es independiente de OpenDroneMap.
- **Cuándo elegirlo:** Casos: Procesar imágenes de dron desde una interfaz; Comparar resultados de dos vuelos de práctica.
- **Requisitos:** nivel 3: preparación pesada; Instalador oficial o Docker; RAM y disco según fotografías; dataset de prueba; hardware prerequisites; API de IA: no; Instalador oficial o Docker; RAM y disco según fotografías; dataset de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/WebODM/WebODM --config core.autocrlf=input --depth 1` — fuente: https://docs.webodm.org/installation/#hardware-requirements
- **Primera prueba propuesta (no ejecutada):** Carga un conjunto pequeño de fotos propias y revisa el informe de procesamiento Éxito: Puedes abrir ortofoto, nube y reporte de calidad del mismo trabajo
- **Combina con:** `blender` [26/creacion-3d], `three.js` [26/animacion], `marimo` [25/datos], `leaflet`, `qgis`
- **Alternativas:** `odm`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. La combinación previa webodm → odm queda obsoleta: WebODM usa ODX, no ODM. El autor distingue los instaladores actuales de productos cobrados por terceros; no extrapoles tutoriales antiguos sin comprobar el origen.

### ODM (`odm`)

- **Repo:** https://github.com/OpenDroneMap/ODM · AGPL-3.0 · nivel 2 · 58/100 · alternativa en «Fotogrametría con drones»
- **Qué es:** ODM (OpenDroneMap), kit de línea de comandos para procesar imágenes aéreas de drones. Licencia AGPL-3.0. Es maduro (~6.6k estrellas, v3.6.2).
- **Cuándo elegirlo:** Casos: Crear un mapa a partir de fotos de dron; Producir una nube de puntos para inspección.
- **Requisitos:** nivel 2: preparación media; Docker; fotografías aéreas propias con solapamiento; RAM y disco según lote; hardware prerequisites; API de IA: no; Docker; fotografías aéreas propias con solapamiento; RAM y disco según lote.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/OpenDroneMap/ODM/blob/master/README.md

  ```bash
  # Windows
  docker run -ti --rm -v c:/Users/youruser/datasets:/datasets opendronemap/odm --project-path /datasets project
  ```
- **Primera prueba propuesta (no ejecutada):** Procesa un lote pequeño de imágenes de prueba y abre la ortofoto y nube de puntos Éxito: Puedes inspeccionar alineación, cobertura y errores visibles
- **Combina con:** `blender` [26/creacion-3d], `three.js` [26/animacion], `marimo` [25/datos]
- **Alternativas:** `webodm`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. Desde abril de 2026, WebODM ya no es su interfaz (ver ficha de webodm). El ejemplo Windows necesita sustituir la ruta del dataset y su carpeta de proyecto; el resultado depende de la calidad de las tomas.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-10-geoespacial.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Fotogrametría y mapas desde imágenes», lee `docs/alexandria/categoria-10-geoespacial.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-10-geoespacial.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
