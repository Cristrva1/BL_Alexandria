[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 📚 DeepSpeed

> Biblioteca de optimización de entrenamiento e inferencia distribuidos de Microsoft: ZeRO, paralelismo y descarga a CPU/NVMe para modelos enormes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 43.3k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

## ¿Qué es?

Biblioteca de código abierto (Apache-2.0) creada por Microsoft y ahora bajo la organización deepspeedai, alojada en la LF AI & Data Foundation. Muy madura.

## ¿Qué hace?

Permite entrenar e inferir modelos muy grandes con eficiencia: ZeRO (etapas 1-3, ZeRO++), descarga a CPU y NVMe, paralelismo de datos, tensores, pipeline y secuencia, precisión mixta, compresión y kernels optimizados.

## ¿Cómo lo hace?

Se instala con pip sobre PyTorch; compila extensiones CUDA/ROCm al vuelo o en la instalación. Se configura con un JSON y se integra con Transformers, Accelerate y Lightning.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Transformers](transformers.md) | Transformers integra DeepSpeed en su Trainer mediante un archivo de configuración. | Instala deepspeed; después pasa `--deepspeed config.json` al Trainer. |
| [Accelerate](accelerate.md) | Accelerate lanza entrenamientos con DeepSpeed sin cambiar el código de entrenamiento. | Ejecuta `accelerate config` y elige DeepSpeed; después `accelerate launch`. |
| [PyTorch Lightning](pytorch-lightning.md) | Lightning ofrece estrategias DeepSpeed integradas. | Instala deepspeed; después usa `strategy="deepspeed"` en el Trainer o Fabric. |
| [Axolotl](axolotl.md) | Combinación recíproca: Axolotl lo enlaza como «Axolotl integra DeepSpeed (incluido Ulysses) para entrenamiento distribuido y ahorro de memoria». | Orden indicado desde Axolotl: Instala DeepSpeed; después indica la configuración deepspeed en el YAML. |
| [OpenRLHF](openrlhf.md) | Combinación recíproca: OpenRLHF lo enlaza como «OpenRLHF entrena con DeepSpeed ZeRO-3 para ahorrar memoria». | Orden indicado desde OpenRLHF: Instala DeepSpeed compatible con tu CUDA. |

**Notas:** Las extensiones CUDA requieren versiones compatibles de compilador, CUDA y PyTorch.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.20.0 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/deepspeedai/DeepSpeed/blob/master/README.md) · [2](https://www.deepspeed.ai/) · [3](https://huggingface.co/docs/transformers/deepspeed)</sub>

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
pip install deepspeed
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/deepspeedai/DeepSpeed/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DeepSpeed para mi objetivo y necesito pasos guiados. Lee https://github.com/deepspeedai/DeepSpeed/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install deepspeed` en un entorno con PyTorch y GPU y ejecuta `ds_report` para comprobar la compatibilidad..

**Qué comprobar:** El informe muestra qué operaciones y extensiones están disponibles..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- entrenar un modelo que no cabe en una GPU repartiendo estados con ZeRO-3
- acelerar un ajuste fino distribuido con Transformers o Accelerate

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: entrenar un modelo que no cabe en una GPU repartiendo estados con ZeRO-3; acelerar un ajuste fino distribuido con Transformers o Accelerate | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, setup.py
- **Etiquetas:** `training` `python` `gpu` `distributed`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed)
- 🌐 Web: <https://www.deepspeed.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/deepspeedai/DeepSpeed/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
