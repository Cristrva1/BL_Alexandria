[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Aprender LLMs desde cero

# 🔬 nanoGPT

> Implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 64.6k | MIT | Python | 2025-11-12 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Resuelve la opacidad de los frameworks: ves exactamente cómo se entrena un GPT sin capas de abstracción.

## Por qué destaca

Referencia didáctica de Karpathy ampliamente usada para aprender cómo funciona realmente el entrenamiento de un GPT, sin capas de abstracción. Su minimalismo (unos pocos cientos de líneas) lo hace el punto de partida habitual para entender y experimentar.

## Cómo funciona

Define el modelo GPT y su bucle de entrenamiento en PyTorch sobre GPU, reproduciendo resultados tipo GPT-2 con unos pocos cientos de líneas y dependencias mínimas.

## Instalación rápida

`git clone https://github.com/karpathy/nanoGPT` y `pip install torch numpy transformers datasets tiktoken`. Requiere GPU para entrenar (CPU solo sirve para pruebas triviales).

## Casos de uso

- Aprender cómo se entrena un GPT
- Experimentos pequeños reproducibles
- Base para afinar modelos propios sobre datos propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres entender el entrenamiento de un GPT desde cero | solo consumes modelos vía API o necesitas un pipeline de chat completo (nanochat) |

**Limitaciones:** Entrenar a escala real exige GPU y tiempo; no es una librería de producción, sino un recurso educativo minimalista.

## Stack y modelos

- **Stack:** Python, PyTorch, GPU
- **Modelos / API:** Entrena modelos propios.
- **Etiquetas:** `learning` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [nanochat](nanochat.md) | 60.4k | Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LLMs from Scratch](llms-from-scratch.md) | 108k | Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en PyTorch paso a paso. |

## Enlaces

- 🐙 GitHub: [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
