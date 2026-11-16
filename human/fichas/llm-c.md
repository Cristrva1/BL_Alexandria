[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Aprender LLMs desde cero

# ⚙️ llm.c

> Implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.5k | MIT | Cuda | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Puntuación de calidad** 52/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Implementación de entrenamiento de LLMs en C/CUDA puro (MIT) de Andrej Karpathy, sin PyTorch ni Python. Es un proyecto educativo y de investigación de rendimiento, poco activo: el último push es de junio de 2025.

## ¿Qué hace?

Se centra en el preentrenamiento, en particular en reproducir GPT-2 y GPT-3 (miniseries). La mejor introducción, según el README, es reproducir GPT-2 (124M). Incluye una versión fp32 'legacy' sencilla para aprender CUDA y una versión de precisión mixta para multi-GPU y multinodo, además de una ruta para CPU limitada.

## ¿Cómo lo hace?

Se compila con `make` (por ejemplo, `make train_gpt2fp32cu`). Requiere toolkit CUDA para GPU; para preparar datos y pesos de referencia se usan scripts Python (`pip install -r requirements.txt`, `dev/download_starter_pack.sh`). En CPU funciona, pero solo para demostraciones pequeñas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [nanochat](nanochat.md) | Pipeline completo y más reciente del mismo autor en PyTorch. (combinación por arquitectura) | Úsalo si quieres resultados completos sin escribir CUDA. |
| [LLMs from Scratch](llms-from-scratch.md) | Teoría y código PyTorch para entender lo que llm.c implementa a bajo nivel. (combinación por arquitectura) | Estudia primero la versión en PyTorch. |
| [PyTorch](pytorch.md) | El repositorio incluye una referencia en PyTorch para comparar resultados. (combinación por arquitectura) | Instálalo solo si quieres verificar contra la referencia. |

**Notas:** Sin alternativas declaradas. Mantenimiento bajo desde 2025.

Estado en GitHub: activo · último push 2025-06-26 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/karpathy/llm.c/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API; GPU, energía y alquiler de hardware pueden ser significativos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es un proyecto técnico de entrenamiento; no es una app de chat lista para personas sin programación |
| Coste | El coste depende del proveedor o la ruta. No necesita API; GPU, energía y alquiler de hardware pueden ser significativos |
| Equipo | Preparación según la ruta elegida. Compilador C; Python para preparación; CUDA y GPU para las rutas aceleradas |

Es un proyecto técnico de entrenamiento; no es una app de chat lista para personas sin programación

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Compilador C
- Python para preparación
- CUDA y GPU para las rutas aceleradas

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/karpathy/llm.c/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar llm.c para mi objetivo y necesito pasos guiados. Lee https://github.com/karpathy/llm.c/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee el ejemplo GPT-2 y localiza las operaciones de forward y backward antes de compilar.

**Qué comprobar:** Puedes relacionar las operaciones matemáticas con el código C.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar entrenamiento sin un framework pesado
- Comparar una implementación C con PyTorch

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar entrenamiento sin un framework pesado; Comparar una implementación C con PyTorch | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un proyecto técnico de entrenamiento; no es una app de chat lista para personas sin programación

## Stack y modelos

- **Stack:** Compilador C; Python para preparación; CUDA y GPU para las rutas aceleradas
- **Etiquetas:** `learning`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [karpathy/llm.c](https://github.com/karpathy/llm.c)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/karpathy/llm.c/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
