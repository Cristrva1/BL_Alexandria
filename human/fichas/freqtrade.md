[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Bots y conexiones a exchanges

# 🖥️ freqtrade

> Bot de trading de criptomonedas con herramientas para preparar estrategias, hacer backtesting y operar en simulación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 56.9k | GPL-3.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Puntuación de calidad** 78/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Freqtrade, bot de trading de criptomonedas en Python. Licencia GPL-3.0. Es muy maduro (~57k estrellas, 2026.10).

## ¿Qué hace?

Ejecuta estrategias en los principales exchanges, con backtesting, optimización de hiperparámetros, gráficos y FreqAI para modelos de ML adaptativos. Se controla por Telegram o una interfaz web. El README insiste en que es educativo y en empezar en modo dry-run.

## ¿Cómo lo hace?

Requiere Python 3.12+ y se instala con Docker (recomendado) o con un script. Se conecta a los exchanges mediante CCXT.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ccxt](ccxt.md) | Capa de conexión con exchanges. | Viene incluida como dependencia. |
| [vectorbt](vectorbt.md) | Explorar ideas rápidamente antes de codificar la estrategia. (combinación por arquitectura) | Prototipa con vectorbt y porta a Freqtrade. |
| [Grafana](grafana.md) | Paneles de rendimiento a partir de la base de datos del bot. (combinación por arquitectura) | Conecta Grafana a la base SQL de Freqtrade. |

**Notas:** Sin alternativas declaradas. Riesgo financiero alto: empieza en dry-run.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 2026.10 (2026-10-30) · licencia declarada GPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/freqtrade/freqtrade/blob/develop/README.md) · [2](https://www.freqtrade.io/en/stable/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El bot básico no exige LLM; FreqAI, datos, infraestructura y exchanges tienen requisitos y costes separados |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Backtest y dry-run son fases distintas; no conectes resultados históricos con una promesa de rendimiento futuro |
| Coste | El coste depende del proveedor o la ruta. El bot básico no exige LLM; FreqAI, datos, infraestructura y exchanges tienen requisitos y costes separados |
| Equipo | Preparación según la ruta elegida. Docker o entorno de la guía; datos; estrategia de ejemplo; modo dry-run |

Backtest y dry-run son fases distintas; no conectes resultados históricos con una promesa de rendimiento futuro

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o entorno de la guía
- datos
- estrategia de ejemplo
- modo dry-run

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://www.freqtrade.io/en/stable/docker_quickstart/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar freqtrade para mi objetivo y necesito pasos guiados. Lee https://www.freqtrade.io/en/stable/docker_quickstart/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta un backtest pequeño y revisa comisiones y sesgos antes de pasar a dry-run.

**Qué comprobar:** Puedes reproducir operaciones simuladas y su configuración.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comparar una regla en datos históricos
- Evaluar una estrategia en simulación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comparar una regla en datos históricos; Evaluar una estrategia en simulación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Backtest y dry-run son fases distintas; no conectes resultados históricos con una promesa de rendimiento futuro

## Stack y modelos

- **Stack:** Docker o entorno de la guía; datos; estrategia de ejemplo; modo dry-run
- **Etiquetas:** `bots` `app` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade)
- 🌐 Web: <https://www.freqtrade.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/freqtrade/freqtrade/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
