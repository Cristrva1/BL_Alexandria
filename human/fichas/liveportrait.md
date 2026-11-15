[🏠 Inicio](../README.md) › [🖼️ Generación de Imagen & Visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Rostros y retratos animados

# 🧑 LivePortrait

> Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen (humanos, pero también mascotas).

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 19.4k | Otra (ver repo) | Python | 2026-06-01 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Qué es

Convierte una foto en un avatar que sigue las expresiones de un "conductor".

## Por qué destaca

Ofrece animación facial rápida y controlable (con retoque de ojos y boca vía "stitching" y retargeting), y ha sido adoptado por plataformas grandes (Kuaishou, Douyin, Jianying); es proyecto de KwaiVGI con pesos públicos.

## Cómo funciona

Usa un modelo de keypoints/warping implícito sobre PyTorch+GPU que deforma la cara de origen siguiendo el movimiento del conductor; un módulo de stitching suaviza la unión con el cuerpo y otro de retargeting controla ojos/boca de forma independiente.

## Instalación rápida

`git clone`, crear entorno y `pip install -r requirements.txt`; descargar los pesos preentrenados indicados en el repo. Requiere GPU NVIDIA con VRAM generosa.

## Casos de uso

- Convertir una foto en avatar/recurso animado
- Presentadores virtuales a partir de un retrato
- Animar ilustraciones de personajes para reels

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| animas retratos a partir de una foto | necesitas swap en vivo (Deep-Live-Cam) o no tienes GPU |

**Limitaciones:** GPU obligatoria; la calidad cae con poses extremas o rostros muy distintos al conductor; revisar licencia antes de uso comercial.

## Stack y modelos

- **Stack:** Python, PyTorch, GPU
- **Modelos / API:** Modelos locales.
- **Etiquetas:** `image` `vision` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MoviePy](moviepy.md) | 15.1k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Enlaces

- 🐙 GitHub: [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait)
- 🌐 Web: <https://liveportrait.github.io>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
