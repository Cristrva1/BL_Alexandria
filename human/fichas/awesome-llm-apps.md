[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Guías, cursos y cookbooks

# 🎓 Awesome LLM Apps

> Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 144k | Apache-2.0 | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio

## Qué es

Repositorio de Shubham Saboo con plantillas de código abierto ordenadas por tipo: agentes simples de un solo archivo, agentes avanzados con herramientas y memoria, equipos multiagente, agentes de voz, agentes con MCP, RAG, chat con documentos y webs, fine-tuning y cursos rápidos de Google ADK y OpenAI Agents SDK. Según la app usa OpenAI, Anthropic, Google, xAI, DeepSeek o modelos abiertos.

## Por qué destaca

Cada ejemplo es un proyecto pequeño y completo que puedes ejecutar en minutos y adaptar a tu caso. Es Apache 2.0 y se añaden plantillas nuevas con frecuencia.

## Cómo funciona

Cada app vive en su carpeta con `requirements.txt` y un script principal, casi siempre en Python con Streamlit, y se ejecuta con tu API key. Las skills de `agent_skills/` se instalan en tu agente de código con el Skills CLI.

## Instalación rápida

`git clone https://github.com/Shubhamsaboo/awesome-llm-apps`, entra en la carpeta de la app, `pip install -r requirements.txt` y ejecuta su script (p. ej. `streamlit run travel_agent.py`) con la API key del modelo que use.

## Casos de uso

- Partir de una plantilla de agente de research o de RAG
- Comparar frameworks de agentes con apps parecidas
- Probar un agente conectado a GitHub o Notion por MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres una plantilla de app con LLM que funcione desde el primer día para adaptarla a tu proyecto | buscas un curso estructurado con lecciones en orden; mira `ai-agents-for-beginners` o `generative-ai-for-beginners` |

**Limitaciones:** Son demos: la calidad y el mantenimiento varían entre apps y casi ninguna está preparada para producción tal cual.

## Stack y modelos

- **Stack:** Python, Streamlit, OpenAI Agents SDK, Google ADK, Agno
- **Modelos / API:** Varía por app: OpenAI, Anthropic, Google Gemini, xAI, DeepSeek y modelos abiertos como Llama o Qwen.
- **Etiquetas:** `agents` `rag` `learning` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [streamlit](streamlit.md) | 46.3k | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. |
| [OpenAI Agents SDK](openai-agents-python.md) | 30.6k | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. |
| [Agent Development Kit (ADK)](adk-python.md) | 22.2k | Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. |
| [firecrawl](firecrawl.md) | 200k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenAI Cookbook](openai-cookbook.md) | 77k | Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales. |
| [Claude Cookbooks](claude-cookbooks.md) | 54.5k | Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización. |

## Enlaces

- 🐙 GitHub: [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 🌐 Web: <https://www.theunwindai.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
