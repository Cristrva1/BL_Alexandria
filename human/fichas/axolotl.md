[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 📚 Axolotl

> Framework de post-entrenamiento de LLM por configuración YAML: ajuste completo, LoRA/QLoRA, DPO/GRPO, multimodal y entrenamiento distribuido.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.7k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — fine-tuning por YAML; necesita GPU · corregido a mano

**Puntuación de calidad** 65/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de código abierto (Apache-2.0) de Axolotl AI. Muy activo y usado por la comunidad de ajuste fino.

## ¿Qué hace?

Entrena y ajusta LLM y modelos multimodales con ajuste completo, LoRA, QLoRA, cuantización, DPO, GRPO y otros métodos de RL, preparación de datos, optimizaciones de atención y entrenamiento distribuido o en la nube.

## ¿Cómo lo hace?

Se instala con uv o pip (o imágenes Docker) en Linux con GPU NVIDIA o AMD. Usa PyTorch, Transformers, PEFT, DeepSpeed y FSDP; los requisitos de VRAM dependen del modelo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DeepSpeed](deepspeed.md) | Axolotl integra DeepSpeed (incluido Ulysses) para entrenamiento distribuido y ahorro de memoria. | Instala DeepSpeed; después indica la configuración deepspeed en el YAML. |
| [PEFT](peft.md) | Los métodos LoRA y QLoRA de Axolotl se apoyan en PEFT. | Viene como dependencia; configura el adaptador en el YAML. |
| [Transformers](transformers.md) | Axolotl carga y guarda modelos en formato Hugging Face Transformers. | Indica el modelo base del Hub en el YAML. |
| [vLLM](vllm.md) | Para GRPO, Axolotl lanza un servidor vLLM (`axolotl vllm-serve`) que genera las muestras. | Instala vLLM; después arranca `axolotl vllm-serve` antes del entrenamiento. |

**Notas:** Alternativas (elige una): llama-factory, unsloth, torchtune.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v0.21.1 (2026-10-27) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/axolotl-ai-cloud/axolotl/blob/main/README.md) · [2](https://docs.axolotl.ai/docs/rlhf.html)</sub>

## Ver similares

Grupo **Fine-tuning de LLM**: Axolotl ocupa la posición 2 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Unsloth](unsloth.md) ⭐ recomendado | 82 | Si quieres afinar LLM con menos VRAM y más velocidad en una sola GPU. |
| 2 | **Axolotl** (esta ficha) | 65 | Si quieres configuraciones YAML reproducibles para fine-tuning en varias GPU. |
| 3 | [LLaMA-Factory](llama-factory.md) | 60 | Si quieres una interfaz web para afinar cientos de modelos sin programar. |
| 4 | [torchtune](torchtune.md) | 52 | Si prefieres recetas nativas de PyTorch fáciles de modificar. |

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/axolotl-ai-cloud/axolotl/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Axolotl para mi objetivo y necesito pasos guiados. Lee https://github.com/axolotl-ai-cloud/axolotl/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la instalación con uv del README en una máquina con GPU y lanza uno de los ejemplos de configuración QLoRA pequeños..

**Qué comprobar:** El entrenamiento arranca y guarda el adaptador al final..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- ajustar un modelo abierto con QLoRA a partir de un archivo YAML
- entrenar con GRPO o DPO en varias GPU

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: ajustar un modelo abierto con QLoRA a partir de un archivo YAML; entrenar con GRPO o DPO en varias GPU | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `training` `python` `llm` `gpu`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [torchtune](torchtune.md) | 5.8k | Biblioteca nativa de PyTorch para post-entrenamiento de LLM con recetas de ajuste completo, LoRA/QLoRA, DPO y destilación; ya sin mantenimiento activo. |
| [LLaMA-Factory](llama-factory.md) | 76k | Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código. |
| [Unsloth](unsloth.md) | 79.5k | App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales. |

## Enlaces

- 🐙 GitHub: [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl)
- 🌐 Web: <https://docs.axolotl.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/axolotl-ai-cloud/axolotl/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
