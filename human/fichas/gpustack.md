[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# ⚙️ GPUStack

> Gestor de clústeres de GPU para servir modelos de IA: configura vLLM, SGLang o TensorRT-LLM, expone APIs compatibles con OpenAI y aprovisiona instancias GPU.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Gestor de clústeres de GPU de código abierto (Apache-2.0) del equipo GPUStack (Seal). Activo.

## ¿Qué hace?

Configura y orquesta motores de inferencia en clústeres de GPU de varios fabricantes, con selección automática de motor y parámetros, claves de API, métricas, panel de administración e instancias GPU accesibles por SSH bajo demanda.

## ¿Cómo lo hace?

El servidor corre en Docker (también en CPU); los nodos trabajadores requieren Linux con driver NVIDIA, Docker y NVIDIA Container Toolkit, o los equivalentes de otros aceleradores.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | GPUStack configura vLLM como motor de inferencia. | Añade el nodo trabajador; después elige vLLM al desplegar. |
| [SGLang](sglang.md) | GPUStack configura SGLang como motor alternativo. | Elige SGLang como motor al desplegar el modelo. |
| [TensorRT-LLM](tensorrt-llm.md) | GPUStack configura TensorRT-LLM en GPU NVIDIA. | Elige TensorRT-LLM como motor en el despliegue. |

**Notas:** Cercano a xinference; GPUStack se centra en gestionar clústeres de GPU.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.3.1 (2026-11-11) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/gpustack/gpustack/blob/main/README.md) · [2](https://docs.gpustack.ai/latest/installation/requirements/)</sub>

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

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/gpustack/gpustack/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GPUStack para mi objetivo y necesito pasos guiados. Lee https://github.com/gpustack/gpustack/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la guía de instalación con Docker en un nodo con GPU NVIDIA, despliega un modelo pequeño y prueba la API con curl..

**Qué comprobar:** El modelo responde por el endpoint compatible con OpenAI..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- servir varios modelos en las GPU de tu laboratorio con una sola consola
- dar a tu equipo claves de API compatibles con OpenAI sobre modelos propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: servir varios modelos en las GPU de tu laboratorio con una sola consola; dar a tu equipo claves de API compatibles con OpenAI sobre modelos propios | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `serving` `python` `gpu` `self-hosted`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [gpustack/gpustack](https://github.com/gpustack/gpustack)
- 🌐 Web: <https://gpustack.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/gpustack/gpustack/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
