[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🖥️ OpenBot

> Espacio autoalojable de CopilotKit para compañeros de IA con navegador propio, permisos, aprobaciones y auditoría, conectables por AG-UI.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.5k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🔴 pesado · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación pesada; app o instalador listo para usar

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de CopilotKit (creadores de AG-UI) para «compañeros de trabajo» de IA autoalojables, en TypeScript. La plantilla es MIT, pero necesita CopilotKit Intelligence, con licencia aparte: gratuita en local para uso personal, de prueba para evaluar en Kubernetes y de pago en producción. Versión v1.0.3 (noviembre de 2026), ~12k estrellas.

## ¿Qué hace?

Da a cada Bot su propio «ordenador» (navegador, archivos y herramientas) y aplica a cada acción inicio de sesión, permisos por herramienta, políticas CEL, aprobaciones y auditoría. Permite traer agentes propios por AG-UI y herramientas por MCP (Google Drive, Notion, Parallel, Exa, Firecrawl, y cientos de apps vía Composio o Arcade), con clientes de escritorio, web, móvil, Slack y Teams.

## ¿Cómo lo hace?

Para una persona, la app de escritorio (Mac/Windows) incluye el backend en Docker. Desde el código usa Bun y Docker (PostgreSQL, API y Bots) y la CLI de CopilotKit para la licencia local. Para equipos se despliega con Helm en Kubernetes (amd64, StorageClass, licencia y clave de modelo). Los modelos pueden ser OpenAI, Claude, Gemini o cualquier endpoint compatible con OpenAI, incluso locales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [CopilotKit](copilotkit.md) | OpenBot está construido sobre CopilotKit y AG-UI; su frontend y la conexión de agentes usan ese stack. | Usa CopilotKit al extender la interfaz o conectar agentes propios. |
| [LangGraph](langgraph.md) | El repositorio incluye un agente de ejemplo LangGraph conectado por AG-UI (`agent-langgraph-agui`). | Despliega OpenBot y registra el agente LangGraph como agente externo. |
| [Mastra](mastra.md) | Incluye un agente de ejemplo de Mastra (`agent-mastra`) conectable por AG-UI. | Arranca OpenBot y conecta el agente Mastra. |
| [crewAI](crewai.md) | Incluye un agente de ejemplo de CrewAI (`agent-crewai`) para la misma vía AG-UI. | Conecta el agente CrewAI después de configurar el modelo. |
| [firecrawl](firecrawl.md) | Firecrawl figura entre los proveedores de investigación web que el catálogo MCP de OpenBot incluye de serie. | Añade la clave de Firecrawl en la configuración de herramientas. |
| [Composio](composio.md) | Composio actúa como intermediario de cientos de apps detrás de una sola cuenta en el catálogo MCP gobernado. | Prepara `setup:composio` y concede solo las apps necesarias. |

**Notas:** Alternativa (elige una): opendots. OpenDots es ahora una «skin» de OpenBot y su repositorio queda como starter mantenido por la comunidad. El agente navegador maneja sesiones reales: mantén los puertos en loopback.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.0.3 (2026-11-14) · licencia declarada MIT (plantilla; Intelligence con licencia aparte) (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/CopilotKit/OpenBot/blob/main/README.md) · [2](https://github.com/CopilotKit/OpenDots/blob/main/README.md)</sub>

## Ver similares

Grupo **Espacios de asistentes de CopilotKit**: OpenBot ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **OpenBot** (esta ficha) ⭐ recomendado | 67 | Si buscas esto: espacio autoalojable de CopilotKit para compañeros de IA con navegador propio, permisos, aprobaciones y auditoría, conectables por AG-UI. |
| 2 | [OpenDots](opendots.md) | 48 | Si buscas esto: interfaz abierta de asistentes persistentes que requiere CopilotKit Intelligence, alojado, evaluado localmente o con licencia. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Elige OpenAI, Claude, Gemini o un endpoint compatible con OpenAI; el despliegue en Kubernetes de evaluación usa una clave de modelo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El README describe una operación totalmente local con OpenBot, Intelligence y un modelo compatible; las apps conectadas siguen usando internet. |
| Coste | El coste depende del proveedor o la ruta. La plantilla es MIT, pero CopilotKit Intelligence tiene licencia aparte: local gratuita para uso personal, prueba para Kubernetes y licencia de producción después. |
| Equipo | Preparación según la ruta elegida. Docker para PostgreSQL, la API y los Bots; Bun para ejecutar desde el código; Kubernetes y Helm para equipos. |

Los agentes externos se conectan por AG-UI (el repositorio trae ejemplos para LangGraph, Mastra, CrewAI, Agno, Pydantic AI, ADK y otros); no usa sesiones de Claude Code o Codex.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y una copia de datos o archivos para la primera prueba.

1. Para probarlo solo, descarga la app de escritorio enlazada en el README; incluye el backend en Docker.
2. Elige el modelo (OpenAI, Claude, Gemini o un endpoint compatible) y revisa la licencia local de CopilotKit Intelligence.
3. Pide una tarea con aprobación activada y revisa la auditoría antes de conectar cuentas reales o un equipo.

**Entrada documentada (bash):**

```
docker run -p 3001:3001 --env-file .env -e EMBEDDED_POSTGRES=on -v openbot-data:/var/lib/postgresql ghcr.io/copilotkit/openbot:latest
```

Comando copiado literalmente de el README (sección «Deploy it»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/CopilotKit/OpenBot/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/CopilotKit/OpenBot/releases)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenBot para mi objetivo y necesito pasos guiados. Lee https://github.com/CopilotKit/OpenBot/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala la app de escritorio, configura un modelo y pide una búsqueda web que requiera aprobación.

**Qué comprobar:** La acción queda pendiente de tu aprobación y aparece en la auditoría.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Dar a un asistente un navegador propio con aprobaciones
- Conectar un agente existente por AG-UI a un espacio común

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Dar a un asistente un navegador propio con aprobaciones; Conectar un agente existente por AG-UI a un espacio común | necesitas una herramienta estable y auditada para datos sensibles |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. CopilotKit Intelligence es un componente con licencia propia, necesario para ejecutar OpenBot.

## Stack y modelos

- **Stack:** TypeScript, docker-compose.yml, package.json
- **Etiquetas:** `agents` `computer-use` `ag-ui` `mcp` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenDots](opendots.md) | 6.6k | Interfaz abierta de asistentes persistentes que requiere CopilotKit Intelligence, alojado, evaluado localmente o con licencia. |

## Enlaces

- 🐙 GitHub: [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)
- 🌐 Web: <open.bot>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/CopilotKit/OpenBot/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
