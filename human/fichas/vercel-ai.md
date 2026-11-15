[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks en TypeScript y multi-lenguaje

# 🟦 AI SDK (Vercel)

> Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Unifica la llamada a decenas de proveedores con una API común y trae hooks de React para chat con streaming. Es la base de muchos frameworks de agentes en TS.

## Por qué destaca

API de proveedores unificada y hooks de UI muy usados; mantenida por Vercel.

## Cómo funciona

Funciones como generateText y streamText llaman al proveedor elegido; los hooks useChat conectan el streaming con la UI.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
npm install ai
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/vercel/ai/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AI SDK (Vercel) para mi objetivo y necesito pasos guiados. Lee https://github.com/vercel/ai/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Chat con streaming en Next.js
- Llamadas a herramientas tipadas
- Cambiar de proveedor sin reescribir

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| construyes una app web con IA en TypeScript | necesitas agentes complejos con memoria y workflows; mira `mastra` |

## Stack y modelos

- **Stack:** TypeScript, React, Next.js
- **Etiquetas:** `agents` `ui` `typescript` `react`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ui](ui.md) | 128k | Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada. |
| [assistant-ui](assistant-ui.md) | 13.2k | Librería React y TypeScript para interfaces de chat con IA de calidad producción. |

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

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/vercel/ai/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
