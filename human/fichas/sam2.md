[🏠 Inicio](../README.md) › [🖼️ Generar imágenes y trabajar con visión](../categorias/11-generaci-n-de-imagen-visi-n.md) › Visión por computador

# 👁️ SAM 2

> Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 20.1k | Apache-2.0 | Jupyter Notebook | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

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

Marca un objeto en un fotograma y SAM 2 lo sigue en todo el video. Más rápido que SAM en imágenes.

## Por qué destaca

Segmentación de video interactiva de alta calidad.

## Cómo funciona

Arquitectura con memoria en streaming que propaga máscaras entre fotogramas.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/facebookresearch/sam2/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SAM 2 para mi objetivo y necesito pasos guiados. Lee https://github.com/facebookresearch/sam2/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Rotoscopía de video
- Seguimiento de objetos
- Anotar datasets de video

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas segmentar objetos en video | solo trabajas con imágenes sueltas; `segment-anything` basta |

## Stack y modelos

- **Stack:** Python, PyTorch
- **Etiquetas:** `vision` `video` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Label Studio](label-studio.md) | 28.7k | Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. |
| [supervision](supervision.md) | 51.6k | Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y medir. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Segment Anything (SAM)](segment-anything.md) | 55.1k | Modelo de Meta que segmenta cualquier objeto en una imagen a partir de un clic o una caja. |

## Enlaces

- 🐙 GitHub: [facebookresearch/sam2](https://github.com/facebookresearch/sam2)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/facebookresearch/sam2/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
