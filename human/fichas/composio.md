[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🛠️ Composio

> Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.1k | MIT | TypeScript | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Composio, monorepo de SDKs que da a los agentes más de 1000 toolkits preautenticados, de ComposioHQ. Licencia MIT para los SDKs; la plataforma es un servicio con API key. Tiene ~31k estrellas.

## ¿Qué hace?

Gestiona sesiones por usuario, autenticación, triggers y un sandbox para que los agentes actúen en apps externas. Cada sesión expone además un endpoint MCP alojado.

## ¿Cómo lo hace?

Incluye SDK de TypeScript (`@composio/core`, o la variante reducida `@composio/slim`), SDK de Python (`pip install composio`), una CLI y adaptadores para OpenAI Agents, Claude Agent SDK, Vercel AI SDK, LangChain y más. Requiere `COMPOSIO_API_KEY`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenAI Agents SDK](openai-agents-python.md) | Adaptador oficial (`composio-openai-agents`). | Instala el SDK y el adaptador. |
| [LangGraph](langgraph.md) | Adaptador LangChain/LangGraph. | Instala el adaptador del proveedor. |
| [Mastra](mastra.md) | Adaptador de proveedor. | Instala el adaptador de Mastra. |
| [Claude Code](claude-code.md) | Cliente del endpoint MCP de la sesión. | Pasa `mcp: true` y añade la URL. |

**Notas:** Sin alternativas declaradas. Dependencia de un servicio comercial para las credenciales de terceros.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada @composio/cli@0.6.1 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ComposioHQ/composio/blob/next/README.md) · [2](https://docs.composio.dev/docs/providers/custom-providers)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La conexión no necesita un LLM propio en su ruta básica; Composio requiere autenticación y su servicio y apps externas tienen condiciones de uso |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El CLI ofrece una superficie local para Claude Code; el SDK de Claude Agent no equivale a incluir créditos o plan de Claude Code |
| Coste | Consumo de APIs o servicios. La conexión no necesita un LLM propio en su ruta básica; Composio requiere autenticación y su servicio y apps externas tienen condiciones de uso |
| Equipo | Preparación según la ruta elegida. Cuenta Composio; CLI o SDK; cuenta externa de prueba |

El CLI ofrece una superficie local para Claude Code; el SDK de Claude Agent no equivale a incluir créditos o plan de Claude Code

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta Composio
- CLI o SDK
- cuenta externa de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ComposioHQ/composio/blob/next/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Composio para mi objetivo y necesito pasos guiados. Lee https://github.com/ComposioHQ/composio/blob/next/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Busca una herramienta de consulta y revisa sus permisos antes de enlazar una cuenta.

**Qué comprobar:** Puedes identificar acción, aplicación y alcance de autorización.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Conectar un agente a un CRM
- Explorar herramientas de consulta de un servicio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Conectar un agente a un CRM; Explorar herramientas de consulta de un servicio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El CLI ofrece una superficie local para Claude Code; el SDK de Claude Agent no equivale a incluir créditos o plan de Claude Code

## Stack y modelos

- **Stack:** Cuenta Composio; CLI o SDK; cuenta externa de prueba
- **Etiquetas:** `agents` `mcp` `automation` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ComposioHQ/composio](https://github.com/ComposioHQ/composio)
- 🌐 Web: <https://docs.composio.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ComposioHQ/composio/blob/next/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
