[🏠 Inicio](../README.md) › [🏠 IA Local: Modelos, Chats & Workspaces](../categorias/08-ia-local-modelos-chats-workspaces.md) › NotebookLM: alternativas y clientes

# 🎙️ notebooklm-py

> API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 20.2k | MIT | Python | 2026-11-08 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Cubre el vacío de automatización que la interfaz web oficial no ofrece.

## Por qué destaca

Abre el NotebookLM real a la automatización, algo que la interfaz web oficial no permite, útil para procesar fuentes a escala. Se instala como un paquete pip y expone una API síncrona clara.

## Cómo funciona

Envuelve los endpoints internos de NotebookLM en una librería Python que sube fuentes y dispara síntesis usando tu sesión/credenciales de Google (no hay API pública oficial).

## Instalación rápida

`pip install` de la librería más configuración de credenciales de Google (cookies de sesión o auth no oficial).

## Casos de uso

- Subir 20 PDFs y pedir una síntesis temática
- Automatizar generación de notas de audio en lote
- Volcar fuentes a un notebook desde un pipeline

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| automatizas el NotebookLM real y aceptas el riesgo de API no oficial | quieres todo local (open-notebook) |

**Limitaciones:** Usa endpoints internos no oficiales de Google; puede romper ante cambios de la web y depende de credenciales de sesión válidas.

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** NotebookLM/Google (Gemini Pro/Ultra).
- **Etiquetas:** `notebooks` `research` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [notebooklm-mcp-cli](notebooklm-mcp-cli.md) | 6.5k | CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP. |

## Enlaces

- 🐙 GitHub: [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py)
- 🌐 Web: <https://github.com/teng-lin/notebooklm-py>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
