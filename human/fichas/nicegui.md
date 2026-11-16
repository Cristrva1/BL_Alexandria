[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Apps de datos en Python

# 📚 NiceGUI

> Framework Python para interfaces web en el navegador con botones, gráficos, mapas, tablas y escenas 3D, útil para paneles, robótica y herramientas internas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.3k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de interfaz de código abierto (MIT) creado por Zauberzeug, una empresa alemana de robótica. Activo, con paquetes en PyPI, Docker y conda-forge.

## ¿Qué hace?

Construye interfaces que se muestran en el navegador desde Python: etiquetas, botones, entradas, subida de archivos, diálogos, Markdown, tablas, gráficos (ECharts, Plotly, Matplotlib), mapas Leaflet y escenas 3D. Recarga al cambiar el código y puede ejecutarse como servidor web o en una ventana nativa.

## ¿Cómo lo hace?

Se instala con pip, uv o Docker. Usa FastAPI y uvicorn en el backend y Vue/Quasar en el frontend, conectados por socket.io; cada elemento es un objeto Python con eventos asíncronos. Funciona con un solo proceso de uvicorn.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Leaflet](leaflet.md) | El elemento `ui.leaflet` de NiceGUI muestra mapas interactivos con Leaflet. | Instala NiceGUI; después añade `ui.leaflet(center=...)` a la página. |
| [echarts](echarts.md) | El elemento `ui.echart` renderiza gráficos de Apache ECharts a partir de un diccionario de opciones. | Instala NiceGUI; después crea `ui.echart({...})` con la configuración del gráfico. |
| [three.js](three-js.md) | El elemento `ui.scene` dibuja escenas 3D en el navegador con three.js. | Instala NiceGUI; después usa `with ui.scene():` para añadir objetos 3D. |
| [pandas](pandas.md) | `ui.table.from_pandas` crea una tabla a partir de un DataFrame de pandas (también existe `from_polars`). | Instala pandas; después llama a `ui.table.from_pandas(df)`. |

**Notas:** Alternativa de Streamlit, Gradio, Panel y Reflex; destaca para control de hardware y robótica por su modelo de eventos.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v4.0.0 (2026-11-04) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zauberzeug/nicegui/blob/main/README.md) · [2](https://nicegui.io/documentation) · [3](https://github.com/zauberzeug/nicegui/blob/main/nicegui/elements/table.py)</sub>

## Ver similares

Grupo **Apps web de datos en Python**: NiceGUI ocupa la posición 4 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [streamlit](streamlit.md) ⭐ recomendado | 76 | Si quieres convertir un script de datos en app web con la menor curva. |
| 2 | [Gradio](gradio.md) | 71 | Si quieres una demo de un modelo de IA con entradas y salidas en minutos. |
| 3 | [Reflex](reflex.md) | 71 | Si quieres una app web completa (frontend y backend) solo en Python. |
| 4 | **NiceGUI** (esta ficha) | 68 | Si quieres una interfaz web en Python con control fino de componentes. |
| 5 | [Panel](panel.md) | 55 | Si trabajas con el ecosistema HoloViz y notebooks y quieres dashboards complejos. |

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

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
python3 -m pip install nicegui
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/zauberzeug/nicegui/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar NiceGUI para mi objetivo y necesito pasos guiados. Lee https://github.com/zauberzeug/nicegui/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `python3 -m pip install nicegui`, escribe un script con `ui.label` y `ui.button` y ejecútalo con `ui.run()`..

**Qué comprobar:** La interfaz se abre en el navegador (puerto 8080) y se recarga al guardar..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- crear un panel de control para un robot o una casa domótica
- hacer una pequeña herramienta web para ajustar parámetros de un algoritmo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: crear un panel de control para un robot o una casa domótica; hacer una pequeña herramienta web para ajustar parámetros de un algoritmo | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, docker-compose.yml, package.json, pyproject.toml
- **Etiquetas:** `python` `web` `ui` `framework`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Reflex](reflex.md) | 29k | Framework para crear aplicaciones web completas (frontend y backend) solo con Python, con estado en clases, componentes y despliegue propio o gestionado. |
| [Panel](panel.md) | 5.8k | Framework de HoloViz para dashboards y apps de datos en Python que funcionan igual en un notebook y como aplicación web servida con `panel serve`. |
| [streamlit](streamlit.md) | 46.4k | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. |
| [Gradio](gradio.md) | 44.1k | Librería Python para crear y compartir apps web de modelos de ML en minutos. |

## Enlaces

- 🐙 GitHub: [zauberzeug/nicegui](https://github.com/zauberzeug/nicegui)
- 🌐 Web: <https://nicegui.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zauberzeug/nicegui/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
