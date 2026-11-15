[🏠 Inicio](../README.md) › [🏠 Usar modelos y asistentes locales](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 Open WebUI

> Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 159k | NOASSERTION | Svelte | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

Da a tu equipo un chat privado con usuarios, documentos, búsqueda web, herramientas y modelos locales o en la nube.

## Por qué destaca

La UI de chat auto-hospedada más popular, muy completa y activa.

## Cómo funciona

Backend Python y frontend Svelte que se conectan a Ollama o a cualquier API OpenAI, con RAG integrado.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python o Docker según la instalación elegida, y un proveedor o motor de modelos.

1. Elige la instalación con paquete o contenedor que documenta el README.
2. Configura un backend, por ejemplo un motor local compatible o un proveedor remoto.
3. Prueba una conversación y confirma dónde se ejecuta el modelo antes de cargar documentos.

**Comando de entrada documentado:**

```shell
pip install open-webui
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/open-webui/open-webui/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Open WebUI para mi objetivo y necesito pasos guiados. Lee https://github.com/open-webui/open-webui/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- ChatGPT privado para tu empresa
- Chat con documentos internos
- Probar modelos locales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas un ChatGPT privado para tu equipo | solo quieres una app de escritorio individual; mira `jan` |

**Limitaciones:** La licencia exige mantener la marca Open WebUI en despliegues grandes.

## Stack y modelos

- **Stack:** Python, Svelte, Docker
- **Etiquetas:** `chatbot` `local` `rag` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [SearXNG](searxng.md) | 39.6k | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. |
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

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

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/open-webui/open-webui/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
