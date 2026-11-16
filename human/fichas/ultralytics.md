[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 👁️ Ultralytics YOLO

> Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 63.4k | AGPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 88/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Ultralytics, paquete con los modelos YOLO para detección, segmentación, clasificación, pose y OBB. Licencia AGPL-3.0, con licencia Enterprise de pago para uso comercial cerrado. Es muy activo (~63k estrellas, v8.4.215).

## ¿Qué hace?

Entrena, valida, predice, rastrea y exporta modelos YOLO con una API Python y la CLI `yolo`. Exporta a ONNX, TensorRT, CoreML, TFLite y otros formatos, y se integra con su plataforma HUB.

## ¿Cómo lo hace?

Se instala con `pip install ultralytics` y usa PyTorch. La documentación completa está en docs.ultralytics.com.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [supervision](supervision.md) | Anotar, contar y rastrear sobre resultados YOLO. | Convierte con `sv.Detections.from_ultralytics`. |
| [Label Studio](label-studio.md) | Etiquetar datos para entrenar. (combinación por arquitectura) | Exporta en formato YOLO. |
| [OpenCV](opencv.md) | Captura y procesado de vídeo. (combinación por arquitectura) | Lee fotogramas con OpenCV. |
| [kornia](kornia.md) | Combinación recíproca: kornia lo enlaza como «Aumentos de datos en GPU para entrenar. (combinación por arquitectura)». | Orden indicado desde kornia: Aplica aumentos antes del entrenamiento. |
| [SAM 3](sam3.md) | Combinación recíproca: SAM 3 lo enlaza como «Combinar detección YOLO con segmentación por concepto. (combinación por arquitectura)». | Orden indicado desde SAM 3: Usa las cajas como prompts. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[CVAT Community](cvat.md) · [DeepFace](deepface.md)

**Notas:** Sin alternativas declaradas. La AGPL obliga a publicar el código de servicios que lo usen, salvo con licencia Enterprise.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v8.4.215 (2026-11-16) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ultralytics/ultralytics/blob/main/README.md) · [2](https://docs.ultralytics.com)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Inferencia local sin API obligatoria; AGPL y licencia Enterprise tienen condiciones distintas y hardware aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La licencia se debe revisar para el uso previsto; un modelo rápido o preciso en benchmarks no garantiza igual resultado en tus imágenes |
| Coste | El coste depende del proveedor o la ruta. Inferencia local sin API obligatoria; AGPL y licencia Enterprise tienen condiciones distintas y hardware aparte |
| Equipo | Preparación según la ruta elegida. Python; PyTorch; modelo y memoria compatibles; imagen de prueba |

La licencia se debe revisar para el uso previsto; un modelo rápido o preciso en benchmarks no garantiza igual resultado en tus imágenes

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- PyTorch
- modelo y memoria compatibles
- imagen de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install ultralytics
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ultralytics/ultralytics/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Ultralytics YOLO para mi objetivo y necesito pasos guiados. Lee https://github.com/ultralytics/ultralytics/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Detecta objetos en una imagen y revisa dos cajas y sus etiquetas.

**Qué comprobar:** Puedes contrastar la detección con el contenido real.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Contar objetos de muestra
- Probar segmentación en un prototipo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Contar objetos de muestra; Probar segmentación en un prototipo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La licencia se debe revisar para el uso previsto; un modelo rápido o preciso en benchmarks no garantiza igual resultado en tus imágenes

## Stack y modelos

- **Stack:** Python; PyTorch; modelo y memoria compatibles; imagen de prueba
- **Etiquetas:** `vision` `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)
- 🌐 Web: <https://platform.ultralytics.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ultralytics/ultralytics/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
