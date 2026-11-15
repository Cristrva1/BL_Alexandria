[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Restauración, upscaling y edición

# 🙂 GFPGAN

> Algoritmo de restauración facial de Tencent ARC que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 37.7k | Otra (ver repo) | Python | 2024-07-26 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Resuelve el problema concreto de las caras "fundidas" que aparecen al reescalar o comprimir fotos.

## Por qué destaca

Resuelve muy bien un problema acotado y es una utilidad ampliamente reutilizada como paso de postproceso en pipelines de imagen; cuenta con demos públicos (Hugging Face, Replicate) y se integra en muchas UIs de SD.

## Cómo funciona

Detecta el rostro, lo alinea y aplica una red GAN (GFPGANv1) sobre PyTorch (GPU opcional) que regenera detalle realista preservando la identidad; combina la salida con la imagen original para no alterar el resto.

## Instalación rápida

`pip install gfpgan` o `git clone` con sus dependencias; los pesos del modelo se descargan en el primer uso. En Windows puede necesitar compilación de extensiones de CUDA.

## Casos de uso

- Mejorar retratos/frames antes de reutilizarlos
- Recuperar rostros degradados en material antiguo
- Postproceso de caras generadas por SD

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| restauras rostros borrosos o fundidos | necesitas upscaling general de la imagen (Real-ESRGAN) |

## Stack y modelos

- **Stack:** Python, PyTorch, GPU opcional
- **Modelos / API:** Modelos locales.
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Real-ESRGAN](real-esrgan.md) | 37.4k | Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [CodeFormer](codeformer.md) | 18.2k | Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas. |

## Enlaces

- 🐙 GitHub: [TencentARC/GFPGAN](https://github.com/TencentARC/GFPGAN)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
