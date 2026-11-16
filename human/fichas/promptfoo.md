[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📡 promptfoo

> CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.2k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 79/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Promptfoo, CLI y librería para evaluar y hacer red teaming de aplicaciones con LLM. Ahora forma parte de OpenAI y sigue siendo open source con licencia MIT. Es muy activo (~27k estrellas, 0.125.1).

## ¿Qué hace?

Ejecuta evaluaciones automáticas de prompts, modelos, agentes y RAG con aserciones, y compara proveedores lado a lado. Hace red teaming y escaneo de vulnerabilidades con informes de seguridad. Revisa pull requests en busca de problemas de seguridad relacionados con LLM y se integra en CI/CD.

## ¿Cómo lo hace?

Se instala con `npm install -g promptfoo`, `brew`, `pip` o se usa con `npx promptfoo@latest`; se configura con YAML y se ejecuta con `promptfoo eval` y `promptfoo view`. Las evaluaciones corren en local, aunque requieren las claves de los proveedores que se prueben.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [langfuse](langfuse.md) | Integración documentada para usar prompts y trazas de Langfuse. | Configura las credenciales de Langfuse en promptfoo. |
| [litellm](litellm.md) | Proveedor nativo de LiteLLM en promptfoo. | Apunta promptfoo al proxy LiteLLM. |
| [vLLM](vllm.md) | Proveedor nativo para evaluar modelos servidos con vLLM. | Lanza vLLM y configúralo como proveedor. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (13). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Anthropic's Prompt Engineering Tutorial](prompt-eng-tutorial.md) · [ChatGPT_DAN](chatgpt-dan.md) · [chatgpt_system_prompt](chatgpt-system-prompt.md) · [Claude Cookbooks](claude-cookbooks.md) · [Cybersecurity Skills (comunidad)](cybersecurity-skills.md) · [garak](garak.md) · [jev-fraud](jev-fraud.md) · [llm-council](llm-council.md) · [NeMo Guardrails](guardrails.md) · [OpenAI Cookbook](openai-cookbook.md) · [Prompt Engineering Guide](prompt-engineering-guide.md) · [prompts.chat](prompts-chat.md) · [system-prompts-and-models-of-ai-tools](system-prompts-and-models-of-ai-tools.md)

**Notas:** Alternativas (elige una): deepeval, ragas, dspy. Tras la compra por OpenAI conviene vigilar la gobernanza del proyecto.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 0.125.1 (2026-10-25) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/promptfoo/promptfoo/blob/main/README.md) · [2](https://www.promptfoo.dev/docs/integrations/langfuse/) · [3](https://www.promptfoo.dev/docs/providers/litellm/) · [4](https://www.promptfoo.dev/docs/providers/vllm/)</sub>

## Ver similares

Grupo **Evaluación y pruebas de LLM**: promptfoo ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **promptfoo** (esta ficha) ⭐ recomendado | 79 | Si buscas esto: cLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. |
| 2 | [DeepEval](deepeval.md) | 63 | Si buscas esto: framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. |
| 3 | [Ragas](ragas.md) | 51 | Si buscas esto: librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. CLI MIT; APIs y servicios adicionales tienen costes y Ollama permite modelos locales |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Una puntuación depende del dataset, proveedor y evaluador; los tests de seguridad deben dirigirse a sistemas propios o autorizados |
| Coste | El coste depende del proveedor o la ruta. CLI MIT; APIs y servicios adicionales tienen costes y Ollama permite modelos locales |
| Equipo | Preparación según la ruta elegida. Node; dataset de preguntas; proveedor o Ollama; criterio de evaluación |

Una puntuación depende del dataset, proveedor y evaluador; los tests de seguridad deben dirigirse a sistemas propios o autorizados

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- dataset de preguntas
- proveedor o Ollama
- criterio de evaluación

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
npm install -g promptfoo
promptfoo init --example getting-started
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/promptfoo/promptfoo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar promptfoo para mi objetivo y necesito pasos guiados. Lee https://github.com/promptfoo/promptfoo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea dos variantes de un prompt y evalúalas con tres casos conocidos.

**Qué comprobar:** Puedes comparar respuestas y detectar un fallo concreto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Evaluar un prompt de soporte
- Probar regresiones de un RAG

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Evaluar un prompt de soporte; Probar regresiones de un RAG | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Una puntuación depende del dataset, proveedor y evaluador; los tests de seguridad deben dirigirse a sistemas propios o autorizados

## Stack y modelos

- **Stack:** Node; dataset de preguntas; proveedor o Ollama; criterio de evaluación
- **Etiquetas:** `evaluation` `security` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DeepEval](deepeval.md) | 19.5k | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. |
| [Ragas](ragas.md) | 16.3k | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. |
| [DSPy](dspy.md) | 39.1k | Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano. |

## Enlaces

- 🐙 GitHub: [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)
- 🌐 Web: <https://promptfoo.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/promptfoo/promptfoo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
