[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Herramientas de navegación para agentes

# 🕷️ agent-browser

> CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 51.2k | Apache-2.0 | Rust | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

agent-browser, CLI nativa en Rust para que agentes controlen un navegador comando a comando, de Vercel Labs. Licencia Apache-2.0. Creado en enero de 2026, tiene ~52k estrellas (v0.43.0).

## ¿Qué hace?

`snapshot` devuelve la página como árbol de accesibilidad compacto con referencias (@e1) y el agente actúa sobre ellas: clic, escribir y navegar.

## ¿Cómo lo hace?

Se instala con `npm install -g agent-browser` o `brew install agent-browser`, y después `agent-browser install` (descarga Chrome for Testing). Un daemon controla el navegador por CDP.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente con shell. (combinación por arquitectura) | Instala la CLI y la skill. |
| [Lightpanda](lightpanda.md) | Navegador headless ligero vía CDP. (combinación por arquitectura) | Evalúa la compatibilidad CDP. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | Depuración profunda complementaria. (combinación por arquitectura) | Úsalo para rendimiento y red. |

**Notas:** Alternativas (elige una): playwright-cli.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.43.0 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/vercel-labs/agent-browser/blob/main/README.md)</sub>

## Ver similares

Grupo **CLIs de navegador para agentes**: agent-browser ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **agent-browser** (esta ficha) ⭐ recomendado | 63 | Si buscas esto: cLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes. |
| 2 | [playwright-cli](playwright-cli.md) | 57 | Si buscas esto: interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El CLI y MCP no requieren modelo propio; el agente y proveedores remotos tienen costes independientes |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Incluye skill portable y MCP stdio; descargar el browser es un paso separado y el perfil de pruebas evita mezclar sesiones personales |
| Coste | Sin pago a un modelo en la ruta básica. El CLI y MCP no requieren modelo propio; el agente y proveedores remotos tienen costes independientes |
| Equipo | Preparación según la ruta elegida. Node; Chrome for Testing o navegador configurado; agente opcional |

Incluye skill portable y MCP stdio; descargar el browser es un paso separado y el perfil de pruebas evita mezclar sesiones personales

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- Chrome for Testing o navegador configurado
- agente opcional

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm install -g agent-browser
agent-browser install           # download Chrome for Testing (first time only)
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/vercel-labs/agent-browser/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar agent-browser para mi objetivo y necesito pasos guiados. Lee https://github.com/vercel-labs/agent-browser/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una página propia y consulta el árbol de accesibilidad antes de actuar.

**Qué comprobar:** Puedes identificar referencias de elementos y cambios tras una acción.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Verificar una interfaz
- Preparar capturas y consultas de una página

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Verificar una interfaz; Preparar capturas y consultas de una página | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Incluye skill portable y MCP stdio; descargar el browser es un paso separado y el perfil de pruebas evita mezclar sesiones personales

## Stack y modelos

- **Stack:** Node; Chrome for Testing o navegador configurado; agente opcional
- **Etiquetas:** `navegador` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [playwright-cli](playwright-cli.md) | 15.2k | Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto. |

## Enlaces

- 🐙 GitHub: [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)
- 🌐 Web: <https://agent-browser.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/vercel-labs/agent-browser/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
