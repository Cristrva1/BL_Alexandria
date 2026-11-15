[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 annas-mcp

> Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's Archive y sus espejos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.1k | — | Go | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta. |
| Coste | El coste depende del proveedor o la ruta. El proyecto documenta requisitos de acceso a la API de Anna's Archive; no asumir acceso ilimitado por conectar un cliente MCP. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

Puede conectarse a un cliente con soporte MCP, incluido Claude Code o Codex. Debes configurar el servidor y sus permisos.

## Qué puedes hacer con él

Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's Archive y sus espejos. Expone búsquedas y descargas como herramientas MCP y permite seleccionar espejos disponibles.

## Por qué destaca

Necesitas integrar búsquedas de documentos en un cliente MCP.

## Cómo funciona

Expone búsquedas y descargas como herramientas MCP y permite seleccionar espejos disponibles.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible.
- Las credenciales del servicio conectado, si las pide el servidor.

1. Instala o configura el servidor según su README.
2. Añade su comando o URL en la configuración MCP de tu cliente.
3. Comprueba que aparecen las herramientas antes de asignar una tarea.

[Instrucciones originales de instalación](https://github.com/iosifache/annas-mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar annas-mcp para mi objetivo y necesito pasos guiados. Lee https://github.com/iosifache/annas-mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Necesitas integrar búsquedas de documentos en un cliente MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas integrar búsquedas de documentos en un cliente MCP | una conexión directa cubre el caso sin añadir infraestructura |

**Limitaciones:** La disponibilidad depende de los espejos y los derechos de acceso de cada documento.

## Stack y modelos

- **Stack:** Go, Go modules
- **Etiquetas:** `servidores` `annas-archive` `cli` `mcp-server` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [markitdown](markitdown.md) | 195k | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. |

## Enlaces

- 🐙 GitHub: [iosifache/annas-mcp](https://github.com/iosifache/annas-mcp)
- 🌐 Web: <https://annas-archive.gl>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/iosifache/annas-mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
