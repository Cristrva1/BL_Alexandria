[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 🔄 PDF Inspector

> Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con coordenadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 20k | MIT | Rust | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca en Rust de Firecrawl (MIT) para clasificar PDF y extraer su texto. Muy activa (v1.26.0) y disponible para Rust, CLI, Python, Node y WebAssembly en navegador.

## ¿Qué hace?

Detecta en 10–50 ms si un PDF es de texto, escaneado, de imagen o mixto, con puntuación de confianza y decisión de OCR por página, y convierte los PDF de texto a Markdown limpio en local en menos de 200 ms (encabezados, listas, código, tablas, negritas, varias columnas, texto RTL). Según Firecrawl evita servicios de OCR caros en cerca del 54 % de los PDF. Marca codificaciones de fuente rotas para recurrir a OCR y puede ejecutar OCR selectivo con PP-OCRv6 Small solo en las páginas que lo necesitan.

## ¿Cómo lo hace?

Analiza el documento una sola vez y comparte el resultado entre detección y extracción; usa los flujos de contenido del PDF, coordenadas y fuentes, detección de tablas por rectángulos y por alineación, y decodificación CID/ToUnicode. Se instala con `pip install pdf-inspector`, `npm install @firecrawl/pdf-inspector` o como crate de Rust.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [firecrawl](firecrawl.md) | Desarrollado por Firecrawl para procesar PDF de texto en local antes de recurrir a OCR. | Integrado en Firecrawl; úsalo directamente solo en canalizaciones propias. |
| [PDFMathTranslate](pdfmathtranslate.md) | El modo `--ultrafast` de PDFMathTranslate usa las posiciones de texto de pdf-inspector. | Viene como dependencia de PDFMathTranslate. |
| [PaddleOCR](paddleocr.md) | El OCR selectivo usa el modelo PP-OCRv6 Small de PaddleOCR. | Activa el OCR selectivo solo para páginas escaneadas. |
| [OCRmyPDF](ocrmypdf.md) | Enviar a OCRmyPDF los PDF clasificados como escaneados (combinación por arquitectura). | Clasifica primero; aplica OCR solo donde haga falta. |

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.26.0 (2026-11-14) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/firecrawl/pdf-inspector/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La extracción básica no exige API; OCR selectivo usa modelo local y requiere dependencias adicionales |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La instalación base y las funciones OCR no tienen los mismos recursos; la clasificación no verifica exactitud de todo el texto |
| Coste | Sin pago a un modelo en la ruta básica. La extracción básica no exige API; OCR selectivo usa modelo local y requiere dependencias adicionales |
| Equipo | Preparación según la ruta elegida. Python para esta ruta; runtime OCR y pesos solo si activas OCR; PDFs de prueba |

La instalación base y las funciones OCR no tienen los mismos recursos; la clasificación no verifica exactitud de todo el texto

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python para esta ruta
- runtime OCR y pesos solo si activas OCR
- PDFs de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install pdf-inspector
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/firecrawl/pdf-inspector/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PDF Inspector para mi objetivo y necesito pasos guiados. Lee https://github.com/firecrawl/pdf-inspector/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clasifica un PDF con texto y otro escaneado y compara el resultado.

**Qué comprobar:** Puedes enrutar el escaneado a OCR y extraer el otro sin ese procesamiento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Decidir cuándo hace falta OCR
- Extraer texto con posiciones de un PDF

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Decidir cuándo hace falta OCR; Extraer texto con posiciones de un PDF | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La instalación base y las funciones OCR no tienen los mismos recursos; la clasificación no verifica exactitud de todo el texto

## Stack y modelos

- **Stack:** Python para esta ruta; runtime OCR y pesos solo si activas OCR; PDFs de prueba
- **Etiquetas:** `pdf` `docs` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector)
- 🌐 Web: <https://firecrawl.github.io/pdf-inspector/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/firecrawl/pdf-inspector/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
