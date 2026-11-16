[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🧑‍💻 bionemo-recipes

> Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 877 | — | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🔴 pesado

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 37/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

BioNeMo Recipes, recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala. Licencia Apache-2.0 en LICENSE/license.txt (GitHub no la detecta por la ubicación). Es de nicho (~880 estrellas, v3.0.0).

## ¿Qué hace?

Ofrece modelos acelerados con TransformerEngine (ESM-2, AMPLIFY, Llama 3, Mixtral, etc.) y recetas autocontenidas para escalar de una GPU a multinodo con FSDP y FP8. Está pensado para desarrolladores de modelos y científicos que ajustan modelos con datos propios.

## ¿Cómo lo hace?

Cada receta es un contenedor Docker (`docker build` y `docker run --gpus all … train.py`). Es compatible con HF Accelerate, PyTorch Lightning o PyTorch puro, y requiere GPU NVIDIA.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Transformers](transformers.md) | Checkpoints publicados en Hugging Face. | Carga los modelos con Transformers. |
| [PyTorch](pytorch.md) | Base de las recetas. | Viene en el contenedor. |
| [PEFT](peft.md) | Ajuste eficiente con datos propios. (combinación por arquitectura) | Aplica LoRA sobre el checkpoint. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v3.0.0 (2026-06-24) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NVIDIA-BioNeMo/bionemo-recipes/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API para las recetas propias; GPUs, almacenamiento y datasets tienen condiciones independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No es un framework único listo para usar; algunas recetas requieren Hopper o Blackwell y sus resultados no son evidencia clínica |
| Coste | El coste depende del proveedor o la ruta. No necesita API para las recetas propias; GPUs, almacenamiento y datasets tienen condiciones independientes |
| Equipo | Preparación según la ruta elegida. Conocimientos de biología computacional; Docker; GPU compatible con la receta; datos autorizados |

No es un framework único listo para usar; algunas recetas requieren Hopper o Blackwell y sus resultados no son evidencia clínica

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Conocimientos de biología computacional
- Docker
- GPU compatible con la receta
- datos autorizados

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/NVIDIA-BioNeMo/bionemo-recipes/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar bionemo-recipes para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA-BioNeMo/bionemo-recipes/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa la receta ESM2 y calcula sus requisitos antes de ejecutar un ejemplo educativo pequeño.

**Qué comprobar:** Puedes identificar modelo, datos y restricciones de hardware.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar modelos de secuencias biológicas
- Reproducir un entrenamiento de investigación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar modelos de secuencias biológicas; Reproducir un entrenamiento de investigación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No es un framework único listo para usar; algunas recetas requieren Hopper o Blackwell y sus resultados no son evidencia clínica

## Stack y modelos

- **Stack:** Conocimientos de biología computacional; Docker; GPU compatible con la receta; datos autorizados
- **Etiquetas:** `entrenamiento` `drug-discovery` `gpu` `machine-learning` `pytorch` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [NVIDIA-BioNeMo/bionemo-recipes](https://github.com/NVIDIA-BioNeMo/bionemo-recipes)
- 🌐 Web: <https://nvidia-bionemo.github.io/bionemo-recipes/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NVIDIA-BioNeMo/bionemo-recipes/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
