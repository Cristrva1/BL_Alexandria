[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🕷️ Jina Reader

> Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.3k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Puntuación de calidad** 52/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Reader, de Jina AI: convierte cualquier URL en entrada apta para LLM y busca en la web. Licencia Apache-2.0. Es popular (~12k estrellas, sin releases) y el código abierto se resincronizó con el SaaS en abril de 2026 sin la capa de almacenamiento.

## ¿Qué hace?

Con `https://r.jina.ai/<url>` devuelve el contenido limpio en Markdown, y con `https://s.jina.ai/<consulta>` busca y devuelve los primeros resultados ya leídos. Sirve para agentes y RAG que necesitan leer páginas sin escribir un scraper. El servicio alojado tiene límites de uso y opciones con clave.

## ¿Cómo lo hace?

Se usa directamente por HTTP o se autoaloja con la imagen `ghcr.io/jina-ai/reader:oss` (Docker, modo sin estado). Algunos artefactos no redistribuibles en `licensed/` son necesarios para compilar o ejecutar, según el README.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Activepieces tiene una pieza oficial `jina-ai` para usar Jina Reader en flujos. | Jina Reader en marcha con sus credenciales; después añade la pieza `jina-ai` en un flujo de Activepieces. |
| [Open WebUI](open-webui.md) | Usar Jina como proveedor de búsqueda web en Open WebUI, documentado en su guía. | Activa la búsqueda web en Open WebUI y elige Jina con tu clave. |
| [LlamaIndex](llama-index.md) | Cargar el texto limpio de URLs en índices de LlamaIndex. (combinación por arquitectura) | Llama a r.jina.ai y crea documentos con la respuesta. |

**Notas:** Alternativas (elige una): firecrawl, crawl4ai.

Estado en GitHub: activo · último push 2026-05-22 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/jina-ai/reader/blob/main/README.md) · [2](https://docs.openwebui.com/features/chat-conversations/web-search/providers/jina) · [3](https://github.com/activepieces/activepieces/tree/main/packages/pieces/community/jina-ai)</sub>

## Ver similares

Grupo **Crawlers que entregan contenido listo para LLM**: Jina Reader ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [crawl4ai](crawl4ai.md) ⭐ recomendado | 72 | Si buscas esto: librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. |
| 2 | [firecrawl](firecrawl.md) | 71 | Si buscas esto: plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |
| 3 | **Jina Reader** (esta ficha) | 52 | Si buscas esto: servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El servicio público tiene cupos y modalidades con clave; self-hosting usa recursos y puede necesitar activos con licencia propia |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El contenedor básico no tiene caché ni control de tasa; localhost usa el puerto HTTP/1.1 del ejemplo |
| Coste | El coste depende del proveedor o la ruta. El servicio público tiene cupos y modalidades con clave; self-hosting usa recursos y puede necesitar activos con licencia propia |
| Equipo | Preparación según la ruta elegida. Navegador para servicio público; Docker solo para self-hosting |

El contenedor básico no tiene caché ni control de tasa; localhost usa el puerto HTTP/1.1 del ejemplo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador para servicio público
- Docker solo para self-hosting

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
docker run --rm -p 3000:8081 ghcr.io/jina-ai/reader:oss
# then: curl http://localhost:3000/https://example.com
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/jina-ai/reader/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Jina Reader para mi objetivo y necesito pasos guiados. Lee https://github.com/jina-ai/reader/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Antepon r.jina.ai a una URL pública y compara el texto devuelto con la página.

**Qué comprobar:** Obtienes contenido legible con su dirección de origen.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Convertir un artículo a texto para consulta
- Preparar una página para un índice documental

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Convertir un artículo a texto para consulta; Preparar una página para un índice documental | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El contenedor básico no tiene caché ni control de tasa; localhost usa el puerto HTTP/1.1 del ejemplo

## Stack y modelos

- **Stack:** Navegador para servicio público; Docker solo para self-hosting
- **Etiquetas:** `scraping` `rag` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [firecrawl](firecrawl.md) | 202k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |
| [crawl4ai](crawl4ai.md) | 87.4k | Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. |

## Enlaces

- 🐙 GitHub: [jina-ai/reader](https://github.com/jina-ai/reader)
- 🌐 Web: <https://jina.ai/reader>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jina-ai/reader/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
