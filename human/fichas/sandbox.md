[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Infraestructura: sandboxes, herramientas y protocolos

# 📦 sandbox

> Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 6.3k | Apache-2.0 | Python | 2026-09-14 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

## Qué es

Resuelve el riesgo de dejar que un agente toque tu host: todo corre contenido en un contenedor reproducible.

## Por qué destaca

Concentra en un solo contenedor todas las herramientas que un agente necesita, ofreciendo un entorno reproducible y aislado poco común. Su exposición vía web y MCP lo hace accesible desde cualquier cliente compatible sin configurar cada pieza por separado.

## Cómo funciona

Levanta un contenedor con los servicios (browser, shell, editor, notebooks) expuestos vía web y conectables por clientes MCP, aislando la ejecución del host y limitando el alcance de las acciones del agente.

## Instalación rápida

`docker run` de la imagen del proyecto; requiere Docker y recursos suficientes para correr navegador + servicios en paralelo.

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
- **Modelos / API:** Clientes MCP; sin LLM propio.
- **Etiquetas:** `agents` `automation` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenHands](openhands.md) | 93.1k | Plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). |
| [ECC](ecc.md) | 300k | Sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [NemoClaw](nemoclaw.md) | 23k | Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. |
| [E2B](e2b.md) | 14.8k | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. |

## Enlaces

- 🐙 GitHub: [agent-infra/sandbox](https://github.com/agent-infra/sandbox)
- 🌐 Web: <https://sandbox.agent-infra.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
