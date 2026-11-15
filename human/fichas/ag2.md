[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🤝 ag2

> Framework maduro para sistemas multiagente con patrones de colaboración (heredero directo de AutoGen).

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 5.1k | Apache-2.0 | Python | 2026-11-09 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Modela conversaciones entre varios agentes que se delegan tareas hasta resolver un objetivo.

## Por qué destaca

Uno de los frameworks multiagente de referencia, con amplia adopción y comunidad activa heredada de AutoGen. Es totalmente open-source y aporta patrones de conversación (secuencial, anidado, grupo) ya probados en producción.

## Cómo funciona

Define agentes conversacionales (asistente, ejecutor de código, usuario) que intercambian mensajes según patrones predefinidos; corre sobre Python y se conecta a APIs de LLM vía variables de entorno.

## Instalación rápida

`pip install ag2` (o `pyautogen` para el nombre legacy). Requiere una clave de API de LLM (OpenAI, Anthropic u otro) configurada por entorno.

## Casos de uso

- Equipos de agentes que se reparten tareas
- Flujos de decisión estructurados
- Agentes que escriben y ejecutan código en bucle

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| construyes multiagente serio en Python | te basta un agente único o quieres orquestación visual |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** OpenAI, Anthropic, Gemini, locales (Ollama); agnóstico vía variables de entorno.
- **Etiquetas:** `automation` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 149k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AutoGen](autogen.md) | 61.8k | Framework de Microsoft para conversaciones entre agentes, hoy en modo mantenimiento. |

## Enlaces

- 🐙 GitHub: [ag2ai/ag2](https://github.com/ag2ai/ag2)
- 🌐 Web: <https://ag2.ai>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
