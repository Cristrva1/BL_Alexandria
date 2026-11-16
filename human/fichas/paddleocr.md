[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 PaddleOCR

> Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 92.7k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Kit de OCR y motor de IA documental de Baidu sobre PaddlePaddle, Apache 2.0. Muy usado (más de 6.000 repositorios dependientes según su insignia) y activo (v3.7.0, último push en septiembre de 2026).

## ¿Qué hace?

Convierte PDF e imágenes en JSON o Markdown listos para LLM: el VLM PaddleOCR-VL-1.6 (0,9B) para análisis de documentos, PP-StructureV3 para conversión con estructura más fina, y PP-OCRv6 para reconocimiento de texto en escenas en muchos idiomas. Según el README lo usan proyectos como Dify y RAGFlow.

## ¿Cómo lo hace?

Biblioteca Python sobre el framework PaddlePaddle, con modelos publicados en Hugging Face y ModelScope. La canalización HPD-Parsing admite servicio compatible con OpenAI e inferencia local con un runtime personalizado de vLLM [DATO NO VERIFICADO: requisitos de hardware por modelo].

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PDF Inspector](pdf-inspector.md) | pdf-inspector usa PP-OCRv6 Small para el OCR selectivo de páginas escaneadas. | Usa pdf-inspector para decidir qué páginas pasan por OCR. |
| [RAGFlow](ragflow.md) | El README cita RAGFlow entre los proyectos que lo integran. | Revisa en RAGFlow qué versión de PaddleOCR usa antes de mezclar instalaciones. |
| [dify](dify.md) | El README cita Dify entre los proyectos que lo integran. | Úsalo como servicio externo de OCR o herramienta dentro de los flujos. |
| [vLLM](vllm.md) | HPD-Parsing usa un runtime personalizado de vLLM para inferencia local. | Sigue la guía de HPD-Parsing; no mezcles con otra versión de vLLM en el mismo entorno. |

**Notas:** Alternativas (elige una): tesseract, olmocr, unlimited-ocr. Se retiró docling por no estar documentado.

Estado en GitHub: activo · último push 2026-09-16 · última versión publicada v3.7.0 (2026-06-11) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ruta local no exige API; GPU, modelos y servicios opcionales tienen requisitos y condiciones propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Elige OCR clásico, estructura o VLM según la tarea; no todos los pipelines tienen la misma instalación y memoria |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no exige API; GPU, modelos y servicios opcionales tienen requisitos y condiciones propios |
| Equipo | Preparación según la ruta elegida. Python y PaddlePaddle compatibles; modelo y paquete de idioma; imagen de prueba |

Elige OCR clásico, estructura o VLM según la tarea; no todos los pipelines tienen la misma instalación y memoria

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y PaddlePaddle compatibles
- modelo y paquete de idioma
- imagen de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/installation.en.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PaddleOCR para mi objetivo y necesito pasos guiados. Lee https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/installation.en.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Reconoce una página con texto y tabla y compara palabras y coordenadas con la imagen.

**Qué comprobar:** Puedes medir errores sobre un fragmento conocido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Digitalizar un formulario propio
- Extraer texto y estructura de una página escaneada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Digitalizar un formulario propio; Extraer texto y estructura de una página escaneada | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Elige OCR clásico, estructura o VLM según la tarea; no todos los pipelines tienen la misma instalación y memoria

## Stack y modelos

- **Stack:** Python y PaddlePaddle compatibles; modelo y paquete de idioma; imagen de prueba
- **Etiquetas:** `ocr` `docs` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Tesseract](tesseract.md) | 77.5k | Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma. |
| [olmOCR](olmocr.md) | 19.8k | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. |
| [Unlimited-OCR](unlimited-ocr.md) | 31.2k | Modelo de Baidu para parsear documentos largos de una sola pasada con visión. |

## Enlaces

- 🐙 GitHub: [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- 🌐 Web: <https://www.paddleocr.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
