[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Serving y gateways de LLM

# 🚀 SGLang

> Framework de servicio de alto rendimiento para LLM y modelos multimodales.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 38.7k | Apache-2.0 | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Compite con vLLM en velocidad, con caché de prefijos RadixAttention y buen soporte de salidas estructuradas. Muy usado para modelos grandes como DeepSeek.

## Por qué destaca

Muy rápido en cargas con prefijos compartidos y en modelos MoE grandes.

## Cómo funciona

Reutiliza la caché KV entre peticiones con un árbol radix y optimiza el scheduler para alto throughput.

## Instalación rápida

`pip install "sglang[all]"` y `python -m sglang.launch_server --model-path Qwen/Qwen3-8B`.

## Casos de uso

- Servir modelos MoE grandes
- Agentes con muchos prompts compartidos
- Salidas JSON restringidas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| buscas el máximo rendimiento en servicio de LLM | quieres la opción más documentada; mira `vllm` |

**Limitaciones:** Requiere GPU.

## Stack y modelos

- **Stack:** Python, CUDA
- **Modelos / API:** Modelos abiertos.
- **Etiquetas:** `inference` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [vLLM](vllm.md) | 96.7k | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. |

## Enlaces

- 🐙 GitHub: [sgl-project/sglang](https://github.com/sgl-project/sglang)
- 🌐 Web: <https://sglang.io>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
