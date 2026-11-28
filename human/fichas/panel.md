[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Apps de datos en Python

# 📚 Panel

> Framework de HoloViz para dashboards y apps de datos en Python que funcionan igual en un notebook y como aplicación web servida con `panel serve`.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.8k | BSD-3-Clause | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 55/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de código abierto (BSD-3-Clause) del ecosistema HoloViz, respaldado por Anaconda y otros patrocinadores. Activo y maduro.

## ¿Qué hace?

Permite crear dashboards y aplicaciones de datos con widgets enlazados a funciones (`pn.bind`) o a clases reactivas (Param). Solo recalcula lo que depende del control que cambió. Muestra gráficos de Matplotlib, Plotly, Bokeh, HoloViews/hvPlot, Altair, ECharts, deck.gl, VTK y Folium, y admite apps multipágina con autenticación. Lumen añade un asistente de chat sobre la app.

## ¿Cómo lo hace?

Se instala con pip o conda. Usa Bokeh como servidor y capa de comunicación; la misma app se ve en Jupyter, JupyterLab, VS Code, Colab o marimo y se sirve con `panel serve`. También puede compilarse a WebAssembly (Pyodide).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [JupyterLab](jupyterlab.md) | Las apps de Panel se renderizan dentro de celdas de Jupyter/JupyterLab mientras se desarrollan. | Instala Panel en el entorno de JupyterLab; después llama a `pn.extension()` en el notebook. |
| [marimo](marimo.md) | Panel documenta su uso dentro de notebooks marimo. | Instala Panel junto a marimo; después muestra los componentes en una celda. |
| [Claude Code](claude-code.md) | HoloViz skills orientan a asistentes de código como Claude Code para crear, revisar y probar apps de Panel con las APIs actuales. | Instala `holoviz-skills` y ejecuta `holoviz-skills install`; después pide la app al asistente. |
| [deck.gl](deck-gl.md) | Panel incluye un pane DeckGL para mostrar visualizaciones geoespaciales de deck.gl. | Instala Panel; después usa `pn.pane.DeckGL` con la especificación de deck.gl. |
| [echarts](echarts.md) | Panel incluye un pane ECharts para gráficos de Apache ECharts. | Instala Panel; después usa `pn.pane.ECharts` con las opciones del gráfico. |

**Notas:** Panel publica una comparación con Streamlit en su documentación; ambos están agrupados como alternativas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.10.0 (2026-10-23) · licencia declarada BSD-3-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/holoviz/panel/blob/main/README.md) · [2](https://panel.holoviz.org/reference/panes/DeckGL.html) · [3](https://panel.holoviz.org/reference/panes/ECharts.html) · [4](https://skills.holoviz.org/)</sub>

## Ver similares

Grupo **Apps web de datos en Python**: Panel ocupa la posición 5 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [streamlit](streamlit.md) ⭐ recomendado | 76 | Si quieres convertir un script de datos en app web con la menor curva. |
| 2 | [Reflex](reflex.md) | 70 | Si quieres una app web completa (frontend y backend) solo en Python. |
| 3 | [Gradio](gradio.md) | 70 | Si quieres una demo de un modelo de IA con entradas y salidas en minutos. |
| 4 | [NiceGUI](nicegui.md) | 68 | Si quieres una interfaz web en Python con control fino de componentes. |
| 5 | **Panel** (esta ficha) | 55 | Si trabajas con el ecosistema HoloViz y notebooks y quieres dashboards complejos. |

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
pip install panel
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/holoviz/panel/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Panel para mi objetivo y necesito pasos guiados. Lee https://github.com/holoviz/panel/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install panel`, crea `app.py` con un widget enlazado a un gráfico y ejecútalo con `panel serve app.py --dev`..

**Qué comprobar:** El dashboard se abre en el navegador y responde a los controles..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- convertir un análisis de notebook en un dashboard interactivo para el equipo
- crear una plataforma interna con varias páginas, tablas editables y autenticación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: convertir un análisis de notebook en un dashboard interactivo para el equipo; crear una plataforma interna con varias páginas, tablas editables y autenticación | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `python` `dashboard` `dataviz` `framework`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Reflex](reflex.md) | 29k | Framework para crear aplicaciones web completas (frontend y backend) solo con Python, con estado en clases, componentes y despliegue propio o gestionado. |
| [NiceGUI](nicegui.md) | 16.3k | Framework Python para interfaces web en el navegador con botones, gráficos, mapas, tablas y escenas 3D, útil para paneles, robótica y herramientas internas. |
| [streamlit](streamlit.md) | 46.4k | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. |
| [Gradio](gradio.md) | 44.1k | Librería Python para crear y compartir apps web de modelos de ML en minutos. |

## Enlaces

- 🐙 GitHub: [holoviz/panel](https://github.com/holoviz/panel)
- 🌐 Web: <https://panel.holoviz.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/holoviz/panel/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
