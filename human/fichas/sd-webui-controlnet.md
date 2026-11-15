[🏠 Inicio](../README.md) › [🖼️ Generar imágenes y trabajar con visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Modelos, librerías y control

# 🧩 sd-webui-controlnet

> Extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI (AUTOMATIC1111), con preprocesadores para poses, bordes, profundidad y más.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.8k | GPL-3.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

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

Lleva el control composicional al flujo de trabajo habitual de la WebUI sin tocar código.

## Por qué destaca

Es la forma estándar de usar ControlNet dentro del ecosistema AUTOMATIC1111, con panel propio y soporte para múltiples unidades de control simultáneas; muy popular entre quienes ya viven en esa UI.

## Cómo funciona

Se instala como extensión de la WebUI y añade un panel que aplica modelos ControlNet sobre la difusión PyTorch+GPU del propio WebUI, encadenando preprocesador (genera el mapa) + modelo de control (inyecta la condición).

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/Mikubill/sd-webui-controlnet/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar sd-webui-controlnet para mi objetivo y necesito pasos guiados. Lee https://github.com/Mikubill/sd-webui-controlnet/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Afinar creativos en SD WebUI con poses/sketches/mapas
- Combinar varios ControlNet a la vez (pose + depth)
- Iterar composición sin salir de la UI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| ya usas SD WebUI y quieres ControlNet sin cambiar de entorno | trabajas en ComfyUI (usa sus propios nodos) o por código (diffusers) |

## Stack y modelos

- **Stack:** Python, SD WebUI (AUTOMATIC1111), modelos ControlNet
- **Etiquetas:** `vision` `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [stable-diffusion-webui](stable-diffusion-webui.md) | 165k | Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. |
| [ControlNet](controlnet.md) | 34.2k | Modelos que guían la generación de imágenes con poses, bordes, profundidad o segmentación. |

## Enlaces

- 🐙 GitHub: [Mikubill/sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Mikubill/sd-webui-controlnet/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
