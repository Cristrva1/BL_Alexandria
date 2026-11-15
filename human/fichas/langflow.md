[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Builders visuales y plataformas de agentes

# 🔗 langflow

> Constructor visual de flujos LLM/agentes construido sobre LangChain.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 157k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

Permite arrastrar y conectar componentes en un lienzo y exportarlos como API o código Python.

## Por qué destaca

Une la potencia del ecosistema LangChain con una interfaz visual, muy valorado para prototipar sin escribir todo el código. Al generar LangChain real por debajo, lo que construyes en visual es portable a código.

## Cómo funciona

Cada nodo del lienzo envuelve un componente LangChain (LLM, retriever, tool, prompt); el flujo se ejecuta como un grafo y se expone vía API. Corre sobre Python con frontend web (React).

## Instalación rápida

`pip install langflow` o vía Docker. Requiere un proveedor de LLM configurado por entorno para los componentes que lo usen.

## Casos de uso

- Iterar componentes de agente sin código
- Prototipar pipelines RAG
- Enseñar LangChain a perfiles no técnicos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| prefieres construir en visual sobre LangChain | quieres todo en código o no usas LangChain |

## Stack y modelos

- **Stack:** Python, React, Docker
- **Modelos / API:** Múltiples; agnóstico vía LangChain.
- **Etiquetas:** `automation` `agents` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 149k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [dify](dify.md) | 161k | Plataforma integral para construir apps de IA con backend y UI listos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Sim](sim.md) | 30.1k | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. |
| [AutoGPT](autogpt.md) | 188k | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. |

## Enlaces

- 🐙 GitHub: [langflow-ai/langflow](https://github.com/langflow-ai/langflow)
- 🌐 Web: <http://www.langflow.org>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
