[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🎓 Claude Cookbooks

> Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 54.7k | MIT | Jupyter Notebook | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Recetario oficial de Anthropic (MIT) con notebooks y guías para construir con la API de Claude. Antes se llamaba anthropic-cookbook, nombre que aún aparece en muchos enlaces del README. Es activo (último push en noviembre de 2026).

## ¿Qué hace?

Ofrece recetas organizadas por capacidades (clasificación, RAG, resumen), uso de herramientas e integraciones, integraciones de terceros (bases vectoriales como Pinecone, embeddings de Voyage AI), multimodalidad (visión, PDF) y técnicas avanzadas (subagentes, evaluaciones automáticas, modo JSON). Recomienda empezar por el curso de fundamentos de la API de Anthropic.

## ¿Cómo lo hace?

Notebooks principalmente en Python que requieren una clave de API de Claude, con su coste correspondiente. Los conceptos son adaptables a cualquier lenguaje con cliente de la API. No se instala; se clona y se ejecuta cada notebook.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Anthropic's Prompt Engineering Tutorial](prompt-eng-tutorial.md) | Base de prompting recomendada antes de las recetas. (combinación por arquitectura) | Completa primero el tutorial de prompts. |
| [claude-agent-sdk-python](claude-agent-sdk-python.md) | Siguiente paso cuando las recetas de herramientas y subagentes se quedan cortas y necesitas el bucle de agente completo. (combinación por arquitectura) | Pasa al SDK cuando quieras agentes con herramientas de sistema. |
| [promptfoo](promptfoo.md) | Automatizar las evaluaciones que el cookbook enseña a construir. (combinación por arquitectura) | Convierte el notebook de evaluaciones en una configuración de promptfoo. |

**Notas:** Alternativas (elige una): openai-cookbook, awesome-llm-apps. Combinación anterior con anthropic-skills sustituida por claude-agent-sdk-python (más directa).

Estado en GitHub: activo · último push 2026-11-04 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/anthropics/claude-cookbooks/blob/main/README.md)</sub>

## Ver similares

Grupo **Cookbooks y ejemplos de apps con LLM**: Claude Cookbooks ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Awesome LLM Apps](awesome-llm-apps.md) ⭐ recomendado | 75 | Si buscas esto: colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM. |
| 2 | [OpenAI Cookbook](openai-cookbook.md) | 58 | Si buscas esto: ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales. |
| 3 | **Claude Cookbooks** (esta ficha) | 56 | Si buscas esto: recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Lectura libre; la ejecución de notebooks requiere API de Claude con facturación propia |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La suscripción de Claude Code no sustituye automáticamente la clave API pedida por estos notebooks |
| Coste | Consumo de APIs o servicios. Lectura libre; la ejecución de notebooks requiere API de Claude con facturación propia |
| Equipo | Preparación según la ruta elegida. Navegador; Python y clave Anthropic para ejecutar ejemplos |

La suscripción de Claude Code no sustituye automáticamente la clave API pedida por estos notebooks

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- Python y clave Anthropic para ejecutar ejemplos

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/anthropics/claude-cookbooks/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Claude Cookbooks para mi objetivo y necesito pasos guiados. Lee https://github.com/anthropics/claude-cookbooks/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee una receta de extracción y adapta sus datos a un párrafo ficticio.

**Qué comprobar:** Entiendes qué se envía al modelo y qué respuesta se valida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Clasificar tickets ficticios
- Estudiar llamadas a herramientas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Clasificar tickets ficticios; Estudiar llamadas a herramientas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La suscripción de Claude Code no sustituye automáticamente la clave API pedida por estos notebooks

## Stack y modelos

- **Stack:** Navegador; Python y clave Anthropic para ejecutar ejemplos
- **Etiquetas:** `learning` `notebooks` `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenAI Cookbook](openai-cookbook.md) | 77.1k | Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales. |
| [Awesome LLM Apps](awesome-llm-apps.md) | 145k | Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM. |

## Enlaces

- 🐙 GitHub: [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/anthropics/claude-cookbooks/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
