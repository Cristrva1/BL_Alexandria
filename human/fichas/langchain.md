[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🦜 langchain

> Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 150k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Ofrece abstracciones y conectores para casi cualquier modelo, base de datos vectorial y fuente de datos.

## Por qué destaca

Estándar de facto del ecosistema LLM, con la comunidad e integraciones más grandes del sector. Su valor está en future-proofing: cambiar de modelo o vector store suele ser mover un parámetro, no reescribir código.

## Cómo funciona

Encadena componentes (prompts, modelos, retrievers, tools) en pipelines o agentes; disponible en Python y JS/TS, con LangGraph para grafos cíclicos con estado.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
uv add langchain
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/langchain-ai/langchain/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar langchain para mi objetivo y necesito pasos guiados. Lee https://github.com/langchain-ai/langchain/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Orquestar LLM + herramientas + memoria
- Base de casi cualquier app de IA
- RAG sobre documentos propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres la base estándar con máximas integraciones | prefieres mínima abstracción o un solo proveedor sin cambiar |

## Stack y modelos

- **Stack:** Python/JS/TS
- **Etiquetas:** `agents` `automation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langflow](langflow.md) | 157k | Constructor visual de flujos LLM/agentes construido sobre LangChain. |
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [Haystack](haystack.md) | 27k | Framework de deepset para pipelines de RAG y agentes listos para producción. |
| [Semantic Kernel](semantic-kernel.md) | 28.8k | SDK de Microsoft para integrar LLM en apps de C#, Python y Java con plugins y planificación. |

## Enlaces

- 🐙 GitHub: [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- 🌐 Web: <https://docs.langchain.com/langchain/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/langchain-ai/langchain/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
