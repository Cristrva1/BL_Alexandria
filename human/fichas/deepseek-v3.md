[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🧩 DeepSeek-V3

> Modelo de lenguaje abierto de DeepSeek (671B parámetros, MoE) para chat, código y razonamiento; se usa por su API compatible con OpenAI o en servidores con varias GPU.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 105k | MIT | Python | 2026-11-15 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

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

## Qué puedes hacer con él

Modelo de lenguaje abierto de DeepSeek (671B parámetros, MoE) para chat, código y razonamiento; se usa por su API compatible con OpenAI o en servidores con varias GPU.

## Por qué destaca

Usos propuestos: Conectar un modelo abierto potente a un agente mediante la API de DeepSeek; Estudiar cómo se sirve un modelo MoE grande con vLLM o SGLang.

## Cómo funciona

Ejecutarlo en local requiere un servidor con varias GPU de centro de datos; para la mayoría de personas la ruta práctica es la API de pago compatible con OpenAI

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- cuenta en la plataforma de DeepSeek para la API
- o un servidor con varias GPU para la ruta local
- un motor de inferencia como SGLang o vLLM

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [SGLang](sglang.md) | 38.9k | Framework de servicio de alto rendimiento para LLM y modelos multimodales. |
| [vLLM](vllm.md) | 96.9k | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. |

## Enlaces

- 🐙 GitHub: [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3)
- 🌐 Web: <https://www.deepseek.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/deepseek-ai/DeepSeek-V3/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
