[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🧠 Nemotron (NVIDIA)

> Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.3k | Apache-2.0 | Jupyter Notebook | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🔴 pesado

**Puntuación de calidad** 45/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Repositorio para desarrolladores de NVIDIA Nemotron, familia de modelos abiertos para IA agéntica: recetas de entrenamiento, guías de despliegue y ejemplos. Licencia Apache-2.0 (los pesos tienen sus propias licencias). Tiene ~2.3k estrellas y está activo.

## ¿Qué hace?

Documenta los modelos Nemotron 3.5 Super (120B-A12B, híbrido Mamba-Transformer con contexto de hasta 1M), Nemotron 3.5 Lightning (30B-A3B), Nemotron 3 Ultra y Nano Omni, con datos y técnicas de entrenamiento abiertas. Incluye un plugin de Claude Code (`nemotron-customize`) para construir pipelines de personalización.

## ¿Cómo lo hace?

Los modelos se descargan de Hugging Face y se despliegan en edge, una GPU o centro de datos, con NIM, TensorRT-LLM, vLLM o SGLang. Las recetas usan la pila NeMo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | Despliegue de los modelos. | Sirve el checkpoint con vLLM. |
| [NemoClaw](nemoclaw.md) | Inferencia gestionada en el stack de agentes de NVIDIA. (combinación por arquitectura) | Configura Nemotron como modelo. |
| [Claude Code](claude-code.md) | Plugin `nemotron-customize`. | Abre Claude Code en la raíz del repo e invoca la skill. |
| [NeMo Speech](nemo.md) | Pila de entrenamiento de las recetas. | Instala NeMo para reproducir recetas. |
| [cosmos](cosmos.md) | Combinación recíproca: cosmos lo enlaza como «Modelos de NVIDIA para agentes que orquestan la simulación. (combinación por arquitectura)». | Orden indicado desde cosmos: Usa Nemotron como planificador. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v0.2.0 (2026-10-15) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NVIDIA-NeMo/Nemotron/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Consultar es gratuito; modelos locales requieren hardware y proveedores remotos tienen sus condiciones; plugin usa el plan del agente |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es un centro de recursos con modelos y recetas distintas; el plugin nemotron-customize es para Claude Code y no implica compatibilidad automática de toda receta |
| Coste | El coste depende del proveedor o la ruta. Consultar es gratuito; modelos locales requieren hardware y proveedores remotos tienen sus condiciones; plugin usa el plan del agente |
| Equipo | Preparación según la ruta elegida. Navegador; modelo o receta elegida; GPU según tarea; Claude Code solo para plugin |

Es un centro de recursos con modelos y recetas distintas; el plugin nemotron-customize es para Claude Code y no implica compatibilidad automática de toda receta

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- modelo o receta elegida
- GPU según tarea
- Claude Code solo para plugin

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/NVIDIA-NeMo/Nemotron/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Nemotron (NVIDIA) para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA-NeMo/Nemotron/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una receta y usa su guía para identificar datos, checkpoint y recursos antes de ejecutarla.

**Qué comprobar:** Puedes diferenciar entrenamiento, adaptación e inferencia.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar modelos abiertos de NVIDIA
- Preparar un pipeline guiado de adaptación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar modelos abiertos de NVIDIA; Preparar un pipeline guiado de adaptación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un centro de recursos con modelos y recetas distintas; el plugin nemotron-customize es para Claude Code y no implica compatibilidad automática de toda receta

## Stack y modelos

- **Stack:** Navegador; modelo o receta elegida; GPU según tarea; Claude Code solo para plugin
- **Etiquetas:** `training` `inference`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [NVIDIA-NeMo/Nemotron](https://github.com/NVIDIA-NeMo/Nemotron)
- 🌐 Web: <https://docs.nvidia.com/nemotron/latest/index.html>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NVIDIA-NeMo/Nemotron/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
