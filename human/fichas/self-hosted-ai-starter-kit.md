[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Ecosistema n8n

# 🔁 Self-hosted AI Starter Kit

> Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 15.3k | Apache-2.0 | — | 2026-10-12 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Kit oficial de n8n que levanta un entorno de IA privado: n8n para orquestar, Ollama para modelos, Qdrant como base vectorial y PostgreSQL. Útil para prototipar agentes y RAG sin enviar datos fuera.

## Por qué destaca

Mantenido por el equipo de n8n; resuelve en un comando el cableado entre las piezas.

## Cómo funciona

Un `docker-compose.yml` con perfiles para CPU y GPU arranca los servicios ya conectados entre sí.

## Instalación rápida

`git clone https://github.com/n8n-io/self-hosted-ai-starter-kit` y `docker compose --profile cpu up` (o `gpu-nvidia`).

## Casos de uso

- Chat con tus documentos en local
- Agentes de n8n con modelos privados
- Demo de IA sin nube

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un stack de IA local funcionando hoy con n8n | vas a producción con alta carga; arma tu propio despliegue |

**Limitaciones:** Es un punto de partida, no un despliegue endurecido para producción.

## Stack y modelos

- **Stack:** Docker Compose, n8n, Ollama, Qdrant, PostgreSQL
- **Modelos / API:** Modelos locales vía Ollama (Llama, Qwen, etc.).
- **Etiquetas:** `automation` `local` `rag` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [Qdrant](qdrant.md) | 35.5k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |

## Enlaces

- 🐙 GitHub: [n8n-io/self-hosted-ai-starter-kit](https://github.com/n8n-io/self-hosted-ai-starter-kit)
- 🌐 Web: <https://n8n.io>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
