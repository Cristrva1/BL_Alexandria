[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › NotebookLM: alternativas y clientes

# 🎚️ notebooklm-mcp-cli

> CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.5k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta documentada usa un servicio en línea mediante sesión o acceso propio; no implica ejecución local del modelo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Conecta un cliente MCP con una sesión de NotebookLM. El acceso y los límites los determina Google, además del agente que invoque las herramientas. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Convierte NotebookLM en una herramienta invocable por asistentes.

## Por qué destaca

Expone NotebookLM como herramienta MCP, permitiendo que asistentes como Claude lo usen como un servicio más dentro de sus flujos. Cubre el mismo caso que la API Python pero pensado para integración con agentes.

## Cómo funciona

Levanta un servidor MCP en Python que traduce las llamadas del cliente a operaciones de NotebookLM (crear, actualizar y consultar notebooks) usando tus credenciales de Google.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar notebooklm-mcp-cli para mi objetivo y necesito pasos guiados. Lee https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `mcp` `notebooks` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [notebooklm-py](notebooklm-py.md) | 20.2k | API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código. |
| [awesome-mcp-servers](awesome-mcp-servers.md) | 97.7k | Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. |

## Enlaces

- 🐙 GitHub: [jacob-bd/gemini-notebook-mcp-cli](https://github.com/jacob-bd/gemini-notebook-mcp-cli)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
