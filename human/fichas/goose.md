[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Agentes de código (terminal e IDE)

# 👨‍💻 goose

> Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 56.6k | Apache-2.0 | Rust | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |
| Otras rutas | El README también documenta proveedores ACP para utilizar acceso de Gemini, además de APIs y modelos locales. |

El README documenta una integración con las sesiones de los agentes indicados. Configurar esa ruta y comprobar sus límites; otras rutas pueden facturar por API.

## Qué puedes hacer con él

Funciona como app de escritorio o CLI y va más allá del código: automatiza tareas de desarrollo y de sistema con extensiones MCP. Nacido en Block.

## Por qué destaca

Diseñado alrededor de MCP desde el inicio, con app de escritorio y recetas compartibles.

## Cómo funciona

Un núcleo en Rust ejecuta el bucle del agente y carga extensiones MCP como herramientas.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/aaif-goose/goose/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar goose para mi objetivo y necesito pasos guiados. Lee https://github.com/aaif-goose/goose/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Automatizar tareas de desarrollo con MCP
- Agente de escritorio para no programadores
- Recetas reutilizables para el equipo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un agente abierto con app de escritorio y MCP | solo programas en terminal y quieres el más usado; mira `opencode` |

## Stack y modelos

- **Stack:** Rust, TypeScript, Electron
- **Etiquetas:** `coding-agent` `agents` `mcp` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Playwright MCP](playwright-mcp.md) | 39.7k | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |
| [GitHub MCP Server](github-mcp-server.md) | 34.5k | Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Open Interpreter](open-interpreter.md) | 68.9k | Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos. |

## Enlaces

- 🐙 GitHub: [aaif-goose/goose](https://github.com/aaif-goose/goose)
- 🌐 Web: <https://goose-docs.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/aaif-goose/goose/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
