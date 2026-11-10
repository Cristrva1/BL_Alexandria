[🏠 Inicio](../README.md) › [🏠 IA Local: Modelos, Chats & Workspaces](../categorias/08-ia-local-modelos-chats-workspaces.md) › NotebookLM: alternativas y clientes

# 🎚️ notebooklm-mcp-cli

> CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 6.5k | MIT | Python | 2026-11-08 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Qué es

Convierte NotebookLM en una herramienta invocable por asistentes.

## Por qué destaca

Expone NotebookLM como herramienta MCP, permitiendo que asistentes como Claude lo usen como un servicio más dentro de sus flujos. Cubre el mismo caso que la API Python pero pensado para integración con agentes.

## Cómo funciona

Levanta un servidor MCP en Python que traduce las llamadas del cliente a operaciones de NotebookLM (crear, actualizar y consultar notebooks) usando tus credenciales de Google.

## Instalación rápida

`pip install` o `git clone` y registro del servidor MCP en tu cliente (Claude Desktop, etc.). Requiere credenciales de Google válidas.

## Casos de uso

- Crear/actualizar notebooks en la nube desde MCP
- Flujos repetibles de audio desde un asistente
- Volcar fuentes desde otro agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| integras NotebookLM con tu asistente MCP | prefieres la API directa en scripts (notebooklm-py) |

**Limitaciones:** Depende de credenciales de Google y de endpoints internos no oficiales; puede romper ante cambios de NotebookLM.

## Stack y modelos

- **Stack:** Python, MCP
- **Modelos / API:** NotebookLM/Google.
- **Etiquetas:** `mcp` `notebooks` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [notebooklm-py](notebooklm-py.md) | 20.2k | API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código. |
| [awesome-mcp-servers](awesome-mcp-servers.md) | 97.6k | Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. |

## Enlaces

- 🐙 GitHub: [jacob-bd/gemini-notebook-mcp-cli](https://github.com/jacob-bd/gemini-notebook-mcp-cli)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
