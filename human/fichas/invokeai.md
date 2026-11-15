[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Interfaces para generar imágenes

# 🖌️ InvokeAI

> Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29.1k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve la fragmentación de herramientas SD reuniendo generación, edición y control en una sola app self-hosted.

## Por qué destaca

Ofrece la experiencia creativa más estable del ecosistema SD, con un canvas tipo Photoshop (capas, máscaras, regiones) y respaldo de una empresa dedicada (InvokeAI Inc.) que mantiene releases regulares.

## Cómo funciona

Un backend Python/PyTorch ejecuta los modelos de difusión sobre GPU y sirve una SPA (React/TypeScript) con lienzo editable; los workflows se guardan como grafos reproducibles y los modelos se gestionan desde la propia app.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/invoke-ai/InvokeAI/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar InvokeAI para mi objetivo y necesito pasos guiados. Lee https://github.com/invoke-ai/InvokeAI/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/invoke-ai/InvokeAI/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
