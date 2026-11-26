[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Modelos y backtesting cuantitativo

# 📚 OpenBB Open Data Platform

> Plataforma abierta de datos financieros (ODP): conecta fuentes públicas y con licencia una vez y las expone a Python, Excel, APIs REST y servidores MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 75.5k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Conjunto de herramientas de datos de código abierto (Apache-2.0) creado por OpenBB. Desde octubre de 2026 lo custodia OpenBQ, una organización sin ánimo de lucro anunciada por OpenBB y liderada desde BrightQuery; por eso el repositorio canónico es ahora openbq-org/OpenBB. Muy popular y activo.

## ¿Qué hace?

Integra fuentes de datos públicas, propietarias y con licencia (acciones, ETF, renta fija, divisas, cripto, derivados, macroeconomía, noticias) y las expone a la vez a entornos Python, OpenBB Workspace y Excel, servidores MCP para agentes y APIs REST. Incluye extensiones de análisis cuantitativo, técnico y econométrico.

## ¿Cómo lo hace?

Se instala con `pip install openbb` (CLI aparte con `pip install openbb-cli`); los datos se consultan con `from openbb import obb`. Los proveedores se configuran con sus credenciales; la extensión `mcp_server` y `platform_api` publican los datos para agentes y aplicaciones.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | OpenBB incluye una extensión de servidor MCP para que los agentes consulten sus datos. | Instala OpenBB y la extensión mcp_server; después registra el servidor en Claude Code. |
| [JupyterLab](jupyterlab.md) | Las consultas de OpenBB devuelven DataFrames que se analizan en cuadernos de JupyterLab (combinación por arquitectura). | Instala openbb en el entorno del cuaderno; después consulta y grafica los datos. |
| [vectorbt](vectorbt.md) | Los históricos obtenidos con OpenBB pueden alimentar backtests vectorizados con vectorbt (combinación por arquitectura). | Descarga los datos con OpenBB; después pásalos a vectorbt. |
| [Backtesting.py](backtesting-py.md) | Los precios OHLC de OpenBB sirven como entrada para estrategias en Backtesting.py (combinación por arquitectura). | Convierte la salida a DataFrame OHLC; después ejecuta el backtest. |

**Notas:** El README todavía enlaza a OpenBB-finance/OpenBB; la API de GitHub redirige el mismo repositorio (id 323048702) a openbq-org/OpenBB, y openbb.co confirma el traspaso a OpenBQ.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada ODP (2026-09-30) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/openbq-org/OpenBB/blob/develop/README.md) · [2](https://openbb.co) · [3](https://github.com/openbq-org/OpenBB/tree/develop/openbb_platform/extensions/mcp_server)</sub>

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
pip install openbb
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/openbq-org/OpenBB/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenBB Open Data Platform para mi objetivo y necesito pasos guiados. Lee https://github.com/openbq-org/OpenBB/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install openbb` y descarga el histórico de precios de un símbolo con `obb.equity.price.historical`..

**Qué comprobar:** Obtienes un DataFrame con fechas y precios del proveedor configurado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- descargar series de precios o datos macro en un DataFrame para análisis
- dar a un agente acceso a datos financieros mediante el servidor MCP de OpenBB

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: descargar series de precios o datos macro en un DataFrame para análisis; dar a un agente acceso a datos financieros mediante el servidor MCP de OpenBB | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. No se verificó rentabilidad ni operación con fondos. Herramienta de investigación: no constituye asesoramiento financiero ni garantiza resultados. Muchos proveedores de datos requieren claves y tienen términos propios.

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `finanzas` `python` `data` `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [openbq-org/OpenBB](https://github.com/openbq-org/OpenBB)
- 🌐 Web: <https://openbb.co>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openbq-org/OpenBB/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
