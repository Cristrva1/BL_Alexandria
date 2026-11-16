[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 DSPy

> Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.1k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Framework de Stanford NLP (MIT) para «programar, no promptear» modelos de lenguaje (Declarative Self-improving Python). Maduro y activo (3.5.0).

## ¿Qué hace?

Permite construir sistemas de IA modulares con código Python compositivo en lugar de prompts frágiles, y ofrece optimizadores que ajustan automáticamente prompts y pesos según una métrica, tanto para clasificadores simples como para pipelines RAG o agentes.

## ¿Cómo lo hace?

Se instala con `pip install dspy`. La integración con LM usa motores nativos `lm15` integrados, sin dependencia de LiteLLM; esto rompe opciones de proveedor anteriores y hay guía de migración. La documentación completa está en dspy.ai.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [MLflow](mlflow.md) | Seguimiento de experimentos y trazas con el flavor oficial de DSPy en MLflow. | Activa el autolog de MLflow antes de optimizar. |
| [langfuse](langfuse.md) | Trazas de los programas DSPy con la integración oficial de Langfuse. | Instrumenta antes de las ejecuciones. |
| [Ragas](ragas.md) | Métricas de RAG como objetivo para los optimizadores (combinación por arquitectura). | Define la métrica antes de compilar. |

**Notas:** Alternativa (elige una): promptfoo. Si actualizas desde versiones con LiteLLM, revisa la guía de migración.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada 3.5.0 (2026-11-10) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/stanfordnlp/dspy/blob/main/README.md) · [2](https://mlflow.org/docs/latest/genai/flavors/dspy/) · [3](https://langfuse.com/integrations/frameworks/dspy) · [4](https://dspy.ai/tutorials/observability/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La optimización repite llamadas y puede acumular consumo; la guía también ofrece Ollama local |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Reserva ejemplos distintos para medir el resultado de la optimización |
| Coste | El coste depende del proveedor o la ruta. La optimización repite llamadas y puede acumular consumo; la guía también ofrece Ollama local |
| Equipo | Preparación según la ruta elegida. Python; modelo elegido; casos etiquetados |

Reserva ejemplos distintos para medir el resultado de la optimización

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- modelo elegido
- casos etiquetados

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install dspy
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/stanfordnlp/dspy/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DSPy para mi objetivo y necesito pasos guiados. Lee https://github.com/stanfordnlp/dspy/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clasifica tema y urgencia de cinco mensajes ficticios antes de optimizar.

**Qué comprobar:** Obtienes campos estructurados y una medida de aciertos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Clasificar solicitudes de soporte
- Optimizar un extractor de datos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Clasificar solicitudes de soporte; Optimizar un extractor de datos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Reserva ejemplos distintos para medir el resultado de la optimización

## Stack y modelos

- **Stack:** Python; modelo elegido; casos etiquetados
- **Etiquetas:** `prompts` `evaluation` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [promptfoo](promptfoo.md) | 27.2k | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. |

## Enlaces

- 🐙 GitHub: [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)
- 🌐 Web: <https://dspy.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/stanfordnlp/dspy/blob/main/README.md)
- [Fuente 2](https://dspy.ai/getting-started/installation/)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
