[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🐍 scrapy

> Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 65.4k | BSD-3-Clause | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Framework de crawling y scraping rápido y de alto nivel para Python, mantenido por Zyte. Licencia BSD-3-Clause. Es el estándar veterano del sector (~65k estrellas, 2.20.0).

## ¿Qué hace?

Recorre sitios y extrae datos estructurados con spiders, selectores CSS y XPath, pipelines de procesamiento, middlewares, control de concurrencia y exportación a JSON, CSV u otros formatos. Sirve para minería de datos, monitorización y pruebas automatizadas. Tiene un ecosistema amplio de plugins.

## ¿Cómo lo hace?

Requiere Python 3.11+ y se instala con `pip install scrapy`; se crea un proyecto con `scrapy startproject`. Está basado en Twisted (asíncrono). Para páginas con JavaScript se usa el plugin oficial scrapy-playwright.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [playwright](playwright.md) | Renderizar páginas con JavaScript desde spiders con el plugin oficial scrapy-playwright. | Instala `scrapy-playwright` y los navegadores de Playwright, y activa su handler de descargas. |
| [Scrapling](scrapling.md) | Parser adaptativo para selectores frágiles. (combinación por arquitectura) | Usa Scrapling en los callbacks de tus spiders. |
| [defuddle](defuddle.md) | Extraer el contenido principal de artículos en un paso posterior. (combinación por arquitectura) | Procesa el HTML guardado con Defuddle. |
| [awesome-web-scraping](awesome-web-scraping.md) | Combinación recíproca: awesome-web-scraping lo enlaza como «Framework de referencia en la sección de Python. (combinación por arquitectura)». | Orden indicado desde awesome-web-scraping: Revisa la lista de Python y empieza por Scrapy si necesitas crawling clásico. |
| [FlareSolverr](flaresolverr.md) | Combinación recíproca: FlareSolverr lo enlaza como «Un spider de Scrapy puede pedir a FlareSolverr la página o las cookies de un sitio autorizado y continuar con peticiones normales (combinación por arquitectura)». | Orden indicado desde FlareSolverr: Despliega FlareSolverr; después llama a su API desde el spider o un middleware. |

**Notas:** Sin alternativas declaradas. Se quita la combinación con crawlee-python por ser frameworks equivalentes. Respeta los términos de uso y robots.txt de cada sitio y la normativa de datos personales.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada 2.20.0 (2026-11-06) · licencia declarada BSD-3-Clause (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/scrapy/scrapy/blob/master/README.rst) · [2](https://docs.scrapy.org/en/latest/) · [3](https://github.com/scrapy-plugins/scrapy-playwright)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere modelos; servidor, proxies y almacenamiento pueden generar gasto |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un framework de desarrollo, no una app de conversación ni una garantía de acceso a cualquier web |
| Coste | Sin pago a un modelo en la ruta básica. No requiere modelos; servidor, proxies y almacenamiento pueden generar gasto |
| Equipo | Preparación según la ruta elegida. Python 3.11+; entorno virtual; conocimientos básicos de selectores |

Es un framework de desarrollo, no una app de conversación ni una garantía de acceso a cualquier web

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.11+
- entorno virtual
- conocimientos básicos de selectores

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (shell):**

```
pip install scrapy
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/scrapy/scrapy/blob/master/README.rst)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar scrapy para mi objetivo y necesito pasos guiados. Lee https://github.com/scrapy/scrapy/blob/master/README.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un spider para una página propia con tres productos y exporta sus nombres.

**Qué comprobar:** El archivo de salida contiene exactamente los tres productos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Recopilar listados públicos permitidos
- Programar extracción repetible con pipelines

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Recopilar listados públicos permitidos; Programar extracción repetible con pipelines | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un framework de desarrollo, no una app de conversación ni una garantía de acceso a cualquier web

## Stack y modelos

- **Stack:** Python 3.11+; entorno virtual; conocimientos básicos de selectores
- **Etiquetas:** `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [scrapy/scrapy](https://github.com/scrapy/scrapy)
- 🌐 Web: <https://scrapy.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/scrapy/scrapy/blob/master/README.rst)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
