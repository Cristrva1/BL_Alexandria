[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Agentes de investigación financiera

# 📊 AutoHedge

> Experimento de agentes coordinados para análisis de mercado, riesgo y flujos de trading automatizado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.7k | MIT | Python | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; requiere clave de API

**Puntuación de calidad** 46/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

AutoHedge, «fondo de cobertura autónomo» de agentes de The Swarm Corporation. Licencia MIT. Tiene ~7k estrellas (sin releases) y su último cambio es de mayo de 2026.

## ¿Qué hace?

Combina agentes especializados (análisis de mercado, tesis, riesgo, ejecución) construidos con el framework Swarms para analizar y operar de forma continua. Por ahora solo opera de forma autónoma en Solana; Coinbase y otros exchanges están anunciados como «próximamente».

## ¿Cómo lo hace?

Se instala con `pip install -U autohedge` y se configura con claves de LLM y una clave privada de wallet (`WALLET_PRIVATE_KEY`). El README lo califica de «enterprise-grade», calificación que no se pudo comprobar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ccxt](ccxt.md) | Obtener datos de mercado de exchanges centralizados para análisis. (combinación por arquitectura) | Usa CCXT en un módulo de datos aparte. |
| [LangGraph](langgraph.md) | Reimplementar el flujo de agentes con control explícito de estados. (combinación por arquitectura) | Compara con un grafo propio en LangGraph. |
| [vectorbt](vectorbt.md) | Validar las tesis con backtesting antes de operar. (combinación por arquitectura) | Backtestea la lógica en vectorbt. |

**Notas:** Sin alternativas declaradas. Riesgo muy alto: opera con una clave privada real de forma autónoma. Riesgo financiero: no es asesoramiento de inversión.

Estado en GitHub: activo · último push 2026-05-11 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/The-Swarm-Corporation/AutoHedge/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. El ejemplo pide claves OpenAI o Anthropic y Jupiter; operaciones y proveedores pueden tener comisiones y consumo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El README incluye WALLET_PRIVATE_KEY; no es una simple app de lectura y no se ha verificado aquí una simulación aislada |
| Coste | El coste depende del proveedor o la ruta. El ejemplo pide claves OpenAI o Anthropic y Jupiter; operaciones y proveedores pueden tener comisiones y consumo |
| Equipo | Preparación según la ruta elegida. Python; credenciales de modelo y herramientas; entorno de investigación sin fondos |

El README incluye WALLET_PRIVATE_KEY; no es una simple app de lectura y no se ha verificado aquí una simulación aislada

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- credenciales de modelo y herramientas
- entorno de investigación sin fondos

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install -U autohedge
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/The-Swarm-Corporation/AutoHedge/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AutoHedge para mi objetivo y necesito pasos guiados. Lee https://github.com/The-Swarm-Corporation/AutoHedge/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa la configuración de agentes y sus herramientas antes de ejecutar un flujo de análisis de prueba.

**Qué comprobar:** Puedes distinguir consulta, decisión y funciones que enviarían operaciones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar coordinación de analistas y riesgo
- Revisar el diseño de un pipeline de trading

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar coordinación de analistas y riesgo; Revisar el diseño de un pipeline de trading | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README incluye WALLET_PRIVATE_KEY; no es una simple app de lectura y no se ha verificado aquí una simulación aislada

## Stack y modelos

- **Stack:** Python; credenciales de modelo y herramientas; entorno de investigación sin fondos
- **Etiquetas:** `finanzas` `ai` `blackrock` `finance` `goldmansachs` `hedgefund` `jpmorgan` `ml`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [The-Swarm-Corporation/AutoHedge](https://github.com/The-Swarm-Corporation/AutoHedge)
- 🌐 Web: <https://swarms.xyz/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/The-Swarm-Corporation/AutoHedge/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
