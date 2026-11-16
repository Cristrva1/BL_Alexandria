[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Fotogrametría y mapas desde imágenes

# 📚 MapLibre GL JS

> Biblioteca abierta de mapas vectoriales interactivos en el navegador con renderizado GPU, nacida como fork de Mapbox GL JS antes de su cambio de licencia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.1k | BSD-3-Clause | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (BSD-3-Clause) de la organización MapLibre, creada como fork de mapbox-gl-js cuando este pasó a una licencia no libre en diciembre de 2020. Madura y con amplio respaldo.

## ¿Qué hace?

Publica mapas interactivos en webs y webviews con teselas vectoriales renderizadas en GPU, estilos personalizables, etiquetas, terreno 3D, rotación e inclinación, y una API de capas, fuentes y eventos.

## ¿Cómo lo hace?

Escrito en TypeScript con WebGL2; se carga desde npm (`maplibre-gl`) o CDN. Necesita una fuente de teselas y un estilo (propios o de un proveedor compatible); el proyecto prohíbe retroportar código de Mapbox posterior al cambio de licencia.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [deck.gl](deck-gl.md) | deck.gl se integra con MapLibre como mapa base para añadir capas de datos en GPU. | Crea el mapa MapLibre; después añade el overlay de deck.gl. |
| [kepler.gl](kepler-gl.md) | kepler.gl usa MapLibre GL como motor de mapa base. | Instala kepler.gl junto a maplibre-gl según su guía. |
| [QGIS](qgis.md) | QGIS genera teselas vectoriales y datos que MapLibre publica en la web (combinación por arquitectura). | Prepara y exporta desde QGIS; después configura las fuentes en MapLibre. |

**Notas:** Alternativas (elige una): leaflet.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v6.18.0 (2026-11-11) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/maplibre/maplibre-gl-js/blob/main/README.md) · [2](https://maplibre.org/maplibre-gl-js/docs/)</sub>

## Ver similares

Grupo **Mapas web interactivos**: MapLibre GL JS ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Leaflet](leaflet.md) ⭐ recomendado | 70 | Si buscas esto: biblioteca JavaScript ligera para mapas web interactivos: unos 40 kB, capas de teselas, marcadores, GeoJSON y un ecosistema enorme de plugins. |
| 2 | **MapLibre GL JS** (esta ficha) | 67 | Si buscas esto: biblioteca abierta de mapas vectoriales interactivos en el navegador con renderizado GPU, nacida como fork de Mapbox GL JS antes de su cambio de licencia. |

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/maplibre/maplibre-gl-js/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MapLibre GL JS para mi objetivo y necesito pasos guiados. Lee https://github.com/maplibre/maplibre-gl-js/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una página con MapLibre desde unpkg y el estilo de demostración de MapLibre..

**Qué comprobar:** El mapa vectorial se carga, rota e inclina con el ratón..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- publicar mapas vectoriales con estilo propio sin depender de un proveedor
- crear mapas 3D con edificios y terreno en una web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: publicar mapas vectoriales con estilo propio sin depender de un proveedor; crear mapas 3D con edificios y terreno en una web | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, docker-compose.yml, package.json
- **Etiquetas:** `dataviz` `typescript` `library` `maps`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Leaflet](leaflet.md) | 45.9k | Biblioteca JavaScript ligera para mapas web interactivos: unos 40 kB, capas de teselas, marcadores, GeoJSON y un ecosistema enorme de plugins. |

## Enlaces

- 🐙 GitHub: [maplibre/maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js)
- 🌐 Web: <https://maplibre.org/maplibre-gl-js/docs/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/maplibre/maplibre-gl-js/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
