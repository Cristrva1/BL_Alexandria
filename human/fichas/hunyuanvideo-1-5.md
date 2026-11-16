[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🧩 HunyuanVideo 1.5

> Modelo de video de Tencent de 8,3B parámetros que genera clips desde texto o imagen en 480p y 720p con GPU de 14 GB o más.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.6k | Tencent Hunyuan Community License | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## ¿Qué es?

Modelo de generación de video de Tencent Hunyuan, publicado en noviembre de 2025 con código de inferencia y entrenamiento en Python. Usa la Tencent Hunyuan Community License (GitHub muestra NOASSERTION), que no se aplica en la UE, el Reino Unido ni Corea del Sur. ~4,6k estrellas; último push en abril de 2026.

## ¿Qué hace?

Genera video a partir de texto (T2V) o de imagen (I2V) en 480p y 720p, con superresolución a 1080p. Ofrece variantes destiladas (CFG y por pasos) y caché de características para acelerar la inferencia. Sucede a HunyuanVideo (13B) con un modelo más ligero.

## ¿Cómo lo hace?

Combina un Diffusion Transformer de 8,3B parámetros y un VAE causal 3D. Requiere Linux, Python 3.10 o superior y una GPU NVIDIA con CUDA: al menos 14 GB de VRAM con offloading. Se instala desde `requirements.txt`, con Flash Attention, SageAttention o flex-block-attn opcionales, y pesos de Hugging Face. Hay integraciones oficiales en ComfyUI y Diffusers. La reescritura de prompts usa un endpoint vLLM opcional.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ComfyUI](comfyui.md) | ComfyUI soporta HunyuanVideo 1.5 de forma nativa con flujos de trabajo y optimizaciones; el README lo enlaza. | Instala ComfyUI, descarga los pesos y carga un flujo de ejemplo. |
| [WanGP](wan2gp.md) | Wan2GP soporta Hunyuan Video 1.5 con poca VRAM (desde unos 6 GB, según el README del modelo). | Usa Wan2GP si tu GPU no llega a 14 GB. |
| [vLLM](vllm.md) | El pipeline reescribe los prompts contra un servidor vLLM (Qwen3 recomendado) si se configuran `T2V_REWRITE_BASE_URL` e `I2V_REWRITE_BASE_URL`. | Levanta vLLM aparte y exporta las variables antes de generar. |

**Notas:** Alternativas (elige una): hunyuanvideo, wan2-2. Revisa la exclusión territorial y la política de uso aceptable antes de usarlo en un producto.

Estado en GitHub: activo · último push 2026-04-10 · última versión publicada sin releases en GitHub · licencia declarada Tencent Hunyuan Community License (GitHub: NOASSERTION) (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/README.md) · [2](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La reescritura de prompts usa un endpoint vLLM opcional; si no se configura, el pipeline genera sin reescritura remota. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Inferencia local con pesos descargados de Hugging Face, sujeta a la Tencent Hunyuan Community License. |
| Coste | El coste depende del proveedor o la ruta. Sin pago por llamada en la ruta local; consume GPU. La licencia excluye la UE, el Reino Unido y Corea del Sur. |
| Equipo | GPU o infraestructura especializada. GPU NVIDIA con CUDA y al menos 14 GB de VRAM con offloading; Linux y Python 3.10 o superior. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.

1. Confirma que tu país no está excluido por la licencia y que tienes Linux, CUDA y al menos 14 GB de VRAM.
2. Instala las dependencias y descarga los pesos según checkpoints-download.md; ComfyUI y Diffusers son rutas alternativas.
3. Genera un clip corto en 480p con offloading activado y mide tiempo y memoria antes de subir a 720p.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/checkpoints-download.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar HunyuanVideo 1.5 para mi objetivo y necesito pasos guiados. Lee https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera un clip de pocos segundos en 480p con offloading activado.

**Qué comprobar:** El video se guarda y anotas tiempo y VRAM usados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Generar un clip corto desde texto con GPU de consumo
- Animar una imagen fija en 480p

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Generar un clip corto desde texto con GPU de consumo; Animar una imagen fija en 480p | no tienes una GPU NVIDIA con memoria suficiente o te afecta la exclusión territorial de la licencia |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Licencia comunitaria de Tencent con exclusión territorial (UE, Reino Unido, Corea del Sur) y política de uso aceptable.

## Stack y modelos

- **Stack:** Python, requirements.txt
- **Etiquetas:** `video` `inference` `local` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [HunyuanVideo](hunyuanvideo.md) | 12.8k | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. |
| [Wan2.2](wan2-2.md) | 18.7k | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0. |

## Enlaces

- 🐙 GitHub: [Tencent-Hunyuan/HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5)
- 🌐 Web: <https://hunyuan.tencent.com/video/zh?tabIndex=0>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
