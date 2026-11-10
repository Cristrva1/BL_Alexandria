[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Video programático y con agentes

# ⚛️ remotion

> Framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a MP4.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 72.2k | Otra (ver repo) | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Convierte el video en un artefacto versionable y parametrizable desde tu código frontend.

## Por qué destaca

Muy popular para generar video a escala y plantillas parametrizadas (uno de los proyectos de video-por-código más activos del ecosistema JS); permite crear miles de variantes cambiando props.

## Cómo funciona

Renderiza componentes React frame a frame con un navegador headless (Chromium) y los une con ffmpeg; las props alimentan las plantillas, y el reloj de Remotion sincroniza animaciones con el tiempo del video.

## Instalación rápida

`npm create video` (o `npm i remotion @remotion/cli`). Requiere Node y Chromium para render; el render final usa ffmpeg.

## Casos de uso

- Generar variantes de video a escala
- Plantillas de video programáticas para marketing
- Animaciones de datos sincronizadas con audio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| generas video a escala con React y quieres variantes parametrizadas | trabajas en Python (moviepy) o buscas un editor visual |

## Stack y modelos

- **Stack:** Node.js, React, Chromium, ffmpeg
- **Modelos / API:** N/A.
- **Etiquetas:** `video` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open-Generative-AI](open-generative-ai.md) | 33.8k | Plataforma alternativa libre a servicios premium de video/imagen que agrupa más de 200 modelos generativos accesibles desde terminal o integrados con agentes. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MoviePy](moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |
| [HyperFrames](hyperframes.md) | 82k | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. |

## Enlaces

- 🐙 GitHub: [remotion-dev/remotion](https://github.com/remotion-dev/remotion)
- 🌐 Web: <https://remotion.dev>
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
