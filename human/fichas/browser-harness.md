[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Herramientas de navegación para agentes

# 🌐 Browser Harness

> Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.1k | MIT | Python | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

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

Conecta el agente a tu navegador por CDP con un arnés pequeño y editable. Útil cuando necesitas libertad total y tus cuentas ya abiertas.

## Por qué destaca

De los creadores de browser-use; se configura con un solo prompt.

## Cómo funciona

Habla con Chrome por el protocolo DevTools y expone comandos simples que el agente invoca.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible.
- Las credenciales del servicio conectado, si las pide el servidor.

1. Instala o configura el servidor según su README.
2. Añade su comando o URL en la configuración MCP de tu cliente.
3. Comprueba que aparecen las herramientas antes de asignar una tarea.

[Instrucciones originales de instalación](https://github.com/browser-use/browser-harness/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Browser Harness para mi objetivo y necesito pasos guiados. Lee https://github.com/browser-use/browser-harness/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Automatizar tareas en webs donde ya estás logueado
- Pruebas manuales asistidas
- Investigación con tu sesión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tu agente debe usar tu navegador real con sesión | necesitas aislamiento; mira `playwright-mcp` |

**Limitaciones:** El agente actúa con tus cuentas reales: supervisa lo que hace.

## Stack y modelos

- **Stack:** Python, CDP
- **Etiquetas:** `browser` `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Playwright MCP](playwright-mcp.md) | 39.7k | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | 56.3k | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. |

## Enlaces

- 🐙 GitHub: [browser-use/browser-harness](https://github.com/browser-use/browser-harness)
- 🌐 Web: <https://browser-harness.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/browser-use/browser-harness/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
