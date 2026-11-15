[🏠 Inicio](../README.md) › [🧠 Mejorar tu agente: skills y prompts](../categorias/02-skills-prompts-gu-as-de-agente.md) › Guías, cursos y cookbooks

# 🎓 Agents Towards Production

> Colección de 28 tutoriales con código para llevar agentes de IA a producción: memoria, despliegue, seguridad, trazas y evaluación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 21.9k | NOASSERTION | Jupyter Notebook | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio · **MCP** 🔌 sí

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

Playbook de Nir Diamant (DiamantAI) con un tutorial por carpeta, en notebooks o scripts listos para ejecutar, sobre cada pieza del stack de un agente: tool calling seguro, datos web, RAG, memoria (Redis, Mem0, Cognee), Docker, FastAPI, GPU, MCP, A2A, LangGraph, seguridad, fine-tuning, trazas y evaluación. Muchos tutoriales los aportan empresas patrocinadoras.

## Por qué destaca

Cubre lo que suele faltar después de la demo (estado, memoria, despliegue, guardrails, evaluación) con código que puedes ejecutar y adaptar. Cada tutorial es independiente, así que vas directo a la pieza que necesitas.

## Cómo funciona

Cada carpeta de `tutorials/` trae su README, su `requirements.txt` y un notebook o una app; la mayoría usa Python con LangChain o LangGraph y la API del proveedor o servicio que explica.

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

1. Abre el material original y elige un capítulo o ejemplo.
2. Revisa los requisitos de ese ejemplo antes de instalar dependencias.
3. Usa las alternativas y recetas para situarlo dentro de tu proyecto.

[Instrucciones originales de instalación](https://github.com/NirDiamant/agents-towards-production/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Agents Towards Production para mi objetivo y necesito pasos guiados. Lee https://github.com/NirDiamant/agents-towards-production/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `agents` `learning` `notebooks` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangGraph](langgraph.md) | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [mem0](mem0.md) | 69k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Enlaces

- 🐙 GitHub: [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production)
- 🌐 Web: <https://diamant-ai.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/NirDiamant/agents-towards-production/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
