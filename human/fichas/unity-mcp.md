[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🧩 unity-mcp

> Servidor MCP que permite a un asistente operar escenas, scripts y recursos dentro de un proyecto del editor Unity.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16k | MIT | C# | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El servidor aporta herramientas a un cliente MCP; el cliente aporta el modelo. Revisar los servicios que usa cada herramienta. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Consumo del agente que ya utilizas. El modelo se consume en el cliente MCP. Programas, licencias y servicios conectados pueden tener requisitos y tarifas independientes. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Configura este servidor en un cliente MCP compatible, incluido Claude Code o Codex. Sus servicios y permisos se preparan aparte.

## Qué puedes hacer con él

Servidor MCP que permite a un asistente operar escenas, scripts y recursos dentro de un proyecto del editor Unity.

## Cómo funciona

Un cliente MCP invoca las herramientas del servidor para trabajar con el programa o servicio conectado.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible y el programa o servicio que va a controlar la herramienta.

1. Prepara un proyecto de prueba en Unity y la extensión y servidor que documenta el README.
2. Configura el servidor en tu cliente MCP y comprueba que aparecen sus herramientas.
3. Pide primero una consulta de la escena y después un cambio pequeño sobre una copia del proyecto.

[Instrucciones originales de instalación](https://github.com/CoplayDev/unity-mcp/blob/beta/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar unity-mcp para mi objetivo y necesito pasos guiados. Lee https://github.com/CoplayDev/unity-mcp/blob/beta/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Servidor MCP que permite a un asistente operar escenas, scripts y recursos dentro de un proyecto del editor Unity.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| buscas esta función: Servidor MCP que permite a un asistente operar escenas, scripts y recursos dentro de un proyecto del editor Unity. | necesitas un producto autónomo y esta pieza requiere un anfitrión compatible |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** C#, docker-compose.yml
- **Etiquetas:** `servidores` `mcp` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [blender](blender.md) | 22k | Código de Blender, la aplicación para modelar, animar, renderizar y editar escenas y contenido tridimensional. |

## Enlaces

- 🐙 GitHub: [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp)
- 🌐 Web: <https://coplaydev.github.io/unity-mcp/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/CoplayDev/unity-mcp/blob/beta/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
