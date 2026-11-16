[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 Jan

> Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 45.7k | NOASSERTION | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Aplicación de escritorio de código abierto presentada como reemplazo de ChatGPT, de Menlo Research (janhq). Licencia Apache 2.0 según su README (GitHub no la detecta como estándar); activa, con versiones frecuentes (v0.8.8).

## ¿Qué hace?

Descarga y ejecuta LLM de Hugging Face (Llama, Gemma, Qwen, GPT-oss, etc.) con control total y privacidad, y se conecta también a OpenAI, Anthropic, Mistral, Groq, MiniMax y otros. Permite crear asistentes personalizados, usar MCP para capacidades de agente y exponer un servidor local compatible con OpenAI en `localhost:1337` para otras aplicaciones.

## ¿Cómo lo hace?

App de escritorio con Tauri (Rust) y frontend en TypeScript que incluye el motor llama.cpp (variantes CPU, CUDA 12/13, Vulkan). Se descarga para Windows, macOS y Linux (deb, AppImage, Arm64); compilar desde código requiere Node.js ≥ 20, Yarn ≥ 4.5.3, Make y Rust.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [llmfit](llmfit.md) | Elegir qué modelo y cuantización caben en tu equipo antes de descargarlos en Jan (combinación por arquitectura). | Ejecuta llmfit primero; descarga en Jan el modelo recomendado. |
| [Ollama](ollama.md) | Usar modelos ya descargados en Ollama añadiéndolo como proveedor compatible con OpenAI (combinación por arquitectura). | Ollama en 11434; añade su URL /v1 como proveedor en Jan. |
| [Playwright MCP](playwright-mcp.md) | Dar al asistente acceso a un navegador mediante su soporte de MCP (combinación por arquitectura). | Registra el servidor MCP en Jan y limita los sitios a los que puede ir. |

**Notas:** Alternativas (elige una): cherry-studio, textgen, chatbox.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v0.8.8 (2026-10-28) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/janhq/jan/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El modo local usa tu equipo; los proveedores remotos tienen sus tarifas; modelos tienen licencias propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Para comenzar usa la distribución de escritorio; make dev y yarn son rutas para desarrollar el código de Jan |
| Coste | El coste depende del proveedor o la ruta. El modo local usa tu equipo; los proveedores remotos tienen sus tarifas; modelos tienen licencias propias |
| Equipo | Preparación según la ruta elegida. Instalador de escritorio oficial; RAM y disco; modelo compatible |

Para comenzar usa la distribución de escritorio; make dev y yarn son rutas para desarrollar el código de Jan

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador de escritorio oficial
- RAM y disco
- modelo compatible

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://jan.ai/docs)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Jan para mi objetivo y necesito pasos guiados. Lee https://jan.ai/docs. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Desde la app descarga un modelo pequeño y prueba una conversación local.

**Qué comprobar:** Ves el modelo cargado y puedes repetir la consulta sin proveedor remoto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Conversar con un modelo privado
- Comparar un modelo local con una API

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Conversar con un modelo privado; Comparar un modelo local con una API | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Para comenzar usa la distribución de escritorio; make dev y yarn son rutas para desarrollar el código de Jan

## Stack y modelos

- **Stack:** Instalador de escritorio oficial; RAM y disco; modelo compatible
- **Etiquetas:** `chatbot` `local` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Cherry Studio](cherry-studio.md) | 53.5k | App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad. |
| [Text Generation WebUI](textgen.md) | 47.7k | App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic. |
| [chatbox](chatbox.md) | 42.3k | Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común. |

## Enlaces

- 🐙 GitHub: [janhq/jan](https://github.com/janhq/jan)
- 🌐 Web: <https://jan.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/janhq/jan/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
