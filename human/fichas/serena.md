[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Serena

> Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.4k | GPL-3.0-or-later (SolidLSP: MIT) | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 65/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** GPL-3.0-or-later (SolidLSP: MIT). Fuente: [LICENSE](https://github.com/oraios/serena/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Serena, un kit de herramientas de código semántico para agentes («el IDE de tu agente»), de Oraios AI. La aplicación es GPL-3.0-or-later y el componente SolidLSP es MIT (GitHub muestra NOASSERTION). Es muy activa (~31k estrellas, v2.1.0).

## ¿Qué hace?

Da al agente recuperación, edición, refactorización y depuración a nivel de símbolo, apoyándose en la estructura del código en lugar de leer archivos enteros. Usa servidores de lenguaje (LSP) de forma gratuita o, como alternativa, un plugin de JetBrains de pago. Se integra con cualquier cliente mediante MCP.

## ¿Cómo lo hace?

Se instala con uv y se conecta al cliente con un comando de arranque o en modo HTTP. El README pide no instalarlo desde marketplaces de MCP o plugins, porque traen comandos desactualizados. Algunos lenguajes requieren instalar su servidor de lenguaje.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Cliente MCP compatible, con instrucciones en la documentación. | Instala Serena con uv y añádelo con su comando de arranque. |
| [Codex CLI](codex.md) | Cliente MCP compatible. | Configura el comando de arranque de Serena en Codex. |
| [Context7](context7.md) | Combinar navegación semántica del código propio con documentación actualizada de librerías. (combinación por arquitectura) | Instala ambos servidores en el mismo agente. |

**Notas:** Alternativas (elige una): codegraph, codebase-memory-mcp, graphify.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v2.1.0 (2026-10-19) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/oraios/serena/blob/main/README.md) · [2](https://oraios.github.io/serena/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El backend LSP usa recursos locales; el plugin JetBrains tiene pago separado; el modelo del agente conserva sus límites |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El autor desaconseja marketplaces con instalaciones antiguas; configura el comando de lanzamiento oficial y el backend adecuado |
| Coste | El coste depende del proveedor o la ruta. El backend LSP usa recursos locales; el plugin JetBrains tiene pago separado; el modelo del agente conserva sus límites |
| Equipo | Preparación según la ruta elegida. uv; servidor de lenguaje del proyecto; repositorio de prueba |

El autor desaconseja marketplaces con instalaciones antiguas; configura el comando de lanzamiento oficial y el backend adecuado

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv
- servidor de lenguaje del proyecto
- repositorio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
uv tool install -p 3.13 serena-agent
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/oraios/serena/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Serena para mi objetivo y necesito pasos guiados. Lee https://github.com/oraios/serena/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide localizar una función por símbolo y enumera sus referencias antes de editar.

**Qué comprobar:** El agente identifica la definición y usos reales.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Navegar una base de código grande
- Refactorizar un símbolo con contexto semántico

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Navegar una base de código grande; Refactorizar un símbolo con contexto semántico | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El autor desaconseja marketplaces con instalaciones antiguas; configura el comando de lanzamiento oficial y el backend adecuado

## Stack y modelos

- **Stack:** uv; servidor de lenguaje del proyecto; repositorio de prueba
- **Etiquetas:** `mcp` `coding-agent` `code` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [codegraph](codegraph.md) | 77.6k | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. |
| [codebase-memory-mcp](codebase-memory-mcp.md) | 48.6k | Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes. |
| [graphify](graphify.md) | 148k | CLI y skill que convierten código y documentos en un grafo consultable; el código se analiza localmente con AST y la extracción semántica tiene rutas separadas. |

## Enlaces

- 🐙 GitHub: [oraios/serena](https://github.com/oraios/serena)
- 🌐 Web: <https://oraios.github.io/serena>
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/oraios/serena/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
