[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › UI generada con IA y frontends para agentes

# 🪄 assistant-ui

> Librería React y TypeScript para interfaces de chat con IA de calidad producción.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.2k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca open source TypeScript/React (MIT) para construir experiencias de chat con IA de calidad de producción. Es activa (assistant-ui@0.0.135, aún 0.x). Tiene un servicio opcional de pago, Assistant Cloud, para persistencia de hilos, telemetría y archivos.

## ¿Qué hace?

Ofrece primitivas componibles (`Thread`, `Message`, `Composer`, `ThreadList`, `ActionBar`…) para construir cualquier interfaz de chat con streaming, adjuntos, edición, ramas, renderizado de herramientas y accesibilidad. Incluye runtimes para Vercel AI SDK, LangGraph, LangChain, data streams y backends propios. Mastra figura entre sus integraciones destacadas.

## ¿Cómo lo hace?

Una CLI genera un proyecto Next.js o añade componentes con estilo a uno existente (`npx assistant-ui@latest create` o `init`). También se puede instalar directamente con `npm install @assistant-ui/react @assistant-ui/ai-sdk ai`. `useChatRuntime` conecta con el AI SDK por defecto.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [AI SDK (Vercel)](vercel-ai.md) | Runtime por defecto (`@assistant-ui/ai-sdk`, `useChatRuntime`). | Instala `ai` y el proveedor; después el runtime de assistant-ui. |
| [LangGraph](langgraph.md) | Runtime oficial `@assistant-ui/react-langgraph`. | Despliega el grafo y usa `useLangGraphRuntime`. |
| [ui](ui.md) | Los componentes con estilo que añade la CLI siguen el patrón de shadcn/ui. (combinación por arquitectura) | Inicializa shadcn/ui o deja que la CLI configure el proyecto. |

**Notas:** Alternativas (elige una): copilotkit.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada assistant-ui@0.0.135 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/assistant-ui/assistant-ui/blob/main/README.md) · [2](https://www.assistant-ui.com/docs/runtimes/ai-sdk) · [3](https://www.assistant-ui.com/docs/runtimes/langgraph)</sub>

## Ver similares

Grupo **Componentes de chat y copilotos para React**: assistant-ui ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [CopilotKit](copilotkit.md) ⭐ recomendado | 69 | Si buscas esto: stack frontend para agentes y UI generativa en React, creadores del protocolo AG-UI. |
| 2 | **assistant-ui** (esta ficha) | 62 | Si buscas esto: librería React y TypeScript para interfaces de chat con IA de calidad producción. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Los componentes no incluyen modelo; admite proveedores como Ollama además de APIs y servicios de pago |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es la interfaz del chat; necesitas configurar el backend y no basta con instalar el paquete React |
| Coste | El coste depende del proveedor o la ruta. Los componentes no incluyen modelo; admite proveedores como Ollama además de APIs y servicios de pago |
| Equipo | Preparación según la ruta elegida. React y TypeScript; Node; runtime y proveedor |

Es la interfaz del chat; necesitas configurar el backend y no basta con instalar el paquete React

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- React y TypeScript
- Node
- runtime y proveedor

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx assistant-ui@latest create   # new project
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/assistant-ui/assistant-ui/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar assistant-ui para mi objetivo y necesito pasos guiados. Lee https://github.com/assistant-ui/assistant-ui/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca un chat mínimo y prueba estados de envío, streaming y error con un backend de prueba.

**Qué comprobar:** Los mensajes y estados de la interfaz corresponden a la respuesta del backend.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir un chat para una app
- Añadir herramientas y adjuntos a una conversación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir un chat para una app; Añadir herramientas y adjuntos a una conversación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es la interfaz del chat; necesitas configurar el backend y no basta con instalar el paquete React

## Stack y modelos

- **Stack:** React y TypeScript; Node; runtime y proveedor
- **Etiquetas:** `ui` `chatbot` `react` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [CopilotKit](copilotkit.md) | 38.7k | Stack frontend para agentes y UI generativa en React, creadores del protocolo AG-UI. |

## Enlaces

- 🐙 GitHub: [assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui)
- 🌐 Web: <https://www.assistant-ui.com>
- 🧪 Receta: [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/assistant-ui/assistant-ui/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
