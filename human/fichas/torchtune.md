[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 📚 torchtune

> Biblioteca nativa de PyTorch para post-entrenamiento de LLM con recetas de ajuste completo, LoRA/QLoRA, DPO y destilación; ya sin mantenimiento activo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.8k | BSD-3-Clause | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Puntuación de calidad** 52/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (BSD-3-Clause) de Meta/PyTorch. Su README avisa de que ya no se mantiene activamente: el desarrollo terminó en 2025. Sigue siendo una referencia útil de recetas en PyTorch puro.

## ¿Qué hace?

Ofrece recetas de ajuste completo, LoRA, QLoRA, DPO, PPO, destilación y cuantización para modelos como Llama, Qwen y Gemma, con configuraciones YAML, checkpoints compatibles con Hugging Face y evaluación con EleutherAI Eval.

## ¿Cómo lo hace?

Se instala con pip junto a torch, torchvision y torchao; la CLI `tune` descarga modelos y ejecuta recetas en una o varias GPU.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | torchtune está construida sobre PyTorch nativo. | Instala PyTorch, torchvision y torchao; después torchtune. |
| [LM Evaluation Harness](lm-eval-harness.md) | torchtune incluye una receta para evaluar modelos con LM Evaluation Harness de EleutherAI. | Instala lm-eval; después ejecuta la receta eleuther_eval. |
| [Transformers](transformers.md) | Los checkpoints se pueden cargar y guardar en formato Hugging Face para usarlos con Transformers. | Usa el checkpointer de Hugging Face en la configuración. |

**Notas:** Alternativas (elige una): axolotl, llama-factory, unsloth, todas con mantenimiento activo.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada v0.6.1 (2025-04-07) · licencia declarada BSD-3-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/meta-pytorch/torchtune/blob/main/README.md) · [2](https://pytorch.org/torchtune/main/tutorials/e2e_flow.html) · [3](https://github.com/meta-pytorch/torchtune/issues/2883)</sub>

## Ver similares

Grupo **Fine-tuning de LLM**: torchtune ocupa la posición 4 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Unsloth](unsloth.md) ⭐ recomendado | 82 | Si quieres afinar LLM con menos VRAM y más velocidad en una sola GPU. |
| 2 | [Axolotl](axolotl.md) | 65 | Si quieres configuraciones YAML reproducibles para fine-tuning en varias GPU. |
| 3 | [LLaMA-Factory](llama-factory.md) | 60 | Si quieres una interfaz web para afinar cientos de modelos sin programar. |
| 4 | **torchtune** (esta ficha) | 52 | Si prefieres recetas nativas de PyTorch fáciles de modificar. |

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
pip install torchtune
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/meta-pytorch/torchtune/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar torchtune para mi objetivo y necesito pasos guiados. Lee https://github.com/meta-pytorch/torchtune/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install torchtune` (junto a torch, torchvision y torchao) y lista las recetas con `tune ls`..

**Qué comprobar:** La CLI muestra las recetas y configuraciones disponibles..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- estudiar recetas limpias de ajuste fino en PyTorch puro
- reproducir un ajuste LoRA con configuraciones existentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: estudiar recetas limpias de ajuste fino en PyTorch puro; reproducir un ajuste LoRA con configuraciones existentes | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Sin mantenimiento activo: según su README, el desarrollo terminó en 2025; no esperes soporte para modelos nuevos.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `training` `python` `pytorch` `llm`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Axolotl](axolotl.md) | 12.7k | Framework de post-entrenamiento de LLM por configuración YAML: ajuste completo, LoRA/QLoRA, DPO/GRPO, multimodal y entrenamiento distribuido. |
| [LLaMA-Factory](llama-factory.md) | 76k | Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código. |
| [Unsloth](unsloth.md) | 79.5k | App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales. |

## Enlaces

- 🐙 GitHub: [meta-pytorch/torchtune](https://github.com/meta-pytorch/torchtune)
- 🌐 Web: <https://pytorch.org/torchtune/main/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/meta-pytorch/torchtune/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
