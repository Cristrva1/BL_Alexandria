[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 Graphiti

> Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 32.8k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El valor por defecto usa OpenAI; admite servidores locales compatibles; base de grafos y embeddings también consumen recursos |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Su MCP es una referencia experimental sin autenticación ni autorización: úsalo aislado para pruebas, no como despliegue público de producción |
| Coste | El coste depende del proveedor o la ruta. El valor por defecto usa OpenAI; admite servidores locales compatibles; base de grafos y embeddings también consumen recursos |
| Equipo | Preparación según la ruta elegida. Python; Neo4j o FalkorDB; LLM y embeddings configurados |

Su MCP es una referencia experimental sin autenticación ni autorización: úsalo aislado para pruebas, no como despliegue público de producción

## Qué puedes hacer con él

Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes.

## Por qué destaca

Usos propuestos: Representar cambios de una relación comercial; Conservar hechos de conversaciones con fechas.

## Cómo funciona

Su MCP es una referencia experimental sin autenticación ni autorización: úsalo aislado para pruebas, no como despliegue público de producción

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- Neo4j o FalkorDB
- LLM y embeddings configurados

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install graphiti-core
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/getzep/graphiti/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Graphiti para mi objetivo y necesito pasos guiados. Lee https://github.com/getzep/graphiti/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade dos hechos con fechas distintas y consulta cuál era válido en cada momento.

**Qué comprobar:** El grafo conserva relaciones temporales y sus fuentes.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Representar cambios de una relación comercial
- Conservar hechos de conversaciones con fechas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Representar cambios de una relación comercial; Conservar hechos de conversaciones con fechas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Su MCP es una referencia experimental sin autenticación ni autorización: úsalo aislado para pruebas, no como despliegue público de producción

## Stack y modelos

- **Stack:** Python; Neo4j o FalkorDB; LLM y embeddings configurados
- **Etiquetas:** `memory` `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mcp-neo4j](mcp-neo4j.md) | 989 | Servidores experimentales de Neo4j Labs para consultar grafos, memoria y recursos Aura desde clientes MCP. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [cognee](cognee.md) | 33.3k | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. |
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |

## Enlaces

- 🐙 GitHub: [getzep/graphiti](https://github.com/getzep/graphiti)
- 🌐 Web: <https://help.getzep.com/graphiti>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/getzep/graphiti/blob/main/README.md)
- [Fuente 2](https://github.com/getzep/graphiti/blob/main/mcp_server/README.md)
- [Fuente 3](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
