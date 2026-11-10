[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 Trigger.dev

> Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 16.7k | Apache-2.0 | TypeScript | 2026-11-03 | 🆕 Aún no (sugerido) |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Escribe tareas largas o con reintentos en TypeScript dentro de tu app y Trigger.dev las ejecuta, reintenta y monitorea. Ideal para equipos de producto con Next.js o Node que no quieren operar colas.

## Por qué destaca

Experiencia de desarrollo muy cuidada: código normal, sin timeouts y con observabilidad incluida.

## Cómo funciona

Despliegas tus tareas a su runtime (cloud o self-host), que las ejecuta con checkpoints, colas, concurrencia y reintentos.

## Instalación rápida

`npx trigger.dev@latest init` dentro de tu proyecto; se usa con su cloud o en self-host con Docker.

## Casos de uso

- Generar PDFs o videos en segundo plano
- Agentes de IA con pasos largos
- Webhooks con reintentos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu app es TypeScript y necesitas tareas largas confiables sin montar colas | quieres un editor visual para no programadores; mira `n8n` |

## Stack y modelos

- **Stack:** TypeScript, Node.js, PostgreSQL, Docker
- **Modelos / API:** Agnóstico: se integra con el AI SDK de Vercel y cualquier API.
- **Etiquetas:** `automation` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AI SDK (Vercel)](vercel-ai.md) | 27.9k | Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. |
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Windmill](windmill.md) | 18.5k | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. |
| [Kestra](kestra.md) | 30.2k | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. |

## Enlaces

- 🐙 GitHub: [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev)
- 🌐 Web: <https://trigger.dev/changelog>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
