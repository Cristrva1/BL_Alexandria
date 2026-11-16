[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Agentes de investigación financiera

# 📊 QuantHarness

> Sistema experimental de agentes LLM que combina indicadores técnicos, patrones y tendencias para análisis de trading.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.9k | MIT | HTML | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Puntuación de calidad** 45/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

QuantHarness, sistema multiagente con LLM para trading de alta frecuencia guiado por precios, de investigadores de Stony Brook, CMU, UBC, Yale y Fudan. Licencia MIT. Es un prototipo de investigación (~3k estrellas, sin releases) con último cambio en agosto de 2026.

## ¿Qué hace?

Combina indicadores técnicos, reconocimiento de patrones en gráficos y análisis de tendencia con agentes de LangChain y LangGraph, y ofrece interfaz web. Los agentes generan y analizan gráficos, por lo que requiere un LLM con entrada de imágenes.

## ¿Cómo lo hace?

Se instala con `pip install -r requirements.txt` y se configuran claves de un LLM multimodal y de datos de mercado.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph](langgraph.md) | Framework de orquestación de los agentes. | Viene en las dependencias. |
| [langchain](langchain.md) | Componentes de LLM y herramientas. | Viene en las dependencias. |
| [langfuse](langfuse.md) | Trazar las llamadas de sus agentes de LangChain y LangGraph con la integración de Langfuse para LangChain (combinación por arquitectura). | Langfuse en marcha y sus claves en el entorno; después añade el callback de Langfuse a la ejecución de los agentes. |

**Notas:** Sin alternativas declaradas. Prototipo académico. Riesgo financiero: no es asesoramiento de inversión.

Estado en GitHub: activo · último push 2026-08-18 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Y-Research-SBU/QuantHarness/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta documentada pide API LLM con visión; datos, agentes múltiples y evaluación acumulan consumo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El resultado de investigación no acredita ejecución HFT ni rendimiento futuro; no se confirma aquí un backend local compatible con todo el flujo |
| Coste | El coste depende del proveedor o la ruta. La ruta documentada pide API LLM con visión; datos, agentes múltiples y evaluación acumulan consumo |
| Equipo | Preparación según la ruta elegida. Python; checkout; datos; modelo con entrada de imagen y credenciales |

El resultado de investigación no acredita ejecución HFT ni rendimiento futuro; no se confirma aquí un backend local compatible con todo el flujo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- checkout
- datos
- modelo con entrada de imagen y credenciales

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install -r requirements.txt
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Y-Research-SBU/QuantHarness/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar QuantHarness para mi objetivo y necesito pasos guiados. Lee https://github.com/Y-Research-SBU/QuantHarness/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Reproduce una evaluación histórica pequeña y revisa los gráficos que recibe cada agente.

**Qué comprobar:** Puedes separar datos del periodo, análisis visual y decisión generada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar agentes que interpretan gráficos
- Comparar componentes de un análisis experimental

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar agentes que interpretan gráficos; Comparar componentes de un análisis experimental | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El resultado de investigación no acredita ejecución HFT ni rendimiento futuro; no se confirma aquí un backend local compatible con todo el flujo

## Stack y modelos

- **Stack:** Python; checkout; datos; modelo con entrada de imagen y credenciales
- **Etiquetas:** `finanzas` `agentic-ai` `large-language-models` `html`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Y-Research-SBU/QuantHarness](https://github.com/Y-Research-SBU/QuantHarness)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Y-Research-SBU/QuantHarness/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
