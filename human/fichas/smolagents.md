[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 smolagents

> Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.4k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 55/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca minimalista de agentes de Hugging Face (Apache 2.0): la lógica principal cabe en unas 1.000 líneas. Activa (v1.26.0).

## ¿Qué hace?

Su `CodeAgent` escribe sus acciones como código Python en lugar de JSON. También hay agentes de tool calling. Permite compartir y descargar herramientas y agentes del Hub, admite texto, visión, vídeo y audio, y usa herramientas de cualquier servidor MCP o de LangChain.

## ¿Cómo lo hace?

Se instala con `pip install "smolagents[toolkit]"`. Es agnóstico de modelo: `transformers` u Ollama en local, proveedores del Hub, LiteLLM para más de 100 LLM, OpenAI o Anthropic. Como ejecuta código, recomienda sandboxes (E2B, Blaxel, Modal o Docker): su `LocalPythonExecutor` no es una frontera de seguridad.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [E2B](e2b.md) | Sandbox gestionado documentado para ejecutar el código del agente. | Cuenta de E2B y extra correspondiente antes de ejecutar CodeAgent. |
| [Transformers](transformers.md) | Modelos locales de Hugging Face. | Requiere GPU para modelos medianos. |
| [litellm](litellm.md) | Acceso a más de 100 LLM con `LiteLLMModel`. | Configura las claves del proveedor. |
| [langfuse](langfuse.md) | Trazas con la integración oficial de Langfuse. | Instrumenta antes de producción. |
| [Hugging Face Agents Course](agents-course.md) | Combinación recíproca: Hugging Face Agents Course lo enlaza como «La unidad 2.1 enseña a construir agentes con smolagents». | Orden indicado desde Hugging Face Agents Course: Sigue la unidad; instala smolagents en el entorno del cuaderno. |

**Notas:** Alternativas (elige una): pydantic-ai, openai-agents-python. No ejecutes CodeAgent sin sandbox con datos o credenciales reales.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.26.0 (2026-05-29) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/huggingface/smolagents/blob/main/README.md) · [2](https://huggingface.co/docs/smolagents/tutorials/secure_code_execution) · [3](https://langfuse.com/integrations/frameworks/smolagents)</sub>

## Ver similares

Grupo **Frameworks de agentes en Python**: smolagents ocupa la posición 8 de 8 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [LangGraph](langgraph.md) ⭐ recomendado | 72 | Si necesitas flujos con estado, ciclos, checkpoints y control fino del grafo en producción. |
| 2 | [crewAI](crewai.md) | 72 | Si piensas en equipos de agentes con roles y tareas y quieres arrancar rápido. |
| 3 | [Deep Agents](deepagents.md) | 70 | Si quieres agentes de largo recorrido con planificación, subagentes y sistema de archivos sobre LangGraph. |
| 4 | [OpenAI Agents SDK](openai-agents-python.md) | 67 | Si usas la API de OpenAI y quieres handoffs, guardrails y trazas oficiales. |
| 5 | [Pydantic AI](pydantic-ai.md) | 66 | Si quieres salidas tipadas y validadas con Pydantic y un estilo cercano a FastAPI. |
| 6 | [Agent Development Kit (ADK)](adk-python.md) | 65 | Si despliegas en Google Cloud/Vertex o usas Gemini y quieres el kit oficial de Google. |
| 7 | [Agno](agno.md) | 61 | Si quieres un runtime de agentes con memoria, conocimiento y equipos listo para servir por API. |
| 8 | **smolagents** (esta ficha) | 55 | Si quieres agentes mínimos que escriben código Python como acciones, de Hugging Face. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Admite Transformers u Ollama locales y APIs; aislamiento y búsqueda externa pueden costar aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El agente ejecuta código: usa el aislamiento documentado y archivos de prueba |
| Coste | El coste depende del proveedor o la ruta. Admite Transformers u Ollama locales y APIs; aislamiento y búsqueda externa pueden costar aparte |
| Equipo | Preparación según la ruta elegida. Python; modelo; ejecutor aislado |

El agente ejecuta código: usa el aislamiento documentado y archivos de prueba

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- modelo
- ejecutor aislado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install "smolagents[toolkit]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/huggingface/smolagents/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar smolagents para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/smolagents/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Calcula el total y promedio de cinco importes ficticios y revisa el código generado.

**Qué comprobar:** Los resultados coinciden con los números de entrada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Calcular indicadores de un CSV
- Transformar datos consultados en un resumen

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Calcular indicadores de un CSV; Transformar datos consultados en un resumen | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El agente ejecuta código: usa el aislamiento documentado y archivos de prueba

## Stack y modelos

- **Stack:** Python; modelo; ejecutor aislado
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pydantic AI](pydantic-ai.md) | 21.2k | Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. |
| [OpenAI Agents SDK](openai-agents-python.md) | 30.7k | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. |

## Enlaces

- 🐙 GitHub: [huggingface/smolagents](https://github.com/huggingface/smolagents)
- 🌐 Web: <https://huggingface.co/docs/smolagents>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/huggingface/smolagents/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
