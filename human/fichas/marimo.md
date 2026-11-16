[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 🗃️ marimo

> Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.6k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

marimo, notebook reactivo de Python que se guarda como script `.py`, de marimo-team. Licencia Apache-2.0. Es maduro y activo (~24k estrellas, 0.25.2).

## ¿Qué hace?

Al ejecutar una celda se actualizan automáticamente las dependientes, sin estado oculto. Los notebooks se versionan en Git, se ejecutan como scripts y se publican como apps web o diapositivas; incluye celdas SQL, elementos de UI interactivos y asistencia con IA.

## ¿Cómo lo hace?

Se instala con `pip install marimo` o conda (`marimo tutorial intro` para empezar). Puede instalar paquetes al importarlos, guardar dependencias inline en el archivo y usarse desde una extensión de VS Code o en WebAssembly.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | Celdas SQL nativas. | Instala DuckDB en el entorno. |
| [Polars](polars.md) | DataFrames con visualización interactiva. | Instala Polars. |
| [Ollama](ollama.md) | Modelo local para el asistente de IA del editor. (combinación por arquitectura) | Configura el proveedor de IA de marimo apuntando a Ollama. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (11). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Anthropic's Prompt Engineering Tutorial](prompt-eng-tutorial.md) · [D3.js](d3.md) · [data-analyst-roadmap](data-analyst-roadmap.md) · [how-to-train-your-gpt](how-to-train-your-gpt.md) · [machine-learning-for-trading](machine-learning-for-trading.md) · [nautilus_trader](nautilus-trader.md) · [ODM](odm.md) · [qlib](qlib.md) · [tensorflow](tensorflow.md) · [vectorbt](vectorbt.md) · [WebODM](webodm.md)

**Notas:** Alternativa (elige una): jupyterlab.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 0.25.2 (2026-10-19) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/marimo-team/marimo/blob/main/README.md) · [2](https://docs.marimo.io/guides/apps.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Notebook básico sin API; AI opcional con claves o modelos locales y marimo pair con su agente |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Documenta pair con Claude Code y Codex; usar un notebook local no implica que el asistente AI también sea local |
| Coste | El coste depende del proveedor o la ruta. Notebook básico sin API; AI opcional con claves o modelos locales y marimo pair con su agente |
| Equipo | Preparación según la ruta elegida. Python; entorno de notebook; CSV pequeño; modelo solo para funciones AI |

Documenta pair con Claude Code y Codex; usar un notebook local no implica que el asistente AI también sea local

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- entorno de notebook
- CSV pequeño
- modelo solo para funciones AI

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (python):**

```
pip install marimo && marimo tutorial intro
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/marimo-team/marimo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar marimo para mi objetivo y necesito pasos guiados. Lee https://github.com/marimo-team/marimo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Completa el tutorial intro y modifica una variable para ver qué celdas se recalculan.

**Qué comprobar:** Puedes reconocer dependencias reactivas y el archivo Python guardado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar datos en un notebook
- Convertir un análisis en una app

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar datos en un notebook; Convertir un análisis en una app | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta pair con Claude Code y Codex; usar un notebook local no implica que el asistente AI también sea local

## Stack y modelos

- **Stack:** Python; entorno de notebook; CSV pequeño; modelo solo para funciones AI
- **Etiquetas:** `notebooks` `data` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [JupyterLab](jupyterlab.md) | 15.4k | Entorno web de Project Jupyter con notebooks, terminal, editor de texto y explorador de archivos, ampliable mediante extensiones. |

## Enlaces

- 🐙 GitHub: [marimo-team/marimo](https://github.com/marimo-team/marimo)
- 🌐 Web: <https://marimo.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/marimo-team/marimo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
