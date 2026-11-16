[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Herramientas de navegación para agentes

# 🌐 Stagehand

> SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.1k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Stagehand, SDK para agentes de navegador de Browserbase. Licencia MIT. Es maduro y activo (~26k estrellas, v3.x).

## ¿Qué hace?

Combina código y lenguaje natural con primitivas `act`, `extract`, `observe` y agentes, para automatizar navegadores de forma robusta frente a cambios del DOM.

## ¿Cómo lo hace?

Disponible para TypeScript (npm) y Python (`pip install stagehand`), más la CLI `browse`. Requiere la clave de un proveedor de modelos (por ejemplo, OpenAI). Funciona en local o en la nube de Browserbase, que también ofrece un servidor MCP alojado.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Cliente del MCP alojado de Browserbase. | Conecta el MCP. |
| [Lightpanda](lightpanda.md) | Navegador headless ligero vía CDP. (combinación por arquitectura) | Conecta por CDP si es compatible. |
| [firecrawl](firecrawl.md) | Extracción masiva complementaria. (combinación por arquitectura) | Usa Firecrawl para el rastreo y Stagehand para las interacciones. |
| [Steel Browser](steel-browser.md) | Combinación recíproca: Steel Browser lo enlaza como «El cookbook oficial de Steel incluye ejemplos de Stagehand en Python y TypeScript». | Orden indicado desde Steel Browser: Arranca Steel; después sigue el ejemplo `stagehand-ts` o `stagehand-py` del cookbook. |

**Notas:** Alternativas (elige una): browser-use, skyvern. La nube de Browserbase es de pago.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada stagehand-server-v3/v3.7.7 (2026-10-23) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/browserbase/stagehand/blob/main/README.md) · [2](https://docs.stagehand.dev/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. Modelo y Browserbase pueden cobrar por uso; SDK, navegador local y MCP hospedado son rutas distintas |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. El MCP remoto documentado necesita cuenta y clave Browserbase; usar Claude Code o Codex para programar no aporta créditos de navegación |
| Coste | El coste depende del proveedor o la ruta. Modelo y Browserbase pueden cobrar por uso; SDK, navegador local y MCP hospedado son rutas distintas |
| Equipo | Preparación según la ruta elegida. Node o Python; modelo y navegador según ruta; clave Browserbase para MCP hospedado; sitio de prueba |

El MCP remoto documentado necesita cuenta y clave Browserbase; usar Claude Code o Codex para programar no aporta créditos de navegación

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node o Python
- modelo y navegador según ruta
- clave Browserbase para MCP hospedado
- sitio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pnpm add @browserbasehq/stagehand 'zod@~4.4.3'
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/browserbase/stagehand/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Stagehand para mi objetivo y necesito pasos guiados. Lee https://github.com/browserbase/stagehand/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Extrae dos campos de una página propia y contrasta la estructura con el contenido visible.

**Qué comprobar:** Puedes comprobar datos y acciones del navegador.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar extracción estructurada
- Automatizar un formulario de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar extracción estructurada; Automatizar un formulario de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP remoto documentado necesita cuenta y clave Browserbase; usar Claude Code o Codex para programar no aporta créditos de navegación

## Stack y modelos

- **Stack:** Node o Python; modelo y navegador según ruta; clave Browserbase para MCP hospedado; sitio de prueba
- **Etiquetas:** `browser` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [browser-use](browser-use.md) | 121k | Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. |
| [Skyvern](skyvern.md) | 23.4k | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. |

## Enlaces

- 🐙 GitHub: [browserbase/stagehand](https://github.com/browserbase/stagehand)
- 🌐 Web: <https://stagehand.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/browserbase/stagehand/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
