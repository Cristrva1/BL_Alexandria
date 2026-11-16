[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📚 OpenLLMetry

> Instrumentación abierta basada en OpenTelemetry para aplicaciones de LLM: traza llamadas a modelos, bases vectoriales y frameworks hacia tu backend de observabilidad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.5k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Conjunto de extensiones de OpenTelemetry de código abierto (Apache-2.0) de Traceloop, empresa que ofrece una plataforma comercial. Sus convenciones semánticas se han incorporado a OpenTelemetry. Activo.

## ¿Qué hace?

Instrumenta automáticamente proveedores de LLM (OpenAI, Anthropic, Bedrock, Ollama…), bases vectoriales (Qdrant, Chroma, Milvus…) y frameworks (LangChain, LlamaIndex, CrewAI, MCP…), y exporta trazas a Grafana, Datadog, Dynatrace, Honeycomb y otros backends OpenTelemetry.

## ¿Cómo lo hace?

Paquetes Python publicados en PyPI (traceloop-sdk y opentelemetry-instrumentation-*); también hay versión para JavaScript en otro repositorio. Se configura el exportador OTLP del destino.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Grafana](grafana.md) | Traceloop documenta el envío de trazas de OpenLLMetry a Grafana. | Configura el exportador OTLP hacia Grafana Tempo o Cloud; después inicializa el SDK. |
| [langchain](langchain.md) | Incluye una instrumentación OpenTelemetry específica para LangChain. | Instala traceloop-sdk; las cadenas de LangChain se trazan al inicializarlo. |
| [LlamaIndex](llama-index.md) | Incluye una instrumentación OpenTelemetry para LlamaIndex. | Inicializa el SDK antes de crear los índices y consultas. |
| [Ollama](ollama.md) | Incluye una instrumentación OpenTelemetry para las llamadas a Ollama. | Inicializa el SDK; las llamadas al cliente de Ollama quedan trazadas. |

**Notas:** Cercano a langfuse y phoenix, que ofrecen interfaz propia; OpenLLMetry solo instrumenta y exporta.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada 0.63.0 (2026-11-05) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/traceloop/openllmetry/blob/main/README.md) · [2](https://www.traceloop.com/docs/openllmetry/integrations/grafana) · [3](https://github.com/traceloop/openllmetry/tree/main/packages)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
pip install traceloop-sdk
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/traceloop/openllmetry/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenLLMetry para mi objetivo y necesito pasos guiados. Lee https://github.com/traceloop/openllmetry/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install traceloop-sdk`, inicializa el SDK en un script con una llamada a un modelo y envía las trazas a la consola o a tu backend..

**Qué comprobar:** Ves las trazas con prompts, tokens y latencias..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- trazar llamadas a OpenAI, LangChain o Ollama en Grafana o Datadog
- añadir observabilidad de LLM a una pila OpenTelemetry existente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: trazar llamadas a OpenAI, LangChain o Ollama en Grafana o Datadog; añadir observabilidad de LLM a una pila OpenTelemetry existente | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, package.json
- **Etiquetas:** `observability` `python` `llm` `opentelemetry`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [traceloop/openllmetry](https://github.com/traceloop/openllmetry)
- 🌐 Web: <https://www.traceloop.com/openllmetry>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/traceloop/openllmetry/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
