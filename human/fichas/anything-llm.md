[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Workspaces privados y segundos cerebros

# 🏠 AnythingLLM

> App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 68.3k | MIT | JavaScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Aplicación de IA «todo en uno» de código abierto (MIT) de Mintplex Labs, con versión de escritorio (Mac, Windows, Linux), Docker multiusuario, instancia alojada y app Android. Madura y activa (v1.19.0).

## ¿Qué hace?

Permite chatear con tus documentos, crear agentes sin código, usar MCP, programar tareas con cron, enrutar conversaciones al mejor modelo según reglas, mantener memorias y seleccionar herramientas para reducir tokens. La versión Docker añade multiusuario con permisos y un widget de chat incrustable para sitios web.

## ¿Cómo lo hace?

Monorepo en Node.js: frontend Vite + React, servidor y un `collector` Express que procesa documentos. Trae un motor local de LLM opcional (CPU o GPU vía Lemonade), embebedor nativo y LanceDB como base vectorial por defecto, y admite muchos proveedores (Ollama, LM Studio, LocalAI, LiteLLM, etc.) y bases vectoriales (PGVector, Qdrant, Chroma, Weaviate, Milvus, Pinecone, entre otras).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor documentado de chat y de embeddings. | Ollama con un modelo de chat y uno de embeddings; desde Docker usa host.docker.internal. |
| [Qdrant](qdrant.md) | Base vectorial soportada cuando LanceDB embebida se queda corta. | Qdrant primero; elige el vectorizador antes de ingerir documentos (cambiarlo obliga a reindexar). |
| [litellm](litellm.md) | Proveedor soportado para enrutar varios modelos detrás de un proxy. | LiteLLM primero; configura su URL y clave. |
| [LocalAI](localai.md) | Proveedor soportado de LLM y embeddings totalmente local. | Alternativa a Ollama como motor: usa uno de los dos. |
| [Chroma](chroma.md) | Combinación recíproca: Chroma lo enlaza como «Base vectorial soportada (Chroma y ChromaCloud)». | Orden indicado desde Chroma: Servidor Chroma primero; configura su URL en AnythingLLM. |
| [Milvus](milvus.md) | Combinación recíproca: Milvus lo enlaza como «Base vectorial soportada por AnythingLLM». | Orden indicado desde Milvus: Milvus primero; configura su URL en AnythingLLM antes de ingerir documentos. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[llamafile](llamafile.md) · [pgvector](pgvector.md)

**Notas:** Alternativas (elige una): open-webui, khoj, private-gpt, onyx.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v1.19.0 (2026-10-26) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Puede usar motor local y proveedores remotos; los modelos, servicios y alojamiento tienen costes separados |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Desktop, Docker y móvil tienen capacidades y licencias que debes comprobar; elige también embeddings locales para una ruta privada completa |
| Coste | El coste depende del proveedor o la ruta. Puede usar motor local y proveedores remotos; los modelos, servicios y alojamiento tienen costes separados |
| Equipo | Preparación según la ruta elegida. App de escritorio o Docker; LLM y embeddings; documento de prueba |

Desktop, Docker y móvil tienen capacidades y licencias que debes comprobar; elige también embeddings locales para una ruta privada completa

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- App de escritorio o Docker
- LLM y embeddings
- documento de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AnythingLLM para mi objetivo y necesito pasos guiados. Lee https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un workspace con un PDF corto y consulta un dato presente en él.

**Qué comprobar:** Puedes abrir el fragmento que apoya la respuesta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar documentación propia
- Separar bases de conocimiento por proyecto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar documentación propia; Separar bases de conocimiento por proyecto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Desktop, Docker y móvil tienen capacidades y licencias que debes comprobar; elige también embeddings locales para una ruta privada completa

## Stack y modelos

- **Stack:** App de escritorio o Docker; LLM y embeddings; documento de prueba
- **Etiquetas:** `rag` `agents` `local` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open WebUI](open-webui.md) | 159k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |
| [Khoj](khoj.md) | 38.1k | Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones. |
| [PrivateGPT](private-gpt.md) | 57.6k | Capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP. |
| [onyx](onyx.md) | 33.4k | Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso. |

## Enlaces

- 🐙 GitHub: [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)
- 🌐 Web: <https://anythingllm.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
