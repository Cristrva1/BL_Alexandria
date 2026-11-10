[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Guías, cursos y cookbooks

# 🎓 Agents Towards Production

> Colección de 28 tutoriales con código para llevar agentes de IA a producción: memoria, despliegue, seguridad, trazas y evaluación.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 21.9k | Otra (ver repo) | Jupyter Notebook | 2026-11-02 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio · **MCP** 🔌 sí

## Qué es

Playbook de Nir Diamant (DiamantAI) con un tutorial por carpeta, en notebooks o scripts listos para ejecutar, sobre cada pieza del stack de un agente: tool calling seguro, datos web, RAG, memoria (Redis, Mem0, Cognee), Docker, FastAPI, GPU, MCP, A2A, LangGraph, seguridad, fine-tuning, trazas y evaluación. Muchos tutoriales los aportan empresas patrocinadoras.

## Por qué destaca

Cubre lo que suele faltar después de la demo (estado, memoria, despliegue, guardrails, evaluación) con código que puedes ejecutar y adaptar. Cada tutorial es independiente, así que vas directo a la pieza que necesitas.

## Cómo funciona

Cada carpeta de `tutorials/` trae su README, su `requirements.txt` y un notebook o una app; la mayoría usa Python con LangChain o LangGraph y la API del proveedor o servicio que explica.

## Instalación rápida

`git clone https://github.com/NirDiamant/agents-towards-production` y, dentro del tutorial elegido, `pip install -r requirements.txt` y `jupyter notebook`; cada uno indica las API keys que necesita.

## Casos de uso

- Añadir memoria persistente a un agente con Redis o Mem0
- Desplegar un agente como API con FastAPI y Docker
- Probar ataques de prompt injection y sus defensas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| ya tienes un prototipo de agente y necesitas resolver memoria, despliegue, seguridad u observabilidad | estás empezando con agentes desde cero; mira `ai-agents-for-beginners` |

**Limitaciones:** Licencia propia no comercial, y varios tutoriales dependen de servicios de patrocinadores (alguno ya retirado, como hushvert).

## Stack y modelos

- **Stack:** Python, Jupyter, LangGraph, FastAPI, Docker
- **Modelos / API:** Depende del tutorial: muchos usan la API de OpenAI y servicios de los patrocinadores; uno enseña a usar modelos locales con Ollama.
- **Etiquetas:** `agents` `learning` `notebooks` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangGraph](langgraph.md) | 44.7k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [mem0](mem0.md) | 68.7k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Enlaces

- 🐙 GitHub: [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production)
- 🌐 Web: <https://diamant-ai.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
