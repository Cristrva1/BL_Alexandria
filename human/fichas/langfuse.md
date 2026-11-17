[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📡 langfuse

> Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 37.4k | MIT + licencia Enterprise (ee/) | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media; varios servicios con Docker Compose

**Puntuación de calidad** 79/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** MIT + licencia Enterprise (ee/). Fuente: [LICENSE](https://github.com/langfuse/langfuse/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Langfuse, plataforma open source de ingeniería de IA para observabilidad y evaluación de agentes; forma parte de ClickHouse desde enero de 2026. Es MIT salvo las carpetas `ee` (GitHub muestra NOASSERTION). Es muy activa (~37k estrellas, v4.80.0).

## ¿Qué hace?

Registra trazas de llamadas a LLM, recuperación, embeddings y herramientas, con uso y costes. Gestiona y versiona prompts, y en beta también skills (`SKILL.md`). Permite evaluaciones con LLM como juez, anotación manual, datasets y experimentos, además de un playground.

## ¿Cómo lo hace?

Se usa en Langfuse Cloud o se autoaloja con Docker Compose, Kubernetes o Terraform. Recibe trazas por SDK de Python y JS/TS o por OpenTelemetry, con integraciones para muchos frameworks. El despliegue propio requiere Postgres, ClickHouse, Redis y almacenamiento S3.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | Integración nativa: LiteLLM envía trazas a Langfuse. | Activa el callback de Langfuse en LiteLLM. |
| [langchain](langchain.md) | Integración nativa con LangChain y LangGraph mediante callback. | Pasa el callback handler de Langfuse a tus cadenas. |
| [Open WebUI](open-webui.md) | Integración documentada con Open WebUI. | Configura el pipeline de Langfuse en Open WebUI. |
| [Ragas](ragas.md) | Guía oficial para evaluar RAG con Ragas y registrar puntuaciones. | Calcula métricas con Ragas y súbelas como scores. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (31). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[ag2](ag2.md) · [Agent Development Kit (ADK)](adk-python.md) · [agentic-rag-for-dummies](agentic-rag-for-dummies.md) · [AgentScope](agentscope.md) · [AI SDK (Vercel)](vercel-ai.md) · [claude-agent-sdk-python](claude-agent-sdk-python.md) · [ClickHouse](clickhouse.md) · [crewAI](crewai.md) · [Deep Agents](deepagents.md) · [DeepEval](deepeval.md) · [dexter](dexter.md) · [dify](dify.md) · [DSPy](dspy.md) · [Grafana](grafana.md) · [Haystack](haystack.md) · [Hugging Face Agents Course](agents-course.md) · [langflow](langflow.md) · [LangGraph.js](langgraphjs.md) · [LangGraph](langgraph.md) · [LibreChat](librechat.md) · [LightRAG](lightrag.md) · [loguru](loguru.md) · [Mastra](mastra.md) · [Microsoft Agent Framework](agent-framework.md) · [OpenAI Agents SDK](openai-agents-python.md) · [promptfoo](promptfoo.md) · [Pydantic AI](pydantic-ai.md) · [QuantHarness](quantharness.md) · [RAGFlow](ragflow.md) · [smolagents](smolagents.md) · [Trigger.dev](trigger-dev.md)

**Notas:** Alternativas (elige una): phoenix, opik, mlflow. Las funciones `ee` tienen otra licencia.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v4.80.0 (2026-11-13) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/langfuse/langfuse/blob/main/README.md) · [2](https://langfuse.com/integrations/gateways/litellm) · [3](https://langfuse.com/integrations/frameworks/langchain) · [4](https://langfuse.com/integrations/no-code/openwebui) · [5](https://langfuse.com/integrations/frameworks/ragas)</sub>

## Ver similares

Grupo **Observabilidad y trazas de LLM**: langfuse ocupa la posición 1 de 5 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **langfuse** (esta ficha) ⭐ recomendado | 79 | Si quieres trazas, prompts y evaluaciones de LLM auto-hospedables con la comunidad más grande. |
| 2 | [Opik](opik.md) | 75 | Si quieres trazas y evaluación de LLM con integración en pruebas. |
| 3 | [MLflow](mlflow.md) | 70 | Si ya gestionas experimentos y modelos de ML clásico y quieres sumar trazas de LLM. |
| 4 | [Phoenix](phoenix.md) | 53 | Si quieres observabilidad basada en OpenTelemetry y evaluación local en notebooks. |
| 5 | [Helicone](helicone.md) | 50 | Si quieres observabilidad como proxy con solo cambiar la URL base. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Self-host requiere infraestructura; Cloud, LLM-as-judge y modelos tienen costes separados; integra trazas de Ollama |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. El MCP documentado en el README consulta documentación y no equivale a acceso automático a tus trazas; el núcleo MIT excluye carpetas ee |
| Coste | El coste depende del proveedor o la ruta. Self-host requiere infraestructura; Cloud, LLM-as-judge y modelos tienen costes separados; integra trazas de Ollama |
| Equipo | Preparación según la ruta elegida. Docker o servicio Cloud; app de prueba; SDK o instrumentación |

El MCP documentado en el README consulta documentación y no equivale a acceso automático a tus trazas; el núcleo MIT excluye carpetas ee

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o servicio Cloud
- app de prueba
- SDK o instrumentación

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Get a copy of the latest Langfuse repository
  git clone --depth=1 https://github.com/langfuse/langfuse.git
  cd langfuse

  # Run the langfuse docker compose
  docker compose up
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/langfuse/langfuse/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar langfuse para mi objetivo y necesito pasos guiados. Lee https://github.com/langfuse/langfuse/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Registra una llamada de prueba y abre su traza para revisar entrada, salida y duración.

**Qué comprobar:** Puedes rastrear una respuesta hasta la llamada que la produjo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Depurar un asistente
- Comparar versiones de un prompt

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Depurar un asistente; Comparar versiones de un prompt | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP documentado en el README consulta documentación y no equivale a acceso automático a tus trazas; el núcleo MIT excluye carpetas ee

## Stack y modelos

- **Stack:** Docker o servicio Cloud; app de prueba; SDK o instrumentación
- **Etiquetas:** `automation` `observability` `typescript` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Phoenix](phoenix.md) | 12.3k | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. |
| [Opik](opik.md) | 23.4k | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. |
| [MLflow](mlflow.md) | 28.8k | Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro. |
| [Helicone](helicone.md) | 6.3k | Pasarela de IA y plataforma de observabilidad de LLM abierta: registra peticiones, costes y latencias, gestiona prompts y enruta a más de 100 modelos. |

## Enlaces

- 🐙 GitHub: [langfuse/langfuse](https://github.com/langfuse/langfuse)
- 🌐 Web: <https://langfuse.com>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langfuse/langfuse/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
