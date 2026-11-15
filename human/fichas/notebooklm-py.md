[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › NotebookLM: alternativas y clientes

# 🎙️ notebooklm-py

> API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 20.2k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta documentada usa un servicio en línea mediante sesión o acceso propio; no implica ejecución local del modelo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Cliente no oficial que reutiliza una sesión de Google/NotebookLM. No es un modelo local ni una API oficial incluida por Claude o Codex. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Cubre el vacío de automatización que la interfaz web oficial no ofrece.

## Por qué destaca

Abre el NotebookLM real a la automatización, algo que la interfaz web oficial no permite, útil para procesar fuentes a escala. Se instala como un paquete pip y expone una API síncrona clara.

## Cómo funciona

Envuelve los endpoints internos de NotebookLM en una librería Python que sube fuentes y dispara síntesis usando tu sesión/credenciales de Google (no hay API pública oficial).

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/teng-lin/notebooklm-py/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar notebooklm-py para mi objetivo y necesito pasos guiados. Lee https://github.com/teng-lin/notebooklm-py/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `notebooks` `research` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [notebooklm-mcp-cli](notebooklm-mcp-cli.md) | 6.5k | CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP. |

## Enlaces

- 🐙 GitHub: [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py)
- 🌐 Web: <https://github.com/teng-lin/notebooklm-py>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/teng-lin/notebooklm-py/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
