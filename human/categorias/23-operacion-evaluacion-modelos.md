[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Operar, evaluar y medir modelos de IA

Servidores de inferencia, gateways, evaluación, trazas y control de contexto. Cada pieza cubre una etapa: ejecutar el modelo, observarlo o comprobar la calidad de sus respuestas.

19 repos · 3 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [vLLM](../fichas/vllm.md) | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. | Sin API de IA en la ruta básica |
| [headroom](../fichas/headroom.md) | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | API de IA opcional |
| [promptfoo](../fichas/promptfoo.md) | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. | Depende de la ruta elegida |

## Secciones

- [Serving y gateways de LLM](#serving-y-gateways-de-llm) — 7 repos
- [Ahorro de contexto y tokens](#ahorro-de-contexto-y-tokens) — 2 repos
- [Observabilidad, evaluación y guardrails](#observabilidad-evaluación-y-guardrails) — 10 repos

## Serving y gateways de LLM

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [vLLM](../fichas/vllm.md) | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. | necesitas servir LLM abiertos a muchos usuarios en GPU | Sin API de IA en la ruta básica |
| [OmniRoute](../fichas/omniroute.md) | Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso. | buscas esta función: Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso. | API de IA opcional |
| [litellm](../fichas/litellm.md) | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. | trabajas con múltiples modelos o quieres fallback/control de costos | Depende de la ruta elegida |
| [SGLang](../fichas/sglang.md) | Framework de servicio de alto rendimiento para LLM y modelos multimodales. | buscas el máximo rendimiento en servicio de LLM | Sin API de IA en la ruta básica |
| [claude-code-router](../fichas/claude-code-router.md) | Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local. | buscas esta función: Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local. | Depende de la ruta elegida |
| [TensorRT-LLM](../fichas/tensorrt-llm.md) | Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de lenguaje con kernels y runtimes especializados. | despliegas LLM en GPU NVIDIA y necesitas optimizar la inferencia | Sin API de IA en la ruta básica |
| [backdoor](../fichas/backdoor.md) | Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code. | quieres estudiar cómo conectar otros modelos al harness de Claude Code | Depende de la ruta elegida |

## Ahorro de contexto y tokens

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [headroom](../fichas/headroom.md) | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | te quedas sin contexto en sesiones largas | API de IA opcional |
| [rtk](../fichas/rtk.md) | Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. | tu agente consume demasiado contexto leyendo salidas extensas de terminal | API de IA opcional |

## Observabilidad, evaluación y guardrails

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [promptfoo](../fichas/promptfoo.md) | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. | quieres pruebas automáticas de prompts y seguridad | Depende de la ruta elegida |
| [langfuse](../fichas/langfuse.md) | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. | operas agentes en serio y necesitas trazas/costes/eval | API de IA opcional |
| [MLflow](../fichas/mlflow.md) | Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro. | tu equipo hace ML clásico y LLM y quiere una sola plataforma | API de IA opcional |
| [loguru](../fichas/loguru.md) | Librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa. | quieres logging fácil y legible en Python sin pelear con stdlib | Sin API de IA en la ruta básica |
| [Opik](../fichas/opik.md) | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. | quieres observabilidad y evaluación en un solo producto abierto | API de IA opcional |
| [DeepEval](../fichas/deepeval.md) | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. | quieres tests de LLM en Python como pytest | Depende de la ruta elegida |
| [Ragas](../fichas/ragas.md) | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. | evalúas un sistema RAG | Depende de la ruta elegida |
| [Phoenix](../fichas/phoenix.md) | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. | quieres observabilidad basada en OpenTelemetry | API de IA opcional |
| [Claude-Code-Usage-Monitor](../fichas/claude-code-usage-monitor.md) | Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible. | buscas esta función: Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible. | Sin API de IA en la ruta básica |
| [NeMo Guardrails](../fichas/guardrails.md) | Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales con LLM. | necesitas políticas de seguridad en un chatbot | Depende de la ruta elegida |

## Recetas relacionadas

- [Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
- [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md) — Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor.
- [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.
- [Agente de voz en tiempo real](../playbooks/agente-de-voz.md) — Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
