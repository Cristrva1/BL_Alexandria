[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🧠 supermemory

> Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.6k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

## Qué puedes hacer con él

Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local.

## Por qué destaca

Usos propuestos: Conservar contexto entre agentes; Buscar documentos y recuerdos de un proyecto.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AI SDK (Vercel)](vercel-ai.md) | 28k | Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. |

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
