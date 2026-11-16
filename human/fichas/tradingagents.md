[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Agentes de investigación financiera

# 📊 TradingAgents

> Framework experimental que organiza agentes de análisis financiero, debate y evaluación de decisiones de trading.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 123k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

TradingAgents, framework multiagente con LLM para trading financiero, de Tauric Research. Licencia Apache-2.0. Es muy popular (~123k estrellas, v0.7.1) y su README promociona Trading-R1, en acceso anticipado.

## ¿Qué hace?

Simula una firma de trading con analistas (fundamental, sentimiento, noticias, técnico), investigadores alcista y bajista que debaten, un trader, gestión de riesgo y gestor de cartera. Puntúa las decisiones sobre cierres reales y evita datos posteriores a la fecha simulada.

## ¿Cómo lo hace?

Está construido con LangGraph (con reanudación por checkpoints) y se instala con `uv pip install .` o con Docker Compose, con perfil para Ollama. Admite muchos proveedores de LLM, incluida una suscripción de ChatGPT.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph](langgraph.md) | Framework sobre el que está construido. | Viene en las dependencias. |
| [Ollama](ollama.md) | Perfil de Docker Compose para modelos locales. | Ejecuta `docker compose --profile ollama run --rm tradingagents-ollama`. |
| [dexter](dexter.md) | Investigación financiera previa con otro agente. (combinación por arquitectura) | Pasa los hallazgos de Dexter como contexto. |

**Notas:** Sin alternativas declaradas. Herramienta de investigación. Riesgo financiero: no es asesoramiento de inversión.

Estado en GitHub: activo · último push 2026-11-04 · última versión publicada v0.7.1 (2026-10-27) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/TauricResearch/TradingAgents/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Admite Ollama y servidores compatibles, además de APIs; datos y múltiples llamadas por análisis pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La investigación multiagente no equivale a rentabilidad validada ni a un motor listo para operar capital |
| Coste | El coste depende del proveedor o la ruta. Admite Ollama y servidores compatibles, además de APIs; datos y múltiples llamadas por análisis pueden costar |
| Equipo | Preparación según la ruta elegida. Python; proveedor u Ollama; datos; configuración del grafo |

La investigación multiagente no equivale a rentabilidad validada ni a un motor listo para operar capital

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- proveedor u Ollama
- datos
- configuración del grafo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents

pip install .
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/TauricResearch/TradingAgents/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar TradingAgents para mi objetivo y necesito pasos guiados. Lee https://github.com/TauricResearch/TradingAgents/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Analiza un periodo histórico pequeño y revisa fuentes y mensajes de cada especialista.

**Qué comprobar:** Puedes identificar qué evidencia apoya cada conclusión y el coste de llamadas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar debate entre agentes financieros
- Comparar proveedores sobre la misma muestra histórica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar debate entre agentes financieros; Comparar proveedores sobre la misma muestra histórica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La investigación multiagente no equivale a rentabilidad validada ni a un motor listo para operar capital

## Stack y modelos

- **Stack:** Python; proveedor u Ollama; datos; configuración del grafo
- **Etiquetas:** `finanzas` `agent` `finance` `llm` `multiagent` `trading` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- 🌐 Web: <https://tauric.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/TauricResearch/TradingAgents/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
