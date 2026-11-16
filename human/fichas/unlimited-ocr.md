[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › OCR

# 🔠 Unlimited-OCR

> Modelo de Baidu para parsear documentos largos de una sola pasada con visión.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.2k | MIT | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Puntuación de calidad** 65/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto de investigación de Baidu (MIT) sobre análisis de documentos ultralargos, con la serie de modelos Unlimited OCR. Unlimited OCR 2 se publicó el 27 de octubre de 2026 junto con un artículo y el benchmark MarathonDocBench; no hay releases en GitHub.

## ¿Qué hace?

Busca analizar documentos de longitud «ilimitada» (lo que llaman OCR-3.0) con una técnica de atención de ventana deslizante (SR-SWA), en lugar de procesar página a página. El modelo está disponible en Hugging Face, ModelScope y Baidu Cloud, y admite entrenamiento con ms-swift.

## ¿Cómo lo hace?

Se ejecuta con Transformers para pruebas rápidas (probado con Python 3.10, torch 2.13 y transformers 4.52.1 en una NVIDIA A800 de 80 GB) o con SGLang, recomendado para servir; también admite inferencia con vLLM. Requiere GPU con mucha memoria [DATO NO VERIFICADO: mínimo de VRAM].

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [SGLang](sglang.md) | Backend recomendado para servir el modelo. | Instala SGLang en un servidor con GPU y carga el modelo desde Hugging Face. |
| [vLLM](vllm.md) | Inferencia soportada gracias a la comunidad de vLLM. | Alternativa a SGLang: usa uno de los dos. |
| [Transformers](transformers.md) | Ejecución nativa para pruebas rápidas. | Fija las versiones probadas en un entorno aislado. |

**Notas:** Alternativas (elige una): olmocr, paddleocr. Se retiraron litellm, cosmos y comfyui por no tener relación documentada.

Estado en GitHub: activo · último push 2026-11-09 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/baidu/Unlimited-OCR/blob/main/README.md)</sub>

## Ver similares

Grupo **OCR de documentos**: Unlimited-OCR ocupa la posición 2 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [PaddleOCR](paddleocr.md) ⭐ recomendado | 72 | Si necesitas OCR multilingüe de producción con modelos ligeros y análisis de maquetación. |
| 2 | **Unlimited-OCR** (esta ficha) | 65 | Si quieres parsear documentos largos de una sola pasada con visión. |
| 3 | [Tesseract](tesseract.md) | 64 | Si quieres el OCR clásico en CPU, sin GPU ni modelos grandes. |
| 4 | [olmOCR](olmocr.md) | 53 | Si conviertes PDF escaneados a texto limpio con un modelo de visión (GPU). |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige API remota; el entorno y pesos usan recursos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La prueba del autor usa una NVIDIA A800 de 80 GB; la promesa unlimited describe el método y no recursos ilimitados en cualquier equipo |
| Coste | Sin pago a un modelo en la ruta básica. No exige API remota; el entorno y pesos usan recursos propios |
| Equipo | Preparación según la ruta elegida. Python 3.10 y versiones fijadas; GPU grande; pesos y runtime del ejemplo |

La prueba del autor usa una NVIDIA A800 de 80 GB; la promesa unlimited describe el método y no recursos ilimitados en cualquier equipo

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10 y versiones fijadas
- GPU grande
- pesos y runtime del ejemplo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
pip install torch==2.13.0 torchvision pillow transformers==4.52.1 huggingface-hub==0.36.0 \
  tokenizers==0.21.4 addict==2.4.0 einops==0.8.2 easydict==1.13
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/baidu/Unlimited-OCR/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Unlimited-OCR para mi objetivo y necesito pasos guiados. Lee https://github.com/baidu/Unlimited-OCR/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prueba un documento corto antes de procesar uno largo y compara texto y tablas.

**Qué comprobar:** Puedes identificar errores y consumo de memoria en tu muestra.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar parsing de documentos largos
- Comparar un VLM OCR con otro motor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar parsing de documentos largos; Comparar un VLM OCR con otro motor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La prueba del autor usa una NVIDIA A800 de 80 GB; la promesa unlimited describe el método y no recursos ilimitados en cualquier equipo

## Stack y modelos

- **Stack:** Python 3.10 y versiones fijadas; GPU grande; pesos y runtime del ejemplo
- **Etiquetas:** `ocr` `docs` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [olmOCR](olmocr.md) | 19.8k | Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. |
| [PaddleOCR](paddleocr.md) | 92.7k | Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. |

## Enlaces

- 🐙 GitHub: [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/baidu/Unlimited-OCR/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
