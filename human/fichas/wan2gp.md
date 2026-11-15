[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 WanGP

> App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.8k | NOASSERTION | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado · **MCP** 🔌 sí

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

WanGP, antes Wan2GP, es una interfaz web para ejecutar en tu GPU decenas de modelos generativos abiertos: video (Wan 2.1/2.2, LTX-2, Hunyuan Video), imagen (Flux, Qwen Image), voz y música (Chatterbox, Index TTS, Ace Step) y 3D. Añade cola de trabajos, LoRAs, galerías y un asistente local, Deepy, que planifica y lanza las generaciones por ti.

## Por qué destaca

Está pensado para quien no tiene una GPU de 80 GB: gestiona memoria y cuantización (int8, fp8, GGUF, NV FP4) para correr modelos con 4-8 GB de VRAM, también en GTX 10XX y AMD, y añade los modelos nuevos casi en cuanto salen.

## Cómo funciona

App Python con interfaz Gradio que descarga los pesos adecuados a tu hardware y aplica offloading con su librería mmgp. Ofrece modo headless por línea de comandos, API propia e interfaz MCP para agentes externos.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/deepbeepmeep/WanGP/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar WanGP para mi objetivo y necesito pasos guiados. Lee https://github.com/deepbeepmeep/WanGP/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Generar video con Wan o LTX en una GPU de 8-12 GB
- Probar modelos nuevos de imagen, voz o música en una sola interfaz
- Lanzar lotes de generación sin supervisión en modo headless

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres generar video e imagen con modelos abiertos en una GPU de consumo sin montar flujos a mano | prefieres construir flujos por nodos con control fino (`comfyui`) o tienes una GPU grande y quieres el código oficial (`wan2-2`) |

**Limitaciones:** Su licencia propia (WanGP Community License) permite el uso gratuito, también en empresas, pero prohíbe venderlo, integrarlo en productos de pago u ofrecerlo como SaaS sin licencia comercial.

## Stack y modelos

- **Stack:** Python, PyTorch, Gradio, Diffusers, mmgp
- **Etiquetas:** `video` `image` `tts` `local` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [MoviePy](moviepy.md) | 15.2k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |
| [LosslessCut](lossless-cut.md) | 46k | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 147k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Enlaces

- 🐙 GitHub: [deepbeepmeep/WanGP](https://github.com/deepbeepmeep/WanGP)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/deepbeepmeep/WanGP/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
