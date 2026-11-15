[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Scraping guiado por LLM

# 🧠 Maxun

> Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.4k | AGPL-3.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La extracción grabada no exige LLM; Cloud, proxies y modelos se pagan según ruta; Ollama sirve para funciones AI locales |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. MCP admite HTTP y stdio; la clave de Maxun autoriza el servicio y no sustituye credenciales de modelos |
| Coste | El coste depende del proveedor o la ruta. La extracción grabada no exige LLM; Cloud, proxies y modelos se pagan según ruta; Ollama sirve para funciones AI locales |
| Equipo | Preparación según la ruta elegida. Docker; cuenta local; modelo solo para funciones AI |

MCP admite HTTP y stdio; la clave de Maxun autoriza el servicio y no sustituye credenciales de modelos

## Qué puedes hacer con él

Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción.

## Por qué destaca

Usos propuestos: Convertir un listado en datos consultables; Monitorear cambios de un catálogo.

## Cómo funciona

MCP admite HTTP y stdio; la clave de Maxun autoriza el servicio y no sustituye credenciales de modelos

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- cuenta local
- modelo solo para funciones AI

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.maxun.dev/installation/docker)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Maxun para mi objetivo y necesito pasos guiados. Lee https://docs.maxun.dev/installation/docker. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Graba un robot que recoge nombres y precios de una página de prueba.

**Qué comprobar:** El robot devuelve filas que puedes repetir y comparar.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Convertir un listado en datos consultables
- Monitorear cambios de un catálogo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Convertir un listado en datos consultables; Monitorear cambios de un catálogo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP admite HTTP y stdio; la clave de Maxun autoriza el servicio y no sustituye credenciales de modelos

## Stack y modelos

- **Stack:** Docker; cuenta local; modelo solo para funciones AI
- **Etiquetas:** `scraping` `automation` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Scrapegraph-ai](scrapegraph-ai.md) | 32.8k | Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. |
| [llm-scraper](llm-scraper.md) | 7k | Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. |

## Enlaces

- 🐙 GitHub: [getmaxun/maxun](https://github.com/getmaxun/maxun)
- 🌐 Web: <https://www.maxun.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/getmaxun/maxun/blob/develop/README.md)
- [Fuente 2](https://docs.maxun.dev/mcp/setup)
- [Fuente 3](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
