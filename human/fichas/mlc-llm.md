[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🧩 MLC LLM

> Motor universal de despliegue de LLM con compilación de ML: ejecuta modelos en GPU de escritorio, móviles y navegador con API compatible con OpenAI.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.4k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; necesita GPU

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Compilador de ML y motor de despliegue de código abierto (Apache-2.0) del proyecto MLC (CMU, OctoAI y comunidad), basado en Apache TVM. Activo; hermano de WebLLM para el navegador.

## ¿Qué hace?

Permite desarrollar, optimizar y desplegar modelos de lenguaje de forma nativa en muchas plataformas: GPU NVIDIA, AMD, Intel y Apple, móviles iOS y Android y navegadores con WebGPU. MLCEngine ofrece una API compatible con OpenAI por REST, Python, JavaScript, Swift y Kotlin.

## ¿Cómo lo hace?

Escrito en Python y C++ sobre TVM; se instala con wheels por plataforma según el quick start. Los modelos se convierten y compilan desde pesos de Hugging Face o se descargan precompilados; el servidor REST se lanza con `mlc_llm serve`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Transformers](transformers.md) | MLC LLM convierte y compila modelos a partir de pesos en formato Hugging Face (combinación por arquitectura). | Descarga los pesos del Hub; después conviértelos y compílalos con las herramientas de MLC LLM. |
| [Open WebUI](open-webui.md) | El servidor REST compatible con OpenAI de MLC LLM puede conectarse a Open WebUI como proveedor (combinación por arquitectura). | Arranca `mlc_llm serve`; después añade su URL como conexión OpenAI en Open WebUI. |
| [litellm](litellm.md) | LiteLLM puede enrutar peticiones al endpoint compatible con OpenAI de MLC LLM junto a otros proveedores (combinación por arquitectura). | Servidor MLC en marcha; después decláralo como modelo compatible con OpenAI en LiteLLM. |

**Notas:** La compilación requiere preparar el entorno de la GPU objetivo; usa modelos precompilados para la primera prueba.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mlc-ai/mlc-llm/blob/main/README.md) · [2](https://llm.mlc.ai/docs/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.

1. Elige el modelo y el backend que documenta el proyecto para tu sistema.
2. Prepara las dependencias y los pesos; no uses una cifra promocional como garantía para tu hardware.
3. Procesa una muestra pequeña y revisa calidad, tiempo y memoria antes de aumentar el tamaño de la tarea.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/mlc-ai/mlc-llm/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MLC LLM para mi objetivo y necesito pasos guiados. Lee https://github.com/mlc-ai/mlc-llm/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el quick start para instalar el paquete de tu plataforma y chatear con un modelo precompilado..

**Qué comprobar:** El modelo responde en local y el servidor REST devuelve respuestas al endpoint de chat..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- ejecutar un LLM en un móvil o en el navegador sin servidor
- servir un modelo en GPU AMD, Intel o Apple con una API compatible con OpenAI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: ejecutar un LLM en un móvil o en el navegador sin servidor; servir un modelo en GPU AMD, Intel o Apple con una API compatible con OpenAI | no quieres preparar modelos, dependencias y hardware propios |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, CMakeLists.txt, pyproject.toml
- **Etiquetas:** `inference` `python` `local` `model`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [mlc-ai/mlc-llm](https://github.com/mlc-ai/mlc-llm)
- 🌐 Web: <https://llm.mlc.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mlc-ai/mlc-llm/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
