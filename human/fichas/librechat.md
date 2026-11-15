[🏠 Inicio](../README.md) › [🏠 Usar modelos y asistentes locales](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 LibreChat

> Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47.1k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Puedes elegir la ruta local documentada o configurar un proveedor remoto; la ruta remota puede requerir API key o acceso propio. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | El coste depende del proveedor o la ruta. La inferencia local consume recursos de tu equipo. Los proveedores remotos y servicios del cliente tienen sus propios planes y tarifas. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Une OpenAI, Anthropic, Google, Azure, OpenRouter y modelos locales con agentes, artifacts, búsqueda y control de usuarios.

## Por qué destaca

La mejor opción multi-proveedor con autenticación empresarial y agentes.

## Cómo funciona

App MERN (MongoDB, Express, React, Node) con conectores a cada proveedor y un constructor de agentes.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/LibreChat-AI/LibreChat/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LibreChat para mi objetivo y necesito pasos guiados. Lee https://github.com/LibreChat-AI/LibreChat/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Un chat con todos los modelos para la empresa
- Agentes con MCP para el equipo
- Controlar costos por usuario

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres todos los proveedores en un chat con SSO | usas sobre todo modelos locales; mira `open-webui` |

## Stack y modelos

- **Stack:** TypeScript, React, Node.js, MongoDB
- **Etiquetas:** `chatbot` `agents` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open WebUI](open-webui.md) | 159k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |
| [LobeHub](lobehub.md) | 85.5k | Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. |

## Enlaces

- 🐙 GitHub: [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat)
- 🌐 Web: <https://librechat.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/LibreChat-AI/LibreChat/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
