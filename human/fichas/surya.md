[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › OCR

# 🧩 Surya

> OCR multilingüe y análisis de layout con un VLM de 689M parámetros: orden de lectura, tablas en HTML y más de 90 idiomas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 21.6k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; necesita GPU

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Modelo y biblioteca de OCR de Datalab (autores de marker). El código es Apache-2.0 y los pesos usan una licencia Open Rail-M modificada con límites comerciales. Activo; la versión actual es un VLM único.

## ¿Qué hace?

Hace OCR, análisis de layout (tablas, imágenes, encabezados, ecuaciones, formularios), orden de lectura y reconocimiento de tablas como HTML con colspan y rowspan, en más de 90 idiomas. El README cita puntuaciones altas en OmniParseBench y olmOCR-bench entre modelos abiertos de menos de 1B.

## ¿Cómo lo hace?

`pip install surya-ocr` instala un cliente sin dependencias pesadas que arranca automáticamente el servidor de inferencia: vLLM en Docker o Podman para GPU NVIDIA, llama.cpp para CPU o Apple Silicon y, de forma experimental, mlx_vlm.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vLLM](vllm.md) | Surya usa vLLM en contenedor como servidor de inferencia por defecto en GPU NVIDIA. | Docker o Podman con NVIDIA Container Toolkit; Surya lanza vLLM en el primer uso. |
| [llama.cpp](llama-cpp.md) | En CPU o Apple Silicon Surya usa llama-server de llama.cpp como backend. | Instala llama.cpp (p. ej. con Homebrew); después ejecuta Surya. |
| [Marker](marker.md) | marker, del mismo equipo, usa los modelos de Surya para convertir PDF a Markdown. | Instala marker; usará Surya para OCR y layout. |

**Notas:** Para usos comerciales por encima de los umbrales de la licencia de pesos, contacta con Datalab.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v0.24.0 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/datalab-to/surya/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.

1. Elige el modelo y el backend que documenta el proyecto para tu sistema.
2. Prepara las dependencias y los pesos; no uses una cifra promocional como garantía para tu hardware.
3. Procesa una muestra pequeña y revisa calidad, tiempo y memoria antes de aumentar el tamaño de la tarea.

**Entrada documentada (consulta la sintaxis original):**

```
pip install surya-ocr
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/datalab-to/surya/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Surya para mi objetivo y necesito pasos guiados. Lee https://github.com/datalab-to/surya/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install surya-ocr` y procesa una página de prueba con OCR y layout..

**Qué comprobar:** Obtienes el texto en orden de lectura y las regiones de layout detectadas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- digitalizar documentos escaneados en varios idiomas conservando el orden de lectura
- extraer tablas de PDF como HTML con celdas combinadas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: digitalizar documentos escaneados en varios idiomas conservando el orden de lectura; extraer tablas de PDF como HTML con celdas combinadas | no tienes el hardware o no aceptas la licencia de los pesos |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Código Apache-2.0; los pesos usan una licencia AI Pubs Open Rail-M modificada (gratis para investigación, uso personal y startups con menos de 5 M$), con licencia comercial aparte.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `ocr` `python` `pdf` `model`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [datalab-to/surya](https://github.com/datalab-to/surya)
- 🌐 Web: <https://www.datalab.to>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/datalab-to/surya/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
