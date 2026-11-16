[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📡 Phoenix

> Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.3k | Elastic-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** Elastic-2.0. Source-available (ELv2). Fuente: [LICENSE](https://github.com/Arize-ai/phoenix/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Arize Phoenix, plataforma de observabilidad de IA para experimentación, evaluación y depuración, de Arize. Licencia Elastic License 2.0 (código disponible, no OSI; GitHub muestra NOASSERTION). Es muy activa (~12k estrellas, arize-phoenix-v21.1.0).

## ¿Qué hace?

Traza aplicaciones LLM con instrumentación basada en OpenTelemetry (OpenInference). Evalúa con LLM, gestiona datasets, experimentos y versiones de prompts, y ofrece un playground. Tiene un servidor MCP remoto para consultar trazas desde Claude Code, Cursor y otros clientes.

## ¿Cómo lo hace?

Se instala con `pip install arize-phoenix` o `npx @arizeai/phoenix-cli setup`, y también se despliega con Docker Compose o Kubernetes/Helm. Es autoalojado; Arize AX es la versión gestionada de pago.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LlamaIndex](llama-index.md) | Integración documentada para trazar LlamaIndex. | Instala la instrumentación de OpenInference para LlamaIndex. |
| [LangGraph](langgraph.md) | Integración documentada para LangGraph. | Instrumenta LangGraph y envía trazas a Phoenix. |
| [Ollama](ollama.md) | Integración documentada con Ollama. | Traza llamadas a modelos locales de Ollama. |
| [Claude Code](claude-code.md) | Servidor MCP remoto para consultar trazas desde el agente. | Conecta Claude Code al endpoint MCP de Phoenix. |

**Notas:** Alternativas (elige una): langfuse, opik. La licencia ELv2 prohíbe ofrecerlo como servicio gestionado a terceros.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada arize-phoenix-v21.1.0 (2026-11-13) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Arize-ai/phoenix/blob/main/README.md) · [2](https://arize.com/docs/phoenix/integrations/python/llamaindex) · [3](https://arize.com/docs/phoenix/integrations/python/langgraph) · [4](https://arize.com/docs/phoenix/integrations/llm-providers/ollama) · [5](https://arize.com/docs/phoenix/integrations/mcp)</sub>

## Ver similares

Grupo **Observabilidad y trazas de LLM**: Phoenix ocupa la posición 4 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [langfuse](langfuse.md) ⭐ recomendado | 79 | Si quieres trazas, prompts y evaluaciones de LLM auto-hospedables con la comunidad más grande. |
| 2 | [Opik](opik.md) | 75 | Si quieres trazas y evaluación de LLM con integración en pruebas. |
| 3 | [MLflow](mlflow.md) | 70 | Si ya gestionas experimentos y modelos de ML clásico y quieres sumar trazas de LLM. |
| 4 | **Phoenix** (esta ficha) | 53 | Si quieres observabilidad basada en OpenTelemetry y evaluación local en notebooks. |
| 5 | [Helicone](helicone.md) | 50 | Si quieres observabilidad como proxy con solo cambiar la URL base. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Autoalojamiento, cómputo y evaluadores se costean aparte; puede observar modelos locales Ollama |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. El README declara Elastic License 2.0, por lo que no debe etiquetarse como licencia abierta sin restricciones; ofrece MCP y plugins Claude Code y Codex |
| Coste | El coste depende del proveedor o la ruta. Autoalojamiento, cómputo y evaluadores se costean aparte; puede observar modelos locales Ollama |
| Equipo | Preparación según la ruta elegida. Python; app de prueba; instrumentación o cliente MCP |

El README declara Elastic License 2.0, por lo que no debe etiquetarse como licencia abierta sin restricciones; ofrece MCP y plugins Claude Code y Codex

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- app de prueba
- instrumentación o cliente MCP

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
pip install arize-phoenix
phoenix serve
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Arize-ai/phoenix/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Phoenix para mi objetivo y necesito pasos guiados. Lee https://github.com/Arize-ai/phoenix/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una traza de muestra y consulta una ejecución antes de conectar una aplicación real.

**Qué comprobar:** Puedes identificar spans, latencia y entradas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Depurar una app con OpenTelemetry
- Consultar trazas desde un agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Depurar una app con OpenTelemetry; Consultar trazas desde un agente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README declara Elastic License 2.0, por lo que no debe etiquetarse como licencia abierta sin restricciones; ofrece MCP y plugins Claude Code y Codex

## Stack y modelos

- **Stack:** Python; app de prueba; instrumentación o cliente MCP
- **Etiquetas:** `observability` `evaluation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| [Opik](opik.md) | 23.4k | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. |

## Enlaces

- 🐙 GitHub: [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)
- 🌐 Web: <https://arize.com/docs/phoenix>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Arize-ai/phoenix/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
