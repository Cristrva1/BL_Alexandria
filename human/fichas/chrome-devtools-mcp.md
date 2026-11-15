[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Chrome DevTools MCP

> Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 56.3k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta. |
| Coste | Consumo del agente que ya utilizas. El modelo se consume en el cliente. Los servicios que la herramienta consulta pueden tener cuentas o tarifas propias. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

Puede conectarse a un cliente con soporte MCP, incluido Claude Code o Codex. Debes configurar el servidor y sus permisos.

## Qué puedes hacer con él

Tu agente de código puede abrir páginas, leer errores de consola, inspeccionar peticiones y medir rendimiento para depurar de verdad.

## Por qué destaca

Hecho por el equipo de Chrome; acceso directo a las DevTools.

## Cómo funciona

Controla Chrome por el protocolo DevTools y expone herramientas MCP de navegación, red y trazas.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible.
- Las credenciales del servicio conectado, si las pide el servidor.

1. Instala o configura el servidor según su README.
2. Añade su comando o URL en la configuración MCP de tu cliente.
3. Comprueba que aparecen las herramientas antes de asignar una tarea.

[Instrucciones originales de instalación](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Chrome DevTools MCP para mi objetivo y necesito pasos guiados. Lee https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Depurar errores de consola con el agente
- Analizar rendimiento de una página
- Revisar peticiones de red

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente necesita depurar una web como lo harías en DevTools | solo quieres automatizar navegación; mira `playwright-mcp` |

## Stack y modelos

- **Stack:** TypeScript, Puppeteer
- **Etiquetas:** `mcp` `browser` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Playwright MCP](playwright-mcp.md) | 39.7k | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |
| [Browser Harness](browser-harness.md) | 19.1k | Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada. |

## Enlaces

- 🐙 GitHub: [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- 🌐 Web: <https://developer.chrome.com/docs/devtools/agents>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
