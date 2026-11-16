[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Fotogrametría y mapas desde imágenes

# 📚 Leaflet

> Biblioteca JavaScript ligera para mapas web interactivos: unos 40 kB, capas de teselas, marcadores, GeoJSON y un ecosistema enorme de plugins.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 45.9k | BSD-2-Clause | JavaScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (BSD-2-Clause) creada en 2010 por Volodymyr Agafonkin y mantenida por la comunidad Leaflet. La biblioteca de mapas web interactivos más extendida; muy madura.

## ¿Qué hace?

Construye mapas interactivos con teselas, marcadores, popups, polígonos, GeoJSON, controles y eventos, y funciona en escritorio y móvil. Su catálogo de plugins cubre clústeres, mapas de calor, dibujo, rutas y muchas otras funciones.

## ¿Cómo lo hace?

Pesa unos 40 kB de JS y 2,4 kB de CSS comprimidos; se carga desde CDN o npm. No incluye datos de mapa: usa servidores de teselas como OpenStreetMap, cuyas condiciones de uso hay que respetar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [WebODM](webodm.md) | WebODM muestra ortofotos y modelos en su interfaz con mapas Leaflet; los mosaicos generados se pueden publicar como capa en una web propia (combinación por arquitectura). | Procesa las imágenes en WebODM; después publica las teselas y añádelas como capa en Leaflet. |
| [QGIS](qgis.md) | QGIS prepara y estiliza datos que se exportan como GeoJSON o teselas para mostrarlos con Leaflet (combinación por arquitectura). | Prepara las capas en QGIS; después exporta y cárgalas en Leaflet. |
| [Claude Code](claude-code.md) | Un agente de código puede generar el HTML y JavaScript de un mapa Leaflet a partir de un GeoJSON (combinación por arquitectura). | Ten el GeoJSON listo; después pide al agente la página y revísala en el navegador. |
| [NiceGUI](nicegui.md) | Combinación recíproca: NiceGUI lo enlaza como «El elemento `ui.leaflet` de NiceGUI muestra mapas interactivos con Leaflet». | Orden indicado desde NiceGUI: Instala NiceGUI; después añade `ui.leaflet(center=...)` a la página. |

**Notas:** Alternativas (elige una): maplibre (mapas vectoriales con WebGL).

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.9.4 (2023-05-18) · licencia declarada BSD-2-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Leaflet/Leaflet/blob/main/README.md) · [2](https://leafletjs.com/)</sub>

## Ver similares

Grupo **Mapas web interactivos**: Leaflet ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Leaflet** (esta ficha) ⭐ recomendado | 70 | Si buscas esto: biblioteca JavaScript ligera para mapas web interactivos: unos 40 kB, capas de teselas, marcadores, GeoJSON y un ecosistema enorme de plugins. |
| 2 | [MapLibre GL JS](maplibre.md) | 67 | Si buscas esto: biblioteca abierta de mapas vectoriales interactivos en el navegador con renderizado GPU, nacida como fork de Mapbox GL JS antes de su cambio de licencia. |

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

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (bash):**

```
npm install leaflet@beta
```

Comando copiado literalmente de la documentación del repositorio (sección «Using npm»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/Leaflet/Leaflet/blob/main/docs/install.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Leaflet para mi objetivo y necesito pasos guiados. Lee https://github.com/Leaflet/Leaflet/blob/main/docs/install.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una página HTML con Leaflet desde CDN, un mapa de OpenStreetMap y un marcador..

**Qué comprobar:** El mapa se desplaza y amplía y el marcador muestra su popup al hacer clic..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- añadir un mapa con marcadores y popups a una web
- publicar datos GeoJSON propios sobre un mapa base de OpenStreetMap

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: añadir un mapa con marcadores y popups a una web; publicar datos GeoJSON propios sobre un mapa base de OpenStreetMap | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** JavaScript, package.json
- **Etiquetas:** `dataviz` `javascript` `library` `maps`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MapLibre GL JS](maplibre.md) | 12.1k | Biblioteca abierta de mapas vectoriales interactivos en el navegador con renderizado GPU, nacida como fork de Mapbox GL JS antes de su cambio de licencia. |

## Enlaces

- 🐙 GitHub: [Leaflet/Leaflet](https://github.com/Leaflet/Leaflet)
- 🌐 Web: <https://leafletjs.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Leaflet/Leaflet/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
