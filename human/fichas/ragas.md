[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📡 Ragas

> Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.3k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El ejemplo usa OPENAI_API_KEY y métricas que pueden consumir modelos y embeddings; cada adaptación debe presupuestarse |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El ejemplo usa OpenAI y algunas métricas consumen modelos y embeddings; el proveedor y coste dependen de la métrica elegida y deben configurarse explícitamente |
| Coste | El coste depende del proveedor o la ruta. El ejemplo usa OPENAI_API_KEY y métricas que pueden consumir modelos y embeddings; cada adaptación debe presupuestarse |
| Equipo | Preparación según la ruta elegida. Python; dataset de evaluación; modelo y embeddings configurados |

El ejemplo usa OpenAI y algunas métricas consumen modelos y embeddings; el proveedor y coste dependen de la métrica elegida y deben configurarse explícitamente

## Qué puedes hacer con él

Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos.

## Por qué destaca

Usos propuestos: Medir un RAG con datos controlados; Comparar versiones de una cadena.

## Cómo funciona

El ejemplo usa OpenAI y algunas métricas consumen modelos y embeddings; el proveedor y coste dependen de la métrica elegida y deben configurarse explícitamente

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- dataset de evaluación
- modelo y embeddings configurados

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install ragas
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/vibrantlabsai/ragas/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Ragas para mi objetivo y necesito pasos guiados. Lee https://github.com/vibrantlabsai/ragas/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Evalúa una respuesta cuyo contexto y referencia conozcas y comprueba qué mide cada métrica.

**Qué comprobar:** Puedes distinguir recuperación, relevancia y fidelidad.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Medir un RAG con datos controlados
- Comparar versiones de una cadena

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Medir un RAG con datos controlados; Comparar versiones de una cadena | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El ejemplo usa OpenAI y algunas métricas consumen modelos y embeddings; el proveedor y coste dependen de la métrica elegida y deben configurarse explícitamente

## Stack y modelos

- **Stack:** Python; dataset de evaluación; modelo y embeddings configurados
- **Etiquetas:** `evaluation` `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DeepEval](deepeval.md) | 19.5k | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. |
| [promptfoo](promptfoo.md) | 27.2k | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. |

## Enlaces

- 🐙 GitHub: [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas)
- 🌐 Web: <https://docs.ragas.io>
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/vibrantlabsai/ragas/blob/main/README.md)
- [Fuente 2](https://docs.ragas.io/en/latest/howtos/customizations/customize_models/)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
