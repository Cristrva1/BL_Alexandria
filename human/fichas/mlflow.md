[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📡 MLflow

> Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28.8k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Seguimiento básico sin API de IA; evaluadores, modelos y alojamiento gestionado pueden generar costes |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El wizard documenta Claude Code y Codex para añadir instrumentación; no es una autorización para cambiar automáticamente proyectos reales |
| Coste | El coste depende del proveedor o la ruta. Seguimiento básico sin API de IA; evaluadores, modelos y alojamiento gestionado pueden generar costes |
| Equipo | Preparación según la ruta elegida. uv o Python; app y datos ficticios; agente opcional para instrumentar |

El wizard documenta Claude Code y Codex para añadir instrumentación; no es una autorización para cambiar automáticamente proyectos reales

## Qué puedes hacer con él

Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro.

## Por qué destaca

Usos propuestos: Registrar experimentos de ML; Añadir trazas a una app de IA.

## Cómo funciona

El wizard documenta Claude Code y Codex para añadir instrumentación; no es una autorización para cambiar automáticamente proyectos reales

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv o Python
- app y datos ficticios
- agente opcional para instrumentar

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uvx mlflow server
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mlflow/mlflow/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MLflow para mi objetivo y necesito pasos guiados. Lee https://github.com/mlflow/mlflow/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inicia el servidor de prueba y registra una ejecución pequeña con parámetros y resultado.

**Qué comprobar:** Puedes abrir la ejecución y comparar sus datos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Registrar experimentos de ML
- Añadir trazas a una app de IA

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Registrar experimentos de ML; Añadir trazas a una app de IA | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El wizard documenta Claude Code y Codex para añadir instrumentación; no es una autorización para cambiar automáticamente proyectos reales

## Stack y modelos

- **Stack:** uv o Python; app y datos ficticios; agente opcional para instrumentar
- **Etiquetas:** `observability` `training` `evaluation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Transformers](transformers.md) | 169k | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. |
| [DSPy](dspy.md) | 39.1k | Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Enlaces

- 🐙 GitHub: [mlflow/mlflow](https://github.com/mlflow/mlflow)
- 🌐 Web: <https://mlflow.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mlflow/mlflow/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
