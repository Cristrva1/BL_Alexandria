[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Video programático y con agentes

# 🎞️ HyperFrames

> Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 82k | Apache-2.0 | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

HyperFrames define cada video como un archivo HTML con atributos de tiempo y pistas, animado con GSAP, CSS, Lottie, Three.js u otras librerías, y lo renderiza a MP4. Incluye CLI para crear, previsualizar y renderizar, un catálogo de unos 450 bloques (transiciones, subtítulos, gráficos, mapas) y skills para que Claude Code, Codex o Cursor produzcan videos a partir de una petición.

## Por qué destaca

Usa HTML plano en vez de React y licencia Apache 2.0 sin cuotas por render, a diferencia de Remotion. El render es determinista (misma entrada, mismos fotogramas), lo que encaja en CI y pipelines automáticos.

## Cómo funciona

El motor abre la composición en Chrome headless con Puppeteer, avanza fotograma a fotograma mediante adaptadores de animación con búsqueda temporal y codifica con FFmpeg mezclando el audio. Renderiza en local, en Docker o distribuido en AWS Lambda.

## Instalación rápida

`npx hyperframes init my-video`, luego `npx hyperframes preview` y `npx hyperframes render` (Node.js 22+ y FFmpeg). Para agentes: `npx hyperframes skills update`, o en Claude Code `claude plugin marketplace add heygen-com/hyperframes` y `claude plugin install hyperframes@hyperframes`.

## Casos de uso

- Videos de lanzamiento de producto generados por un agente
- Explicar un PR con diffs animados, narración y subtítulos
- Animaciones de datos y mapas para redes sociales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres que un agente de código genere videos con motion graphics a partir de HTML, con licencia permisiva | tu equipo ya trabaja con componentes React y el ecosistema de `remotion`, o prefieres editar en una línea de tiempo visual |

**Limitaciones:** Necesita Node.js 22+ y FFmpeg, el Studio todavía está evolucionando y los modelos generativos de HeyGen del plan Pro son de pago.

## Stack y modelos

- **Stack:** TypeScript, Node.js, Puppeteer, FFmpeg, GSAP
- **Modelos / API:** No llama a un LLM por sí mismo: lo opera tu agente de código (Claude Code, Codex, Cursor, Gemini CLI). El plan Pro del Studio añade modelos de video, voz y música de HeyGen.
- **Etiquetas:** `video` `agents` `skills` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 155k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [GSAP](gsap.md) | 30.4k | Librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincronizados sobre cualquier propiedad del DOM. |
| [Kokoro](kokoro.md) | 10k | Modelo de texto a voz de solo 82M parámetros con calidad alta y licencia Apache. |
| [whisperX](whisperx.md) | 25.2k | Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [remotion](remotion.md) | 72.2k | Framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a MP4. |
| [MoviePy](moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Enlaces

- 🐙 GitHub: [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)
- 🌐 Web: <https://hyperframes.heygen.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
