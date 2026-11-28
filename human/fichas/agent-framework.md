[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks en TypeScript y multi-lenguaje

# 🟦 Microsoft Agent Framework

> Framework de Microsoft para agentes y workflows multiagente en Python y .NET, sucesor de AutoGen y Semantic Kernel.

## Cuándo elegir esta ficha

Microsoft Learn documenta los runtimes. El repositorio no respondió en la consulta directa. Verifica su disponibilidad antes de intentar instalar.

Referencia de consulta del catálogo.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/microsoft/agent-framework/blob/main/README.md) · [Fuente 2](https://github.com/microsoft/agent-framework) · [Fuente 3](https://learn.microsoft.com/en-us/agent-framework/overview/)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.7k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework open source (MIT) de Microsoft para construir, orquestar y desplegar agentes y workflows multiagente. Lo presentan como sucesor de AutoGen y Semantic Kernel, con guías oficiales de migración desde ambos. Es muy activo: el SDK de Python va por la 1.26.0, y hay implementaciones en .NET y un SDK de Go en otro repositorio.

## ¿Qué hace?

Ofrece agentes con varios proveedores de LLM, un sistema de middleware para el procesamiento de peticiones y respuestas, y workflows basados en grafos (secuenciales, concurrentes, con checkpoints y human-in-the-loop). También incluye agentes declarativos en YAML y 'Agent Skills' construidas a partir de varias fuentes. Trae una DevUI para probar y depurar y paquetes experimentales en 'AF Labs' (benchmarks, aprendizaje por refuerzo). Además permite desplegar agentes alojados en Microsoft Foundry.

## ¿Cómo lo hace?

Paquetes `agent-framework` en PyPI (Python) y `Microsoft.Agents.AI` en NuGet (.NET), con una API coherente entre los dos lenguajes. Trae instrumentación OpenTelemetry integrada para trazas distribuidas. Funciona con Azure OpenAI, OpenAI y otros proveedores; parte de las funciones (Foundry Hosted Agents) dependen de servicios de Azure. La documentación está en Microsoft Learn.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [langfuse](langfuse.md) | Trazas de agentes y workflows a través de OpenTelemetry (integración oficial de Langfuse para Microsoft Agent Framework). | Langfuse primero; configura el exportador OTLP antes de crear los agentes. |
| [CopilotKit](copilotkit.md) | Interfaz React/Next.js para agentes de Agent Framework (integración documentada por CopilotKit). | Expón el agente desde el backend de Agent Framework y conecta CopilotKit en el frontend. |
| [ag2](ag2.md) | Útil si migras desde AutoGen 0.2/AG2: hay una guía oficial de migración desde AutoGen. (combinación por arquitectura: no se integran entre sí, se usan como origen y destino de una migración). | Mantén AG2 solo mientras portas los agentes a Agent Framework con la guía de Microsoft. |
| [Ollama](ollama.md) | Modelos locales para desarrollo mediante un endpoint compatible con OpenAI. (combinación por arquitectura) | Arranca Ollama y apunta el cliente compatible con OpenAI a su URL local. |
| [AI Agents for Beginners](ai-agents-for-beginners.md) | Combinación recíproca: AI Agents for Beginners lo enlaza como «Framework usado en todos los ejemplos de código del curso». | Orden indicado desde AI Agents for Beginners: Sigue la lección de configuración del curso; instala agent-framework en Python. |

**Notas:** Sin alternativas declaradas en el catálogo; frameworks comparables: langgraph, crewai, openai-agents-python. Hallazgo: AutoGen (microsoft/autogen) no está en el catálogo; Agent Framework es su sucesor oficial.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada python-1.26.0 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/microsoft/agent-framework/blob/main/README.md) · [2](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen) · [3](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel) · [4](https://docs.langfuse.com/integrations/frameworks/microsoft-agent-framework) · [5](https://docs.copilotkit.ai/microsoft-agent-framework)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Admite Ollama y otros proveedores; Foundry y despliegues gestionados pueden generar gasto |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelos locales documentados. La skill de construcción usa el agente; el runtime tiene autenticación y costes propios; módulos Lab son experimentales |
| Coste | El coste depende del proveedor o la ruta. Admite Ollama y otros proveedores; Foundry y despliegues gestionados pueden generar gasto |
| Equipo | Preparación según la ruta elegida. Python o .NET; proveedor configurado |

La skill de construcción usa el agente; el runtime tiene autenticación y costes propios; módulos Lab son experimentales

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python o .NET
- proveedor configurado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install agent-framework
# This installs the standard package set; install `agent-framework-lab` separately for experimental modules.
# It may take a minute on first install on Windows.
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/microsoft/agent-framework/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Microsoft Agent Framework para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/agent-framework/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prueba un agente y después un workflow con dos pasos y un punto de control.

**Qué comprobar:** Puedes seguir las transiciones y recuperar el estado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Migrar una prueba de Semantic Kernel
- Coordinar especialistas con un flujo explícito

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Migrar una prueba de Semantic Kernel; Coordinar especialistas con un flujo explícito | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La skill de construcción usa el agente; el runtime tiene autenticación y costes propios; módulos Lab son experimentales

## Stack y modelos

- **Stack:** Python o .NET; proveedor configurado
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [microsoft/agent-framework](https://github.com/microsoft/agent-framework)
- 🌐 Web: <https://aka.ms/agent-framework>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/agent-framework/blob/main/README.md)
- [Fuente 2](https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/model-providers/?pivots=programming-language-python)
- [Fuente 3](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
