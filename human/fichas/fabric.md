[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Prompts y prompt engineering

# 💡 Fabric

> CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 44.6k | MIT | Go | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Qué es

Organiza prompts reutilizables (patterns) para tareas como resumir videos, extraer ideas o analizar textos. Se encadena con pipes en la terminal.

## Por qué destaca

Biblioteca comunitaria de patrones muy cuidada y uso cómodo con pipes de Unix.

## Cómo funciona

Un binario Go envía el texto de entrada junto con el pattern elegido al proveedor LLM configurado.

## Instalación rápida

`go install github.com/danielmiessler/fabric/cmd/fabric@latest` y luego `fabric --setup`.

## Casos de uso

- Resumir transcripciones de YouTube
- Extraer ideas clave de artículos
- Prompts reutilizables en scripts

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres prompts reutilizables desde la terminal | buscas solo una lista de prompts para copiar; mira `prompts-chat` |

## Stack y modelos

- **Stack:** Go, Markdown
- **Modelos / API:** Agnóstico: OpenAI, Anthropic, Ollama y otros.
- **Etiquetas:** `prompts` `automation` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [yt-dlp](yt-dlp.md) | 207k | Descargador de audio y video por línea de comandos compatible con miles de sitios. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [prompts.chat](prompts-chat.md) | 177k | La colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts), auto-hospedable. |

## Enlaces

- 🐙 GitHub: [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric)
- 🌐 Web: <https://danielmiessler.com/p/fabric-origin-story>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
