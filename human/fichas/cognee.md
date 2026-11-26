[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 cognee

> Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 33.3k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de memoria de IA de código abierto (Apache 2.0) de topoteretes que da a los agentes memoria persistente a largo plazo, con artículo de investigación propio. Activa (v1.6.8) y con servicio gestionado Cognee Cloud.

## ¿Qué hace?

Convierte documentos, código y conversaciones en un grafo de conocimiento autoalojado que los agentes pueden consultar y mejorar. Casos de uso: un «cerebro de empresa» que une documentación, tickets, código y trabajo de agentes; memoria entre ejecuciones con decisiones y reglas aprendidas; y memoria estructurada con modelos de datos y ontologías propias. Funciona en local sin clave de API usando modelos pequeños en CPU.

## ¿Cómo lo hace?

Biblioteca Python 3.10–3.14 (`uv pip install "cognee[gliner]"`): sin clave de LLM extrae el grafo con un modelo local (GLiNER) y las etapas que requieren LLM se saltan; con clave usa OpenAI por defecto u otro proveedor. Ofrece plugins de memoria para Claude Code, Codex y OpenClaw, servidor MCP, SDK de TypeScript y Rust, API REST (imagen Docker en el puerto 8000, multiinquilino con autenticación por defecto) y una interfaz local con `cognee-cli -ui`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin oficial de memoria (`claude plugin install cognee-memory@cognee`). | Instala Cognee y configura el LLM; luego añade el marketplace y el plugin. |
| [Codex CLI](codex.md) | Plugin oficial para Codex. | Activa los hooks de Codex primero; después añade el marketplace y el plugin. |
| [OpenClaw](openclaw.md) | Plugin oficial `@cognee/cognee-openclaw`. | OpenClaw instalado; añade el plugin desde npm. |
| [Neo4j MCP (oficial)](neo4j-mcp.md) | Combinación recíproca: Neo4j MCP (oficial) lo enlaza como «Cognee documenta Neo4j como almacén de grafos; el servidor MCP da al agente consultas Cypher directas sobre lo que Cognee construye. (combinación por arquitectura)». | Orden indicado desde Neo4j MCP (oficial): Configura Cognee con Neo4j y luego añade el servidor MCP. |

**Notas:** Alternativas (elige una): graphiti, mem0, graphrag, letta. En la API, `ENABLE_BACKEND_ACCESS_CONTROL=false` solo para uso local de un usuario.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.6.8 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/topoteretes/cognee/blob/main/README.md)</sub>

## Ver similares

Grupo **Capas de memoria para apps y agentes de IA**: cognee ocupa la posición 2 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [mem0](mem0.md) ⭐ recomendado | 77 | Si tu app necesita memoria de usuario a largo plazo con una API sencilla. |
| 2 | **cognee** (esta ficha) | 68 | Si quieres convertir documentos en un grafo de conocimiento consultable por agentes. |
| 3 | [Graphiti](graphiti.md) | 62 | Si necesitas un grafo temporal que registre cómo cambian los hechos en el tiempo. |
| 4 | [supermemory](supermemory.md) | 62 | Si buscas una API de memoria y contexto rápida orientada a productos. |
| 5 | [Letta](letta.md) | 57 | Si quieres agentes con estado gestionados por un servidor (antes MemGPT). |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. GLiNER y embeddings locales cubren la ruta básica; generación, visión, transcripción o Cloud pueden añadir costes |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Los plugins de los dos agentes están documentados; MCP usa stdio o HTTP; no asumas que sampling permite usar cualquier plan del cliente |
| Coste | El coste depende del proveedor o la ruta. GLiNER y embeddings locales cubren la ruta básica; generación, visión, transcripción o Cloud pueden añadir costes |
| Equipo | Preparación según la ruta elegida. Python 3.10–3.14; modelos locales iniciales; plugins opcionales |

Los plugins de los dos agentes están documentados; MCP usa stdio o HTTP; no asumas que sampling permite usar cualquier plan del cliente

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10–3.14
- modelos locales iniciales
- plugins opcionales

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv pip install "cognee[gliner]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/topoteretes/cognee/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar cognee para mi objetivo y necesito pasos guiados. Lee https://github.com/topoteretes/cognee/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Guarda un hecho ficticio con remember y recupéralo con recall sin configurar una clave LLM.

**Qué comprobar:** Se devuelve el texto de origen y no una respuesta inventada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir memoria de documentos
- Recuperar contexto desde Claude Code o Codex

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir memoria de documentos; Recuperar contexto desde Claude Code o Codex | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los plugins de los dos agentes están documentados; MCP usa stdio o HTTP; no asumas que sampling permite usar cualquier plan del cliente

## Stack y modelos

- **Stack:** Python 3.10–3.14; modelos locales iniciales; plugins opcionales
- **Etiquetas:** `memory` `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Graphiti](graphiti.md) | 32.8k | Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes. |
| [mem0](mem0.md) | 69k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |
| [Letta](letta.md) | 3.8k | Harness de agentes con estado (Letta Code, antes MemGPT): memoria, identidad y skills que el propio agente reescribe con el tiempo. |

## Enlaces

- 🐙 GitHub: [topoteretes/cognee](https://github.com/topoteretes/cognee)
- 🌐 Web: <https://www.cognee.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/topoteretes/cognee/blob/main/README.md)
- [Fuente 2](https://github.com/topoteretes/cognee/blob/main/cognee-mcp/README.md)
- [Fuente 3](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
