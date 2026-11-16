[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🎓 Awesome LLM Apps

> Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 145k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio

## ¿Qué es?

Colección (Apache-2.0) de @Shubhamsaboo con más de 100 plantillas open source de agentes, skills de agente y apps RAG. Es muy popular (~145k estrellas) y se actualiza a diario. El README afirma que cada plantilla está probada de principio a fin [DATO NO VERIFICADO].

## ¿Qué hace?

Reúne ejemplos ejecutables organizados por tipo: agentes iniciales y avanzados, equipos multiagente, agentes de voz, agentes MCP, RAG, apps con memoria, interfaces generativas y fine-tuning. Funcionan con Claude, Gemini, GPT, DeepSeek, Llama, Qwen y modelos locales. Usan frameworks variados, entre ellos Agno, OpenAI Agents SDK, Google ADK, CrewAI y LangGraph.

## ¿Cómo lo hace?

Cada plantilla es independiente: se clona el repositorio, se entra en la carpeta, se ejecuta `pip install -r requirements.txt` y se lanza, muchas veces con Streamlit. Las skills de agente se instalan con `npx skills add <url>`. Cada ejemplo pide sus propias claves de API. La calidad y el mantenimiento varían entre plantillas, así que hay que revisarlas antes de producción.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [streamlit](streamlit.md) | Interfaz de muchas de las apps de ejemplo. | Se instala con los requirements de cada plantilla. |
| [OpenAI Agents SDK](openai-agents-python.md) | Framework usado por varias plantillas de agentes (citado en el README). | Instálalo dentro del entorno de la plantilla que lo use. |
| [Agent Development Kit (ADK)](adk-python.md) | Framework de Google usado en otras plantillas (citado en el README). | Instálalo en el entorno de la plantilla correspondiente. |
| [firecrawl](firecrawl.md) | Extracción web en plantillas de investigación y scraping (citado en el README). | Configura la clave de Firecrawl antes de lanzar esas plantillas. |

**Notas:** Alternativas (elige una): openai-cookbook, claude-cookbooks.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La colección se consulta gratis; hay apps con API, modelos locales y skills que usan el plan del anfitrión |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | Modelos locales documentados. Documenta skills para Claude Code y Codex; no todas las apps son skills ni tienen idéntica compatibilidad o instalación |
| Coste | El coste depende del proveedor o la ruta. La colección se consulta gratis; hay apps con API, modelos locales y skills que usan el plan del anfitrión |
| Equipo | Preparación según la ruta elegida. Navegador; entorno y proveedor específicos del ejemplo elegido |

Documenta skills para Claude Code y Codex; no todas las apps son skills ni tienen idéntica compatibilidad o instalación

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- entorno y proveedor específicos del ejemplo elegido

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Awesome LLM Apps para mi objetivo y necesito pasos guiados. Lee https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Escoge una app de RAG local y revisa su README y requisitos antes de descargar modelos.

**Qué comprobar:** Sabes qué archivos, modelo y servicio necesita esa app concreta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender con un asistente de viajes
- Estudiar un RAG con Llama local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender con un asistente de viajes; Estudiar un RAG con Llama local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta skills para Claude Code y Codex; no todas las apps son skills ni tienen idéntica compatibilidad o instalación

## Stack y modelos

- **Stack:** Navegador; entorno y proveedor específicos del ejemplo elegido
- **Etiquetas:** `agents` `rag` `learning` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenAI Cookbook](openai-cookbook.md) | 77.1k | Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales. |
| [Claude Cookbooks](claude-cookbooks.md) | 54.7k | Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización. |

## Enlaces

- 🐙 GitHub: [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 🌐 Web: <https://www.theunwindai.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
