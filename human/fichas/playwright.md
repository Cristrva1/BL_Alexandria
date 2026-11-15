[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Automatización y pruebas por código

# 🎭 playwright

> Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 100k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Los tests y control básico no necesitan API de IA; agente y servicios de browser Cloud son independientes |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El MCP es el proyecto compañero playwright-mcp y el CLI otra superficie; instala la ruta adecuada en lugar de confundir biblioteca, skill y servidor |
| Coste | Sin pago a un modelo en la ruta básica. Los tests y control básico no necesitan API de IA; agente y servicios de browser Cloud son independientes |
| Equipo | Preparación según la ruta elegida. Node; navegadores descargados; aplicación de prueba |

El MCP es el proyecto compañero playwright-mcp y el CLI otra superficie; instala la ruta adecuada en lugar de confundir biblioteca, skill y servidor

## Qué puedes hacer con él

Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje.

## Por qué destaca

Usos propuestos: Probar un formulario; Crear regresiones de una web.

## Cómo funciona

El MCP es el proyecto compañero playwright-mcp y el CLI otra superficie; instala la ruta adecuada en lugar de confundir biblioteca, skill y servidor

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- navegadores descargados
- aplicación de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm i -D @playwright/test
npx playwright install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/microsoft/playwright/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar playwright para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/playwright/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Escribe un test que abra una página local y compruebe un título.

**Qué comprobar:** Puedes distinguir fallo de aserción y fallo de arranque del navegador.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un formulario
- Crear regresiones de una web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un formulario; Crear regresiones de una web | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP es el proyecto compañero playwright-mcp y el CLI otra superficie; instala la ruta adecuada en lugar de confundir biblioteca, skill y servidor

## Stack y modelos

- **Stack:** Node; navegadores descargados; aplicación de prueba
- **Etiquetas:** `automation` `browser` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |
| [crawlee](crawlee.md) | 26.4k | Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Puppeteer](puppeteer.md) | 95.8k | Librería de Google para controlar Chrome y Firefox desde Node.js. |
| [Selenium](selenium.md) | 34.6k | Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. |

## Enlaces

- 🐙 GitHub: [microsoft/playwright](https://github.com/microsoft/playwright)
- 🌐 Web: <https://playwright.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/playwright/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
