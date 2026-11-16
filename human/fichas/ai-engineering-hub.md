[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🧠 ai-engineering-hub

> Colección de tutoriales y proyectos prácticos sobre LLM, RAG, agentes y aplicaciones de inteligencia artificial.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 41.9k | MIT | Jupyter Notebook | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección (MIT) de @patchy631 con tutoriales y más de 93 proyectos de ingeniería de IA: 22 de nivel principiante, 48 intermedios y 23 avanzados. Es activa (último push en noviembre de 2026) y está asociada a una newsletter.

## ¿Qué hace?

Ofrece proyectos prácticos sobre LLMs, RAG, agentes, MCP (el tema más presente) y aplicaciones multimodales, a menudo con modelos como DeepSeek y herramientas como CrewAI, LlamaIndex o Firecrawl. Sirve como material de aprendizaje por proyectos. El README los califica de 'production-ready' [DATO NO VERIFICADO].

## ¿Cómo lo hace?

Cada proyecto vive en su carpeta con instrucciones y dependencias propias, en su mayoría Python. Requiere las claves de API de los servicios que use cada ejemplo, aunque algunos usan modelos locales con Ollama. Hay que revisar versiones, porque muchos ejemplos fijan bibliotecas que evolucionan rápido.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [crewAI](crewai.md) | Framework de agentes usado en varios proyectos. | Instálalo en el entorno del proyecto que lo use. |
| [LlamaIndex](llama-index.md) | RAG en varios proyectos del hub. | Instálalo según el proyecto. |
| [firecrawl](firecrawl.md) | Extracción web usada en proyectos de investigación. | Configura su clave antes de ejecutar esos ejemplos. |
| [Ollama](ollama.md) | Modelos locales en algunos proyectos. | Instala Ollama y descarga el modelo indicado. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-01 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/patchy631/ai-engineering-hub/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Tutoriales públicos; APIs, nube y GPU pueden generar costes según el ejemplo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Las comparaciones con Claude Code son contenido educativo y no una integración instalada del catálogo |
| Coste | El coste depende del proveedor o la ruta. Tutoriales públicos; APIs, nube y GPU pueden generar costes según el ejemplo |
| Equipo | Preparación según la ruta elegida. Python; README específico del tutorial; modelo local o proveedor |

Las comparaciones con Claude Code son contenido educativo y no una integración instalada del catálogo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- README específico del tutorial
- modelo local o proveedor

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/patchy631/ai-engineering-hub/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ai-engineering-hub para mi objetivo y necesito pasos guiados. Lee https://github.com/patchy631/ai-engineering-hub/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige Simple RAG Workflow y dibuja ingestión, recuperación y generación.

**Qué comprobar:** Puedes identificar dónde se almacenan documentos y dónde se usa el modelo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender RAG con Ollama
- Comparar técnicas de ajuste fino

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender RAG con Ollama; Comparar técnicas de ajuste fino | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las comparaciones con Claude Code son contenido educativo y no una integración instalada del catálogo

## Stack y modelos

- **Stack:** Python; README específico del tutorial; modelo local o proveedor
- **Etiquetas:** `guias` `agents` `ai` `llms` `machine-learning` `mcp` `rag` `jupyter notebook`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)
- 🌐 Web: <https://join.dailydoseofds.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/patchy631/ai-engineering-hub/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
