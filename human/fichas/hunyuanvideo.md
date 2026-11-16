[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 HunyuanVideo

> Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.8k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige API remota; hardware y almacenamiento son importantes y los pesos tienen licencia Hunyuan propia |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta original cita 45 GB VRAM para 544x960x129 y 60 GB para 720x1280x129; no es una instalación ligera para cualquier laptop |
| Coste | El coste depende del proveedor o la ruta. No exige API remota; hardware y almacenamiento son importantes y los pesos tienen licencia Hunyuan propia |
| Equipo | Preparación según la ruta elegida. Python 3.10.9 y PyTorch según ruta; GPU grande; pesos y licencia |

La ruta original cita 45 GB VRAM para 544x960x129 y 60 GB para 720x1280x129; no es una instalación ligera para cualquier laptop

## Qué puedes hacer con él

Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia.

## Por qué destaca

Usos propuestos: Estudiar generación local de video; Probar un prompt visual con pesos abiertos.

## Cómo funciona

La ruta original cita 45 GB VRAM para 544x960x129 y 60 GB para 720x1280x129; no es una instalación ligera para cualquier laptop

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10.9 y PyTorch según ruta
- GPU grande
- pesos y licencia

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar HunyuanVideo para mi objetivo y necesito pasos guiados. Lee https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Comprueba la resolución y memoria de la tabla antes de generar el ejemplo más pequeño viable.

**Qué comprobar:** El clip y sus recursos se pueden comparar con la configuración elegida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar generación local de video
- Probar un prompt visual con pesos abiertos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar generación local de video; Probar un prompt visual con pesos abiertos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La ruta original cita 45 GB VRAM para 544x960x129 y 60 GB para 720x1280x129; no es una instalación ligera para cualquier laptop

## Stack y modelos

- **Stack:** Python 3.10.9 y PyTorch según ruta; GPU grande; pesos y licencia
- **Etiquetas:** `video` `inference` `local` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 147k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |
| [diffusers](diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. |
| [Real-ESRGAN](real-esrgan.md) | 37.5k | Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible generación de detalles nuevos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Wan2.2](wan2-2.md) | 18.7k | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. |

## Enlaces

- 🐙 GitHub: [Tencent-Hunyuan/HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo)
- 🌐 Web: <https://aivideo.hunyuan.tencent.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
