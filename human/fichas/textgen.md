[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 Text Generation WebUI

> App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47.7k | AGPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Aplicación de escritorio para LLM locales, de código abierto (AGPL-3.0) y sin telemetría, de oobabooga (antes text-generation-webui). Madura y con versiones regulares (v4.9).

## ¿Qué hace?

Ofrece chat en modos instruct, chat-instruct y chat con personajes, visión multimodal, adjuntos (texto, PDF, docx), edición y ramas de conversación, y un cuaderno de generación libre. Permite llamadas a herramientas (cada herramienta es un archivo .py, incluidas búsqueda web y lectura de páginas) y servidores MCP, entrenamiento de LoRA y generación de imágenes con modelos diffusers. Expone una API compatible con OpenAI y Anthropic para usarla como reemplazo local.

## ¿Cómo lo hace?

Aplicación Python con varios backends: llama.cpp, ik_llama.cpp, Transformers y ExLlamaV3, con plantillas Jinja2 para formatear prompts. Las compilaciones portátiles para Linux, Windows y macOS (CUDA, Vulkan, ROCm o CPU) incluyen todas las dependencias y usan modelos GGUF; los backends extra, el entrenamiento y la generación de imágenes requieren la instalación completa.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LibreChat](librechat.md) | Usar la API compatible con OpenAI de TextGen como endpoint personalizado en un chat multiusuario (combinación por arquitectura). | Activa la API en TextGen; regístrala en `librechat.yaml`. |
| [llmfit](llmfit.md) | Saber qué modelo y cuantización caben antes de descargar (combinación por arquitectura). | Ejecuta llmfit primero. |
| [Unsloth](unsloth.md) | Afinar modelos con más eficiencia fuera de TextGen y cargar el resultado en él (combinación por arquitectura). | Entrena y exporta el adaptador o GGUF con Unsloth; luego cárgalo en TextGen. |
| [SillyTavern](sillytavern.md) | Combinación recíproca: SillyTavern lo enlaza como «Text generation web UI (Ooba) es uno de los backends de texto que SillyTavern soporta». | Orden indicado desde SillyTavern: Arranca textgen con su API habilitada; después conéctalo desde SillyTavern. |

**Notas:** Alternativas (elige una): jan, open-webui.

Estado en GitHub: activo · último push 2026-08-17 · última versión publicada v4.9 (2026-05-20) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/oobabooga/textgen/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige API de proveedor; modelos, memoria y disco son recursos y licencias propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Antes conocida por rutas text-generation-webui; usa la distribución que corresponda a tu hardware y distingue API de inferencia de token de autenticación |
| Coste | Sin pago a un modelo en la ruta básica. No exige API de proveedor; modelos, memoria y disco son recursos y licencias propios |
| Equipo | Preparación según la ruta elegida. Distribución portable apropiada a tu GPU o CPU; modelo GGUF |

Antes conocida por rutas text-generation-webui; usa la distribución que corresponda a tu hardware y distingue API de inferencia de token de autenticación

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Distribución portable apropiada a tu GPU o CPU
- modelo GGUF

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/oobabooga/textgen/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Text Generation WebUI para mi objetivo y necesito pasos guiados. Lee https://github.com/oobabooga/textgen/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga un modelo pequeño en la app y revisa texto generado y consumo de memoria.

**Qué comprobar:** Puedes identificar backend, modelo y memoria utilizada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar modelos GGUF sin una API remota
- Servir un endpoint local para otra app

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar modelos GGUF sin una API remota; Servir un endpoint local para otra app | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Antes conocida por rutas text-generation-webui; usa la distribución que corresponda a tu hardware y distingue API de inferencia de token de autenticación

## Stack y modelos

- **Stack:** Distribución portable apropiada a tu GPU o CPU; modelo GGUF
- **Etiquetas:** `chatbot` `local` `inference` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Jan](jan.md) | 45.7k | Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. |
| [Open WebUI](open-webui.md) | 159k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |

## Enlaces

- 🐙 GitHub: [oobabooga/textgen](https://github.com/oobabooga/textgen)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/oobabooga/textgen/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
