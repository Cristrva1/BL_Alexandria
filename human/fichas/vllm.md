[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# 🚀 vLLM

> Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 96.9k | Apache-2.0 | Python | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## ¿Qué es?

vLLM, motor de inferencia y servicio de LLM nacido en el Sky Computing Lab de UC Berkeley y mantenido por una comunidad amplia. Licencia Apache-2.0. Es uno de los proyectos open source de IA más activos (~97k estrellas; última versión candidata v0.33.0rc3).

## ¿Qué hace?

Sirve modelos de lenguaje y multimodales con alto rendimiento gracias a PagedAttention, batching continuo, caché de prefijos, decodificación especulativa y muchos formatos de cuantización (FP8, INT4, GPTQ/AWQ, GGUF…). Ofrece paralelismo tensorial, de pipeline, de datos y de expertos para inferencia distribuida, salidas estructuradas, tool calling y multi-LoRA. Expone una API compatible con OpenAI, además de Anthropic Messages y gRPC.

## ¿Cómo lo hace?

Se instala con `uv pip install vllm` (o imagen Docker) y se lanza con `vllm serve <modelo>`. Está escrito en Python con kernels CUDA/HIP y torch.compile. Funciona en GPU NVIDIA y AMD y en otros aceleradores mediante plugins; el rendimiento óptimo exige una GPU con memoria suficiente para el modelo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | LiteLLM tiene proveedor nativo para vLLM. | Lanza `vllm serve` y añade el endpoint en LiteLLM. |
| [Open WebUI](open-webui.md) | La documentación de vLLM explica cómo usarlo con Open WebUI. | Apunta Open WebUI al endpoint OpenAI de vLLM. |
| [langchain](langchain.md) | Integración con LangChain documentada por vLLM. | Usa el cliente compatible con OpenAI de LangChain contra vLLM. |

**Notas:** Alternativas (elige una): sglang.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.33.0rc3 (2026-11-02) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/vllm-project/vllm/blob/main/README.md) · [2](https://docs.vllm.ai/en/latest/deployment/frameworks/open-webui.html) · [3](https://docs.litellm.ai/docs/providers/vllm) · [4](https://docs.vllm.ai/en/latest/serving/integrations/langchain.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API de pago para inferencia propia; GPU, alquiler y licencia de pesos son independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es un motor de serving y no una app de chat; confirma la matriz de hardware y versión antes de instalar |
| Coste | Sin pago a un modelo en la ruta básica. No necesita API de pago para inferencia propia; GPU, alquiler y licencia de pesos son independientes |
| Equipo | Preparación según la ruta elegida. uv y Python compatibles; hardware soportado; pesos y memoria del modelo |

Es un motor de serving y no una app de chat; confirma la matriz de hardware y versión antes de instalar

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv y Python compatibles
- hardware soportado
- pesos y memoria del modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv pip install vllm
vllm download-kernels  # precompiled kernels for faster startup
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/vllm-project/vllm/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar vLLM para mi objetivo y necesito pasos guiados. Lee https://github.com/vllm-project/vllm/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el quickstart con un modelo que quepa en tu equipo y solicita una respuesta breve.

**Qué comprobar:** Puedes comprobar modelo cargado y endpoint de inferencia.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Servir un modelo propio
- Estudiar rendimiento de inferencia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Servir un modelo propio; Estudiar rendimiento de inferencia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un motor de serving y no una app de chat; confirma la matriz de hardware y versión antes de instalar

## Stack y modelos

- **Stack:** uv y Python compatibles; hardware soportado; pesos y memoria del modelo
- **Etiquetas:** `inference` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SGLang](sglang.md) | 38.9k | Framework de servicio de alto rendimiento para LLM y modelos multimodales. |

## Enlaces

- 🐙 GitHub: [vllm-project/vllm](https://github.com/vllm-project/vllm)
- 🌐 Web: <https://vllm.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/vllm-project/vllm/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
