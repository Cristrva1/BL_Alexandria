[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 🏠 chatbox

> Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.3k | GPL-3.0 | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Cliente de escritorio para ChatGPT, Claude y otros LLM, en su edición comunitaria de código abierto (GPLv3) de chatboxai; el código se sincroniza con la versión Pro. Activo (v1.24.4).

## ¿Qué hace?

Ofrece chat con varios proveedores (OpenAI, Azure OpenAI, Claude, Gemini, Ollama y otros), generación de imágenes con DALL-E 3, Markdown, LaTeX y resaltado de código, atajos de teclado y respuestas en streaming. Guarda los datos en el dispositivo y se instala sin despliegue.

## ¿Cómo lo hace?

Aplicación Electron con interfaz React (procesos main, renderer y preload) y pruebas con Vitest. Se descarga para Windows 10+, macOS 11+ y Linux (AppImage), además de iOS y Android.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor soportado para usar modelos locales. | Ollama en marcha; selecciónalo en la configuración de Chatbox. |
| [litellm](litellm.md) | Un proxy compatible con OpenAI para varios proveedores con una sola clave (combinación por arquitectura). | LiteLLM primero; configura su URL como API compatible con OpenAI. |
| [LocalAI](localai.md) | Servidor local compatible con OpenAI como alternativa a Ollama (combinación por arquitectura). | Usa LocalAI u Ollama, no ambos. |

**Notas:** Alternativa (elige una): jan.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v1.24.4 (2026-11-12) · licencia declarada GPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/chatboxai/chatbox/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Community usa GPLv3; planes comerciales y proveedores tienen condiciones propias; Ollama local requiere recursos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No confundas la edición comunitaria con los servicios comerciales ni un proveedor Claude con Claude Code |
| Coste | El coste depende del proveedor o la ruta. Community usa GPLv3; planes comerciales y proveedores tienen condiciones propias; Ollama local requiere recursos |
| Equipo | Preparación según la ruta elegida. Instalador Community para tu sistema; proveedor o instancia Ollama |

No confundas la edición comunitaria con los servicios comerciales ni un proveedor Claude con Claude Code

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador Community para tu sistema
- proveedor o instancia Ollama

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/chatboxai/chatbox/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar chatbox para mi objetivo y necesito pasos guiados. Lee https://github.com/chatboxai/chatbox/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta un proveedor y guarda una conversación con una nota ficticia.

**Qué comprobar:** Puedes identificar el modelo y recuperar el chat.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Conversar con varios proveedores
- Probar un modelo local desde escritorio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Conversar con varios proveedores; Probar un modelo local desde escritorio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No confundas la edición comunitaria con los servicios comerciales ni un proveedor Claude con Claude Code

## Stack y modelos

- **Stack:** Instalador Community para tu sistema; proveedor o instancia Ollama
- **Etiquetas:** `chats` `assistant` `chatbot` `chatgpt` `claude` `claude-code` `copilot` `deepseek`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Jan](jan.md) | 45.7k | Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. |

## Enlaces

- 🐙 GitHub: [chatboxai/chatbox](https://github.com/chatboxai/chatbox)
- 🌐 Web: <https://chatboxai.app?utm_medium=github>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/chatboxai/chatbox/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
