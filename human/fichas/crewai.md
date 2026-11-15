[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 👥 crewAI

> Framework para orquestar "crews" de agentes con roles y tareas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 60.9k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

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

Cada agente recibe un rol y objetivo, y el equipo coopera o se reparte el trabajo de forma secuencial o jerárquica.

## Por qué destaca

Muy popular por su curva de aprendizaje suave; es de las formas más rápidas de montar un equipo de agentes funcional. Es independiente de LangChain y aporta un modelo mental claro (agentes, tareas, crew) que se lee casi como prosa.

## Cómo funciona

Declaras agentes (rol, meta, herramientas) y tareas, y CrewAI orquesta su ejecución secuencial o jerárquica; está escrito en Python y delega el LLM al proveedor que configures.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/crewAIInc/crewAI/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar crewAI para mi objetivo y necesito pasos guiados. Lee https://github.com/crewAIInc/crewAI/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Avanzar rápido en flujos de agentes
- Prototipos colaborativos
- Pipelines de research/redacción repartidos por rol

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres velocidad y un modelo mental simple de "equipo" | necesitas control de bajo nivel o orquestación muy custom |

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `automation` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [mem0](mem0.md) | 69k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AutoGen](autogen.md) | 61.8k | Framework de Microsoft para conversaciones entre agentes, hoy en modo mantenimiento. |
| [LangGraph](langgraph.md) | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [Agno](agno.md) | 43.2k | Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente. |
| [MetaGPT](metagpt.md) | 71.3k | Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo. |

## Enlaces

- 🐙 GitHub: [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
- 🌐 Web: <https://crewai.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/crewAIInc/crewAI/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
