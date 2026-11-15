[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Guías, cursos y cookbooks

# 🎓 Claude Cookbooks

> Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 54.5k | MIT | Jupyter Notebook | 2026-11-04 | 🆕 Aún no (sugerido) |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## Qué es

Notebooks y guías de Anthropic con código copiable para construir con Claude: clasificación, resumen, RAG (con Pinecone o embeddings de Voyage AI), tool use y un agente de atención al cliente, visión y extracción de formularios, subagentes, PDFs, salida JSON consistente, moderación, prompt caching y checklists de coste y latencia.

## Por qué destaca

Es la referencia oficial y sigue la evolución de la API, así que los patrones reflejan cómo recomienda Anthropic usar Claude. Cada receta es corta y se adapta fácil a otro lenguaje.

## Cómo funciona

Son notebooks de Jupyter agrupados por tema (capacidades, herramientas, integraciones, multimodal, técnicas avanzadas) que llaman a la API con el SDK `anthropic` de Python; el `pyproject.toml` incluye también el Claude Agent SDK.

## Instalación rápida

`git clone https://github.com/anthropics/claude-cookbooks && cd claude-cookbooks && uv sync` y abre los notebooks en Jupyter con tu `ANTHROPIC_API_KEY`.

## Casos de uso

- Aprender tool use con un agente de atención al cliente
- Aplicar prompt caching para bajar el coste de una app
- Montar un RAG con Claude y una base vectorial

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| construyes sobre la API de Claude y quieres ejemplos oficiales que puedas copiar | tu app usa la API de OpenAI; mira `openai-cookbook` |

**Limitaciones:** Casi todo el código es Python y necesitas una API key de Anthropic de pago para ejecutarlo.

## Stack y modelos

- **Stack:** Python, Jupyter, Anthropic SDK, Claude Agent SDK
- **Modelos / API:** API de Claude (Anthropic); algunas recetas usan servicios externos como Voyage AI o Pinecone.
- **Etiquetas:** `learning` `notebooks` `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Anthropic's Prompt Engineering Tutorial](prompt-eng-tutorial.md) | 39.2k | Tutorial interactivo oficial de Anthropic para aprender ingeniería de prompts con ejercicios. |
| [Anthropic Skills](anthropic-skills.md) | 192k | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. |
| [promptfoo](promptfoo.md) | 27k | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenAI Cookbook](openai-cookbook.md) | 77k | Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales. |
| [Awesome LLM Apps](awesome-llm-apps.md) | 144k | Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM. |

## Enlaces

- 🐙 GitHub: [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
