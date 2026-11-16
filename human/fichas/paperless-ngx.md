[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Gestión y archivo de documentos

# ⚙️ paperless-ngx

> Gestor documental autoalojado para importar, reconocer texto, buscar y archivar documentos escaneados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 48.1k | GPL-3.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Puntuación de calidad** 73/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Sistema de gestión documental de código abierto (GPL-3.0), sucesor oficial de Paperless y Paperless-ng, mantenido por una comunidad. Muy activo (v3.4.2), con demo pública.

## ¿Qué hace?

Convierte documentos físicos en un archivo en línea buscable: aplica OCR, extrae texto, clasifica con etiquetas, corresponsales y tipos de documento, y permite buscar y gestionar todo desde una interfaz web. La lista completa de funciones está en su documentación.

## ¿Cómo lo hace?

Aplicación Django con Celery y Redis/Valkey; el OCR se hace con OCRmyPDF (dependencia del proyecto). Se despliega con Docker Compose mediante un script de instalación o los archivos de `docker/compose`, con variantes para PostgreSQL, MariaDB o SQLite, y opcionalmente Tika y Gotenberg para procesar documentos de Office y correos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OCRmyPDF](ocrmypdf.md) | Motor de OCR integrado. | Incluido; ajusta idiomas en la configuración. |
| [Tesseract](tesseract.md) | Motor usado por OCRmyPDF; los idiomas se añaden como paquetes de Tesseract. | Define `PAPERLESS_OCR_LANGUAGES` antes del primer arranque. |
| [ERPNext](erpnext.md) | Archivar facturas y justificantes que se registran en el ERP (combinación por arquitectura). | Define cuál es el sistema maestro de cada documento. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (5). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Apache Tika](tika.md) · [pdfcraft](pdfcraft.md) · [PdfDing](pdfding.md) · [Stirling-PDF](stirling-pdf.md) · [syncthing](syncthing.md)

**Notas:** Para varios usuarios usa la variante con PostgreSQL. La lista de proyectos relacionados está en su wiki.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.4.2 (2026-11-03) · licencia declarada GPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/paperless-ngx/paperless-ngx/blob/dev/README.md) · [2](https://github.com/paperless-ngx/paperless-ngx/tree/dev/docker/compose)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ruta básica usa OCR local sin API de IA; servidor, almacenamiento y copias requieren recursos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No es solo un conversor PDF: administra un archivo documental persistente; configura retención y copias antes de importar una colección real |
| Coste | Sin pago a un modelo en la ruta básica. La ruta básica usa OCR local sin API de IA; servidor, almacenamiento y copias requieren recursos |
| Equipo | Preparación según la ruta elegida. Docker o entorno de la guía; directorio persistente; idiomas OCR; documentos ficticios |

No es solo un conversor PDF: administra un archivo documental persistente; configura retención y copias antes de importar una colección real

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o entorno de la guía
- directorio persistente
- idiomas OCR
- documentos ficticios

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.paperless-ngx.com/setup/#installation)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar paperless-ngx para mi objetivo y necesito pasos guiados. Lee https://docs.paperless-ngx.com/setup/#installation. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Importa un documento de prueba y búscalo por una palabra reconocida y una etiqueta.

**Qué comprobar:** Puedes abrir el original y localizarlo con su texto OCR.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar recibos de prueba
- Construir un archivo documental buscable

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar recibos de prueba; Construir un archivo documental buscable | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No es solo un conversor PDF: administra un archivo documental persistente; configura retención y copias antes de importar una colección real

## Stack y modelos

- **Stack:** Docker o entorno de la guía; directorio persistente; idiomas OCR; documentos ficticios
- **Etiquetas:** `gestion` `server` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)
- 🌐 Web: <http://docs.paperless-ngx.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/paperless-ngx/paperless-ngx/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
