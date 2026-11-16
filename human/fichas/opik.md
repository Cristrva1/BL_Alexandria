[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📡 Opik

> Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.4k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 75/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Opik, plataforma open source de Comet para observabilidad, evaluación y trazado de agentes de IA. Licencia Apache-2.0 en toda la plataforma (servidor incluido). Es muy activa (~23k estrellas, 2.2.143).

## ¿Qué hace?

Traza llamadas a LLM, conversaciones y agentes con árboles de pasos y herramientas. Evalúa con datasets, experimentos y métricas de LLM como juez (alucinación, moderación, RAG). Incluye optimizador de prompts y agentes, monitorización en producción y guardrails.

## ¿Cómo lo hace?

Se usa en Comet Cloud o se autoaloja (Docker Compose o Kubernetes); el cliente se instala con `pip install opik`. Tiene servidor MCP (`uvx opik mcp configure`) e integraciones con decenas de frameworks.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph](langgraph.md) | Integración nativa para trazar grafos de LangGraph. | Envuelve el grafo con el tracer de Opik. |
| [litellm](litellm.md) | Integración nativa con LiteLLM. | Activa el callback de Opik en LiteLLM. |
| [Ragas](ragas.md) | Integración documentada para registrar métricas de Ragas. | Calcula métricas con Ragas y regístralas en Opik. |
| [DSPy](dspy.md) | Integración documentada con DSPy. | Activa el callback de Opik en DSPy. |

**Notas:** Alternativas (elige una): langfuse, phoenix.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 2.2.143 (2026-11-06) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/comet-ml/opik/blob/main/README.md) · [2](https://www.comet.com/docs/opik/integrations/langgraph) · [3](https://www.comet.com/docs/opik/integrations/litellm) · [4](https://www.comet.com/docs/opik/integrations/ragas) · [5](https://www.comet.com/docs/opik/integrations/dspy)</sub>

## Ver similares

Grupo **Observabilidad y trazas de LLM**: Opik ocupa la posición 2 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [langfuse](langfuse.md) ⭐ recomendado | 79 | Si quieres trazas, prompts y evaluaciones de LLM auto-hospedables con la comunidad más grande. |
| 2 | **Opik** (esta ficha) | 75 | Si quieres trazas y evaluación de LLM con integración en pruebas. |
| 3 | [MLflow](mlflow.md) | 70 | Si ya gestionas experimentos y modelos de ML clásico y quieres sumar trazas de LLM. |
| 4 | [Phoenix](phoenix.md) | 53 | Si quieres observabilidad basada en OpenTelemetry y evaluación local en notebooks. |
| 5 | [Helicone](helicone.md) | 50 | Si quieres observabilidad como proxy con solo cambiar la URL base. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Plataforma Apache autoalojable o Cloud; los modelos evaluadores y la infraestructura tienen costes propios |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Documenta configuración MCP para Claude Code, Codex y otros clientes; puede registrar Ollama, pero no sirve el modelo por sí mismo |
| Coste | El coste depende del proveedor o la ruta. Plataforma Apache autoalojable o Cloud; los modelos evaluadores y la infraestructura tienen costes propios |
| Equipo | Preparación según la ruta elegida. Python; Cloud o instancia propia; app y datos de prueba; uv para MCP |

Documenta configuración MCP para Claude Code, Codex y otros clientes; puede registrar Ollama, pero no sirve el modelo por sí mismo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- Cloud o instancia propia
- app y datos de prueba
- uv para MCP

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install opik
opik configure
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/comet-ml/opik/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Opik para mi objetivo y necesito pasos guiados. Lee https://github.com/comet-ml/opik/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Registra una traza y consúltala desde el panel o MCP con acceso de prueba.

**Qué comprobar:** Puedes localizar entrada, salida y evaluación de esa ejecución.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Depurar una cadena RAG
- Revisar fallos con un agente de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Depurar una cadena RAG; Revisar fallos con un agente de código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta configuración MCP para Claude Code, Codex y otros clientes; puede registrar Ollama, pero no sirve el modelo por sí mismo

## Stack y modelos

- **Stack:** Python; Cloud o instancia propia; app y datos de prueba; uv para MCP
- **Etiquetas:** `observability` `evaluation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| [Phoenix](phoenix.md) | 12.3k | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. |

## Enlaces

- 🐙 GitHub: [comet-ml/opik](https://github.com/comet-ml/opik)
- 🌐 Web: <https://www.comet.com/docs/opik/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/comet-ml/opik/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
