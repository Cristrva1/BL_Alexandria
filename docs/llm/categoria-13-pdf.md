# Alexandría para agentes · Herramientas PDF

Categoría 13 «PDF, OCR y procesamiento de documentos» › subcategoría `pdf`. 6 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=13&sub=pdf · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `stirling-pdf` | Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar… | 1 Básico | 76 | MIT + licencia propietaria (app/proprietary/, app/saas/) (open-core) | recomendado |
| `pdfmathtranslate` | Traduce papers en PDF conservando el formato, fórmulas y figuras, con versión… | 1 Básico | 68 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `docuseal` | Aplicación para preparar formularios y gestionar la firma electrónica de… | 3 Avanzado | 64 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `documenso` | Plataforma abierta de firma electrónica para enviar un PDF a firmantes por… | 3 Avanzado | 56 | AGPL-3.0 (open-core) | sin grupo |
| `pdfcraft` | Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para… | 1 Básico | 55 | AGPL-3.0 (OSI copyleft) | alternativa |
| `pdfding` | Gestor, visor y editor de PDF autoalojado (AGPL-3.0) con colecciones… | 1 Básico | 45 | AGPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Stirling-PDF (`stirling-pdf`)

- **Repo:** https://github.com/Stirling-Tools/Stirling-PDF · MIT + licencia propietaria (app/proprietary/, app/saas/) · nivel 1 · 76/100 · recomendado en «Suites de herramientas PDF»
- **Qué es:** Plataforma de edición de PDF de código abierto con modelo «open core» de Stirling Tools (licencia mixta; ver LICENSE). Muy activa (v3.3.0), con planes de servidor y Enterprise de pago.
- **Cuándo elegirlo:** Casos: Preparar un expediente de prueba; Separar y convertir documentos desde una interfaz.
- **Requisitos:** nivel 1: preparación sencilla; Docker o app oficial; PDFs ficticios; almacenamiento persistente si usas servidor; hardware prerequisites; API de IA: no; Docker o app oficial; PDFs ficticios; almacenamiento persistente si usas servidor.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -p 8080:8080 docker.stirlingpdf.com/stirlingtools/stirling-pdf` — fuente: https://github.com/Stirling-Tools/Stirling-PDF/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Une dos PDFs de prueba y verifica orden, páginas y metadatos del resultado Éxito: El archivo final se abre y contiene las páginas esperadas
- **Combina con:** `ocrmypdf` [13/ocr], `activepieces` [1/motores], `paperless-ngx` [13/gestion], `docuseal`
- **Alternativas:** `pdfcraft`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativa (elige una): pdfcraft. La edición de PDF, firma y redacción tienen efectos distintos: comprueba la salida de la operación elegida antes de sustituir un archivo.

### PDFMathTranslate (`pdfmathtranslate`)

- **Repo:** https://github.com/PDFMathTranslate/PDFMathTranslate · AGPL-3.0 · nivel 1 · 68/100
- **Qué es:** Herramienta de código abierto (AGPL-3.0) para traducir PDF científicos conservando el diseño, también conocida como pdf2zh. Muy activa (v1.9.11) y con servicio público gratuito en línea.
- **Cuándo elegirlo:** Casos: Leer un artículo en otro idioma; Crear una versión bilingüe de documentación propia.
- **Requisitos:** nivel 1: preparación sencilla; Python 3.11–3.12; proveedor de traducción u Ollama; PDF de prueba; hardware prerequisites; API de IA: depends; Python 3.11–3.12; proveedor de traducción u Ollama; PDF de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/PDFMathTranslate/PDFMathTranslate/blob/main/README.md

  ```bash
  pip install uv
     uv tool install --python 3.12 pdf2zh
  ```
- **Primera prueba propuesta (no ejecutada):** Traduce dos páginas con fórmulas y compara texto, nombres y disposición con el original Éxito: Puedes detectar traducciones incorrectas sin confundirlas con cambios de formato
- **Combina con:** `pdf-inspector` [13/conversion], `ollama` [8/motores], `litellm` [23/serving]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. El servicio público en línea procesa tus documentos en servidores ajenos. MCP stdio está documentado; conservar fórmulas y formato es un objetivo, no garantía de traducción técnica correcta.

### docuseal (`docuseal`)

- **Repo:** https://github.com/docusealco/docuseal · AGPL-3.0 · nivel 3 · 64/100
- **Qué es:** Plataforma de código abierto (AGPL-3.0) para rellenar y firmar documentos, de DocuSeal. Activa (3.3.6), con nube de pago y funciones Pro.
- **Cuándo elegirlo:** Casos: Preparar formularios internos de prueba; Evaluar un flujo de firma documental.
- **Requisitos:** nivel 3: preparación pesada; Docker; dominio y correo solo para despliegue real; documento y destinatario ficticios; hardware prerequisites; API de IA: no; Docker; dominio y correo solo para despliegue real; documento y destinatario ficticios.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run --name docuseal -p 3000:3000 -v.:/data docuseal/docuseal` — fuente: https://github.com/docusealco/docuseal/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una plantilla de prueba con campos de texto y firma y completa una vista de ensayo Éxito: Puedes revisar el documento resultante y la ubicación de los campos
- **Combina con:** `activepieces` [1/motores], `twenty-main` [18/crm], `stirling-pdf`, `pdfcraft`
- **Alternativas:** `documenso`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Para producción usa PostgreSQL en lugar de SQLite y configura SMTP con SPF/DKIM. El ejemplo es para revisar la herramienta con datos de prueba; configura dominio, persistencia y permisos antes de un uso real.

### Documenso (`documenso`)

- **Repo:** https://github.com/documenso/documenso · AGPL-3.0 · nivel 3 · 56/100
- **Qué es:** Alternativa de código abierto a DocuSign para gestionar firmas electrónicas de documentos PDF.
- **Cuándo elegirlo:** Casos: Recoger la firma de un acuerdo de prueba entre dos personas de tu equipo; Preparar una plantilla con campos de firma y fecha para reutilizarla. Evítalo si solo necesitas firmar algún PDF suelto y no quieres mantener un servidor con base de datos y correo.
- **Requisitos:** nivel 3: preparación pesada; TypeScript, package.json; hardware prerequisites; API de IA: opcional.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/documenso/documenso/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** En la instalación local de desarrollo, crea una cuenta con un correo ficticio y confírmala desde http://localhost:9000. Sube un PDF propio de una página, añade como firmante a «Firmante Ficticio»… Éxito: En http://localhost:9000 abre el correo del firmante y firma. El documento pasa a completado y el PDF descargado…
- **Combina con:** `stirling-pdf`, `paperless-ngx` [13/gestion], `activepieces` [1/motores]
- **Alternativas:** `docuseal`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

### pdfcraft (`pdfcraft`)

- **Repo:** https://github.com/PDFCraftTool/pdfcraft · AGPL-3.0 · nivel 1 · 55/100 · alternativa en «Suites de herramientas PDF»
- **Qué es:** Suite de herramientas PDF en el navegador de PDFCraftTool, AGPL-3.0, activa con versiones por fecha. Tiene un proyecto hermano de escritorio, LibrePDF (Apache 2.0).
- **Cuándo elegirlo:** Casos: Editar PDFs desde un navegador; Convertir o dividir un documento de prueba.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Navegador moderno; PDFs de prueba; Node solo para self-hosting; hardware prerequisites; API de IA: no; Navegador moderno; PDFs de prueba; Node solo para self-hosting.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull ghcr.io/pdfcrafttool/pdfcraft:latest` — fuente: https://github.com/PDFCraftTool/pdfcraft/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre dos PDFs en la app y combínalos sin usar un servicio externo de conversión Éxito: Puedes descargar el resultado y comprobar páginas y orden
- **Combina con:** `coolify` [22/infraestructura], `docuseal`, `paperless-ngx` [13/gestion]
- **Alternativas:** `stirling-pdf`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativa (elige una): stirling-pdf. Se retiró markitdown por falta de relación. La referencia a Ollama corresponde al proyecto relacionado LibrePDF, no demuestra esa función en PDFCraft web.

### PdfDing (`pdfding`)

- **Repo:** https://github.com/mrmn2/PdfDing · AGPL-3.0 · nivel 1 · 45/100
- **Qué es:** Gestor, visor y editor de PDF autoalojado (AGPL-3.0), creado por mrmn y financiado por el NGI0 Commons Fund de NLnet. Su repositorio canónico es Codeberg (codeberg.org/mrmn/PdfDing), donde sigue activo con la v1.15.0 del 1 de noviembre de…
- **Cuándo elegirlo:** Casos: Organizar una colección de PDFs; Consultar documentos desde varios dispositivos.
- **Requisitos:** nivel 1: preparación sencilla; Docker o entorno de la guía; volumen para documentos; cuenta de prueba; hardware prerequisites; API de IA: no; Docker o entorno de la guía; volumen para documentos; cuenta de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://docs.pdfding.com/getting_started/docker/

  ```bash
  docker run --name pdfding \
      -p 8000:8000 \
      -v sqlite_data:/home/nonroot/pdfding/db -v media:/home/nonroot/pdfding/media \
      -e HOST_NAME=127.0.0.1 -e SECRET_KEY=some_secret \
      -e CSRF_COOKIE_SECURE=FALSE -e SESSION_COOKIE_SECURE=FALSE \
      -d \
      mrmn/pdfding:latest
  ```
- **Primera prueba propuesta (no ejecutada):** Sube un PDF ficticio, añade una etiqueta y continúa su lectura en otra sesión Éxito: Puedes encontrar el documento y su progreso guardado
- **Combina con:** `ocrmypdf` [13/ocr], `paperless-ngx` [13/gestion], `coolify` [22/infraestructura]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Fuente canónica: Codeberg. El repositorio de GitHub está archivado y solo se conserva como identidad de la estrella en el catálogo (`gh`, `github_id`); las…. El repositorio de GitHub está archivado desde que el proyecto se mudó a Codeberg; usa Codeberg y docs.pdfding.com como referencia. Sin OCR ni IA integrados.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-13-pdf.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Herramientas PDF», lee `docs/alexandria/categoria-13-pdf.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-13-pdf.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
