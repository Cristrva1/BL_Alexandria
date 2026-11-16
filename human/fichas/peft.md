[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ PEFT

> Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 21.9k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

PEFT, librería de Hugging Face para fine-tuning eficiente en parámetros (LoRA y similares). Licencia Apache-2.0. Es madura (~22k estrellas, v0.21.3).

## ¿Qué hace?

Adapta modelos grandes entrenando una pequeña fracción de parámetros, lo que reduce el coste de cómputo y almacenamiento. Gestiona adaptadores para entrenamiento e inferencia.

## ¿Cómo lo hace?

Se instala con `pip install peft` y está integrada con Transformers, Diffusers y Accelerate.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Transformers](transformers.md) | Integración nativa. | Instala Transformers primero. |
| [TRL](trl.md) | Entrenar con LoRA en SFT, DPO o GRPO. | Pasa la configuración de PEFT al trainer. |
| [diffusers](diffusers.md) | Gestión de adaptadores en modelos de difusión. | Carga adaptadores LoRA en el pipeline. |
| [LLaMA-Factory](llama-factory.md) | Combinación recíproca: LLaMA-Factory lo enlaza como «Métodos LoRA y QLoRA». | Orden indicado desde LLaMA-Factory: Viene como dependencia. |
| [airllm](airllm.md) | Combinación recíproca: airllm lo enlaza como «Entrenar adaptadores con pesos congelados por capas (combinación por arquitectura; [DATO NO VERIFICADO: si usa PEFT internamente])». | Orden indicado desde airllm: Fija las versiones de PEFT y transformers en el mismo entorno. |
| [bionemo-recipes](bionemo-recipes.md) | Combinación recíproca: bionemo-recipes lo enlaza como «Ajuste eficiente con datos propios. (combinación por arquitectura)». | Orden indicado desde bionemo-recipes: Aplica LoRA sobre el checkpoint. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Axolotl](axolotl.md) · [FinGPT](fingpt.md)

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.21.3 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/huggingface/peft/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Sin API de modelo alojado; entrenar y almacenar pesos requiere cómputo propio o alquilado |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Reducir parámetros entrenables no elimina toda la memoria del modelo base; los ejemplos de hardware no se generalizan a cualquier modelo |
| Coste | Sin pago a un modelo en la ruta básica. Sin API de modelo alojado; entrenar y almacenar pesos requiere cómputo propio o alquilado |
| Equipo | Preparación según la ruta elegida. Python; modelo Transformers; dataset; hardware suficiente |

Reducir parámetros entrenables no elimina toda la memoria del modelo base; los ejemplos de hardware no se generalizan a cualquier modelo

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- modelo Transformers
- dataset
- hardware suficiente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install peft
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/huggingface/peft/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PEFT para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/peft/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Estudia el ejemplo LoRA y comprueba qué parámetros serán entrenables.

**Qué comprobar:** Puedes distinguir modelo base de adaptador.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Ajustar un modelo con menos parámetros
- Reutilizar un adaptador entrenado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Ajustar un modelo con menos parámetros; Reutilizar un adaptador entrenado | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Reducir parámetros entrenables no elimina toda la memoria del modelo base; los ejemplos de hardware no se generalizan a cualquier modelo

## Stack y modelos

- **Stack:** Python; modelo Transformers; dataset; hardware suficiente
- **Etiquetas:** `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [huggingface/peft](https://github.com/huggingface/peft)
- 🌐 Web: <https://huggingface.co/docs/peft>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/huggingface/peft/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
