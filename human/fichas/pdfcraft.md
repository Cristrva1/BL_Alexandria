[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Herramientas PDF

# 📄 pdfcraft

> Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada.

## Cuándo elegir esta ficha

Ambos nombres se parecen, con IDs, upstreams, flujos y licencias distintos. El editor web cubre utilidades PDF, la librería prepara Markdown y EPUB desde escaneos.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/PDFCraftTool/pdfcraft/blob/50aef68b77f7f6286862b3f648a8b49cde7cddad/README.md) · [Fuente 2](https://api.github.com/repos/PDFCraftTool/pdfcraft) · [Fuente 3](https://github.com/PDFCraftTool/pdfcraft/commit/50aef68b77f7f6286862b3f648a8b49cde7cddad)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.8k | AGPL-3.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 54/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Suite de herramientas PDF en el navegador de PDFCraftTool, AGPL-3.0, activa con versiones por fecha. Tiene un proyecto hermano de escritorio, LibrePDF (Apache 2.0).

## ¿Qué hace?

Ofrece más de 80 herramientas para unir, dividir, comprimir, convertir, rotar y editar PDF directamente en el navegador, sin subir archivos a servidores. Interfaz en ocho idiomas, entre ellos español.

## ¿Cómo lo hace?

Aplicación Next.js con Tailwind CSS que procesa los archivos en el cliente con WebAssembly y bibliotecas como pdf-lib. Se despliega como sitio estático o con la imagen Docker `ghcr.io/pdfcrafttool/pdfcraft` (por ejemplo en el puerto 8080) o Docker Compose.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [coolify](coolify.md) | Autoalojar la imagen Docker con dominio y HTTPS (combinación por arquitectura). | Crea el servicio desde la imagen en Coolify. |
| [docuseal](docuseal.md) | Preparar el PDF (unir, comprimir) antes de enviarlo a firmar (combinación por arquitectura). | Independientes. |
| [paperless-ngx](paperless-ngx.md) | Ajustar documentos antes de archivarlos (combinación por arquitectura). | Independientes. |

**Notas:** Alternativa (elige una): stirling-pdf. Se retiró markitdown por falta de relación.

Estado en GitHub: activo · último push 2026-11-08 · última versión publicada v2026.11.08-98e89d4 (2026-11-08) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md)</sub>

## Ver similares

Grupo **Suites de herramientas PDF**: pdfcraft ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Stirling-PDF](stirling-pdf.md) ⭐ recomendado | 76 | Si buscas esto: aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. |
| 2 | **pdfcraft** (esta ficha) | 54 | Si buscas esto: conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las herramientas del navegador no requieren modelo; hosting propio y productos enlazados tienen condiciones aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La referencia a Ollama corresponde al proyecto relacionado LibrePDF, no demuestra esa función en PDFCraft web |
| Coste | Sin pago a un modelo en la ruta básica. Las herramientas del navegador no requieren modelo; hosting propio y productos enlazados tienen condiciones aparte |
| Equipo | Preparación según la ruta elegida. Navegador moderno; PDFs de prueba; Node solo para self-hosting |

La referencia a Ollama corresponde al proyecto relacionado LibrePDF, no demuestra esa función en PDFCraft web

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador moderno
- PDFs de prueba
- Node solo para self-hosting

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
docker pull ghcr.io/pdfcrafttool/pdfcraft:latest
```

Comando copiado literalmente de el README (sección «Option 1: Use Pre-built Image»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar pdfcraft para mi objetivo y necesito pasos guiados. Lee https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre dos PDFs en la app y combínalos sin usar un servicio externo de conversión.

**Qué comprobar:** Puedes descargar el resultado y comprobar páginas y orden.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Editar PDFs desde un navegador
- Convertir o dividir un documento de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Editar PDFs desde un navegador; Convertir o dividir un documento de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La referencia a Ollama corresponde al proyecto relacionado LibrePDF, no demuestra esa función en PDFCraft web

## Stack y modelos

- **Stack:** Navegador moderno; PDFs de prueba; Node solo para self-hosting
- **Etiquetas:** `pdf` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Stirling-PDF](stirling-pdf.md) | 96.6k | Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. |

## Enlaces

- 🐙 GitHub: [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft)
- 🌐 Web: <https://pdfcraft.devtoolcafe.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
