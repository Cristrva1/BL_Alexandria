[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Navegadores y servidores de ejecución

# 📚 Camoufox

> Navegador basado en Firefox para scraping y agentes que genera una identidad de dispositivo coherente en cada arranque y se controla con Playwright.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.3k | MPL-2.0 (navegador) y MIT (paquetes de Python) | C | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Navegador antidetección de código abierto creado por daijro. El navegador es MPL-2.0 y los paquetes de lanzamiento de Python son MIT. Muy activo; el propio README avisa de que está en desarrollo.

## ¿Qué hace?

Lanza un Firefox modificado con una identidad de dispositivo distinta y coherente en cada arranque (pantalla, GPU, WebGL, fuentes, audio, geolocalización según el proxy), reportada de forma nativa en lugar de con sobrescrituras en JavaScript, y lo expone como navegador de Playwright.

## ¿Cómo lo hace?

Parchea el código de Firefox y usa el protocolo Juggler en un mundo aislado para que la página no detecte la automatización. El lanzador toma la identidad de un generador de huellas (fpgen) y la pasa al navegador. Hay paquetes para Python y para Node.js (`camoufox` con `playwright-core`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [playwright](playwright.md) | Camoufox se controla con Playwright: el lanzador devuelve un `Browser` de Playwright normal. | Instala Camoufox y descarga el navegador; después usa tu código de Playwright con el navegador que devuelve. |
| [crawlee-python](crawlee-python.md) | Crawlee para Python documenta un ejemplo de PlaywrightCrawler con Camoufox. | Instala `crawlee[playwright]` y Camoufox; después pasa Camoufox como navegador del crawler. |
| [crawlee](crawlee.md) | Crawlee para Node.js incluye una guía para evitar bloqueos usando Camoufox con su PlaywrightCrawler. | Instala `camoufox` y Crawlee; después configura el lanzador de Camoufox en el crawler. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v158.0.1-beta.41 (2026-10-29) · licencia declarada MPL-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/daijro/camoufox/blob/main/README.md) · [2](https://crawlee.dev/python/docs/examples/playwright-crawler-with-camoufox) · [3](https://github.com/apify/crawlee/blob/master/docs/guides/avoid-blocking-camoufox.ts)</sub>

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

**Entrada documentada (consulta la sintaxis original):**

```
pip install -U "camoufox[geoip]"
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/daijro/camoufox/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Camoufox para mi objetivo y necesito pasos guiados. Lee https://github.com/daijro/camoufox/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install -U "camoufox[geoip]"`, descarga el navegador con su comando `fetch` y abre una página con el ejemplo del README..

**Qué comprobar:** Obtienes un objeto `Browser` de Playwright normal controlando Camoufox..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- automatizar navegación en sitios propios o autorizados que bloquean navegadores headless
- probar cómo responde tu web a distintas huellas de navegador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: automatizar navegación en sitios propios o autorizados que bloquean navegadores headless; probar cómo responde tu web a distintas huellas de navegador | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Proyecto en desarrollo, no recomendado para producción estable. Falsear huellas para evadir detección puede violar los términos de servicio de los sitios.

## Stack y modelos

- **Stack:** C
- **Etiquetas:** `browser` `scraping` `firefox` `playwright`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [daijro/camoufox](https://github.com/daijro/camoufox)
- 🌐 Web: <https://camoufox.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/daijro/camoufox/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
