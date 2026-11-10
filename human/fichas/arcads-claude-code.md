[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Skills de dominio: marketing, SEO y negocio

# 📈 Arcads AI Video Skill Pack

> Pack de skills para Claude Code y Cursor que crea anuncios en video e imagen con la API de Arcads (Seedance, Sora, Veo, Kling).

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| — | — | — | — | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

> ⚠️ El repositorio original ya no está disponible en GitHub; se conserva el clon local.

## Qué es

Repo de trabajo que convierte Claude Code o Cursor en un estudio de anuncios: genera videos UGC, presentaciones de producto, lookbooks y miniaturas de YouTube con los modelos de Arcads, y anuncios estáticos para Meta con 37 plantillas. Incluye pipelines multipaso (estilo Pixar o plastilina con ffmpeg), subtitulado con Whisper y HyperFrames, y publicación como anuncios pausados en Meta.

## Por qué destaca

Trae fórmulas de prompt probadas para cada modelo, estimación de coste en créditos antes de cada generación y un log por llamada. Cubre del brief al anuncio subido a Meta sin salir del editor.

## Cómo funciona

Las skills de `skills/` y `shared/skills/` guían al agente para llamar a la API de Arcads, esperar el resultado y ordenar los archivos. Un hook SessionStart revisa `.env` y `MASTER_CONTEXT.md` y copia las skills a `.claude/` y `.cursor/`.

## Instalación rápida

`git clone https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial && cd arcads-claude-code-mrpaidsocial && ./scripts/setup.sh` (pide tu API key de Arcads); luego abre la carpeta en Claude Code o Cursor.

## Casos de uso

- Generar un video UGC de producto con Seedance 2.0
- Crear anuncios estáticos para Meta a partir de plantillas
- Clonar la estructura de un anuncio de referencia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| ya tienes cuenta de Arcads y quieres producir creatividades publicitarias desde Claude Code o Cursor | quieres generar video con modelos abiertos sin servicio de pago; mira `comfyui` u `openmontage` |

**Limitaciones:** Requiere cuenta de pago de Arcads (cada generación consume créditos) y el README promociona una comunidad de pago; los pipelines avanzados piden ffmpeg, jq y Node.

## Stack y modelos

- **Stack:** Python, Bash, ffmpeg, Node.js (HyperFrames), Whisper
- **Modelos / API:** Generación con la API de Arcads (Seedance 2.0, Sora 2, Veo 3.1, Kling 3.0, Nano Banana, GPT Image 2); el agente que orquesta es Claude Code o Cursor.
- **Etiquetas:** `video` `image` `skills` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [HyperFrames](hyperframes.md) | 82k | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. |
| [whisper](whisper.md) | 112k | Modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo. |
| [FFmpeg](ffmpeg.md) | 66.9k | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. |
| [Marketing Skills](marketingskills.md) | 59.5k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. |

## Enlaces

- 🐙 GitHub: [krusemediallc/arcads-claude-code](https://github.com/krusemediallc/arcads-claude-code)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
