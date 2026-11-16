[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 📚 Accelerate

> Biblioteca de Hugging Face para ejecutar el mismo código de PyTorch en una GPU, varias, TPU o con DeepSpeed y FSDP, con precisión mixta, cambiando pocas líneas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.9k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 3 Avanzado — preparación sencilla; requiere programar con él; dominio especializado

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (Apache-2.0) de Hugging Face. Muy madura; base del Trainer de Transformers.

## ¿Qué hace?

Abstrae el código específico de dispositivos y distribución para que el mismo bucle de PyTorch funcione en CPU, una o varias GPU, TPU, multinodo, DeepSpeed o FSDP, con precisión mixta (incluida FP8) y carga de modelos grandes.

## ¿Cómo lo hace?

Se instala con pip sobre PyTorch; se configura con `accelerate config` y se ejecuta con `accelerate launch`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DeepSpeed](deepspeed.md) | Accelerate integra DeepSpeed sin cambiar el código de entrenamiento. | Elige DeepSpeed en `accelerate config`; después lanza el script. |
| [Transformers](transformers.md) | El Trainer de Transformers usa Accelerate internamente. | Instala ambos; el Trainer aprovecha la configuración de Accelerate. |
| [PyTorch](pytorch.md) | Accelerate prepara modelos y bucles de PyTorch para cualquier configuración de hardware. | Instala PyTorch; después envuelve el bucle con Accelerator. |

**Notas:** Para estructurar proyectos grandes, pytorch-lightning aporta más organización.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v1.15.0 (2026-09-09) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/huggingface/accelerate/blob/main/README.md) · [2](https://huggingface.co/docs/accelerate)</sub>

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
pip install accelerate
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/huggingface/accelerate/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Accelerate para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/accelerate/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install accelerate`, ejecuta `accelerate config` y lanza un script de ejemplo con `accelerate launch`..

**Qué comprobar:** El script se ejecuta con la configuración elegida..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- convertir un bucle de entrenamiento de PyTorch a multi-GPU sin reescribirlo
- lanzar un entrenamiento con DeepSpeed desde un archivo de configuración

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: convertir un bucle de entrenamiento de PyTorch a multi-GPU sin reescribirlo; lanzar un entrenamiento con DeepSpeed desde un archivo de configuración | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml, setup.py
- **Etiquetas:** `training` `python` `pytorch`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [huggingface/accelerate](https://github.com/huggingface/accelerate)
- 🌐 Web: <https://huggingface.co/docs/accelerate>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/huggingface/accelerate/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
