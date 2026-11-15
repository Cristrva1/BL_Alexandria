[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Builders visuales y plataformas de agentes

# 🧩 Sim

> Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.1k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

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

Diseña agentes conectando bloques en un canvas, prueba en vivo y despliega como API o chat. Open source y auto-hospedable.

## Por qué destaca

Interfaz moderna y rápida, con colaboración en tiempo real y muchas integraciones.

## Cómo funciona

Un editor Next.js guarda los workflows y un ejecutor corre cada bloque (LLM, herramientas, lógica) con trazas.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/simstudioai/sim/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Sim para mi objetivo y necesito pasos guiados. Lee https://github.com/simstudioai/sim/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Agentes de soporte con herramientas
- Workflows de IA desplegados como API
- Prototipos colaborativos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un constructor visual de agentes moderno y abierto | prefieres automatización general con cientos de apps; mira `n8n` |

## Stack y modelos

- **Stack:** TypeScript, Next.js, PostgreSQL
- **Etiquetas:** `agents` `automation` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Flowise](flowise.md) | 55.6k | Constructor visual para diseñar aplicaciones de IA conectando modelos, herramientas, memoria y fuentes de datos. |
| [langflow](langflow.md) | 157k | Constructor visual de flujos LLM/agentes construido sobre LangChain. |
| [dify](dify.md) | 161k | Plataforma integral para construir apps de IA con backend y UI listos. |
| [AutoGPT](autogpt.md) | 188k | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. |

## Enlaces

- 🐙 GitHub: [simstudioai/sim](https://github.com/simstudioai/sim)
- 🌐 Web: <https://www.sim.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/simstudioai/sim/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
