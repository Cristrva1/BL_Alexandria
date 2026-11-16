[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 📚 Xberg (antes Kreuzberg)

> Motor de extracción de documentos en Rust: texto, tablas y metadatos de más de 100 formatos, con OCR, transcripción, embeddings y MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.6k | MIT | Rust | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor de inteligencia documental de código abierto (MIT) de xberg-io. Es la nueva iteración de Kreuzberg, reconstruida y renombrada en una línea v1; la API de GitHub redirige el repositorio original a este nombre. Muy activo.

## ¿Qué hace?

Extrae texto limpio, tablas, metadatos y datos estructurados de 107 formatos (PDF, Office, imágenes, HTML, correo, e-books, publicaciones científicas, código fuente), recorre archivos comprimidos anidados con límites de seguridad, descarga y rastrea URL, transcribe audio y vídeo, aplica OCR bajo demanda y genera embeddings.

## ¿Cómo lo hace?

Núcleo en Rust; se instala con `pip install xberg`, npm, Homebrew, Docker o Helm, y funciona en CPU sin GPU. Ofrece biblioteca, CLI de 14 comandos, API REST (`xberg serve`), servidor MCP y skills de agente (`npx skills add xberg-io/xberg`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Xberg publica skills de agente (`npx skills add xberg-io/xberg`) y un servidor MCP para extraer documentos desde agentes de código. | Instala Xberg; después añade la skill o registra su servidor MCP en Claude Code. |
| [Tesseract](tesseract.md) | Tesseract es uno de los motores de OCR que Xberg usa bajo demanda para documentos escaneados. | Instala Tesseract y sus idiomas; después activa el backend en la configuración. |
| [Qdrant](qdrant.md) | Los fragmentos y embeddings que genera Xberg se pueden indexar en Qdrant para búsqueda semántica (combinación por arquitectura). | Extrae y vectoriza con Xberg; después sube los puntos a una colección de Qdrant. |

**Notas:** Alternativas (elige una): tika, unstructured. Proyectos que usaban Kreuzberg deben revisar la migración a la línea v1 de Xberg; la rama Kreuzberg v4 LTS sigue en kreuzberg-dev.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.4.0 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/xberg-io/xberg/blob/main/README.md) · [2](https://docs.xberg.io)</sub>

## Ver similares

Grupo **Conversión de documentos a Markdown/JSON para IA**: Xberg (antes Kreuzberg) ocupa la posición 3 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Docling](docling.md) ⭐ recomendado | 78 | Si necesitas PDF, DOCX y PPTX a Markdown/JSON con estructura, tablas y uso local. |
| 2 | [MinerU](mineru.md) | 68 | Si procesas PDF científicos o en chino con fórmulas y maquetación compleja. |
| 3 | **Xberg (antes Kreuzberg)** (esta ficha) | 63 | Si quieres un extractor en Rust con OCR, transcripción y MCP en un solo binario. |
| 4 | [Marker](marker.md) | 60 | Si conviertes PDF a Markdown con tablas, fórmulas y código, con GPU opcional. |
| 5 | [Apache Tika](tika.md) | 59 | Si necesitas extraer texto y metadatos de más de mil formatos en un servidor Java probado. |
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

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
pip install xberg
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/xberg-io/xberg/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Xberg (antes Kreuzberg) para mi objetivo y necesito pasos guiados. Lee https://github.com/xberg-io/xberg/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install xberg` y extrae el texto de un PDF y un DOCX de prueba..

**Qué comprobar:** Obtienes Markdown limpio con tablas y metadatos de ambos archivos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- preparar documentos variados (PDF, Office, correos, archivos comprimidos) para un sistema RAG
- extraer texto y tablas de escaneos con OCR en lote sin GPU

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: preparar documentos variados (PDF, Office, correos, archivos comprimidos) para un sistema RAG; extraer texto y tablas de escaneos con OCR en lote sin GPU | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Rust, Cargo.toml, composer.json, package.json, pyproject.toml
- **Etiquetas:** `docs` `rust` `pdf` `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Apache Tika](tika.md) | 4.2k | Kit de Apache que detecta y extrae texto y metadatos de más de mil tipos de archivo; desde 4.0 emite Markdown pensado para LLM y RAG. |
| [Unstructured](unstructured.md) | 15.7k | ETL open source que transforma documentos complejos en datos estructurados para LLM. |

## Enlaces

- 🐙 GitHub: [xberg-io/xberg](https://github.com/xberg-io/xberg)
- 🌐 Web: <https://docs.xberg.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/xberg-io/xberg/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
