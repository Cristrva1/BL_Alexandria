[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Modelos y backtesting cuantitativo

# 📚 Backtesting.py

> Framework ligero de Python para hacer backtesting de estrategias de trading sobre datos OHLC, con optimización y gráficos interactivos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.2k | AGPL-3.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 52/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de backtesting de código abierto (AGPL-3.0) creada por kernc. Madura, con ritmo de cambios bajo (último push en agosto de 2026).

## ¿Qué hace?

Permite definir estrategias con indicadores y reglas, ejecutarlas sobre datos históricos de cualquier instrumento, optimizar parámetros (incluida búsqueda por cuadrícula y optimización bayesiana) y analizar estadísticas y operaciones con gráficos interactivos.

## ¿Cómo lo hace?

Se instala con `pip install backtesting`; funciona con DataFrames OHLC de pandas y genera gráficos con Bokeh, visibles en Jupyter o como HTML.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [yfinance](yfinance.md) | yfinance proporciona DataFrames OHLC listos para Backtesting.py (combinación por arquitectura). | Descarga los datos con yfinance; después pásalos al Backtest. |
| [JupyterLab](jupyterlab.md) | Los gráficos interactivos de Backtesting.py se muestran en cuadernos Jupyter. | Instala backtesting en el entorno de JupyterLab; después ejecuta y grafica el backtest. |
| [Claude Code](claude-code.md) | Un agente de código puede escribir clases Strategy y pruebas de parámetros para Backtesting.py (combinación por arquitectura). | Proyecto con datos de prueba; después pide al agente la estrategia y revisa los resultados. |
| [OpenBB Open Data Platform](openbb.md) | Combinación recíproca: OpenBB Open Data Platform lo enlaza como «Los precios OHLC de OpenBB sirven como entrada para estrategias en Backtesting.py (combinación por arquitectura)». | Orden indicado desde OpenBB Open Data Platform: Convierte la salida a DataFrame OHLC; después ejecuta el backtest. |

**Notas:** Alternativas (elige una): vectorbt. Los resultados de backtest no anticipan resultados reales.

Estado en GitHub: activo · último push 2026-08-05 · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/kernc/backtesting.py/blob/master/README.md) · [2](https://kernc.github.io/backtesting.py/)</sub>

## Ver similares

Grupo **Backtesting en Python**: Backtesting.py ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [vectorbt](vectorbt.md) ⭐ recomendado | 56 | Si buscas esto: biblioteca de análisis cuantitativo para explorar señales y comparar estrategias sobre datos de mercado. |
| 2 | **Backtesting.py** (esta ficha) | 52 | Si buscas esto: framework ligero de Python para hacer backtesting de estrategias de trading sobre datos OHLC, con optimización y gráficos interactivos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Elige un ejemplo de consulta de datos, backtesting o simulación que no envíe órdenes reales.
2. Prepara datos de prueba y, si el proveedor lo requiere, una cuenta y credenciales de solo lectura; revisa sus cuotas por separado.
3. Comprueba los resultados y el coste observado. La ejecución con fondos es otra configuración y no se activa como parte de esta primera prueba.

**Entrada documentada (consulta la sintaxis original):**

```
pip install backtesting
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/kernc/backtesting.py/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Backtesting.py para mi objetivo y necesito pasos guiados. Lee https://github.com/kernc/backtesting.py/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install backtesting` y ejecuta el ejemplo SmaCross de la documentación..

**Qué comprobar:** Obtienes estadísticas del backtest y un gráfico interactivo con operaciones..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- probar una estrategia de cruce de medias sobre datos históricos
- optimizar parámetros de una estrategia y ver el resultado en un gráfico interactivo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: probar una estrategia de cruce de medias sobre datos históricos; optimizar parámetros de una estrategia y ver el resultado en un gráfico interactivo | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. No se verificó rentabilidad ni operación con fondos. Licencia AGPL-3.0. Herramienta de investigación: no constituye asesoramiento financiero ni garantiza resultados.

## Stack y modelos

- **Stack:** Python, pyproject.toml, requirements.txt, setup.py
- **Etiquetas:** `finanzas` `python` `library`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [vectorbt](vectorbt.md) | 9.9k | Biblioteca de análisis cuantitativo para explorar señales y comparar estrategias sobre datos de mercado. |

## Enlaces

- 🐙 GitHub: [kernc/backtesting.py](https://github.com/kernc/backtesting.py)
- 🌐 Web: <https://kernc.github.io/backtesting.py/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/kernc/backtesting.py/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
