[🏠 Inicio](../README.md) › [🧠 Mejorar tu agente: skills y prompts](../categorias/02-skills-prompts-gu-as-de-agente.md) › Guías, cursos y cookbooks

# 🎓 Claude Cookbooks

> Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 54.7k | MIT | Jupyter Notebook | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo. |
| Coste | Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Notebooks y guías de Anthropic con código copiable para construir con Claude: clasificación, resumen, RAG (con Pinecone o embeddings de Voyage AI), tool use y un agente de atención al cliente, visión y extracción de formularios, subagentes, PDFs, salida JSON consistente, moderación, prompt caching y checklists de coste y latencia.

## Por qué destaca

Es la referencia oficial y sigue la evolución de la API, así que los patrones reflejan cómo recomienda Anthropic usar Claude. Cada receta es corta y se adapta fácil a otro lenguaje.

## Cómo funciona

Son notebooks de Jupyter agrupados por tema (capacidades, herramientas, integraciones, multimodal, técnicas avanzadas) que llaman a la API con el SDK `anthropic` de Python; el `pyproject.toml` incluye también el Claude Agent SDK.

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

1. Abre el material original y elige un capítulo o ejemplo.
2. Revisa los requisitos de ese ejemplo antes de instalar dependencias.
3. Usa las alternativas y recetas para situarlo dentro de tu proyecto.

[Instrucciones originales de instalación](https://github.com/anthropics/claude-cookbooks/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Claude Cookbooks para mi objetivo y necesito pasos guiados. Lee https://github.com/anthropics/claude-cookbooks/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `learning` `notebooks` `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Anthropic's Prompt Engineering Tutorial](prompt-eng-tutorial.md) | 39.3k | Tutorial interactivo oficial de Anthropic para aprender ingeniería de prompts con ejercicios. |
| [Anthropic Skills](anthropic-skills.md) | 195k | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. |
| [promptfoo](promptfoo.md) | 27.2k | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenAI Cookbook](openai-cookbook.md) | 77.1k | Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales. |
| [Awesome LLM Apps](awesome-llm-apps.md) | 145k | Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM. |

## Enlaces

- 🐙 GitHub: [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/anthropics/claude-cookbooks/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
