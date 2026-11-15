[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Interfaces para generar imágenes

# 🧠 ComfyUI

> Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 147k | GPL-3.0 | Python | 2026-06-23 |

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

Resuelve la composición de flujos de difusión complejos que una UI fija no permite.

## Por qué destaca

Es la referencia para flujos de difusión avanzados y reproducibles, con una comunidad enorme y un ecosistema de nodos/extensiones muy activo. Su autor (comfyanonymous) lo mantiene con foco en rendimiento y compatibilidad con los modelos más recientes (SDXL, Flux).

## Cómo funciona

Ejecuta modelos de difusión (Stable Diffusion, SDXL, Flux) sobre PyTorch+GPU, encadenando nodos en un grafo visual servido desde una interfaz web local que expone cada paso como bloque configurable.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python o una distribución preparada, modelos compatibles y hardware suficiente.

1. Elige la distribución para tu sistema y la ruta de CPU o GPU del README.
2. Prepara los pesos y el workflow de ejemplo correspondiente.
3. Genera una imagen pequeña y comprueba memoria, resultado y licencias de los modelos antes de ampliar el flujo.

[Instrucciones originales de instalación](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ComfyUI para mi objetivo y necesito pasos guiados. Lee https://github.com/Comfy-Org/ComfyUI/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Pipeline para generar/transformar/exportar imágenes de campaña
- Composición fina y repetible
- Flujos con ControlNet/IPAdapter encadenados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres control total y pipelines reproducibles | buscas simplicidad inmediata (Fooocus) |

**Limitaciones:** Requiere GPU con VRAM suficiente; los checkpoints pesan varios GB y la curva del grafo de nodos es empinada para nuevos.

## Stack y modelos

- **Stack:** Python, GPU, PyTorch, modelos locales
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Real-ESRGAN](real-esrgan.md) | 37.5k | Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [WanGP](wan2gp.md) | 11.8k | App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas. |
| [Stable Diffusion WebUI Forge](sd-webui-forge.md) | 13.1k | Versión optimizada de la WebUI de Stable Diffusion, más rápida y con menos memoria. |

## Enlaces

- 🐙 GitHub: [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
- 🌐 Web: <https://www.comfy.org/>
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
