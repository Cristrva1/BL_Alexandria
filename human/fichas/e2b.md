[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🛠️ E2B

> Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 14.8k | Apache-2.0 | Python | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** ☁️ cloud/API · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Qué es

Arranca microVMs aisladas en milisegundos donde el agente puede ejecutar código, instalar paquetes o usar un escritorio. Muy usado para intérpretes de código y agentes de datos.

## Por qué destaca

Aislamiento real con Firecracker y SDKs simples; estándar en agentes que ejecutan código.

## Cómo funciona

Cada sandbox es una microVM Firecracker controlada por SDK; el agente envía código y recibe la salida.

## Instalación rápida

`pip install e2b-code-interpreter` o `npm i @e2b/code-interpreter` con tu clave de API.

## Casos de uso

- Intérprete de código para un chatbot
- Agentes de análisis de datos
- Ejecutar código generado sin riesgo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente ejecuta código y necesitas aislarlo | solo necesitas ejecutar código localmente de confianza |

**Limitaciones:** El servicio gestionado es de pago por uso; el self-host es más complejo.

## Stack y modelos

- **Stack:** Python, TypeScript, Firecracker
- **Modelos / API:** Agnóstico.
- **Etiquetas:** `agents` `security` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [smolagents](smolagents.md) | 30.3k | Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. |
| [Open SWE](open-swe.md) | 11.2k | Agente de código asíncrono de LangChain para montar tu propio agente interno de ingeniería. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [sandbox](sandbox.md) | 6.3k | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |

## Enlaces

- 🐙 GitHub: [e2b-dev/E2B](https://github.com/e2b-dev/E2B)
- 🌐 Web: <https://docs.e2b.dev/?utm_source=github&utm_medium=referral&utm_campaign=repo_website&utm_content=e2b>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
