[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🧩 GhidraMCP

> Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.9k | Apache-2.0 | Java | 2026-11-14 |

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

Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios.

## Cómo funciona

Un cliente MCP invoca las herramientas del servidor para trabajar con el programa o servicio conectado.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible y el programa o servicio que va a controlar la herramienta.

1. Prepara el servidor y sus dependencias siguiendo la configuración del README.
2. Añade el comando o la URL en el cliente MCP y configura los permisos y credenciales de los servicios conectados.
3. Comprueba que aparecen sus herramientas y prueba una consulta pequeña antes de permitir modificaciones.

[Instrucciones originales de instalación](https://github.com/LaurieWired/GhidraMCP/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GhidraMCP para mi objetivo y necesito pasos guiados. Lee https://github.com/LaurieWired/GhidraMCP/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| buscas esta función: Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios. | necesitas un producto autónomo y esta pieza requiere un anfitrión compatible |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Java, pyproject.toml
- **Etiquetas:** `servidores` `mcp` `java`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ghidra](ghidra.md) | 100k | Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria. |

## Enlaces

- 🐙 GitHub: [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/LaurieWired/GhidraMCP/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
