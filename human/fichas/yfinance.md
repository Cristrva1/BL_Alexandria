[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Modelos y backtesting cuantitativo

# 📚 yfinance

> Biblioteca Python no oficial para descargar datos de mercado y fundamentales de Yahoo! Finance en DataFrames de pandas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.9k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de código abierto (Apache-2.0) creada por Ran Aroussi, muy usada en investigación y educación. No está afiliada ni respaldada por Yahoo, Inc.

## ¿Qué hace?

Ofrece una forma pythónica de obtener datos de Yahoo Finance: históricos de precios, dividendos y splits, fundamentales, calendarios, opciones, noticias y búsqueda, para uno o varios símbolos, con caché.

## ¿Cómo lo hace?

Se instala con `pip install yfinance`; usa `Ticker`, `Tickers` y `download` y devuelve DataFrames de pandas. Depende de endpoints no documentados que Yahoo puede limitar o cambiar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vectorbt](vectorbt.md) | vectorbt incluye una clase de datos que descarga históricos con yfinance para backtests vectorizados. | Instala ambos; después usa la descarga de Yahoo de vectorbt. |
| [Backtesting.py](backtesting-py.md) | Los DataFrames OHLC de yfinance se pasan directamente a Backtesting.py (combinación por arquitectura). | Descarga con yfinance; después ejecuta el backtest con ese DataFrame. |
| [JupyterLab](jupyterlab.md) | yfinance se usa habitualmente en cuadernos para explorar y graficar datos de mercado (combinación por arquitectura). | Instala yfinance en el entorno del cuaderno. |

**Notas:** Para usos profesionales, considera un proveedor de datos con licencia.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 1.8.0 (2026-11-03) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ranaroussi/yfinance/blob/main/README.md) · [2](https://ranaroussi.github.io/yfinance) · [3](https://vectorbt.dev/api/data/custom/)</sub>

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
pip install yfinance
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/ranaroussi/yfinance/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar yfinance para mi objetivo y necesito pasos guiados. Lee https://github.com/ranaroussi/yfinance/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install yfinance` y descarga un año de precios de un símbolo con `Ticker(...).history`..

**Qué comprobar:** Obtienes un DataFrame con precios OHLC, volumen y fechas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- descargar históricos de precios para un estudio o backtest
- obtener fundamentales y dividendos de una cartera en un cuaderno

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: descargar históricos de precios para un estudio o backtest; obtener fundamentales y dividendos de una cartera en un cuaderno | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. No se verificó rentabilidad ni operación con fondos. No está afiliado a Yahoo: usa sus APIs públicas, destinadas a uso personal, sujetas a sus términos y a cambios sin aviso. Herramienta de investigación: no constituye asesoramiento financiero ni garantiza resultados.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `finanzas` `python` `library` `data`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ranaroussi/yfinance](https://github.com/ranaroussi/yfinance)
- 🌐 Web: <https://ranaroussi.github.io/yfinance>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ranaroussi/yfinance/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
