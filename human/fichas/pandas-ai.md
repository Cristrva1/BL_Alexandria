[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 📊 PandasAI

> Librería para conversar con tus datos (SQL, CSV, Parquet) usando LLM.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.9k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

PandasAI, librería de Python para conversar con tus datos en lenguaje natural, de Sinaptik AI. Es MIT salvo `pandasai/ee` (GitHub muestra NOASSERTION). Tiene ~24k estrellas (v3.0.0), pero su último cambio es de octubre de 2025.

## ¿Qué hace?

Permite hacer preguntas sobre DataFrames, CSV, Parquet y bases SQL y obtener respuestas, tablas o gráficos. Genera y ejecuta código para responder, y admite varios DataFrames a la vez. Puede ejecutar el código en un sandbox Docker.

## ¿Cómo lo hace?

Se instala con `pip install pandasai pandasai-litellm` y requiere Python 3.8–3.11. Usa LiteLLM para conectar con distintos proveedores. Como ejecuta código generado por LLM, conviene usar el sandbox (`pandasai-docker`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | Conexión con modelos mediante el paquete `pandasai-litellm`. | Instala ambos paquetes y configura el modelo. |
| [DuckDB](duckdb.md) | Consultar archivos analíticos grandes. (combinación por arquitectura) | Carga los datos con DuckDB y pásalos a PandasAI. |
| [streamlit](streamlit.md) | Interfaz web sencilla para preguntar a los datos. (combinación por arquitectura) | Envuelve las llamadas a PandasAI en una app Streamlit. |

**Notas:** Alternativas (elige una): wrenai. Sin cambios en más de un año; requiere Python ≤3.11.

Estado en GitHub: activo · último push 2025-10-28 · última versión publicada v3.0.0 (2025-10-07) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/sinaptik-ai/pandas-ai/blob/main/README.md) · [2](https://docs.pandas-ai.com/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El ejemplo usa OpenAI mediante LiteLLM y consume API; proveedor y sandbox tienen condiciones propias; no se confirma aquí una ruta local completa |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Puede generar y ejecutar código de análisis; prueba datos ficticios y revisa resultados antes de usar información real |
| Coste | El coste depende del proveedor o la ruta. El ejemplo usa OpenAI mediante LiteLLM y consume API; proveedor y sandbox tienen condiciones propias; no se confirma aquí una ruta local completa |
| Equipo | Preparación según la ruta elegida. Python >=3.8 y <=3.11 según README; datos ficticios; LLM configurado |

Puede generar y ejecutar código de análisis; prueba datos ficticios y revisa resultados antes de usar información real

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python >=3.8 y <=3.11 según README
- datos ficticios
- LLM configurado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install pandasai
pip install pandasai-litellm
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/sinaptik-ai/pandas-ai/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PandasAI para mi objetivo y necesito pasos guiados. Lee https://github.com/sinaptik-ai/pandas-ai/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pregunta el promedio por región de un CSV pequeño y calcula el resultado también de forma directa.

**Qué comprobar:** La respuesta y el código generado coinciden con los datos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar una tabla con lenguaje natural
- Generar un gráfico desde una pregunta

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar una tabla con lenguaje natural; Generar un gráfico desde una pregunta | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Puede generar y ejecutar código de análisis; prueba datos ficticios y revisa resultados antes de usar información real

## Stack y modelos

- **Stack:** Python >=3.8 y <=3.11 según README; datos ficticios; LLM configurado
- **Etiquetas:** `analytics` `data` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [WrenAI](wrenai.md) | 18.2k | BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada. |

## Enlaces

- 🐙 GitHub: [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai)
- 🌐 Web: <https://pandas-ai.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/sinaptik-ai/pandas-ai/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
