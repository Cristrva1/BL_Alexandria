[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Modelos y backtesting cuantitativo

# 📚 vectorbt

> Biblioteca de análisis cuantitativo para explorar señales y comparar estrategias sobre datos de mercado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.9k | NOASSERTION | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

VectorBT, toolkit de Python para investigación de trading a escala, de @polakowo. Licencia Apache-2.0 con Commons Clause, «fair-code» que no permite vender el software (GitHub muestra NOASSERTION). Tiene ~10k estrellas (v1.2.1) y una versión comercial, VectorBT PRO.

## ¿Qué hace?

Permite explorar datos de mercado, crear indicadores y señales y comparar miles de estrategias entre activos y marcos temporales con operaciones vectorizadas. Analiza operaciones, comisiones, drawdowns y rendimiento con gráficos interactivos.

## ¿Cómo lo hace?

Se instala con `pip install -U vectorbt` (extras `[full]` y `[rust]`). Usa NumPy, pandas, Numba y Plotly. Algunas dependencias opcionales tienen licencias más restrictivas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ccxt](ccxt.md) | Datos históricos de cripto para los backtests. (combinación por arquitectura) | Descarga velas con CCXT. |
| [freqtrade](freqtrade.md) | Llevar la idea validada a un bot. (combinación por arquitectura) | Reimplementa la estrategia en Freqtrade. |
| [marimo](marimo.md) | Exploración interactiva de resultados. (combinación por arquitectura) | Ejecuta los análisis en notebooks marimo. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (6). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[AutoHedge](autohedge.md) · [binance-trader](binance-trader.md) · [FinRL](finrl.md) · [lumibot](lumibot.md) · [machine-learning-for-trading](machine-learning-for-trading.md) · [Vibe-Trading](vibe-trading.md)

**Notas:** Sin alternativas declaradas. Commons Clause: no es open source según la OSI.

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada v1.2.1 (2026-11-11) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/polakowo/vectorbt/blob/master/README.md) · [2](https://vectorbt.dev)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige LLM; usa Apache-2.0 con Commons Clause y ofrece productos comerciales distintos; datos y cómputo cuestan según ruta |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Probar muchas combinaciones aumenta el riesgo de sobreajuste; sus mensajes comerciales no acreditan una ventaja en tu caso |
| Coste | El coste depende del proveedor o la ruta. No exige LLM; usa Apache-2.0 con Commons Clause y ofrece productos comerciales distintos; datos y cómputo cuestan según ruta |
| Equipo | Preparación según la ruta elegida. Python; dependencias compatibles; serie histórica; comisiones y frecuencia definidas |

Probar muchas combinaciones aumenta el riesgo de sobreajuste; sus mensajes comerciales no acreditan una ventaja en tu caso

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- dependencias compatibles
- serie histórica
- comisiones y frecuencia definidas

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (sh):**

```
pip install -U vectorbt
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/polakowo/vectorbt/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar vectorbt para mi objetivo y necesito pasos guiados. Lee https://github.com/polakowo/vectorbt/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Evalúa unas pocas combinaciones y reserva un periodo fuera de muestra.

**Qué comprobar:** Puedes revisar parámetros, operaciones y resultados separados de entrenamiento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comparar indicadores en una serie
- Explorar sensibilidad de una regla histórica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comparar indicadores en una serie; Explorar sensibilidad de una regla histórica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Probar muchas combinaciones aumenta el riesgo de sobreajuste; sus mensajes comerciales no acreditan una ventaja en tu caso

## Stack y modelos

- **Stack:** Python; dependencias compatibles; serie histórica; comisiones y frecuencia definidas
- **Etiquetas:** `cuant` `framework` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [polakowo/vectorbt](https://github.com/polakowo/vectorbt)
- 🌐 Web: <https://vectorbt.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/polakowo/vectorbt/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
