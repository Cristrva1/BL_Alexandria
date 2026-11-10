[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de código (terminal e IDE)

# 🙌 OpenHands

> Plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin).

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 93.1k | MIT | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

El agente puede leer y editar código, correr comandos y navegar la web dentro de un sandbox.

## Por qué destaca

Uno de los proyectos open-source de agentes de programación más populares, con foco en acciones reales en lugar de solo respuestas. Soporta varios runtimes (local, remoto, cloud) y agentes compatibles con ACP.

## Cómo funciona

Un bucle agente-acción-observación ejecuta tareas dentro de un contenedor Docker aislado; backend en Python con UI web, y el agente opera sobre el filesystem, shell y navegador del sandbox.

## Instalación rápida

`docker run` de la imagen oficial (o `pip install openhands-ai` para el modo CLI). Requiere Docker y una clave de proveedor de LLM.

## Casos de uso

- Agente que edita código, corre comandos y navega
- Automatizar tareas dev
- Resolver issues end-to-end en un repo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un agente que "haga", no solo hable | solo necesitas chat/RAG o no puedes correr Docker |

**Limitaciones:** El sandbox Docker consume recursos y la ejecución de código arbitrario exige cuidar el aislamiento.

## Stack y modelos

- **Stack:** Python/TS, Docker
- **Modelos / API:** OpenAI, Anthropic, Gemini, locales; agnóstico vía variables de entorno.
- **Etiquetas:** `agents` `automation` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ECC](ecc.md) | 300k | Sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura. |
| [sandbox](sandbox.md) | 6.3k | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open SWE](open-swe.md) | 11.2k | Agente de código asíncrono de LangChain para montar tu propio agente interno de ingeniería. |
| [SWE-agent](swe-agent.md) | 20.8k | Agente de Princeton y Stanford que toma un issue de GitHub e intenta resolverlo solo. |

## Enlaces

- 🐙 GitHub: [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 🌐 Web: <https://openhands.dev>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
