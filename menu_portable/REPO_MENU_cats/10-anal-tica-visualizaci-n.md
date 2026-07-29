# 10. Analítica & Visualización — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `streamlit`
role=platform · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Welcome to Streamlit 👋.
**Stack:** python, typescript
**Repo:** https://github.com/streamlit/streamlit.git

**Instalación** [~]: `git clone https://github.com/streamlit/streamlit.git && cd streamlit && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres <img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b
**Evita si:** —
**Combina con:** `uplot`

## `uplot`
role=library · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** A small (~50 KB min), fast chart for time series, lines, areas, ohlc & bars _(MIT Licensed)_.
**Stack:** javascript/typescript, python, typescript, javascript, react
**Repo:** https://github.com/leeoniya/uPlot.git

**Instalación** [~]: `pip install uplot   (o: uv add uplot)`
_Nombre PyPI puede diferir de 'uPlot'; verifica en pypi.org._

**Elige si:** quieres a small ([~50 kb min](https://github.com/leeoniya/uplot/tree/master/dist/uplot.i
**Evita si:** —
**Combina con:** `streamlit`
