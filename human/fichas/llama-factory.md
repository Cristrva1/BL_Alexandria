[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ LLaMA-Factory

> Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 76k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

LlamaFactory, framework para fine-tuning unificado de más de 100 LLM y modelos de visión con CLI e interfaz web sin código, de @hiyouga. Licencia Apache-2.0. Es maduro (~76k estrellas, v0.9.5) y está citado por empresas como Amazon y NVIDIA.

## ¿Qué hace?

Admite SFT, preentrenamiento, reward modeling, PPO, DPO, KTO y otros métodos, con LoRA, QLoRA y entrenamiento completo. LlamaBoard (Gradio) permite configurar el entrenamiento sin código, e incluye inferencia con API estilo OpenAI.

## ¿Cómo lo hace?

Se instala desde el repo con pip (extras para métricas, DeepSpeed, etc.) o se usa en Colab o PAI-DSW. La inferencia rápida usa workers de vLLM o SGLang (`infer_backend: vllm`). El README promociona otro proyecto del autor (PenguinHarness) y a sus patrocinadores.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PEFT](peft.md) | Métodos LoRA y QLoRA. | Viene como dependencia. |
| [Transformers](transformers.md) | Modelos base. | Viene como dependencia. |
| [vLLM](vllm.md) | Worker de inferencia integrado. | Configura `infer_backend: vllm`. |
| [SGLang](sglang.md) | Worker de inferencia alternativo. | Configura el backend SGLang. |
| [Gradio](gradio.md) | Combinación recíproca: Gradio lo enlaza como «Su LlamaBoard está construido con Gradio». | Orden indicado desde Gradio: Usa la UI de LlamaFactory. |

**Notas:** Alternativas (elige una): unsloth.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.9.5 (2026-05-30) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/hiyouga/LlamaFactory/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige API de modelo remota; cómputo, almacenamiento y acceso a pesos son independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La interfaz reduce programación pero no elimina requisitos de memoria, licencia o evaluación de datos; no todas las configuraciones caben en un portátil |
| Coste | Sin pago a un modelo en la ruta básica. No exige API de modelo remota; cómputo, almacenamiento y acceso a pesos son independientes |
| Equipo | Preparación según la ruta elegida. Python; modelo y dataset autorizados; GPU y memoria según configuración |

La interfaz reduce programación pero no elimina requisitos de memoria, licencia o evaluación de datos; no todas las configuraciones caben en un portátil

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- modelo y dataset autorizados
- GPU y memoria según configuración

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone --depth 1 https://github.com/hiyouga/LlamaFactory.git
cd LlamaFactory
pip install -e .
pip install -r requirements/metrics.txt
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/hiyouga/LlamaFactory/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LLaMA-Factory para mi objetivo y necesito pasos guiados. Lee https://github.com/hiyouga/LlamaFactory/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre la interfaz y revisa un dataset pequeño antes de lanzar un ajuste LoRA.

**Qué comprobar:** Puedes identificar modelo base, datos y parámetros de entrenamiento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Ajustar un modelo con ejemplos propios
- Comparar un adaptador antes de exportarlo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Ajustar un modelo con ejemplos propios; Comparar un adaptador antes de exportarlo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La interfaz reduce programación pero no elimina requisitos de memoria, licencia o evaluación de datos; no todas las configuraciones caben en un portátil

## Stack y modelos

- **Stack:** Python; modelo y dataset autorizados; GPU y memoria según configuración
- **Etiquetas:** `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Unsloth](unsloth.md) | 79.5k | App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcionales. |

## Enlaces

- 🐙 GitHub: [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)
- 🌐 Web: <https://llamafactory.readthedocs.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/hiyouga/LlamaFactory/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
