[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 PaddleOCR

> Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 92.7k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

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

Reconoce texto en más de 80 idiomas y analiza documentos con tablas y layout. Incluye modelos pequeños para dispositivos.

## Por qué destaca

Precisión muy alta, multilingüe y con modelos optimizados.

## Cómo funciona

Modelos de detección, reconocimiento y análisis de layout en PaddlePaddle.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PaddleOCR para mi objetivo y necesito pasos guiados. Lee https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- OCR de facturas y recibos
- Documentos multilingües
- OCR en dispositivos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas OCR preciso y multilingüe | solo quieres hacer buscables PDFs escaneados; mira `ocrmypdf` |

## Stack y modelos

- **Stack:** Python, PaddlePaddle
- **Etiquetas:** `ocr` `docs` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Docling](docling.md) | 70.6k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Tesseract](tesseract.md) | 77.5k | Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma. |
| [olmOCR](olmocr.md) | 19.8k | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. |
| [Unlimited-OCR](unlimited-ocr.md) | 31.2k | Modelo de Baidu para parsear documentos largos de una sola pasada con visión. |

## Enlaces

- 🐙 GitHub: [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- 🌐 Web: <https://www.paddleocr.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
