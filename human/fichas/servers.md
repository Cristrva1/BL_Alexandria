[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 📚 servers

> Colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 92k | Apache-2.0 (en transición desde MIT) | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 79/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** Apache-2.0 (en transición desde MIT). Documentación bajo CC-BY-4.0. Fuente: [LICENSE](https://github.com/modelcontextprotocol/servers/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Repositorio oficial de servidores de referencia del Model Context Protocol. El proyecto MCP está pasando de MIT a Apache-2.0 (GitHub muestra NOASSERTION). Es muy popular (~92k estrellas, v2.4.0).

## ¿Qué hace?

Contiene implementaciones de referencia que muestran funciones de MCP y el uso de los SDK: Everything (servidor de pruebas), Fetch, Filesystem, Git, Memory (grafo de conocimiento), Sequential Thinking y Time. Los servidores antiguos se movieron a servers-archived y la lista de servidores de terceros ahora vive en el MCP Registry. El README advierte que son ejemplos educativos, no soluciones listas para producción.

## ¿Cómo lo hace?

Cada servidor se ejecuta con `npx` (TypeScript) o `uvx` (Python) desde la configuración del cliente MCP, o con Docker. Están escritos con los SDK oficiales. Revisa los permisos (por ejemplo, las rutas permitidas de Filesystem) antes de usarlos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [MCP Inspector](mcp-inspector.md) | Probar los servidores de referencia, sobre todo Everything, que existe para ejercitar clientes. (combinación por arquitectura) | Lanza el Inspector contra el servidor elegido. |
| [mcp-use](mcp-use.md) | Tomar los servidores como ejemplo al construir uno propio. (combinación por arquitectura) | Estudia el servidor parecido y construye el tuyo con mcp-use. |
| [awesome-mcp-servers](awesome-mcp-servers.md) | Encontrar servidores de la comunidad más allá de las referencias. (combinación por arquitectura) | Consulta también el MCP Registry oficial. |
| [OpenDots](opendots.md) | Combinación recíproca: OpenDots lo enlaza como «Servidores MCP de referencia como herramientas. (combinación por arquitectura)». | Orden indicado desde OpenDots: Añade los MCP por Dot. |

**Notas:** Sin alternativas declaradas. No son para producción, según el propio README.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v2.4.0 (2026-11-11) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/modelcontextprotocol/servers/blob/main/README.md) · [2](https://registry.modelcontextprotocol.io/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Leer no requiere API; el cliente y cada implementación elegida tienen sus requisitos |
| Claude Code | Depende del recurso o la configuración |
| Codex | Depende del recurso o la configuración |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. Los autores los presentan como implementaciones educativas de referencia, no servicios listos para producción |
| Coste | Sin pago a un modelo en la ruta básica. Leer no requiere API; el cliente y cada implementación elegida tienen sus requisitos |
| Equipo | Preparación según la ruta elegida. Navegador; Node o Python según el servidor elegido |

Los autores los presentan como implementaciones educativas de referencia, no servicios listos para producción

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- Node o Python según el servidor elegido

1. Elige un servidor de referencia y comprueba sus permisos sobre datos ficticios.
2. Comprueba: Entiendes qué herramientas expone y qué datos puede modificar.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/modelcontextprotocol/servers/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar servers para mi objetivo y necesito pasos guiados. Lee https://github.com/modelcontextprotocol/servers/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige un servidor de referencia y comprueba sus permisos sobre datos ficticios.

**Qué comprobar:** Entiendes qué herramientas expone y qué datos puede modificar.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender cómo se implementa memoria MCP
- Estudiar acceso a un repositorio Git de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender cómo se implementa memoria MCP; Estudiar acceso a un repositorio Git de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los autores los presentan como implementaciones educativas de referencia, no servicios listos para producción

## Stack y modelos

- **Stack:** Navegador; Node o Python según el servidor elegido
- **Etiquetas:** `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- 🌐 Web: <https://modelcontextprotocol.io>
- 🧪 Receta: [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/modelcontextprotocol/servers/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
