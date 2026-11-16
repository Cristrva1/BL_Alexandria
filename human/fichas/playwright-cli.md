[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Herramientas de navegación para agentes

# 🎭 playwright-cli

> Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.2k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Playwright CLI, CLI de Playwright con skills para agentes de código, de Microsoft. Licencia Apache-2.0. Tiene ~15k estrellas (v0.1.x).

## ¿Qué hace?

Expone la automatización del navegador como comandos (más eficientes en tokens que MCP, según el README): navegar, hacer snapshots, clic, trazas, etc.

## ¿Cómo lo hace?

Requiere Node.js 20+ y se instala con `npm install -g @playwright/cli@latest`. Funciona con Claude Code, GitHub Copilot y otros agentes, y puede conectarse a un navegador abierto con la extensión Playwright MCP Bridge.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [playwright](playwright.md) | Motor subyacente. | Viene incluido. |
| [Claude Code](claude-code.md) | Agente documentado. | Instala las skills. |
| [Playwright MCP](playwright-mcp.md) | Variante MCP para agentes sin shell. | Elige CLI o MCP según el agente. |

**Notas:** Alternativas (elige una): agent-browser.

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada v0.1.24 (2026-11-10) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/microsoft/playwright-cli/blob/main/README.md)</sub>

## Ver similares

Grupo **CLIs de navegador para agentes**: playwright-cli ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [agent-browser](agent-browser.md) ⭐ recomendado | 63 | Si buscas esto: cLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes. |
| 2 | **playwright-cli** (esta ficha) | 57 | Si buscas esto: interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El CLI no necesita API de IA propia; el agente usa su modelo o plan |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Los hosts compatibles pueden leer las skills instaladas; control por CLI y MCP son superficies distintas y las sesiones deben separarse al trabajar en paralelo |
| Coste | El coste depende del proveedor o la ruta. El CLI no necesita API de IA propia; el agente usa su modelo o plan |
| Equipo | Preparación según la ruta elegida. Node; navegador; agente con shell; aplicación de prueba |

Los hosts compatibles pueden leer las skills instaladas; control por CLI y MCP son superficies distintas y las sesiones deben separarse al trabajar en paralelo

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- navegador
- agente con shell
- aplicación de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm install -g @playwright/cli@latest
playwright-cli --help
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/microsoft/playwright-cli/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar playwright-cli para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/playwright-cli/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala sus skills y abre una página de prueba para obtener snapshot antes de pulsar un control.

**Qué comprobar:** Puedes usar referencias del snapshot y comprobar el resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un flujo con un agente
- Registrar una secuencia de navegación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un flujo con un agente; Registrar una secuencia de navegación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los hosts compatibles pueden leer las skills instaladas; control por CLI y MCP son superficies distintas y las sesiones deben separarse al trabajar en paralelo

## Stack y modelos

- **Stack:** Node; navegador; agente con shell; aplicación de prueba
- **Etiquetas:** `browser` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [agent-browser](agent-browser.md) | 51.2k | CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes. |

## Enlaces

- 🐙 GitHub: [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli)
- 🌐 Web: <https://playwright.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/playwright-cli/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
