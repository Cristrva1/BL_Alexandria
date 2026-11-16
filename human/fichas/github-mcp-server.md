[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 GitHub MCP Server

> Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 34.5k | MIT | Go | 2026-06-24 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Servidor MCP oficial de GitHub que conecta herramientas de IA con la plataforma. Licencia MIT. Es muy activo (~35k estrellas, v2.1.0).

## ¿Qué hace?

Permite a agentes leer repositorios y código, gestionar issues y PR, analizar código, revisar workflows de Actions y automatizar tareas, organizados en toolsets que se pueden activar o desactivar. Tiene modo de solo lectura y políticas de gobierno para organizaciones. Se publica también como módulo Go.

## ¿Cómo lo hace?

Se usa en remoto (alojado por GitHub, con OAuth o token) en hosts compatibles, o en local con Docker (`ghcr.io/github/github-mcp-server`) o el binario y un token personal. Hay guías de instalación para Claude, Codex y otros clientes. Limita los toolsets y permisos del token a lo necesario.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Guía oficial de instalación para Claude. | Sigue `docs/installation-guides/install-claude.md`. |
| [Codex CLI](codex.md) | Guía oficial de instalación para Codex. | Sigue `docs/installation-guides/install-codex.md`. |
| [strix](strix.md) | Strix usa el servidor MCP de GitHub como ejemplo de configuración. | Añádelo a `~/.strix/mcp-servers.json`. |

**Notas:** Sin alternativas declaradas. Usa el modo de solo lectura cuando no necesites escribir.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.1.0 (2026-11-03) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/github/github-mcp-server/blob/main/README.md) · [2](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-claude.md) · [3](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-codex.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La herramienta no exige modelo propio; el cliente, planes GitHub y acciones del servicio tienen límites y posibles costes |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Empieza con el conjunto de herramientas y permisos de lectura necesario; no copies tokens de ejemplo como credenciales reales |
| Coste | El coste depende del proveedor o la ruta. La herramienta no exige modelo propio; el cliente, planes GitHub y acciones del servicio tienen límites y posibles costes |
| Equipo | Preparación según la ruta elegida. Cuenta GitHub; cliente MCP; token con permisos adecuados o autenticación remota |

Empieza con el conjunto de herramientas y permisos de lectura necesario; no copies tokens de ejemplo como credenciales reales

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta GitHub
- cliente MCP
- token con permisos adecuados o autenticación remota

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/github/github-mcp-server/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GitHub MCP Server para mi objetivo y necesito pasos guiados. Lee https://github.com/github/github-mcp-server/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lista archivos y lee un README de un repositorio público antes de habilitar herramientas de escritura.

**Qué comprobar:** El agente devuelve contenidos y enlaces del repositorio elegido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar una base de código
- Revisar el estado de una pull request

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar una base de código; Revisar el estado de una pull request | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Empieza con el conjunto de herramientas y permisos de lectura necesario; no copies tokens de ejemplo como credenciales reales

## Stack y modelos

- **Stack:** Cuenta GitHub; cliente MCP; token con permisos adecuados o autenticación remota
- **Etiquetas:** `mcp` `code` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [github/github-mcp-server](https://github.com/github/github-mcp-server)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/github/github-mcp-server/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
