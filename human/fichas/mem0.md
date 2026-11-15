[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 mem0

> Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 69k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

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

Resuelve el "amnesia" del LLM: el agente conserva preferencias y hechos entre sesiones sin reenviar todo el historial.

## Por qué destaca

Es uno de los proyectos de memoria de agentes más adoptados, con SDK estable en Python y TS e integraciones amplias en el ecosistema de frameworks (LangChain, CrewAI, etc.). Su enfoque de extracción+actualización incremental de hechos evita duplicados y desactualizaciones.

## Cómo funciona

Combina extracción de hechos vía LLM con almacenamiento en vector DBs (Qdrant, Chroma, etc.) para indexar y consultar memorias relevantes por similitud, actualizando o borrando recuerdos contradictorios en lugar de solo acumularlos.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install mem0ai
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/mem0ai/mem0/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mem0 para mi objetivo y necesito pasos guiados. Lee https://github.com/mem0ai/mem0/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Recordar preferencias del usuario entre sesiones
- Memoria long-term para agentes
- Personalización acumulativa sin inflar el prompt

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres memoria estándar lista con integraciones amplias | necesitas todo local sin llamadas a API (mempalace) o control total del almacenamiento |

## Stack y modelos

- **Stack:** Python/TypeScript, vector DBs (Qdrant, Chroma, pgvector)
- **Etiquetas:** `memory` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [crewAI](crewai.md) | 60.9k | Framework para orquestar "crews" de agentes con roles y tareas. |
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [agentmemory](agentmemory.md) | 30.4k | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Letta](letta.md) | 25.4k | Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT). |
| [cognee](cognee.md) | 33.3k | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. |
| [supermemory](supermemory.md) | 31.6k | Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local. |

## Enlaces

- 🐙 GitHub: [mem0ai/mem0](https://github.com/mem0ai/mem0)
- 🌐 Web: <https://mem0.ai>
- 🧪 Receta: [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/mem0ai/mem0/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
