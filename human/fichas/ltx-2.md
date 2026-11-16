[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🧩 LTX-2

> Código oficial de inferencia y entrenamiento LoRA de LTX-2 y LTX-2.5, modelo DiT de Lightricks que genera vídeo con audio sincronizado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.3k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## ¿Qué es?

Paquete oficial de inferencia y entrenador LoRA de Lightricks para el modelo audio-vídeo LTX-2, que alberga también LTX-2.5. El código es Apache-2.0 y los modelos tienen licencias propias. El README de LTX-Video (retirado del catálogo) lo indica como sucesor.

## ¿Qué hace?

Genera vídeo con audio sincronizado a partir de texto o imagen con un único modelo DiT, con modos de rendimiento (pipeline destilado rápido y ruta DFR de calidad de producción), IC-LoRA para control y entrenamiento de LoRA propios. Incluye integración con ComfyUI.

## ¿Cómo lo hace?

Se clona el repositorio y se instalan sus paquetes Python (el extra `natten`, más rápido, solo en Linux con CUDA). Los pesos y VAE se descargan de Hugging Face; para poca memoria documenta cuantización fp8 y descarga a CPU o disco. Necesita una GPU NVIDIA con mucha VRAM para resultados razonables.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ComfyUI](comfyui.md) | El README documenta la integración con ComfyUI para usar LTX-2 en flujos de nodos. | Instala ComfyUI y los nodos de LTX; después descarga los pesos indicados. |
| [FFmpeg](ffmpeg.md) | Los clips generados se concatenan, recodifican o mezclan con FFmpeg para su publicación (combinación por arquitectura). | Genera los clips; después procésalos con FFmpeg. |
| [PyTorch](pytorch.md) | Los pipelines de LTX-2 se ejecutan sobre PyTorch con CUDA. | Instala PyTorch con la versión de CUDA de tu GPU; después las dependencias de LTX-2. |

**Notas:** Revisa las licencias de los pesos antes de uso comercial.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v1.6.2 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Lightricks/LTX-2/blob/main/README.md) · [2](https://huggingface.co/Lightricks/LTX-2.5)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.

1. Elige el modelo y el backend que documenta el proyecto para tu sistema.
2. Prepara las dependencias y los pesos; no uses una cifra promocional como garantía para tu hardware.
3. Procesa una muestra pequeña y revisa calidad, tiempo y memoria antes de aumentar el tamaño de la tarea.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Lightricks/LTX-2/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LTX-2 para mi objetivo y necesito pasos guiados. Lee https://github.com/Lightricks/LTX-2/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona el repositorio, instala las dependencias, descarga los pesos de LTX-2.5 y ejecuta la DistilledPipeline con un prompt corto..

**Qué comprobar:** Se genera un clip de vídeo con audio en la carpeta de salida sin agotar la VRAM..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- generar clips cortos con audio a partir de texto o una imagen en una GPU propia
- entrenar un LoRA de estilo o personaje para el modelo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: generar clips cortos con audio a partir de texto o una imagen en una GPU propia; entrenar un LoRA de estilo o personaje para el modelo | no tienes el hardware o no aceptas la licencia de los pesos |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. El código es Apache-2.0, pero los pesos usan las licencias LTX-2 Community (no OSI) y el codificador Gemma 3 la licencia de Google.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `video` `python` `model` `local`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2)
- 🌐 Web: <https://ltx.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Lightricks/LTX-2/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
