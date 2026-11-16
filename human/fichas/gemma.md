[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Modelos abiertos y fundacionales

# 📚 Gemma (biblioteca JAX)

> Biblioteca oficial de Google DeepMind para usar y ajustar los modelos de pesos abiertos Gemma en JAX: muestreo, multimodal, LoRA y ajuste fino.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.9k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; requiere programar con él; necesita GPU

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (Apache-2.0) de Google DeepMind para la familia Gemma. Activa, con documentación en gemma-llm.readthedocs.io.

## ¿Qué hace?

Permite cargar checkpoints Gemma, muestrear en modo chat (incluidas entradas de imagen en modelos multimodales), ajustar con LoRA o ajuste completo, cuantizar y entrenar con utilidades de JAX.

## ¿Cómo lo hace?

Requiere instalar JAX para CPU, GPU o TPU y después `pip install gemma`; los checkpoints se descargan aceptando los términos de Gemma. Los modelos grandes necesitan GPU o TPU con memoria suficiente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [JAX](jax.md) | La biblioteca está construida sobre JAX. | Instala JAX según tu hardware; después gemma. |
| [JupyterLab](jupyterlab.md) | Los ejemplos y tutoriales de Gemma se ejecutan como cuadernos (combinación por arquitectura). | Instala gemma en el entorno de JupyterLab. |
| [LM Evaluation Harness](lm-eval-harness.md) | LM Evaluation Harness puede medir el rendimiento de un Gemma ajustado frente al original (combinación por arquitectura). | Exporta o carga el modelo en un backend compatible; después evalúa. |

**Notas:** Para usar Gemma en PyTorch o con Ollama, hay rutas alternativas fuera de esta biblioteca.

Estado en GitHub: activo · último push 2026-10-28 · última versión publicada v4.0.1 (2026-05-20) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google-deepmind/gemma/blob/main/README.md) · [2](https://gemma-llm.readthedocs.io) · [3](https://ai.google.dev/gemma/terms)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

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
pip install gemma
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/google-deepmind/gemma/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Gemma (biblioteca JAX) para mi objetivo y necesito pasos guiados. Lee https://github.com/google-deepmind/gemma/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala JAX para tu hardware y después `pip install gemma`; ejecuta el ejemplo de muestreo con un checkpoint pequeño..

**Qué comprobar:** El modelo responde al prompt de ejemplo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- chatear con un modelo Gemma en Python con JAX
- ajustar Gemma con LoRA en GPU o TPU

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: chatear con un modelo Gemma en Python con JAX; ajustar Gemma con LoRA en GPU o TPU | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. El código es Apache-2.0, pero los pesos de Gemma se rigen por los términos de uso de Gemma de Google.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `model` `python` `jax` `llm`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [google-deepmind/gemma](https://github.com/google-deepmind/gemma)
- 🌐 Web: <https://gemma-llm.readthedocs.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-deepmind/gemma/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
