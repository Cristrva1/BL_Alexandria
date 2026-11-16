[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › NotebookLM: alternativas y clientes

# 🎙️ notebooklm-py

> API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 20.2k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

API de Python no oficial y skill para agentes para Google NotebookLM, rebautizado como Gemini Notebook en julio de 2026, creada por teng-lin. MIT y muy activa (v0.8.6); usa APIs no documentadas de Google que pueden cambiar sin aviso y no tiene afiliación con Google.

## ¿Qué hace?

Da acceso programático a NotebookLM, incluidas funciones que la web no expone: importación masiva de fuentes (URL, PDF, YouTube, Google Drive), consultas de investigación con importación automática, y generación de resúmenes en audio (podcasts), videos, presentaciones, cuestionarios, tarjetas, infografías, tablas, mapas mentales y guías de estudio. Descarga los artefactos (MP3, MP4, PDF, PNG, CSV, JSON, Markdown) en lote y exporta a Docs/Sheets.

## ¿Cómo lo hace?

Biblioteca Python asíncrona con CLI, un servidor REST local con rutas protegidas y una skill para Claude Code, Codex y otros agentes (instalable con `npx skills add` o `notebooklm skill install`). Se autentica con tu sesión de Google y está sujeta a límites de uso; recomendada para prototipos, investigación y proyectos personales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Skill oficial para que el agente orqueste NotebookLM mientras Gemini hace la lectura con citas. | Instala la biblioteca, inicia sesión con Google y después la skill. |
| [Codex CLI](codex.md) | También soportado como agente para la skill. | Igual que con Claude Code; usa un solo agente por flujo. |
| [obsidian-second-brain](obsidian-second-brain.md) | El README propone ejecutar la CLI desde la raíz de una bóveda de Obsidian para que informes y mapas queden como archivos (combinación por arquitectura con esta plantilla). | Configura la bóveda primero; ejecuta la CLI desde su carpeta raíz. |

**Notas:** Se retiró la combinación con notebooklm-mcp-cli: ambos son clientes no oficiales de la misma API y se solapan; elige uno.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.8.6 (2026-10-29) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/teng-lin/notebooklm-py/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa tu cuenta y cupos de NotebookLM, no una API local de modelo; el agente y los planes Google tienen límites separados |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. API no oficial con endpoints que pueden cambiar; los archivos descargados quedan locales pero la generación ocurre en Google |
| Coste | El coste depende del proveedor o la ruta. Usa tu cuenta y cupos de NotebookLM, no una API local de modelo; el agente y los planes Google tienen límites separados |
| Equipo | Preparación según la ruta elegida. Python y uv o pipx; sesión Google; Chromium para login; notebook de prueba |

API no oficial con endpoints que pueden cambiar; los archivos descargados quedan locales pero la generación ocurre en Google

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv o pipx
- sesión Google
- Chromium para login
- notebook de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/teng-lin/notebooklm-py/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar notebooklm-py para mi objetivo y necesito pasos guiados. Lee https://github.com/teng-lin/notebooklm-py/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un notebook con una fuente propia breve y pregunta por un dato verificable.

**Qué comprobar:** La consulta y las referencias aparecen en el mismo notebook de Google.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Automatizar consultas documentales
- Exportar mapas o resúmenes propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Automatizar consultas documentales; Exportar mapas o resúmenes propios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** API no oficial con endpoints que pueden cambiar; los archivos descargados quedan locales pero la generación ocurre en Google

## Stack y modelos

- **Stack:** Python y uv o pipx; sesión Google; Chromium para login; notebook de prueba
- **Etiquetas:** `notebooks` `research` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py)
- 🌐 Web: <https://github.com/teng-lin/notebooklm-py>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/teng-lin/notebooklm-py/blob/main/README.md)
- [Fuente 2](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
