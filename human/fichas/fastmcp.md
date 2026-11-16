[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › SDKs y frameworks para crear MCP

# 🧰 FastMCP

> La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28.5k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Framework Python para construir servidores, clientes y aplicaciones interactivas del Model Context Protocol, hecho por Prefect. Licencia Apache-2.0. Es muy popular (~29k estrellas, v4.2.0); su versión 1.0 se incorporó al SDK oficial de Python en 2024.

## ¿Qué hace?

Define herramientas, recursos y prompts con funciones Python decoradas y genera el esquema, la validación y el transporte. Incluye cliente, composición y proxy de servidores, autenticación, pruebas y despliegue. Prefect ofrece aparte FastMCP Gateway (producto comercial) para operar servidores a escala.

## ¿Cómo lo hace?

Se instala con `uv pip install fastmcp` o `pip install fastmcp` y se ejecuta con `fastmcp run`. Tiene comandos para instalar el servidor en clientes como Claude Code y una contraparte TypeScript mantenida por el mismo equipo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Instalar el servidor en Claude Code con la integración documentada de FastMCP. | Ejecuta el comando de instalación para Claude Code de FastMCP. |
| [MCP Inspector](mcp-inspector.md) | Probar y depurar el servidor antes de usarlo. (combinación por arquitectura) | Lanza el Inspector contra tu servidor. |
| [Pydantic AI](pydantic-ai.md) | Consumir el servidor desde agentes Python con el cliente MCP de Pydantic AI. (combinación por arquitectura) | Conecta el servidor como toolset MCP en Pydantic AI. |

**Notas:** Alternativas (elige una): mcp-python-sdk.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v4.2.0 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/PrefectHQ/fastmcp/blob/main/README.md) · [2](https://gofastmcp.com/getting-started/installation) · [3](https://gofastmcp.com/integrations/claude-code)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca no necesita modelo; el cliente, alojamiento y servicios conectados pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un framework para construir servidores y clientes, no un servidor de negocio ya configurado |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca no necesita modelo; el cliente, alojamiento y servicios conectados pueden costar |
| Equipo | Preparación según la ruta elegida. Python y uv; proyecto de prueba |

Es un framework para construir servidores y clientes, no un servidor de negocio ya configurado

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- proyecto de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
uv add fastmcp
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/PrefectHQ/fastmcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FastMCP para mi objetivo y necesito pasos guiados. Lee https://github.com/PrefectHQ/fastmcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Copia la herramienta add del ejemplo y solicita sumar dos números con un cliente MCP.

**Qué comprobar:** La herramienta devuelve la suma esperada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Exponer una función de inventario como herramienta
- Probar autenticación de un servidor propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Exponer una función de inventario como herramienta; Probar autenticación de un servidor propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un framework para construir servidores y clientes, no un servidor de negocio ya configurado

## Stack y modelos

- **Stack:** Python y uv; proyecto de prueba
- **Etiquetas:** `mcp` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MCP Python SDK](mcp-python-sdk.md) | 24.9k | SDK oficial de Python para crear servidores y clientes del Model Context Protocol. |

## Enlaces

- 🐙 GitHub: [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)
- 🌐 Web: <https://gofastmcp.com>
- 🧪 Receta: [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/PrefectHQ/fastmcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
