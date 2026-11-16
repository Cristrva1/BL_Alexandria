[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Rostros y retratos animados

# 🙂 InsightFace

> Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.2k | — | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 54/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

InsightFace, proyecto de análisis facial 2D y 3D mantenido por Jia Guo y Jiankang Deng. El código es MIT, pero los datos de entrenamiento y los modelos entrenados con ellos son solo para investigación no comercial; GitHub no detecta licencia. Tiene ~30k estrellas y es una referencia histórica del área.

## ¿Qué hace?

Ofrece detección (SCRFD/RetinaFace), reconocimiento (ArcFace), alineación, atributos y reconstrucción 3D, con un model zoo. Sus modelos (por ejemplo, inswapper) son la base de muchas herramientas de face swap.

## ¿Cómo lo hace?

Se usa mediante el paquete Python `insightface` (que descarga los modelos automáticamente) con ONNX Runtime. El código de entrenamiento funciona con PyTorch 1.6+ y/o MXNet.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FaceFusion](facefusion.md) | Usa modelos de análisis facial del ecosistema. (combinación por arquitectura) | Instala FaceFusion con sus modelos. |
| [Deep-Live-Cam](deep-live-cam.md) | Usa su modelo inswapper. | Viene como dependencia. |
| [LivePortrait](liveportrait.md) | Detección y recorte facial. (combinación por arquitectura) | Viene como dependencia en la ruta por defecto. |
| [DeepFace](deepface.md) | Combinación recíproca: DeepFace lo enlaza como «El modelo de reconocimiento Buffalo_L que envuelve DeepFace procede de InsightFace». | Orden indicado desde DeepFace: Instala DeepFace; después usa `model_name="Buffalo_L"` (revisa la licencia de los pesos de InsightFace). |

**Notas:** Sin alternativas declaradas. Los pesos no permiten uso comercial.

Estado en GitHub: activo · último push 2026-10-19 · última versión publicada model-zoo (2026-09-03) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/deepinsight/insightface/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Código MIT, pero modelos preentrenados proporcionados para investigación no comercial; uso comercial requiere revisar la licencia correspondiente |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La licencia de código y modelos es distinta incluso en descargas automáticas; el paquete actual ofrece base y GUI con dependencias diferentes |
| Coste | El coste depende del proveedor o la ruta. Código MIT, pero modelos preentrenados proporcionados para investigación no comercial; uso comercial requiere revisar la licencia correspondiente |
| Equipo | Preparación según la ruta elegida. Python; runtime ONNX; modelos con licencia adecuada; datos autorizados |

La licencia de código y modelos es distinta incluso en descargas automáticas; el paquete actual ofrece base y GUI con dependencias diferentes

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- runtime ONNX
- modelos con licencia adecuada
- datos autorizados

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/deepinsight/insightface/blob/master/python-package/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar InsightFace para mi objetivo y necesito pasos guiados. Lee https://github.com/deepinsight/insightface/blob/master/python-package/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta detección sobre una imagen propia y revisa resultados antes de usar comparaciones.

**Qué comprobar:** Puedes identificar modelo, backend y caras detectadas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar alineación facial
- Evaluar detección en un dataset de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar alineación facial; Evaluar detección en un dataset de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La licencia de código y modelos es distinta incluso en descargas automáticas; el paquete actual ofrece base y GUI con dependencias diferentes

## Stack y modelos

- **Stack:** Python; runtime ONNX; modelos con licencia adecuada; datos autorizados
- **Etiquetas:** `vision` `image` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [deepinsight/insightface](https://github.com/deepinsight/insightface)
- 🌐 Web: <https://insightface.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/deepinsight/insightface/blob/master/README.md)
- [Fuente 2](https://github.com/deepinsight/insightface/blob/master/python-package/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
