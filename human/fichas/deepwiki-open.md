[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧬 DeepWiki Open

> Generador de wikis con IA para repos de GitHub, GitLab o Bitbucket, versión abierta de DeepWiki.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 18.4k | MIT | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

Analiza un repositorio y crea documentación navegable con diagramas y un chat para preguntar sobre el código.

## Por qué destaca

Documentación automática con diagramas Mermaid y opción de modelos locales.

## Cómo funciona

Clona el repo, crea embeddings del código y genera páginas y diagramas con el LLM; un chat usa RAG sobre el código.

## Instalación rápida

`docker compose up` con tus claves de API en `.env`.

## Casos de uso

- Documentar un repo heredado
- Onboarding de nuevos desarrolladores
- Preguntar sobre código ajeno

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres documentación automática de un repositorio | necesitas contexto de librerías externas; mira `context7` |

## Stack y modelos

- **Stack:** Python, Next.js
- **Modelos / API:** OpenAI, Gemini, Ollama y otros.
- **Etiquetas:** `code` `docs` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Context7](context7.md) | 64.5k | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. |

## Enlaces

- 🐙 GitHub: [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open)
- 🌐 Web: <https://grok-wiki.com/>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
