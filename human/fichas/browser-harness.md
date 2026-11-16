[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Herramientas de navegación para agentes

# 🌐 Browser Harness

> Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.1k | MIT | Python | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Browser Harness, harness con el que Claude Code, Codex o Cursor usan tu Chrome real con tu sesión iniciada, de browser-use. Licencia MIT. Creado en abril de 2026 (~19k estrellas, v0.1.13); ahora es el motor de Browser Use y se recomienda usar la CLI `browser-use`.

## ¿Qué hace?

Abre páginas, hace clic, escribe, lee y descarga en tu navegador real mediante el protocolo de depuración remota.

## ¿Cómo lo hace?

Se instala con `uv tool install browser-use` y `browser-use skill install`, y luego activando la depuración remota en `chrome://inspect`. Al usar tu sesión real, el agente actúa con tus credenciales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente documentado. | Registra la skill. |
| [Codex CLI](codex.md) | Agente documentado. | Registra la skill. |
| [Gemini CLI](gemini-cli.md) | Cualquier cliente MCP puede usar Browser Harness vía `browser-harness-mcp`; Gemini CLI es uno de ellos. (combinación por arquitectura) | Registra `browser-harness-mcp` en la configuración MCP de Gemini CLI. |

**Notas:** Alternativas (elige una): playwright-mcp, chrome-devtools-mcp, browser-use. Riesgo: acceso del agente a sesiones autenticadas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.1.13 (2026-09-04) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/browser-use/browser-harness/blob/main/README.md)</sub>

## Ver similares

Grupo **Agentes que navegan la web**: Browser Harness ocupa la posición 4 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [browser-use](browser-use.md) ⭐ recomendado | 73 | Si quieres el framework Python más usado para que un LLM controle el navegador. |
| 2 | [Stagehand](stagehand.md) | 61 | Si trabajas en TypeScript y quieres mezclar código Playwright con acciones en lenguaje natural. |
| 3 | [Skyvern](skyvern.md) | 60 | Si automatizas formularios y flujos repetitivos con visión y no quieres selectores frágiles. |
| 4 | **Browser Harness** (esta ficha) | 60 | Si quieres que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El acceso al navegador propio no necesita API de modelo adicional; el agente y Cloud opcional se pagan aparte |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Ahora es el motor de Browser Use y el README recomienda su CLI; conectar una sesión autenticada concede acceso a lo que esa sesión puede hacer |
| Coste | El coste depende del proveedor o la ruta. El acceso al navegador propio no necesita API de modelo adicional; el agente y Cloud opcional se pagan aparte |
| Equipo | Preparación según la ruta elegida. Browser Use CLI actual; Chrome y perfil de prueba; cliente agente |

Ahora es el motor de Browser Use y el README recomienda su CLI; conectar una sesión autenticada concede acceso a lo que esa sesión puede hacer

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Browser Use CLI actual
- Chrome y perfil de prueba
- cliente agente

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/browser-use/browser-harness/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Browser Harness para mi objetivo y necesito pasos guiados. Lee https://github.com/browser-use/browser-harness/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta un perfil de prueba y solicita solo leer el título de una página.

**Qué comprobar:** Puedes identificar qué navegador y sesión expone al agente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un agente con un browser propio
- Inspeccionar una página autenticada de laboratorio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un agente con un browser propio; Inspeccionar una página autenticada de laboratorio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ahora es el motor de Browser Use y el README recomienda su CLI; conectar una sesión autenticada concede acceso a lo que esa sesión puede hacer

## Stack y modelos

- **Stack:** Browser Use CLI actual; Chrome y perfil de prueba; cliente agente
- **Etiquetas:** `browser` `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Playwright MCP](playwright-mcp.md) | 39.7k | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | 56.3k | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. |
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |

## Enlaces

- 🐙 GitHub: [browser-use/browser-harness](https://github.com/browser-use/browser-harness)
- 🌐 Web: <https://browser-harness.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/browser-use/browser-harness/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
