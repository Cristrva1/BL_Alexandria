[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🔥 firecrawl

> Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 202k | AGPL-3.0 | TypeScript | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

API para buscar, extraer e interactuar con la web a escala, pensada como «API de contexto» para agentes de IA, de Firecrawl. Licencia AGPL-3.0, con servicio alojado de pago. Es muy popular y activo (~202k estrellas, v2.11.0).

## ¿Qué hace?

Convierte sitios en Markdown limpio o JSON estructurado mediante scrape, crawl, map, search y extracción con LLM; también procesa PDF y DOCX, interactúa con páginas y monitoriza cambios. Ofrece SDK, CLI, skills y un servidor MCP (firecrawl-mcp) para conectarlo a agentes. Tiene integraciones oficiales con n8n, Zapier, Lovable y otros.

## ¿Cómo lo hace?

Se usa con la API alojada (clave de firecrawl.dev) o se autoaloja con Docker según la guía; la versión autoalojada no incluye todo: por ejemplo, el servicio «Alexandria» de proveedores de datos solo funciona en Firecrawl Cloud, y motores como Fire-engine se configuran aparte. Para agentes, `npx -y firecrawl-cli@latest init` instala CLI y skills, y el MCP se ejecuta con `npx -y firecrawl-mcp`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Activepieces tiene una pieza oficial `firecrawl` para usar firecrawl en flujos. | firecrawl en marcha con sus credenciales; después añade la pieza `firecrawl` en un flujo de Activepieces. |
| [Claude Code](claude-code.md) | Dar al agente scraping y búsqueda con el servidor MCP oficial firecrawl-mcp. | Añade `firecrawl-mcp` a la configuración MCP con tu clave. |
| [gpt-researcher](gpt-researcher.md) | Usar Firecrawl como scraper de GPT Researcher, documentado en su guía de scraping. | Define el scraper Firecrawl y su clave en la configuración de GPT Researcher. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (12). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[ai-engineering-hub](ai-engineering-hub.md) · [Awesome LLM Apps](awesome-llm-apps.md) · [awesome-web-scraping](awesome-web-scraping.md) · [CAMEL](camel.md) · [chatwoot](chatwoot.md) · [deer-flow](deer-flow.md) · [onyx](onyx.md) · [OpenBot](openbot.md) · [PDF Inspector](pdf-inspector.md) · [public-apis](public-apis.md) · [social-media-agent](social-media-agent.md) · [Stagehand](stagehand.md)

**Notas:** Alternativas (elige una): jina-reader. Se quita la combinación con crawl4ai por solaparse como crawler. Coincidencia de nombre: el producto «Alexandria» de Firecrawl no tiene relación con esta biblioteca. Respeta los términos de uso y robots.txt de cada sitio y la normativa de datos personales.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.11.0 (2026-06-19) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/firecrawl/firecrawl/blob/main/README.md) · [2](https://docs.firecrawl.dev/mcp-server) · [3](https://n8n.io/integrations/firecrawl/) · [4](https://docs.gptr.dev/docs/gpt-researcher/gptr/scraping) · [5](https://github.com/activepieces/activepieces/tree/main/packages/pieces/community/firecrawl)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta alojada consume créditos de Firecrawl; el agente tiene sus propios límites; self-hosting tiene infraestructura y funciones distintas |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Hay CLI, skill y MCP stdio; compatibilidad MCP no significa que la suscripción del cliente pague Firecrawl |
| Coste | El coste depende del proveedor o la ruta. La ruta alojada consume créditos de Firecrawl; el agente tiene sus propios límites; self-hosting tiene infraestructura y funciones distintas |
| Equipo | Preparación según la ruta elegida. Node.js; cuenta Firecrawl para la ruta alojada; cliente elegido |

Hay CLI, skill y MCP stdio; compatibilidad MCP no significa que la suscripción del cliente pague Firecrawl

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- cuenta Firecrawl para la ruta alojada
- cliente elegido

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx -y firecrawl-cli@latest init --all --browser
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/firecrawl/firecrawl/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar firecrawl para mi objetivo y necesito pasos guiados. Lee https://github.com/firecrawl/firecrawl/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Extrae título y contenido de una página pública de prueba y revisa el Markdown.

**Qué comprobar:** Se conserva el contenido principal con la URL de origen.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar páginas para un buscador documental
- Crear un mapa de URLs de una web propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar páginas para un buscador documental; Crear un mapa de URLs de una web propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Hay CLI, skill y MCP stdio; compatibilidad MCP no significa que la suscripción del cliente pague Firecrawl

## Stack y modelos

- **Stack:** Node.js; cuenta Firecrawl para la ruta alojada; cliente elegido
- **Etiquetas:** `scraping` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Jina Reader](jina-reader.md) | 12.3k | Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai. |

## Enlaces

- 🐙 GitHub: [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
- 🌐 Web: <https://firecrawl.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/firecrawl/firecrawl/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
