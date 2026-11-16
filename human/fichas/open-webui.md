[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 Open WebUI

> Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 159k | NOASSERTION | Svelte | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Open WebUI, plataforma de chat con IA autoalojada y extensible, diseñada para poder funcionar sin conexión, de Open WebUI Inc. (creada por Timothy Jaeryang Baek). Usa la «Open WebUI License», tipo BSD-3 con una cláusula que obliga a conservar la marca Open WebUI; las contribuciones anteriores siguen bajo sus licencias originales. No es una licencia OSI estándar, por eso GitHub muestra NOASSERTION. Es muy popular (~159k estrellas, v0.13.x) y tiene edición Enterprise.

## ¿Qué hace?

Ofrece una interfaz web tipo ChatGPT para modelos locales vía Ollama o para cualquier API compatible con OpenAI, local o en la nube. Su documentación incluye búsqueda web, bases de conocimiento y una app de escritorio para macOS, Windows y Linux.

## ¿Cómo lo hace?

Frontend en Svelte y backend en Python: se instala con `pip install open-webui` o `uvx` (Python 3.12) o como contenedor Docker. Las imágenes `:main` (con dependencias locales de IA), `:slim` (delega embeddings, extracción y voz a servicios externos), `:cuda` (GPU) y `:ollama` (Ollama incluido) cubren distintos equipos. Se configura con variables como `OLLAMA_BASE_URL` y `OPENAI_API_KEY`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Fuente de modelos locales; es la conexión principal documentada. | Ollama primero, o elige la imagen `:ollama` para tener ambos en un contenedor. |
| [litellm](litellm.md) | Como endpoint compatible con OpenAI, LiteLLM da acceso a más de 100 proveedores con claves virtuales y control de gasto desde la misma interfaz. | LiteLLM proxy primero (puerto 4000); luego añádelo como conexión OpenAI en Open WebUI. |
| [SearXNG](searxng.md) | Motor de búsqueda web autoalojado para las respuestas con búsqueda en Open WebUI. | SearXNG primero; activa el formato `json` en su `settings.yml` (si no, Open WebUI recibe 403) y define `SEARXNG_QUERY_URL`. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (16). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[exo](exo.md) · [Fabric](fabric.md) · [FreeToken](freetoken.md) · [Helicone](helicone.md) · [Jina Reader](jina-reader.md) · [KoboldCpp](koboldcpp.md) · [langfuse](langfuse.md) · [llama.cpp](llama-cpp.md) · [llamafile](llamafile.md) · [LocalAI](localai.md) · [MLC LLM](mlc-llm.md) · [MLX LM](mlx-lm.md) · [prompts.chat](prompts-chat.md) · [SGLang](sglang.md) · [TensorRT-LLM](tensorrt-llm.md) · [vLLM](vllm.md)

**Notas:** Alternativas (elige una): librechat, lobehub, anything-llm, textgen. La cláusula de marca limita el rebranding: revisa LICENSE antes de redistribuirlo con otra imagen.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.13.3 (2026-11-08) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/open-webui/open-webui/blob/main/README.md) · [2](https://docs.openwebui.com/features/chat-conversations/web-search/providers/searxng)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Los modelos remotos consumen API; Ollama local necesita hardware; la licencia exige conservar branding salvo las excepciones aplicables |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Instalar la interfaz no instala todos los modelos; confirma que Docker puede alcanzar el servidor de inferencia |
| Coste | El coste depende del proveedor o la ruta. Los modelos remotos consumen API; Ollama local necesita hardware; la licencia exige conservar branding salvo las excepciones aplicables |
| Equipo | Preparación según la ruta elegida. Docker; Ollama accesible o proveedor remoto; volumen persistente |

Instalar la interfaz no instala todos los modelos; confirma que Docker puede alcanzar el servidor de inferencia

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- Ollama accesible o proveedor remoto
- volumen persistente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/open-webui/open-webui/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Open WebUI para mi objetivo y necesito pasos guiados. Lee https://github.com/open-webui/open-webui/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta un modelo y conversa sobre un texto ficticio antes de cargar documentos privados.

**Qué comprobar:** Puedes ver el modelo seleccionado y conservar una conversación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Unificar chats de modelos locales
- Crear una interfaz compartida para un equipo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Unificar chats de modelos locales; Crear una interfaz compartida para un equipo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Instalar la interfaz no instala todos los modelos; confirma que Docker puede alcanzar el servidor de inferencia

## Stack y modelos

- **Stack:** Docker; Ollama accesible o proveedor remoto; volumen persistente
- **Etiquetas:** `chatbot` `local` `rag` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LibreChat](librechat.md) | 47.1k | Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada. |
| [LobeHub](lobehub.md) | 85.5k | Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. |
| [AnythingLLM](anything-llm.md) | 68.3k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |
| [Text Generation WebUI](textgen.md) | 47.7k | App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic. |

## Enlaces

- 🐙 GitHub: [open-webui/open-webui](https://github.com/open-webui/open-webui)
- 🌐 Web: <https://openwebui.com>
- 🧪 Receta: [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/open-webui/open-webui/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
