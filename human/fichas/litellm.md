[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Serving y gateways de LLM

# 🔀 litellm

> Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 63k | Otra (ver repo) | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Resuelve el lock-in: cambias de proveedor o añades fallback sin reescribir el código de tu app.

## Por qué destaca

Es un estándar de facto para abstraer proveedores, muy adoptado por su routing, control de costos, reintentos y fallback entre modelos. Su amplia cobertura (OpenAI, Anthropic, Google, Bedrock, locales vía Ollama/vLLM) lo hace casi ubicuo en stacks multi-modelo.

## Cómo funciona

Traduce cada petición al formato del proveedor destino y puede correr como proxy/gateway (modo servidor) con balanceo, reintentos, budget tracking y registro de uso, además de como librería embebida.

## Instalación rápida

`pip install litellm` (o despliegue del proxy vía Docker); requiere las claves de los proveedores que uses vía variables de entorno.

## Casos de uso

- Probar varios modelos sin reescribir código
- Balancear costo/fallback entre proveedores
- Centralizar control de costos y rate limits

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas con múltiples modelos o quieres fallback/control de costos | usas un único proveedor fijo y no necesitas abstracción |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** OpenAI, Anthropic, Google, Bedrock, Azure, locales (Ollama, vLLM), etc.
- **Etiquetas:** `inference` `llmops` `python` `docker`
- **Modo de instalación sugerido:** 📦 **Dependencia del proyecto** — instálalo dentro de cada proyecto que lo use

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 149k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| [llm-council](llm-council.md) | 26.4k | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. |

## Enlaces

- 🐙 GitHub: [BerriAI/litellm](https://github.com/BerriAI/litellm)
- 🌐 Web: <https://docs.litellm.ai/docs/>
- 🧪 Receta: [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md)
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)
- 🧪 Receta: [Agente de voz en tiempo real](../playbooks/agente-de-voz.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
