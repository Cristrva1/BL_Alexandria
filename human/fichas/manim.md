[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Motores de video y escenas por código

# 🎞️ Manim (ManimGL)

> Motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenGL.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 96.5k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

ManimGL, motor de animación programática para vídeos matemáticos explicativos, creado por el autor de 3Blue1Brown (@3b1b). Licencia MIT. Tiene ~97k estrellas (v1.7.2); es la versión personal del autor, distinta de la edición comunitaria.

## ¿Qué hace?

Anima con precisión fórmulas, gráficos y geometría desde Python, con previsualización interactiva en OpenGL.

## ¿Cómo lo hace?

Requiere Python 3.10+ y se instala con `pip install manimgl` (ojo con el nombre del paquete), además de FFmpeg y LaTeX.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Renderizar el vídeo. | Instala FFmpeg. |
| [Kokoro](kokoro.md) | Narración de la explicación. (combinación por arquitectura) | Genera el audio y móntalo. |
| [MoviePy](moviepy.md) | Montaje posterior. (combinación por arquitectura) | Une escenas y audio. |

**Notas:** Alternativas (elige una): manim-community. Para documentación y estabilidad, la comunidad recomienda ManimCE.

Estado en GitHub: activo · último push 2026-09-09 · última versión publicada v1.7.2 (2024-12-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/3b1b/manim/blob/master/README.md)</sub>

## Ver similares

Grupo **Animaciones matemáticas (Manim)**: Manim (ManimGL) ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [manim](manim-community.md) ⭐ recomendado | 71 | Si buscas esto: motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas. |
| 2 | **Manim (ManimGL)** (esta ficha) | 57 | Si buscas esto: motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenGL. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Código MIT sin API de IA; cómputo y recursos externos aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Este es ManimGL de 3Blue1Brown y usa manimgl; no mezcles sus imports o comandos con Manim Community |
| Coste | Sin pago a un modelo en la ruta básica. Código MIT sin API de IA; cómputo y recursos externos aparte |
| Equipo | Preparación según la ruta elegida. Python; FFmpeg; OpenGL; LaTeX si escribes fórmulas; escena pequeña |

Este es ManimGL de 3Blue1Brown y usa manimgl; no mezcles sus imports o comandos con Manim Community

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- FFmpeg
- OpenGL
- LaTeX si escribes fórmulas
- escena pequeña

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (sh):**

```
# Install manimgl
pip install manimgl

# Try it out
manimgl
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/3b1b/manim/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Manim (ManimGL) para mi objetivo y necesito pasos guiados. Lee https://github.com/3b1b/manim/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta una escena de ejemplo y cambia una forma o texto.

**Qué comprobar:** Puedes abrir la animación y localizar su código.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explicar una transformación matemática
- Preparar una animación geométrica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explicar una transformación matemática; Preparar una animación geométrica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Este es ManimGL de 3Blue1Brown y usa manimgl; no mezcles sus imports o comandos con Manim Community

## Stack y modelos

- **Stack:** Python; FFmpeg; OpenGL; LaTeX si escribes fórmulas; escena pequeña
- **Etiquetas:** `video` `dataviz` `learning` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [manim](manim-community.md) | 42.5k | Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas. |

## Enlaces

- 🐙 GitHub: [3b1b/manim](https://github.com/3b1b/manim)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/3b1b/manim/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
