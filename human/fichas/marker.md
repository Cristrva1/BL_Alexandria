[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Conversión de documentos para IA

# 🔄 Marker

> Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.9k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Conversor de documentos de Datalab que produce Markdown, JSON, fragmentos y HTML. El código es Apache 2.0, pero los pesos de los modelos usan una licencia OpenRAIL-M modificada (gratuita para investigación, uso personal y empresas pequeñas, con condiciones para el resto); activo (v2.2.0) y con API gestionada de pago.

## ¿Qué hace?

Convierte PDF, imágenes, PPTX, DOCX, XLSX, HTML y EPUB en cualquier idioma, da formato a tablas, formularios, ecuaciones, fórmulas en línea, enlaces y código, extrae imágenes y elimina encabezados y pies. Opcionalmente usa un LLM (`--use_llm`) para fusionar tablas entre páginas y mejorar matemáticas y formularios. Según su propio benchmark supera a MinerU y docling en precisión y velocidad [DATO NO VERIFICADO: benchmark del propio proyecto].

## ¿Cómo lo hace?

Biblioteca Python 3.10+ con PyTorch (`pip install marker-pdf`, `[full]` para formatos no PDF) que funciona en GPU, CPU o MPS. El modo `balanced` enruta páginas sencillas a extracción de texto con un modelo de diseño ONNX y las complejas al VLM Surya 2.5 (0,69B); el modo `vllm` aplica OCR por VLM a todas las páginas. Surya lanza su servidor automáticamente y necesita vLLM (GPU NVIDIA) o llama.cpp (CPU / Apple Silicon).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | Backend requerido por Surya en GPU NVIDIA para el modo VLM. | Instala vLLM en el mismo entorno o servidor antes de usar los modos `balanced` o `vllm`. |
| [llama.cpp](llama-cpp.md) | Backend de Surya en CPU o Apple Silicon. | Instala llama.cpp antes de la primera conversión. |
| [Pandoc](pandoc.md) | Publicar el Markdown resultante en DOCX, EPUB o LaTeX (combinación por arquitectura). | Encadénalos en un script. |
| [Surya](surya.md) | Combinación recíproca: Surya lo enlaza como «marker, del mismo equipo, usa los modelos de Surya para convertir PDF a Markdown». | Orden indicado desde Surya: Instala marker; usará Surya para OCR y layout. |

**Notas:** Alternativas (elige una): docling, mineru, pdf-craft. Se retiró llama-index por no estar documentado en el README actual.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v2.2.0 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/datalab-to/marker/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Código Apache-2.0; pesos con licencia modificada y condiciones comerciales según organización; LLM opcional puede usar proveedores de pago |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Instalar marker-pdf no completa por sí solo el backend de inferencia; verifica requisitos del modelo y su licencia antes de ampliar volumen |
| Coste | El coste depende del proveedor o la ruta. Código Apache-2.0; pesos con licencia modificada y condiciones comerciales según organización; LLM opcional puede usar proveedores de pago |
| Equipo | Preparación según la ruta elegida. Python; backend Surya con vLLM o llama.cpp según sistema; pesos; PDF de prueba |

Instalar marker-pdf no completa por sí solo el backend de inferencia; verifica requisitos del modelo y su licencia antes de ampliar volumen

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- backend Surya con vLLM o llama.cpp según sistema
- pesos
- PDF de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
pip install marker-pdf
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/datalab-to/marker/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Marker para mi objetivo y necesito pasos guiados. Lee https://github.com/datalab-to/marker/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte un PDF de dos páginas con una tabla y compara texto y columnas.

**Qué comprobar:** Puedes localizar errores y decidir si activar la mejora LLM.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Extraer contenido de informes
- Preparar documentos escaneados para búsqueda

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Extraer contenido de informes; Preparar documentos escaneados para búsqueda | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Instalar marker-pdf no completa por sí solo el backend de inferencia; verifica requisitos del modelo y su licencia antes de ampliar volumen

## Stack y modelos

- **Stack:** Python; backend Surya con vLLM o llama.cpp según sistema; pesos; PDF de prueba
- **Etiquetas:** `docs` `pdf` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Docling](docling.md) | 70.6k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |
| [MinerU](mineru.md) | 83.7k | Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes. |
| [pdf-craft](pdf-craft.md) | 6.7k | Herramienta para convertir libros escaneados en PDF a documentos editables mediante rutas de OCR y procesamiento. |

## Enlaces

- 🐙 GitHub: [datalab-to/marker](https://github.com/datalab-to/marker)
- 🌐 Web: <https://www.datalab.to>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/datalab-to/marker/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
