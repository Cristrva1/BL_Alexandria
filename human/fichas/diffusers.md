[🏠 Inicio](../README.md) › [🖼️ Generar imágenes y trabajar con visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Modelos, librerías y control

# 🤗 diffusers

> Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 34.9k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

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

Es la capa de abstracción que unifica el zoo de modelos de difusión bajo una misma interfaz Python.

## Por qué destaca

Es el estándar de facto para usar difusión programáticamente, mantenido por Hugging Face y con soporte inmediato para los modelos más nuevos (SDXL, Flux, SD3, video). Su adopción es masiva: casi cualquier proyecto de difusión en Python la usa como base.

## Cómo funciona

Carga modelos open-source desde el Hub y ejecuta su inferencia sobre PyTorch+GPU (o alternativas como Flax/Diffusers-ONNX) mediante clases `Pipeline` componibles; cada paso (scheduler, VAE, U-Net/transformer) es intercambiable.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/huggingface/diffusers/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar diffusers para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/diffusers/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ControlNet](controlnet.md) | 34.2k | Modelos que guían la generación de imágenes con poses, bordes, profundidad o segmentación. |
| [cosmos](cosmos.md) | 12.4k | Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots. |

## Enlaces

- 🐙 GitHub: [huggingface/diffusers](https://github.com/huggingface/diffusers)
- 🌐 Web: <https://huggingface.co/docs/diffusers>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/huggingface/diffusers/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
