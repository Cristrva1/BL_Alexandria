[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Playwright MCP

> Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.7k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Servidor MCP oficial de Microsoft que da a los LLM automatización de navegador con Playwright. Licencia Apache-2.0. Es muy popular y activo (~40k estrellas, v0.0.85, aún 0.x).

## ¿Qué hace?

Permite a un modelo navegar, hacer clic, rellenar formularios y leer páginas a través del árbol de accesibilidad (instantáneas estructuradas), sin depender de capturas de pantalla ni modelos de visión. El README recomienda Playwright CLI + skills para agentes de programación (más eficiente en tokens) y reserva el MCP para bucles que se benefician de estado persistente e inspección rica.

## ¿Cómo lo hace?

Se añade al cliente MCP con `npx @playwright/mcp@latest` (VS Code, Cursor, Windsurf, Claude Desktop, Goose, Grok, Junie y otros); requiere Node.js. Tiene opciones de navegador, perfil, modo headless y capacidades adicionales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Automatización de navegador desde el agente con `claude mcp add`. | Registra `npx @playwright/mcp@latest` como servidor MCP. |
| [playwright](playwright.md) | Motor de automatización sobre el que se construye. | Se instala con el servidor; los navegadores se descargan con Playwright. |
| [MCP Inspector](mcp-inspector.md) | Inspeccionar las herramientas y respuestas del servidor. (combinación por arquitectura) | Conecta el Inspector al servidor. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (11). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[agent-desktop](agent-desktop.md) · [Cherry Studio](cherry-studio.md) · [Cline](cline.md) · [goose](goose.md) · [hello-halo](hello-halo.md) · [Jan](jan.md) · [Kilo Code](kilocode.md) · [LobeHub](lobehub.md) · [odysseus](odysseus.md) · [playwright-cli](playwright-cli.md) · [SurfSense](surfsense.md)

**Notas:** Alternativas (elige una): chrome-devtools-mcp, browser-use, browser-harness.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.0.85 (2026-11-09) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/microsoft/playwright-mcp/blob/main/README.md)</sub>

## Ver similares

Grupo **Servidores MCP de navegador**: Playwright MCP ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Chrome DevTools MCP](chrome-devtools-mcp.md) ⭐ recomendado | 72 | Si buscas esto: servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. |
| 2 | **Playwright MCP** (esta ficha) | 62 | Si buscas esto: servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API adicional de modelo; usa el agente anfitrión y recursos del navegador |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El README documenta los tres clientes; revisa el perfil elegido porque puede conservar sesiones y cookies |
| Coste | Consumo del agente que ya utilizas. No necesita API adicional de modelo; usa el agente anfitrión y recursos del navegador |
| Equipo | Preparación según la ruta elegida. Node.js; npm; cliente MCP; navegador de prueba |

El README documenta los tres clientes; revisa el perfil elegido porque puede conservar sesiones y cookies

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- npm
- cliente MCP
- navegador de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
claude mcp add playwright npx @playwright/mcp@latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/microsoft/playwright-mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Playwright MCP para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/playwright-mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una página local con un formulario ficticio y comprueba sus campos antes de rellenarla.

**Qué comprobar:** La instantánea accesible identifica campos y el resultado de la acción.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar una navegación de tu app
- Inspeccionar un formulario de desarrollo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar una navegación de tu app; Inspeccionar un formulario de desarrollo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README documenta los tres clientes; revisa el perfil elegido porque puede conservar sesiones y cookies

## Stack y modelos

- **Stack:** Node.js; npm; cliente MCP; navegador de prueba
- **Etiquetas:** `mcp` `browser` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | 56.3k | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. |
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |
| [Browser Harness](browser-harness.md) | 19.1k | Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada. |

## Enlaces

- 🐙 GitHub: [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)
- 🌐 Web: <https://www.npmjs.com/package/@playwright/mcp>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/playwright-mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
