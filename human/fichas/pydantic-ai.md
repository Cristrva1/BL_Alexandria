[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 Pydantic AI

> Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 21.2k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

SDK de IA para Python (MIT) del equipo de Pydantic: un bucle de agente tipado y extensible. Muy activo (v2.68.0). Se apoya en productos comerciales de la misma empresa (Logfire, AI Gateway).

## ¿Qué hace?

Cubre agentes, voz en tiempo real, generación de imágenes y embeddings con cualquier modelo (OpenAI, Anthropic, Google, Bedrock, Groq, Mistral, xAI, Ollama y docenas más), cambiando solo una cadena. Pydantic AI Harness añade capacidades para trabajo largo (memoria, archivos, shell con lista blanca), Pydantic Evals evalúa salidas y trayectorias, y la ejecución duradera se hace con Temporal y otros.

## ¿Cómo lo hace?

Se instala con `uv add pydantic-ai` (extras como `[temporal]` o `[openai-realtime]`), con validación de tipos de extremo a extremo. Para observabilidad recomienda Pydantic Logfire, que es comercial, y soporta MCP.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [langfuse](langfuse.md) | Trazas de código abierto con la integración oficial, como alternativa a Logfire. | Instrumenta vía OpenTelemetry. |
| [FastMCP](fastmcp.md) | Servidores MCP propios como herramientas; Pydantic AI documenta el cliente MCP (combinación por arquitectura). | Servidor MCP primero. |
| [Ollama](ollama.md) | Proveedor de modelos locales soportado. | Ollama con el modelo descargado primero. |
| [browser-use](browser-use.md) | Combinación recíproca: browser-use lo enlaza como «Browser Use 1.0 está construido sobre Pydantic AI y acepta cualquier cadena de modelo de Pydantic AI». | Orden indicado desde browser-use: Instala el extra correspondiente de pydantic-ai para el proveedor elegido. |
| [loguru](loguru.md) | Combinación recíproca: loguru lo enlaza como «Logging sencillo en agentes Python. (combinación por arquitectura)». | Orden indicado desde loguru: Configura Loguru al iniciar el agente. |
| [MCP Python SDK](mcp-python-sdk.md) | Combinación recíproca: MCP Python SDK lo enlaza como «Usar servidores MCP desde agentes Pydantic AI. (combinación por arquitectura)». | Orden indicado desde MCP Python SDK: Conecta el servidor como toolset MCP. |

**Notas:** Alternativas (elige una): openai-agents-python, smolagents, langgraph.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.68.0 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pydantic/pydantic-ai/blob/main/README.md) · [2](https://langfuse.com/integrations/frameworks/pydantic-ai) · [3](https://ai.pydantic.dev/mcp/) · [4](https://ai.pydantic.dev/models/overview/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Admite Ollama y APIs; Logfire opcional y servicios asociados se presupuestan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Empieza con el paquete base; el harness de programación es un componente adicional |
| Coste | El coste depende del proveedor o la ruta. Admite Ollama y APIs; Logfire opcional y servicios asociados se presupuestan aparte |
| Equipo | Preparación según la ruta elegida. Python y uv; esquema de salida; modelo |

Empieza con el paquete base; el harness de programación es un componente adicional

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- esquema de salida
- modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv add pydantic-ai
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/pydantic/pydantic-ai/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Pydantic AI para mi objetivo y necesito pasos guiados. Lee https://github.com/pydantic/pydantic-ai/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Extrae nombre, importe y moneda de una factura ficticia.

**Qué comprobar:** El resultado respeta los tipos o informa del fallo de validación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Extraer campos de mensajes
- Validar datos generados antes de guardarlos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Extraer campos de mensajes; Validar datos generados antes de guardarlos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Empieza con el paquete base; el harness de programación es un componente adicional

## Stack y modelos

- **Stack:** Python y uv; esquema de salida; modelo
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenAI Agents SDK](openai-agents-python.md) | 30.7k | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. |
| [smolagents](smolagents.md) | 30.4k | Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. |
| [LangGraph](langgraph.md) | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |

## Enlaces

- 🐙 GitHub: [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)
- 🌐 Web: <https://pydantic.dev/pydantic-ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pydantic/pydantic-ai/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
