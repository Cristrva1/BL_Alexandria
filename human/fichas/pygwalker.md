[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 📚 PyGWalker

> Convierte un DataFrame de pandas o Polars en una interfaz de exploración visual tipo Tableau dentro de Jupyter, Streamlit o marimo, arrastrando campos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (Apache-2.0) de Kanaries, enlace Python de Graphic Walker. Kanaries ofrece además servicios en la nube y una app de escritorio. Último push en septiembre de 2026.

## ¿Qué hace?

Convierte un DataFrame de pandas, Polars o una tabla de PyArrow (o una conexión a base de datos) en una interfaz de exploración visual: arrastrar campos para crear gráficos, filtrar, agregar y guardar la configuración de las vistas. Funciona en Jupyter, JupyterLab, Jupyter Lite, VS Code, Colab, Kaggle y Streamlit.

## ¿Cómo lo hace?

Se instala con pip o conda. `pyg.walk(df)` muestra el widget; el parámetro `computation` decide si las consultas se calculan en el navegador, en el kernel local con DuckDB (para datos más grandes) o en la nube de Kanaries.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [pandas](pandas.md) | PyGWalker recibe DataFrames de pandas en `pyg.walk(df)`. | Carga los datos con pandas; después llama a `pyg.walk(df)`. |
| [Polars](polars.md) | PyGWalker acepta también DataFrames de Polars. | Carga los datos con Polars; después pásalos a `pyg.walk`. |
| [DuckDB](duckdb.md) | Con `computation="kernel"` PyGWalker usa DuckDB en el kernel de Python para calcular consultas sobre conjuntos más grandes. | Instala PyGWalker (incluye la dependencia); después usa `computation="kernel"`. |
| [JupyterLab](jupyterlab.md) | PyGWalker funciona como widget en Jupyter Notebook y JupyterLab. | Instala PyGWalker en el entorno de JupyterLab; después ejecútalo en una celda. |
| [streamlit](streamlit.md) | PyGWalker documenta su uso dentro de apps de Streamlit para publicar la exploración en web. | Instala PyGWalker en la app de Streamlit; después usa su componente para Streamlit. |

Estado en GitHub: activo · último push 2026-09-05 · última versión publicada 0.5.0.1 (2026-04-04) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Kanaries/pygwalker/blob/main/README.md)</sub>

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
pip install pygwalker
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Kanaries/pygwalker/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PyGWalker para mi objetivo y necesito pasos guiados. Lee https://github.com/Kanaries/pygwalker/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install pygwalker` y, en un notebook, ejecuta `pyg.walk(df)` con un DataFrame..

**Qué comprobar:** Aparece una interfaz donde arrastras columnas para crear gráficos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- explorar un conjunto de datos nuevo con gráficos de arrastrar y soltar sin escribir código de visualización
- publicar una exploración interactiva de datos dentro de una app de Streamlit

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: explorar un conjunto de datos nuevo con gráficos de arrastrar y soltar sin escribir código de visualización; publicar una exploración interactiva de datos dentro de una app de Streamlit | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. La opción `computation="cloud"` y algunas funciones de IA usan servicios de Kanaries; el último push es de septiembre de 2026 (ritmo moderado).

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `dataviz` `python` `jupyter` `eda`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Kanaries/pygwalker](https://github.com/Kanaries/pygwalker)
- 🌐 Web: <https://kanaries.net/pygwalker>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Kanaries/pygwalker/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
