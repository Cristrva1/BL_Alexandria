[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 📚 scikit-learn

> La biblioteca de machine learning clásico en Python: clasificación, regresión, clustering, reducción de dimensión, selección de modelos y preprocesado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 68.2k | BSD-3-Clause | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Biblioteca de código abierto (BSD-3-Clause) desarrollada por una comunidad internacional desde 2007, con apoyo de Inria y patrocinadores. Imprescindible y muy madura.

## ¿Qué hace?

Ofrece algoritmos de aprendizaje supervisado y no supervisado, preprocesado, ingeniería de características, selección y evaluación de modelos, pipelines y utilidades de datos, con documentación y ejemplos extensos.

## ¿Cómo lo hace?

Se instala con pip o conda; requiere Python reciente, NumPy y SciPy. La API de estimadores se integra con pandas y con herramientas de seguimiento de experimentos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [JupyterLab](jupyterlab.md) | scikit-learn se usa habitualmente en cuadernos para explorar datos y modelos (combinación por arquitectura). | Instala scikit-learn en el entorno de JupyterLab. |
| [MLflow](mlflow.md) | MLflow incluye autolog para scikit-learn que registra parámetros, métricas y modelos. | Instala mlflow; después llama a `mlflow.sklearn.autolog()` antes de entrenar. |
| [ML for Beginners](ml-for-beginners.md) | El curso ML for Beginners enseña machine learning clásico con scikit-learn. | Sigue las lecciones con scikit-learn instalado. |
| [pandas](pandas.md) | Combinación recíproca: pandas lo enlaza como «scikit-learn acepta DataFrames de pandas como entrada y puede devolver salidas en pandas con `set_output(transform="pandas")`». | Orden indicado desde pandas: Prepara los datos con pandas; después pásalos a los estimadores de scikit-learn. |

**Notas:** No está pensado para deep learning ni GPU; para eso usa pytorch o jax.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 1.9.1 (2026-09-11) · licencia declarada BSD-3-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/scikit-learn/scikit-learn/blob/main/README.rst) · [2](https://scikit-learn.org) · [3](https://mlflow.org/docs/latest/ml/traditional-ml/sklearn/)</sub>

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
pip install -U scikit-learn
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/scikit-learn/scikit-learn/blob/main/README.rst)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar scikit-learn para mi objetivo y necesito pasos guiados. Lee https://github.com/scikit-learn/scikit-learn/blob/main/README.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install -U scikit-learn` y entrena un clasificador sobre el conjunto iris incluido..

**Qué comprobar:** Obtienes la precisión del modelo en validación cruzada..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- entrenar y validar un clasificador sobre datos tabulares
- construir un pipeline de preprocesado y modelo reproducible

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: entrenar y validar un clasificador sobre datos tabulares; construir un pipeline de preprocesado y modelo reproducible | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `ml` `python` `library` `data`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)
- 🌐 Web: <https://scikit-learn.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/scikit-learn/scikit-learn/blob/main/README.rst)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
