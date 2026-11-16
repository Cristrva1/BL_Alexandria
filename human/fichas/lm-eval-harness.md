[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📚 LM Evaluation Harness

> Arnés estándar de EleutherAI para evaluar modelos de lenguaje en cientos de benchmarks académicos con backends Hugging Face, vLLM, SGLang o APIs.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.5k | MIT | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de evaluación de código abierto (MIT) de EleutherAI. Estándar de facto: es el motor del Open LLM Leaderboard de Hugging Face y lo usan muchos laboratorios. Activo.

## ¿Qué hace?

Evalúa modelos de lenguaje en más de 60 benchmarks académicos con cientos de subtareas, en modos few-shot y generativos, con plantillas de prompt configurables, eliminación de trazas de razonamiento, modelos dirigidos (steering) y salida reproducible.

## ¿Cómo lo hace?

Se instala con pip; desde finales de 2025 los backends son extras (`lm_eval[hf]`, `lm_eval[vllm]`…). Las tareas se definen en YAML y Jinja; los modelos locales necesitan GPU según su tamaño.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | lm-eval-harness incluye un backend vLLM para evaluar más rápido. | Instala `lm_eval[vllm]`; después usa `--model vllm`. |
| [SGLang](sglang.md) | Desde 2025 incluye soporte para SGLang como backend de evaluación. | Instala SGLang; después usa el backend sglang. |
| [Transformers](transformers.md) | El backend hf carga modelos de Hugging Face Transformers. | Instala `lm_eval[hf]`; después indica el modelo con `--model_args pretrained=...`. |
| [torchtune](torchtune.md) | Combinación recíproca: torchtune lo enlaza como «torchtune incluye una receta para evaluar modelos con LM Evaluation Harness de EleutherAI». | Orden indicado desde torchtune: Instala lm-eval; después ejecuta la receta eleuther_eval. |
| [Gemma (biblioteca JAX)](gemma.md) | Combinación recíproca: Gemma (biblioteca JAX) lo enlaza como «LM Evaluation Harness puede medir el rendimiento de un Gemma ajustado frente al original (combinación por arquitectura)». | Orden indicado desde Gemma (biblioteca JAX): Exporta o carga el modelo en un backend compatible; después evalúa. |

**Notas:** Las puntuaciones dependen de la versión de la tarea y del prompt; regístralas junto a los resultados.

Estado en GitHub: activo · último push 2026-11-04 · última versión publicada v0.4.13 (2026-08-31) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

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
pip install "lm_eval[hf]"
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LM Evaluation Harness para mi objetivo y necesito pasos guiados. Lee https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install "lm_eval[hf]"` y evalúa un modelo pequeño de Hugging Face en una tarea ligera con `lm_eval --model hf --tasks ...`..

**Qué comprobar:** Obtienes una tabla con la métrica de la tarea y su error estándar..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- comparar un modelo ajustado con su base en MMLU, HellaSwag o GSM8K
- reproducir resultados de tablas de clasificación con la misma configuración

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: comparar un modelo ajustado con su base en MMLU, HellaSwag o GSM8K; reproducir resultados de tablas de clasificación con la misma configuración | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `evaluation` `python` `llm` `benchmark`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
- 🌐 Web: <https://www.eleuther.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
