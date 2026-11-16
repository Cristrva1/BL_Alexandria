[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Operar, evaluar y medir modelos de IA

Servidores de inferencia, gateways, evaluación, trazas y control de contexto. Cada pieza cubre una etapa: ejecutar el modelo, observarlo o comprobar la calidad de sus respuestas.

26 repos · 3 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [vLLM](../fichas/vllm.md) | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. | Sin clave propia de API de IA en la ruta básica |
| [headroom](../fichas/headroom.md) | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | API de IA opcional |
| [promptfoo](../fichas/promptfoo.md) | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. | API de IA opcional |

## Secciones

- [Serving y gateways de LLM](#serving-y-gateways-de-llm) — 11 repos
- [Ahorro de contexto y tokens](#ahorro-de-contexto-y-tokens) — 2 repos
- [Observabilidad, evaluación y guardrails](#observabilidad-evaluación-y-guardrails) — 13 repos

## Serving y gateways de LLM

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [vLLM](../fichas/vllm.md) | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. | Tu objetivo encaja con estos ejemplos: Servir un modelo propio; Estudiar rendimiento de inferencia | Sin clave propia de API de IA en la ruta básica |
| [OmniRoute](../fichas/omniroute.md) | Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso. | Tu objetivo encaja con estos ejemplos: Centralizar proveedores de un agente; Comparar rutas y límites de consumo | API de IA opcional |
| [litellm](../fichas/litellm.md) | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. | Tu objetivo encaja con estos ejemplos: Unificar llamadas a varios modelos; Enrutar un agente por un gateway propio | API de IA opcional |
| [Ray](../fichas/ray.md) | Motor de cómputo distribuido para IA: escala Python de un portátil a un clúster, con bibliotecas para datos, entrenamiento, ajuste, RL y serving. | Tu objetivo encaja con estos ejemplos: paralelizar un procesamiento de datos o entrenamiento en varias máquinas; servir modelos con autoescalado mediante Ray Serve | Sin clave propia de API de IA en la ruta básica |
| [SGLang](../fichas/sglang.md) | Framework de servicio de alto rendimiento para LLM y modelos multimodales. | Tu objetivo encaja con estos ejemplos: Servir un modelo para una aplicación; Estudiar inferencia multimodal | Sin clave propia de API de IA en la ruta básica |
| [claude-code-router](../fichas/claude-code-router.md) | Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local. | Tu objetivo encaja con estos ejemplos: Comparar proveedores desde Claude Code; Organizar perfiles para Codex | Depende de la ruta elegida |
| [TensorRT-LLM](../fichas/tensorrt-llm.md) | Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de lenguaje con kernels y runtimes especializados. | Tu objetivo encaja con estos ejemplos: Optimizar inferencia en GPU propia; Estudiar kernels y runtimes de NVIDIA | Sin clave propia de API de IA en la ruta básica |
| [Xinference](../fichas/xinference.md) | Plataforma abierta de inferencia para modelos de lenguaje, visión, embeddings, reranking, imagen, audio y vídeo, con API compatible con OpenAI y varios motores. | Tu objetivo encaja con estos ejemplos: servir un LLM, un modelo de embeddings y uno de voz desde un mismo servidor; conectar Dify, LangChain o LlamaIndex a modelos propios | Sin clave propia de API de IA en la ruta básica |
| [BentoML](../fichas/bentoml.md) | Framework Python para convertir modelos y pipelines de IA en APIs de producción, con empaquetado en imágenes Docker y despliegue reproducible. | Tu objetivo encaja con estos ejemplos: publicar un modelo de Transformers como API REST; empaquetar un LLM servido con vLLM en una imagen desplegable | Sin clave propia de API de IA en la ruta básica |
| [GPUStack](../fichas/gpustack.md) | Gestor de clústeres de GPU para servir modelos de IA: configura vLLM, SGLang o TensorRT-LLM, expone APIs compatibles con OpenAI y aprovisiona instancias GPU. | Tu objetivo encaja con estos ejemplos: servir varios modelos en las GPU de tu laboratorio con una sola consola; dar a tu equipo claves de API compatibles con OpenAI sobre modelos propios | Sin clave propia de API de IA en la ruta básica |
| [backdoor](../fichas/backdoor.md) | Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code. | Tu objetivo encaja con estos ejemplos: Probar un backend local con Claude Code; Comparar proveedores compatibles | API de IA opcional |

## Ahorro de contexto y tokens

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [headroom](../fichas/headroom.md) | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | Tu objetivo encaja con estos ejemplos: Reducir salidas extensas de herramientas; Comparar una sesión con y sin compresión | API de IA opcional |
| [rtk](../fichas/rtk.md) | Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. | Tu objetivo encaja con estos ejemplos: Reducir salida repetitiva de comandos; Estudiar consumo de contexto por tarea | API de IA opcional |

## Observabilidad, evaluación y guardrails

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [promptfoo](../fichas/promptfoo.md) | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. | Tu objetivo encaja con estos ejemplos: Evaluar un prompt de soporte; Probar regresiones de un RAG | API de IA opcional |
| [langfuse](../fichas/langfuse.md) | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. | Tu objetivo encaja con estos ejemplos: Depurar un asistente; Comparar versiones de un prompt | API de IA opcional |
| [MLflow](../fichas/mlflow.md) | Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro. | Tu objetivo encaja con estos ejemplos: Registrar experimentos de ML; Añadir trazas a una app de IA | API de IA opcional |
| [loguru](../fichas/loguru.md) | Librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa. | Tu objetivo encaja con estos ejemplos: Depurar una automatización; Añadir logs legibles a una app | Sin clave propia de API de IA en la ruta básica |
| [Opik](../fichas/opik.md) | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. | Tu objetivo encaja con estos ejemplos: Depurar una cadena RAG; Revisar fallos con un agente de código | API de IA opcional |
| [DeepEval](../fichas/deepeval.md) | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. | Tu objetivo encaja con estos ejemplos: Detectar regresiones de un chatbot; Probar relevancia de respuestas RAG | API de IA opcional |
| [Ragas](../fichas/ragas.md) | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. | Tu objetivo encaja con estos ejemplos: Medir un RAG con datos controlados; Comparar versiones de una cadena | Depende de la ruta elegida |
| [LM Evaluation Harness](../fichas/lm-eval-harness.md) | Arnés estándar de EleutherAI para evaluar modelos de lenguaje en cientos de benchmarks académicos con backends Hugging Face, vLLM, SGLang o APIs. | Tu objetivo encaja con estos ejemplos: comparar un modelo ajustado con su base en MMLU, HellaSwag o GSM8K; reproducir resultados de tablas de clasificación con la misma configuración | API de IA opcional |
| [Phoenix](../fichas/phoenix.md) | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. | Tu objetivo encaja con estos ejemplos: Depurar una app con OpenTelemetry; Consultar trazas desde un agente | API de IA opcional |
| [Claude-Code-Usage-Monitor](../fichas/claude-code-usage-monitor.md) | Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible. | Tu objetivo encaja con estos ejemplos: Revisar el uso de una sesión; Estudiar alertas y proyecciones de cuota | Sin clave propia de API de IA en la ruta básica |
| [OpenLLMetry](../fichas/openllmetry.md) | Instrumentación abierta basada en OpenTelemetry para aplicaciones de LLM: traza llamadas a modelos, bases vectoriales y frameworks hacia tu backend de observabilidad. | Tu objetivo encaja con estos ejemplos: trazar llamadas a OpenAI, LangChain o Ollama en Grafana o Datadog; añadir observabilidad de LLM a una pila OpenTelemetry existente | Sin clave propia de API de IA en la ruta básica |
| [NeMo Guardrails](../fichas/guardrails.md) | Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales con LLM. | Tu objetivo encaja con estos ejemplos: Guiar un asistente de soporte; Evaluar controles de una app propia | Depende de la ruta elegida |
| [Helicone](../fichas/helicone.md) | Pasarela de IA y plataforma de observabilidad de LLM abierta: registra peticiones, costes y latencias, gestiona prompts y enruta a más de 100 modelos. | Tu objetivo encaja con estos ejemplos: ver coste y latencia de todas las llamadas a modelos de tu aplicación; versionar prompts y enrutar entre proveedores con reintentos | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
- [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md) — Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor.
- [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.
- [Agente de voz en tiempo real](../playbooks/agente-de-voz.md) — Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
