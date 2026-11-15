[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 cognee

> Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 33.3k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

## Qué puedes hacer con él

Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños.

## Por qué destaca

Usos propuestos: Construir memoria de documentos; Recuperar contexto desde Claude Code o Codex.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| [mcp-neo4j](mcp-neo4j.md) | 989 | Servidores experimentales de Neo4j Labs para consultar grafos, memoria y recursos Aura desde clientes MCP. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Graphiti](graphiti.md) | 32.8k | Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes. |
| [mem0](mem0.md) | 69k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |
| [Letta](letta.md) | 25.4k | Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT). |

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
