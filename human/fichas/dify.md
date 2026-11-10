[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Builders visuales y plataformas de agentes

# 🧱 dify

> Plataforma integral para construir apps de IA con backend y UI listos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 161k | Otra (ver repo) | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Combina orquestación de prompts, RAG, agentes, workflows y observabilidad en un mismo producto autoalojable.

## Por qué destaca

Todo-en-uno muy popular para llevar apps de IA a producción sin ensamblar piezas sueltas. Cubre desde el chatbot con RAG hasta workflows visuales y agentes, con gestión de usuarios y API propia.

## Cómo funciona

Define apps (chatbot, agente, workflow) desde un panel web; el backend en Python orquesta modelos y herramientas sobre PostgreSQL/Redis, y se despliega con Docker Compose.

## Instalación rápida

`docker compose up` desde el repo (o cloud gestionado de Dify). Requiere Docker y al menos una clave de proveedor de LLM.

## Casos de uso

- Desplegar un chatbot/asistente con RAG
- Apps IA para clientes
- Workflows visuales con herramientas propias

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres una app IA completa autoalojada | solo necesitas una librería o un prototipo puntual |

## Stack y modelos

- **Stack:** Python/TS, React, PostgreSQL, Redis, Docker
- **Modelos / API:** OpenAI, Anthropic, Google, locales; agnóstico vía variables de entorno.
- **Etiquetas:** `automation` `agents` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langflow](langflow.md) | 157k | Constructor visual de flujos LLM/agentes construido sobre LangChain. |
| [Flowise](flowise.md) | 55.6k | Builder visual drag-and-drop para pipelines LLM. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Sim](sim.md) | 30.1k | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. |
| [RAGFlow](ragflow.md) | 94k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. |

## Enlaces

- 🐙 GitHub: [langgenius/dify](https://github.com/langgenius/dify)
- 🌐 Web: <https://dify.ai>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
