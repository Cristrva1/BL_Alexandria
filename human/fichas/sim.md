[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Builders visuales y plataformas de agentes

# 🧩 Sim

> Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.1k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma open source (Apache-2.0) de Sim Studio para construir, desplegar y monitorizar agentes y workflows de IA con un lienzo visual. Hay versión cloud (sim.ai) y autoalojada. Es muy activa (v0.9.58) y popular (~30k estrellas), aunque sigue en versiones 0.x.

## ¿Qué hace?

Permite diseñar workflows y agentes conectando bloques en un lienzo, con integraciones (Slack y otras), bases de conocimiento, sandbox de ejecución, trabajos programados y chat. Incluye un servidor MCP que permite a Claude, Claude Code, Codex u otros clientes MCP gestionar espacios de trabajo y ejecutar y desplegar workflows. También admite modelos locales vía Ollama y vLLM.

## ¿Cómo lo hace?

Hecho con Next.js y Bun sobre PostgreSQL (Drizzle ORM) y Better Auth. El autoalojamiento requiere Node.js 20+ y Docker. `npx sim-setup` es un asistente que crea el despliegue, provisiona la base de datos, genera secretos y escribe `.env`; luego se añaden capacidades con `npx sim-setup add <capacidad>`. Hay modos de desarrollo local y Kubernetes (Helm) desde el código fuente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Modelos locales; el README documenta el soporte de Ollama. | Instala Ollama y descarga los modelos antes de configurar el proveedor en Sim (ver la documentación de autoalojamiento). |
| [vLLM](vllm.md) | Servir modelos locales de alto rendimiento; el README documenta el soporte de vLLM. | Despliega vLLM con su API compatible y configúralo como proveedor en Sim. |
| [Claude Code](claude-code.md) | Gestionar y ejecutar workflows de Sim desde Claude Code vía su servidor MCP (`claude mcp add --transport http sim https://mcp.sim.ai/mcp`). | Ten Sim (cloud o autoalojado) operativo; añade después el servidor MCP en Claude Code. |
| [Codex CLI](codex.md) | Mismo uso desde Codex CLI (`codex mcp add sim --url https://mcp.sim.ai/mcp`). | Sim primero; luego registra el MCP en Codex. |

**Notas:** Alternativas (elige una): langflow, dify, autogpt. Combinación anterior con langfuse eliminada: no se encontró integración documentada en el README ni en la documentación revisada.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.9.58 (2026-11-15) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/simstudioai/sim/blob/main/README.md) · [2](https://docs.sim.ai/mcp/overview) · [3](https://docs.sim.ai/self-hosting/docker) · [4](https://docs.sim.ai/desktop) · [5](https://docs.sim.ai/platform/self-hosting/desktop)</sub>

## Ver similares

Grupo **Builders visuales de agentes**: Sim ocupa la posición 4 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [langflow](langflow.md) ⭐ recomendado | 70 | Si quieres diseñar flujos de LangChain visualmente y exportarlos. |
| 2 | [dify](dify.md) | 70 | Si quieres construir apps de LLM y RAG con interfaz visual y despliegue completo. |
| 3 | [AutoGPT](autogpt.md) | 70 | Si quieres una plataforma de agentes continuos con marketplace de bloques. |
| 4 | **Sim** (esta ficha) | 62 | Si quieres un lienzo colaborativo para agentes y workflows con monitorización. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Cloud y servicios adicionales tienen planes; self-hosting añade infraestructura; las llamadas a modelos se presupuestan según ruta |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. MCP HTTP permite operar workflows desde clientes; inicia sesión y distingue ese acceso de las credenciales del modelo |
| Coste | El coste depende del proveedor o la ruta. Cloud y servicios adicionales tienen planes; self-hosting añade infraestructura; las llamadas a modelos se presupuestan según ruta |
| Equipo | Preparación según la ruta elegida. Node.js 20+; Docker; proveedor o modelo local |

MCP HTTP permite operar workflows desde clientes; inicia sesión y distingue ese acceso de las credenciales del modelo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js 20+
- Docker
- proveedor o modelo local

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx sim-setup
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/simstudioai/sim/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Sim para mi objetivo y necesito pasos guiados. Lee https://github.com/simstudioai/sim/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Construye un flujo visual que recibe texto, lo resume y registra la salida.

**Qué comprobar:** La ejecución muestra cada bloque y el resumen final.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Automatizar una clasificación de mensajes
- Probar un flujo con Ollama antes de usar una API

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Buscas un constructor visual que pueda conectarse a servicios de trabajo y un cliente de macOS con navegador, terminal y acceso a carpetas autorizadas. | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Sim Desktop requiere macOS 12 o posterior y se conecta al despliegue de Sim. En otros sistemas se usa la app web.

## Stack y modelos

- **Stack:** Node.js 20+; Docker; proveedor o modelo local
- **Etiquetas:** `agents` `automation` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langflow](langflow.md) | 157k | Constructor visual de flujos LLM/agentes construido sobre LangChain. |
| [dify](dify.md) | 161k | Plataforma integral para construir apps de IA con backend y UI listos. |
| [AutoGPT](autogpt.md) | 188k | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. |

## Enlaces

- 🐙 GitHub: [simstudioai/sim](https://github.com/simstudioai/sim)
- 🌐 Web: <https://www.sim.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/simstudioai/sim/blob/main/README.md)
- [Fuente 2](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
