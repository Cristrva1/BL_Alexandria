[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ Unsloth

> App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 79.5k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; dominio especializado

**Puntuación de calidad** 82/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Unsloth, app de escritorio y librería para ejecutar y entrenar modelos en local, de unslothai. Tiene licencia dual: el núcleo es Apache-2.0 y componentes opcionales como la UI de Unsloth Studio son AGPL-3.0. Es muy popular (~80k estrellas) y sus releases siguen en beta (v0.1.917-beta).

## ¿Qué hace?

Ejecuta y entrena LLM, modelos de difusión, TTS, embeddings y de decisión en formatos GGUF, MLX y otros. Según el proyecto, el fine-tuning es unas 2 veces más rápido y usa ~70% menos VRAM sin perder precisión (afirmación propia). Exporta a GGUF, NVFP4 o FP8 y puede lanzar agentes sobre modelos locales (`unsloth start claude --model …`).

## ¿Cómo lo hace?

Hay apps nativas para Windows, macOS y Linux; la librería se instala con `uv pip install unsloth --torch-backend=auto`. Se apoya en PyTorch, Transformers y TRL, y conviene una GPU NVIDIA para entrenar. Ofrece notebooks gratuitos en Colab.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [TRL](trl.md) | Trainers SFT, GRPO y DPO sobre modelos cargados con Unsloth. | Instala TRL y entrena con sus trainers. |
| [Ollama](ollama.md) | Servir el GGUF exportado. | Exporta a GGUF e impórtalo en Ollama. |
| [llama.cpp](llama-cpp.md) | Inferencia del GGUF exportado. | Carga el GGUF con llama.cpp. |
| [Claude Code](claude-code.md) | Agente sobre un modelo local vía `unsloth start claude`. | Instala Claude Code y lanza con un modelo local. |
| [LLM Course](llm-course.md) | Combinación recíproca: LLM Course lo enlaza como «Fine-tuning eficiente usado en el notebook 'Fine-tune Llama 3.1 with Unsloth'». | Orden indicado desde LLM Course: Abre el notebook en Colab con GPU; instala Unsloth según indique. |
| [SGLang](sglang.md) | Combinación recíproca: SGLang lo enlaza como «Servir con SGLang modelos afinados con Unsloth. (combinación por arquitectura)». | Orden indicado desde SGLang: Afina y exporta con Unsloth y sirve los pesos con SGLang. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Text Generation WebUI](textgen.md)

**Notas:** Alternativas (elige una): llama-factory. La AGPL de Studio importa si redistribuyes la UI.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.1.917-beta (2026-11-11) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/unslothai/unsloth/blob/main/README.md)</sub>

## Ver similares

Grupo **Fine-tuning de LLM**: Unsloth ocupa la posición 1 de 4 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Unsloth** (esta ficha) ⭐ recomendado | 82 | Si quieres afinar LLM con menos VRAM y más velocidad en una sola GPU. |
| 2 | [Axolotl](axolotl.md) | 65 | Si quieres configuraciones YAML reproducibles para fine-tuning en varias GPU. |
| 3 | [LLaMA-Factory](llama-factory.md) | 60 | Si quieres una interfaz web para afinar cientos de modelos sin programar. |
| 4 | [torchtune](torchtune.md) | 52 | Si prefieres recetas nativas de PyTorch fáciles de modificar. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta local no exige API de pago; hardware, modelos y conexiones Cloud o ChatGPT tienen costes o cuotas propios |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Unsloth Start conecta Claude Code y Codex a modelos locales; los porcentajes de velocidad y memoria publicados dependen del modelo y hardware |
| Coste | El coste depende del proveedor o la ruta. La ruta local no exige API de pago; hardware, modelos y conexiones Cloud o ChatGPT tienen costes o cuotas propios |
| Equipo | Preparación según la ruta elegida. App para tu sistema; modelo que quepa en memoria; GPU según tarea |

Unsloth Start conecta Claude Code y Codex a modelos locales; los porcentajes de velocidad y memoria publicados dependen del modelo y hardware

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- App para tu sistema
- modelo que quepa en memoria
- GPU según tarea

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (powershell):**

```
winget install --id UnslothAI.Unsloth -e
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/unslothai/unsloth/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Unsloth para mi objetivo y necesito pasos guiados. Lee https://github.com/unslothai/unsloth/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga un modelo pequeño compatible y prueba una pregunta conocida antes de iniciar fine-tuning.

**Qué comprobar:** Puedes identificar modelo, formato y memoria utilizada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar inferencia local
- Preparar un ajuste fino pequeño

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar inferencia local; Preparar un ajuste fino pequeño | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Unsloth Start conecta Claude Code y Codex a modelos locales; los porcentajes de velocidad y memoria publicados dependen del modelo y hardware

## Stack y modelos

- **Stack:** App para tu sistema; modelo que quepa en memoria; GPU según tarea
- **Etiquetas:** `training` `local` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LLaMA-Factory](llama-factory.md) | 76k | Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código. |
| [Axolotl](axolotl.md) | 12.7k | Framework de post-entrenamiento de LLM por configuración YAML: ajuste completo, LoRA/QLoRA, DPO/GRPO, multimodal y entrenamiento distribuido. |
| [torchtune](torchtune.md) | 5.8k | Biblioteca nativa de PyTorch para post-entrenamiento de LLM con recetas de ajuste completo, LoRA/QLoRA, DPO y destilación; ya sin mantenimiento activo. |

## Enlaces

- 🐙 GitHub: [unslothai/unsloth](https://github.com/unslothai/unsloth)
- 🌐 Web: <https://unsloth.ai/docs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/unslothai/unsloth/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
