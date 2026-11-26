[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Librerías de gráficos

# 📈 uPlot

> Biblioteca compacta de gráficos de series temporales en JavaScript, orientada a renderizar datos con Canvas y controles programables.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.6k | MIT | JavaScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

μPlot, librería compacta de gráficos de series temporales sobre Canvas 2D, de @leeoniya. Licencia MIT. Es madura (~11k estrellas, 1.6.32).

## ¿Qué hace?

Dibuja series temporales, líneas, áreas, OHLC y barras muy rápido y con poca memoria (~50 KB minificado), apto para cientos de miles de puntos y actualizaciones en streaming. Prioriza rendimiento sobre variedad de tipos y animaciones.

## ¿Cómo lo hace?

Se instala con `npm install uplot` o se carga desde `dist/`. Es JavaScript puro sin dependencias; los envoltorios para frameworks son de la comunidad.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Grafana](grafana.md) | Grafana usa uPlot en sus paneles de series temporales. (combinación por arquitectura) | Para paneles completos usa Grafana; para embeber, uPlot. |
| [swr](swr.md) | Actualizar series en vivo con la recarga de datos de SWR. (combinación por arquitectura) | Obtén los datos con SWR y llama a `setData`. |
| [DuckDB](duckdb.md) | Agregar series largas antes de pintarlas. (combinación por arquitectura) | Agrupa por intervalo en DuckDB. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 1.6.32 (2025-03-14) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/leeoniya/uPlot/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa modelo ni servicios por defecto; los datos y el alojamiento son aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Las cifras de rapidez del autor dependen de datos, navegador y equipo; no se garantiza rendimiento sin penalización |
| Coste | Sin pago a un modelo en la ruta básica. No usa modelo ni servicios por defecto; los datos y el alojamiento son aparte |
| Equipo | Preparación según la ruta elegida. JavaScript; datos temporales ordenados; estilos y build distribuidos |

Las cifras de rapidez del autor dependen de datos, navegador y equipo; no se garantiza rendimiento sin penalización

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- JavaScript
- datos temporales ordenados
- estilos y build distribuidos

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/leeoniya/uPlot/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar uPlot para mi objetivo y necesito pasos guiados. Lee https://github.com/leeoniya/uPlot/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Grafica una serie de cien puntos y comprueba tiempos y escala.

**Qué comprobar:** El cursor y los valores corresponden a los datos originales.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Mostrar métricas temporales de un sensor
- Comparar rendimiento de gráficas con tus propios datos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Mostrar métricas temporales de un sensor; Comparar rendimiento de gráficas con tus propios datos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las cifras de rapidez del autor dependen de datos, navegador y equipo; no se garantiza rendimiento sin penalización

## Stack y modelos

- **Stack:** JavaScript; datos temporales ordenados; estilos y build distribuidos
- **Etiquetas:** `dataviz` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [leeoniya/uPlot](https://github.com/leeoniya/uPlot)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/leeoniya/uPlot/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
