[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Rostros y retratos animados

# 🧑 LivePortrait

> Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen (humanos, pero también mascotas).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.5k | NOASSERTION | Python | 2026-06-23 |

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

Convierte una foto en un avatar que sigue las expresiones de un "conductor".

## Por qué destaca

Ofrece animación facial rápida y controlable (con retoque de ojos y boca vía "stitching" y retargeting), y ha sido adoptado por plataformas grandes (Kuaishou, Douyin, Jianying); es proyecto de KwaiVGI con pesos públicos.

## Cómo funciona

Usa un modelo de keypoints/warping implícito sobre PyTorch+GPU que deforma la cara de origen siguiendo el movimiento del conductor; un módulo de stitching suaviza la unión con el cuerpo y otro de retargeting controla ojos/boca de forma independiente.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/KlingAIResearch/LivePortrait/blob/main/readme.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LivePortrait para mi objetivo y necesito pasos guiados. Lee https://github.com/KlingAIResearch/LivePortrait/blob/main/readme.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Convertir una foto en avatar/recurso animado
- Presentadores virtuales a partir de un retrato
- Animar ilustraciones de personajes para reels

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| animas retratos a partir de una foto | necesitas swap en vivo (Deep-Live-Cam) o no tienes GPU |

**Limitaciones:** GPU obligatoria; la calidad cae con poses extremas o rostros muy distintos al conductor; revisar licencia antes de uso comercial.

## Stack y modelos

- **Stack:** Python, PyTorch, GPU
- **Etiquetas:** `image` `vision` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MoviePy](moviepy.md) | 15.2k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Enlaces

- 🐙 GitHub: [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait)
- 🌐 Web: <https://liveportrait.github.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/KlingAIResearch/LivePortrait/blob/main/readme.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
