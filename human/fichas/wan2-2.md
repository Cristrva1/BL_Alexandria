[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 Wan2.2

> Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.7k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

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

## Qué puedes hacer con él

Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y licencia Apache 2.0.

## Por qué destaca

Usos propuestos: Prototipar una escena desde texto; Animar una imagen propia con un modelo local.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 147k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |
| [diffusers](diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. |
| [Real-ESRGAN](real-esrgan.md) | 37.5k | Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible generación de detalles nuevos. |
| [CosyVoice](cosyvoice.md) | 24.4k | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [HunyuanVideo](hunyuanvideo.md) | 12.8k | Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de inferencia. |

## Enlaces

- 🐙 GitHub: [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2)
- 🌐 Web: <https://wan.video>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
