[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Simulación, evolución y debate entre modelos

# 🧬 openevolve

> Agente de codificación evolutivo que optimiza algoritmos por simulación genética.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 7.8k | Apache-2.0 | Python | 2026-11-08 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Genera, evalúa y muta candidatos de código a lo largo de múltiples generaciones.

## Por qué destaca

Supera la generación en un solo paso al explorar el espacio de soluciones, encontrando algoritmos inéditos (inspirado en AlphaEvolve de Google). Es el proyecto open-source que más cerca está de replicar ese enfoque.

## Cómo funciona

Un bucle evolutivo usa el LLM como operador de mutación y una función de evaluación como fitness; implementado en Python con numpy/PyTorch y componentes en Rust para velocidad.

## Instalación rápida

`pip install openevolve` (o `git clone` del repo). Requiere un proveedor de LLM de frontera (Claude/GPT-4o) y, según el problema, cómputo no trivial para evaluar muchas generaciones.

## Casos de uso

- Empaquetado geométrico
- Optimización de carteras
- Mejorar scripts en tiempo real

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| optimizas problemas algorítmicos donde cabe explorar muchas variantes | haces tareas de texto comunes o buscas respuesta inmediata |

**Limitaciones:** Consume muchos tokens de LLM y cómputo por generación; no es práctico para tareas triviales.

## Stack y modelos

- **Stack:** Python, PyTorch/numpy, Rust
- **Modelos / API:** Modelos de frontera creativos (Claude, GPT-4o); agnóstico vía variables de entorno.
- **Etiquetas:** `automation` `agents` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [llm-council](llm-council.md) | 26.4k | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. |

## Enlaces

- 🐙 GitHub: [algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
