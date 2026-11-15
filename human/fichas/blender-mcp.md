[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Blender MCP

> Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 34.5k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta. |
| Coste | El coste depende del proveedor o la ruta. Controlar Blender y generar modelos en servicios externos son rutas distintas: los proveedores de generación pueden cobrar. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

Puede conectarse a un cliente con soporte MCP, incluido Claude Code o Codex. Debes configurar el servidor y sus permisos.

## Qué puedes hacer con él

Crea y modifica escenas, objetos y materiales hablando con tu asistente. Útil para prototipos 3D rápidos.

## Por qué destaca

Lleva el modelado 3D a la conversación con un agente; muy popular entre creadores.

## Cómo funciona

Un addon de Blender abre un socket y un servidor MCP traduce las herramientas del agente en comandos de Blender.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible.
- Las credenciales del servicio conectado, si las pide el servidor.

1. Instala o configura el servidor según su README.
2. Añade su comando o URL en la configuración MCP de tu cliente.
3. Comprueba que aparecen las herramientas antes de asignar una tarea.

**Comando de entrada documentado:**

```shell
uvx blender-mcp
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/ahujasid/mcp-for-blender/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Blender MCP para mi objetivo y necesito pasos guiados. Lee https://github.com/ahujasid/mcp-for-blender/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Prototipar escenas 3D por chat
- Automatizar tareas repetitivas en Blender
- Generar assets simples

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres manejar Blender con tu agente | no trabajas en 3D |

**Limitaciones:** No es oficial de la Blender Foundation; puede ejecutar código arbitrario en Blender.

## Stack y modelos

- **Stack:** Python, Blender
- **Etiquetas:** `mcp` `design` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Enlaces

- 🐙 GitHub: [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender)
- 🌐 Web: <https://www.mcp-for-blender.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/ahujasid/mcp-for-blender/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
