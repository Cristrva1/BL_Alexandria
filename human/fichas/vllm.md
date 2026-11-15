[🏠 Inicio](../README.md) › [🧬 Memoria, conocimiento y operación de IA](../categorias/06-memoria-rag-llm-ops.md) › Serving y gateways de LLM

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
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Sirve modelos abiertos a muchos usuarios con una API compatible con OpenAI, gracias a PagedAttention y batching continuo.

## Por qué destaca

Estándar en producción para servir LLM abiertos en GPU.

## Cómo funciona

Gestiona la caché KV por páginas, agrupa peticiones dinámicamente y soporta paralelismo entre GPUs.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install vllm
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/vllm-project/vllm/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar vLLM para mi objetivo y necesito pasos guiados. Lee https://github.com/vllm-project/vllm/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- API privada de LLM para la empresa
- Servir modelos afinados
- Inferencia por lotes barata

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas servir LLM abiertos a muchos usuarios en GPU | solo los usas tú en un portátil; mira `ollama` |

**Limitaciones:** Requiere GPU con bastante memoria.

## Stack y modelos

- **Stack:** Python, CUDA, PyTorch
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

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/vllm-project/vllm/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
