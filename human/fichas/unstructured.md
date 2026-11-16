[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 🔄 Unstructured

> ETL open source que transforma documentos complejos en datos estructurados para LLM.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.7k | Apache-2.0 | HTML | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (Apache 2.0) de Unstructured.io para ingerir y preprocesar documentos e imágenes. Muy activa (0.27.x); la empresa ofrece modelos de mayor calidad en su API de pago Transform v2, y según su propia tabla la versión abierta queda claramente por debajo en tablas [DATO NO VERIFICADO: benchmark de la empresa].

## ¿Qué hace?

Particiona PDF, HTML, Word y muchos otros formatos en elementos tipados (títulos, párrafos, tablas, listas) listos para limpiar, trocear y cargar en canalizaciones de RAG o análisis. Se usa como etapa de preprocesado antes de generar embeddings.

## ¿Cómo lo hace?

Biblioteca Python instalable desde PyPI (con extras por formato) o en contenedor Docker multiplataforma (imagen basada en wolfi-base). Para imágenes necesita Tesseract y para PDF Tesseract y Poppler; otros formatos requieren dependencias del sistema como LibreOffice [DATO NO VERIFICADO: lista completa].

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Tesseract](tesseract.md) | Dependencia necesaria para OCR de imágenes y PDF. | Instala Tesseract (y sus paquetes de idioma) antes de procesar escaneados. |
| [langchain](langchain.md) | Usar los elementos particionados como cargador de documentos en canalizaciones de RAG (combinación por arquitectura). | Instala el paquete de integración en el mismo entorno. |
| [Qdrant](qdrant.md) | Guardar los fragmentos procesados con sus embeddings (combinación por arquitectura). | Define el troceado y el modelo de embeddings antes de crear la colección. |

**Notas:** Alternativa (elige una): docling. Se retiró llama-index por no estar documentado en el README.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada 0.27.37 (2026-11-06) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Unstructured-IO/unstructured/blob/main/README.md)</sub>

## Ver similares

Grupo **Conversión de documentos a Markdown/JSON para IA**: Unstructured ocupa la posición 6 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Docling](docling.md) ⭐ recomendado | 78 | Si necesitas PDF, DOCX y PPTX a Markdown/JSON con estructura, tablas y uso local. |
| 2 | [MinerU](mineru.md) | 68 | Si procesas PDF científicos o en chino con fórmulas y maquetación compleja. |
| 3 | [Xberg (antes Kreuzberg)](xberg.md) | 63 | Si quieres un extractor en Rust con OCR, transcripción y MCP en un solo binario. |
| 4 | [Marker](marker.md) | 60 | Si conviertes PDF a Markdown con tablas, fórmulas y código, con GPU opcional. |
| 5 | [Apache Tika](tika.md) | 59 | Si necesitas extraer texto y metadatos de más de mil formatos en un servidor Java probado. |
| 6 | **Unstructured** (esta ficha) | 58 | Si quieres particionar muchos formatos en elementos para pipelines de RAG. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La biblioteca local y la plataforma gestionada son rutas distintas; partición, enriquecimiento y modelos externos pueden consumir servicios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Instala dependencias del formato; el contenedor y la biblioteca no garantizan por sí solos todas las funciones de la plataforma |
| Coste | El coste depende del proveedor o la ruta. La biblioteca local y la plataforma gestionada son rutas distintas; partición, enriquecimiento y modelos externos pueden consumir servicios |
| Equipo | Preparación según la ruta elegida. Python; extras por formato; herramientas del sistema para PDF o imágenes |

Instala dependencias del formato; el contenedor y la biblioteca no garantizan por sí solos todas las funciones de la plataforma

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- extras por formato
- herramientas del sistema para PDF o imágenes

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install "unstructured[all-docs]"
```

Comando copiado literalmente de el README (sección «Installing the library»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/Unstructured-IO/unstructured/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Unstructured para mi objetivo y necesito pasos guiados. Lee https://github.com/Unstructured-IO/unstructured/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Divide un documento ficticio en elementos y comprueba título, párrafos y tabla.

**Qué comprobar:** Los elementos conservan el orden y tipos que necesitas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar documentos para una base de conocimiento
- Crear un pipeline ETL de archivos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar documentos para una base de conocimiento; Crear un pipeline ETL de archivos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Instala dependencias del formato; el contenedor y la biblioteca no garantizan por sí solos todas las funciones de la plataforma

## Stack y modelos

- **Stack:** Python; extras por formato; herramientas del sistema para PDF o imágenes
- **Etiquetas:** `docs` `data` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Docling](docling.md) | 70.6k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |
| [Xberg (antes Kreuzberg)](xberg.md) | 9.6k | Motor de extracción de documentos en Rust: texto, tablas y metadatos de más de 100 formatos, con OCR, transcripción, embeddings y MCP. |
| [Apache Tika](tika.md) | 4.2k | Kit de Apache que detecta y extrae texto y metadatos de más de mil tipos de archivo; desde 4.0 emite Markdown pensado para LLM y RAG. |

## Enlaces

- 🐙 GitHub: [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)
- 🌐 Web: <https://www.unstructured.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Unstructured-IO/unstructured/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
