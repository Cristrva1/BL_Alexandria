[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Awesome GitHub Copilot

> Colección comunitaria de GitHub con agentes, instrucciones, skills, hooks y plugins para personalizar GitHub Copilot.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 41.2k | MIT | JavaScript | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección comunitaria alojada por GitHub (MIT) de agentes personalizados, instrucciones, skills, hooks, flujos de trabajo y plugins para GitHub Copilot. Muy activa; tiene web con búsqueda y un Learning Hub.

## ¿Qué hace?

Ofrece agentes especializados de Copilot que se integran con servidores MCP, instrucciones de estilo que se aplican por patrón de archivo, skills autocontenidas y paquetes de plugins por flujo de trabajo. Publica un `llms.txt` para que los agentes lean el catálogo.

## ¿Cómo lo hace?

Archivos Markdown en el repositorio. Los plugins se instalan con la CLI de Copilot (`copilot plugin marketplace add github/awesome-copilot` y `copilot plugin install <plugin>@awesome-copilot`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [GitHub MCP Server](github-mcp-server.md) | Servidor MCP que pueden usar los agentes de Copilot de la colección (combinación por arquitectura). | Configura el MCP en Copilot antes de usar agentes que lo requieran. |
| [Spec Kit](spec-kit.md) | Proceso de desarrollo guiado por especificaciones con integración para Copilot. | `specify init <proyecto> --integration copilot`. |
| [GitHub CLI](cli.md) | Trabajar con repos, PR e incidencias desde la terminal junto a Copilot (combinación por arquitectura). | Independientes. |

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/github/awesome-copilot/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las personalizaciones se usan con el acceso de Copilot; no acreditan consumo incluido en Claude Code o Codex |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El destino principal es GitHub Copilot; el comando contiene un marcador que debes sustituir, no ejecutar literalmente |
| Coste | Consumo del agente que ya utilizas. Las personalizaciones se usan con el acceso de Copilot; no acreditan consumo incluido en Claude Code o Codex |
| Equipo | Preparación según la ruta elegida. GitHub Copilot y un plugin elegido del catálogo |

El destino principal es GitHub Copilot; el comando contiene un marcador que debes sustituir, no ejecutar literalmente

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- GitHub Copilot y un plugin elegido del catálogo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
copilot plugin install <plugin-name>@awesome-copilot
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/github/awesome-copilot/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Awesome GitHub Copilot para mi objetivo y necesito pasos guiados. Lee https://github.com/github/awesome-copilot/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sustituye el marcador plugin-name por un plugin listado y consulta sus instrucciones.

**Qué comprobar:** Copilot reconoce la personalización seleccionada y puedes ver sus capacidades.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Añadir instrucciones de equipo al asistente de programación
- Estudiar un agente especializado antes de adaptarlo a un proyecto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Añadir instrucciones de equipo al asistente de programación; Estudiar un agente especializado antes de adaptarlo a un proyecto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El destino principal es GitHub Copilot; el comando contiene un marcador que debes sustituir, no ejecutar literalmente

## Stack y modelos

- **Stack:** GitHub Copilot y un plugin elegido del catálogo
- **Etiquetas:** `skills` `coding-agent` `prompts` `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [github/awesome-copilot](https://github.com/github/awesome-copilot)
- 🌐 Web: <https://awesome-copilot.github.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/github/awesome-copilot/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
