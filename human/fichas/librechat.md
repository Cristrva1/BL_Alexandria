[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 LibreChat

> Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47.1k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de chat con IA de código abierto (MIT) y autoalojable, del equipo LibreChat-AI, con agentes, MCP y autenticación multiusuario empresarial. Muy activa (v0.8.8 descrita en el README; sin releases formales en GitHub).

## ¿Qué hace?

Unifica en una interfaz OpenAI, Azure, Anthropic, AWS Bedrock, Google/Vertex y cualquier API compatible con OpenAI (Ollama, groq, Mistral, together.ai y otros) mediante endpoints personalizados. Incluye agentes con herramientas y MCP, artefactos, intérprete de código, búsqueda de archivos, generación de imágenes, búsqueda en conversaciones y, en la v0.8.8, una API de gestión de agentes (beta), espacios de trabajo adjuntos (muy experimental) con controles de aprobación de código, visor de trazas y exportación por OpenTelemetry con identidad de trazas para Langfuse.

## ¿Cómo lo hace?

Aplicación Node.js/React configurada con `librechat.yaml`. El Docker Compose del repositorio levanta la API con MongoDB, Meilisearch para búsqueda, PostgreSQL con pgvector y un servicio RAG API para archivos; la interfaz suele quedar en el puerto 3080 [DATO NO VERIFICADO: puerto por defecto, tomado de la documentación].

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | LiteLLM como endpoint personalizado para centralizar proveedores, claves y gasto. | LiteLLM primero; declara su URL en `librechat.yaml`. |
| [Ollama](ollama.md) | Ollama figura entre los proveedores locales compatibles. | Ollama accesible desde la red de Docker (host.docker.internal o IP). |
| [langfuse](langfuse.md) | La v0.8.8 permite configurar identidad y metadatos de trazas para Langfuse. | Langfuse en marcha con claves de proyecto; configúralas en LibreChat. |
| [llama.cpp](llama-cpp.md) | Combinación recíproca: llama.cpp lo enlaza como «LibreChat admite endpoints personalizados compatibles con OpenAI, como el de llama.cpp». | Orden indicado desde llama.cpp: Servidor de llama.cpp accesible desde el contenedor de LibreChat; luego decláralo en `librechat.yaml`. |
| [pgvector](pgvector.md) | Combinación recíproca: pgvector lo enlaza como «El Docker Compose de LibreChat usa una imagen pgvector para su RAG API». | Orden indicado desde pgvector: Ya viene incluido; no instales otro Postgres salvo que quieras externalizarlo. |
| [exo](exo.md) | Combinación recíproca: exo lo enlaza como «Endpoint personalizado compatible con OpenAI para un chat multiusuario sobre el clúster (combinación por arquitectura)». | Orden indicado desde exo: Igual que arriba; asegúrate de que el contenedor llega a la IP del nodo. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (3). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[llamafile](llamafile.md) · [LocalAI](localai.md) · [Text Generation WebUI](textgen.md)

**Notas:** Alternativas (elige una): open-webui, lobehub. Meilisearch, pgvector y RAG API ya vienen en su Compose.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/LibreChat-AI/LibreChat/blob/main/README.md) · [2](https://github.com/LibreChat-AI/LibreChat/blob/main/docker-compose.yml)</sub>

## Ver similares

Grupo **Interfaces de chat con LLM**: LibreChat ocupa la posición 4 de 8 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Open WebUI](open-webui.md) ⭐ recomendado | 74 | Si quieres la interfaz más completa para Ollama o APIs, multiusuario y con RAG. |
| 2 | [Cherry Studio](cherry-studio.md) | 72 | Si quieres un cliente de escritorio para muchos proveedores con asistentes predefinidos. |
| 3 | [LobeHub](lobehub.md) | 70 | Si quieres una interfaz moderna con plugins, agentes y despliegue sencillo. |
| 4 | **LibreChat** (esta ficha) | 68 | Si necesitas un clon de ChatGPT multiusuario con muchos proveedores, agentes y control de acceso. |
| 5 | [Jan](jan.md) | 65 | Si prefieres una app de escritorio que funcione sin conexión con modelos locales. |
| 6 | [NextChat](nextchat.md) | 63 | Si quieres desplegar una interfaz ligera en Vercel con un clic. |
| 7 | [chatbox](chatbox.md) | 52 | Si quieres un cliente de escritorio y móvil sencillo para tus claves de API. |
| 8 | [Text Generation WebUI](textgen.md) | 50 | Si quieres experimentar con muchos backends y formatos de modelos locales (GGUF, EXL2, Transformers). |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La interfaz abierta no incluye crédito de modelos; almacenamiento, herramientas y proveedores tienen costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Sus agentes y MCP funcionan dentro de LibreChat; no acreditan usar una suscripción de otro editor para ejecutarlo |
| Coste | El coste depende del proveedor o la ruta. La interfaz abierta no incluye crédito de modelos; almacenamiento, herramientas y proveedores tienen costes propios |
| Equipo | Preparación según la ruta elegida. Ruta de despliegue elegida; base de datos; proveedor u Ollama |

Sus agentes y MCP funcionan dentro de LibreChat; no acreditan usar una suscripción de otro editor para ejecutarlo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Ruta de despliegue elegida
- base de datos
- proveedor u Ollama

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://www.librechat.ai/docs)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LibreChat para mi objetivo y necesito pasos guiados. Lee https://www.librechat.ai/docs. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta un proveedor y prueba un agente sin herramientas antes de añadir archivos.

**Qué comprobar:** Puedes identificar el modelo y revisar la conversación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Unificar proveedores en una interfaz
- Crear asistentes con herramientas y archivos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Unificar proveedores en una interfaz; Crear asistentes con herramientas y archivos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Sus agentes y MCP funcionan dentro de LibreChat; no acreditan usar una suscripción de otro editor para ejecutarlo

## Stack y modelos

- **Stack:** Ruta de despliegue elegida; base de datos; proveedor u Ollama
- **Etiquetas:** `chatbot` `agents` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open WebUI](open-webui.md) | 159k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |
| [LobeHub](lobehub.md) | 85.5k | Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. |

## Enlaces

- 🐙 GitHub: [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat)
- 🌐 Web: <https://librechat.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/LibreChat-AI/LibreChat/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
