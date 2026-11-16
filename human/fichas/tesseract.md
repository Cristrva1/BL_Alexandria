[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 Tesseract

> Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 77.5k | Apache-2.0 | C++ | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Motor de OCR de código abierto (Apache 2.0) con biblioteca `libtesseract` y programa `tesseract`; nacido en HP y desarrollado después por Google. Hoy lo lidera Stefan Weil y lo mantiene Zdenko Podobny; maduro (5.5.4).

## ¿Qué hace?

Reconoce texto en más de 100 idiomas con soporte Unicode a partir de PNG, JPEG, TIFF y otros formatos, y produce texto plano, hOCR, PDF buscable, TSV, ALTO y otros. Es la base de OCR de muchas herramientas de documentos.

## ¿Cómo lo hace?

Desde Tesseract 4 usa un motor de redes neuronales LSTM centrado en líneas, además del motor clásico de patrones. Necesita archivos `traineddata` por idioma (repositorios tessdata). Se instala con paquetes del sistema o compilando; se usa desde la CLI o la API C/C++, con wrappers en muchos lenguajes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OCRmyPDF](ocrmypdf.md) | OCRmyPDF usa Tesseract para añadir capas de texto a PDF. | Instala Tesseract y los idiomas primero. |
| [paperless-ngx](paperless-ngx.md) | Hace el OCR de Paperless a través de OCRmyPDF. | Incluido en la imagen de Paperless; añade idiomas con su configuración. |
| [Unstructured](unstructured.md) | Dependencia de unstructured para OCR de imágenes y PDF. | Instálalo antes de procesar escaneados. |

**Notas:** Alternativa (elige una): paddleocr. Para diseños complejos o escritura a mano rinde peor que los modelos VLM.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 5.5.4 (2026-10-28) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/tesseract-ocr/tesseract/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere API; modelos de idioma y procesamiento son locales |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es un motor OCR con modelos locales, no un LLM conversacional; la calidad depende de la imagen y el idioma configurado |
| Coste | Sin pago a un modelo en la ruta básica. No requiere API; modelos de idioma y procesamiento son locales |
| Equipo | Preparación según la ruta elegida. Binario o paquete; datos entrenados del idioma; imagen legible |

Es un motor OCR con modelos locales, no un LLM conversacional; la calidad depende de la imagen y el idioma configurado

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario o paquete
- datos entrenados del idioma
- imagen legible

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://tesseract-ocr.github.io/tessdoc/Installation.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Tesseract para mi objetivo y necesito pasos guiados. Lee https://tesseract-ocr.github.io/tessdoc/Installation.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Reconoce una imagen con una frase conocida y cuenta errores del resultado.

**Qué comprobar:** Puedes comprobar si idioma, orientación y resolución son adecuados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Digitalizar texto de una fotografía propia
- Incorporar OCR local a un script

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Digitalizar texto de una fotografía propia; Incorporar OCR local a un script | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un motor OCR con modelos locales, no un LLM conversacional; la calidad depende de la imagen y el idioma configurado

## Stack y modelos

- **Stack:** Binario o paquete; datos entrenados del idioma; imagen legible
- **Etiquetas:** `ocr` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PaddleOCR](paddleocr.md) | 92.7k | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. |

## Enlaces

- 🐙 GitHub: [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- 🌐 Web: <https://tesseract-ocr.github.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/tesseract-ocr/tesseract/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
