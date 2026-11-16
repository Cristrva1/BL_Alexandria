[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 llama.cpp

> Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 135k | MIT | C++ | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## ¿Qué es?

Motor de inferencia de LLM y modelos de visión (VLM) en C/C++, mantenido por la organización ggml-org sobre la biblioteca de tensores ggml. Licencia MIT, desarrollo diario desde 2023 y primera versión 1.0.0 publicada en noviembre de 2026; es la base de muchas herramientas locales.

## ¿Qué hace?

Ejecuta modelos en formato GGUF en local o en la nube con configuración mínima: chat en terminal (`llama cli`), servidor con API compatible con OpenAI y una interfaz web integrada (`llama serve`). Descarga modelos directamente de Hugging Face con `-hf`. Sirve para probar modelos abiertos, servirlos a otras aplicaciones o integrarlos en software propio.

## ¿Cómo lo hace?

Implementación en C/C++ sin dependencias, con cuantización entera de 1,5 a 8 bits para reducir memoria. Optimiza Apple Silicon (NEON, Accelerate, Metal), x86 (AVX, AVX2, AVX512, AMX) y RISC-V, y tiene núcleos CUDA para NVIDIA, HIP para AMD, Vulkan y SYCL para GPU Intel; puede repartir capas entre CPU y GPU. Se instala con el script de llama.app, Docker, binarios precompilados o compilando desde el código.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Open WebUI](open-webui.md) | Interfaz de chat multiusuario conectada al servidor compatible con OpenAI de `llama serve` (combinación por arquitectura). | Arranca `llama serve` primero y registra su URL /v1 como conexión OpenAI en Open WebUI; evita choques de puerto (ambos suelen usar 8080). |
| [llmfit](llmfit.md) | llmfit detecta tu hardware y recomienda qué modelo y cuantización caben; lista llama.cpp entre sus proveedores locales. | Ejecuta llmfit antes de descargar modelos para elegir el GGUF adecuado. |
| [LibreChat](librechat.md) | LibreChat admite endpoints personalizados compatibles con OpenAI, como el de llama.cpp. | Servidor de llama.cpp accesible desde el contenedor de LibreChat; luego decláralo en `librechat.yaml`. |
| [litellm](litellm.md) | Poner el servidor de llama.cpp detrás de un proxy único con claves, límites y registro de gasto (combinación por arquitectura). | llama.cpp primero; añade su endpoint como modelo OpenAI-compatible en la configuración de LiteLLM. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (9). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[local-deep-research](local-deep-research.md) · [Marker](marker.md) · [OpenCursor](opencursor.md) · [PrivateGPT](private-gpt.md) · [Surya](surya.md) · [txtai](txtai.md) · [Unsloth](unsloth.md) · [whisper.cpp](whisper-cpp.md) · [Xinference](xinference.md)

**Notas:** Alternativas (elige una como motor principal): ollama, llamafile, localai.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.0.0 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ggml-org/llama.cpp/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige API remota; cómputo, memoria, disco y licencia de los pesos se revisan por separado |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No todos los modelos o backends ofrecen las mismas funciones de herramientas y visión |
| Coste | Sin pago a un modelo en la ruta básica. No exige API remota; cómputo, memoria, disco y licencia de los pesos se revisan por separado |
| Equipo | Preparación según la ruta elegida. Binario o compilación para tu sistema; modelo GGUF; memoria suficiente |

No todos los modelos o backends ofrecen las mismas funciones de herramientas y visión

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario o compilación para tu sistema
- modelo GGUF
- memoria suficiente

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ggml-org/llama.cpp/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar llama.cpp para mi objetivo y necesito pasos guiados. Lee https://github.com/ggml-org/llama.cpp/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta un GGUF pequeño y observa memoria y velocidad de respuesta.

**Qué comprobar:** Puedes generar texto y reconocer qué backend y modelo se utilizan.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Servir un modelo en CPU
- Comparar cuantizaciones de un mismo modelo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Servir un modelo en CPU; Comparar cuantizaciones de un mismo modelo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No todos los modelos o backends ofrecen las mismas funciones de herramientas y visión

## Stack y modelos

- **Stack:** Binario o compilación para tu sistema; modelo GGUF; memoria suficiente
- **Etiquetas:** `inference` `local` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [llamafile](llamafile.md) | 26.6k | Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. |
| [LocalAI](localai.md) | 50.4k | Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria. |

## Enlaces

- 🐙 GitHub: [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
- 🌐 Web: <https://llama.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ggml-org/llama.cpp/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
