[🏠 Inicio](../README.md) › [🧑‍💻 Entender código, trabajar con datos y entrenar modelos](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Aprender LLMs desde cero

# ⚙️ llm.c

> Implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.5k | MIT | Cuda | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve la abstracción total: muestra qué hace realmente la GPU en cada pasada, sin ocultarlo tras un framework.

## Por qué destaca

Referencia didáctica de Karpathy que reproduce GPT-2 con dependencias mínimas, ideal para entender qué hace realmente la GPU bajo el capó. Su valor educativo sobre el cómputo de bajo nivel es difícil de igualar en otros recursos.

## Cómo funciona

Escribe a mano los kernels de las pasadas forward/backward en C y CUDA, gestionando memoria y operaciones que normalmente oculta un framework como PyTorch, reproduciendo el entrenamiento de GPT-2.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/karpathy/llm.c/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar llm.c para mi objetivo y necesito pasos guiados. Lee https://github.com/karpathy/llm.c/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Entrenar GPT-2 con mínima dependencia
- Entender el cómputo de bajo nivel
- Enseñar qué hace realmente un framework bajo el capó

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres bajo nivel sin abstracciones y tienes GPU CUDA | prefieres PyTorch (nanoGPT) o no tienes CUDA |

**Limitaciones:** Exige GPU NVIDIA con CUDA y toolkit instalado; no es portable a otras arquitecturas y no busca ser productivo, sino pedagógico.

## Stack y modelos

- **Stack:** C, CUDA
- **Etiquetas:** `learning`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [nanoGPT](nanogpt.md) | 64.8k | Implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo. |

## Enlaces

- 🐙 GitHub: [karpathy/llm.c](https://github.com/karpathy/llm.c)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/karpathy/llm.c/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
