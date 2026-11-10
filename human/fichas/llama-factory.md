[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ LLaMA-Factory

> Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 76k | Apache-2.0 | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

Soporta LoRA, QLoRA, ajuste completo, DPO y más desde una UI o CLI. Muy usado en investigación e industria.

## Por qué destaca

La herramienta más completa para afinar modelos con interfaz.

## Cómo funciona

Unifica recetas de entrenamiento sobre Transformers y PEFT con una UI Gradio (LlamaBoard).

## Instalación rápida

`git clone https://github.com/hiyouga/LlamaFactory && pip install -e ".[torch,metrics]"` y `llamafactory-cli webui`.

## Casos de uso

- Afinar con DPO o RLHF
- Entrenar modelos de visión-lenguaje
- Experimentar sin código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres muchas técnicas de fine-tuning con UI | buscas la opción más eficiente en memoria; mira `unsloth` |

**Limitaciones:** Requiere GPU.

## Stack y modelos

- **Stack:** Python, PyTorch, Gradio
- **Modelos / API:** Modelos abiertos.
- **Etiquetas:** `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PEFT](peft.md) | 21.9k | Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA. |
| [Transformers](transformers.md) | 169k | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Unsloth](unsloth.md) | 79.3k | Fine-tuning y ejecución local de LLM hasta 2 veces más rápido y con mucha menos memoria, ahora con UI. |

## Enlaces

- 🐙 GitHub: [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)
- 🌐 Web: <https://llamafactory.readthedocs.io>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
