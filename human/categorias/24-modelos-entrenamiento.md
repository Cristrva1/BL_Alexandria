[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Modelos abiertos y entrenamiento

Modelos, bibliotecas de entrenamiento y ajuste fino. Revisa la licencia de los pesos, la memoria necesaria y la opción de inferencia antes de descargar o entrenar.

14 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Unsloth](../fichas/unsloth.md) | App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales. | API de IA opcional |
| [TimesFM](../fichas/timesfm.md) | Modelos preentrenados de Google para pronóstico de series temporales; las licencias de los pesos cambian por versión. | API de IA opcional |

## Secciones

- [Entrenar y afinar modelos](#entrenar-y-afinar-modelos) — 8 repos
- [Modelos abiertos y fundacionales](#modelos-abiertos-y-fundacionales) — 6 repos

## Entrenar y afinar modelos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Unsloth](../fichas/unsloth.md) | App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales. | Tu objetivo encaja con estos ejemplos: Probar inferencia local; Preparar un ajuste fino pequeño | API de IA opcional |
| [tensorflow](../fichas/tensorflow.md) | Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entornos. | Tu objetivo encaja con estos ejemplos: Aprender redes neuronales; Construir un clasificador educativo | Sin clave propia de API de IA en la ruta básica |
| [Transformers](../fichas/transformers.md) | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. | Tu objetivo encaja con estos ejemplos: Clasificar un texto localmente; Probar un modelo de visión | Sin clave propia de API de IA en la ruta básica |
| [PyTorch](../fichas/pytorch.md) | Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU. | Tu objetivo encaja con estos ejemplos: Aprender tensores; Entrenar una red educativa | Sin clave propia de API de IA en la ruta básica |
| [LLaMA-Factory](../fichas/llama-factory.md) | Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código. | Tu objetivo encaja con estos ejemplos: Ajustar un modelo con ejemplos propios; Comparar un adaptador antes de exportarlo | Sin clave propia de API de IA en la ruta básica |
| [PEFT](../fichas/peft.md) | Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA. | Tu objetivo encaja con estos ejemplos: Ajustar un modelo con menos parámetros; Reutilizar un adaptador entrenado | Sin clave propia de API de IA en la ruta básica |
| [TRL](../fichas/trl.md) | Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más. | Tu objetivo encaja con estos ejemplos: Aprender ajuste supervisado; Estudiar DPO o GRPO | Sin clave propia de API de IA en la ruta básica |
| [bionemo-recipes](../fichas/bionemo-recipes.md) | Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala. | Tu objetivo encaja con estos ejemplos: Estudiar modelos de secuencias biológicas; Reproducir un entrenamiento de investigación | Sin clave propia de API de IA en la ruta básica |

## Modelos abiertos y fundacionales

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [TimesFM](../fichas/timesfm.md) | Modelos preentrenados de Google para pronóstico de series temporales; las licencias de los pesos cambian por versión. | Tu objetivo encaja con estos ejemplos: Estudiar demanda con series temporales; Comparar un baseline de pronóstico | API de IA opcional |
| [DeepSeek-V3](../fichas/deepseek-v3.md) | Modelo de lenguaje abierto de DeepSeek (671B parámetros, MoE) para chat, código y razonamiento; se usa por su API compatible con OpenAI o en servidores con varias GPU. | Tu objetivo encaja con estos ejemplos: Conectar un modelo abierto potente a un agente mediante la API de DeepSeek; Estudiar cómo se sirve un modelo MoE grande con vLLM o SGLang | API de IA opcional |
| [laya](../fichas/laya.md) | Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados. | Tu objetivo encaja con estos ejemplos: Clasificar consultas por intención; Elegir una opción estructurada | Sin clave propia de API de IA en la ruta básica |
| [cosmos](../fichas/cosmos.md) | Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots. | Tu objetivo encaja con estos ejemplos: Explorar datos sintéticos para robótica; Estudiar generación de escenas físicas | API de IA opcional |
| [Nemotron (NVIDIA)](../fichas/nemotron.md) | Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos. | Tu objetivo encaja con estos ejemplos: Explorar modelos abiertos de NVIDIA; Preparar un pipeline guiado de adaptación | API de IA opcional |
| [Kimi K2.7 Code](../fichas/kimi-k2-7-code.md) | Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos oficiales se publican en Hugging Face. | Tu objetivo encaja con estos ejemplos: Comparar generación de código; Estudiar uso de herramientas con un modelo abierto | API de IA opcional |

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
