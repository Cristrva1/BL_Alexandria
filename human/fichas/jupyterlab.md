[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 🖥️ JupyterLab

> Entorno web de Project Jupyter con notebooks, terminal, editor de texto y explorador de archivos, ampliable mediante extensiones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.4k | BSD-3-Clause | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Interfaz de nueva generación de Project Jupyter (organización jupyterlab), en TypeScript y Python con licencia BSD-3-Clause. Es el repositorio canónico de la experiencia de notebook de Jupyter; la rama 3 dejó de mantenerse en 2024. Versión v4.6.6 (noviembre de 2026), ~15k estrellas.

## ¿Qué hace?

Ofrece en el navegador notebooks, consolas, terminal, editor de texto, explorador de archivos y salidas enriquecidas en paneles reorganizables. Se amplía con extensiones distribuidas por PyPI, conda o npm.

## ¿Cómo lo hace?

Se instala con `pip install jupyterlab`, conda o mamba (conda-forge) y se abre con `jupyter lab`, que arranca un servidor Jupyter local. Los kernels (ipykernel para Python u otros lenguajes) ejecutan el código. Las extensiones precompiladas no requieren compilar; las de código fuente sí.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | Entrenar y depurar modelos de forma interactiva en notebooks. (combinación por arquitectura) | Instala PyTorch en el entorno del kernel. |
| [tensorflow](tensorflow.md) | Experimentar con modelos de TensorFlow paso a paso en notebooks. (combinación por arquitectura) | Instala TensorFlow en el entorno del kernel. |
| [DuckDB](duckdb.md) | Consultas SQL sobre CSV y Parquet dentro del notebook. (combinación por arquitectura) | Añade el paquete `duckdb` al kernel. |
| [Polars](polars.md) | DataFrames rápidos para análisis interactivo. (combinación por arquitectura) | Añade `polars` al kernel. |
| [Apache Iceberg](apache-iceberg.md) | Combinación recíproca: Apache Iceberg lo enlaza como «Explorar tablas con PyIceberg, DuckDB o Spark desde notebooks. (combinación por arquitectura)». | Orden indicado desde Apache Iceberg: Instala JupyterLab en el mismo entorno que PyIceberg. |
| [Delta Lake](delta-lake.md) | Combinación recíproca: Delta Lake lo enlaza como «Explorar tablas Delta con PySpark, delta-rs o DuckDB desde notebooks. (combinación por arquitectura)». | Orden indicado desde Delta Lake: Instala JupyterLab en el entorno con PySpark o deltalake. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (5). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Backtesting.py](backtesting-py.md) · [deck.gl](deck-gl.md) · [kepler.gl](kepler-gl.md) · [OpenBB Open Data Platform](openbb.md) · [yfinance](yfinance.md)

**Notas:** Alternativa (elige una): marimo. Los notebooks .ipynb se versionan mal en Git; considera jupytext o marimo si te importa.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v4.6.6 (2026-11-06) · licencia declarada BSD-3-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/jupyterlab/jupyterlab/blob/main/README.md) · [2](https://jupyterlab.readthedocs.io/en/stable/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. Sin coste de modelo. Las extensiones de IA (p. ej. Jupyter AI) se configuran aparte con sus proveedores. |
| Equipo | Equipo normal; revisar dependencias. Python con pip, conda o mamba; los kernels y extensiones añaden sus propias dependencias. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y una copia de datos o archivos para la primera prueba.

1. Crea un entorno de Python e instala JupyterLab con pip, conda o mamba.
2. Ejecuta `jupyter lab` en una carpeta de prueba y crea un notebook.
3. Ejecuta unas celdas y guarda el notebook antes de instalar extensiones.

**Entrada documentada (consulta la sintaxis original):**

```
pip install jupyterlab
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/jupyterlab/jupyterlab/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://jupyterlab.readthedocs.io/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar JupyterLab para mi objetivo y necesito pasos guiados. Lee https://github.com/jupyterlab/jupyterlab/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un notebook, carga un CSV ficticio y dibuja un gráfico simple.

**Qué comprobar:** El notebook guarda código, tabla y gráfico al reabrirlo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Analizar datos de muestra en un notebook
- Documentar un experimento con código y resultados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Analizar datos de muestra en un notebook; Documentar un experimento con código y resultados | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json, pyproject.toml
- **Etiquetas:** `notebooks` `data` `python` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [marimo](marimo.md) | 23.6k | Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. |

## Enlaces

- 🐙 GitHub: [jupyterlab/jupyterlab](https://github.com/jupyterlab/jupyterlab)
- 🌐 Web: <https://jupyterlab.readthedocs.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jupyterlab/jupyterlab/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
