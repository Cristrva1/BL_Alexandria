[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Fotogrametría y mapas desde imágenes

# 🖥️ kepler.gl

> Herramienta web de exploración visual de grandes datos geográficos sin código, también usable como componente React y widget de Jupyter.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.1k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Aplicación de análisis geoespacial de código abierto (MIT), creada en Uber y hoy proyecto de la OpenJS Foundation dentro del ecosistema vis.gl. Activa.

## ¿Qué hace?

Permite explorar visualmente grandes conjuntos de datos de geolocalización: capas de puntos, arcos, hexágonos, rutas y polígonos, filtros, animación temporal y exportación de mapas. Se usa como app web, componente React incrustable y widget de Jupyter, y documenta integración con asistentes de IA y MCP.

## ¿Cómo lo hace?

Escrito en TypeScript con React y Redux sobre deck.gl y MapLibre GL; se instala con `npm install --save @kepler.gl/components maplibre-gl` o se usa la demo pública, que procesa los datos en el navegador.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [deck.gl](deck-gl.md) | kepler.gl se construye sobre deck.gl para el renderizado de sus capas. | Usa kepler.gl para explorar y deck.gl para llevar la visualización a una app propia. |
| [MapLibre GL JS](maplibre.md) | kepler.gl usa MapLibre GL como mapa base. | Instala maplibre-gl junto a los componentes de kepler.gl. |
| [JupyterLab](jupyterlab.md) | kepler.gl ofrece un widget de Jupyter documentado para explorar DataFrames en cuadernos. | Instala el widget de kepler.gl en el entorno de JupyterLab; después pásale los datos. |
| [Claude Code](claude-code.md) | El README dedica una sección a asistentes de IA y MCP para que los agentes creen y manipulen mapas de kepler.gl. | Sigue la sección de MCP del README; después registra el servidor en Claude Code. |

**Notas:** La demo procesa los datos en el navegador; revisa memoria con conjuntos muy grandes.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.3.0-alpha.21 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/keplergl/kepler.gl/blob/master/README.md) · [2](https://docs.kepler.gl/)</sub>

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

[Instrucciones originales de instalación](https://github.com/keplergl/kepler.gl/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar kepler.gl para mi objetivo y necesito pasos guiados. Lee https://github.com/keplergl/kepler.gl/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre la demo de kepler.gl y carga un CSV con columnas de latitud y longitud..

**Qué comprobar:** El mapa crea capas automáticamente y permite filtrar por tiempo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- explorar millones de viajes o eventos geolocalizados en el navegador
- incrustar un explorador de mapas en una aplicación React o en un cuaderno

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: explorar millones de viajes o eventos geolocalizados en el navegador; incrustar un explorador de mapas en una aplicación React o en un cuaderno | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `dataviz` `typescript` `app` `maps`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [keplergl/kepler.gl](https://github.com/keplergl/kepler.gl)
- 🌐 Web: <http://kepler.gl>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/keplergl/kepler.gl/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
