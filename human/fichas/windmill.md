[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 Windmill

> Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 18.5k | Otra (ver repo) | Rust | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Convierte scripts de Python, TypeScript, Go o SQL en workflows, endpoints y apps con UI generada. Sirve a equipos técnicos que quieren la flexibilidad del código con la comodidad de un orquestador visual.

## Por qué destaca

Orquestador muy rápido escrito en Rust, con editor visual y versionado en Git; compite con Airflow y Temporal sin su complejidad.

## Cómo funciona

Cada script se ejecuta en workers aislados; los flujos encadenan scripts como pasos y guardan estado en PostgreSQL.

## Instalación rápida

`docker compose up -d` con el `docker-compose.yml` del repo (incluye PostgreSQL); abre `http://localhost`.

## Casos de uso

- Jobs programados que antes vivían en cron
- Paneles internos sobre scripts existentes
- Agentes de IA con pasos auditables

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu equipo programa y quiere workflows versionados en código | prefieres arrastrar nodos sin escribir código; mira `n8n` |

**Limitaciones:** Algunas funciones empresariales (SSO, auditoría) son de pago.

## Stack y modelos

- **Stack:** Rust, TypeScript, Svelte, PostgreSQL, Docker
- **Modelos / API:** Agnóstico: llama a OpenAI, Anthropic u otros desde tus scripts.
- **Etiquetas:** `automation` `agents` `rust` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [Kestra](kestra.md) | 30.2k | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. |
| [Trigger.dev](trigger-dev.md) | 16.7k | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. |

## Enlaces

- 🐙 GitHub: [windmill-labs/windmill](https://github.com/windmill-labs/windmill)
- 🌐 Web: <https://windmill.dev>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
