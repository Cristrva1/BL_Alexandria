[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📡 promptfoo

> CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.2k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Defines casos de prueba en YAML y comparas salidas de varios modelos con aserciones. También escanea vulnerabilidades como inyección de prompts.

## Por qué destaca

Muy práctico para CI: evaluación y red teaming en una sola herramienta.

## Cómo funciona

Ejecuta la matriz de prompts por modelos y casos, evalúa con reglas o con un LLM juez y muestra resultados en una web local.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/promptfoo/promptfoo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar promptfoo para mi objetivo y necesito pasos guiados. Lee https://github.com/promptfoo/promptfoo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Comparar GPT, Claude y Gemini en tu caso
- Pruebas de regresión de prompts en CI
- Red teaming de un chatbot

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres pruebas automáticas de prompts y seguridad | necesitas observabilidad en producción; mira `langfuse` |

## Stack y modelos

- **Stack:** TypeScript, Node.js
- **Etiquetas:** `evaluation` `security` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DeepEval](deepeval.md) | 19.5k | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. |
| [Ragas](ragas.md) | 16.3k | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. |
| [DSPy](dspy.md) | 39.1k | Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano. |

## Enlaces

- 🐙 GitHub: [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)
- 🌐 Web: <https://promptfoo.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/promptfoo/promptfoo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
