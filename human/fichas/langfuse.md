[🏠 Inicio](../README.md) › [🧬 Memoria, conocimiento y operación de IA](../categorias/06-memoria-rag-llm-ops.md) › Observabilidad, evaluación y guardrails

# 📡 langfuse

> Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 37.4k | NOASSERTION | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve la opacidad: ves qué prompt, qué modelo, qué coste y qué salida tuvo cada paso de tu pipeline.

## Por qué destaca

Es una de las plataformas de LLM observability de referencia, con self-host y cloud e integraciones con los frameworks más usados (LangChain, OpenAI SDK, LiteLLM, CrewAI). Su soporte de OpenTelemetry la hace compatible con instrumentación existente.

## Cómo funciona

Instrumentas tu app con sus SDKs (o vía OpenTelemetry) para enviar trazas, costos y evaluaciones a un backend con UI de análisis, permitiendo seguir el árbol completo de una petición de agente paso a paso.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/langfuse/langfuse/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar langfuse para mi objetivo y necesito pasos guiados. Lee https://github.com/langfuse/langfuse/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Ver el detalle de cada llamada/agente
- Evaluar prompts y medir costos
- Depurar flujos multi-paso de agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| operas agentes en serio y necesitas trazas/costes/eval | haces prototipos triviales o no quieres operar el backend |

## Stack y modelos

- **Stack:** TypeScript, Docker, PostgreSQL, self-host/cloud
- **Etiquetas:** `automation` `observability` `typescript` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [ag2](ag2.md) | 5.1k | Framework maduro para sistemas multiagente con patrones de colaboración (heredero directo de AutoGen). |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Phoenix](phoenix.md) | 12.3k | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. |
| [Opik](opik.md) | 23.4k | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. |
| [MLflow](mlflow.md) | 28.8k | Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro. |

## Enlaces

- 🐙 GitHub: [langfuse/langfuse](https://github.com/langfuse/langfuse)
- 🌐 Web: <https://langfuse.com>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/langfuse/langfuse/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
