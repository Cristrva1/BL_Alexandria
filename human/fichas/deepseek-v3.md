[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🧩 DeepSeek-V3

> Modelo de lenguaje abierto de DeepSeek (671B parámetros, MoE) para chat, código y razonamiento; se usa por su API compatible con OpenAI o en servidores con varias GPU.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 105k | MIT | Python | 2026-11-15 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; necesita GPU

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

DeepSeek-V3, modelo de lenguaje MoE de DeepSeek con 671B parámetros totales y 37B activos por token. El código es MIT y los pesos usan un Model Agreement propio. El repo tiene ~105k estrellas, pero no se actualiza desde agosto de 2025 y DeepSeek ha publicado versiones posteriores.

## ¿Qué hace?

Sirve para chat, código y razonamiento. Usa Multi-head Latent Attention, DeepSeekMoE, balanceo sin pérdida auxiliar y predicción multi-token, y destila razonamiento de DeepSeek-R1. Según DeepSeek, se entrenó con 14.8T tokens en 2.788M horas de GPU H800.

## ¿Cómo lo hace?

Se usa por la API de DeepSeek (compatible con OpenAI) o en local con varios GPU mediante SGLang, vLLM, LMDeploy, TensorRT-LLM o LightLLM, en BF16 o FP8. No es viable en hardware doméstico sin cuantizar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [SGLang](sglang.md) | Soporte documentado en BF16 y FP8. | Sirve el modelo con SGLang. |
| [vLLM](vllm.md) | Soporte documentado. | Sirve el modelo con vLLM. |
| [litellm](litellm.md) | Enrutar a la API de DeepSeek o a un servidor propio. (combinación por arquitectura) | Añade el modelo al proxy. |
| [TensorRT-LLM](tensorrt-llm.md) | Soporte documentado para GPU NVIDIA. | Construye el motor con TensorRT-LLM. |

**Notas:** Sin alternativas declaradas. Repo histórico: conviene evaluar las versiones más nuevas de DeepSeek.

Estado en GitHub: activo · último push 2025-08-28 · última versión publicada v1.0.0 (2025-06-27) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/deepseek-ai/DeepSeek-V3/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. API de pago compatible con OpenAI en platform.deepseek.com; la ruta local no usa API pero necesita infraestructura de varias GPU |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Pesos abiertos en Hugging Face; se sirven con SGLang, vLLM, LMDeploy o TensorRT-LLM en servidores con varias GPU |
| Coste | El coste depende del proveedor o la ruta. La API se paga por uso; la ruta local evita ese pago pero exige hardware de centro de datos |
| Equipo | GPU o infraestructura especializada. API: cuenta en platform.deepseek.com; local: servidor con varias GPU y un motor como SGLang o vLLM |

No es un cliente de Claude Code, Codex o Antigravity; se usa como proveedor de modelo vía API compatible con OpenAI

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- cuenta en la plataforma de DeepSeek para la API
- o un servidor con varias GPU para la ruta local
- un motor de inferencia como SGLang o vLLM

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/deepseek-ai/DeepSeek-V3.git
```

Comando copiado literalmente de el README (sección «Model Weights & Demo Code Preparation»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/deepseek-ai/DeepSeek-V3/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DeepSeek-V3 para mi objetivo y necesito pasos guiados. Lee https://github.com/deepseek-ai/DeepSeek-V3/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Envía una petición de prueba a la API de DeepSeek desde un cliente compatible con OpenAI y pide completar una función corta.

**Qué comprobar:** Recibes la respuesta y ves en tu panel el consumo de esa llamada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Conectar un modelo abierto potente a un agente mediante la API de DeepSeek
- Estudiar cómo se sirve un modelo MoE grande con vLLM o SGLang

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Conectar un modelo abierto potente a un agente mediante la API de DeepSeek; Estudiar cómo se sirve un modelo MoE grande con vLLM o SGLang | Quieres correr un modelo en un equipo doméstico; elige un modelo pequeño con Ollama y revisa los límites antes de elegirlo |

**Limitaciones:** No cabe en un equipo doméstico: la demo oficial usa dos nodos de 8 GPU. No es un IDE ni una integración nativa con Claude Code, Codex o Antigravity

## Stack y modelos

- **Stack:** API: cuenta en platform.deepseek.com; local: servidor con varias GPU y un motor como SGLang o vLLM
- **Etiquetas:** `llm` `inference` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3)
- 🌐 Web: <https://www.deepseek.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/deepseek-ai/DeepSeek-V3/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
