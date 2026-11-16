[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 supermemory

> Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.6k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor de memoria y contexto para IA de Supermemory, que se define como laboratorio de investigación. El repositorio es MIT (servidor en versión 0.0.x) y el servicio principal es una API alojada; afirma ser el n.º 1 en LongMemEval, LoCoMo y ConvoMem [DATO NO VERIFICADO: benchmarks propios].

## ¿Qué hace?

Aprende de las conversaciones, extrae hechos, mantiene perfiles de usuario (unos 50 ms por llamada), gestiona actualizaciones y contradicciones y olvida información caducada. Combina RAG y memoria en una sola consulta, sincroniza Google Drive, Gmail, Notion, OneDrive y GitHub, y extrae contenido de PDF, imágenes (OCR), video (transcripción) y código. Da memoria persistente a Claude Code, Cursor, Codex y OpenCode mediante plugins o MCP.

## ¿Cómo lo hace?

Ofrece una API única con SDK, un servidor MCP alojado (`https://mcp.supermemory.ai/mcp`, código abierto) y una versión local de un solo binario (`npx supermemory local` o script de instalación) que en el primer arranque prepara su motor de grafos embebido, embeddings locales y una clave de API. Admite cualquier modelo o funcionar sin conexión con Ollama.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin y servidor MCP para memoria persistente entre conversaciones. | Decide entre la nube y la versión local; después registra el MCP o el plugin. |
| [OpenCode](opencode.md) | Agente soportado por plugin o MCP. | Igual que arriba. |
| [Ollama](ollama.md) | La versión local puede funcionar sin conexión con Ollama. | Ollama primero con los modelos; después arranca `supermemory-server`. |

**Notas:** Alternativas (elige una): mem0, agentmemory. Con el MCP alojado los datos se procesan en sus servidores.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada server-v0.0.9 (2026-10-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/supermemoryai/supermemory/blob/main/README.md)</sub>

## Ver similares

Grupo **Capas de memoria para apps y agentes de IA**: supermemory ocupa la posición 4 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [mem0](mem0.md) ⭐ recomendado | 76 | Si tu app necesita memoria de usuario a largo plazo con una API sencilla. |
| 2 | [cognee](cognee.md) | 68 | Si quieres convertir documentos en un grafo de conocimiento consultable por agentes. |
| 3 | [Graphiti](graphiti.md) | 61 | Si necesitas un grafo temporal que registre cómo cambian los hechos en el tiempo. |
| 4 | **supermemory** (esta ficha) | 61 | Si buscas una API de memoria y contexto rápida orientada a productos. |
| 5 | [Letta](letta.md) | 55 | Si quieres agentes con estado gestionados por un servidor (antes MemGPT). |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La instancia local admite embeddings locales y Ollama; API Cloud y proveedores remotos tienen planes y consumo separados |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Los plugins y MCP son vías de conexión; confirma que apuntan a la instancia local si buscas mantener el procesamiento en tu equipo |
| Coste | El coste depende del proveedor o la ruta. La instancia local admite embeddings locales y Ollama; API Cloud y proveedores remotos tienen planes y consumo separados |
| Equipo | Preparación según la ruta elegida. Node.js para ruta local; modelo elegido; cuenta para Cloud |

Los plugins y MCP son vías de conexión; confirma que apuntan a la instancia local si buscas mantener el procesamiento en tu equipo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js para ruta local
- modelo elegido
- cuenta para Cloud

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx supermemory local
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/supermemoryai/supermemory/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar supermemory para mi objetivo y necesito pasos guiados. Lee https://github.com/supermemoryai/supermemory/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Guarda una nota de prueba y consulta su contenido desde una segunda sesión.

**Qué comprobar:** Puedes verificar qué se almacenó y en qué instancia.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Conservar contexto entre agentes
- Buscar documentos y recuerdos de un proyecto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Conservar contexto entre agentes; Buscar documentos y recuerdos de un proyecto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los plugins y MCP son vías de conexión; confirma que apuntan a la instancia local si buscas mantener el procesamiento en tu equipo

## Stack y modelos

- **Stack:** Node.js para ruta local; modelo elegido; cuenta para Cloud
- **Etiquetas:** `memory` `rag` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mem0](mem0.md) | 69k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [agentmemory](agentmemory.md) | 30.4k | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. |

## Enlaces

- 🐙 GitHub: [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory)
- 🌐 Web: <https://supermemory.ai/docs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/supermemoryai/supermemory/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
