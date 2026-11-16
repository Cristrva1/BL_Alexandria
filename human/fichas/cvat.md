[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# ⚙️ CVAT Community

> Plataforma autoalojable para anotar imágenes, vídeo, audio y 3D con equipos, preanotación con modelos y exportación a más de 20 formatos de datasets.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.1k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Edición comunitaria, autoalojable y de código abierto (MIT) de CVAT, una de las herramientas de anotación de datos más usadas en visión por computador desde 2018. Es la base de CVAT Online y CVAT Enterprise (comerciales). Muy activa.

## ¿Qué hace?

Permite anotar imágenes, vídeo, audio y nubes de puntos 3D con cajas, polígonos, máscaras, puntos y pistas, gestionar proyectos y tareas, colaborar en equipo, conectar almacenamiento en la nube, preanotar con modelos (SAM, YOLO, Detectron2, HRNet de MMPose…) y exportar o importar más de 20 formatos (COCO, YOLO, Pascal VOC…).

## ¿Cómo lo hace?

Se despliega con Docker Compose o Kubernetes. Backend Django con PostgreSQL y Redis, frontend React; las funciones de IA se ejecutan como serverless en Nuclio. Ofrece SDK (`cvat-sdk`) y CLI (`cvat-cli`) en Python y usa bibliotecas de FFmpeg para vídeo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Detectron2](detectron2.md) | CVAT incluye una función serverless con RetinaNet R101 de Detectron2 para detectar objetos automáticamente. | Despliega CVAT con el componente serverless; después instala la función de Detectron2 con nuctl. |
| [mmpose](mmpose.md) | CVAT incluye una función serverless con HRNet32 de MMPose para estimar pose de cuerpo completo. | Despliega CVAT con el componente serverless; después instala la función de MMPose. |
| [Ultralytics YOLO](ultralytics.md) | CVAT exporta e importa anotaciones en los formatos YOLO de Ultralytics (detección, segmentación, pose) para entrenar con esa biblioteca. | Anota en CVAT y exporta en formato Ultralytics YOLO; después entrena con `yolo train`. |

**Notas:** Alternativa de Label Studio: CVAT está más especializado en visión (vídeo, pistas y 3D); Label Studio cubre más tipos de datos generales.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v2.83.0 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/cvat-ai/cvat/blob/develop/README.md) · [2](https://github.com/cvat-ai/cvat/blob/develop/cvat/apps/dataset_manager/formats/yolo.py)</sub>

## Ver similares

Grupo **Etiquetado de datos para visión**: CVAT Community ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Label Studio](label-studio.md) ⭐ recomendado | 71 | Si buscas esto: herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. |
| 2 | **CVAT Community** (esta ficha) | 68 | Si buscas esto: plataforma autoalojable para anotar imágenes, vídeo, audio y 3D con equipos, preanotación con modelos y exportación a más de 20 formatos de datasets. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
docker compose up -d
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/cvat-ai/cvat/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar CVAT Community para mi objetivo y necesito pasos guiados. Lee https://github.com/cvat-ai/cvat/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona el repositorio y ejecuta `docker compose up -d`; crea un usuario y una tarea con unas pocas imágenes..

**Qué comprobar:** Puedes dibujar cajas o polígonos y exportar las anotaciones en formato COCO o YOLO..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- etiquetar un dataset de detección o segmentación con varias personas
- preanotar vídeos con un modelo y corregir solo los errores

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: etiquetar un dataset de detección o segmentación con varias personas; preanotar vídeos con un modelo y corregir solo los errores | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. CVAT Community es MIT; el código de /serverless puede usar recursos de terceros con licencias no comerciales. CVAT Online y Enterprise son de pago.

## Stack y modelos

- **Stack:** Python, Dockerfile, docker-compose.yml, package.json, pyproject.toml
- **Etiquetas:** `annotation` `vision` `dataset` `self-hosted`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Label Studio](label-studio.md) | 28.7k | Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. |

## Enlaces

- 🐙 GitHub: [cvat-ai/cvat](https://github.com/cvat-ai/cvat)
- 🌐 Web: <https://www.cvat.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cvat-ai/cvat/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
