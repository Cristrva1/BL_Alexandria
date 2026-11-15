[🏠 Inicio](../README.md) › [🧬 Memoria, conocimiento y operación de IA](../categorias/06-memoria-rag-llm-ops.md) › Serving y gateways de LLM

# 🚀 SGLang

> Framework de servicio de alto rendimiento para LLM y modelos multimodales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.9k | Apache-2.0 | Python | 2026-11-10 |

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

Compite con vLLM en velocidad, con caché de prefijos RadixAttention y buen soporte de salidas estructuradas. Muy usado para modelos grandes como DeepSeek.

## Por qué destaca

Muy rápido en cargas con prefijos compartidos y en modelos MoE grandes.

## Cómo funciona

Reutiliza la caché KV entre peticiones con un árbol radix y optimiza el scheduler para alto throughput.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/sgl-project/sglang/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SGLang para mi objetivo y necesito pasos guiados. Lee https://github.com/sgl-project/sglang/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Servir modelos MoE grandes
- Agentes con muchos prompts compartidos
- Salidas JSON restringidas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| buscas el máximo rendimiento en servicio de LLM | quieres la opción más documentada; mira `vllm` |

**Limitaciones:** Requiere GPU.

## Stack y modelos

- **Stack:** Python, CUDA
- **Etiquetas:** `inference` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [vLLM](vllm.md) | 96.9k | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. |

## Enlaces

- 🐙 GitHub: [sgl-project/sglang](https://github.com/sgl-project/sglang)
- 🌐 Web: <https://sglang.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/sgl-project/sglang/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
