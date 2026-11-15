[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Aprender LLMs desde cero

# ⚙️ llm.c

> Implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 31.4k | MIT | Cuda | 2025-06-26 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

## Qué es

Resuelve la abstracción total: muestra qué hace realmente la GPU en cada pasada, sin ocultarlo tras un framework.

## Por qué destaca

Referencia didáctica de Karpathy que reproduce GPT-2 con dependencias mínimas, ideal para entender qué hace realmente la GPU bajo el capó. Su valor educativo sobre el cómputo de bajo nivel es difícil de igualar en otros recursos.

## Cómo funciona

Escribe a mano los kernels de las pasadas forward/backward en C y CUDA, gestionando memoria y operaciones que normalmente oculta un framework como PyTorch, reproduciendo el entrenamiento de GPT-2.

## Instalación rápida

`git clone https://github.com/karpathy/llm.c`, instalar CUDA toolkit y compilar con `make`. Requiere una GPU NVIDIA con CUDA; sin él no tiene sentido.

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
- **Modelos / API:** Entrena modelos propios.
- **Etiquetas:** `learning`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [nanoGPT](nanogpt.md) | 64.6k | Implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo. |

## Enlaces

- 🐙 GitHub: [karpathy/llm.c](https://github.com/karpathy/llm.c)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
