[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Fotogrametría y mapas desde imágenes

# ⚙️ WebODM

> Interfaz para procesar fotografías aéreas y obtener mapas y modelos con el ecosistema de OpenDroneMap.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.3k | AGPL-3.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

WebODM, software de procesamiento de imágenes de drones con interfaz web, liderado por @pierotofy. Licencia AGPL-3.0. Es maduro (~4.3k estrellas, v4.0.1) y desde abril de 2026 es independiente de OpenDroneMap.

## ¿Qué hace?

Genera mapas georreferenciados, nubes de puntos, modelos de elevación, modelos 3D texturizados y gaussian splats a partir de fotos aéreas. Admite varios motores de procesamiento: ODX (su fork propio), MicMac y LGT. Incluye gestión de proyectos, visor de mapas y 3D, y API.

## ¿Cómo lo hace?

Se instala con los instaladores oficiales gratuitos o con Docker; usa Django 5.2, PostgreSQL 18 y Valkey. El README avisa de que quien pagó un instalador después de abril de 2026 compró otro software y documenta la migración. Revisa los requisitos de hardware antes de procesar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [blender](blender.md) | Editar o renderizar los modelos exportados. (combinación por arquitectura) | Exporta el modelo texturizado e impórtalo en Blender. |
| [three.js](three-js.md) | Publicar modelos o splats en una web propia. (combinación por arquitectura) | Exporta y carga con three.js. |
| [marimo](marimo.md) | Analizar ortomosaicos y DEM exportados. (combinación por arquitectura) | Abre los GeoTIFF en un notebook. |
| [Leaflet](leaflet.md) | Combinación recíproca: Leaflet lo enlaza como «WebODM muestra ortofotos y modelos en su interfaz con mapas Leaflet; los mosaicos generados se pueden publicar como capa en una web propia (combinación por arquitectura)». | Orden indicado desde Leaflet: Procesa las imágenes en WebODM; después publica las teselas y añádelas como capa en Leaflet. |
| [QGIS](qgis.md) | Combinación recíproca: QGIS lo enlaza como «Las ortofotos y modelos de elevación generados con WebODM se analizan en QGIS (combinación por arquitectura)». | Orden indicado desde QGIS: Procesa las imágenes en WebODM; después descarga los GeoTIFF y ábrelos en QGIS. |

**Notas:** Sin alternativas declaradas. La combinación previa webodm → odm queda obsoleta: WebODM usa ODX, no ODM.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v4.0.1 (2026-11-15) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/WebODM/WebODM/blob/master/README.md) · [2](https://webodm.org/blog/announcement/) · [3](https://docs.webodm.org/)</sub>

## Ver similares

Grupo **Fotogrametría con drones**: WebODM ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ODM](odm.md) ⭐ recomendado | 58 | Si buscas esto: herramientas para convertir fotografías aéreas en mapas, nubes de puntos, modelos 3D y modelos de elevación. |
| 2 | **WebODM** (esta ficha) | 57 | Si buscas esto: interfaz para procesar fotografías aéreas y obtener mapas y modelos con el ecosistema de OpenDroneMap. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Los instaladores oficiales actuales se anuncian gratuitos; hardware, soporte o servicios externos pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El autor distingue los instaladores actuales de productos cobrados por terceros; no extrapoles tutoriales antiguos sin comprobar el origen |
| Coste | El coste depende del proveedor o la ruta. Los instaladores oficiales actuales se anuncian gratuitos; hardware, soporte o servicios externos pueden costar |
| Equipo | Preparación según la ruta elegida. Instalador oficial o Docker; RAM y disco según fotografías; dataset de prueba |

El autor distingue los instaladores actuales de productos cobrados por terceros; no extrapoles tutoriales antiguos sin comprobar el origen

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador oficial o Docker
- RAM y disco según fotografías
- dataset de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
git clone https://github.com/WebODM/WebODM --config core.autocrlf=input --depth 1
```

Comando copiado literalmente de la documentación oficial enlazada desde el README (sección «Docker»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://docs.webodm.org/installation/#hardware-requirements)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar WebODM para mi objetivo y necesito pasos guiados. Lee https://docs.webodm.org/installation/#hardware-requirements. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga un conjunto pequeño de fotos propias y revisa el informe de procesamiento.

**Qué comprobar:** Puedes abrir ortofoto, nube y reporte de calidad del mismo trabajo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Procesar imágenes de dron desde una interfaz
- Comparar resultados de dos vuelos de práctica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Procesar imágenes de dron desde una interfaz; Comparar resultados de dos vuelos de práctica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El autor distingue los instaladores actuales de productos cobrados por terceros; no extrapoles tutoriales antiguos sin comprobar el origen

## Stack y modelos

- **Stack:** Instalador oficial o Docker; RAM y disco según fotografías; dataset de prueba
- **Etiquetas:** `geoespacial` `server` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [WebODM/WebODM](https://github.com/WebODM/WebODM)
- 🌐 Web: <https://webodm.org/download>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/WebODM/WebODM/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
