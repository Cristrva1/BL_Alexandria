[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Interfaces para generar imágenes

# 🖼️ Krita AI Diffusion

> Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.9k | GPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Puntuación de calidad** 55/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Generative AI for Krita, plugin para usar IA generativa dentro de Krita, de @Acly (Interstice). Licencia GPL-3.0. Es maduro (~11k estrellas, v1.53.0).

## ¿Qué hace?

Integra generación, inpainting, outpainting, refinado, regiones, control por bocetos y poses, y upscaling en el flujo de pintura de Krita, con selección como máscara. Prioriza precisión y control sobre la generación por texto. Puede usar modelos propios en local o generación en la nube de pago.

## ¿Cómo lo hace?

Se instala como plugin de Krita desde la release y, desde el docker del plugin, se configura un servidor ComfyUI local gestionado o uno existente con las extensiones requeridas. En local necesita GPU NVIDIA con al menos 6 GB de VRAM (también admite AMD, Apple Silicon o CPU con menos rendimiento).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ComfyUI](comfyui.md) | Backend requerido del plugin. | Deja que el plugin instale ComfyUI o conecta uno con las extensiones listadas. |
| [FLUX.2](flux2.md) | Usar modelos FLUX en Krita a través de ComfyUI. (combinación por arquitectura) | Instala el modelo en ComfyUI y selecciónalo en el plugin. |
| [Real-ESRGAN](real-esrgan.md) | Upscaling en ComfyUI con modelos ESRGAN. (combinación por arquitectura) | Instala los modelos de upscale en ComfyUI. |

**Notas:** Alternativas (elige una): invokeai.

Estado en GitHub: activo · último push 2026-11-06 · última versión publicada v1.53.0 (2026-08-22) · licencia declarada GPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Acly/krita-ai-diffusion/blob/main/README.md) · [2](https://docs.interstice.cloud/installation) · [3](https://docs.interstice.cloud/comfyui-setup)</sub>

## Ver similares

Grupo **Interfaces de creación de imágenes**: Krita AI Diffusion ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [InvokeAI](invokeai.md) ⭐ recomendado | 73 | Si buscas esto: suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables. |
| 2 | **Krita AI Diffusion** (esta ficha) | 55 | Si buscas esto: plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El servidor local consume tu equipo; Cloud tiene condiciones propias; modelos y descargas se presupuestan según ruta |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El autor recomienda al menos 6 GB VRAM NVIDIA para local; CPU es posible pero muy lenta; revisa soporte del backend de tu GPU |
| Coste | El coste depende del proveedor o la ruta. El servidor local consume tu equipo; Cloud tiene condiciones propias; modelos y descargas se presupuestan según ruta |
| Equipo | Preparación según la ruta elegida. Krita compatible; plugin; servidor local o Cloud; GPU recomendada para local |

El autor recomienda al menos 6 GB VRAM NVIDIA para local; CPU es posible pero muy lenta; revisa soporte del backend de tu GPU

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Krita compatible
- plugin
- servidor local o Cloud
- GPU recomendada para local

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.interstice.cloud/installation)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Krita AI Diffusion para mi objetivo y necesito pasos guiados. Lee https://docs.interstice.cloud/installation. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Selecciona una región de una imagen propia y genera una modificación en otra capa.

**Qué comprobar:** Puedes aceptar o descartar la capa manteniendo el original.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Completar un fondo en una ilustración
- Usar un boceto para guiar una imagen

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Completar un fondo en una ilustración; Usar un boceto para guiar una imagen | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El autor recomienda al menos 6 GB VRAM NVIDIA para local; CPU es posible pero muy lenta; revisa soporte del backend de tu GPU

## Stack y modelos

- **Stack:** Krita compatible; plugin; servidor local o Cloud; GPU recomendada para local
- **Etiquetas:** `image` `design` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [InvokeAI](invokeai.md) | 29.1k | Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables. |

## Enlaces

- 🐙 GitHub: [Acly/krita-ai-diffusion](https://github.com/Acly/krita-ai-diffusion)
- 🌐 Web: <https://www.interstice.cloud>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Acly/krita-ai-diffusion/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
