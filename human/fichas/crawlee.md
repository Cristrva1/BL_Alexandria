[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🦗 crawlee

> Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.4k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Librería de web scraping y automatización de navegadores para Node.js, de Apify. Licencia Apache-2.0. Es madura y activa (~26k estrellas, v3.18.2).

## ¿Qué hace?

Cubre el crawling de principio a fin: cola de URLs, reintentos, almacenamiento de resultados, rotación de proxies y gestión de sesiones. Trabaja con HTTP plano (Cheerio, JSDOM) o con navegadores (Playwright, Puppeteer) con la misma interfaz. Por defecto intenta parecer humano para evitar protecciones antibots.

## ¿Cómo lo hace?

Requiere Node.js 22.13+; se crea un proyecto con `npx crawlee create my-crawler` o se instala con `npm install crawlee playwright`. Se ejecuta en local o en la plataforma Apify. Es TypeScript.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [playwright](playwright.md) | Crawler de navegador basado en Playwright, soportado de forma nativa. | Instala `crawlee` y `playwright` y usa `PlaywrightCrawler`. |
| [defuddle](defuddle.md) | Limpiar el contenido principal de cada página en el mismo proyecto Node.js. (combinación por arquitectura) | Pasa el HTML de cada página a Defuddle. |
| [llm-scraper](llm-scraper.md) | Extraer datos estructurados con un LLM de las páginas que abre Crawlee. (combinación por arquitectura) | Pasa la página de Playwright a LLM Scraper con un esquema Zod. |
| [awesome-web-scraping](awesome-web-scraping.md) | Combinación recíproca: awesome-web-scraping lo enlaza como «Opción moderna para JavaScript/TypeScript. (combinación por arquitectura)». | Orden indicado desde awesome-web-scraping: Compárala con las demás de la sección de JavaScript. |
| [Camoufox](camoufox.md) | Combinación recíproca: Camoufox lo enlaza como «Crawlee para Node.js incluye una guía para evitar bloqueos usando Camoufox con su PlaywrightCrawler». | Orden indicado desde Camoufox: Instala `camoufox` y Crawlee; después configura el lanzador de Camoufox en el crawler. |

**Notas:** Sin alternativas declaradas. Respeta los términos de uso y robots.txt de cada sitio y la normativa de datos personales.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.18.2 (2026-09-29) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/apify/crawlee/blob/master/README.md) · [2](https://crawlee.dev/js/docs/quick-start)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca no exige IA ni Apify Cloud; proxies y alojamiento son opcionales de pago |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El generador ofrece plantillas; elige HTTP para HTML sencillo y navegador cuando sea necesario |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca no exige IA ni Apify Cloud; proxies y alojamiento son opcionales de pago |
| Equipo | Preparación según la ruta elegida. Node.js >=22.13; npm; navegador si eliges Playwright |

El generador ofrece plantillas; elige HTTP para HTML sencillo y navegador cuando sea necesario

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js >=22.13
- npm
- navegador si eliges Playwright

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npx crawlee create my-crawler
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/apify/crawlee/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar crawlee para mi objetivo y necesito pasos guiados. Lee https://github.com/apify/crawlee/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un crawler con límite pequeño y recoge títulos de tres páginas de prueba.

**Qué comprobar:** La cola termina y guarda un registro por página.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Rastrear una documentación propia
- Extraer datos de páginas con JavaScript

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Rastrear una documentación propia; Extraer datos de páginas con JavaScript | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El generador ofrece plantillas; elige HTTP para HTML sencillo y navegador cuando sea necesario

## Stack y modelos

- **Stack:** Node.js >=22.13; npm; navegador si eliges Playwright
- **Etiquetas:** `scraping` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [apify/crawlee](https://github.com/apify/crawlee)
- 🌐 Web: <https://crawlee.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/apify/crawlee/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
