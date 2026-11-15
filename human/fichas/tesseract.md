[🏠 Inicio](../README.md) › [📄 Trabajar con documentos y presentaciones](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 Tesseract

> Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 77.5k | Apache-2.0 | C++ | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma. La precisión depende del idioma, el escaneo y la preparación de la imagen.

## Por qué destaca

Estable, gratuito y disponible en todos los sistemas.

## Cómo funciona

Procesa imágenes y produce texto reconocible que puedes buscar, copiar o integrar en otros programas.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/tesseract-ocr/tesseract/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Tesseract para mi objetivo y necesito pasos guiados. Lee https://github.com/tesseract-ocr/tesseract/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- OCR de imágenes simples
- Base para OCRmyPDF
- Digitalizar documentos sin GPU

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres OCR clásico sin GPU | tus documentos tienen layouts complejos; mira `paddleocr` |

## Stack y modelos

- **Stack:** C++
- **Etiquetas:** `ocr` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OCRmyPDF](ocrmypdf.md) | 35.3k | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PaddleOCR](paddleocr.md) | 92.7k | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. |

## Enlaces

- 🐙 GitHub: [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- 🌐 Web: <https://tesseract-ocr.github.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/tesseract-ocr/tesseract/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
