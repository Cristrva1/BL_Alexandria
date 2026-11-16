[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 OCRmyPDF

> Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 35.3k | MPL-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de línea de comandos de código abierto (MPL-2.0) que añade una capa de texto OCR a PDF escaneados. Muy madura (v17.14) y probada en millones de PDF.

## ¿Qué hace?

Genera PDF/A buscables, coloca el texto OCR bajo la imagen para copiar y pegar, conserva la resolución original, inserta el OCR sin pérdidas cuando puede, optimiza imágenes (a menudo reduce el tamaño), endereza y limpia páginas y corrige rotaciones. Reconoce más de 100 idiomas y procesa archivos de miles de páginas en local.

## ¿Cómo lo hace?

Programa Python que usa el motor Tesseract y reparte el trabajo entre todos los núcleos de CPU. Se instala con `apt install ocrmypdf`, Homebrew, pip o Docker (x64 y ARM) en Linux, Windows, macOS y FreeBSD; los idiomas se añaden instalando paquetes de Tesseract.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Tesseract](tesseract.md) | Es su motor de OCR. | Instala Tesseract y los idiomas necesarios antes (los paquetes del sistema lo hacen solos). |
| [paperless-ngx](paperless-ngx.md) | Paperless-ngx usa OCRmyPDF como dependencia para el OCR de documentos. | Viene incluido en Paperless; no lo instales aparte para ese uso. |
| [Stirling-PDF](stirling-pdf.md) | La imagen de Stirling PDF incluye OCRmyPDF para su herramienta de OCR. | Incluido en la imagen Docker. |
| [PDF Inspector](pdf-inspector.md) | Combinación recíproca: PDF Inspector lo enlaza como «Enviar a OCRmyPDF los PDF clasificados como escaneados (combinación por arquitectura)». | Orden indicado desde PDF Inspector: Clasifica primero; aplica OCR solo donde haga falta. |
| [PdfDing](pdfding.md) | Combinación recíproca: PdfDing lo enlaza como «Aplicar OCR a escaneados antes de subirlos para poder buscar y resaltar texto (combinación por arquitectura)». | Orden indicado desde PdfDing: Procesa los archivos antes de importarlos. |

**Notas:** Se retiró docling por no estar documentado.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v17.14.2 (2026-11-16) · licencia declarada MPL-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ocrmypdf/OCRmyPDF/blob/main/README.md) · [2](https://github.com/paperless-ngx/paperless-ngx/blob/dev/pyproject.toml)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita LLM ni API; procesamiento y paquetes locales consumen recursos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La capa OCR puede contener errores; instala el idioma correcto y conserva el PDF original |
| Coste | Sin pago a un modelo en la ruta básica. No necesita LLM ni API; procesamiento y paquetes locales consumen recursos |
| Equipo | Preparación según la ruta elegida. Python; Ghostscript; Tesseract; paquete del idioma; PDF de prueba |

La capa OCR puede contener errores; instala el idioma correcto y conserva el PDF original

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- Ghostscript
- Tesseract
- paquete del idioma
- PDF de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://ocrmypdf.readthedocs.io/en/latest/installation.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OCRmyPDF para mi objetivo y necesito pasos guiados. Lee https://ocrmypdf.readthedocs.io/en/latest/installation.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade OCR a una copia escaneada y busca una palabra que conoces.

**Qué comprobar:** Puedes seleccionar y buscar texto manteniendo la imagen de la página.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Hacer buscables documentos escaneados
- Preparar un archivo histórico propio para indexación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Hacer buscables documentos escaneados; Preparar un archivo histórico propio para indexación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La capa OCR puede contener errores; instala el idioma correcto y conserva el PDF original

## Stack y modelos

- **Stack:** Python; Ghostscript; Tesseract; paquete del idioma; PDF de prueba
- **Etiquetas:** `ocr` `pdf` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF)
- 🌐 Web: <http://ocrmypdf.readthedocs.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ocrmypdf/OCRmyPDF/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
