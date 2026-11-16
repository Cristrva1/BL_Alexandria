[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › SDKs y frameworks para crear MCP

# 🧰 MCP TypeScript SDK

> SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.8k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

SDK oficial en TypeScript del Model Context Protocol. La rama principal es la v2 estable (v2.4.0), que implementa la especificación MCP 2026-07-28. El proyecto MCP está pasando de MIT a Apache-2.0 (GitHub muestra NOASSERTION); ~14k estrellas.

## ¿Qué hace?

Proporciona librerías de servidor (herramientas, recursos, prompts, Streamable HTTP, stdio, ayudas de autenticación) y de cliente (transportes, ayudas OAuth). Se publica en paquetes separados: `@modelcontextprotocol/server` y `@modelcontextprotocol/client`. Funciona en Node.js, Bun y Deno.

## ¿Cómo lo hace?

Se instala con npm (`npm install @modelcontextprotocol/server`, más `zod` para los esquemas). Hay guía de migración desde la v1. Es la base de muchos servidores MCP en JavaScript.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [MCP Inspector](mcp-inspector.md) | Herramienta oficial para probar servidores construidos con el SDK. | Ejecuta `npx @modelcontextprotocol/inspector` contra tu servidor. |
| [AI SDK (Vercel)](vercel-ai.md) | Consumir servidores MCP desde apps con el cliente MCP del AI SDK. | Conecta tu servidor con las herramientas MCP del AI SDK. |
| [Claude Code](claude-code.md) | Probar el servidor en un agente real. (combinación por arquitectura) | Regístralo con `claude mcp add`. |

**Notas:** Alternativas (elige una): mcp-use.

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v2.4.0 (2026-10-23) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/README.md) · [2](https://modelcontextprotocol.io/docs/tools/inspector) · [3](https://ai-sdk.dev/docs/ai-sdk-core/mcp-tools)</sub>

## Ver similares

Grupo **SDKs de MCP en TypeScript**: MCP TypeScript SDK ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [mcp-use](mcp-use.md) ⭐ recomendado | 64 | Si buscas esto: framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. |
| 2 | **MCP TypeScript SDK** (esta ficha) | 60 | Si buscas esto: sDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El SDK no llama modelos por sí solo; servicios y despliegue se presupuestan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La rama revisada es v2 con paquetes server y client separados; no mezcles imports de tutoriales v1 |
| Coste | Sin pago a un modelo en la ruta básica. El SDK no llama modelos por sí solo; servicios y despliegue se presupuestan aparte |
| Equipo | Preparación según la ruta elegida. Node.js; TypeScript; gestor de paquetes |

La rama revisada es v2 con paquetes server y client separados; no mezcles imports de tutoriales v1

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- TypeScript
- gestor de paquetes

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm install @modelcontextprotocol/server
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MCP TypeScript SDK para mi objetivo y necesito pasos guiados. Lee https://github.com/modelcontextprotocol/typescript-sdk/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el ejemplo v2 para exponer una herramienta y llámala desde Inspector.

**Qué comprobar:** Ves el esquema y una respuesta válida de la herramienta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir un servidor MCP en TypeScript
- Crear un cliente que enumere herramientas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir un servidor MCP en TypeScript; Crear un cliente que enumere herramientas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La rama revisada es v2 con paquetes server y client separados; no mezcles imports de tutoriales v1

## Stack y modelos

- **Stack:** Node.js; TypeScript; gestor de paquetes
- **Etiquetas:** `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mcp-use](mcp-use.md) | 11k | Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. |

## Enlaces

- 🐙 GitHub: [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)
- 🌐 Web: <https://ts.sdk.modelcontextprotocol.io/v2>
- 🧪 Receta: [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
