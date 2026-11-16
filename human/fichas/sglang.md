[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# 🚀 SGLang

> Framework de servicio de alto rendimiento para LLM y modelos multimodales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.9k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## ¿Qué es?

SGLang, framework de inferencia para modelos de lenguaje, visión-lenguaje y difusión, de la comunidad sgl-project (LMSYS). Licencia Apache-2.0. Es muy activo (~39k estrellas, v0.5.23).

## ¿Qué hace?

Sirve modelos optimizados para cargas agénticas, servicio a gran escala y rollouts de aprendizaje por refuerzo. Soporta un abanico amplio de hardware: GPU NVIDIA y AMD, TPU de Google, Intel, NPU, CPU y Apple Silicon. Incluye SGLang Diffusion para modelos de imagen y vídeo y expone APIs compatibles con OpenAI.

## ¿Cómo lo hace?

Se usa con la imagen Docker `lmsysorg/sglang` o con `uv pip install --prerelease=allow sglang`, y se lanza con los comandos del Cookbook según modelo y hardware. Está escrito en Python con kernels propios. Requiere aceleradores compatibles para rendimiento real.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | Usar SGLang a través del proveedor compatible con OpenAI de LiteLLM. (combinación por arquitectura) | Lanza SGLang y regístralo como endpoint OpenAI en LiteLLM. |
| [Open WebUI](open-webui.md) | Interfaz de chat sobre el endpoint OpenAI de SGLang. (combinación por arquitectura) | Configura la conexión OpenAI de Open WebUI con la URL de SGLang. |
| [Unsloth](unsloth.md) | Servir con SGLang modelos afinados con Unsloth. (combinación por arquitectura) | Afina y exporta con Unsloth y sirve los pesos con SGLang. |

**Notas:** Alternativas (elige una): vllm.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.5.23 (2026-11-02) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/sgl-project/sglang/blob/main/README.md) · [2](https://docs.sglang.io/docs/basic_usage/openai_api)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Sin API de modelo alojado en la ruta propia; cómputo y pesos tienen sus costes y licencias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El comando del README admite prereleases; selecciona una versión apropiada según la documentación de tu hardware; patrocinio a contribuidores no es integración con sus agentes |
| Coste | Sin pago a un modelo en la ruta básica. Sin API de modelo alojado en la ruta propia; cómputo y pesos tienen sus costes y licencias |
| Equipo | Preparación según la ruta elegida. uv; hardware y drivers compatibles; modelo con memoria suficiente |

El comando del README admite prereleases; selecciona una versión apropiada según la documentación de tu hardware; patrocinio a contribuidores no es integración con sus agentes

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv
- hardware y drivers compatibles
- modelo con memoria suficiente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv pip install --prerelease=allow sglang
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/sgl-project/sglang/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SGLang para mi objetivo y necesito pasos guiados. Lee https://github.com/sgl-project/sglang/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el quickstart y comprueba una petición breve al modelo servido.

**Qué comprobar:** Puedes identificar modelo, proceso y respuesta del endpoint.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Servir un modelo para una aplicación
- Estudiar inferencia multimodal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Servir un modelo para una aplicación; Estudiar inferencia multimodal | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El comando del README admite prereleases; selecciona una versión apropiada según la documentación de tu hardware; patrocinio a contribuidores no es integración con sus agentes

## Stack y modelos

- **Stack:** uv; hardware y drivers compatibles; modelo con memoria suficiente
- **Etiquetas:** `inference` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [vLLM](vllm.md) | 96.9k | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. |

## Enlaces

- 🐙 GitHub: [sgl-project/sglang](https://github.com/sgl-project/sglang)
- 🌐 Web: <https://sglang.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/sgl-project/sglang/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
