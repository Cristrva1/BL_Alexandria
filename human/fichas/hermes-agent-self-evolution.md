[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Simulación, evolución y debate entre modelos

# 🕸️ hermes-agent-self-evolution

> Herramientas para optimizar skills, prompts y código de Hermes Agent mediante búsqueda evolutiva con DSPy y GEPA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.7k | — | Python | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 37/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de Nous Research para mejorar automáticamente Hermes Agent mediante evolución de prompts con DSPy y GEPA. El repositorio no tiene archivo LICENSE: la mención 'MIT licensed' del README parece referirse a GEPA [DATO NO VERIFICADO]. Es temprana: solo está implementada la fase 1 y el último push es de junio de 2026.

## ¿Qué hace?

Lee una skill (SKILL.md) de Hermes Agent, genera un dataset de evaluación (sintético o a partir de historial real de sesiones de Claude Code, Copilot y Hermes) y usa GEPA para proponer y seleccionar variantes mejores a partir de trazas de ejecución. El resultado se propone como PR contra hermes-agent. La optimización de descripciones de herramientas, prompts de sistema y código está planificada pero sin implementar.

## ¿Cómo lo hace?

Paquete Python que se instala desde el código fuente (`pip install -e ".[dev]"`) y se apunta al repositorio local de hermes-agent con `HERMES_AGENT_REPO`. No necesita GPU, todo va por llamadas a API; el README estima de 2 a 10 dólares por ejecución. Hay que revisar qué historial de sesiones se envía al LLM, porque puede contener datos sensibles.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [hermes-agent](hermes-agent.md) | Objetivo de la optimización; sin él la herramienta no tiene uso. | Instala Hermes Agent primero y exporta HERMES_AGENT_REPO. |
| [DSPy](dspy.md) | Motor de optimización (DSPy + GEPA) sobre el que está construida. | Se instala como dependencia; consulta la documentación de GEPA en DSPy para entender los parámetros. |
| [Claude Code](claude-code.md) | Su historial de sesiones puede servir como fuente de evaluación real (`--eval-source sessiondb`). | Úsalo solo si aceptas que esas sesiones se procesen con un LLM externo. |

**Notas:** Sin alternativas declaradas. Sin archivo de licencia en el repositorio.

Estado en GitHub: activo · último push 2026-06-17 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NousResearch/hermes-agent-self-evolution/blob/main/README.md) · [2](https://github.com/NousResearch/hermes-agent) · [3](https://dspy.ai/api/optimizers/GEPA/overview/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta documentada opera mediante APIs y no requiere entrenamiento GPU; el presupuesto depende de iteraciones y evaluaciones |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Solo la evolución de skills figura implementada; herramientas, prompts del sistema, código y bucle continuo son fases previstas; lee sesiones Claude Code como datos |
| Coste | Consumo de APIs o servicios. La ruta documentada opera mediante APIs y no requiere entrenamiento GPU; el presupuesto depende de iteraciones y evaluaciones |
| Equipo | Preparación según la ruta elegida. Python; checkout de Hermes Agent; credenciales del optimizador; casos de evaluación |

Solo la evolución de skills figura implementada; herramientas, prompts del sistema, código y bucle continuo son fases previstas; lee sesiones Claude Code como datos

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- checkout de Hermes Agent
- credenciales del optimizador
- casos de evaluación

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Install
git clone https://github.com/NousResearch/hermes-agent-self-evolution.git
cd hermes-agent-self-evolution
pip install -e ".[dev]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/NousResearch/hermes-agent-self-evolution/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar hermes-agent-self-evolution para mi objetivo y necesito pasos guiados. Lee https://github.com/NousResearch/hermes-agent-self-evolution/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Optimiza una skill pequeña con datos sintéticos y compara el candidato antes de aceptarlo.

**Qué comprobar:** Puedes revisar diferencias y puntuaciones manteniendo la versión inicial.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Refinar una skill de revisión de código
- Comparar instrucciones con fallos observados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Refinar una skill de revisión de código; Comparar instrucciones con fallos observados | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Solo la evolución de skills figura implementada; herramientas, prompts del sistema, código y bucle continuo son fases previstas; lee sesiones Claude Code como datos

## Stack y modelos

- **Stack:** Python; checkout de Hermes Agent; credenciales del optimizador; casos de evaluación
- **Etiquetas:** `experimentos` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NousResearch/hermes-agent-self-evolution/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
