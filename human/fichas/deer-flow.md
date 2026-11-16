[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Agentes de research autónomo

# 🦌 deer-flow

> Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 85.3k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

DeerFlow 2.0, «super agent harness» open source de ByteDance, construido sobre LangGraph y LangChain. Licencia MIT. Es una reescritura completa sin código compartido con la v1 (el framework Deep Research sigue en la rama 1.x), tiene ~85k estrellas y está activo.

## ¿Qué hace?

Orquesta subagentes, memoria y sandboxes para tareas de largo recorrido: investigación, código, informes y más. Incluye skills, servidores MCP y un toolset de búsqueda y crawling de BytePlus (InfoQuest).

## ¿Cómo lo hace?

Requiere Python 3.12+, Node 22+, pnpm, uv y nginx (`make check`), y se configura con `make setup`. Se recomienda ejecutarlo con Docker (`make docker-init` descarga la imagen sandbox). El README promociona el Coding Plan de Volcengine/BytePlus.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph](langgraph.md) | Runtime sobre el que está construido. | Viene incluido. |
| [firecrawl](firecrawl.md) | Crawling web alternativo a InfoQuest. (combinación por arquitectura) | Configúralo como herramienta o MCP. |
| [SearXNG](searxng.md) | Búsqueda autoalojada. (combinación por arquitectura) | Configúralo como herramienta de búsqueda. |
| [sandbox](sandbox.md) | Combinación recíproca: sandbox lo enlaza como «Sandbox para el harness. (combinación por arquitectura)». | Orden indicado desde sandbox: Configúralo como entorno de ejecución. |

**Notas:** Sin alternativas declaradas; se solapa con gpt-researcher en el modo investigación (solo anotado).

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.2.0 (2026-11-04) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/bytedance/deer-flow/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Los modelos, herramientas y sandbox tienen costes por configuración; la integración Claude Code no incluye inferencia del servidor |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Documenta el skill claude-to-deerflow para controlar una instancia activa; pedir a Codex que instale el proyecto no demuestra una integración runtime con Codex |
| Coste | El coste depende del proveedor o la ruta. Los modelos, herramientas y sandbox tienen costes por configuración; la integración Claude Code no incluye inferencia del servidor |
| Equipo | Preparación según la ruta elegida. Docker o entorno de desarrollo; modelo configurado; carpeta de prueba |

Documenta el skill claude-to-deerflow para controlar una instancia activa; pedir a Codex que instale el proyecto no demuestra una integración runtime con Codex

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o entorno de desarrollo
- modelo configurado
- carpeta de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow
make setup          # interactive wizard: writes config.yaml and .env (about 2 minutes)
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/bytedance/deer-flow/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar deer-flow para mi objetivo y necesito pasos guiados. Lee https://github.com/bytedance/deer-flow/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Completa setup y solicita un informe corto con fuentes antes de habilitar herramientas de escritura.

**Qué comprobar:** Puedes contrastar las referencias y revisar las acciones del agente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Investigar un tema con fuentes
- Coordinar una generación de informe

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Investigar un tema con fuentes; Coordinar una generación de informe | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta el skill claude-to-deerflow para controlar una instancia activa; pedir a Codex que instale el proyecto no demuestra una integración runtime con Codex

## Stack y modelos

- **Stack:** Docker o entorno de desarrollo; modelo configurado; carpeta de prueba
- **Etiquetas:** `automation` `research` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
- 🌐 Web: <https://deerflow.tech>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/bytedance/deer-flow/blob/main/README.md)
- [Fuente 2](https://github.com/bytedance/deer-flow/blob/main/docs/guide/skills-and-tools.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
