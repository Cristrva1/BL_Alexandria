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
| API de IA | Depende de la ruta elegida. La plataforma y el SDK abierto tienen rutas distintas; Ollama sirve para LLM local, pero el ejemplo conserva OpenAI para embeddings si no los cambias |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelos locales documentados. Las skills enseñan a integrar Mem0; no incluyen el servicio ni ejecutan gratis la memoria de tu aplicación |
| Coste | El coste depende del proveedor o la ruta. La plataforma y el SDK abierto tienen rutas distintas; Ollama sirve para LLM local, pero el ejemplo conserva OpenAI para embeddings si no los cambias |
| Equipo | Preparación según la ruta elegida. Python; LLM; embeddings; almacén; identificador ficticio de usuario |

Las skills enseñan a integrar Mem0; no incluyen el servicio ni ejecutan gratis la memoria de tu aplicación

## Qué puedes hacer con él

Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental.

## Por qué destaca

Usos propuestos: Recordar preferencias de atención; Mantener contexto de una app entre conversaciones.

## Cómo funciona

Las skills enseñan a integrar Mem0; no incluyen el servicio ni ejecutan gratis la memoria de tu aplicación

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- LLM
- embeddings
- almacén
- identificador ficticio de usuario

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install mem0ai
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mem0ai/mem0/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mem0 para mi objetivo y necesito pasos guiados. Lee https://github.com/mem0ai/mem0/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Guarda dos preferencias de un usuario ficticio y consulta una de ellas por su identificador.

**Qué comprobar:** La búsqueda devuelve la preferencia del usuario correcto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Recordar preferencias de atención
- Mantener contexto de una app entre conversaciones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Recordar preferencias de atención; Mantener contexto de una app entre conversaciones | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las skills enseñan a integrar Mem0; no incluyen el servicio ni ejecutan gratis la memoria de tu aplicación

## Stack y modelos

- **Stack:** Python; LLM; embeddings; almacén; identificador ficticio de usuario
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

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mem0ai/mem0/blob/main/README.md)
- [Fuente 2](https://docs.mem0.ai/components/llms/models/ollama)
- [Fuente 3](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
