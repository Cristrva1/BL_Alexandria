[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 HunyuanVideo

> Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.8k | Tencent Hunyuan Community License | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** Tencent Hunyuan Community License. No aplica en la UE, Reino Unido ni Corea del Sur; límites de uso comercial. Fuente: [LICENSE](https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/LICENSE.txt). GitHub la marca como NOASSERTION.

## ¿Qué es?

HunyuanVideo, modelo abierto de generación de vídeo de 13B parámetros de Tencent Hunyuan. Usa la Tencent Hunyuan Community License, que excluye expresamente la UE, Reino Unido y Corea del Sur (GitHub muestra NOASSERTION). Tiene ~13k estrellas y su sucesor es HunyuanVideo-1.5 (repositorio aparte, noviembre de 2025).

## ¿Qué hace?

Genera vídeo a partir de texto con un transformer de difusión y ofrece inferencia en varias GPU, pesos FP8 y modelos derivados (I2V, Avatar, Custom). Es la base de varias implementaciones de la comunidad.

## ¿Cómo lo hace?

Se instala con PyTorch para CUDA, `requirements.txt` y, opcionalmente, flash-attention y xDiT para paralelismo. Requiere GPU con mucha memoria; existen versiones optimizadas de la comunidad para menos VRAM.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [diffusers](diffusers.md) | Pipeline de HunyuanVideo en diffusers. | Usa el pipeline `HunyuanVideoPipeline`. |
| [ComfyUI](comfyui.md) | Soporte nativo en ComfyUI. | Carga los pesos y usa el flujo de ejemplo. |
| [WanGP](wan2gp.md) | Interfaz para GPU modestas con soporte de Hunyuan Video. | Selecciona Hunyuan Video en WanGP. |

**Notas:** Alternativas (elige una): wan2-2, hunyuanvideo-1-5. La licencia no aplica en la UE, Reino Unido ni Corea del Sur; para proyectos nuevos valora HunyuanVideo-1.5.

Estado en GitHub: activo · último push 2026-10-08 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md) · [2](https://huggingface.co/docs/diffusers/main/api/pipelines/hunyuan_video) · [3](https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video)</sub>

## Ver similares

Grupo **Modelos abiertos de video generativo**: HunyuanVideo ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Wan2.2](wan2-2.md) ⭐ recomendado | 67 | Si buscas esto: familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. |
| 2 | **HunyuanVideo** (esta ficha) | 57 | Si buscas esto: modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. |
| 3 | [HunyuanVideo 1.5](hunyuanvideo-1-5.md) | 41 | Si buscas esto: modelo de video de Tencent de 8,3B parámetros que genera clips desde texto o imagen en 480p y 720p con GPU de 14 GB o más. |

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

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10.9 y PyTorch según ruta
- GPU grande
- pesos y licencia

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker pull hunyuanvideo/hunyuanvideo:cuda_12
```

Comando copiado literalmente de el README (sección «Installation Guide for Linux»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

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

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Wan2.2](wan2-2.md) | 18.7k | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. |
| [HunyuanVideo 1.5](hunyuanvideo-1-5.md) | 4.6k | Modelo de video de Tencent de 8,3B parámetros que genera clips desde texto o imagen en 480p y 720p con GPU de 14 GB o más. |

## Enlaces

- 🐙 GitHub: [Tencent-Hunyuan/HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo)
- 🌐 Web: <https://aivideo.hunyuan.tencent.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
