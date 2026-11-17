[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 📚 Colly

> Framework de scraping y crawling para Go: callbacks por selector, límites por dominio, caché, cookies y ejecución paralela.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.6k | Apache-2.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de scraping de código abierto (Apache-2.0) para Go, mantenida por la comunidad gocolly. Madura y estable en su versión v2; actividad moderada.

## ¿Qué hace?

Facilita escribir crawlers, scrapers y spiders que extraen datos estructurados para minería, procesamiento o archivo. Ofrece más de mil peticiones por segundo en un núcleo según el README, retardos y concurrencia máxima por dominio, cookies y sesiones automáticas, ejecución síncrona, asíncrona o paralela, caché y conversión de codificaciones.

## ¿Cómo lo hace?

Se usa como módulo Go (`github.com/gocolly/colly/v2`) con callbacks `OnHTML`, `OnRequest` y `OnResponse`; incluye ejemplos en `_examples`. No ejecuta JavaScript: para páginas dinámicas se necesita un navegador aparte.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | Los resultados que Colly escribe en CSV o JSON se pueden consultar directamente con DuckDB (combinación por arquitectura). | Ejecuta el crawler para generar archivos; después consúltalos con DuckDB. |
| [Polars](polars.md) | Polars carga y limpia los datos extraídos por Colly para analizarlos (combinación por arquitectura). | Exporta a CSV o JSON; después procésalos con Polars. |
| [Claude Code](claude-code.md) | Un agente de código puede escribir y ajustar los callbacks del crawler en Go a partir de la estructura de una página (combinación por arquitectura). | Proyecto Go con Colly; después pide al agente el extractor y pruébalo con pocas páginas. |

**Notas:** Alternativas cercanas en el catálogo: scrapy (Python), crawlee (Node/Python).

Estado en GitHub: activo · último push 2026-10-16 · última versión publicada v2.2.0 (2025-03-27) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/gocolly/colly/blob/master/README.md) · [2](https://pkg.go.dev/github.com/gocolly/colly/v2)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/gocolly/colly/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Colly para mi objetivo y necesito pasos guiados. Lee https://github.com/gocolly/colly/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un módulo Go, añade Colly v2 y ejecuta uno de los ejemplos del repositorio contra un sitio de prueba..

**Qué comprobar:** El programa visita las páginas y escribe los campos extraídos en la salida..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- escribir un rastreador rápido que extraiga datos estructurados de un sitio
- archivar páginas de un dominio respetando límites de velocidad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: escribir un rastreador rápido que extraiga datos estructurados de un sitio; archivar páginas de un dominio respetando límites de velocidad | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Respeta robots.txt y los términos de cada sitio al rastrear.

## Stack y modelos

- **Stack:** Go, go.mod
- **Etiquetas:** `scraping` `go` `library`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [gocolly/colly](https://github.com/gocolly/colly)
- 🌐 Web: <https://go-colly.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/gocolly/colly/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
