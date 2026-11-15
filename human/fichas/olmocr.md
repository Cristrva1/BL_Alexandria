[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 olmOCR

> Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.8k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado

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

Pensado para crear datasets de entrenamiento a partir de millones de PDFs, con orden de lectura correcto.

## Por qué destaca

Calidad alta y coste por página muy bajo en lotes grandes.

## Cómo funciona

Un VLM afinado lee cada página como imagen y produce texto lineal; se sirve con vLLM.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install olmocr
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/allenai/olmocr/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar olmOCR para mi objetivo y necesito pasos guiados. Lee https://github.com/allenai/olmocr/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Convertir archivos de PDFs masivos
- Crear datasets de texto
- OCR de alta calidad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| procesas grandes volúmenes de PDFs con GPU | no tienes GPU; mira `ocrmypdf` o `tesseract` |

**Limitaciones:** Requiere GPU con bastante memoria.

## Stack y modelos

- **Stack:** Python, vLLM
- **Etiquetas:** `ocr` `pdf` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [vLLM](vllm.md) | 96.9k | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PaddleOCR](paddleocr.md) | 92.7k | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. |
| [Docling](docling.md) | 70.6k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |
| [Unlimited-OCR](unlimited-ocr.md) | 31.2k | Modelo de Baidu para parsear documentos largos de una sola pasada con visión. |

## Enlaces

- 🐙 GitHub: [allenai/olmocr](https://github.com/allenai/olmocr)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/allenai/olmocr/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
