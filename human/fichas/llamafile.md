[🏠 Inicio](../README.md) › [🏠 IA Local: Modelos, Chats & Workspaces](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🦙 llamafile

> Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 26.6k | Otra (ver repo) | C++ | 2026-11-09 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Qué es

Empaqueta modelo y motor en un ejecutable que funciona en Windows, macOS y Linux sin instalar nada. Proyecto de Mozilla.

## Por qué destaca

Portabilidad extrema: un archivo y listo.

## Cómo funciona

Combina llama.cpp con Cosmopolitan Libc para crear binarios multiplataforma con el modelo embebido.

## Instalación rápida

Descarga un `.llamafile`, dale permiso de ejecución y ábrelo.

## Casos de uso

- Llevar un modelo en una memoria USB
- Demos sin instalación
- IA local en equipos sin permisos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres repartir un modelo que funcione con doble clic | vas a cambiar de modelos a menudo; mira `ollama` |

## Stack y modelos

- **Stack:** C++, Cosmopolitan
- **Modelos / API:** Modelos abiertos.
- **Etiquetas:** `inference` `local` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [llama.cpp](llama-cpp.md) | 134k | Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. |

## Enlaces

- 🐙 GitHub: [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile)
- 🌐 Web: <https://docs.mozilla.ai/llamafile>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
