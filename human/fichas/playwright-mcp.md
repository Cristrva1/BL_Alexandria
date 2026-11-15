[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Playwright MCP

> Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.7k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API adicional de modelo; usa el agente anfitrión y recursos del navegador |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El README documenta los tres clientes; revisa el perfil elegido porque puede conservar sesiones y cookies |
| Coste | Consumo del agente que ya utilizas. No necesita API adicional de modelo; usa el agente anfitrión y recursos del navegador |
| Equipo | Preparación según la ruta elegida. Node.js; npm; cliente MCP; navegador de prueba |

El README documenta los tres clientes; revisa el perfil elegido porque puede conservar sesiones y cookies

## Qué puedes hacer con él

Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright.

## Por qué destaca

Usos propuestos: Probar una navegación de tu app; Inspeccionar un formulario de desarrollo.

## Cómo funciona

El README documenta los tres clientes; revisa el perfil elegido porque puede conservar sesiones y cookies

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- npm
- cliente MCP
- navegador de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
claude mcp add playwright npx @playwright/mcp@latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/microsoft/playwright-mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Playwright MCP para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/playwright-mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una página local con un formulario ficticio y comprueba sus campos antes de rellenarla.

**Qué comprobar:** La instantánea accesible identifica campos y el resultado de la acción.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar una navegación de tu app
- Inspeccionar un formulario de desarrollo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar una navegación de tu app; Inspeccionar un formulario de desarrollo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README documenta los tres clientes; revisa el perfil elegido porque puede conservar sesiones y cookies

## Stack y modelos

- **Stack:** Node.js; npm; cliente MCP; navegador de prueba
- **Etiquetas:** `mcp` `browser` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [playwright](playwright.md) | 100k | Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | 56.3k | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. |
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |
| [Browser Harness](browser-harness.md) | 19.1k | Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada. |

## Enlaces

- 🐙 GitHub: [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)
- 🌐 Web: <https://www.npmjs.com/package/@playwright/mcp>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/playwright-mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
