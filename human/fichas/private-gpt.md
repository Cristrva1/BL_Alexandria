[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Workspaces privados y segundos cerebros

# 🏠 PrivateGPT

> Capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 57.6k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Capa de API de código abierto (Apache 2.0) de Zylon que convierte modelos locales en aplicaciones de IA para producción; es la base de la plataforma on-premise Zylon. Versión 1.0.1 publicada en 2026.

## ¿Qué hace?

Ofrece una API que sigue el modelo de la API de Claude: mensajes con streaming y conteo de tokens, ingesta de archivos, recuperación con citas y RAG agéntico, herramientas integradas (búsqueda web, lectura web, ejecución de código), herramientas propias y conectores MCP, acceso estructurado a bases de datos y CSV, embeddings y orquestación. Incluye una interfaz de pruebas en `/ui`; el producto es la API.

## ¿Cómo lo hace?

No ejecuta modelos: se conecta a cualquier servidor compatible con OpenAI que implemente `/v1/chat/completions` y `/v1/models` mediante `OPENAI_API_BASE` (y `OPENAI_EMBEDDING_API_BASE` para embeddings). Se instala con Homebrew en macOS o con `uv tool install` (Python 3.11) en Linux y Windows, o con Docker; API en el puerto 8080.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Punto de partida recomendado como servidor de LLM y embeddings. | Ollama primero con el modelo de chat y el de embeddings; después exporta las variables y arranca PrivateGPT. |
| [vLLM](vllm.md) | Servidor compatible con OpenAI para producción con GPU (combinación por arquitectura). | vLLM primero; apunta `OPENAI_API_BASE` a su /v1 y usa otro puerto distinto de 8080. |
| [llama.cpp](llama-cpp.md) | `llama serve` cumple los endpoints requeridos (combinación por arquitectura). | Arráncalo en un puerto distinto de 8080 para no chocar con PrivateGPT. |

**Notas:** Alternativa (elige una): anything-llm. La combinación antigua con qdrant se retiró porque el README actual no la menciona.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v1.0.1 (2026-06-18) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zylon-ai/private-gpt/blob/main/README.md) · [2](https://docs.privategpt.dev/getting-started/quickstart)</sub>

## Ver similares

Grupo **Workspaces privados con documentos y chat**: PrivateGPT ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [AnythingLLM](anything-llm.md) ⭐ recomendado | 78 | Si buscas esto: app todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |
| 2 | **PrivateGPT** (esta ficha) | 67 | Si buscas esto: capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP. |
| 3 | [Khoj](khoj.md) | 48 | Si buscas esto: segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El servidor de inferencia y embeddings usan recursos propios o proveedores según configuración; no incluye modelos de pago |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La guía documenta backend local para Claude Code; no confirma por eso integración de todas las funciones de Codex o Antigravity |
| Coste | El coste depende del proveedor o la ruta. El servidor de inferencia y embeddings usan recursos propios o proveedores según configuración; no incluye modelos de pago |
| Equipo | Preparación según la ruta elegida. Servidor LLM compatible OpenAI; Python 3.11 o distribución adecuada; documentos de prueba |

La guía documenta backend local para Claude Code; no confirma por eso integración de todas las funciones de Codex o Antigravity

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servidor LLM compatible OpenAI
- Python 3.11 o distribución adecuada
- documentos de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.privategpt.dev/getting-started/quickstart)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PrivateGPT para mi objetivo y necesito pasos guiados. Lee https://docs.privategpt.dev/getting-started/quickstart. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta el servidor local y consulta un documento breve con la API de RAG.

**Qué comprobar:** Puedes seguir la consulta y comprobar el fragmento recuperado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir una API privada sobre documentos
- Usar un modelo local como backend de programación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir una API privada sobre documentos; Usar un modelo local como backend de programación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La guía documenta backend local para Claude Code; no confirma por eso integración de todas las funciones de Codex o Antigravity

## Stack y modelos

- **Stack:** Servidor LLM compatible OpenAI; Python 3.11 o distribución adecuada; documentos de prueba
- **Etiquetas:** `rag` `local` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AnythingLLM](anything-llm.md) | 68.3k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |

## Enlaces

- 🐙 GitHub: [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt)
- 🌐 Web: <https://www.zylon.ai/private-gpt>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zylon-ai/private-gpt/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
