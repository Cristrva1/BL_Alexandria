# Alexandría para agentes · Librerías de gráficos

Categoría 10 «Dashboards, analítica y mapas» › subcategoría `graficos`. 5 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=10&sub=graficos · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `echarts` | Librería de visualización potente para gráficos y dashboards web (proyecto… | 2 Intermedio | 71 | Apache-2.0 (OSI permisiva) | recomendado |
| `d3` | Librería JavaScript para visualizaciones de datos a medida con SVG, Canvas y… | 2 Intermedio | 70 | ISC (OSI permisiva) | alternativa |
| `recharts` | Librería de gráficos para React construida con D3, declarativa y componible. | 2 Intermedio | 69 | MIT (OSI permisiva) | alternativa |
| `chart-js` | Librería JavaScript para dibujar gráficos en canvas dentro de una página o… | 2 Intermedio | 64 | MIT (OSI permisiva) | alternativa |
| `uplot` | Biblioteca compacta de gráficos de series temporales en JavaScript, orientada a… | 2 Intermedio | 59 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### echarts (`echarts`)

- **Repo:** https://github.com/apache/echarts · Apache-2.0 · nivel 2 · 71/100 · recomendado en «Librerías de gráficos»
- **Qué es:** Apache ECharts, librería de visualización de la Apache Software Foundation. Licencia Apache-2.0. Es muy madura (~68k estrellas, 6.1.0).
- **Cuándo elegirlo:** Casos: Construir un dashboard interactivo; Combinar mapa y estadísticas en una web.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; JavaScript; contenedor con tamaño; datos; hardware prerequisites; API de IA: no; JavaScript; contenedor con tamaño; datos.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install echarts --save` — fuente: https://github.com/apache/echarts/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una serie de ventas y añade una segunda para comparar Éxito: La leyenda distingue ambas series y el tooltip muestra valores correctos
- **Combina con:** `metabase` [10/bi], `superset` [10/bi], `heroui` [9/componentes], `ant-design` [9/componentes], `awesome-dataviz` [10/recursos], `dash` [25/apps]
- **Alternativas:** `d3`, `recharts`, `chart-js`
- **Riesgos y avisos:** Alternativas (elige una): d3, chart-js, recharts. Npm install del README prepara el desarrollo del repositorio; sigue el handbook para integrar ECharts en tu app.

### D3.js (`d3`)

- **Repo:** https://github.com/d3/d3 · ISC · nivel 2 · 70/100 · alternativa en «Librerías de gráficos»
- **Qué es:** D3 (Data-Driven Documents), librería JavaScript de bajo nivel para visualización de datos. Licencia ISC. Es infraestructura muy madura (~114k estrellas, v7.9.2).
- **Cuándo elegirlo:** Casos: Diseñar una visualización a medida; Explorar relaciones entre datos con interacción.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; JavaScript; HTML/SVG o Canvas; datos de prueba; hardware prerequisites; API de IA: no; JavaScript; HTML/SVG o Canvas; datos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `yarn add d3` — fuente: https://github.com/d3/d3/blob/main/docs/getting-started.md
- **Primera prueba propuesta (no ejecutada):** Construye un gráfico de barras de tres categorías con escala y ejes explícitos Éxito: Cada barra y etiqueta corresponde a su valor
- **Combina con:** `recharts`, `awesome-dataviz` [10/recursos], `marimo` [25/datos]
- **Alternativas:** `echarts`, `recharts`, `chart-js`
- **Riesgos y avisos:** Alternativas (elige una): echarts. Curva de aprendizaje alta. Ofrece piezas de bajo nivel; exige más programación que una biblioteca de gráficos ya montados.

### Recharts (`recharts`)

- **Repo:** https://github.com/recharts/recharts · MIT · nivel 2 · 69/100 · alternativa en «Librerías de gráficos»
- **Qué es:** Recharts, librería de gráficos para React construida con D3. Licencia MIT. Es madura (~28k estrellas, v3.10.1).
- **Cuándo elegirlo:** Casos: Visualizar una serie de ventas; Comparar categorías en un dashboard React.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; React; Node; react-is compatible; datos de prueba; hardware prerequisites; API de IA: no; React; Node; react-is compatible; datos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/recharts/recharts/blob/main/README.md

  ```sh
  # latest stable
  npm install recharts react-is
  ```
- **Primera prueba propuesta (no ejecutada):** Dibuja una línea con cinco valores y comprueba etiquetas y tooltip Éxito: Los puntos corresponden a los datos y el gráfico cabe en móvil
- **Combina con:** `ui` [9/componentes], `d3`, `tailwindcss` [9/estilos], `mui` [9/componentes], `mantine` [9/componentes]
- **Alternativas:** `echarts`, `d3`, `chart-js`
- **Riesgos y avisos:** Alternativas (elige una): chart-js, echarts. El signo $ del ejemplo es un indicador de terminal y no parte del comando; ajusta react-is a la versión de React.

### Chart.js (`chart-js`)

- **Repo:** https://github.com/chartjs/Chart.js · MIT · nivel 2 · 64/100 · alternativa en «Librerías de gráficos»
- **Qué es:** Chart.js, librería JavaScript de gráficos sobre Canvas para diseñadores y desarrolladores. Licencia MIT. Es muy madura (~68k estrellas, v4.6.1).
- **Cuándo elegirlo:** Casos: Añadir gráficos a una página sencilla; Comparar resultados por periodo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; JavaScript; canvas; gestor npm o script distribuido; hardware prerequisites; API de IA: no; JavaScript; canvas; gestor npm o script distribuido.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install chart.js` — fuente: https://github.com/chartjs/Chart.js/blob/master/docs/getting-started/installation.md
- **Primera prueba propuesta (no ejecutada):** Muestra un gráfico con tres categorías y cambia un valor Éxito: El gráfico se actualiza y conserva etiquetas y leyenda
- **Combina con:** `tailwindcss` [9/estilos], `duckdb` [25/datos], `supabase` [22/infraestructura]
- **Alternativas:** `echarts`, `d3`, `recharts`
- **Riesgos y avisos:** Alternativas (elige una): echarts, recharts. El canvas necesita tamaño y alternativa textual adecuados para comunicar los datos a todos los usuarios.

### uPlot (`uplot`)

- **Repo:** https://github.com/leeoniya/uPlot · MIT · nivel 2 · 59/100
- **Qué es:** μPlot, librería compacta de gráficos de series temporales sobre Canvas 2D, de @leeoniya. Licencia MIT. Es madura (~11k estrellas, 1.6.32).
- **Cuándo elegirlo:** Casos: Mostrar métricas temporales de un sensor; Comparar rendimiento de gráficas con tus propios datos.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; JavaScript; datos temporales ordenados; estilos y build distribuidos; hardware prerequisites; API de IA: no; JavaScript; datos temporales ordenados; estilos y build distribuidos.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/leeoniya/uPlot/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Grafica una serie de cien puntos y comprueba tiempos y escala Éxito: El cursor y los valores corresponden a los datos originales
- **Combina con:** `grafana` [10/bi], `swr` [9/componentes], `duckdb` [25/datos]
- **Riesgos y avisos:** Sin alternativas declaradas. Las cifras de rapidez del autor dependen de datos, navegador y equipo; no se garantiza rendimiento sin penalización.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-10-graficos.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Librerías de gráficos», lee `docs/alexandria/categoria-10-graficos.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-10-graficos.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
