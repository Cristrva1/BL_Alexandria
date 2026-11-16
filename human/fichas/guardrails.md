[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 📡 NeMo Guardrails

> Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales con LLM.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.5k | NOASSERTION | Python | 2026-06-24 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

NeMo Guardrails, toolkit open source de NVIDIA para añadir barreras programables a aplicaciones conversacionales con LLM. Licencia Apache-2.0 según el README (GitHub muestra NOASSERTION). Es activo (~7.5k estrellas, v0.24.1).

## ¿Qué hace?

Controla la salida del modelo con «rails»: no hablar de ciertos temas, seguir un diálogo, filtrar entradas y salidas, detectar jailbreaks, verificar hechos y moderar contenido. Las reglas se definen con configuración y el lenguaje Colang. Se puede usar como librería de Python o como servidor de guardrails.

## ¿Cómo lo hace?

Se instala con `pip install nemoguardrails` y requiere Python 3.11–3.13 (desde 0.25.0 ya no admite 3.10). La integración con LangChain es opcional (`NEMOGUARDRAILS_LLM_FRAMEWORK=langchain`). Recoge telemetría anónima de uso (revisa la sección de privacidad para desactivarla).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [langchain](langchain.md) | Integración opcional con LangChain documentada en el README. | Activa el framework LangChain y envuelve tu cadena con los rails. |
| [promptfoo](promptfoo.md) | Hacer red teaming de la app protegida para comprobar los rails. (combinación por arquitectura) | Configura los rails y lanza promptfoo contra el servidor. |
| [vLLM](vllm.md) | Proteger un modelo autoalojado. (combinación por arquitectura) | Sirve el modelo con vLLM y apúntale la configuración de Guardrails. |

**Notas:** Sin alternativas declaradas. No confundir con Guardrails AI (otro proyecto, no catalogado). Telemetría activa por defecto.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.24.1 (2026-09-16) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NVIDIA-NeMo/Guardrails/blob/develop/README.md) · [2](https://docs.nvidia.com/nemo/guardrails)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Los modelos y servicios usados por las reglas pueden generar consumo; el toolkit Apache no los incluye |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. NeMo Guardrails no garantiza seguridad total ni adecuación a todo sector; develop es desarrollo y la versión publicada debe elegirse de forma explícita |
| Coste | El coste depende del proveedor o la ruta. Los modelos y servicios usados por las reglas pueden generar consumo; el toolkit Apache no los incluye |
| Equipo | Preparación según la ruta elegida. Python; app conversacional; configuración Colang; modelo según rails |

NeMo Guardrails no garantiza seguridad total ni adecuación a todo sector; develop es desarrollo y la versión publicada debe elegirse de forma explícita

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- app conversacional
- configuración Colang
- modelo según rails

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install nemoguardrails
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/NVIDIA-NeMo/Guardrails/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar NeMo Guardrails para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA-NeMo/Guardrails/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Define un flujo de tema permitido y prueba una pregunta dentro y otra fuera de ese tema.

**Qué comprobar:** Puedes comprobar la regla aplicada y registrar sus límites.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Guiar un asistente de soporte
- Evaluar controles de una app propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Guiar un asistente de soporte; Evaluar controles de una app propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** NeMo Guardrails no garantiza seguridad total ni adecuación a todo sector; develop es desarrollo y la versión publicada debe elegirse de forma explícita

## Stack y modelos

- **Stack:** Python; app conversacional; configuración Colang; modelo según rails
- **Etiquetas:** `security` `chatbot` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)
- 🌐 Web: <https://docs.nvidia.com/nemo/guardrails/latest/index.html>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NVIDIA-NeMo/Guardrails/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
