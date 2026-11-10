[🏠 Inicio](../README.md) › [🕷️ Scraping, Búsqueda & Research Web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# 🔍 SearXNG

> Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 39.4k | AGPL-3.0 | Python | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Qué es

Combina resultados de más de 70 servicios sin rastrearte. Muchos agentes de investigación lo usan como API de búsqueda gratuita y propia.

## Por qué destaca

Buscador auto-hospedado sin coste por consulta, con salida JSON para agentes.

## Cómo funciona

Envía tu consulta a varios motores, combina y ordena los resultados y los devuelve en HTML o JSON.

## Instalación rápida

`docker run -d -p 8080:8080 searxng/searxng` y habilita el formato JSON en `settings.yml`.

## Casos de uso

- Búsqueda para agentes sin pagar API
- Buscador privado del equipo
- Research con fuentes variadas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tus agentes necesitan buscar en la web sin coste por consulta | necesitas resultados con SLA comercial |

**Limitaciones:** Licencia AGPL-3.0; algunos motores pueden bloquear consultas masivas.

## Stack y modelos

- **Stack:** Python, Docker
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `search` `research` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [gpt-researcher](gpt-researcher.md) | 30.6k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |
| [Open WebUI](open-webui.md) | 158k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |
| [Vane](vane.md) | 38.1k | Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica). |

## Enlaces

- 🐙 GitHub: [searxng/searxng](https://github.com/searxng/searxng)
- 🌐 Web: <https://docs.searxng.org>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)
- 🧪 Receta: [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md)
- 🧪 Receta: [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
