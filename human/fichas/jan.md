[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 Jan

> Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 45.7k | Apache-2.0 | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** Apache-2.0. Fuente: [LICENSE](https://github.com/janhq/jan/blob/main/LICENSE). GitHub la marca como NOASSERTION.

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

## Ver similares

Grupo **Interfaces de chat con LLM**: Jan ocupa la posición 5 de 8 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Open WebUI](open-webui.md) ⭐ recomendado | 74 | Si quieres la interfaz más completa para Ollama o APIs, multiusuario y con RAG. |
| 2 | [Cherry Studio](cherry-studio.md) | 72 | Si quieres un cliente de escritorio para muchos proveedores con asistentes predefinidos. |
| 3 | [LobeHub](lobehub.md) | 70 | Si quieres una interfaz moderna con plugins, agentes y despliegue sencillo. |
| 4 | [LibreChat](librechat.md) | 69 | Si necesitas un clon de ChatGPT multiusuario con muchos proveedores, agentes y control de acceso. |
| 5 | **Jan** (esta ficha) | 66 | Si prefieres una app de escritorio que funcione sin conexión con modelos locales. |
| 6 | [NextChat](nextchat.md) | 64 | Si quieres desplegar una interfaz ligera en Vercel con un clic. |
| 7 | [chatbox](chatbox.md) | 52 | Si quieres un cliente de escritorio y móvil sencillo para tus claves de API. |
| 8 | [Text Generation WebUI](textgen.md) | 51 | Si quieres experimentar con muchos backends y formatos de modelos locales (GGUF, EXL2, Transformers). |

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

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/janhq/jan
```

Comando copiado literalmente de el README (sección «Run with Make»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/janhq/jan/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Jan para mi objetivo y necesito pasos guiados. Lee https://github.com/janhq/jan/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
