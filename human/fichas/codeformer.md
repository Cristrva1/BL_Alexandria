[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Restauración, upscaling y edición

# 🩹 CodeFormer

> Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 18.2k | Otra (ver repo) | Python | 2025-11-18 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Recupera detalles de caras en fotos de baja calidad con buena fidelidad.

## Por qué destaca

Equilibrio configurable entre calidad y fidelidad al original.

## Cómo funciona

Transformer que busca en un diccionario aprendido de rasgos faciales para reconstruir la cara.

## Instalación rápida

Clona el repo, `pip install -r requirements.txt` y ejecuta `inference_codeformer.py`.

## Casos de uso

- Restaurar fotos familiares
- Mejorar rostros en imágenes generadas
- Limpiar fotos de baja calidad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres restaurar rostros | quieres escalar la imagen completa; mira `real-esrgan` |

**Limitaciones:** Licencia no comercial (S-Lab).

## Stack y modelos

- **Stack:** Python, PyTorch
- **Modelos / API:** Modelo propio.
- **Etiquetas:** `image` `vision` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Real-ESRGAN](real-esrgan.md) | 37.4k | Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [GFPGAN](gfpgan.md) | 37.7k | Algoritmo de restauración facial de Tencent ARC que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados. |

## Enlaces

- 🐙 GitHub: [sczhou/CodeFormer](https://github.com/sczhou/CodeFormer)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
