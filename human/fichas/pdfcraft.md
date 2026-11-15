[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Herramientas PDF

# 📄 pdfcraft

> Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.8k | AGPL-3.0 | TypeScript | 2026-06-23 |

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

Apunta a ser la alternativa local y sin nube a los servicios online de PDF.

## Por qué destaca

Todo el procesamiento ocurre en tu navegador, así que los documentos nunca salen de tu equipo ni dependen de un servicio de pago; útil para manipular PDFs sensibles sin subirlos a terceros.

## Cómo funciona

Carga el PDF en el cliente y manipula sus páginas con librerías JS de PDF (p. ej. pdf-lib) en el propio navegador, sin subir nada a la nube; las operaciones son por página o por documento completo.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un navegador compatible y un PDF de prueba.

1. Abre la web enlazada por el README para probar la interfaz sin desplegar el código.
2. Elige una operación sencilla, por ejemplo combinar o dividir archivos, y utiliza documentos de prueba.
3. Descarga y abre el resultado. El despliegue propio con Node o Docker es una ruta distinta que requiere preparación técnica.

[Instrucciones originales de instalación](https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://pdfcraft.devtoolcafe.com/en/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar pdfcraft para mi objetivo y necesito pasos guiados. Lee https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Combinar/dividir/convertir PDF sin subirlos a la nube
- Manipulación local de documentos sensibles
- Comprimir PDF antes de enviarlos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| manipulas PDFs con privacidad y sin instalar nada | necesitas conversión a Markdown para IA (markitdown) o edición de contenido (no solo manipulación de páginas) |

## Stack y modelos

- **Stack:** web/TS
- **Etiquetas:** `pdf` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [markitdown](markitdown.md) | 195k | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Stirling-PDF](stirling-pdf.md) | 96.6k | Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. |

## Enlaces

- 🐙 GitHub: [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft)
- 🌐 Web: <https://pdfcraft.devtoolcafe.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
