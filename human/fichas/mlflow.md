[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📡 MLflow

> Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28.8k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

MLflow, plataforma open source de ingeniería de IA para agentes, LLM y modelos de ML. Licencia Apache-2.0. Es muy madura (~29k estrellas, v3.18.0) y el README cita más de 60 millones de descargas mensuales.

## ¿Qué hace?

Para apps de LLM ofrece trazas basadas en OpenTelemetry, evaluación, gestión y optimización de prompts y un AI Gateway. Para ML clásico mantiene seguimiento de experimentos, registro de modelos y despliegue. Tiene SDK para Python, TypeScript/JavaScript, Java y R.

## ¿Cómo lo hace?

Se arranca un servidor con `uvx mlflow server` o `pip install mlflow`, y se instrumenta el código con autolog o el SDK. Incluye un asistente que configura el proyecto con Claude Code, Codex u OpenCode. Para producción necesita base de datos y almacenamiento de artefactos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DSPy](dspy.md) | Trazado nativo de DSPy con autolog. | Activa `mlflow.dspy.autolog()`. |
| [Transformers](transformers.md) | Flavor nativo para registrar y servir modelos de Transformers. | Registra el pipeline con `mlflow.transformers`. |
| [DeepEval](deepeval.md) | Métricas de DeepEval disponibles como scorers de terceros en MLflow. | Instala deepeval y úsalo desde la evaluación de MLflow. |
| [Ragas](ragas.md) | Métricas de Ragas disponibles como scorers de terceros. | Instala ragas y úsalo desde la evaluación de MLflow. |
| [qlib](qlib.md) | Combinación recíproca: qlib lo enlaza como «El recorder de Qlib se basa en MLflow». | Orden indicado desde qlib: Configura el URI de MLflow para los experimentos. |
| [Apache Airflow](airflow.md) | Combinación recíproca: Apache Airflow lo enlaza como «Airflow programa los pasos de entrenamiento y evaluación y MLflow registra parámetros, métricas y modelos de cada ejecución (combinación por arquitectura)». | Orden indicado desde Apache Airflow: Servidor de MLflow primero; después tareas de Airflow que usen su cliente con MLFLOW_TRACKING_URI. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (4). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Dagster](dagster.md) · [Prefect](prefect.md) · [PyTorch Lightning](pytorch-lightning.md) · [scikit-learn](scikit-learn.md)

**Notas:** Alternativas (elige una): langfuse.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.18.0 (2026-11-04) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mlflow/mlflow/blob/master/README.md) · [2](https://mlflow.org/docs/latest/genai/tracing/integrations/listing/dspy) · [3](https://mlflow.org/docs/latest/ml/deep-learning/transformers/) · [4](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/third-party/deepeval) · [5](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/third-party/ragas)</sub>

## Ver similares

Grupo **Observabilidad y trazas de LLM**: MLflow ocupa la posición 3 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [langfuse](langfuse.md) ⭐ recomendado | 79 | Si quieres trazas, prompts y evaluaciones de LLM auto-hospedables con la comunidad más grande. |
| 2 | [Opik](opik.md) | 75 | Si quieres trazas y evaluación de LLM con integración en pruebas. |
| 3 | **MLflow** (esta ficha) | 70 | Si ya gestionas experimentos y modelos de ML clásico y quieres sumar trazas de LLM. |
| 4 | [Phoenix](phoenix.md) | 53 | Si quieres observabilidad basada en OpenTelemetry y evaluación local en notebooks. |
| 5 | [Helicone](helicone.md) | 50 | Si quieres observabilidad como proxy con solo cambiar la URL base. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Seguimiento básico sin API de IA; evaluadores, modelos y alojamiento gestionado pueden generar costes |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El wizard documenta Claude Code y Codex para añadir instrumentación; no es una autorización para cambiar automáticamente proyectos reales |
| Coste | El coste depende del proveedor o la ruta. Seguimiento básico sin API de IA; evaluadores, modelos y alojamiento gestionado pueden generar costes |
| Equipo | Preparación según la ruta elegida. uv o Python; app y datos ficticios; agente opcional para instrumentar |

El wizard documenta Claude Code y Codex para añadir instrumentación; no es una autorización para cambiar automáticamente proyectos reales

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv o Python
- app y datos ficticios
- agente opcional para instrumentar

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uvx mlflow server
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mlflow/mlflow/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MLflow para mi objetivo y necesito pasos guiados. Lee https://github.com/mlflow/mlflow/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inicia el servidor de prueba y registra una ejecución pequeña con parámetros y resultado.

**Qué comprobar:** Puedes abrir la ejecución y comparar sus datos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Registrar experimentos de ML
- Añadir trazas a una app de IA

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Registrar experimentos de ML; Añadir trazas a una app de IA | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El wizard documenta Claude Code y Codex para añadir instrumentación; no es una autorización para cambiar automáticamente proyectos reales

## Stack y modelos

- **Stack:** uv o Python; app y datos ficticios; agente opcional para instrumentar
- **Etiquetas:** `observability` `training` `evaluation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Enlaces

- 🐙 GitHub: [mlflow/mlflow](https://github.com/mlflow/mlflow)
- 🌐 Web: <https://mlflow.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mlflow/mlflow/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
