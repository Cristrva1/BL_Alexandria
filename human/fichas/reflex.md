[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Apps de datos en Python

# 📚 Reflex

> Framework para crear aplicaciones web completas (frontend y backend) solo con Python, con estado en clases, componentes y despliegue propio o gestionado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 71/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de código abierto (Apache-2.0) de Reflex Inc. para aplicaciones web full-stack en Python puro. La empresa ofrece además servicios comerciales: AI Builder, alojamiento gestionado y una edición Enterprise.

## ¿Qué hace?

Permite definir páginas, componentes y estado en Python: los eventos del usuario llaman a métodos del estado en el servidor y la interfaz se actualiza sola. Incluye componentes (formularios, tablas, gráficos), enrutado, base de datos con SQLModel, autenticación por terceros y despliegue. Publica un servidor MCP y un Agent Toolkit para asistentes de código.

## ¿Cómo lo hace?

Se instala con `uv add reflex` (o pip en un entorno virtual); `reflex init` crea el proyecto y `reflex run` levanta el servidor de desarrollo con recarga. Compila el frontend a React/Next.js (requiere Node, que gestiona el propio Reflex) y el backend corre en Python; se puede autoalojar con Docker.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Reflex publica un servidor MCP y un Agent Toolkit (MCP y skills) para que asistentes de código como Claude Code trabajen con su documentación y componentes. | Crea el proyecto Reflex; después añade el servidor MCP de Reflex al asistente. |
| [pandas](pandas.md) | El componente `rx.data_table` acepta un DataFrame de pandas para mostrar datos en una tabla. | Instala pandas en el proyecto; después pasa el DataFrame a `rx.data_table(data=df)`. |
| [coolify](coolify.md) | Reflex documenta el autoalojamiento con Docker, y Coolify despliega contenedores desde un repositorio (combinación por arquitectura). | Prepara el Dockerfile según el ejemplo de Reflex; después despliégalo en Coolify. |

**Notas:** Es alternativa de Streamlit, Gradio, NiceGUI y Panel: Reflex apunta a apps completas con varias páginas y estado; Streamlit y Gradio a prototipos y demos rápidas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.11.0 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/reflex-dev/reflex/blob/main/README.md) · [2](https://github.com/reflex-dev/reflex/blob/main/MCP_README.md) · [3](https://github.com/reflex-dev/reflex/blob/main/docs/library/tables-and-data-grids/data_table.md)</sub>

## Ver similares

Grupo **Apps web de datos en Python**: Reflex ocupa la posición 3 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [streamlit](streamlit.md) ⭐ recomendado | 76 | Si quieres convertir un script de datos en app web con la menor curva. |
| 2 | [Gradio](gradio.md) | 71 | Si quieres una demo de un modelo de IA con entradas y salidas en minutos. |
| 3 | **Reflex** (esta ficha) | 71 | Si quieres una app web completa (frontend y backend) solo en Python. |
| 4 | [NiceGUI](nicegui.md) | 68 | Si quieres una interfaz web en Python con control fino de componentes. |
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
uv add reflex
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/reflex-dev/reflex/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Reflex para mi objetivo y necesito pasos guiados. Lee https://github.com/reflex-dev/reflex/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un proyecto con `uv init`, ejecuta `uv add reflex`, `uv run reflex init` y `uv run reflex run`..

**Qué comprobar:** La app de ejemplo se abre en http://localhost:3000 y se recarga al editar el código..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- construir un panel interno o una herramienta con formularios y tablas sin escribir JavaScript
- prototipar una app de IA con estado, como un generador de imágenes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: construir un panel interno o una herramienta con formularios y tablas sin escribir JavaScript; prototipar una app de IA con estado, como un generador de imágenes | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. El framework es Apache-2.0; AI Builder, el alojamiento gestionado y algunos componentes empresariales (p. ej. AG Grid) son servicios o licencias aparte.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `python` `web` `framework` `ui`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [NiceGUI](nicegui.md) | 16.3k | Framework Python para interfaces web en el navegador con botones, gráficos, mapas, tablas y escenas 3D, útil para paneles, robótica y herramientas internas. |
| [Panel](panel.md) | 5.8k | Framework de HoloViz para dashboards y apps de datos en Python que funcionan igual en un notebook y como aplicación web servida con `panel serve`. |
| [streamlit](streamlit.md) | 46.4k | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. |
| [Gradio](gradio.md) | 44.1k | Librería Python para crear y compartir apps web de modelos de ML en minutos. |

## Enlaces

- 🐙 GitHub: [reflex-dev/reflex](https://github.com/reflex-dev/reflex)
- 🌐 Web: <https://reflex.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/reflex-dev/reflex/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
