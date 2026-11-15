[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de research autónomo

# 🦌 deer-flow

> Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 85.2k | MIT | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Coordina tareas complejas delegando en agentes especializados.

## Por qué destaca

Orquestación potente y extensible; alcanzó gran visibilidad (#1 en GitHub Trending en su lanzamiento v2) y cuenta con el respaldo de ByteDance. Su diseño por skills lo hace ampliable sin tocar el núcleo.

## Cómo funciona

Un orquestador reparte sub-tareas a agentes con herramientas y sandbox, integrando memoria entre pasos; implementado en Python/TS sobre LangChain.

## Instalación rápida

`git clone` del repo y arranque con sus scripts (o Docker). Requiere claves de proveedor de LLM y, para el sandbox, Docker.

## Casos de uso

- Research profundo
- Tareas complejas multi-paso con herramientas
- Flujos extensibles vía skills propias

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un orquestador completo y extensible | buscas algo minimalista o sin Docker |

## Stack y modelos

- **Stack:** Python/TS, LangChain, Docker
- **Modelos / API:** Múltiples; agnóstico vía variables de entorno.
- **Etiquetas:** `automation` `research` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [gpt-researcher](gpt-researcher.md) | 30.6k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |
| [firecrawl](firecrawl.md) | 200k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |

## Enlaces

- 🐙 GitHub: [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
- 🌐 Web: <https://deerflow.tech>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
