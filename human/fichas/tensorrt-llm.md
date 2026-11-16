[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# 🧬 TensorRT-LLM

> Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de lenguaje con kernels y runtimes especializados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.1k | NOASSERTION | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; requiere programar con él

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

TensorRT LLM, la librería de NVIDIA para optimizar inferencia de LLM y modelos de generación visual en GPU NVIDIA. Licencia Apache-2.0 según el README (GitHub muestra NOASSERTION). Es activa (~15k estrellas, v1.2.1).

## ¿Qué hace?

Ofrece kernels especializados, un runtime eficiente y una API de Python (LLM API) construida sobre PyTorch para servir modelos en una o varias GPU. Incluye cuantización, caché KV optimizada, decodificación especulativa y técnicas para MoE a gran escala. Sirve modelos con `trtllm-serve` mediante una API compatible con OpenAI.

## ¿Cómo lo hace?

Se instala con pip o con contenedores NGC y solo funciona en GPU NVIDIA con CUDA. Desde la versión 1.0 tiene política formal de deprecaciones. Recoge telemetría anónima por defecto (se desactiva automáticamente en CI; revisa la documentación para desactivarla).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | Enrutar a `trtllm-serve` como endpoint compatible con OpenAI. (combinación por arquitectura) | Lanza trtllm-serve y regístralo en LiteLLM. |
| [Open WebUI](open-webui.md) | Chat sobre modelos servidos con TensorRT LLM. (combinación por arquitectura) | Configura Open WebUI contra el endpoint de trtllm-serve. |
| [Transformers](transformers.md) | Partir de checkpoints de Hugging Face para optimizarlos. (combinación por arquitectura) | Descarga el modelo con Transformers/Hub y cárgalo en la LLM API. |
| [DeepSeek-V3](deepseek-v3.md) | Combinación recíproca: DeepSeek-V3 lo enlaza como «Soporte documentado para GPU NVIDIA». | Orden indicado desde DeepSeek-V3: Construye el motor con TensorRT-LLM. |
| [GPUStack](gpustack.md) | Combinación recíproca: GPUStack lo enlaza como «GPUStack configura TensorRT-LLM en GPU NVIDIA». | Orden indicado desde GPUStack: Elige TensorRT-LLM como motor en el despliegue. |

**Notas:** Sin alternativas declaradas. Recoge telemetría por defecto. Exclusivo de NVIDIA.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.2.1 (2026-04-20) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NVIDIA/TensorRT-LLM/blob/main/README.md) · [2](https://nvidia.github.io/TensorRT-LLM/) · [3](https://nvidia.github.io/TensorRT-LLM/commands/trtllm-serve/index.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere API de modelo remota; hardware, energía, nube y licencia del modelo son independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es infraestructura especializada y no una instalación universal para cualquier portátil o GPU |
| Coste | Sin pago a un modelo en la ruta básica. No requiere API de modelo remota; hardware, energía, nube y licencia del modelo son independientes |
| Equipo | Preparación según la ruta elegida. GPU NVIDIA compatible; CUDA y dependencias según versión; modelo soportado |

Es infraestructura especializada y no una instalación universal para cualquier portátil o GPU

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- GPU NVIDIA compatible
- CUDA y dependencias según versión
- modelo soportado

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://nvidia.github.io/TensorRT-LLM/installation/index.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar TensorRT-LLM para mi objetivo y necesito pasos guiados. Lee https://nvidia.github.io/TensorRT-LLM/installation/index.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Comprueba la matriz de hardware y ejecuta el ejemplo mínimo de inferencia antes de optimizar.

**Qué comprobar:** Puedes relacionar motor, modelo y configuración de memoria.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Optimizar inferencia en GPU propia
- Estudiar kernels y runtimes de NVIDIA

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Optimizar inferencia en GPU propia; Estudiar kernels y runtimes de NVIDIA | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es infraestructura especializada y no una instalación universal para cualquier portátil o GPU

## Stack y modelos

- **Stack:** GPU NVIDIA compatible; CUDA y dependencias según versión; modelo soportado
- **Etiquetas:** `serving` `blackwell` `cuda` `llm-serving` `moe` `pytorch` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)
- 🌐 Web: <https://nvidia.github.io/TensorRT-LLM>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NVIDIA/TensorRT-LLM/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
