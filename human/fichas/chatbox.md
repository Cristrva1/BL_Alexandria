[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 🏠 chatbox

> Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.3k | GPL-3.0 | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 52/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

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

## Ver similares

Grupo **Interfaces de chat con LLM**: chatbox ocupa la posición 8 de 8 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Open WebUI](open-webui.md) ⭐ recomendado | 74 | Si quieres la interfaz más completa para Ollama o APIs, multiusuario y con RAG. |
| 2 | [Cherry Studio](cherry-studio.md) | 72 | Si quieres un cliente de escritorio para muchos proveedores con asistentes predefinidos. |
| 3 | [LobeHub](lobehub.md) | 70 | Si quieres una interfaz moderna con plugins, agentes y despliegue sencillo. |
| 4 | [LibreChat](librechat.md) | 68 | Si necesitas un clon de ChatGPT multiusuario con muchos proveedores, agentes y control de acceso. |
| 5 | [Jan](jan.md) | 65 | Si prefieres una app de escritorio que funcione sin conexión con modelos locales. |
| 6 | [NextChat](nextchat.md) | 63 | Si quieres desplegar una interfaz ligera en Vercel con un clic. |
| 7 | [Text Generation WebUI](textgen.md) | 53 | Si quieres experimentar con muchos backends y formatos de modelos locales (GGUF, EXL2, Transformers). |
| 8 | **chatbox** (esta ficha) | 52 | Si quieres un cliente de escritorio y móvil sencillo para tus claves de API. |

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

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/chatboxai/chatbox.git
```

Comando copiado literalmente de el README (sección «Quick Setup»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

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
| [NextChat](nextchat.md) | 89k | Cliente de chat de IA ligero y multiplataforma (web, escritorio y móvil) para Claude, GPT, Gemini, DeepSeek y modelos autoalojados, con soporte MCP. |
| [LobeHub](lobehub.md) | 85.5k | Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. |

## Enlaces

- 🐙 GitHub: [chatboxai/chatbox](https://github.com/chatboxai/chatbox)
- 🌐 Web: <https://chatboxai.app?utm_medium=github>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/chatboxai/chatbox/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
