[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ LLaMA-Factory

> Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 76k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

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

Soporta LoRA, QLoRA, ajuste completo, DPO y más desde una UI o CLI. Muy usado en investigación e industria.

## Por qué destaca

La herramienta más completa para afinar modelos con interfaz.

## Cómo funciona

Unifica recetas de entrenamiento sobre Transformers y PEFT con una UI Gradio (LlamaBoard).

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/hiyouga/LlamaFactory/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LLaMA-Factory para mi objetivo y necesito pasos guiados. Lee https://github.com/hiyouga/LlamaFactory/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Afinar con DPO o RLHF
- Entrenar modelos de visión-lenguaje
- Experimentar sin código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres muchas técnicas de fine-tuning con UI | buscas la opción más eficiente en memoria; mira `unsloth` |

**Limitaciones:** Requiere GPU.

## Stack y modelos

- **Stack:** Python, PyTorch, Gradio
- **Etiquetas:** `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PEFT](peft.md) | 21.9k | Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA. |
| [Transformers](transformers.md) | 169k | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Unsloth](unsloth.md) | 79.5k | Fine-tuning y ejecución local de LLM hasta 2 veces más rápido y con mucha menos memoria, ahora con UI. |

## Enlaces

- 🐙 GitHub: [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)
- 🌐 Web: <https://llamafactory.readthedocs.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/hiyouga/LlamaFactory/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
