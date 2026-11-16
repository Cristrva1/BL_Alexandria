[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 Wan2.2

> Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.7k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Wan2.2, familia de modelos abiertos de generación de vídeo de Alibaba (Wan-AI). Licencia Apache-2.0 para los modelos; no reclaman derechos sobre el contenido generado. Tiene ~19k estrellas (sin releases) y su último cambio es de septiembre de 2026.

## ¿Qué hace?

Genera vídeo desde texto, imagen o ambos con una arquitectura Mixture-of-Experts para la difusión. Incluye un modelo híbrido TI2V de 5B con un VAE de alta compresión que genera 720p en una GPU de consumo, además de Wan2.2-S2V (vídeo guiado por audio) y Wan2.2-Animate (animación y sustitución de personajes).

## ¿Cómo lo hace?

Se instala con `pip install -r requirements.txt` y se descargan los pesos de Hugging Face o ModelScope. Los modelos 14B requieren unos 80 GB de VRAM (o varias GPU); el TI2V-5B funciona con 24 GB (RTX 4090) con offloading. S2V puede sintetizar la voz con CosyVoice.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ComfyUI](comfyui.md) | Integración oficial en ComfyUI. | Sigue el tutorial de Wan2.2 en la documentación de Comfy. |
| [diffusers](diffusers.md) | T2V, I2V, TI2V y Animate integrados en diffusers. | Usa los checkpoints `-Diffusers` de Hugging Face. |
| [CosyVoice](cosyvoice.md) | Síntesis de voz para Speech-to-Video. | Instala `requirements_s2v.txt`. |
| [Real-ESRGAN](real-esrgan.md) | Ampliar los vídeos generados. (combinación por arquitectura) | Pasa los fotogramas por Real-ESRGAN. |
| [WanGP](wan2gp.md) | Combinación recíproca: WanGP lo enlaza como «Ejecuta los modelos Wan 2.2 con menos VRAM». | Orden indicado desde WanGP: Descarga el modelo desde la interfaz. |

**Notas:** Alternativas (elige una): hunyuanvideo, hunyuanvideo-1-5.

Estado en GitHub: activo · último push 2026-09-21 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Wan-Video/Wan2.2/blob/main/README.md) · [2](https://docs.comfy.org/tutorials/video/wan/wan2_2) · [3](https://huggingface.co/docs/diffusers/main/en/api/pipelines/wan)</sub>

## Ver similares

Grupo **Modelos abiertos de video generativo**: Wan2.2 ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Wan2.2** (esta ficha) ⭐ recomendado | 67 | Si buscas esto: familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. |
| 2 | [HunyuanVideo](hunyuanvideo.md) | 54 | Si buscas esto: modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. |
| 3 | [HunyuanVideo 1.5](hunyuanvideo-1-5.md) | 41 | Si buscas esto: modelo de video de Tencent de 8,3B parámetros que genera clips desde texto o imagen en 480p y 720p con GPU de 14 GB o más. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Inferencia local usa hardware; expansión de prompts puede llamar DashScope; pesos y descargas tienen licencias propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El ejemplo 5B cita al menos 24 GB VRAM; otros ejemplos 14B citan 80 GB; no extrapoles esos mínimos a interfaces optimizadas de terceros |
| Coste | El coste depende del proveedor o la ruta. Inferencia local usa hardware; expansión de prompts puede llamar DashScope; pesos y descargas tienen licencias propias |
| Equipo | Preparación según la ruta elegida. Python y PyTorch >=2.4; GPU; pesos y disco según variante |

El ejemplo 5B cita al menos 24 GB VRAM; otros ejemplos 14B citan 80 GB; no extrapoles esos mínimos a interfaces optimizadas de terceros

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y PyTorch >=2.4
- GPU
- pesos y disco según variante

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
git clone https://github.com/Wan-Video/Wan2.2.git
cd Wan2.2

# Ensure torch >= 2.4.0
# If the installation of `flash_attn` fails, try installing the other packages first and install `flash_attn` last
pip install -r requirements.txt
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Wan2.2 para mi objetivo y necesito pasos guiados. Lee https://github.com/Wan-Video/Wan2.2/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige primero el modelo TI2V-5B y la ruta de memoria documentada y genera un clip breve.

**Qué comprobar:** Puedes identificar pesos, tamaño, duración y recursos de la ejecución.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar una escena desde texto
- Animar una imagen propia con un modelo local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar una escena desde texto; Animar una imagen propia con un modelo local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El ejemplo 5B cita al menos 24 GB VRAM; otros ejemplos 14B citan 80 GB; no extrapoles esos mínimos a interfaces optimizadas de terceros

## Stack y modelos

- **Stack:** Python y PyTorch >=2.4; GPU; pesos y disco según variante
- **Etiquetas:** `video` `inference` `local` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [HunyuanVideo](hunyuanvideo.md) | 12.8k | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. |
| [HunyuanVideo 1.5](hunyuanvideo-1-5.md) | 4.6k | Modelo de video de Tencent de 8,3B parámetros que genera clips desde texto o imagen en 480p y 720p con GPU de 14 GB o más. |

## Enlaces

- 🐙 GitHub: [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2)
- 🌐 Web: <https://wan.video>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
