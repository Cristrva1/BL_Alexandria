[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 📚 pysubs2

> Convierte formatos de subtítulos y ajusta sus tiempos en lote desde Python o la terminal, sin cambiar el video ni usar una API de IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 455 | MIT | Python | 2026-11-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 50/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

pysubs2 es una biblioteca Python y una utilidad de terminal para transformar archivos de subtítulos.

## ¿Qué hace?

Convierte formatos y permite ajustar tiempos o editar texto de subtítulos ya existentes.

## ¿Cómo lo hace?

Carga los bloques como eventos con texto y tiempos, aplica el ajuste y guarda una nueva salida en el formato elegido.

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[libass](libass.md)

Estado en GitHub: activo · último push 2026-11-10 · licencia declarada MIT (consultado el 2026-11-24).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-24); no se instaló ni ejecutó. Fuentes: [1](https://github.com/tkarabela/pysubs2/blob/6371ae8bc2f9fed19aeb51a8e09d920e8bb86ce5/README.md) · [2](https://pysubs2.readthedocs.io/en/latest/) · [3](https://pypi.org/project/pysubs2/1.9.1/) · [4](https://github.com/tkarabela/pysubs2/actions/runs/40979280401)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Carga y transformación de archivos de subtítulos en Python. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La ruta básica procesa los datos en tu equipo sin un modelo. |
| Coste | Sin pago a un modelo en la ruta básica. Código MIT. La tarea de ejemplo se ejecuta con herramientas gratuitas en tu equipo. |
| Equipo | Equipo normal; revisar dependencias. Python 3.12 o posterior. La distribución comprobada declara cero dependencias de ejecución. |

La ruta básica funciona sin iniciar sesión en un agente de IA.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.12 o posterior y entorno virtual.
- Un archivo de subtítulos de ejemplo.

1. Prepara Python 3.12 o posterior en un entorno virtual y una copia de un archivo ASS pequeño.
2. Consulta la instalación para la versión 1.9.1 en PyPI. Para convertir una sola copia, sigue el ejemplo de terminal del README con el nombre de ese archivo.
3. Abre el SRT generado y comprueba cantidad de bloques y tiempos antes de procesar un lote.

**Entrada documentada (consulta la sintaxis original):**

```
pip install pysubs2
```

El README muestra el comando general. Selecciona la versión revisada 1.9.1 en el registro oficial y sigue los pasos.

[Instrucciones originales de instalación](https://github.com/tkarabela/pysubs2/blob/6371ae8bc2f9fed19aeb51a8e09d920e8bb86ce5/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/tkarabela/pysubs2/blob/6371ae8bc2f9fed19aeb51a8e09d920e8bb86ce5/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar pysubs2 para mi objetivo y necesito pasos guiados. Lee https://github.com/tkarabela/pysubs2/blob/6371ae8bc2f9fed19aeb51a8e09d920e8bb86ce5/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte una copia de un ASS de dos líneas a SRT siguiendo el ejemplo del README fijado..

**Qué comprobar:** Abre el SRT y comprueba que conserva las dos líneas y sus tiempos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Convertir un archivo ASS de edición a SRT para compartirlo con un reproductor.
- Corregir un desfase constante de los subtítulos en varios clips propios.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Convertir un archivo ASS de edición a SRT para compartirlo con un reproductor.; Corregir un desfase constante de los subtítulos en varios clips propios. | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. La conversión a SRT puede perder estilos propios de ASS. Empieza con una copia y elige UTF-8 para preservar acentos.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `subtítulos` `srt` `webvtt` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [tkarabela/pysubs2](https://github.com/tkarabela/pysubs2)
- 🌐 Web: <http://pysubs2.readthedocs.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-24. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/tkarabela/pysubs2/blob/6371ae8bc2f9fed19aeb51a8e09d920e8bb86ce5/README.md)
- [Fuente 2](https://pysubs2.readthedocs.io/en/latest/)
- [Fuente 3](https://pypi.org/project/pysubs2/1.9.1/)
- [Fuente 4](https://github.com/tkarabela/pysubs2/actions/runs/40979280401)
- [Fuente 5](https://github.com/tkarabela/pysubs2/security/advisories)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
