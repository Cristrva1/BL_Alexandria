[🏠 Inicio](../README.md) › [🧑‍💻 Entender código, trabajar con datos y entrenar modelos](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ Transformers

> Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 169k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

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

Da acceso a cientos de miles de modelos con una API común para inferencia y entrenamiento. Es la base del ecosistema de modelos abiertos.

## Por qué destaca

El estándar para trabajar con modelos abiertos.

## Cómo funciona

Define arquitecturas en PyTorch y carga pesos desde Hugging Face Hub con pipelines de alto nivel.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/huggingface/transformers/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Transformers para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/transformers/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Clasificar texto con un modelo abierto
- Afinar modelos pequeños
- Prototipos de visión o audio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| trabajas con modelos abiertos en Python | solo quieres chatear con un modelo local; mira `ollama` |

## Stack y modelos

- **Stack:** Python, PyTorch
- **Etiquetas:** `training` `inference` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PEFT](peft.md) | 21.9k | Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA. |
| [TRL](trl.md) | 19.7k | Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más. |
| [PyTorch](pytorch.md) | 106k | Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU. |

## Enlaces

- 🐙 GitHub: [huggingface/transformers](https://github.com/huggingface/transformers)
- 🌐 Web: <https://huggingface.co/transformers>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/huggingface/transformers/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
