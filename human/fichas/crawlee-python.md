[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🦗 crawlee-python

> Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.7k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Versión en Python de Crawlee, la librería de scraping y automatización de navegadores de Apify. Licencia Apache-2.0. Es activa (~10k estrellas, v1.11.2).

## ¿Qué hace?

Ofrece cola de URLs, reintentos, almacenamiento, proxies y sesiones con varios crawlers, entre ellos uno HTTP con BeautifulSoup y otro de navegador con Playwright. Intenta parecer humano por defecto. Tiene tipado completo y estilo asíncrono.

## ¿Cómo lo hace?

Se instala con `pip install 'crawlee[all]'` y `playwright install` para los navegadores, o se crea un proyecto con `uvx 'crawlee[cli]' create my-crawler`. Se ejecuta en local o en Apify.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [playwright](playwright.md) | Crawler de navegador soportado de forma nativa. | Instala los navegadores con `playwright install` y usa `PlaywrightCrawler`. |
| [Scrapegraph-ai](scrapegraph-ai.md) | Extraer datos con LLM a partir de las páginas recogidas. (combinación por arquitectura) | Recoge con Crawlee y pasa el HTML a ScrapeGraphAI. |
| [Qdrant](qdrant.md) | Indexar el contenido rastreado para RAG. (combinación por arquitectura) | Trocea y vectoriza los resultados y guárdalos en Qdrant. |
| [FlareSolverr](flaresolverr.md) | Combinación recíproca: FlareSolverr lo enlaza como «Un crawler HTTP de Crawlee puede obtener de FlareSolverr las cookies de un sitio autorizado antes de continuar (combinación por arquitectura)». | Orden indicado desde FlareSolverr: Despliega FlareSolverr; después usa sus cookies en las peticiones de Crawlee. |
| [Camoufox](camoufox.md) | Combinación recíproca: Camoufox lo enlaza como «Crawlee para Python documenta un ejemplo de PlaywrightCrawler con Camoufox». | Orden indicado desde Camoufox: Instala `crawlee[playwright]` y Camoufox; después pasa Camoufox como navegador del crawler. |

**Notas:** Sin alternativas declaradas. Se quita la combinación con scrapy por ser frameworks equivalentes. Respeta los términos de uso y robots.txt de cada sitio y la normativa de datos personales.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.11.2 (2026-11-10) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/apify/crawlee-python/blob/master/README.md) · [2](https://crawlee.dev/python/docs/quick-start)</sub>

## Ver similares

Grupo **Crawlee (Node.js y Python)**: crawlee-python ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **crawlee-python** (esta ficha) ⭐ recomendado | 66 | Si buscas esto: versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python. |
| 2 | [crawlee](crawlee.md) | 65 | Si buscas esto: framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El crawling básico no necesita LLM; la extracción con Pydantic AI o Stagehand y proveedores externos puede costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. No atribuyas las necesidades de los módulos de IA a la ruta básica de scraping |
| Coste | El coste depende del proveedor o la ruta. El crawling básico no necesita LLM; la extracción con Pydantic AI o Stagehand y proveedores externos puede costar |
| Equipo | Preparación según la ruta elegida. Python; entorno virtual; navegador si eliges Playwright |

No atribuyas las necesidades de los módulos de IA a la ruta básica de scraping

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- entorno virtual
- navegador si eliges Playwright

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
python -m pip install 'crawlee[all]'
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/apify/crawlee-python/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar crawlee-python para mi objetivo y necesito pasos guiados. Lee https://github.com/apify/crawlee-python/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Recoge enlaces de tres páginas con una cola acotada y guarda sus títulos.

**Qué comprobar:** Se controlan duplicados y obtienes los tres registros esperados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Recopilar documentos públicos
- Crear un crawler con reintentos y exportación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Recopilar documentos públicos; Crear un crawler con reintentos y exportación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No atribuyas las necesidades de los módulos de IA a la ruta básica de scraping

## Stack y modelos

- **Stack:** Python; entorno virtual; navegador si eliges Playwright
- **Etiquetas:** `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [apify/crawlee-python](https://github.com/apify/crawlee-python)
- 🌐 Web: <https://crawlee.dev/python/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/apify/crawlee-python/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
