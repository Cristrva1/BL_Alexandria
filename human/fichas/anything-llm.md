[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Workspaces privados y segundos cerebros

# 🏠 AnythingLLM

> App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 68.3k | MIT | JavaScript | 2026-11-10 |

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

Organiza documentos en espacios de trabajo, crea RAG sin configurar nada y añade agentes con herramientas. Escritorio o Docker multiusuario.

## Por qué destaca

La forma más fácil de tener RAG privado con agentes.

## Cómo funciona

Incluye base vectorial, embeddings y conectores a LLM; cada workspace tiene su contexto y agentes.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AnythingLLM para mi objetivo y necesito pasos guiados. Lee https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Chat con los documentos de la empresa
- Agentes con búsqueda web
- IA privada en un portátil

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres RAG privado sin programar | necesitas un pipeline de RAG a medida; mira `llama-index` |

## Stack y modelos

- **Stack:** JavaScript, Node.js, React
- **Etiquetas:** `rag` `agents` `local` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open WebUI](open-webui.md) | 159k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |
| [Khoj](khoj.md) | 38.1k | Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones. |
| [PrivateGPT](private-gpt.md) | 57.6k | Capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP. |
| [onyx](onyx.md) | 33.4k | Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso. |

## Enlaces

- 🐙 GitHub: [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)
- 🌐 Web: <https://anythingllm.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
