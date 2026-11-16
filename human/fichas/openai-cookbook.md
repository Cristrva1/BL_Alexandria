[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🎓 OpenAI Cookbook

> Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 77.1k | MIT | Jupyter Notebook | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Recetario oficial de OpenAI (MIT) con ejemplos de código y guías para tareas comunes con su API. Se navega en cookbook.openai.com. Es activo (último push en noviembre de 2026) y maduro.

## ¿Qué hace?

Ofrece notebooks y guías para tareas comunes: embeddings y búsqueda, RAG, function calling, salidas estructuradas, evaluación, agentes, voz en tiempo real, visión, fine-tuning y patrones de producción. También recoge recursos relacionados de terceros. El contenido está atado a la API y los productos de OpenAI.

## ¿Cómo lo hace?

La mayoría de los ejemplos son notebooks Python que requieren una cuenta y una clave de API de OpenAI (`OPENAI_API_KEY`), con su coste correspondiente. Los conceptos se pueden trasladar a otros lenguajes. No se instala como paquete: se clona o se consulta en la web.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [openai-python](openai-python.md) | SDK oficial usado por casi todos los notebooks. | Instala `openai` en el entorno antes de ejecutar los ejemplos. |
| [OpenAI Agents SDK](openai-agents-python.md) | Recetas de agentes del cookbook basadas en el Agents SDK de OpenAI. | Instálalo cuando sigas las recetas de agentes. |
| [promptfoo](promptfoo.md) | Llevar las evaluaciones del cookbook a una suite automatizada y comparable entre modelos. (combinación por arquitectura) | Reutiliza los casos de prueba del notebook en promptfoo. |
| [Generative AI for Beginners](generative-ai-for-beginners.md) | Combinación recíproca: Generative AI for Beginners lo enlaza como «Recetas más avanzadas para quienes usan la API de OpenAI en los ejercicios. (combinación por arquitectura)». | Orden indicado desde Generative AI for Beginners: Úsalo como siguiente paso práctico tras las lecciones 'Build'. |

**Notas:** Alternativas (elige una): claude-cookbooks, awesome-llm-apps.

Estado en GitHub: activo · último push 2026-11-14 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/openai/openai-cookbook/blob/main/README.md) · [2](https://cookbook.openai.com)</sub>

## Ver similares

Grupo **Cookbooks y ejemplos de apps con LLM**: OpenAI Cookbook ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Awesome LLM Apps](awesome-llm-apps.md) ⭐ recomendado | 75 | Si buscas esto: colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM. |
| 2 | **OpenAI Cookbook** (esta ficha) | 58 | Si buscas esto: ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales. |
| 3 | [Claude Cookbooks](claude-cookbooks.md) | 56 | Si buscas esto: recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Lectura libre; los ejemplos API requieren cuenta, clave y consumo separado de ChatGPT o Codex |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Es un recetario oficial de API; no es un paquete de plugins ni una promesa de acceso mediante suscripción |
| Coste | Consumo de APIs o servicios. Lectura libre; los ejemplos API requieren cuenta, clave y consumo separado de ChatGPT o Codex |
| Equipo | Preparación según la ruta elegida. Navegador; Python y API key de OpenAI si ejecutas notebooks |

Es un recetario oficial de API; no es un paquete de plugins ni una promesa de acceso mediante suscripción

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- Python y API key de OpenAI si ejecutas notebooks

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/openai/openai-cookbook/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenAI Cookbook para mi objetivo y necesito pasos guiados. Lee https://github.com/openai/openai-cookbook/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una receta de salida estructurada y revisa su esquema antes de ejecutar una entrada breve.

**Qué comprobar:** Puedes identificar la petición, respuesta esperada y consumo de la receta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Extraer campos de un texto
- Aprender a evaluar respuestas de una aplicación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Extraer campos de un texto; Aprender a evaluar respuestas de una aplicación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un recetario oficial de API; no es un paquete de plugins ni una promesa de acceso mediante suscripción

## Stack y modelos

- **Stack:** Navegador; Python y API key de OpenAI si ejecutas notebooks
- **Etiquetas:** `learning` `notebooks` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Cookbooks](claude-cookbooks.md) | 54.7k | Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, caché y optimización. |
| [Awesome LLM Apps](awesome-llm-apps.md) | 145k | Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y skills, con varios LLM. |

## Enlaces

- 🐙 GitHub: [openai/openai-cookbook](https://github.com/openai/openai-cookbook)
- 🌐 Web: <https://cookbook.openai.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openai/openai-cookbook/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
