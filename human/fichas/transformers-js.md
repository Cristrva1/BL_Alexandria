[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🏠 transformers.js

> Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.4k | Apache-2.0 | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca JavaScript oficial de Hugging Face para ejecutar modelos Transformers directamente en el navegador, sin servidor. Apache 2.0, madura y activa (v4.3.2); funcionalmente equivalente a la biblioteca `transformers` de Python.

## ¿Qué hace?

Ejecuta modelos preentrenados para NLP (clasificación, entidades, preguntas y respuestas, resumen, traducción, generación de texto), visión (clasificación, detección, segmentación, profundidad), audio (reconocimiento de voz, clasificación, texto a voz) y tareas multimodales (embeddings, clasificación zero-shot). Usa la misma API `pipeline` que la versión de Python.

## ¿Cómo lo hace?

Ejecuta los modelos con ONNX Runtime: por defecto en CPU vía WebAssembly y en GPU con WebGPU (`device: 'webgpu'`). Los modelos de PyTorch, TensorFlow o JAX se convierten a ONNX con Optimum. Se instala con `npm i @huggingface/transformers` o se importa desde CDN como módulo ES.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Qdrant](qdrant.md) | Generar embeddings en el cliente o en Node.js y guardarlos en una base vectorial (combinación por arquitectura). | Elige el modelo de embeddings primero; la dimensión de la colección de Qdrant debe coincidir. |
| [supabase](supabase.md) | Generar embeddings y guardarlos en Postgres con pgvector en Supabase (combinación por arquitectura). | Activa pgvector en Supabase y crea la tabla con la dimensión del modelo. |
| [whisper](whisper.md) | Ejecutar modelos Whisper convertidos a ONNX para transcribir en el navegador (combinación por arquitectura). | Usa las variantes ONNX publicadas en Hugging Face; las grandes requieren WebGPU. |

**Notas:** Se retiró la combinación antigua con swr por no tener relación con la inferencia.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada 4.3.2 (2026-10-28) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/huggingface/transformers.js/blob/main/README.md) · [2](https://huggingface.co/docs/transformers.js)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere API remota después de disponer de modelos y assets; cada modelo conserva su licencia; distribución y hardware pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No todos los Transformers se ejecutan sin conversión; confirma compatibilidad y backend WebGPU o WASM del modelo elegido |
| Coste | Sin pago a un modelo en la ruta básica. No requiere API remota después de disponer de modelos y assets; cada modelo conserva su licencia; distribución y hardware pueden costar |
| Equipo | Preparación según la ruta elegida. Node o navegador compatible; modelo ONNX admitido; RAM y descarga inicial |

No todos los Transformers se ejecutan sin conversión; confirma compatibilidad y backend WebGPU o WASM del modelo elegido

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node o navegador compatible
- modelo ONNX admitido
- RAM y descarga inicial

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm i @huggingface/transformers
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/huggingface/transformers.js/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar transformers.js para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/transformers.js/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta un pipeline de clasificación de texto sobre dos frases de prueba.

**Qué comprobar:** El modelo devuelve etiquetas que puedes comparar con las frases.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Clasificar texto en el navegador
- Procesar audio o imágenes sin servidor de modelos externo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Clasificar texto en el navegador; Procesar audio o imágenes sin servidor de modelos externo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No todos los Transformers se ejecutan sin conversión; confirma compatibilidad y backend WebGPU o WASM del modelo elegido

## Stack y modelos

- **Stack:** Node o navegador compatible; modelo ONNX admitido; RAM y descarga inicial
- **Etiquetas:** `motores` `browser` `javascript` `transformers` `webml`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [huggingface/transformers.js](https://github.com/huggingface/transformers.js)
- 🌐 Web: <https://huggingface.co/docs/transformers.js>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/huggingface/transformers.js/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
