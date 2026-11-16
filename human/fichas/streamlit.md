[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Apps de datos en Python

# 📊 streamlit

> Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 46.4k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Streamlit, framework de apps de datos en Python, propiedad de Snowflake. Licencia Apache-2.0. Es muy maduro (~46k estrellas, 1.67.0) y ahora se presenta como «agent-native».

## ¿Qué hace?

Convierte scripts Python en apps web (dashboards, herramientas de pronóstico, flujos de revisión y aprobación) sin frontend ni API separados. Gestiona interfaz, estado, caché, inicio de sesión y temas.

## ¿Cómo lo hace?

Se instala con `pip install streamlit` y se ejecuta con `streamlit run app.py`. Se despliega en Streamlit Community Cloud, Snowflake o servidor propio.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [dash](dash.md) | Gráficos Plotly en paralelo para casos más complejos. (combinación por arquitectura) | Elige según la complejidad. |
| [Polars](polars.md) | DataFrames rápidos dentro de la app. (combinación por arquitectura) | Procesa con Polars y muestra con `st.dataframe`. |
| [DuckDB](duckdb.md) | Consultas SQL locales en la app. (combinación por arquitectura) | Consulta con DuckDB y muestra el resultado. |
| [Awesome LLM Apps](awesome-llm-apps.md) | Combinación recíproca: Awesome LLM Apps lo enlaza como «Interfaz de muchas de las apps de ejemplo». | Orden indicado desde Awesome LLM Apps: Se instala con los requirements de cada plantilla. |

**Notas:** Alternativas (elige una): gradio.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 1.67.0 (2026-11-05) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/streamlit/streamlit/blob/develop/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La app básica no necesita LLM; AI, hosting y fuentes de datos tienen costes separados |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. streamlit skills instala instrucciones para Claude Code y agentes que leen .agents; no convierte la suscripción del agente en backend de cualquier app creada |
| Coste | El coste depende del proveedor o la ruta. La app básica no necesita LLM; AI, hosting y fuentes de datos tienen costes separados |
| Equipo | Preparación según la ruta elegida. Python; script pequeño; datos ficticios |

streamlit skills instala instrucciones para Claude Code y agentes que leen .agents; no convierte la suscripción del agente en backend de cualquier app creada

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- script pequeño
- datos ficticios

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install streamlit
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/streamlit/streamlit/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar streamlit para mi objetivo y necesito pasos guiados. Lee https://github.com/streamlit/streamlit/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una app con un control y una tabla de ejemplo y comprueba que la interacción actualiza la vista.

**Qué comprobar:** Puedes identificar script, estado y resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un dashboard de ventas ficticias
- Explorar un simulador de demanda

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un dashboard de ventas ficticias; Explorar un simulador de demanda | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** streamlit skills instala instrucciones para Claude Code y agentes que leen .agents; no convierte la suscripción del agente en backend de cualquier app creada

## Stack y modelos

- **Stack:** Python; script pequeño; datos ficticios
- **Etiquetas:** `ui` `dataviz` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Gradio](gradio.md) | 44.1k | Librería Python para crear y compartir apps web de modelos de ML en minutos. |

## Enlaces

- 🐙 GitHub: [streamlit/streamlit](https://github.com/streamlit/streamlit)
- 🌐 Web: <https://streamlit.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/streamlit/streamlit/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
