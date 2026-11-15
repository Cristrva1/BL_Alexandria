[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📡 DeepEval

> Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.5k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Muchas métricas usan un juez LLM por consumo o uno local Ollama; Confident AI y embeddings tienen configuración propia |
| Claude Code | Depende del recurso o la configuración |
| Codex | Depende del recurso o la configuración |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | Modelos locales documentados. El MCP mencionado pertenece al servicio compañero Confident AI; no todas las métricas necesitan LLM y un juez pequeño puede fallar al seguir el esquema |
| Coste | El coste depende del proveedor o la ruta. Muchas métricas usan un juez LLM por consumo o uno local Ollama; Confident AI y embeddings tienen configuración propia |
| Equipo | Preparación según la ruta elegida. Python; casos con respuestas conocidas; modelo evaluador y embeddings si se usan |

El MCP mencionado pertenece al servicio compañero Confident AI; no todas las métricas necesitan LLM y un juez pequeño puede fallar al seguir el esquema

## Qué puedes hacer con él

Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas.

## Por qué destaca

Usos propuestos: Detectar regresiones de un chatbot; Probar relevancia de respuestas RAG.

## Cómo funciona

El MCP mencionado pertenece al servicio compañero Confident AI; no todas las métricas necesitan LLM y un juez pequeño puede fallar al seguir el esquema

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- casos con respuestas conocidas
- modelo evaluador y embeddings si se usan

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
pip install -U deepeval
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/confident-ai/deepeval/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DeepEval para mi objetivo y necesito pasos guiados. Lee https://github.com/confident-ai/deepeval/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Evalúa tres respuestas ficticias con un criterio explícito y revisa una puntuación manualmente.

**Qué comprobar:** Puedes relacionar el resultado con el caso y el juez seleccionado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Detectar regresiones de un chatbot
- Probar relevancia de respuestas RAG

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Detectar regresiones de un chatbot; Probar relevancia de respuestas RAG | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP mencionado pertenece al servicio compañero Confident AI; no todas las métricas necesitan LLM y un juez pequeño puede fallar al seguir el esquema

## Stack y modelos

- **Stack:** Python; casos con respuestas conocidas; modelo evaluador y embeddings si se usan
- **Etiquetas:** `evaluation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ragas](ragas.md) | 16.3k | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. |
| [promptfoo](promptfoo.md) | 27.2k | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. |

## Enlaces

- 🐙 GitHub: [confident-ai/deepeval](https://github.com/confident-ai/deepeval)
- 🌐 Web: <https://deepeval.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/confident-ai/deepeval/blob/main/README.md)
- [Fuente 2](https://deepeval.com/docs/metrics-introduction)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
