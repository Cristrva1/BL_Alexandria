[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Modelos, librerías y control

# 🤗 diffusers

> Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 34.9k | Apache-2.0 | Python | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

## Qué es

Es la capa de abstracción que unifica el zoo de modelos de difusión bajo una misma interfaz Python.

## Por qué destaca

Es el estándar de facto para usar difusión programáticamente, mantenido por Hugging Face y con soporte inmediato para los modelos más nuevos (SDXL, Flux, SD3, video). Su adopción es masiva: casi cualquier proyecto de difusión en Python la usa como base.

## Cómo funciona

Carga modelos open-source desde el Hub y ejecuta su inferencia sobre PyTorch+GPU (o alternativas como Flax/Diffusers-ONNX) mediante clases `Pipeline` componibles; cada paso (scheduler, VAE, U-Net/transformer) es intercambiable.

## Instalación rápida

`pip install diffusers transformers accelerate`; los pesos se descargan automáticamente desde el Hub al instanciar un pipeline. Requiere GPU para uso práctico (aunque corre en CPU, muy lento) y espacio en disco para los pesos.

## Casos de uso

- Generación/transformación visual desde scripts propios
- Base reutilizable para apps y servicios
- Experimentación con schedulers y modelos nuevos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| programas generación y quieres control total por código | quieres una UI lista (Fooocus) o grafos nodales (ComfyUI) |

**Limitaciones:** GPU prácticamente obligatoria para latencia razonable; gestionar versiones de pesos y dependencias puede romper pipelines entre releases.

## Stack y modelos

- **Stack:** Python, PyTorch, Hugging Face Hub
- **Modelos / API:** Modelos open-source (local/self-host), agnóstico del proveedor.
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ControlNet](controlnet.md) | 34.2k | Modelos que guían la generación de imágenes con poses, bordes, profundidad o segmentación. |
| [cosmos](cosmos.md) | 12.3k | Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots. |

## Enlaces

- 🐙 GitHub: [huggingface/diffusers](https://github.com/huggingface/diffusers)
- 🌐 Web: <https://huggingface.co/docs/diffusers>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
