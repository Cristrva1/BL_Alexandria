[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Simulación, evolución y debate entre modelos

# 🏛️ llm-council

> "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 26.4k | — | Python | 2025-11-22 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Cada modelo aporta una respuesta y luego se contrastan para llegar a un consenso.

## Por qué destaca

Combina perspectivas de varios modelos para reducir el sesgo de uno solo; propuesta sencilla y didáctica popularizada por Karpathy. Sirve tanto para obtener mejores respuestas como para comparar modelos.

## Cómo funciona

Envía la consulta a varios LLMs, los hace revisar las respuestas de los demás y agrega un resultado de consenso; app ligera en Python/web con backend FastAPI.

## Instalación rápida

`git clone` del repo y ejecución según su README. Requiere claves de varios proveedores de LLM (OpenAI, Anthropic, Google, xAI) para que el consejo tenga variedad.

## Casos de uso

- Respuestas por consenso multi-modelo
- Reducir sesgo de un solo modelo
- Comparar modelos en preguntas reales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres consenso entre modelos o comparar proveedores | te basta un único LLM o el coste multi-modelo no es asumible |

**Limitaciones:** Cada consulta se multiplica por el nº de modelos del consejo, elevando coste y latencia.

## Stack y modelos

- **Stack:** Python, React, FastAPI, PostgreSQL
- **Modelos / API:** Múltiples LLMs (OpenAI, Anthropic, Google, xAI Grok).
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Enlaces

- 🐙 GitHub: [karpathy/llm-council](https://github.com/karpathy/llm-council)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
