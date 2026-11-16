[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › UI generada con IA y frontends para agentes

# 🪄 OpenUI

> Estándar abierto de Thesys para UI generativa: el LLM responde con interfaces, no solo texto.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.2k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de UI generativa (MIT) de Thesys, construido en torno a OpenUI Lang, un lenguaje compacto y pensado para streaming. Es activo (@openuidev/server@0.4.3) y reciente. El README avisa de que no existe ninguna criptomoneda oficial con su nombre.

## ¿Qué hace?

Permite que el modelo responda con interfaces en lugar de solo texto: defines componentes, se generan los prompts y el modelo emite OpenUI Lang, que se renderiza progresivamente. Tiene runtimes oficiales para React, Vue, Svelte y Angular, componentes de chat, integración con agentes de LangChain/LangGraph y observabilidad, opcionalmente en la nube de Thesys.

## ¿Cómo lo hace?

Paquetes npm (`@openuidev/react-lang`, `@openuidev/react-ui`, `@openuidev/lang-core`, `@openuidev/langchain`…) y una CLI para crear un proyecto (`npx @openuidev/cli@latest create`). Funciona con cualquier proveedor de modelos a través del servidor.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph](langgraph.md) | Agentes LangGraph que emiten UI con el paquete `@openuidev/langchain`. | Instala `@openuidev/langchain @langchain/langgraph` y conecta el agente. |
| [langchain](langchain.md) | Integración oficial para agentes y servidores LangChain. | Usa el mismo paquete de integración. |
| [CopilotKit](copilotkit.md) | Combinación anterior del catálogo: frontend de agentes. (combinación por arquitectura) (OpenUI y AG-UI/A2UI son enfoques distintos de UI generativa) | Evalúa si necesitas ambos; normalmente se elige uno. |

**Notas:** Sin alternativas declaradas; enfoques comparables: json-render, copilotkit (A2UI).

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada @openuidev/server@0.4.3 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/thesysdev/openui/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El framework y la skill no incluyen llamadas de modelo; proveedor y backend tienen costes separados |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. La skill sirve para construir y depurar; su portabilidad no implica que la app use la suscripción del agente para inferencia |
| Coste | El coste depende del proveedor o la ruta. El framework y la skill no incluyen llamadas de modelo; proveedor y backend tienen costes separados |
| Equipo | Preparación según la ruta elegida. Node; framework elegido; backend y modelo; catálogo de componentes |

La skill sirve para construir y depurar; su portabilidad no implica que la app use la suscripción del agente para inferencia

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- framework elegido
- backend y modelo
- catálogo de componentes

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx @openuidev/cli@latest create --name genui-chat-app
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/thesysdev/openui/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenUI para mi objetivo y necesito pasos guiados. Lee https://github.com/thesysdev/openui/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Define una tarjeta permitida y pide al modelo una respuesta que la utilice.

**Qué comprobar:** El renderer muestra solo componentes del catálogo esperado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear respuestas de chat con interfaz
- Construir formularios generados y acotados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear respuestas de chat con interfaz; Construir formularios generados y acotados | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La skill sirve para construir y depurar; su portabilidad no implica que la app use la suscripción del agente para inferencia

## Stack y modelos

- **Stack:** Node; framework elegido; backend y modelo; catálogo de componentes
- **Etiquetas:** `ui` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [thesysdev/openui](https://github.com/thesysdev/openui)
- 🌐 Web: <https://www.openui.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/thesysdev/openui/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
