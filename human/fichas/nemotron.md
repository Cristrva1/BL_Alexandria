[🏠 Inicio](../README.md) › [🧑‍💻 Entender código, trabajar con datos y entrenar modelos](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🧠 Nemotron (NVIDIA)

> Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.3k | Apache-2.0 | Jupyter Notebook | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🔴 pesado

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

Reúne guías de entrenamiento, despliegue y casos de uso de los modelos Nemotron, pensados para IA agéntica eficiente.

## Por qué destaca

Modelos abiertos con datos y recetas publicados, optimizados para GPUs NVIDIA.

## Cómo funciona

Notebooks y documentación que usan NeMo, vLLM o TensorRT-LLM.

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

1. Abre el material original y elige un capítulo o ejemplo.
2. Revisa los requisitos de ese ejemplo antes de instalar dependencias.
3. Usa las alternativas y recetas para situarlo dentro de tu proyecto.

[Instrucciones originales de instalación](https://github.com/NVIDIA-NeMo/Nemotron/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Nemotron (NVIDIA) para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA-NeMo/Nemotron/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Desplegar modelos abiertos de NVIDIA
- Afinar Nemotron
- Agentes con modelos eficientes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas GPUs NVIDIA y quieres modelos abiertos optimizados | buscas la forma más simple de correr modelos; mira `ollama` |

## Stack y modelos

- **Stack:** Python, Jupyter
- **Etiquetas:** `training` `inference`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [vLLM](vllm.md) | 96.9k | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. |
| [NemoClaw](nemoclaw.md) | 23k | Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. |

## Enlaces

- 🐙 GitHub: [NVIDIA-NeMo/Nemotron](https://github.com/NVIDIA-NeMo/Nemotron)
- 🌐 Web: <https://docs.nvidia.com/nemotron/latest/index.html>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/NVIDIA-NeMo/Nemotron/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
