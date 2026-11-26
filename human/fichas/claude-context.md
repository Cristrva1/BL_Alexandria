[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🧩 Claude Context

> Permite que asistentes busquen funciones y conceptos por significado en una base de código a través de un conector MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.7k | MIT | TypeScript | 2026-11-22 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP); requiere clave de API

**Puntuación de calidad** 48/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Permite que asistentes busquen funciones y conceptos por significado en una base de código a través de un conector MCP.

## ¿Qué hace?

Permite que asistentes busquen funciones y conceptos por significado en una base de código a través de un conector MCP.

## ¿Cómo lo hace?

Fragmenta e indexa el código en una base vectorial para recuperar resultados por similitud.

Estado en GitHub: activo · último push 2026-11-12 · licencia declarada MIT (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zilliztech/claude-context/blob/64a87f9b31b0c983f731c91242322562ffd91c7d/README.md) · [2](https://github.com/zilliztech/claude-context/blob/master/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. El arranque revisado configura una clave de OpenAI para embeddings y una base Milvus o Zilliz. No se afirmó otra ruta en la ficha. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | El coste depende del proveedor o la ruta. La indexación consume embeddings y almacenamiento; no los cubre el plan del agente. |
| Equipo | Equipo normal; revisar dependencias. Node.js 20+, un cliente MCP, base vectorial y una configuración de embeddings según el proveedor escogido. |

Configura este servidor en un cliente MCP compatible, incluido Claude Code o Codex. Sus servicios y permisos se preparan aparte.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js 20+, un cliente MCP, base vectorial y una configuración de embeddings según el proveedor escogido.

1. Según Quick Start, prepara la colección de prueba en Milvus o Zilliz y la clave de embeddings, después añade el servidor al cliente.
2. Configura un índice de prueba sobre código público e intenta encontrar una función conocida.
3. Comprueba el resultado: la búsqueda devuelve el archivo y fragmento esperado, y puedes comprobar el proveedor de embeddings utilizado.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/zilliztech/claude-context/blob/64a87f9b31b0c983f731c91242322562ffd91c7d/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/zilliztech/claude-context/blob/64a87f9b31b0c983f731c91242322562ffd91c7d/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Claude Context para mi objetivo y necesito pasos guiados. Lee https://github.com/zilliztech/claude-context/blob/64a87f9b31b0c983f731c91242322562ffd91c7d/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un índice de prueba sobre código público e intenta encontrar una función conocida..

**Qué comprobar:** La búsqueda devuelve el archivo y fragmento esperado, y puedes comprobar el proveedor de embeddings utilizado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Encontrar archivos relacionados con la autenticación en un proyecto de ejemplo.
- Indexar una biblioteca ficticia y comprobar qué resultado devuelve por función.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Encontrar archivos relacionados con la autenticación en un proyecto de ejemplo.; Indexar una biblioteca ficticia y comprobar qué resultado devuelve por función. | necesitas un producto autónomo y esta pieza requiere un cliente MCP |

**Limitaciones:** Los embeddings y almacenamiento pueden ser servicios externos. La cuenta del cliente no cubre esos cargos; no enviar código sensible sin revisar destino y retención. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [zilliztech/claude-context](https://github.com/zilliztech/claude-context)
- 🌐 Web: <https://github.com/zilliztech/claude-context/tree/master/docs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zilliztech/claude-context/blob/64a87f9b31b0c983f731c91242322562ffd91c7d/README.md)
- [Fuente 2](https://github.com/zilliztech/claude-context/blob/master/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
