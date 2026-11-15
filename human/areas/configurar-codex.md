[Áreas](../areas.md) · [Inicio](../README.md)

# Configuración de Codex

Prepara el cliente de Codex y reúne skills, contexto y conexiones que tienen compatibilidad documentada.

23 repos únicos · 5 subcategorías. [Ver en el explorador](../../docs/index.html#/area/configurar-codex).

## Primera configuración, paso a paso

1. **Prepara el cliente.** Abre la fuente oficial de Codex, elige la instalación para tu sistema y comprueba el acceso de tu cuenta antes de añadir extensiones.
2. **Prueba un proyecto pequeño.** Abre una carpeta de prueba y pide al agente que explique un archivo. Confirma qué permisos solicita y que puedes revisar los cambios.
3. **Añade una mejora concreta.** Elige una sola skill o conexión de las subcategorías. Abre su ficha, lee la fuente y sigue la instalación indicada para este cliente.
4. **Comprueba el resultado y el consumo.** Repite la tarea pequeña, revisa si la mejora ayuda y consulta el uso de tu cuenta. Los servicios externos tienen sus propios accesos y costes.

[Fuente oficial del cliente](https://github.com/openai/codex#readme)

Esta colección reúne clientes, extensiones y material para configurar el agente. Cada ficha distingue su forma de uso. La compatibilidad con skills o MCP no implica que tu plan pague todas las APIs de las aplicaciones que construyas.

## Opciones para empezar

[Codex CLI](../fichas/codex.md), [Agent Skills (Addy Osmani)](../fichas/agent-skills.md), [superpowers](../fichas/superpowers.md)

Son opciones para comparar. No es necesario instalar todas.

## Subcategorías

### Instalación y primeros pasos

Cliente oficial y formas de empezar con un proyecto.

[Explorar 1 repos](../../docs/index.html#/explorar?area=configurar-codex&topic=codex-inicio)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [Codex CLI](../fichas/codex.md) | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. | API de IA opcional |

### Skills y método de trabajo

Instrucciones y plugins documentados para Codex.

[Explorar 6 repos](../../docs/index.html#/explorar?area=configurar-codex&topic=codex-skills)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [Agent Skills (Addy Osmani)](../fichas/agent-skills.md) | Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes. | Sin API de IA en la ruta básica |
| [agent-toolkit](../fichas/agent-toolkit.md) | Conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documentación y planificación. | Sin API de IA en la ruta básica |
| [Agentic Awesome Skills](../fichas/antigravity-awesome-skills.md) | Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con instalador npx y MCP local. | Sin API de IA en la ruta básica |
| [skills](../fichas/google-skills.md) | Colección de skills para trabajar con productos y tecnologías de Google desde agentes de programación compatibles. | Sin API de IA en la ruta básica |
| [Stitch Skills](../fichas/stitch-skills.md) | Colección de skills de agente para trabajar con el servidor MCP de Google Stitch. | Sin API de IA en la ruta básica |
| [superpowers](../fichas/superpowers.md) | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. | Sin API de IA en la ruta básica |

### MCP y herramientas de navegador

Conectar documentación, GitHub y navegación al agente.

[Explorar 5 repos](../../docs/index.html#/explorar?area=configurar-codex&topic=codex-mcp)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [Chrome DevTools MCP](../fichas/chrome-devtools-mcp.md) | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. | Sin API de IA en la ruta básica |
| [Context7](../fichas/context7.md) | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. | Sin API de IA en la ruta básica |
| [GitHub MCP Server](../fichas/github-mcp-server.md) | Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código. | Sin API de IA en la ruta básica |
| [Playwright MCP](../fichas/playwright-mcp.md) | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. | Sin API de IA en la ruta básica |
| [Serena](../fichas/serena.md) | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. | Sin API de IA en la ruta básica |

### Memoria, contexto y sesiones

Mantener decisiones y organizar el contexto de trabajo.

[Explorar 5 repos](../../docs/index.html#/explorar?area=configurar-codex&topic=codex-contexto)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [claude-mem](../fichas/claude-mem.md) | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. | API de IA opcional |
| [elephant-goldfish-model](../fichas/elephant-goldfish-model.md) | Plugin con instrucciones para diseñar y revisar software con agentes mediante contextos y perspectivas complementarias. | Sin API de IA en la ruta básica |
| [Engram](../fichas/engram.md) | Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. | Sin API de IA en la ruta básica |
| [headroom](../fichas/headroom.md) | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | API de IA opcional |
| [T3 Code](../fichas/t3code.md) | Interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina. | API de IA opcional |

### Diseño, documentos y seguridad

Skills y herramientas de oficio con acceso documentado desde Codex.

[Explorar 6 repos](../../docs/index.html#/explorar?area=configurar-codex&topic=codex-especialidades)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [Cybersecurity Skills (comunidad)](../fichas/cybersecurity-skills.md) | Biblioteca comunitaria de skills para análisis de seguridad, defensa y pruebas autorizadas con Claude Code, Codex y otros agentes. | Sin API de IA en la ruta básica |
| [impeccable](../fichas/impeccable.md) | Guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio. | Sin API de IA en la ruta básica |
| [Marketing Skills](../fichas/marketingskills.md) | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. | Sin API de IA en la ruta básica |
| [ppt-master](../fichas/ppt-master.md) | Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos. | Sin API de IA en la ruta básica |
| [Remotion Agent Skills](../fichas/skills-remotion.md) | Skills oficiales de Remotion para que tu agente de código cree videos con React. | Sin API de IA en la ruta básica |
| [taste-skill](../fichas/taste-skill.md) | Skills "anti-slop" para producir frontends premium (layout, tipografía, motion y espaciado) más skills de generación de imagen para crear mood boards de referencia. | Sin API de IA en la ruta básica |

La revisión de documentación no equivale a una instalación probada. Consulta cada ficha para acceso, coste, equipo y pasos de arranque.
