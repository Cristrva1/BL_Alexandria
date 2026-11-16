[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › NotebookLM: alternativas y clientes

# 🎚️ notebooklm-mcp-cli

> CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.5k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 51/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

CLI y servidor MCP no oficiales para Gemini Notebook (antes Google NotebookLM), de jacob-bd. MIT y muy activo (v0.16.5); el repositorio se renombró a `gemini-notebook-mcp-cli`. Las cuentas personales se prueban con regularidad; el soporte Enterprise es experimental.

## ¿Qué hace?

Permite crear y gestionar cuadernos, fuentes y artefactos (por ejemplo videos y presentaciones) desde la terminal con `nlm` o desde asistentes de IA vía MCP. El asistente `nlm setup` detecta las herramientas instaladas y las conecta: Claude Code, Claude Desktop, Codex CLI/ChatGPT, Gemini CLI, Cursor, Windsurf, Cline, Antigravity, GitHub Copilot y otras.

## ¿Cómo lo hace?

Se instala con `uv tool install notebooklm-mcp-cli` y se autentica con `nlm login` usando tu cuenta de Google. Ofrece almacenamiento protegido del inicio de sesión (cifrado con la clave en el llavero del sistema) mediante `nlm auth storage set protected`; servidores, cron o Docker pueden seguir usando el archivo plano. Depende de APIs no oficiales que pueden cambiar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Cliente MCP soportado por `nlm setup`. | `nlm login` primero; después `nlm setup` y marca Claude Code. |
| [Codex CLI](codex.md) | Cliente soportado (`nlm setup add codex`). | Igual que arriba. |
| [Gemini CLI](gemini-cli.md) | Cliente MCP soportado por el asistente de configuración. | Igual que arriba. |

**Notas:** Activa el almacenamiento protegido en equipos personales. Se retiraron las combinaciones con notebooklm-py (solapamiento) y awesome-mcp-servers (es una lista, no una integración).

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v0.16.5 (2026-11-14) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige clave LLM propia; cuenta y límites de Google, servicios y agente anfitrión tienen condiciones separadas |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. Documenta los tres clientes; instalar CLI o MCP no vuelve local la generación ni evita los cupos de NotebookLM |
| Coste | El coste depende del proveedor o la ruta. No exige clave LLM propia; cuenta y límites de Google, servicios y agente anfitrión tienen condiciones separadas |
| Equipo | Preparación según la ruta elegida. Python; cuenta Google; cliente MCP; sesión del navegador |

Documenta los tres clientes; instalar CLI o MCP no vuelve local la generación ni evita los cupos de NotebookLM

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- cuenta Google
- cliente MCP
- sesión del navegador

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
pip install notebooklm-mcp-cli
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar notebooklm-mcp-cli para mi objetivo y necesito pasos guiados. Lee https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta el asistente de setup, conecta un cliente y consulta una fuente ficticia en un notebook de prueba.

**Qué comprobar:** Puedes contrastar la respuesta y comprobar el estado de autenticación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Administrar fuentes desde un agente
- Exportar contenido generado por NotebookLM

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Administrar fuentes desde un agente; Exportar contenido generado por NotebookLM | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta los tres clientes; instalar CLI o MCP no vuelve local la generación ni evita los cupos de NotebookLM

## Stack y modelos

- **Stack:** Python; cuenta Google; cliente MCP; sesión del navegador
- **Etiquetas:** `mcp` `notebooks` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [jacob-bd/gemini-notebook-mcp-cli](https://github.com/jacob-bd/gemini-notebook-mcp-cli)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
