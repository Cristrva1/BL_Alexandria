[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Automatización y pruebas por código

# 🌐 Puppeteer

> Librería de Google para controlar Chrome y Firefox desde Node.js.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 95.8k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Puppeteer, librería JavaScript para controlar Chrome o Firefox mediante el protocolo DevTools o WebDriver BiDi, mantenida por el equipo de Chrome. Licencia Apache-2.0. Es madura (~96k estrellas).

## ¿Qué hace?

Automatiza navegación, capturas de pantalla, PDF, scraping, pruebas y rendimiento, en modo headless por defecto.

## ¿Cómo lo hace?

Se instala con `npm i puppeteer` (descarga un Chrome compatible) o `npm i puppeteer-core` (sin navegador).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Lightpanda](lightpanda.md) | Navegador headless ligero, documentado con Puppeteer. | Conecta con `browserWSEndpoint` al CDP de Lightpanda. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | MCP para agentes basado en DevTools. | Úsalo para depurar desde el agente. |
| [awesome-chrome-devtools](awesome-chrome-devtools.md) | Ecosistema CDP. | Consulta herramientas relacionadas. |
| [Nanobrowser](nanobrowser.md) | Combinación recíproca: Nanobrowser lo enlaza como «Nanobrowser usa Puppeteer para seguir los marcos de la página sobre la API `chrome.debugger`». | Orden indicado desde Nanobrowser: No requiere instalación aparte: Puppeteer va incluido en la extensión. |
| [Steel Browser](steel-browser.md) | Combinación recíproca: Steel Browser lo enlaza como «Steel controla Chrome con Puppeteer y la documentación muestra cómo conectar Puppeteer a una sesión». | Orden indicado desde Steel Browser: Arranca Steel con Docker; después conecta Puppeteer a la URL CDP de la sesión. |

**Notas:** Alternativas (elige una): playwright, selenium.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada browsers-v3.2.7 (2026-11-10) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/puppeteer/puppeteer/blob/main/README.md) · [2](https://pptr.dev/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca no exige API de IA; servicios remotos y modelo del agente tienen sus costes |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Puppeteer descarga Chrome y puppeteer-core no; el MCP recomendado es chrome-devtools-mcp, un proyecto compañero que se configura aparte |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca no exige API de IA; servicios remotos y modelo del agente tienen sus costes |
| Equipo | Preparación según la ruta elegida. Node; Chrome compatible o navegador propio con puppeteer-core; página de prueba |

Puppeteer descarga Chrome y puppeteer-core no; el MCP recomendado es chrome-devtools-mcp, un proyecto compañero que se configura aparte

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- Chrome compatible o navegador propio con puppeteer-core
- página de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash npm2yarn):**

```
npm i puppeteer # Downloads compatible Chrome during installation.
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/puppeteer/puppeteer/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Puppeteer para mi objetivo y necesito pasos guiados. Lee https://github.com/puppeteer/puppeteer/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una página de prueba y consulta su título o captura antes de añadir interacciones.

**Qué comprobar:** Puedes comprobar navegador y salida obtenida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Automatizar una captura
- Extraer datos de una página propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Automatizar una captura; Extraer datos de una página propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Puppeteer descarga Chrome y puppeteer-core no; el MCP recomendado es chrome-devtools-mcp, un proyecto compañero que se configura aparte

## Stack y modelos

- **Stack:** Node; Chrome compatible o navegador propio con puppeteer-core; página de prueba
- **Etiquetas:** `browser` `scraping` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| [Selenium](selenium.md) | 34.6k | Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. |
| [Cypress](cypress.md) | 51k | Framework de pruebas end-to-end y de componentes para todo lo que corre en un navegador, con ejecución interactiva, recarga en vivo y depuración paso a paso. |
| [WebdriverIO](webdriverio.md) | 9.9k | Framework de automatización de navegadores y apps móviles para Node.js basado en WebDriver, WebDriver BiDi y Appium, con servidor MCP para asistentes de IA. |

## Enlaces

- 🐙 GitHub: [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer)
- 🌐 Web: <https://pptr.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/puppeteer/puppeteer/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
