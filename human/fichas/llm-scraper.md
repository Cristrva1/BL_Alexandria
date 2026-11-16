[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Scraping guiado por LLM

# 🧾 llm-scraper

> Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Librería TypeScript para extraer datos estructurados de cualquier página web con LLM, de @mishushakov. Licencia MIT. Es estable (~7k estrellas, sin releases) y su versión 2.0 usa el Vercel AI SDK 6.

## ¿Qué hace?

Define un esquema (Zod o JSON Schema) y obtén datos tipados de una página abierta con Playwright. Admite modelos GPT, Claude, Gemini, Llama y Qwen, varios modos de formato (HTML, Markdown, texto, imagen) y streaming.

## ¿Cómo lo hace?

Se instala con `npm i zod playwright llm-scraper` y el proveedor del AI SDK que prefieras (`@ai-sdk/openai`, `@ai-sdk/anthropic`, `ollama-ai-provider-v2`…). Requiere Node.js y navegadores de Playwright.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [playwright](playwright.md) | Abre y controla la página que se analiza. | Instala Playwright y sus navegadores. |
| [AI SDK (Vercel)](vercel-ai.md) | Proveedores de modelos mediante el AI SDK 6. | Instala el paquete de proveedor del AI SDK correspondiente. |
| [Ollama](ollama.md) | Modelos locales mediante `ollama-ai-provider-v2`, documentado en el README. | Levanta Ollama e instala el proveedor. |

**Notas:** Alternativas (elige una): maxun. Se quita la combinación con firecrawl por no estar documentada. Respeta los términos de uso y robots.txt de cada sitio y la normativa de datos personales.

Estado en GitHub: activo · último push 2026-10-26 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mishushakov/llm-scraper/blob/main/README.md) · [2](https://ai-sdk.dev/docs/introduction)</sub>

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
