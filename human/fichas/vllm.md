[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# 🚀 vLLM

> Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 96.9k | Apache-2.0 | Python | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

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

## Qué puedes hacer con él

Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU.

## Por qué destaca

Usos propuestos: Servir un modelo propio; Estudiar rendimiento de inferencia.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [Open WebUI](open-webui.md) | 159k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |

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
