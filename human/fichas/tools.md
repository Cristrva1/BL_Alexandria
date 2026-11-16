[🏠 Inicio](../README.md)

# 🧰 tools

> Carpeta interna de herramientas auxiliares del hub; no es un producto para instalar.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| — | — | — | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

> 🧰 Carpeta interna del hub; no es un producto para instalar.

## ¿Qué es?

tools, entrada interna del hub BL_Alexandria que representa sus utilidades auxiliares de mantenimiento, no un proyecto externo. No tiene repositorio en GitHub ni licencia propia. En el repositorio actual estas utilidades están en `src/repo_intelligence/tools/` y `tools_check/`; no hay una carpeta `tools/` en la raíz.

## ¿Qué hace?

Los envoltorios de `src/repo_intelligence/tools/` llaman a herramientas externas para el análisis de repos: `crawl4ai_docs.py` (Crawl4AI para obtener Markdown de una URL), `markitdown_runner.py` (MarkItDown, con copia del README como respaldo), `repomix_runner.py` (empaqueta un repo con Repomix) y `gitnexus_runner.py` (`gitnexus analyze`). `tools_check/` verifica las guías heredadas que quedan en `guias/` (`check_guias.py`) y reconcilia los JSON con su contenido (`reconcile_json.py`); `Guia.md` lo genera `repo-intelligence guide build`.

## ¿Cómo lo hace?

Son scripts Python del propio repo que se ejecutan con `uv run` dentro del entorno del proyecto. Las herramientas externas (crawl4ai, markitdown, repomix, gitnexus) deben estar instaladas para que funcionen los envoltorios correspondientes. Sirven para mantener la biblioteca, no como dependencia de otros proyectos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [crawl4ai](crawl4ai.md) | Envoltorio `crawl4ai_docs.py` (AsyncWebCrawler). | Instala crawl4ai en el entorno del proyecto. |
| [markitdown](markitdown.md) | Envoltorio `markitdown_runner.py` (CLI markitdown). | Instala la CLI markitdown. |
| [Repomix](repomix.md) | Envoltorio `repomix_runner.py`. | Instala repomix (npm). |
| [GitNexus](gitnexus.md) | Envoltorio `gitnexus_runner.py`. | Instala la CLI gitnexus. |
| [Guía (histórica)](guia.md) | Combinación recíproca: Guía (histórica) lo enlaza como «Utilidades internas del hub que alimentan y verifican el índice del que se genera la guía». | Orden indicado desde Guía (histórica): Ambas vienen con el repositorio; no requieren instalación. |

**Notas:** Entrada local (categoría 0), excluida del recuento de cobertura. La ficha describía una carpeta `tools/` que ya no existe; se documentan las ubicaciones reales.

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Cristrva1/BL_Alexandria/tree/main/src/repo_intelligence/tools) · [2](https://github.com/Cristrva1/BL_Alexandria/tree/main/tools_check)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API: por confirmar. No se ha verificado si la ruta elegida necesita una API de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Ejecución con modelos locales por confirmar. Ejecutar el programa en tu equipo no demuestra que el modelo también sea local. |
| Coste | Coste por confirmar. Código disponible no significa servicios, modelos, infraestructura o licencias sin coste. |
| Equipo | Requisitos por confirmar. Consultar los requisitos originales de la variante que vayas a usar. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

No se instala: es parte de este repositorio.

## Casos de uso

- Mantenimiento interno de la biblioteca
- Referencia de utilidades
- Apoyo a los scripts del hub

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| mantienes esta biblioteca | buscas una herramienta para tu proyecto |

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `skills`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
