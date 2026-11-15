[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Motores de video y escenas por código

# 🎞️ Manim (ManimGL)

> Motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenGL.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 96.5k | MIT | Python | 2026-11-10 |

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

Manim permite describir en código Python escenas con fórmulas LaTeX, gráficas, geometría y transformaciones animadas, y exportarlas a video. Este repo es ManimGL, la versión original que Grant Sanderson usa en 3Blue1Brown; la edición comunitaria (ManimCommunity/manim) es un fork más estable y mejor documentado.

## Por qué destaca

Da una precisión difícil de lograr con un editor: cada objeto y transición se define por código y se puede versionar. Es la herramienta detrás de los videos de 3Blue1Brown y de muchos canales educativos.

## Cómo funciona

Cada escena es una clase Python con objetos matemáticos (Mobjects) y animaciones encadenadas; ManimGL las dibuja con OpenGL en una ventana interactiva y escribe el video con FFmpeg.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install manimgl
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/3b1b/manim/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Manim (ManimGL) para mi objetivo y necesito pasos guiados. Lee https://github.com/3b1b/manim/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Animar demostraciones y fórmulas para clases o YouTube
- Visualizar algoritmos o conceptos de machine learning
- Generar videos explicativos a partir de código escrito por un LLM

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres animaciones matemáticas o técnicas precisas definidas en código Python | buscas estabilidad y documentación para empezar (usa la edición comunitaria ManimCommunity/manim) o motion graphics de marketing; mira `remotion` o `hyperframes` |

**Limitaciones:** La API cambia entre versiones y no es compatible con la edición comunitaria, así que el código y los tutoriales de una no sirven para la otra.

## Stack y modelos

- **Stack:** Python, OpenGL, FFmpeg, LaTeX
- **Etiquetas:** `video` `dataviz` `learning` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Kokoro](kokoro.md) | 10.1k | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |
| [MoviePy](moviepy.md) | 15.2k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |
| [FFmpeg](ffmpeg.md) | 67.3k | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [manim](manim-community.md) | 42.5k | Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas. |

## Enlaces

- 🐙 GitHub: [3b1b/manim](https://github.com/3b1b/manim)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/3b1b/manim/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
