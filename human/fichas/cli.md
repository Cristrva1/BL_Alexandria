[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › CLIs y SDKs de desarrollo

# 🧰 GitHub CLI

> CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47k | MIT | Go | 2026-08-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

GitHub CLI (`gh`), la herramienta oficial de GitHub para la terminal. Licencia MIT. Es madura y muy activa (~47k estrellas, v2.104.0).

## ¿Qué hace?

Lleva a la terminal pull requests, issues, releases, Actions, repos, gists y la API de GitHub (`gh api`), además de extensiones de la comunidad. Funciona con GitHub.com, Enterprise Cloud y las versiones soportadas de Enterprise Server. Es la vía habitual con la que los agentes de programación operan sobre GitHub.

## ¿Cómo lo hace?

Es un binario en Go para macOS, Windows y Linux, instalable con Homebrew, winget, paquetes de distribución o desde las releases. Se autentica con `gh auth login` (navegador o token). La clave PGP de los repositorios de paquetes de Linux rotó el 5 de septiembre de 2026; si fallan las actualizaciones, consulta el anuncio.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Dar al agente acceso a PR, issues y CI desde la terminal. (combinación por arquitectura) | Autentica `gh` y permite su uso al agente. |
| [GitHub MCP Server](github-mcp-server.md) | Acceso a GitHub vía MCP para clientes sin shell. (combinación por arquitectura) | Usa `gh` en terminal y el servidor MCP en clientes sin shell. |
| [activepieces](activepieces.md) | Activepieces tiene una pieza oficial `github` para usar GitHub CLI en flujos. | GitHub CLI en marcha con sus credenciales; después añade la pieza `github` en un flujo de Activepieces. |
| [Agentic Awesome Skills (AAS)](antigravity-awesome-skills.md) | Combinación recíproca: Agentic Awesome Skills (AAS) lo enlaza como «Instalación de skills individuales con `gh skill`». | Orden indicado desde Agentic Awesome Skills (AAS): GitHub CLI con soporte de `gh skill` instalado. |
| [Awesome GitHub Copilot](awesome-copilot.md) | Combinación recíproca: Awesome GitHub Copilot lo enlaza como «Trabajar con repos, PR e incidencias desde la terminal junto a Copilot (combinación por arquitectura)». | Orden indicado desde Awesome GitHub Copilot: Independientes. |

**Notas:** Sin alternativas declaradas. Limita los scopes del token que uses con agentes.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v2.104.0 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1]() · [2](https://cli.github.com/manual/) · [3](https://github.com/activepieces/activepieces/tree/main/packages/pieces/community/github)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa modelo; GitHub y acciones de la cuenta conservan sus límites y costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Instala gh antes de instalar su skill opcional; los comandos que escriben o publican afectan la cuenta autenticada |
| Coste | Sin pago a un modelo en la ruta básica. No usa modelo; GitHub y acciones de la cuenta conservan sus límites y costes |
| Equipo | Preparación según la ruta elegida. Binario gh oficial; cuenta GitHub para operaciones autenticadas |

Instala gh antes de instalar su skill opcional; los comandos que escriben o publican afectan la cuenta autenticada

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario gh oficial
- cuenta GitHub para operaciones autenticadas

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/cli/cli/blob/trunk/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GitHub CLI para mi objetivo y necesito pasos guiados. Lee https://github.com/cli/cli/blob/trunk/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Autentica tu cuenta y consulta el estado de una pull request de un repositorio de prueba.

**Qué comprobar:** Ves el estado que coincide con la interfaz de GitHub.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar issues desde terminal
- Revisar ejecuciones de Actions

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar issues desde terminal; Revisar ejecuciones de Actions | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Instala gh antes de instalar su skill opcional; los comandos que escriben o publican afectan la cuenta autenticada

## Stack y modelos

- **Stack:** Binario gh oficial; cuenta GitHub para operaciones autenticadas
- **Etiquetas:** `code` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [cli/cli](https://github.com/cli/cli)
- 🌐 Web: <https://cli.github.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cli/cli/blob/trunk/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
