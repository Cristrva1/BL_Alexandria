[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🦗 crawlee

> Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.4k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

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

## Qué puedes hacer con él

Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos.

## Por qué destaca

Usos propuestos: Rastrear una documentación propia; Extraer datos de páginas con JavaScript.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |

## Enlaces

- 🐙 GitHub: [apify/crawlee](https://github.com/apify/crawlee)
- 🌐 Web: <https://crawlee.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/apify/crawlee/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
