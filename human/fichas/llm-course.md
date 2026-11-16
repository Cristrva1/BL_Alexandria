[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Aprender LLMs desde cero

# 📘 LLM Course

> Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender LLM de cero a producción.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 85.1k | Apache-2.0 | — | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## ¿Qué es?

Curso gratuito (Apache-2.0) de Maxime Labonne para aprender LLMs, con rutas de estudio y notebooks de Colab. Es muy popular (~85k estrellas). El autor coescribió el libro 'LLM Engineer's Handbook' basado en este curso. Último push en febrero de 2026.

## ¿Qué hace?

Se divide en tres partes: 'LLM Fundamentals' (matemáticas, Python y redes neuronales; opcional), 'The LLM Scientist' (preentrenamiento, fine-tuning, alineación, evaluación, cuantización) y 'The LLM Engineer' (aplicaciones, RAG, agentes, despliegue y seguridad). Incluye notebooks de herramientas propias como LLM AutoEval, LazyMergekit, LazyAxolotl y AutoQuant.

## ¿Cómo lo hace?

Es una hoja de ruta en Markdown con enlaces a artículos y notebooks de Google Colab. Algunos notebooks requieren GPU (Colab gratuito o de pago, RunPod) y claves de Hugging Face. Hay ejemplos de fine-tuning con Unsloth, TRL (QLoRA) y Axolotl.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Unsloth](unsloth.md) | Fine-tuning eficiente usado en el notebook 'Fine-tune Llama 3.1 with Unsloth'. | Abre el notebook en Colab con GPU; instala Unsloth según indique. |
| [TRL](trl.md) | Fine-tuning supervisado con QLoRA usado en el notebook de Mistral-7b. | Se instala dentro del notebook. |
| [PyTorch](pytorch.md) | Base técnica de la parte 'LLM Scientist'. (combinación por arquitectura) | Instálalo con soporte CUDA si vas a entrenar en local. |
| [awesome-machine-learning](awesome-machine-learning.md) | Combinación recíproca: awesome-machine-learning lo enlaza como «Ruta de estudio guiada para quien llega a la lista buscando aprender LLMs. (combinación por arquitectura)». | Orden indicado desde awesome-machine-learning: Combina la exploración de la lista con un curso estructurado. |
| [ML for Beginners](ml-for-beginners.md) | Combinación recíproca: ML for Beginners lo enlaza como «Tras el ML clásico, llm-course ofrece el recorrido hacia modelos de lenguaje (combinación por arquitectura)». | Orden indicado desde ML for Beginners: Completa el curso; después sigue con llm-course. |

**Notas:** Alternativas (elige una): llms-from-scratch, generative-ai-for-beginners. Combinación anterior con llama-factory eliminada: el curso no lo usa (y es alternativa de unsloth).

Estado en GitHub: activo · último push 2026-02-05 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mlabonne/llm-course/blob/main/README.md) · [2](https://mlabonne.github.io/blog/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Los recursos son públicos; Colab, GPU, nube y APIs pueden tener límites o coste |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es un mapa de aprendizaje con recursos externos y prácticas locales; no existe una instalación única para toda la ruta |
| Coste | El coste depende del proveedor o la ruta. Los recursos son públicos; Colab, GPU, nube y APIs pueden tener límites o coste |
| Equipo | Preparación según la ruta elegida. Navegador; Python y cómputo al practicar |

Es un mapa de aprendizaje con recursos externos y prácticas locales; no existe una instalación única para toda la ruta

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- Python y cómputo al practicar

1. Recorre la ruta de fundamentos y elige el notebook de cuantización solo después de revisar sus requisitos.
2. Comprueba: Puedes ubicar la diferencia entre entrenar, cuantizar y servir un modelo.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mlabonne/llm-course/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LLM Course para mi objetivo y necesito pasos guiados. Lee https://github.com/mlabonne/llm-course/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Recorre la ruta de fundamentos y elige el notebook de cuantización solo después de revisar sus requisitos.

**Qué comprobar:** Puedes ubicar la diferencia entre entrenar, cuantizar y servir un modelo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un plan de aprendizaje de LLM
- Estudiar cuantización GGUF

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un plan de aprendizaje de LLM; Estudiar cuantización GGUF | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un mapa de aprendizaje con recursos externos y prácticas locales; no existe una instalación única para toda la ruta

## Stack y modelos

- **Stack:** Navegador; Python y cómputo al practicar
- **Etiquetas:** `learning` `training` `notebooks`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LLMs from Scratch](llms-from-scratch.md) | 108k | Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en PyTorch paso a paso. |
| [Generative AI for Beginners](generative-ai-for-beginners.md) | 124k | Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa. |

## Enlaces

- 🐙 GitHub: [mlabonne/llm-course](https://github.com/mlabonne/llm-course)
- 🌐 Web: <https://mlabonne.github.io/blog/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mlabonne/llm-course/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
