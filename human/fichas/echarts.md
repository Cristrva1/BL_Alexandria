[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Librerías de gráficos

# 📉 echarts

> Librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 67.7k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Apache ECharts, librería de visualización de la Apache Software Foundation. Licencia Apache-2.0. Es muy madura (~68k estrellas, 6.1.0).

## ¿Qué hace?

Ofrece decenas de tipos de gráficos (series, mapas, grafos, árboles, 3D con ECharts GL, calendarios) muy interactivos y personalizables, pensados para productos comerciales y paneles. Renderiza con Canvas o SVG y maneja grandes volúmenes de datos con renderizado progresivo.

## ¿Cómo lo hace?

Se instala con `npm install echarts` o desde CDN y se configura con un objeto `option` declarativo. Está escrito en TypeScript sobre la librería de renderizado ZRender.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [metabase](metabase.md) | Metabase usa ECharts en sus visualizaciones. (combinación por arquitectura) | No requiere instalación aparte. |
| [Apache Superset](superset.md) | Superset usa ECharts en muchos de sus gráficos. (combinación por arquitectura) | No requiere instalación aparte. |
| [heroui](heroui.md) | Paneles con componentes HeroUI y gráficos ECharts. (combinación por arquitectura) | Envuelve el gráfico en un componente de tarjeta. |
| [Ant Design](ant-design.md) | Combinación recíproca: Ant Design lo enlaza como «Gráficos avanzados en paneles de administración junto a las tablas y formularios de antd. (combinación por arquitectura); el ecosistema oficial ofrece Ant Design Charts como opción integrada». | Orden indicado desde Ant Design: Instala echarts y su envoltorio para React; úsalo en componentes Card o layouts de antd. |
| [awesome-dataviz](awesome-dataviz.md) | Combinación recíproca: awesome-dataviz lo enlaza como «Una de las librerías destacadas de la lista. (combinación por arquitectura)». | Orden indicado desde awesome-dataviz: Compara alternativas en la lista antes de elegir. |
| [dash](dash.md) | Combinación recíproca: dash lo enlaza como «Gráficos alternativos mediante componentes comunitarios. (combinación por arquitectura)». | Orden indicado desde dash: Integra el componente correspondiente. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[NiceGUI](nicegui.md) · [Panel](panel.md)

**Notas:** Alternativas (elige una): d3, chart-js, recharts.

Estado en GitHub: activo · último push 2026-10-13 · última versión publicada 6.1.0 (2026-05-19) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/apache/echarts/blob/master/README.md) · [2](https://echarts.apache.org/en/index.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca Apache-2.0 no requiere IA; datos y mapas externos conservan sus condiciones |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. npm install del README prepara el desarrollo del repositorio; sigue el handbook para integrar ECharts en tu app |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca Apache-2.0 no requiere IA; datos y mapas externos conservan sus condiciones |
| Equipo | Preparación según la ruta elegida. JavaScript; contenedor con tamaño; datos |

npm install del README prepara el desarrollo del repositorio; sigue el handbook para integrar ECharts en tu app

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- JavaScript
- contenedor con tamaño
- datos

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://echarts.apache.org/handbook/en/get-started/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar echarts para mi objetivo y necesito pasos guiados. Lee https://echarts.apache.org/handbook/en/get-started/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una serie de ventas y añade una segunda para comparar.

**Qué comprobar:** La leyenda distingue ambas series y el tooltip muestra valores correctos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir un dashboard interactivo
- Combinar mapa y estadísticas en una web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir un dashboard interactivo; Combinar mapa y estadísticas en una web | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** npm install del README prepara el desarrollo del repositorio; sigue el handbook para integrar ECharts en tu app

## Stack y modelos

- **Stack:** JavaScript; contenedor con tamaño; datos
- **Etiquetas:** `dataviz` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [D3.js](d3.md) | 114k | Librería JavaScript para visualizaciones de datos a medida con SVG, Canvas y HTML. |
| [Chart.js](chart-js.md) | 67.8k | Librería JavaScript para dibujar gráficos en canvas dentro de una página o aplicación web. |
| [Recharts](recharts.md) | 27.7k | Librería de gráficos para React construida con D3, declarativa y componible. |

## Enlaces

- 🐙 GitHub: [apache/echarts](https://github.com/apache/echarts)
- 🌐 Web: <https://echarts.apache.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/apache/echarts/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
