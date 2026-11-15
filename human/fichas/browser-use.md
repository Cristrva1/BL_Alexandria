[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Herramientas de navegación para agentes

# 🌐 browser-use

> Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 121k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La biblioteca MIT permite navegador y modelo locales; los defaults del ejemplo usan gateway y browser Cloud facturados |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. La versión actual integra browser-harness y registra skills para Claude/Codex y MCP; una sesión con cookies puede actuar con los permisos de esa cuenta |
| Coste | El coste depende del proveedor o la ruta. La biblioteca MIT permite navegador y modelo locales; los defaults del ejemplo usan gateway y browser Cloud facturados |
| Equipo | Preparación según la ruta elegida. Python y uv; Chrome o browser Cloud; agente o proveedor; perfil de prueba |

La versión actual integra browser-harness y registra skills para Claude/Codex y MCP; una sesión con cookies puede actuar con los permisos de esa cuenta

## Qué puedes hacer con él

Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos.

## Por qué destaca

Usos propuestos: Extraer información de una web propia; Probar navegación con un agente.

## Cómo funciona

La versión actual integra browser-harness y registra skills para Claude/Codex y MCP; una sesión con cookies puede actuar con los permisos de esa cuenta

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- Chrome o browser Cloud
- agente o proveedor
- perfil de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/browser-use/browser-use/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar browser-use para mi objetivo y necesito pasos guiados. Lee https://github.com/browser-use/browser-use/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta un navegador de prueba y solicita leer una página sin enviar formularios ni usar cuentas personales.

**Qué comprobar:** Puedes revisar pestaña, contexto y resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Extraer información de una web propia
- Probar navegación con un agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Extraer información de una web propia; Probar navegación con un agente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La versión actual integra browser-harness y registra skills para Claude/Codex y MCP; una sesión con cookies puede actuar con los permisos de esa cuenta

## Stack y modelos

- **Stack:** Python y uv; Chrome o browser Cloud; agente o proveedor; perfil de prueba
- **Etiquetas:** `automation` `browser` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| [gpt-researcher](gpt-researcher.md) | 30.7k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Gemini Computer Use (preview)](computer-use-preview.md) | 3.3k | Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. |
| [Stagehand](stagehand.md) | 26.1k | SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. |
| [Skyvern](skyvern.md) | 23.4k | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. |
| [Playwright MCP](playwright-mcp.md) | 39.7k | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |

## Enlaces

- 🐙 GitHub: [browser-use/browser-use](https://github.com/browser-use/browser-use)
- 🌐 Web: <https://browser-use.com>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/browser-use/browser-use/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
