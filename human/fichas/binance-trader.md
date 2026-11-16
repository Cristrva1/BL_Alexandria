[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Bots y conexiones a exchanges

# 📊 binance-trader

> Bot experimental de Python para estudiar estrategias y automatización con la API de Binance.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.8k | — | Python | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 36/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Binance Trader, bot experimental de Python para operar en Binance, de @yasinkuyu. El README declara MIT pero el repo no tiene archivo de licencia que GitHub detecte. Tiene ~3k estrellas y su última versión (v1.1.0) es de enero de 2026.

## ¿Qué hace?

Automatiza compras y ventas con una estrategia sencilla basada en márgenes sobre pares de Binance. La v1.1.0 corrige errores antiguos de órdenes, precisión de lotes y concurrencia.

## ¿Cómo lo hace?

Es un script de Python con dependencias mínimas (`requests`) y una imagen Docker. Requiere claves de API de Binance.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ccxt](ccxt.md) | Migrar a una librería de exchanges mantenida y multiplataforma. (combinación por arquitectura) | Reescribe las llamadas con CCXT. |
| [vectorbt](vectorbt.md) | Evaluar la estrategia con datos históricos. (combinación por arquitectura) | Backtestea antes de usar dinero real. |
| [coolify](coolify.md) | Desplegar su imagen Docker en un servidor propio gestionado con Coolify (combinación por arquitectura). | Coolify primero; las claves de API de Binance como secretos y con permisos mínimos (sin retirada de fondos). |

**Notas:** Sin alternativas declaradas. Proyecto experimental. Riesgo financiero: no es asesoramiento de inversión.

Estado en GitHub: activo · último push 2026-01-03 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/yasinkuyu/binance-trader/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa LLM; operaciones, datos, red y exchange tienen costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Bot experimental con documentación antigua; no se confirma que sus endpoints funcionen hoy ni que tenga una simulación completa |
| Coste | El coste depende del proveedor o la ruta. No usa LLM; operaciones, datos, red y exchange tienen costes propios |
| Equipo | Preparación según la ruta elegida. Python y dependencias históricas; API Binance solo para funciones privadas; entorno aislado |

Bot experimental con documentación antigua; no se confirma que sus endpoints funcionen hoy ni que tenga una simulación completa

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y dependencias históricas
- API Binance solo para funciones privadas
- entorno aislado

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/yasinkuyu/binance-trader/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar binance-trader para mi objetivo y necesito pasos guiados. Lee https://github.com/yasinkuyu/binance-trader/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Examina la configuración y localiza las llamadas de lectura y de creación de órdenes sin activar el bot.

**Qué comprobar:** Puedes identificar qué credenciales y acciones afectarán una cuenta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar una estrategia de ejemplo
- Analizar cómo se conecta un bot a un exchange

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar una estrategia de ejemplo; Analizar cómo se conecta un bot a un exchange | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Bot experimental con documentación antigua; no se confirma que sus endpoints funcionen hoy ni que tenga una simulación completa

## Stack y modelos

- **Stack:** Python y dependencias históricas; API Binance solo para funciones privadas; entorno aislado
- **Etiquetas:** `finanzas` `arbitrage` `binance` `bitcoin` `btc` `cryptocurrency` `trade` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [yasinkuyu/binance-trader](https://github.com/yasinkuyu/binance-trader)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/yasinkuyu/binance-trader/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
