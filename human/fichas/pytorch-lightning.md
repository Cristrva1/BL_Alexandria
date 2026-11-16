[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 📚 PyTorch Lightning

> Framework que estructura el entrenamiento en PyTorch y lo escala de una GPU a miles sin cambiar el código, con Lightning Fabric para control experto.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.4k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Framework de código abierto (Apache-2.0) de Lightning AI, empresa que ofrece una plataforma en la nube. Muy maduro.

## ¿Qué hace?

Elimina el código repetitivo del entrenamiento en PyTorch: bucles, precisión mixta, multi-GPU y multinodo (DDP, FSDP, DeepSpeed), checkpoints, callbacks y registro con múltiples herramientas; Fabric permite escalar código PyTorch existente con más control.

## ¿Cómo lo hace?

Se instala con pip (`lightning`) sobre PyTorch. Incluye loggers para MLflow, TensorBoard, W&B y otros.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | Lightning organiza y escala código de PyTorch. | Instala PyTorch; después lightning. |
| [DeepSpeed](deepspeed.md) | Lightning ofrece la estrategia deepspeed en Trainer y Fabric. | Instala deepspeed; después usa `strategy="deepspeed"`. |
| [MLflow](mlflow.md) | Lightning incluye MLFlowLogger para registrar métricas y modelos en MLflow. | Arranca MLflow; después pasa MLFlowLogger al Trainer. |

**Notas:** Añade una capa de abstracción; para scripts sencillos puede bastar accelerate.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 2.6.6 (2026-09-10) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Lightning-AI/pytorch-lightning/blob/master/README.md) · [2](https://lightning.ai/docs/pytorch/stable/extensions/generated/lightning.pytorch.loggers.MLFlowLogger.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
pip install lightning
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Lightning-AI/pytorch-lightning/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PyTorch Lightning para mi objetivo y necesito pasos guiados. Lee https://github.com/Lightning-AI/pytorch-lightning/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install lightning` y ejecuta el ejemplo de autoencoder del README..

**Qué comprobar:** El Trainer entrena y muestra métricas por época..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- organizar un proyecto de entrenamiento en PyTorch sin código repetitivo
- pasar de una GPU a varias con DDP, FSDP o DeepSpeed

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: organizar un proyecto de entrenamiento en PyTorch sin código repetitivo; pasar de una GPU a varias con DDP, FSDP o DeepSpeed | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml, requirements.txt, setup.py
- **Etiquetas:** `training` `python` `pytorch`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)
- 🌐 Web: <https://lightning.ai/pytorch-lightning/?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Lightning-AI/pytorch-lightning/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
