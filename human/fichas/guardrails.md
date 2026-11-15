[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Observabilidad, evaluación y guardrails

# 📡 NeMo Guardrails

> Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales con LLM.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 7.5k | Otra (ver repo) | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Controla de qué puede hablar tu bot, bloquea jailbreaks y valida entradas y salidas con reglas en el lenguaje Colang.

## Por qué destaca

Respaldado por NVIDIA y muy flexible para políticas de conversación.

## Cómo funciona

Intercepta la conversación y aplica flujos de Colang y verificaciones (moderación, hechos) antes y después del LLM.

## Instalación rápida

`pip install nemoguardrails`.

## Casos de uso

- Limitar temas de un chatbot
- Bloquear inyecciones de prompt
- Verificar respuestas contra hechos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas políticas de seguridad en un chatbot | solo quieres probar vulnerabilidades; mira `promptfoo` |

## Stack y modelos

- **Stack:** Python, Colang
- **Modelos / API:** Agnóstico.
- **Etiquetas:** `security` `chatbot` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 149k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |

## Enlaces

- 🐙 GitHub: [NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)
- 🌐 Web: <https://docs.nvidia.com/nemo/guardrails/latest/index.html>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
