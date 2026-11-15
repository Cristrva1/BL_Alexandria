[🏠 Inicio](../README.md) › [🎬 Audio, Voz & Video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🎞️ OpenCut

> Editor de video libre con línea de tiempo, alternativa a CapCut, que funciona en el navegador y procesa en tu equipo.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 98k | MIT | TypeScript | 2026-09-24 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## Qué es

OpenCut es un editor de video pensado como alternativa abierta a CapCut: privado (los videos no salen de tu dispositivo), sin funciones de pago y fácil de usar. Hoy se usa la versión clásica en opencut.app mientras el equipo reescribe el proyecto desde cero, con un núcleo en Rust para web, escritorio y móvil.

## Por qué destaca

Cubre lo básico de CapCut sin muros de pago ni subir tus videos a un servidor. La reescritura anuncia API de editor, plugins de terceros, modo headless para render por lotes y servidor MCP para agentes.

## Cómo funciona

La versión clásica es una app Next.js con un núcleo Rust compilado a WebAssembly para composición en GPU, efectos y máscaras. La nueva arquitectura comparte ese núcleo Rust entre navegador, escritorio y móvil, en un monorepo gestionado con moon.

## Instalación rápida

Úsalo directamente en opencut.app (versión clásica). Para la reescritura: instala proto, ejecuta `proto use` y `moon run web:dev`; la versión clásica se auto-hospeda con `docker compose up -d`.

## Casos de uso

- Editar reels y videos cortos sin pagar suscripción
- Montar clips con texto y música sin subirlos a la nube
- Auto-hospedar un editor web para tu equipo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un editor con línea de tiempo, libre y privado, como alternativa a CapCut | necesitas estabilidad o automatización hoy; para montar por código mira `moviepy` o `remotion`, y para cortes sin pérdida `lossless-cut` |

**Limitaciones:** Está en plena reescritura: el repo principal aún no es apto para producción y la versión clásica (opencut-classic) está archivada.

## Stack y modelos

- **Stack:** TypeScript, Rust, WebAssembly, Next.js
- **Modelos / API:** No usa LLM.
- **Etiquetas:** `video` `ui` `typescript` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LosslessCut](lossless-cut.md) | 45.9k | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. |
| [OBS Studio](obs-studio.md) | 79.3k | App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real. |
| [whisperX](whisperx.md) | 25.2k | Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |

## Enlaces

- 🐙 GitHub: [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)
- 🌐 Web: <https://opencut.app>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
