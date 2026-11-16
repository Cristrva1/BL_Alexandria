[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Fotogrametría y mapas desde imágenes

# 🖥️ QGIS

> Sistema de información geográfica libre y multiplataforma: gestión de datos espaciales, cartografía, análisis, Python y QGIS Server.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.8k | GPL-2.0 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

SIG de escritorio de código abierto (GPL-2.0 o posterior) desarrollado por la comunidad QGIS y miembro de OSGeo. Muy maduro, con versiones LTR y regulares.

## ¿Qué hace?

Gestiona datos espaciales vectoriales, ráster, nubes de puntos y mallas; crea cartografía de calidad, ejecuta análisis geoespacial con su caja de herramientas de procesamiento y se amplía con plugins y scripts en Python. QGIS Server publica mapas como servicios OGC.

## ¿Cómo lo hace?

Escrito en C++ con Qt; usa GDAL/OGR, PROJ y GEOS. Se instala desde qgis.org para Windows, macOS y Linux, o con imágenes Docker; la API PyQGIS permite automatizar tareas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Leaflet](leaflet.md) | Las capas preparadas en QGIS se exportan como GeoJSON o teselas para mapas web con Leaflet (combinación por arquitectura). | Prepara y exporta en QGIS; después cárgalas en Leaflet. |
| [MapLibre GL JS](maplibre.md) | QGIS puede generar teselas vectoriales que MapLibre muestra en la web (combinación por arquitectura). | Genera las teselas desde QGIS; después configura la fuente en MapLibre. |
| [WebODM](webodm.md) | Las ortofotos y modelos de elevación generados con WebODM se analizan en QGIS (combinación por arquitectura). | Procesa las imágenes en WebODM; después descarga los GeoTIFF y ábrelos en QGIS. |
| [DuckDB](duckdb.md) | DuckDB con su extensión espacial prepara GeoParquet o tablas espaciales que QGIS abre directamente (combinación por arquitectura). | Exporta desde DuckDB a GeoParquet o GeoPackage; después cárgalo en QGIS. |

**Notas:** Curva de aprendizaje alta para análisis avanzado; la documentación oficial y los tutoriales de la comunidad son amplios.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada final-3_44_15 (2026-09-25) · licencia declarada GPL-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/qgis/QGIS/blob/master/README.md) · [2](https://qgis.org)</sub>

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

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y una copia de datos o archivos para la primera prueba.

1. Abre las descargas o la web de la aplicación enlazadas por el autor; elige la versión para tu sistema.
2. Sigue su guía de inicio y configura únicamente la función que necesitas probar.
3. Abre un archivo o caso pequeño, guarda un resultado y comprueba que puedes recuperarlo antes de importar material real.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/qgis/QGIS/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://qgis.org)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar QGIS para mi objetivo y necesito pasos guiados. Lee https://github.com/qgis/QGIS/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala QGIS, carga una capa GeoJSON y un mapa base, y exporta un mapa en PDF..

**Qué comprobar:** El PDF contiene el mapa con la capa estilizada, leyenda y escala..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- preparar y analizar capas geográficas para un estudio o mapa impreso
- publicar servicios de mapas WMS/WFS con QGIS Server

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: preparar y analizar capas geográficas para un estudio o mapa impreso; publicar servicios de mapas WMS/WFS con QGIS Server | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt, requirements.txt
- **Etiquetas:** `dataviz` `cpp` `app` `maps`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [qgis/QGIS](https://github.com/qgis/QGIS)
- 🌐 Web: <https://qgis.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/qgis/QGIS/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
