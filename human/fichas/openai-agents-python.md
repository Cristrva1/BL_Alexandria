[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 OpenAI Agents SDK

> SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.7k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

Define agentes con instrucciones y herramientas, pasa el control entre ellos y añade validaciones. Funciona con modelos de OpenAI y otros compatibles.

## Por qué destaca

Pocas abstracciones, buena documentación y trazas listas en el panel de OpenAI.

## Cómo funciona

Un bucle ejecuta al agente, llama herramientas o transfiere a otro agente, y registra cada paso como traza.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install openai-agents
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/openai/openai-agents-python/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenAI Agents SDK para mi objetivo y necesito pasos guiados. Lee https://github.com/openai/openai-agents-python/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Agentes de soporte con traspasos
- Flujos con guardrails de entrada y salida
- Agentes de voz en tiempo real

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas OpenAI y quieres agentes multiagente con poco código | necesitas control de estado avanzado; mira `langgraph` |

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [openai-python](openai-python.md) | 32.2k | SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API. |
| [FastMCP](fastmcp.md) | 28.5k | La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pydantic AI](pydantic-ai.md) | 21.2k | Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. |
| [LangGraph](langgraph.md) | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [smolagents](smolagents.md) | 30.4k | Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. |
| [Deep Agents](deepagents.md) | 31.3k | Arnés de agentes de LangChain listo para usar, con planificación, subagentes y sistema de archivos. |
| [Agent Development Kit (ADK)](adk-python.md) | 22.2k | Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. |

## Enlaces

- 🐙 GitHub: [openai/openai-agents-python](https://github.com/openai/openai-agents-python)
- 🌐 Web: <https://openai.github.io/openai-agents-python/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/openai/openai-agents-python/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
