[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 👁️ supervision

> Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y medir.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 51.6k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 78/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

supervision, herramientas reutilizables de visión por computador de Roboflow. Licencia MIT. Es madura y muy activa (~52k estrellas, 0.31.7).

## ¿Qué hace?

Carga datasets, dibuja detecciones y máscaras, cuenta objetos que cruzan zonas o líneas, rastrea (ByteTrack) y convierte entre formatos. Es independiente del modelo, con conectores para Ultralytics, Transformers, Inference y otros.

## ¿Cómo lo hace?

Requiere Python 3.10+ y se instala con `pip install supervision`. Usar Roboflow Inference requiere una API key de Roboflow.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ultralytics YOLO](ultralytics.md) | Conector nativo `from_ultralytics`. | Instala ambos y convierte los resultados. |
| [OpenCV](opencv.md) | Lectura y escritura de vídeo. | Instala `opencv-python`. |
| [SAM 3](sam3.md) | Visualizar máscaras de segmentación. (combinación por arquitectura) | Convierte las máscaras. |
| [Label Studio](label-studio.md) | Combinación recíproca: Label Studio lo enlaza como «Revisar y convertir anotaciones. (combinación por arquitectura)». | Orden indicado desde Label Studio: Carga el dataset exportado. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 0.31.7 (2026-11-11) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/roboflow/supervision/blob/develop/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Las utilidades básicas no exigen API; el ejemplo con Roboflow Inference necesita clave y condiciones del servicio |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Supervision procesa resultados de modelos y no los reemplaza; la compatibilidad depende del adaptador y formato de detecciones |
| Coste | El coste depende del proveedor o la ruta. Las utilidades básicas no exigen API; el ejemplo con Roboflow Inference necesita clave y condiciones del servicio |
| Equipo | Preparación según la ruta elegida. Python; imagen y detecciones de prueba; modelo aparte si lo ejecutas |

Supervision procesa resultados de modelos y no los reemplaza; la compatibilidad depende del adaptador y formato de detecciones

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- imagen y detecciones de prueba
- modelo aparte si lo ejecutas

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install supervision
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/roboflow/supervision/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar supervision para mi objetivo y necesito pasos guiados. Lee https://github.com/roboflow/supervision/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Dibuja cajas de detección de muestra y verifica coordenadas y etiquetas.

**Qué comprobar:** Puedes comprobar el resultado anotado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Visualizar detecciones
- Contar cruces en un video de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Visualizar detecciones; Contar cruces en un video de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Supervision procesa resultados de modelos y no los reemplaza; la compatibilidad depende del adaptador y formato de detecciones

## Stack y modelos

- **Stack:** Python; imagen y detecciones de prueba; modelo aparte si lo ejecutas
- **Etiquetas:** `vision` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [roboflow/supervision](https://github.com/roboflow/supervision)
- 🌐 Web: <https://supervision.roboflow.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/roboflow/supervision/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
