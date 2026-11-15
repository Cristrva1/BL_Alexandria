[🏠 Inicio](../README.md) › [🏠 Usar modelos y asistentes locales](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 Ollama

> La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 187k | MIT | Go | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Un comando para bajar y ejecutar modelos como Qwen, Gemma, DeepSeek o gpt-oss. Casi todas las apps de IA local lo soportan.

## Por qué destaca

Experiencia muy simple y el ecosistema de integraciones más amplio en IA local.

## Cómo funciona

Usa llama.cpp por debajo, gestiona modelos cuantizados y sirve una API REST local.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Equipo compatible con el modelo elegido y espacio para sus pesos.

1. Instala el motor de Ollama para tu sistema desde la fuente oficial.
2. Elige un modelo que quepa en la memoria del equipo y sigue su descarga y primer chat.
3. Conecta una interfaz como Open WebUI solo cuando hayas comprobado la inferencia local del motor.

[Instrucciones originales de instalación](https://github.com/ollama/ollama/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Ollama para mi objetivo y necesito pasos guiados. Lee https://github.com/ollama/ollama/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Usar modelos locales en n8n
- Backend local para Open WebUI
- Programar con modelos privados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres modelos locales funcionando en minutos | necesitas servir a muchos usuarios con GPU; mira `vllm` |

## Stack y modelos

- **Stack:** Go, C++
- **Etiquetas:** `inference` `local` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open WebUI](open-webui.md) | 159k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [AnythingLLM](anything-llm.md) | 68.3k | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [llama.cpp](llama-cpp.md) | 135k | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. |
| [LocalAI](localai.md) | 50.4k | Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria. |
| [llamafile](llamafile.md) | 26.6k | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. |

## Enlaces

- 🐙 GitHub: [ollama/ollama](https://github.com/ollama/ollama)
- 🌐 Web: <https://ollama.com>
- 🧪 Receta: [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md)
- 🧪 Receta: [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/ollama/ollama/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
