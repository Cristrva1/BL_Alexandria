[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks en TypeScript y multi-lenguaje

# 🟦 AI SDK (Vercel)

> Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Toolkit TypeScript de Vercel (AI SDK) para construir aplicaciones y agentes con IA. El LICENSE es Apache-2.0 aunque GitHub no reconozca la licencia (NOASSERTION). Es un monorepo maduro y muy activo, con publicaciones casi a diario de paquetes como `ai`, `@ai-sdk/react` o `@ai-sdk/vue`.

## ¿Qué hace?

Unifica la llamada a modelos de muchos proveedores (texto, objetos estructurados, herramientas, streaming) tras una sola API. Incluye la clase `ToolLoopAgent` para agentes que ejecutan herramientas en bucle. También trae AI SDK UI, hooks para React, Vue, Svelte y otros frameworks que gestionan el estado de chats con streaming. Por defecto enruta a través de Vercel AI Gateway, un servicio de pago de Vercel, aunque también se pueden instalar proveedores directos (`@ai-sdk/openai`, etc.).

## ¿Cómo lo hace?

Paquetes npm (`npm i ai` más el proveedor elegido) para Node.js, edge runtimes y frameworks como Next.js, Nuxt o SvelteKit. Las claves van por variables de entorno: la de AI Gateway o la del proveedor directo. Si se usa el gateway, conviene revisar costes y privacidad porque añade un intermediario. La documentación está en ai-sdk.dev.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [assistant-ui](assistant-ui.md) | Componentes de chat en React con runtime oficial para AI SDK (documentado por assistant-ui). | Instala ai y el proveedor primero; luego @assistant-ui/react con su runtime de AI SDK. |
| [ui](ui.md) | shadcn/ui como base de componentes; AI Elements, el kit de componentes de chat de Vercel para AI SDK, se distribuye como registro de shadcn. | Inicializa shadcn/ui en el proyecto y añade después los componentes de AI Elements que necesites. |
| [langfuse](langfuse.md) | Trazas y costes de las llamadas del AI SDK mediante su telemetría OpenTelemetry (integración oficial de Langfuse). | Langfuse (cloud o autoalojado) primero; activa `experimental_telemetry` y el exportador de Langfuse. |
| [Ollama](ollama.md) | Modelos locales mediante el proveedor comunitario de Ollama, listado en la documentación del AI SDK. | Instala Ollama y descarga un modelo; luego añade el paquete del proveedor comunitario. |
| [mem0](mem0.md) | Memoria persistente de usuario mediante el proveedor de Mem0 para el AI SDK (integración documentada por Mem0). | Configura Mem0 (cloud o autoalojado) y envuelve el modelo con su proveedor. |

**Notas:** Alternativas (elige una): langgraphjs, mastra. Ojo: algunos ejemplos del README usan modelos vía AI Gateway que requieren cuenta de Vercel.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada @ai-sdk/vue@3.0.332 (2026-11-13) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/vercel/ai/blob/main/README.md) · [2](https://ai-sdk.dev/docs/ai-sdk-ui/overview) · [3](https://www.assistant-ui.com/docs/runtimes/ai-sdk) · [4](https://ai-sdk.dev/elements) · [5](https://docs.langfuse.com/integrations/frameworks/vercel-ai-sdk) · [6](https://ai-sdk.dev/providers/community-providers/ollama) · [7](https://docs.mem0.ai/integrations/vercel-ai-sdk)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El SDK no incluye modelos ni créditos; proveedores, AI Gateway y alojamiento tienen costes separados |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Compatibilidad por confirmar |
| Antigravity | Compatibilidad por confirmar |
| Modelos locales | Modelo local no documentado. El README ofrece una skill para Claude Code; instalarla no paga la inferencia de la aplicación |
| Coste | El coste depende del proveedor o la ruta. El SDK no incluye modelos ni créditos; proveedores, AI Gateway y alojamiento tienen costes separados |
| Equipo | Preparación según la ruta elegida. Node.js; proyecto TypeScript; paquete del proveedor |

El README ofrece una skill para Claude Code; instalarla no paga la inferencia de la aplicación

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- proyecto TypeScript
- paquete del proveedor

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
npm install ai
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/vercel/ai/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AI SDK (Vercel) para mi objetivo y necesito pasos guiados. Lee https://github.com/vercel/ai/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade una respuesta de chat en streaming y una herramienta de consulta de estado.

**Qué comprobar:** El texto llega por partes y la llamada devuelve el estado ficticio.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir una interfaz de chat
- Extraer datos tipados de un mensaje

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir una interfaz de chat; Extraer datos tipados de un mensaje | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README ofrece una skill para Claude Code; instalarla no paga la inferencia de la aplicación

## Stack y modelos

- **Stack:** Node.js; proyecto TypeScript; paquete del proveedor
- **Etiquetas:** `agents` `ui` `typescript` `react`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LangGraph.js](langgraphjs.md) | 3.4k | Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador. |
| [Mastra](mastra.md) | 29.5k | Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. |

## Enlaces

- 🐙 GitHub: [vercel/ai](https://github.com/vercel/ai)
- 🌐 Web: <https://ai-sdk.dev>
- 🧪 Receta: [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/vercel/ai/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
