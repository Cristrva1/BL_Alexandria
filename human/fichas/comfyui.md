[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Interfaces para generar imágenes

# 🧠 ComfyUI

> Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 147k | GPL-3.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## ¿Qué es?

ComfyUI, motor modular de creación con IA basado en grafos de nodos, mantenido por Comfy Org. Licencia GPL-3.0. Es uno de los proyectos de IA generativa más populares (~147k estrellas, v0.45.0).

## ¿Qué hace?

Permite construir flujos de generación y edición de imagen, vídeo, audio y 3D conectando nodos, con soporte nativo para modelos abiertos recientes (SD 1.5/SDXL/SD3.5, Flux.1/Flux.2, Qwen Image, Wan 2.1/2.2, LTX-Video, HunyuanVideo…). Carga checkpoints, VAE, LoRA, ControlNet y upscalers, y solo reejecuta las partes del grafo que cambian. Los «Partner nodes» opcionales dan acceso de pago a modelos cerrados.

## ¿Cómo lo hace?

Se usa con la app de escritorio (recomendada), la versión portable de Windows, `comfy-cli` o instalación manual con PyTorch para CUDA, ROCm, XPU o Apple Silicon. Funciona sin conexión; `--offline` desactiva los nodos de API de pago. El ecosistema de nodos personalizados es enorme, pero de calidad y seguridad variables.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FLUX.2](flux2.md) | Tutoriales oficiales de Comfy para FLUX.2. | Descarga los pesos de FLUX.2 y carga el flujo de ejemplo. |
| [Krita AI Diffusion](krita-ai-diffusion.md) | El plugin de Krita usa ComfyUI como backend. | Instala ComfyUI con las extensiones requeridas y conéctalo desde Krita. |
| [Real-ESRGAN](real-esrgan.md) | Cargar modelos ESRGAN como upscalers. | Copia los pesos en `models/upscale_models`. |
| [HunyuanVideo 1.5](hunyuanvideo-1-5.md) | ComfyUI soporta HunyuanVideo 1.5 de forma nativa con flujos de video de ejemplo. | Descarga los pesos de HunyuanVideo 1.5 y carga el flujo de ejemplo. |

**Notas:** Alternativas (elige una): wan2gp. Revisa los nodos personalizados antes de instalarlos: ejecutan código arbitrario.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.45.0 (2026-11-10) · licencia declarada GPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md) · [2](https://docs.comfy.org) · [3](https://docs.comfy.org/tutorials/flux/flux-2-dev)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta local usa tu equipo; Cloud y nodos API opcionales son de pago; los pesos tienen licencias propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El modo offline desactiva nodos API opcionales; importar un workflow puede exigir modelos o nodos adicionales |
| Coste | El coste depende del proveedor o la ruta. La ruta local usa tu equipo; Cloud y nodos API opcionales son de pago; los pesos tienen licencias propias |
| Equipo | Preparación según la ruta elegida. Python o distribución elegida; modelo; RAM y GPU según workflow |

El modo offline desactiva nodos API opcionales; importar un workflow puede exigir modelos o nodos adicionales

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python o distribución elegida
- modelo
- RAM y GPU según workflow

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install comfy-cli
comfy install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ComfyUI para mi objetivo y necesito pasos guiados. Lee https://github.com/Comfy-Org/ComfyUI/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga un workflow mínimo y conecta modelo, prompt, sampler y guardado.

**Qué comprobar:** Obtienes una imagen y puedes identificar los nodos que la produjeron.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un pipeline reproducible de imagen
- Comparar dos ajustes del mismo modelo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un pipeline reproducible de imagen; Comparar dos ajustes del mismo modelo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El modo offline desactiva nodos API opcionales; importar un workflow puede exigir modelos o nodos adicionales

## Stack y modelos

- **Stack:** Python o distribución elegida; modelo; RAM y GPU según workflow
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [WanGP](wan2gp.md) | 11.8k | App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas. |

## Enlaces

- 🐙 GitHub: [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
- 🌐 Web: <https://www.comfy.org/>
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Comfy-Org/ComfyUI/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
