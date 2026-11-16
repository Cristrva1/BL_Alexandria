[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › SDKs y frameworks para crear MCP

# 🛠️ mcp-use

> Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

Framework TypeScript para construir, probar y publicar servidores MCP, plugins de ChatGPT y conectores de Claude, de mcp-use. Licencia MIT. Es activo (~11k estrellas, mcp-use@2.12.4).

## ¿Qué hace?

Ofrece tipado completo, vistas nativas y soporte de MCP Apps, un Inspector integrado y una experiencia pensada para agentes: andamiaje, invocación, inspección, capturas y despliegue desde el propio agente. Incluye ejemplos y opción de despliegue en su plataforma.

## ¿Cómo lo hace?

Se instala con npm (`mcp-use`) y se crea un proyecto con su CLI; la v2 tiene guía de migración que puede ejecutar el agente. La documentación está en docs.mcp-use.com.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Construir y probar conectores desde el agente con el flujo «agent-first» de mcp-use. | Crea el proyecto y deja que el agente use los comandos de mcp-use. |
| [awesome-mcp-servers](awesome-mcp-servers.md) | Buscar servidores existentes antes de construir uno. (combinación por arquitectura) | Consulta la lista y reutiliza lo que exista. |
| [Google MCP](mcp.md) | Referencia de servidores MCP de Google para integrarlos o tomarlos como ejemplo. (combinación por arquitectura) | Revisa la lista de Google y conecta los que necesites. |

**Notas:** Alternativas (elige una): mcp-typescript-sdk.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada mcp-use@2.12.4 (2026-11-11) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mcp-use/mcp-use/blob/main/README.md) · [2](https://docs.mcp-use.com/v2/typescript/getting-started/welcome)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El servidor básico no exige LLM; agentes, proveedores y alojamiento tienen costes según ruta |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. MCP Apps con widgets requiere capacidades del cliente adicionales a las de un servidor MCP de texto |
| Coste | El coste depende del proveedor o la ruta. El servidor básico no exige LLM; agentes, proveedores y alojamiento tienen costes según ruta |
| Equipo | Preparación según la ruta elegida. Node.js; plantilla elegida; Python solo para su ruta correspondiente |

MCP Apps con widgets requiere capacidades del cliente adicionales a las de un servidor MCP de texto

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- plantilla elegida
- Python solo para su ruta correspondiente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx -y create-mcp-use-app@latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mcp-use/mcp-use/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mcp-use para mi objetivo y necesito pasos guiados. Lee https://github.com/mcp-use/mcp-use/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera una app MCP de ejemplo y prueba su herramienta desde el inspector incluido.

**Qué comprobar:** Puedes ver una respuesta y la interfaz asociada si el cliente admite MCP Apps.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir una herramienta con interfaz embebida
- Desplegar un servidor MCP para una app propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir una herramienta con interfaz embebida; Desplegar un servidor MCP para una app propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP Apps con widgets requiere capacidades del cliente adicionales a las de un servidor MCP de texto

## Stack y modelos

- **Stack:** Node.js; plantilla elegida; Python solo para su ruta correspondiente
- **Etiquetas:** `automation` `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MCP TypeScript SDK](mcp-typescript-sdk.md) | 13.8k | SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. |

## Enlaces

- 🐙 GitHub: [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use)
- 🌐 Web: <https://manufact.com>
- 🧪 Receta: [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mcp-use/mcp-use/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
