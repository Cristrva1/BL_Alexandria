[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 olmOCR

> Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.8k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; necesita GPU

**Puntuación de calidad** 51/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Kit del Allen Institute for AI (Apache 2.0) para convertir PDF y documentos de imagen en texto limpio. Versión v0.4.27; el último push es de marzo de 2026 y el último modelo anunciado en el README, de octubre de 2025.

## ¿Qué hace?

Convierte PDF, PNG y JPEG a Markdown con orden de lectura natural incluso con figuras y varias columnas, y soporta ecuaciones, tablas, escritura a mano y formatos complejos; elimina encabezados y pies. Según el README cuesta menos de 200 USD por millón de páginas. Incluye el benchmark olmOCR-Bench y código para entrenar modelos propios.

## ¿Cómo lo hace?

Se basa en un VLM de 7B parámetros servido con vLLM, por lo que necesita una GPU NVIDIA reciente con al menos 12 GB (probado en RTX 4090, L40S, A100, H100), o un servidor vLLM remoto con `--server` instalando solo el paquete base. Requiere poppler-utils y fuentes adicionales; hay imágenes Docker oficiales con CUDA 12.8.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | Motor de inferencia de su canalización, local o remoto. | Servidor vLLM con el modelo olmOCR primero si usas `--server`. |
| [LightRAG](lightrag.md) | Alimentar un RAG con Markdown limpio de documentos escaneados (combinación por arquitectura). | Convierte primero y luego indexa. |
| [open-notebook](open-notebook.md) | Cargar documentos convertidos como fuentes de investigación (combinación por arquitectura). | Convierte primero y súbelos como Markdown. |

**Notas:** Alternativas (elige una): paddleocr, docling, unlimited-ocr.

Estado en GitHub: activo · último push 2026-03-25 · última versión publicada v0.4.27 (2026-03-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/allenai/olmocr/blob/main/README.md)</sub>

## Ver similares

Grupo **OCR de documentos**: olmOCR ocupa la posición 4 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [PaddleOCR](paddleocr.md) ⭐ recomendado | 73 | Si necesitas OCR multilingüe de producción con modelos ligeros y análisis de maquetación. |
| 2 | [Tesseract](tesseract.md) | 64 | Si quieres el OCR clásico en CPU, sin GPU ni modelos grandes. |
| 3 | [Unlimited-OCR](unlimited-ocr.md) | 62 | Si quieres parsear documentos largos de una sola pasada con visión. |
| 4 | **olmOCR** (esta ficha) | 51 | Si conviertes PDF escaneados a texto limpio con un modelo de visión (GPU). |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta local necesita GPU; endpoints alojados cobran según proveedor; guardar resultados también consume espacio |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Instalar el paquete cliente no proporciona por sí solo GPU ni créditos remotos; comienza con pocas páginas |
| Coste | El coste depende del proveedor o la ruta. La ruta local necesita GPU; endpoints alojados cobran según proveedor; guardar resultados también consume espacio |
| Equipo | Preparación según la ruta elegida. Python y dependencias del sistema; GPU para inferencia local o proveedor remoto; PDF |

Instalar el paquete cliente no proporciona por sí solo GPU ni créditos remotos; comienza con pocas páginas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y dependencias del sistema
- GPU para inferencia local o proveedor remoto
- PDF

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install olmocr
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/allenai/olmocr/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar olmOCR para mi objetivo y necesito pasos guiados. Lee https://github.com/allenai/olmocr/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte unas páginas con texto conocido y revisa orden de lectura y símbolos.

**Qué comprobar:** Puedes comparar la salida con la página original y detectar omisiones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar PDFs para entrenamiento documental
- Procesar escaneos con un VLM

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar PDFs para entrenamiento documental; Procesar escaneos con un VLM | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Instalar el paquete cliente no proporciona por sí solo GPU ni créditos remotos; comienza con pocas páginas

## Stack y modelos

- **Stack:** Python y dependencias del sistema; GPU para inferencia local o proveedor remoto; PDF
- **Etiquetas:** `ocr` `pdf` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PaddleOCR](paddleocr.md) | 92.7k | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. |
| [Docling](docling.md) | 70.6k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |
| [Unlimited-OCR](unlimited-ocr.md) | 31.2k | Modelo de Baidu para parsear documentos largos de una sola pasada con visión. |

## Enlaces

- 🐙 GitHub: [allenai/olmocr](https://github.com/allenai/olmocr)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/allenai/olmocr/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
