[🏠 Inicio](../README.md) › [🖼️ Generar imágenes y trabajar con visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Rostros y retratos animados

# 👤 face_recognition

> Librería de Python con API de alto nivel para detección y reconocimiento facial: localizar caras, compararlas e identificarlas por similitud.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 56.9k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Envuelve dlib para que el reconocimiento facial sea trivial desde un script.

## Por qué destaca

Es de las librerías de reconocimiento facial más populares y accesibles, ideal para prototipos por su API mínima (`face_locations`, `face_encodings`, `compare_faces`); muy usada como referencia didáctica.

## Cómo funciona

Envuelve los modelos de dlib (detector HOG/CNN y embeddings faciales de 128 dimensiones) para comparar rostros por distancia entre vectores; el umbral de distancia decide si dos caras son la misma persona.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/ageitgey/face_recognition/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar face_recognition para mi objetivo y necesito pasos guiados. Lee https://github.com/ageitgey/face_recognition/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Detectar/identificar rostros en imágenes
- Etiquetado automático de álbumes
- Comparar identidad entre dos fotos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas reconocimiento facial básico y rápido de implementar | buscas restauración/animación (GFPGAN/LivePortrait) o precisión de producción (mejor DeepFace/InsightFace) |

**Limitaciones:** La instalación de dlib es frágil en Windows; el modelo por defecto (HOG) es menos preciso que alternativas modernas; el repo recibe mantenimiento esporádico.

## Stack y modelos

- **Stack:** Python, dlib
- **Etiquetas:** `image` `vision` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Deep-Live-Cam](deep-live-cam.md) | 98.1k | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [InsightFace](insightface.md) | 30.2k | Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación. |

## Enlaces

- 🐙 GitHub: [ageitgey/face_recognition](https://github.com/ageitgey/face_recognition)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/ageitgey/face_recognition/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
