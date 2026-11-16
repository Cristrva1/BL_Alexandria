[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Herramientas PDF

# 📑 Stirling-PDF

> Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 96.6k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 76/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de edición de PDF de código abierto con modelo «open core» de Stirling Tools (licencia mixta; ver LICENSE). Muy activa (v3.3.0), con planes de servidor y Enterprise de pago.

## ¿Qué hace?

Ofrece más de 50 herramientas para editar, unir, dividir, firmar, censurar, convertir, aplicar OCR y comprimir PDF, con canalizaciones sin código en la interfaz y API REST para casi todas. Funciona como app de escritorio, en el navegador o autoalojado con API privada; interfaz en más de 40 idiomas, y SSO y auditoría en la oferta Enterprise.

## ¿Cómo lo hace?

Servidor Java (imagen basada en Eclipse Temurin) con frontend TypeScript, que incluye en su imagen herramientas como OCRmyPDF, Tesseract, LibreOffice (vía unoserver), QPDF, Ghostscript, Calibre e ImageMagick. Arranque rápido con `docker run -p 8080:8080 docker.stirlingpdf.com/stirlingtools/stirling-pdf`; también desktop y Kubernetes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OCRmyPDF](ocrmypdf.md) | Incluido en la imagen para la herramienta de OCR. | No hace falta instalarlo aparte. |
| [activepieces](activepieces.md) | Automatizar conversiones u OCR masivo llamando a su API REST (combinación por arquitectura). | Protege la API con clave antes de exponerla. |
| [paperless-ngx](paperless-ngx.md) | Preparar o limpiar PDF antes de archivarlos (combinación por arquitectura). | Independientes; cambia el puerto 8080 si choca con otro servicio. |
| [docuseal](docuseal.md) | Combinación recíproca: docuseal lo enlaza como «Preparar o convertir documentos antes de enviarlos a firmar (combinación por arquitectura)». | Orden indicado desde docuseal: Independientes; cambia puertos si coinciden. |

**Notas:** Alternativa (elige una): pdfcraft.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v3.3.0 (2026-11-05) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Stirling-Tools/Stirling-PDF/blob/main/README.md) · [2](https://github.com/Stirling-Tools/Stirling-PDF/blob/main/docker/base/Dockerfile)</sub>

## Ver similares

Grupo **Suites de herramientas PDF**: Stirling-PDF ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Stirling-PDF** (esta ficha) ⭐ recomendado | 76 | Si buscas esto: aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. |
| 2 | [pdfcraft](pdfcraft.md) | 51 | Si buscas esto: conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El proyecto es open-core; Server y Enterprise tienen planes; la operación PDF básica no exige modelo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La edición de PDF, firma y redacción tienen efectos distintos: comprueba la salida de la operación elegida antes de sustituir un archivo |
| Coste | El coste depende del proveedor o la ruta. El proyecto es open-core; Server y Enterprise tienen planes; la operación PDF básica no exige modelo |
| Equipo | Preparación según la ruta elegida. Docker o app oficial; PDFs ficticios; almacenamiento persistente si usas servidor |

La edición de PDF, firma y redacción tienen efectos distintos: comprueba la salida de la operación elegida antes de sustituir un archivo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o app oficial
- PDFs ficticios
- almacenamiento persistente si usas servidor

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
docker run -p 8080:8080 docker.stirlingpdf.com/stirlingtools/stirling-pdf
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Stirling-Tools/Stirling-PDF/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Stirling-PDF para mi objetivo y necesito pasos guiados. Lee https://github.com/Stirling-Tools/Stirling-PDF/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Une dos PDFs de prueba y verifica orden, páginas y metadatos del resultado.

**Qué comprobar:** El archivo final se abre y contiene las páginas esperadas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un expediente de prueba
- Separar y convertir documentos desde una interfaz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un expediente de prueba; Separar y convertir documentos desde una interfaz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La edición de PDF, firma y redacción tienen efectos distintos: comprueba la salida de la operación elegida antes de sustituir un archivo

## Stack y modelos

- **Stack:** Docker o app oficial; PDFs ficticios; almacenamiento persistente si usas servidor
- **Etiquetas:** `pdf` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [pdfcraft](pdfcraft.md) | 9.8k | Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada. |

## Enlaces

- 🐙 GitHub: [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)
- 🌐 Web: <https://stirling.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Stirling-Tools/Stirling-PDF/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
