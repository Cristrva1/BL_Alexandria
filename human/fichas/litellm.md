[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# 🔀 litellm

> Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 63.3k | NOASSERTION | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

LiteLLM, gateway de IA y SDK de Python de BerriAI que unifica el acceso a más de 100 proveedores de LLM con el formato de OpenAI. El código es MIT, salvo `litellm/enterprise/`, que tiene licencia comercial (por eso GitHub muestra NOASSERTION). Es muy popular (~63k estrellas, v1.10x).

## ¿Qué hace?

Permite llamar a OpenAI, Anthropic, Gemini, Bedrock, Azure, Ollama y otros con una sola interfaz. Como proxy centralizado añade claves virtuales, control de gasto, guardrails, balanceo de carga, enrutamiento automático por complejidad, panel de administración y una pasarela MCP. Funciones como SSO o ciertos guardrails requieren la licencia Enterprise.

## ¿Cómo lo hace?

En el SDK, `completion()` traduce cada llamada al proveedor indicado en el prefijo del modelo (`openai/...`, `anthropic/...`) y `Router` reparte entre modelos. El proxy (`litellm[proxy]`, puerto 4000) expone endpoints compatibles con OpenAI como `/chat/completions`, `/embeddings`, `/responses` y `/messages`, de modo que un cliente de OpenAI solo cambia `base_url`. Los paquetes `litellm` y `litellm-core` no deben instalarse en el mismo entorno. Fija versiones: el 24 de marzo de 2026 se publicaron en PyPI las versiones maliciosas 1.82.7 y 1.82.8, con un ladrón de credenciales. La imagen Docker oficial no se vio afectada.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor local soportado (`ollama`, `ollama_chat`): mezcla modelos locales y de nube con la misma API. | Ollama primero; luego registra sus modelos en LiteLLM. |
| [Open WebUI](open-webui.md) | Interfaz de chat que consume el proxy como si fuera OpenAI. | LiteLLM primero; después añade su URL como conexión en Open WebUI. |
| [langfuse](langfuse.md) | Integración de observabilidad documentada por LiteLLM: trazas, costes y latencia de cada llamada. | Langfuse primero (para tener sus claves); luego actívalo como callback en LiteLLM. |
| [Claude Code](claude-code.md) | El proxy expone `/messages` (formato Anthropic), así que Claude Code puede apuntar a LiteLLM para usar otros modelos o centralizar gasto. (combinación por arquitectura) | LiteLLM proxy primero; luego configura la URL base en Claude Code. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (45). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[activepieces](activepieces.md) · [Agent Development Kit (ADK)](adk-python.md) · [AgentScope](agentscope.md) · [Aider](aider.md) · [AnythingLLM](anything-llm.md) · [Baileys](baileys.md) · [chatbox](chatbox.md) · [ChatDev](chatdev.md) · [Cherry Studio](cherry-studio.md) · [crawl4ai](crawl4ai.md) · [daily_stock_analysis](daily-stock-analysis.md) · [DeepSeek Harness (DSH)](deepseek-harness.md) · [DeepSeek-V3](deepseek-v3.md) · [exo](exo.md) · [FreeToken](freetoken.md) · [graphrag](graphrag.md) · [headroom](headroom.md) · [huginn](huginn.md) · [Khoj](khoj.md) · [LibreChat](librechat.md) · [llama.cpp](llama-cpp.md) · [llm-council](llm-council.md) · [LobeHub](lobehub.md) · [loguru](loguru.md) · [Mercury Agent](mercury-agent.md) · [MiroFish](mirofish.md) · [MLC LLM](mlc-llm.md) · [MLX LM](mlx-lm.md) · [NextChat](nextchat.md) · [onyx](onyx.md) · [OpenAI Agents SDK](openai-agents-python.md) · [openai-python](openai-python.md) · [OpenCode](opencode.md) · [openevolve](openevolve.md) · [OpenManus](openmanus.md) · [Opik](opik.md) · [PDFMathTranslate](pdfmathtranslate.md) · [Presenton](presenton.md) · [promptfoo](promptfoo.md) · [SGLang](sglang.md) · [smolagents](smolagents.md) · [STORM](storm.md) · [TensorRT-LLM](tensorrt-llm.md) · [txtai](txtai.md) · [vLLM](vllm.md)

**Notas:** Alternativas (elige una): omniroute, claude-code-router, backdoor. Incidente de cadena de suministro de marzo de 2026 (PYSEC-2026-2): si instalaste 1.82.7 o 1.82.8, rota todos los secretos y busca `litellm_init.pth`.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.109.1 (2026-11-12) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/BerriAI/litellm/blob/main/README.md) · [2](https://docs.litellm.ai/docs/providers/ollama) · [3](https://docs.litellm.ai/docs/observability/langfuse_integration) · [4](https://docs.litellm.ai/blog/security-update-march-2026) · [5](https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Las llamadas siguen usando claves, cuotas y precios de cada proveedor; Ollama y LM Studio permiten rutas locales |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Documenta harnesses de Claude Code y Codex en el SDK; pasar por el gateway no incorpora suscripciones ni elimina diferencias entre protocolos |
| Coste | El coste depende del proveedor o la ruta. Las llamadas siguen usando claves, cuotas y precios de cada proveedor; Ollama y LM Studio permiten rutas locales |
| Equipo | Preparación según la ruta elegida. Python y uv; proveedor o endpoint local; presupuesto de prueba |

Documenta harnesses de Claude Code y Codex en el SDK; pasar por el gateway no incorpora suscripciones ni elimina diferencias entre protocolos

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- proveedor o endpoint local
- presupuesto de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
uv add litellm
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/BerriAI/litellm/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar litellm para mi objetivo y necesito pasos guiados. Lee https://github.com/BerriAI/litellm/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un único proveedor y envía una petición breve antes de activar fallback y balanceo.

**Qué comprobar:** Puedes identificar el proveedor real y su consumo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Unificar llamadas a varios modelos
- Enrutar un agente por un gateway propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Unificar llamadas a varios modelos; Enrutar un agente por un gateway propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta harnesses de Claude Code y Codex en el SDK; pasar por el gateway no incorpora suscripciones ni elimina diferencias entre protocolos

## Stack y modelos

- **Stack:** Python y uv; proveedor o endpoint local; presupuesto de prueba
- **Etiquetas:** `inference` `llmops` `python` `docker`
- **Modo de instalación sugerido:** 📦 **Dependencia del proyecto** — instálalo dentro de cada proyecto que lo use

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OmniRoute](omniroute.md) | 87.5k | Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso. |
| [claude-code-router](claude-code-router.md) | 38.1k | Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local. |
| [backdoor](backdoor.md) | 302 | Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code. |

## Enlaces

- 🐙 GitHub: [BerriAI/litellm](https://github.com/BerriAI/litellm)
- 🌐 Web: <https://docs.litellm.ai/docs/>
- 🧪 Receta: [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md)
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)
- 🧪 Receta: [Agente de voz en tiempo real](../playbooks/agente-de-voz.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/BerriAI/litellm/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
