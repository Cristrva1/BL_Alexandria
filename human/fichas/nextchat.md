[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 🖥️ NextChat

> Cliente de chat de IA ligero y multiplataforma (web, escritorio y móvil) para Claude, GPT, Gemini, DeepSeek y modelos autoalojados, con soporte MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 89k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación sencilla; requiere clave de API

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Cliente de chat de código abierto (MIT), antes ChatGPT-Next-Web, muy popular. Su organización ofrece además un servicio SaaS de pago por uso; el repositorio sigue siendo el cliente autoalojable.

## ¿Qué hace?

Proporciona una interfaz rápida para conversar con varios proveedores, con plantillas de prompts (máscaras), compresión de historial, exportación, PWA y apps de escritorio. Admite modelos autoalojados compatibles (RWKV-Runner, LocalAI) y servidores MCP.

## ¿Cómo lo hace?

Escrito en TypeScript con Next.js; se despliega en Vercel con un clic, con Docker (`docker run -d -p 3000:3000 ...` y variables como `OPENAI_API_KEY` y `CODE`) o como app de escritorio. Los datos de chat se guardan localmente en el navegador.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LocalAI](localai.md) | El README declara compatibilidad con despliegues de LocalAI como modelo autoalojado. | LocalAI en marcha; después configura su URL como endpoint compatible con OpenAI. |
| [litellm](litellm.md) | Un proxy LiteLLM con API compatible con OpenAI permite usar desde NextChat proveedores que no soporta directamente (combinación por arquitectura). | LiteLLM primero; después pon su URL como base de la API en NextChat. |
| [FastMCP](fastmcp.md) | NextChat soporta servidores MCP; FastMCP sirve para escribir servidores propios que conectar (combinación por arquitectura). | Escribe el servidor con FastMCP; después regístralo en la configuración MCP de NextChat. |

**Notas:** Alternativas (elige una): lobehub, chatbox. Protege el despliegue con la variable CODE si es público.

Estado en GitHub: activo · último push 2026-10-20 · última versión publicada v2.16.1 (2025-07-29) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ChatGPTNextWeb/NextChat/blob/main/README.md)</sub>

## Ver similares

Grupo **Interfaces de chat con LLM**: NextChat ocupa la posición 6 de 8 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Open WebUI](open-webui.md) ⭐ recomendado | 74 | Si quieres la interfaz más completa para Ollama o APIs, multiusuario y con RAG. |
| 2 | [Cherry Studio](cherry-studio.md) | 72 | Si quieres un cliente de escritorio para muchos proveedores con asistentes predefinidos. |
| 3 | [LobeHub](lobehub.md) | 70 | Si quieres una interfaz moderna con plugins, agentes y despliegue sencillo. |
| 4 | [LibreChat](librechat.md) | 69 | Si necesitas un clon de ChatGPT multiusuario con muchos proveedores, agentes y control de acceso. |
| 5 | [Jan](jan.md) | 66 | Si prefieres una app de escritorio que funcione sin conexión con modelos locales. |
| 6 | **NextChat** (esta ficha) | 64 | Si quieres desplegar una interfaz ligera en Vercel con un clic. |
| 7 | [chatbox](chatbox.md) | 52 | Si quieres un cliente de escritorio y móvil sencillo para tus claves de API. |
| 8 | [Text Generation WebUI](textgen.md) | 51 | Si quieres experimentar con muchos backends y formatos de modelos locales (GGUF, EXL2, Transformers). |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/ChatGPTNextWeb/NextChat/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar NextChat para mi objetivo y necesito pasos guiados. Lee https://github.com/ChatGPTNextWeb/NextChat/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega NextChat con Docker o Vercel usando tu clave de API y abre un chat..

**Qué comprobar:** El chat responde con el modelo configurado y el historial queda en el navegador..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- desplegar un chat privado con tu propia clave para un equipo pequeño
- usar un modelo autoalojado compatible con OpenAI desde una interfaz web ligera

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: desplegar un chat privado con tu propia clave para un equipo pequeño; usar un modelo autoalojado compatible con OpenAI desde una interfaz web ligera | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, docker-compose.yml, package.json
- **Etiquetas:** `chatbot` `typescript` `app` `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LobeHub](lobehub.md) | 85.5k | Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. |
| [chatbox](chatbox.md) | 42.3k | Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común. |

## Enlaces

- 🐙 GitHub: [ChatGPTNextWeb/NextChat](https://github.com/ChatGPTNextWeb/NextChat)
- 🌐 Web: <https://nextchat.club>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ChatGPTNextWeb/NextChat/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
