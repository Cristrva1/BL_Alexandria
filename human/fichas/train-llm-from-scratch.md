[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Aprender LLMs desde cero

# 🧑‍💻 train-llm-from-scratch

> Tutorial y código de PyTorch para construir y entrenar un modelo de lenguaje desde los datos hasta la generación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.2k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🔴 pesado

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Tutorial y código (MIT) de @FareedKhan-dev para entrenar un modelo de lenguaje desde cero en PyTorch puro. Empezó como tutorial de preentrenamiento y hoy cubre hasta modelos alineados de estilo razonador. Es activo (último push en octubre de 2026) y tiene CI.

## ¿Qué hace?

Implementa a mano, sin `trl`, `peft` ni `transformers`, todo el pipeline: modelo base → SFT → modelo de recompensa → PPO/DPO → GRPO → evaluación y chat. Tiene dos arquitecturas: el transformer original de 'Attention is All You Need' y una moderna con RoPE, RMSNorm, SwiGLU, atención agrupada y latente, Mixture of Experts y KV cache. Incluye una ruta para entrenar un modelo pequeño en CPU en minutos y tablas de GPU para modelos de hasta miles de millones de parámetros.

## ¿Cómo lo hace?

Paquete Python 3.10+ instalable con `pip install -e .`. La ruta de portátil no requiere GPU; los modelos grandes necesitan GPUs con mucha memoria, según la tabla del README. El código está pensado para leerse y aprender, no para entrenar en producción.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PyTorch](pytorch.md) | Única base del código. | Instala PyTorch (CPU o CUDA) antes de `pip install -e .`. |
| [TRL](trl.md) | Contrastar las implementaciones manuales de SFT, DPO, PPO y GRPO con la biblioteca de referencia. (combinación por arquitectura) | Úsala después para entrenar en serio. |
| [nanochat](nanochat.md) | Pipeline completo optimizado para comparar rendimiento y resultados. (combinación por arquitectura) | Opcional, como siguiente paso. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-10-02 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige API; GPU, almacenamiento y seguimiento externo opcional tienen sus costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Los extras train, ui, docs y all son alternativas; empezar por un corpus pequeño evita confundir la demostración con entrenar un modelo grande |
| Coste | El coste depende del proveedor o la ruta. No exige API; GPU, almacenamiento y seguimiento externo opcional tienen sus costes |
| Equipo | Preparación según la ruta elegida. Python y PyTorch; datos pequeños; CPU o GPU según escala |

Los extras train, ui, docs y all son alternativas; empezar por un corpus pequeño evita confundir la demostración con entrenar un modelo grande

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y PyTorch
- datos pequeños
- CPU o GPU según escala

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/FareedKhan-dev/train-llm-from-scratch.git
cd train-llm-from-scratch
pip install -e .
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar train-llm-from-scratch para mi objetivo y necesito pasos guiados. Lee https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala el paquete en un entorno de prueba y estudia la configuración de un entrenamiento mínimo.

**Qué comprobar:** Puedes identificar tamaño del modelo, datos y salida de checkpoints.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comprender la preparación de un corpus
- Explorar un entrenamiento pequeño controlado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comprender la preparación de un corpus; Explorar un entrenamiento pequeño controlado | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los extras train, ui, docs y all son alternativas; empezar por un corpus pequeño evita confundir la demostración con entrenar un modelo grande

## Stack y modelos

- **Stack:** Python y PyTorch; datos pequeños; CPU o GPU según escala
- **Etiquetas:** `aprender` `gemini` `large-language-models` `llm` `openai` `training` `transformers` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch)
- 🌐 Web: <https://fareedkhan-dev.github.io/train-llm-from-scratch/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/FareedKhan-dev/train-llm-from-scratch/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
