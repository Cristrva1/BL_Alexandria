[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🐝 ruflo

> Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 81.7k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado · **MCP** 🔌 sí

## ¿Qué es?

Ruflo, meta-harness de agentes para Claude Code y Codex, de @ruvnet. Licencia MIT. Tiene ~82k estrellas y está activo; el README es muy promocional (swarms, federación, ruOS).

## ¿Qué hace?

Añade al proyecto agentes, hooks, memoria y un servidor MCP para coordinar enjambres de agentes que aprenden de cada tarea y recuerdan entre sesiones. Incluye una consola visual y una TUI.

## ¿Cómo lo hace?

Se inicia con `npx ruflo@latest init`; otras vías son los plugins de Claude Code (≥2.1.287) o un servidor MCP para Codex y otros clientes (`npx -y ruflo@latest mcp start`). Los mods se ejecutan con los permisos de tu cuenta, así que conviene revisarlos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Anfitrión principal (plugins y hooks). | Instala Claude Code y luego `ruflo init`. |
| [Codex CLI](codex.md) | Cliente vía servidor MCP. | Añade el MCP de ruflo a Codex. |
| [OpenCode](opencode.md) | Cliente MCP genérico. (combinación por arquitectura) | Añade el MCP de ruflo a OpenCode. |

**Notas:** Sin alternativas declaradas. Se quita mem0 de las combinaciones porque ruflo trae su propia memoria. Cuidado con las afirmaciones de marketing.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.77.1 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ruvnet/ruflo/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Usa el proveedor o plan de los agentes; el plugin local ruvllm documenta Ollama |
| Claude Code | Integración documentada por el proyecto |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Claude Code tiene integración de proyecto; otros clientes usan el servidor MCP estándar y no heredan necesariamente sus hooks ni todas las funciones |
| Coste | El coste depende del proveedor o la ruta. Usa el proveedor o plan de los agentes; el plugin local ruvllm documenta Ollama |
| Equipo | Preparación según la ruta elegida. Node; carpeta de proyecto; Claude Code o cliente MCP; modelo para agentes |

Claude Code tiene integración de proyecto; otros clientes usan el servidor MCP estándar y no heredan necesariamente sus hooks ni todas las funciones

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- carpeta de proyecto
- Claude Code o cliente MCP
- modelo para agentes

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx ruflo@latest init
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ruvnet/ruflo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ruflo para mi objetivo y necesito pasos guiados. Lee https://github.com/ruvnet/ruflo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inicializa una carpeta de prueba y examina los agentes, hooks y configuración añadidos antes de encargar trabajo.

**Qué comprobar:** Puedes identificar los archivos creados y herramientas MCP disponibles.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Coordinar tareas de código
- Estudiar memoria compartida entre agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Coordinar tareas de código; Estudiar memoria compartida entre agentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Claude Code tiene integración de proyecto; otros clientes usan el servidor MCP estándar y no heredan necesariamente sus hooks ni todas las funciones

## Stack y modelos

- **Stack:** Node; carpeta de proyecto; Claude Code o cliente MCP; modelo para agentes
- **Etiquetas:** `automation` `agents` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [ruvnet/ruflo](https://github.com/ruvnet/ruflo)
- 🌐 Web: <https://cognitum.one>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ruvnet/ruflo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
