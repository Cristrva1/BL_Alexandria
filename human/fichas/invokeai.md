[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Interfaces para generar imágenes

# 🖌️ InvokeAI

> Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 29.1k | Apache-2.0 | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado

## Qué es

Resuelve la fragmentación de herramientas SD reuniendo generación, edición y control en una sola app self-hosted.

## Por qué destaca

Ofrece la experiencia creativa más estable del ecosistema SD, con un canvas tipo Photoshop (capas, máscaras, regiones) y respaldo de una empresa dedicada (InvokeAI Inc.) que mantiene releases regulares.

## Cómo funciona

Un backend Python/PyTorch ejecuta los modelos de difusión sobre GPU y sirve una SPA (React/TypeScript) con lienzo editable; los workflows se guardan como grafos reproducibles y los modelos se gestionan desde la propia app.

## Instalación rápida

Instalador automático multiplataforma (launcher) o `pip install invokeai`; arranca un servidor web local tras configurar los modelos. Requiere GPU NVIDIA con VRAM generosa (8 GB+) y pesos de SD/SDXL descargados.

## Casos de uso

- Trabajo creativo serio con SD
- Canvas e inpainting profesional con regiones
- Iteración de campaña visual con workflows reutilizables

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas creatividad profesional y quieres una app estable con canvas | solo haces una prueba puntual (Fooocus) o prefieres grafos nodales (ComfyUI) |

**Limitaciones:** Setup pesado y exigente en VRAM; la curva de aprendizaje del canvas y los workflows es mayor que en alternativas más simples.

## Stack y modelos

- **Stack:** Python, PyTorch, React, TypeScript, Docker
- **Modelos / API:** Local-first (modelos de difusión open-source).
- **Etiquetas:** `image` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [diffusers](diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. |
| [ControlNet](controlnet.md) | 34.2k | Modelos que guían la generación de imágenes con poses, bordes, profundidad o segmentación. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Krita AI Diffusion](krita-ai-diffusion.md) | 10.9k | Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting. |

## Enlaces

- 🐙 GitHub: [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI)
- 🌐 Web: <https://invoke-ai.github.io/InvokeAI/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
