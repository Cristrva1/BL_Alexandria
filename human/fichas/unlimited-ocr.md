[🏠 Inicio](../README.md) › [📄 Documentos & Presentaciones](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 Unlimited-OCR

> Modelo de Baidu para parsear documentos largos de una sola pasada con visión.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 31.1k | MIT | Python | 2026-11-09 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

## Qué es

Extrae texto y estructura de documentos de muchas páginas sin dividirlos, pensado para contexto largo.

## Por qué destaca

Enfoque de una sola pasada para documentos largos.

## Cómo funciona

Un modelo de visión-lenguaje procesa secuencias largas de páginas y genera el texto estructurado.

## Instalación rápida

Sigue el README para descargar el modelo y ejecutar la inferencia (requiere GPU).

## Casos de uso

- Parsear documentos largos
- Contratos de muchas páginas
- Investigación en OCR

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| procesas documentos muy largos con GPU | necesitas algo probado y ligero; mira `docling` |

**Limitaciones:** Requiere GPU; proyecto reciente.

## Stack y modelos

- **Stack:** Python, PyTorch
- **Modelos / API:** Modelo propio.
- **Etiquetas:** `ocr` `docs` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [cosmos](cosmos.md) | 12.3k | Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots. |
| [ComfyUI](comfyui.md) | 146k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [olmOCR](olmocr.md) | 19.8k | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. |
| [PaddleOCR](paddleocr.md) | 92.5k | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. |

## Enlaces

- 🐙 GitHub: [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
