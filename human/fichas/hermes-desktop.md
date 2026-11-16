[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Workspaces privados y segundos cerebros

# 🏠 Hermes Desktop

> App de escritorio que envuelve al agente Hermes en una interfaz nativa.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.6k | MIT | TypeScript | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Aplicación de escritorio nativa mantenida por la comunidad (Hermes One, de fathah) para instalar, configurar y usar Hermes Agent de Nous Research. Licencia MIT; en desarrollo activo (v0.7.8), con funciones que pueden cambiar.

## ¿Qué hace?

Guía la instalación de Hermes Agent y la configuración de proveedores (OpenRouter, Anthropic, OpenAI, Gemini, xAI, Nous Portal, Qwen, MiniMax, Hugging Face, Groq y endpoints locales compatibles con OpenAI como LM Studio, Ollama o vLLM). Ofrece chat con streaming, 22 comandos de barra, sesiones con búsqueda de texto completo, perfiles aislados, 14 conjuntos de herramientas, memoria con proveedores como Mem0 o Honcho, editor de personalidad (SOUL.md), tareas cron con 15 destinos y 16 pasarelas de mensajería (Telegram, Discord, Slack, WhatsApp, Signal, Matrix, email, SMS y otras).

## ¿Cómo lo hace?

App Electron que usa el script oficial de instalación de Hermes y guarda los datos en `~/.hermes`, sustituyendo la gestión manual de la CLI. Se descarga desde hermesone.org o GitHub Releases; el instalador de Windows no está firmado y el .rpm de Fedora no está firmado con GPG ni se actualiza solo. En WSL el instalador puede bloquearse esperando sudo para Playwright.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [hermes-agent](hermes-agent.md) | Es su interfaz gráfica: instala y gestiona Hermes Agent. | Instala la app; ella instala Hermes Agent. No mezcles con una instalación manual distinta en `~/.hermes`. |
| [Ollama](ollama.md) | Endpoint local compatible con OpenAI soportado como proveedor. | Ollama en marcha; añádelo en la pantalla de proveedores. |
| [mem0](mem0.md) | Proveedor de memoria listado en la app. | Configura la clave o el servidor de Mem0 antes de activarlo en la sección de memoria. |
| [vLLM](vllm.md) | Endpoint local compatible con OpenAI soportado. | vLLM en un equipo con GPU; registra su URL como proveedor. |

**Notas:** El README sugiere conceder temporalmente sudo sin contraseña en WSL para instalar; revierte el cambio al terminar.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v0.7.8 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/fathah/hermes-desktop/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La interfaz no incluye créditos; el backend, modelo y servicios externos se presupuestan según ruta |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Proyecto en desarrollo activo; no hace falta aplicar el ejemplo de sudoers del README para explicar o elegir la ruta de instalación |
| Coste | El coste depende del proveedor o la ruta. La interfaz no incluye créditos; el backend, modelo y servicios externos se presupuestan según ruta |
| Equipo | Preparación según la ruta elegida. Instalador oficial del proyecto; backend Hermes local o remoto; proveedor o endpoint local |

Proyecto en desarrollo activo; no hace falta aplicar el ejemplo de sudoers del README para explicar o elegir la ruta de instalación

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador oficial del proyecto
- backend Hermes local o remoto
- proveedor o endpoint local

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/fathah/hermes-desktop/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Hermes Desktop para mi objetivo y necesito pasos guiados. Lee https://github.com/fathah/hermes-desktop/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un backend de prueba y confirma la dirección antes de iniciar un chat.

**Qué comprobar:** La interfaz muestra el backend y devuelve una respuesta del proveedor elegido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Usar Hermes desde una interfaz de escritorio
- Consultar una instancia remota de Hermes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Usar Hermes desde una interfaz de escritorio; Consultar una instancia remota de Hermes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Proyecto en desarrollo activo; no hace falta aplicar el ejemplo de sudoers del README para explicar o elegir la ruta de instalación

## Stack y modelos

- **Stack:** Instalador oficial del proyecto; backend Hermes local o remoto; proveedor o endpoint local
- **Etiquetas:** `agents` `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop)
- 🌐 Web: <https://hermesone.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/fathah/hermes-desktop/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
