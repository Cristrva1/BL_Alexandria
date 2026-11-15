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
| API de IA | API de IA opcional. CLI MIT; APIs y servicios adicionales tienen costes y Ollama permite modelos locales |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Una puntuación depende del dataset, proveedor y evaluador; los tests de seguridad deben dirigirse a sistemas propios o autorizados |
| Coste | El coste depende del proveedor o la ruta. CLI MIT; APIs y servicios adicionales tienen costes y Ollama permite modelos locales |
| Equipo | Preparación según la ruta elegida. Node; dataset de preguntas; proveedor o Ollama; criterio de evaluación |

Una puntuación depende del dataset, proveedor y evaluador; los tests de seguridad deben dirigirse a sistemas propios o autorizados

## Qué puedes hacer con él

CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad.

## Por qué destaca

Usos propuestos: Evaluar un prompt de soporte; Probar regresiones de un RAG.

## Cómo funciona

Una puntuación depende del dataset, proveedor y evaluador; los tests de seguridad deben dirigirse a sistemas propios o autorizados

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- dataset de preguntas
- proveedor o Ollama
- criterio de evaluación

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
npm install -g promptfoo
promptfoo init --example getting-started
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/promptfoo/promptfoo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar promptfoo para mi objetivo y necesito pasos guiados. Lee https://github.com/promptfoo/promptfoo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea dos variantes de un prompt y evalúalas con tres casos conocidos.

**Qué comprobar:** Puedes comparar respuestas y detectar un fallo concreto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Evaluar un prompt de soporte
- Probar regresiones de un RAG

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Evaluar un prompt de soporte; Probar regresiones de un RAG | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Una puntuación depende del dataset, proveedor y evaluador; los tests de seguridad deben dirigirse a sistemas propios o autorizados

## Stack y modelos

- **Stack:** Node; dataset de preguntas; proveedor o Ollama; criterio de evaluación
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

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/promptfoo/promptfoo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
