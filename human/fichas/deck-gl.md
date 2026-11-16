[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Fotogrametría y mapas desde imágenes

# 📚 deck.gl

> Framework de visualización en WebGL2/WebGPU para grandes conjuntos de datos, con capas apilables sobre mapas y vistas 3D.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.8k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Framework de visualización de código abierto (MIT) del grupo vis.gl de la OpenJS Foundation, creado originalmente en Uber. Maduro y activo.

## ¿Qué hace?

Renderiza de forma eficiente grandes conjuntos de datos mediante capas componibles, con selección, resaltado y filtrado interactivo, proyecciones cartográficas e integración con proveedores de mapas base. Incluye un catálogo amplio de capas probadas y se extiende con capas propias.

## ¿Cómo lo hace?

Escrito en TypeScript sobre luma.gl (WebGL2/WebGPU); se usa por script, npm, con React o desde Python con pydeck en Jupyter. Se integra con MapLibre, Mapbox y Google Maps como mapa base.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [MapLibre GL JS](maplibre.md) | deck.gl se integra con MapLibre GL JS como mapa base, intercalando sus capas con las del estilo. | Crea el mapa MapLibre; después añade las capas de deck.gl como overlay. |
| [kepler.gl](kepler-gl.md) | kepler.gl está construido sobre deck.gl y MapLibre. | Usa kepler.gl para exploración sin código y deck.gl para visualizaciones a medida. |
| [Apache Superset](superset.md) | Apache Superset incluye tipos de gráfico basados en deck.gl para datos geoespaciales. | Superset con una fuente de datos con coordenadas; después crea un gráfico deck.gl. |
| [JupyterLab](jupyterlab.md) | pydeck, el binding de Python de deck.gl, muestra mapas interactivos en cuadernos Jupyter. | Instala pydeck en el entorno de JupyterLab; después renderiza las capas en una celda. |
| [Panel](panel.md) | Combinación recíproca: Panel lo enlaza como «Panel incluye un pane DeckGL para mostrar visualizaciones geoespaciales de deck.gl». | Orden indicado desde Panel: Instala Panel; después usa `pn.pane.DeckGL` con la especificación de deck.gl. |

**Notas:** Para mapas base comerciales revisa las condiciones y claves del proveedor.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v9.3.12 (2026-10-30) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/visgl/deck.gl/blob/master/README.md) · [2](https://deck.gl/docs) · [3](https://superset.apache.org/docs/configuration/map-tiles/)</sub>

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

**Entrada documentada (consulta la sintaxis original):**

```
npm install deck.gl
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/visgl/deck.gl/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar deck.gl para mi objetivo y necesito pasos guiados. Lee https://github.com/visgl/deck.gl/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala `npm install deck.gl` o `pip install pydeck` y dibuja una capa de puntos con datos de ejemplo..

**Qué comprobar:** El mapa muestra los puntos y permite seleccionar uno con el ratón..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- visualizar millones de puntos geográficos con interacción fluida
- crear mapas 3D de densidad o rutas en una web o cuaderno

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: visualizar millones de puntos geográficos con interacción fluida; crear mapas 3D de densidad o rutas en una web o cuaderno | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `dataviz` `typescript` `library` `maps`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [visgl/deck.gl](https://github.com/visgl/deck.gl)
- 🌐 Web: <https://deck.gl>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/visgl/deck.gl/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
