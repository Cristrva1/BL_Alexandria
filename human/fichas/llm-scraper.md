[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Scraping guiado por LLM

# 🧾 llm-scraper

> Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El modelo puede ser Ollama local o un proveedor API; no es gratis por instalar la biblioteca |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Instala el adaptador del proveedor además de llm-scraper y descarga el navegador de Playwright |
| Coste | El coste depende del proveedor o la ruta. El modelo puede ser Ollama local o un proveedor API; no es gratis por instalar la biblioteca |
| Equipo | Preparación según la ruta elegida. Node.js; Playwright; esquema Zod; modelo elegido |

Instala el adaptador del proveedor además de llm-scraper y descarga el navegador de Playwright

## Qué puedes hacer con él

Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído.

## Por qué destaca

Usos propuestos: Extraer campos sin escribir selectores específicos; Normalizar información de páginas similares.

## Cómo funciona

Instala el adaptador del proveedor además de llm-scraper y descarga el navegador de Playwright

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- Playwright
- esquema Zod
- modelo elegido

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
npm i zod playwright llm-scraper
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mishushakov/llm-scraper/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar llm-scraper para mi objetivo y necesito pasos guiados. Lee https://github.com/mishushakov/llm-scraper/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Define nombre, precio y moneda y extrae un producto ficticio de una página de prueba.

**Qué comprobar:** El objeto respeta el esquema y coincide con la página.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Extraer campos sin escribir selectores específicos
- Normalizar información de páginas similares

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Extraer campos sin escribir selectores específicos; Normalizar información de páginas similares | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Instala el adaptador del proveedor además de llm-scraper y descarga el navegador de Playwright

## Stack y modelos

- **Stack:** Node.js; Playwright; esquema Zod; modelo elegido
- **Etiquetas:** `scraping` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| [firecrawl](firecrawl.md) | 202k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Maxun](maxun.md) | 18.4k | Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción. |

## Enlaces

- 🐙 GitHub: [mishushakov/llm-scraper](https://github.com/mishushakov/llm-scraper)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mishushakov/llm-scraper/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
