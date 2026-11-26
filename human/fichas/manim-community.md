[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Motores de video y escenas por código

# 🎬 manim

> Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 42.5k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 71/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Manim Community Edition (ManimCE), fork comunitario de 3b1b/manim para animaciones matemáticas explicativas. Doble licencia MIT (3blue1brown LLC y Manim Community Developers). Es madura y activa (~43k estrellas, v0.22.1).

## ¿Qué hace?

Ofrece la API de Manim con documentación amplia, estabilidad, pruebas y una comunidad activa, orientada a usuarios generales.

## ¿Cómo lo hace?

Requiere instalar dependencias previas según el sistema (y LaTeX para fórmulas) y se instala con `pip install manim` o uv. La guía por sistema operativo está en docs.manim.community.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Renderizar vídeo. | Instala FFmpeg. |
| [Kokoro](kokoro.md) | Narración. (combinación por arquitectura) | Genera el audio y móntalo. |
| [srt-whiteboard-animation](srt-whiteboard-animation.md) | Otro estilo explicativo, de pizarra. (combinación por arquitectura) | Elige según el formato. |

**Notas:** Alternativas (elige una): manim.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v0.22.1 (2026-10-27) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ManimCommunity/manim/blob/main/README.md) · [2](https://docs.manim.community/)</sub>

## Ver similares

Grupo **Animaciones matemáticas (Manim)**: manim ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **manim** (esta ficha) ⭐ recomendado | 71 | Si buscas esto: motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas. |
| 2 | [Manim (ManimGL)](manim.md) | 54 | Si buscas esto: motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenGL. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Código MIT sin API de IA; render y recursos independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Manim Community usa from manim y su propio CLI; es una línea distinta de ManimGL y sus tutoriales no son intercambiables sin adaptar |
| Coste | Sin pago a un modelo en la ruta básica. Código MIT sin API de IA; render y recursos independientes |
| Equipo | Preparación según la ruta elegida. Python; dependencias de la versión; LaTeX según escena; equipo |

Manim Community usa from manim y su propio CLI; es una línea distinta de ManimGL y sus tutoriales no son intercambiables sin adaptar

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- dependencias de la versión
- LaTeX según escena
- equipo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
pip install manim
```

Comando copiado literalmente de la documentación del repositorio; revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/ManimCommunity/manim/blob/main/docs/source/installation.rst)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar manim para mi objetivo y necesito pasos guiados. Lee https://github.com/ManimCommunity/manim/blob/main/docs/source/installation.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue SquareToCircle y modifica una propiedad para observar la transformación.

**Qué comprobar:** Puedes renderizar y relacionar el resultado con la escena Python.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una explicación matemática
- Crear una animación de geometría

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una explicación matemática; Crear una animación de geometría | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Manim Community usa from manim y su propio CLI; es una línea distinta de ManimGL y sus tutoriales no son intercambiables sin adaptar

## Stack y modelos

- **Stack:** Python; dependencias de la versión; LaTeX según escena; equipo
- **Etiquetas:** `programatico` `animations` `hacktoberfest` `manim` `math` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Manim (ManimGL)](manim.md) | 96.5k | Motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenGL. |

## Enlaces

- 🐙 GitHub: [ManimCommunity/manim](https://github.com/ManimCommunity/manim)
- 🌐 Web: <https://www.manim.community>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ManimCommunity/manim/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
