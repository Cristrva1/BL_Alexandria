[🏠 Inicio](../README.md) › [🧬 Memoria, RAG & LLM Ops](../categorias/06-memoria-rag-llm-ops.md) › Ahorro de contexto y tokens

# 🧬 rtk

> Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 86.6k | Apache-2.0 | Rust | 2026-11-14 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Qué es

Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. Resume resultados de pruebas, diffs y logs antes de entregarlos al agente y registra el ahorro observado.

## Por qué destaca

Tu agente consume demasiado contexto leyendo salidas extensas de terminal.

## Cómo funciona

Resume resultados de pruebas, diffs y logs antes de entregarlos al agente y registra el ahorro observado.

## Instalación rápida

Clona `git clone https://github.com/rtk-ai/rtk.git` y sigue la instalación del [README original](https://github.com/rtk-ai/rtk/blob/develop/README.md). Las dependencias se configuran por proyecto.

## Casos de uso

- Tu agente consume demasiado contexto leyendo salidas extensas de terminal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente consume demasiado contexto leyendo salidas extensas de terminal | el coste operativo supera el volumen de uso del proyecto |

**Limitaciones:** La compresión puede omitir detalles; el porcentaje de ahorro depende del flujo real.

## Stack y modelos

- **Stack:** Rust, Cargo
- **Modelos / API:** Configurar el proveedor o entorno indicado en el README; esta revisión no ejecutó el proyecto.
- **Etiquetas:** `tokens` `agentic-coding` `ai-coding` `anthropic` `claude-code` `cli` `command-line-tool` `cost-reduction`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [headroom](headroom.md) | 79.7k | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. |

## Enlaces

- 🐙 GitHub: [rtk-ai/rtk](https://github.com/rtk-ai/rtk)
- 🌐 Web: <https://www.rtk-ai.app>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
