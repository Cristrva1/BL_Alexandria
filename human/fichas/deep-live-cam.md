[🏠 Inicio](../README.md) › [🖼️ Generar imágenes y trabajar con visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Rostros y retratos animados

# 🎭 Deep-Live-Cam

> Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 98.1k | AGPL-3.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Convierte un cambio de rostro, que normalmente requiere pipeline complejo, en un flujo de "un clic".

## Por qué destaca

Es de los proyectos de swap en vivo más conocidos por su facilidad de uso (una sola imagen de origen y arrancar); incluye chequeos contra contenido inapropiado (NSFW/real) para desincentivar usos problemáticos.

## Cómo funciona

Combina detección facial (insightface/face_swapper) y reenactment sobre PyTorch+GPU (con backend ONNX Runtime o CUDA) para reemplazar el rostro fotograma a fotograma en un flujo en directo desde la webcam o un archivo.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/hacksider/Deep-Live-Cam/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Deep-Live-Cam para mi objetivo y necesito pasos guiados. Lee https://github.com/hacksider/Deep-Live-Cam/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Animar personajes
- Contenido creativo con rostro (uso responsable y consentido)
- Prototipos de presentadores virtuales en vivo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas swap en vivo legítimo con consentimiento | no puedes garantizar uso ético/consentimiento o no tienes GPU |

**Limitaciones:** Uso responsable obligatorio: deepfakes de personas sin consentimiento pueden ser ilegales y violar ToS; GPU requerida para tiempo real; revisar licencia antes de uso comercial.

## Stack y modelos

- **Stack:** Python, PyTorch, ONNX Runtime, GPU
- **Etiquetas:** `vision` `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [face_recognition](face-recognition.md) | 56.9k | Librería de Python con API de alto nivel para detección y reconocimiento facial: localizar caras, compararlas e identificarlas por similitud. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [FaceFusion](facefusion.md) | 30.7k | Plataforma para intercambio y mejora de rostros en imágenes y video. |

## Enlaces

- 🐙 GitHub: [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)
- 🌐 Web: <https://deeplivecam.net/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/hacksider/Deep-Live-Cam/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
