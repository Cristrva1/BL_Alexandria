[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 mem0

> Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 69k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Capa de memoria para asistentes y agentes de IA de Mem0 («mem-zero»), de código abierto (Apache 2.0) con plataforma gestionada de pago. Muy activa; en abril de 2026 publicó un nuevo algoritmo de memoria y su evaluación es reproducible con un marco abierto.

## ¿Qué hace?

Recuerda preferencias y contexto a nivel de usuario, sesión y agente para personalizar respuestas. El algoritmo nuevo extrae en una sola pasada y solo añade (no sobrescribe), trata los hechos confirmados por el agente como de primera clase, enlaza entidades y combina recuperación semántica, BM25 y por entidades con razonamiento temporal. Sus cifras publicadas (92,5 en LoCoMo, 94,4 en LongMemEval) corresponden a la plataforma gestionada, que incluye componentes propietarios.

## ¿Cómo lo hace?

Se usa como biblioteca (`pip install mem0ai` o `npm install mem0ai`), como servidor autoalojado (`cd server && docker compose up -d`, en el puerto 3000, con autenticación activada por defecto) o en la nube. Tiene CLI (`@mem0/cli` o `mem0-cli`) y SDK multiplataforma; admite varios LLM y bases vectoriales, entre ellos Ollama y Qdrant según su documentación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph](langgraph.md) | Guía oficial para construir un bot con LangGraph y memoria de Mem0. | Configura Mem0 (biblioteca o servidor) y añade sus llamadas al grafo de LangGraph. |
| [crewAI](crewai.md) | Integración documentada para dar memoria a equipos de agentes de CrewAI. | Mem0 configurado primero; activa la memoria en la definición del crew. |
| [Qdrant](qdrant.md) | Base vectorial documentada como almacén de Mem0 en código abierto. | Qdrant primero; la dimensión de la colección debe coincidir con el modelo de embeddings. |
| [Hermes Desktop](hermes-desktop.md) | Hermes Desktop lista Mem0 entre sus proveedores de memoria. | Clave o servidor de Mem0 listo antes de activarlo en la app. |

**Notas:** Alternativas (elige una): letta, cognee, supermemory. La migración de la v2 a la v3 de código abierto tiene guía propia.

Estado en GitHub: activo · último push 2026-11-06 · última versión publicada ts-v3.3.1 (2026-09-25) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mem0ai/mem0/blob/main/README.md) · [2](https://docs.mem0.ai/integrations/langgraph) · [3](https://docs.mem0.ai/integrations/crewai) · [4](https://docs.mem0.ai/components/vectordbs/dbs/qdrant)</sub>

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

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Letta](letta.md) | 3.8k | Harness de agentes con estado (Letta Code, antes MemGPT): memoria, identidad y skills que el propio agente reescribe con el tiempo. |
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
