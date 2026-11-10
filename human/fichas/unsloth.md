[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ Unsloth

> Fine-tuning y ejecución local de LLM hasta 2 veces más rápido y con mucha menos memoria, ahora con UI.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 79.3k | Apache-2.0 | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

Afina modelos como Qwen, Llama o Gemma en una sola GPU y expórtalos a GGUF u Ollama. Ofrece notebooks gratuitos y una interfaz local.

## Por qué destaca

La forma más eficiente de afinar modelos en hardware modesto.

## Cómo funciona

Kernels optimizados a mano y cuantización reducen memoria y tiempo en LoRA y QLoRA.

## Instalación rápida

`pip install unsloth` o usa sus notebooks de Colab.

## Casos de uso

- Afinar un modelo con datos propios
- Entrenar en una GPU de consumo
- Exportar a Ollama

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres afinar un LLM con pocos recursos | necesitas muchas técnicas y una UI de entrenamiento; mira `llama-factory` |

**Limitaciones:** Requiere GPU NVIDIA para entrenar.

## Stack y modelos

- **Stack:** Python, Triton, PyTorch
- **Modelos / API:** Modelos abiertos.
- **Etiquetas:** `training` `local` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [TRL](trl.md) | 19.7k | Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LLaMA-Factory](llama-factory.md) | 76k | Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código. |

## Enlaces

- 🐙 GitHub: [unslothai/unsloth](https://github.com/unslothai/unsloth)
- 🌐 Web: <https://unsloth.ai/docs>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
