[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Serving y gateways de LLM

# 🚀 vLLM

> Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 96.7k | Apache-2.0 | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Sirve modelos abiertos a muchos usuarios con una API compatible con OpenAI, gracias a PagedAttention y batching continuo.

## Por qué destaca

Estándar en producción para servir LLM abiertos en GPU.

## Cómo funciona

Gestiona la caché KV por páginas, agrupa peticiones dinámicamente y soporta paralelismo entre GPUs.

## Instalación rápida

`pip install vllm` y `vllm serve Qwen/Qwen3-8B` (requiere GPU NVIDIA o AMD).

## Casos de uso

- API privada de LLM para la empresa
- Servir modelos afinados
- Inferencia por lotes barata

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas servir LLM abiertos a muchos usuarios en GPU | solo los usas tú en un portátil; mira `ollama` |

**Limitaciones:** Requiere GPU con bastante memoria.

## Stack y modelos

- **Stack:** Python, CUDA, PyTorch
- **Modelos / API:** Modelos abiertos de Hugging Face.
- **Etiquetas:** `inference` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [Open WebUI](open-webui.md) | 158k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SGLang](sglang.md) | 38.7k | Framework de servicio de alto rendimiento para LLM y modelos multimodales. |

## Enlaces

- 🐙 GitHub: [vllm-project/vllm](https://github.com/vllm-project/vllm)
- 🌐 Web: <https://vllm.ai>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
