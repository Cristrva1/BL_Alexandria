[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🦜 langchain

> Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 150k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Framework (MIT) de LangChain Inc. para construir agentes y aplicaciones con LLM encadenando componentes intercambiables e integraciones de terceros. Es uno de los proyectos más populares del ecosistema y está en desarrollo activo (langchain-core 1.8.1).

## ¿Qué hace?

Ofrece una interfaz estándar para modelos, embeddings, almacenes vectoriales, cargadores y herramientas, de modo que se puede cambiar de proveedor sin reescribir la aplicación (por ejemplo, `init_chat_model("openai:...")`). Incluye agentes con patrones habituales. Para orquestación avanzada remite a LangGraph y, para empezar rápido, a Deep Agents.

## ¿Cómo lo hace?

Paquete Python (`uv add langchain`) con paquetes de integración por proveedor y equivalente en JS (LangChain.js). La observabilidad y el despliegue se resuelven con LangSmith (comercial) o con herramientas de terceros.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph](langgraph.md) | Orquestación con estado del mismo equipo cuando el agente necesita control fino. | Añade langgraph cuando los agentes de LangChain se queden cortos. |
| [langfuse](langfuse.md) | Trazas y evaluación de código abierto con la integración oficial de Langfuse. | Configura el callback de Langfuse en las cadenas o agentes. |
| [Qdrant](qdrant.md) | Almacén vectorial con integración oficial (`langchain-qdrant`). | Qdrant en marcha primero; luego el paquete de integración. |
| [Ollama](ollama.md) | Modelos locales con el proveedor oficial (`langchain-ollama`). | Ollama con el modelo descargado antes de configurar el proveedor. |

**Notas:** Alternativas (elige una): llama-index, haystack. Se quitaron langflow y litellm: no son necesarias y el README no las documenta.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada langchain-core==1.8.1 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/langchain-ai/langchain/blob/master/README.md) · [2](https://langfuse.com/integrations/frameworks/langchain) · [3](https://docs.langchain.com/oss/python/integrations/vectorstores/qdrant) · [4](https://docs.langchain.com/oss/python/integrations/providers/ollama)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Pagas el proveedor o el hardware local; LangSmith es opcional y tiene condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Instala la integración del modelo además del paquete base; compatibilidad con Anthropic API no equivale a Claude Code |
| Coste | El coste depende del proveedor o la ruta. Pagas el proveedor o el hardware local; LangSmith es opcional y tiene condiciones propias |
| Equipo | Preparación según la ruta elegida. Python y uv; proveedor o modelo local |

Instala la integración del modelo además del paquete base; compatibilidad con Anthropic API no equivale a Claude Code

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- proveedor o modelo local

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv add langchain
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/langchain-ai/langchain/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar langchain para mi objetivo y necesito pasos guiados. Lee https://github.com/langchain-ai/langchain/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pregunta por existencias a una herramienta con tres productos ficticios.

**Qué comprobar:** La respuesta coincide con los datos y muestra la llamada a la herramienta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar un catálogo de prueba
- Responder sobre documentos propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar un catálogo de prueba; Responder sobre documentos propios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Instala la integración del modelo además del paquete base; compatibilidad con Anthropic API no equivale a Claude Code

## Stack y modelos

- **Stack:** Python y uv; proveedor o modelo local
- **Etiquetas:** `agents` `automation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [Haystack](haystack.md) | 27k | Framework de deepset para pipelines de RAG y agentes listos para producción. |

## Enlaces

- 🐙 GitHub: [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- 🌐 Web: <https://docs.langchain.com/langchain/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langchain-ai/langchain/blob/master/README.md)
- [Fuente 2](https://docs.langchain.com/oss/python/integrations/chat/ollama)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
