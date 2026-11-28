[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 📏 llmfit

> Inspector de hardware que estima qué modelos de lenguaje y cuantizaciones caben en tu CPU, RAM y GPU.

## Cuándo elegir esta ficha

Pasar a consultor previo de hardware dentro de IA local. Se perdería el inventario comparativo de cuantizaciones si se retira. Su README al corte también documenta que el modo benchmark coordina un proveedor en ejecución. Ollama y llama.cpp cubren la etapa de inferencia y permiten medir el uso real. Mantener como referencia visible antes de descargar.

Revisión documental del 2026-11-27. [Fuente 1](https://raw.githubusercontent.com/AlexsJones/llmfit/57048e7f888082da0e6b24cbbf4013feebfcef1a/README.md) · [Fuente 2](https://api.github.com/repos/AlexsJones/llmfit) · [Fuente 3](https://github.com/AlexsJones/llmfit/commit/57048e7f888082da0e6b24cbbf4013feebfcef1a)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39k | MIT | Rust | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de terminal de código abierto (MIT) escrita en Rust por Alex Jones que calcula qué LLM puede ejecutar tu hardware. Proyecto de 2026 muy activo (v1.1.20).

## ¿Qué hace?

Detecta CPU, RAM, GPU, VRAM y memoria unificada, puntúa cada modelo por calidad, velocidad, ajuste y contexto, y recomienda cuantizaciones (GGUF, AWQ, GPTQ, EXL2) que funcionarán bien. Admite varias GPU, modelos MoE, estimación de velocidad y planificación de modelos repartidos en varias máquinas (por ejemplo con Ray y vLLM). También permite medir tokens por segundo reales y aportar resultados al proyecto.

## ¿Cómo lo hace?

Ofrece una TUI interactiva (por defecto), un modo CLI clásico, un panel web y una API REST (`/api/v1/system`, `/api/v1/models`). Detecta NVIDIA CUDA, Apple Silicon, AMD ROCm e Intel OneAPI e integra proveedores locales como Ollama, llama.cpp, MLX, Docker Model Runner y LM Studio. Se instala con Homebrew, Scoop o desde sus binarios, en macOS, Linux y Windows.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor local soportado: elige con llmfit el modelo que cabe y descárgalo en Ollama. | Ollama instalado; ejecuta llmfit para decidir el modelo antes de `ollama pull`. |
| [llama.cpp](llama-cpp.md) | Proveedor local soportado para descargar y servir el GGUF recomendado. | Igual: primero la recomendación, luego la descarga. |
| [vLLM](vllm.md) | El README describe comprobar si un modelo cabe en varias máquinas con Ray y vLLM antes de lanzarlo. | Usa llmfit para planificar; despliega vLLM después. |
| [airllm](airllm.md) | Combinación recíproca: airllm lo enlaza como «Comprobar si un modelo cabe en memoria de forma normal antes de recurrir a la carga por capas, mucho más lenta (combinación por arquitectura)». | Orden indicado desde airllm: Ejecuta llmfit primero; usa AirLLM solo si el modelo no cabe. |
| [Jan](jan.md) | Combinación recíproca: Jan lo enlaza como «Elegir qué modelo y cuantización caben en tu equipo antes de descargarlos en Jan (combinación por arquitectura)». | Orden indicado desde Jan: Ejecuta llmfit primero; descarga en Jan el modelo recomendado. |
| [Text Generation WebUI](textgen.md) | Combinación recíproca: Text Generation WebUI lo enlaza como «Saber qué modelo y cuantización caben antes de descargar (combinación por arquitectura)». | Orden indicado desde Text Generation WebUI: Ejecuta llmfit primero. |

**Notas:** Las estimaciones de velocidad son proyecciones; contrástalas con la función de benchmark.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.1.20 (2026-11-03) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/AlexsJones/llmfit/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La estimación no necesita llamar a un LLM; descargar o ejecutar modelos añade recursos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Estima ajuste al hardware y velocidad; no mide por sí mismo la calidad del modelo en tu tarea |
| Coste | Sin pago a un modelo en la ruta básica. La estimación no necesita llamar a un LLM; descargar o ejecutar modelos añade recursos |
| Equipo | Preparación según la ruta elegida. Binario para tu sistema; acceso a datos de hardware |

Estima ajuste al hardware y velocidad; no mide por sí mismo la calidad del modelo en tu tarea

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario para tu sistema
- acceso a datos de hardware

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (sh):**

```
winget install --exact --id AlexsJones.llmfit
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/AlexsJones/llmfit/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar llmfit para mi objetivo y necesito pasos guiados. Lee https://github.com/AlexsJones/llmfit/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta el inspector y compara RAM y VRAM detectadas con tu equipo.

**Qué comprobar:** Las recomendaciones explican qué modelos y cuantizaciones podrían caber.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Elegir un modelo antes de descargarlo
- Comparar requisitos de dos cuantizaciones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Elegir un modelo antes de descargarlo; Comparar requisitos de dos cuantizaciones | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Estima ajuste al hardware y velocidad; no mide por sí mismo la calidad del modelo en tu tarea

## Stack y modelos

- **Stack:** Binario para tu sistema; acceso a datos de hardware
- **Etiquetas:** `inference` `local` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/AlexsJones/llmfit/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
