[🏠 Inicio](../README.md) › [🕷️ Buscar y extraer información web](../categorias/04-scraping-b-squeda-research-web.md) › Navegadores y automatización web

# 🎭 playwright-cli

> Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.2k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Resuelve el problema de los árboles de accesibilidad y los JSON de herramientas que inflan el prompt en cada turno.

## Por qué destaca

Alternativa token-eficiente a Playwright MCP, pensada para agentes de código (Claude Code, Cursor, Codex) que necesitan tocar la web sin quemar contexto. Procede del propio ecosistema Playwright de Microsoft, lo que garantiza compatibilidad con su API de automatización.

## Cómo funciona

Envuelve los comandos de Playwright en un CLI que el agente invoca paso a paso (navegar, clickar, leer), devolviendo salidas compactas en lugar de volcar el DOM o el accessibility tree enteros en cada turno.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/microsoft/playwright-cli/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar playwright-cli para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/playwright-cli/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Que un agente automatice el browser de forma token-eficiente
- Alternativa a Playwright MCP cuando el contexto aprieta
- Flujos de login/scraping guiados por un agente de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente vive en CLI y el contexto es un recurso caro | necesitas estado persistente entre sesiones o un servidor MCP con recursos expuestos (usa Playwright MCP) |

## Stack y modelos

- **Stack:** TypeScript/Node.js, CLI
- **Etiquetas:** `browser` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [agent-browser](agent-browser.md) | 51.2k | CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes. |

## Enlaces

- 🐙 GitHub: [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli)
- 🌐 Web: <https://playwright.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/microsoft/playwright-cli/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
