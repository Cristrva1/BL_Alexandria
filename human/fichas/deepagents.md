[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 Deep Agents

> Arnés de agentes de LangChain listo para usar, con planificación, subagentes y sistema de archivos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.3k | MIT | Python | 2026-08-23 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## ¿Qué es?

Harness de agentes de código abierto (MIT) de LangChain, «con pilas incluidas», que funciona sin configuración y es extensible. Activo (0.7.38), con versión JS/TS.

## ¿Qué hace?

Trae defaults para trabajo largo y multipaso: subagentes con contexto aislado, sistema de archivos con backends locales, en sandbox o remotos, gestión de contexto (resume hilos y descarga salidas de herramientas a disco), acceso a shell en el sandbox elegido, memoria persistente, aprobación humana de herramientas, skills y herramientas propias o de cualquier servidor MCP.

## ¿Cómo lo hace?

Se instala con `uv add deepagents` y está construido sobre LangGraph (streaming, persistencia, checkpoints), con trazas, evaluación y despliegue mediante LangSmith. Es agnóstico de modelo: vale cualquier LLM con tool calling, incluidos modelos locales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph](langgraph.md) | Base de ejecución sobre la que está construido. | Se instala como dependencia; baja a LangGraph para personalizar el grafo. |
| [langchain](langchain.md) | Modelos e integraciones del mismo ecosistema. | Añade los paquetes del proveedor de modelos. |
| [langfuse](langfuse.md) | Trazas de código abierto mediante la integración de Langfuse con LangChain/LangGraph (combinación por arquitectura). | Configura el callback antes de producción. |

**Notas:** Alternativa (elige una): openai-agents-python. Si da shell al agente, úsalo dentro de un sandbox.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada deepagents==0.7.38 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/langchain-ai/deepagents/blob/main/README.md) · [2](https://langfuse.com/integrations/frameworks/langchain)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Usa el modelo configurado y sus costes; Ollama, vLLM y llama.cpp requieren hardware suficiente |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Su parecido con Claude Code no acredita el uso de la suscripción de Claude Code |
| Coste | El coste depende del proveedor o la ruta. Usa el modelo configurado y sus costes; Ollama, vLLM y llama.cpp requieren hardware suficiente |
| Equipo | Preparación según la ruta elegida. Python y uv; modelo con herramientas; directorio de prueba |

Su parecido con Claude Code no acredita el uso de la suscripción de Claude Code

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- modelo con herramientas
- directorio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv add deepagents
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/langchain-ai/deepagents/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Deep Agents para mi objetivo y necesito pasos guiados. Lee https://github.com/langchain-ai/deepagents/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide un plan y un informe sobre tres archivos de ejemplo.

**Qué comprobar:** Puedes revisar el plan, las lecturas y el informe guardado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Resumir documentos de proyecto
- Dividir una revisión de archivos en tareas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Resumir documentos de proyecto; Dividir una revisión de archivos en tareas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Su parecido con Claude Code no acredita el uso de la suscripción de Claude Code

## Stack y modelos

- **Stack:** Python y uv; modelo con herramientas; directorio de prueba
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenAI Agents SDK](openai-agents-python.md) | 30.7k | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. |

## Enlaces

- 🐙 GitHub: [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)
- 🌐 Web: <https://docs.langchain.com/deepagents>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langchain-ai/deepagents/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
