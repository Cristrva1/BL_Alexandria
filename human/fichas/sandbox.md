[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 📦 sandbox

> Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.3k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve el riesgo de dejar que un agente toque tu host: todo corre contenido en un contenedor reproducible.

## Por qué destaca

Concentra en un solo contenedor todas las herramientas que un agente necesita, ofreciendo un entorno reproducible y aislado poco común. Su exposición vía web y MCP lo hace accesible desde cualquier cliente compatible sin configurar cada pieza por separado.

## Cómo funciona

Levanta un contenedor con los servicios (browser, shell, editor, notebooks) expuestos vía web y conectables por clientes MCP, aislando la ejecución del host y limitando el alcance de las acciones del agente.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/agent-infra/sandbox/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar sandbox para mi objetivo y necesito pasos guiados. Lee https://github.com/agent-infra/sandbox/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Ejecutar agentes de forma aislada
- Entorno reproducible para tareas dev
- Probar agentes que manipulan archivos/terminal sin riesgo al host

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres aislar la ejecución de agentes y reproducibilidad | te basta correr local sin sandbox o no puedes asumir el overhead de Docker |

## Stack y modelos

- **Stack:** Docker, web, MCP
- **Etiquetas:** `agents` `automation` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenHands](openhands.md) | 93.5k | Plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). |
| [ECC](ecc.md) | 303k | Colección de plugins, skills, hooks y convenciones para organizar el trabajo de agentes de código en un proyecto. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [NemoClaw](nemoclaw.md) | 23k | Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. |
| [E2B](e2b.md) | 14.9k | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. |

## Enlaces

- 🐙 GitHub: [agent-infra/sandbox](https://github.com/agent-infra/sandbox)
- 🌐 Web: <https://sandbox.agent-infra.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/agent-infra/sandbox/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
