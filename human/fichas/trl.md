[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ TRL

> Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.7k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

TRL, librería de Hugging Face para post-entrenar modelos fundacionales (SFT, GRPO, DPO, reward modeling…). Licencia Apache-2.0. Es madura y muy activa (~20k estrellas, v1.18.0).

## ¿Qué hace?

Ofrece trainers como SFTTrainer, GRPOTrainer, DPOTrainer y RewardTrainer. AsyncGRPOTrainer, ya estable, separa la generación (en un servidor vLLM) del entrenamiento para acelerar GRPO.

## ¿Cómo lo hace?

Se instala con `pip install trl` y escala con Accelerate, DeepSpeed y PEFT. También tiene CLI.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Transformers](transformers.md) | Modelos base. | Instala Transformers. |
| [PEFT](peft.md) | LoRA y adaptadores. | Instala `peft`. |
| [Unsloth](unsloth.md) | Entrenamiento acelerado compatible con los trainers de TRL. | Carga el modelo con Unsloth y entrena con TRL. |
| [vLLM](vllm.md) | Generación en AsyncGRPOTrainer. | Levanta el servidor vLLM. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.18.0 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/huggingface/trl/blob/main/README.md) · [2](https://huggingface.co/docs/trl/async_grpo_trainer)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Entrenamiento propio sin API obligatoria; cómputo y posibles modelos de recompensa tienen costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. SFT, DPO y GRPO son métodos distintos; la disponibilidad de un trainer no garantiza una mejora sin evaluar el resultado |
| Coste | Sin pago a un modelo en la ruta básica. Entrenamiento propio sin API obligatoria; cómputo y posibles modelos de recompensa tienen costes |
| Equipo | Preparación según la ruta elegida. Python; Transformers; modelo y datos; GPU según método |

SFT, DPO y GRPO son métodos distintos; la disponibilidad de un trainer no garantiza una mejora sin evaluar el resultado

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- Transformers
- modelo y datos
- GPU según método

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install trl
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/huggingface/trl/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar TRL para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/trl/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige el ejemplo SFT y revisa formato de datos antes de probar métodos de recompensa.

**Qué comprobar:** Puedes relacionar datos, método y checkpoint.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender ajuste supervisado
- Estudiar DPO o GRPO

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender ajuste supervisado; Estudiar DPO o GRPO | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** SFT, DPO y GRPO son métodos distintos; la disponibilidad de un trainer no garantiza una mejora sin evaluar el resultado

## Stack y modelos

- **Stack:** Python; Transformers; modelo y datos; GPU según método
- **Etiquetas:** `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [huggingface/trl](https://github.com/huggingface/trl)
- 🌐 Web: <http://hf.co/docs/trl>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/huggingface/trl/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
