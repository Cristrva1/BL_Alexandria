[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🟩 NeMo-Agent-Toolkit

> Toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo).

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 2.7k | Apache-2.0 | Python | 2026-11-09 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

## Qué es

Aporta componentes para conectar, evaluar y desplegar agentes en infraestructura empresarial.

## Por qué destaca

Respaldo y rendimiento de NVIDIA, orientado a despliegues empresariales sobre su stack de modelos NIM e infra GPU. Incluye evaluación y guardrails, no solo orquestación.

## Cómo funciona

Compone agentes y herramientas mediante perfiles configurables y los conecta a modelos NVIDIA NIM u otros compatibles (OpenAI-style); librería Python (Apache-2.0) con servidor FastAPI.

## Instalación rápida

`pip install nvidia-nat` (o `git clone` del repo). Para sacar provecho real necesitas acceso a NIM/NGC o GPUs NVIDIA; de ahí el setup 🔴.

## Casos de uso

- Agentes empresariales en stack NVIDIA
- Pipelines con modelos propios tras un firewall
- RAG con guardrails y evaluación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas con infra NVIDIA o necesitas guardrails/eval empresarial | quieres algo ligero y agnóstico |

## Stack y modelos

- **Stack:** Python, FastAPI (Apache-2.0)
- **Modelos / API:** NVIDIA NIM y compatibles OpenAI.
- **Etiquetas:** `automation` `agents` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 149k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |

## Enlaces

- 🐙 GitHub: [NVIDIA/NeMo-Agent-Toolkit](https://github.com/NVIDIA/NeMo-Agent-Toolkit)
- 🌐 Web: <https://docs.nvidia.com/nemo/agent-toolkit/latest/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
