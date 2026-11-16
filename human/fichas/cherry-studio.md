[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 Cherry Studio

> App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 53.5k | AGPL-3.0 | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Estación de trabajo de IA de escritorio para Windows, macOS y Linux, de CherryHQ, con app móvil aparte. La edición comunitaria es AGPL-3.0 (el uso comercial se permite cumpliendo la AGPL; hay licencia comercial y una edición Enterprise); muy activa (v2.2.2).

## ¿Qué hace?

Reúne chat con varios modelos (incluida la comparación de respuestas en una misma conversación), agentes con instrucciones, espacios de trabajo, modelos y permisos propios que trabajan con archivos, ejecutan comandos y automatizan el navegador o el equipo. Permite ampliar con skills y servidores MCP, programar tareas, conectar agentes a mensajería («Channels»), crear bases de conocimiento locales desde archivos, carpetas y webs, y generar imágenes.

## ¿Cómo lo hace?

Aplicación de escritorio que conecta proveedores en la nube (OpenAI, Anthropic, Gemini y servicios compatibles) y modelos locales vía Ollama y LM Studio, con gestión centralizada de claves y modelos. Se descarga desde su web; la edición Enterprise añade gestión centralizada de modelos y despliegue privado.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor local soportado para chatear con modelos sin enviar datos fuera. | Ollama con modelos descargados; selecciónalo en la configuración de proveedores. |
| [litellm](litellm.md) | Usar un proxy propio como servicio compatible personalizado (combinación por arquitectura). | LiteLLM primero; añade su URL y clave como proveedor compatible con OpenAI. |
| [Playwright MCP](playwright-mcp.md) | Ampliar los agentes con un servidor MCP de navegador (combinación por arquitectura). | Registra el MCP y revisa los permisos de herramientas del agente. |

**Notas:** Alternativas (elige una): jan, lobehub. Los agentes pueden ejecutar comandos: revisa sus permisos.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.2.2 (2026-11-13) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/CherryHQ/cherry-studio/blob/main/README.md)</sub>

## Ver similares

Grupo **Interfaces de chat con LLM**: Cherry Studio ocupa la posición 2 de 8 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Open WebUI](open-webui.md) ⭐ recomendado | 74 | Si quieres la interfaz más completa para Ollama o APIs, multiusuario y con RAG. |
| 2 | **Cherry Studio** (esta ficha) | 72 | Si quieres un cliente de escritorio para muchos proveedores con asistentes predefinidos. |
| 3 | [LobeHub](lobehub.md) | 70 | Si quieres una interfaz moderna con plugins, agentes y despliegue sencillo. |
| 4 | [LibreChat](librechat.md) | 68 | Si necesitas un clon de ChatGPT multiusuario con muchos proveedores, agentes y control de acceso. |
| 5 | [Jan](jan.md) | 65 | Si prefieres una app de escritorio que funcione sin conexión con modelos locales. |
| 6 | [NextChat](nextchat.md) | 63 | Si quieres desplegar una interfaz ligera en Vercel con un clic. |
| 7 | [chatbox](chatbox.md) | 52 | Si quieres un cliente de escritorio y móvil sencillo para tus claves de API. |
| 8 | [Text Generation WebUI](textgen.md) | 50 | Si quieres experimentar con muchos backends y formatos de modelos locales (GGUF, EXL2, Transformers). |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Los proveedores y funciones remotas pueden cobrar; el código es AGPL y ofrece alternativa de licencia comercial |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es una app multiproveedor; escoger Anthropic u OpenAI no la convierte en sesión de Claude Code o Codex |
| Coste | El coste depende del proveedor o la ruta. Los proveedores y funciones remotas pueden cobrar; el código es AGPL y ofrece alternativa de licencia comercial |
| Equipo | Preparación según la ruta elegida. Instalador para Windows, macOS o Linux; proveedor o Ollama/LM Studio |

Es una app multiproveedor; escoger Anthropic u OpenAI no la convierte en sesión de Claude Code o Codex

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador para Windows, macOS o Linux
- proveedor o Ollama/LM Studio

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://cherryai.com/docs/en/getting-started/quick-start/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Cherry Studio para mi objetivo y necesito pasos guiados. Lee https://cherryai.com/docs/en/getting-started/quick-start/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un modelo y prueba una pregunta sobre una nota ficticia en un espacio de trabajo.

**Qué comprobar:** Puedes comprobar el proveedor y la respuesta usada en la conversación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comparar respuestas de varios modelos
- Organizar una base documental de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comparar respuestas de varios modelos; Organizar una base documental de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una app multiproveedor; escoger Anthropic u OpenAI no la convierte en sesión de Claude Code o Codex

## Stack y modelos

- **Stack:** Instalador para Windows, macOS o Linux; proveedor o Ollama/LM Studio
- **Etiquetas:** `chatbot` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Jan](jan.md) | 45.7k | Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. |
| [LobeHub](lobehub.md) | 85.5k | Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. |

## Enlaces

- 🐙 GitHub: [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)
- 🌐 Web: <https://cherryai.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/CherryHQ/cherry-studio/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
