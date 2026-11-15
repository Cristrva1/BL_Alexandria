[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🕷️ Jina Reader

> Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.3k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

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

## Qué puedes hacer con él

Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai.

## Por qué destaca

Usos propuestos: Convertir un artículo a texto para consulta; Preparar una página para un índice documental.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |

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
