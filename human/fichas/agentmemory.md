[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 💾 agentmemory

> Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.4k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Memoria persistente de código abierto (Apache 2.0) para sesiones de programación y agentes, de rohitg00, que se presenta como implementación del patrón «LLM Wiki» de Karpathy con puntuación de confianza, ciclo de vida, grafos y búsqueda híbrida. Muy activo (v0.9.33).

## ¿Qué hace?

Captura las sesiones de Claude Code, GitHub Copilot CLI, Cursor, Gemini CLI, Codex CLI, Hermes, OpenClaw, pi, OpenCode, DeepSeek Harness y cualquier cliente MCP, hace buscables decisiones y arreglos y permite a otro agente retomar historial, lecciones y traspasos. Elimina secretos al capturar, permite reproducir sin conexión y ofrece un visor en vivo para explorar, editar, exportar y olvidar memorias.

## ¿Cómo lo hace?

Requiere Node.js 20+; se ejecuta con `npx -y @agentmemory/agentmemory@latest`. Sin clave usa búsqueda por palabras clave (BM25) y coincidencias estructurales del grafo; con embeddings locales o remotos añade búsqueda semántica. La API queda en `localhost:3111` y el visor en `localhost:3113`, ambos solo en loopback por defecto; la configuración vive en `~/.agentmemory/.env`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Captura con hooks y plugins nativos. | Arranca agentmemory primero y luego conecta el agente según su guía. |
| [Gemini CLI](gemini-cli.md) | Agente soportado de forma nativa. | Igual que arriba. |
| [hermes-agent](hermes-agent.md) | Agente soportado de forma nativa. | Igual que arriba. |
| [DeepSeek Harness (DSH)](deepseek-harness.md) | agentmemory declara capturar sesiones de DeepSeek Harness para que otro agente retome historial y lecciones. | Conecta agentmemory después de configurar DSH. |

**Notas:** Alternativas (elige una): engram, supermemory, claude-mem. No expongas los puertos 3111/3113 fuera de loopback sin autenticación.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v0.9.33 (2026-11-09) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/rohitg00/agentmemory/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Captura y búsqueda por palabras funcionan sin clave; embeddings locales son opcionales; compresión LLM puede hacer una llamada por observación |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración documentada por el proyecto |
| Modelos locales | Modelos locales documentados. Las funciones y hooks dependen del runtime del cliente; la instalación de MCP no prueba que la captura automática esté activa |
| Coste | El coste depende del proveedor o la ruta. Captura y búsqueda por palabras funcionan sin clave; embeddings locales son opcionales; compresión LLM puede hacer una llamada por observación |
| Equipo | Preparación según la ruta elegida. Node.js >=20; servidor local; hooks revisados en el cliente |

Las funciones y hooks dependen del runtime del cliente; la instalación de MCP no prueba que la captura automática esté activa

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js >=20
- servidor local
- hooks revisados en el cliente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx -y @agentmemory/agentmemory@latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/rohitg00/agentmemory/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar agentmemory para mi objetivo y necesito pasos guiados. Lee https://github.com/rohitg00/agentmemory/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Registra una decisión ficticia y búscala desde otro cliente conectado al mismo servidor.

**Qué comprobar:** Puedes inspeccionar el recuerdo y confirmar que ambos clientes usan la misma instancia.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Compartir contexto entre Claude Code y Codex
- Consultar decisiones por proyecto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Compartir contexto entre Claude Code y Codex; Consultar decisiones por proyecto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las funciones y hooks dependen del runtime del cliente; la instalación de MCP no prueba que la captura automática esté activa

## Stack y modelos

- **Stack:** Node.js >=20; servidor local; hooks revisados en el cliente
- **Etiquetas:** `agents` `memory` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Engram](engram.md) | 8.2k | Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. |
| [supermemory](supermemory.md) | 31.6k | Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local. |
| [claude-mem](claude-mem.md) | 117k | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. |

## Enlaces

- 🐙 GitHub: [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)
- 🌐 Web: <https://www.agent-memory.dev/docs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/rohitg00/agentmemory/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
