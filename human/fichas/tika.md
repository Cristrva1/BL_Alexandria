[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# ⚙️ Apache Tika

> Kit de Apache que detecta y extrae texto y metadatos de más de mil tipos de archivo; desde 4.0 emite Markdown pensado para LLM y RAG.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.2k | Apache-2.0 | Java | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto de la Apache Software Foundation (Apache-2.0), referencia histórica en extracción de contenido. Muy maduro; la serie 4.x se orienta a pipelines de agentes.

## ¿Qué hace?

Detecta el tipo y extrae texto y metadatos de más de mil formatos (PPT, XLS, PDF, imágenes, correos, archivos comprimidos). La versión 4 emite Markdown por defecto, analiza en procesos aislados ante fallos y añade parsers con modelos de visión para documentos difíciles.

## ¿Cómo lo hace?

Escrito en Java; se usa como biblioteca Maven, aplicación o tika-server por REST (también en Docker). El OCR clásico usa Tesseract instalado en el sistema; los parsers VLM necesitan credenciales del proveedor.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Tesseract](tesseract.md) | Tika usa Tesseract como motor de OCR para imágenes y PDF escaneados. | Instala Tesseract y sus idiomas en el sistema o la imagen; después activa el parser de OCR. |
| [paperless-ngx](paperless-ngx.md) | Paperless-ngx usa Apache Tika (con Gotenberg) para procesar documentos de Office y correos. | Despliega tika-server junto a Paperless-ngx y habilita su integración en la configuración. |
| [Claude Code](claude-code.md) | El README de Tika incluye una sección para usarlo desde agentes de IA, con salida Markdown estructurada. | Arranca tika-server; después indica al agente cómo llamar al endpoint de extracción. |

**Notas:** Alternativas (elige una): xberg, unstructured. Tika incluye subcomponentes con licencias propias (ver LICENSE).

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/apache/tika/blob/main/README.md) · [2](https://github.com/paperless-ngx/paperless-ngx/blob/dev/docs/configuration.md)</sub>

## Ver similares

Grupo **Conversión de documentos a Markdown/JSON para IA**: Apache Tika ocupa la posición 5 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Docling](docling.md) ⭐ recomendado | 78 | Si necesitas PDF, DOCX y PPTX a Markdown/JSON con estructura, tablas y uso local. |
| 2 | [MinerU](mineru.md) | 68 | Si procesas PDF científicos o en chino con fórmulas y maquetación compleja. |
| 3 | [Xberg (antes Kreuzberg)](xberg.md) | 63 | Si quieres un extractor en Rust con OCR, transcripción y MCP en un solo binario. |
| 4 | [Marker](marker.md) | 60 | Si conviertes PDF a Markdown con tablas, fórmulas y código, con GPU opcional. |
| 5 | **Apache Tika** (esta ficha) | 59 | Si necesitas extraer texto y metadatos de más de mil formatos en un servidor Java probado. |
| 6 | [Unstructured](unstructured.md) | 58 | Si quieres particionar muchos formatos en elementos para pipelines de RAG. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica y las funciones de IA se configuran por separado; activar un proveedor puede añadir credenciales y consumo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | El coste depende del proveedor o la ruta. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/apache/tika/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Apache Tika para mi objetivo y necesito pasos guiados. Lee https://github.com/apache/tika/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca tika-server con su imagen Docker o JAR y envía un PDF de prueba al endpoint de extracción..

**Qué comprobar:** El servidor devuelve el texto en Markdown y los metadatos del documento..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- extraer texto y metadatos de archivos heterogéneos en un pipeline de indexación
- alimentar un sistema RAG con Markdown generado desde documentos Office y PDF

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: extraer texto y metadatos de archivos heterogéneos en un pipeline de indexación; alimentar un sistema RAG con Markdown generado desde documentos Office y PDF | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Java, pom.xml
- **Etiquetas:** `docs` `java` `pdf` `server`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Xberg (antes Kreuzberg)](xberg.md) | 9.6k | Motor de extracción de documentos en Rust: texto, tablas y metadatos de más de 100 formatos, con OCR, transcripción, embeddings y MCP. |
| [Unstructured](unstructured.md) | 15.7k | ETL open source que transforma documentos complejos en datos estructurados para LLM. |

## Enlaces

- 🐙 GitHub: [apache/tika](https://github.com/apache/tika)
- 🌐 Web: <https://tika.apache.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/apache/tika/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
