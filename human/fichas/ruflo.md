[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Asistentes autónomos y equipos de agentes

# 🐝 ruflo

> Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow).

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 81.4k | MIT | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Qué es

Orquesta swarms de agentes especializados a escala.

## Por qué destaca

Motor en Rust con embeddings, memoria persistente y plugins, orientado a coordinación masiva de agentes con seguridad de nivel enterprise. Es de nicho pero ambicioso y aprovecha el rendimiento de Rust para la orquestación.

## Cómo funciona

Un coordinador en Rust reparte trabajo entre agentes, comparte memoria federada (embeddings) y comunica equipos; se apoya en los CLIs de Claude Code y Codex como ejecutores.

## Instalación rápida

`cargo install` o build desde fuente con `git clone` (consulta el README). Requiere tener instalados los CLIs de agentes (Claude Code/Codex) y sus claves.

## Casos de uso

- Swarms de agentes especializados
- Memoria autoaprendida y comms entre equipos
- Paralelizar tareas de codificación a escala

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| orquestas muchos agentes a escala y quieres rendimiento | solo necesitas 1-2 agentes o no usas Claude Code/Codex |

**Limitaciones:** Setup pesado (Rust + CLIs de agentes) y caso de uso estrecho; no es una librería de uso general.

## Stack y modelos

- **Stack:** Rust
- **Modelos / API:** Claude Code, Codex (vía sus CLIs).
- **Etiquetas:** `automation` `agents` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mem0](mem0.md) | 68.7k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [ECC](ecc.md) | 300k | Sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura. |

## Enlaces

- 🐙 GitHub: [ruvnet/ruflo](https://github.com/ruvnet/ruflo)
- 🌐 Web: <https://cognitum.one>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
