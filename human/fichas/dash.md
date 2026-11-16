[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Apps de datos en Python

# 🧮 dash

> Framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24.5k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Dash, framework de Plotly para construir apps analíticas web en Python (también R y Julia), sobre Plotly.js, React y Flask. Licencia MIT. Es maduro (~24k estrellas, v4.5.0) y tiene versión comercial (Dash Enterprise).

## ¿Qué hace?

Une componentes de interfaz (desplegables, sliders, gráficos) con código Python analítico mediante callbacks, sin escribir JavaScript. Tiene una galería de apps de ejemplo.

## ¿Cómo lo hace?

Se instala con `pip install dash` y se ejecuta como app Flask. Dash Enterprise añade despliegue y autenticación corporativa.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [streamlit](streamlit.md) | Prototipar rápido y migrar a Dash cuando crece. (combinación por arquitectura) | Elige según la complejidad. |
| [echarts](echarts.md) | Gráficos alternativos mediante componentes comunitarios. (combinación por arquitectura) | Integra el componente correspondiente. |
| [DuckDB](duckdb.md) | Fuente de datos SQL en proceso. (combinación por arquitectura) | Consulta en los callbacks. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v4.5.0 (2026-10-29) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/plotly/dash/blob/dev/README.md) · [2](https://dash.plotly.com/getting-started)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Dash OSS no exige API de IA; Dash Enterprise, hosting y fuentes de datos son independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un framework Python; el README mezcla ejemplos OSS y funciones Enterprise que no vienen todas con el paquete básico |
| Coste | El coste depende del proveedor o la ruta. Dash OSS no exige API de IA; Dash Enterprise, hosting y fuentes de datos son independientes |
| Equipo | Preparación según la ruta elegida. Python; entorno de desarrollo; datos de muestra |

Es un framework Python; el README mezcla ejemplos OSS y funciones Enterprise que no vienen todas con el paquete básico

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- entorno de desarrollo
- datos de muestra

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://dash.plotly.com/getting-started)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dash para mi objetivo y necesito pasos guiados. Lee https://dash.plotly.com/getting-started. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la app inicial y conecta un selector a un gráfico pequeño.

**Qué comprobar:** Puedes comprobar qué callback cambia la figura.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un tablero interactivo
- Comparar escenarios con controles

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un tablero interactivo; Comparar escenarios con controles | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un framework Python; el README mezcla ejemplos OSS y funciones Enterprise que no vienen todas con el paquete básico

## Stack y modelos

- **Stack:** Python; entorno de desarrollo; datos de muestra
- **Etiquetas:** `automation` `ui` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [plotly/dash](https://github.com/plotly/dash)
- 🌐 Web: <https://plotly.com/dash>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/plotly/dash/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
