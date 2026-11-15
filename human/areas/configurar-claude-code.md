[Áreas](../areas.md) · [Inicio](../README.md)

# Configuración de Claude Code

Prepara Claude Code, elige plugins y conecta herramientas para trabajar con un proyecto real.

28 repos únicos · 7 subcategorías. [Ver en el explorador](../../docs/index.html#/area/configurar-claude-code).

## Primera configuración, paso a paso

1. **Prepara el cliente.** Abre la fuente oficial de Claude Code, elige la instalación para tu sistema y comprueba el acceso de tu cuenta antes de añadir extensiones.
2. **Prueba un proyecto pequeño.** Abre una carpeta de prueba y pide al agente que explique un archivo. Confirma qué permisos solicita y que puedes revisar los cambios.
3. **Añade una mejora concreta.** Elige una sola skill o conexión de las subcategorías. Abre su ficha, lee la fuente y sigue la instalación indicada para este cliente.
4. **Comprueba el resultado y el consumo.** Repite la tarea pequeña, revisa si la mejora ayuda y consulta el uso de tu cuenta. Los servicios externos tienen sus propios accesos y costes.

[Fuente oficial del cliente](https://github.com/anthropics/claude-code#readme)

Esta colección reúne clientes, extensiones y material para configurar el agente. Cada ficha distingue su forma de uso. La compatibilidad con skills o MCP no implica que tu plan pague todas las APIs de las aplicaciones que construyas.

## Opciones para empezar

[Claude Code](../fichas/claude-code.md), [Claude Code Plugins Directory](../fichas/claude-plugins-official.md), [superpowers](../fichas/superpowers.md)

Son opciones para comparar. No es necesario instalar todas.

## Subcategorías

### Instalación y primeros pasos

Cliente oficial y selección inicial de herramientas.

[Explorar 1 repos](../../docs/index.html#/explorar?area=configurar-claude-code&topic=claude-inicio)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [Claude Code](../fichas/claude-code.md) | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. | API de IA opcional |

### Skills, plugins y métodos

Añadir instrucciones y un método de trabajo sin cargar todo el catálogo.

[Explorar 6 repos](../../docs/index.html#/explorar?area=configurar-claude-code&topic=claude-skills)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [agent-toolkit](../fichas/agent-toolkit.md) | Conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documentación y planificación. | Sin API de IA en la ruta básica |
| [Agentic Awesome Skills](../fichas/antigravity-awesome-skills.md) | Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con instalador npx y MCP local. | Sin API de IA en la ruta básica |
| [Anthropic Skills](../fichas/anthropic-skills.md) | Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills. | Sin API de IA en la ruta básica |
| [Claude Code Plugins Directory](../fichas/claude-plugins-official.md) | Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code. | Sin API de IA en la ruta básica |
| [SuperClaude_Framework](../fichas/superclaude-framework.md) | Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code. | Sin API de IA en la ruta básica |
| [superpowers](../fichas/superpowers.md) | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. | Sin API de IA en la ruta básica |

### MCP y navegador

Conectar documentación, repositorios y herramientas de navegador.

[Explorar 5 repos](../../docs/index.html#/explorar?area=configurar-claude-code&topic=claude-mcp)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [Chrome DevTools MCP](../fichas/chrome-devtools-mcp.md) | Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. | Sin API de IA en la ruta básica |
| [Context7](../fichas/context7.md) | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. | Sin API de IA en la ruta básica |
| [GitHub MCP Server](../fichas/github-mcp-server.md) | Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código. | Sin API de IA en la ruta básica |
| [Playwright MCP](../fichas/playwright-mcp.md) | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. | Sin API de IA en la ruta básica |
| [Serena](../fichas/serena.md) | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. | Sin API de IA en la ruta básica |

### Memoria y uso del contexto

Conservar decisiones y revisar el contexto de las sesiones.

[Explorar 6 repos](../../docs/index.html#/explorar?area=configurar-claude-code&topic=claude-memoria)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [claude-mem](../fichas/claude-mem.md) | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. | API de IA opcional |
| [claude-token-efficient](../fichas/claude-token-efficient.md) | Instrucciones para reducir la verbosidad de Claude Code y medir el coste de respuestas y contexto. | Sin API de IA en la ruta básica |
| [Engram](../fichas/engram.md) | Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. | Sin API de IA en la ruta básica |
| [headroom](../fichas/headroom.md) | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | API de IA opcional |
| [mempalace](../fichas/mempalace.md) | Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos. | Sin API de IA en la ruta básica |
| [rtk](../fichas/rtk.md) | Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. | API de IA opcional |

### Hooks y automatización de sesiones

Material de consulta con ejemplos de hooks y controles de Claude Code. Revisa cada ejemplo antes de adaptarlo.

[Explorar 1 repos](../../docs/index.html#/explorar?area=configurar-claude-code&topic=claude-hooks)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [claude-code-hooks-mastery](../fichas/claude-code-hooks-mastery.md) | Ejemplos y material para aprender a configurar hooks de Claude Code y ejecutar comprobaciones en su flujo de trabajo. | Sin API de IA en la ruta básica |

### Consumo y proveedores

Herramientas auxiliares para observar uso y estudiar el enrutamiento. No son una ampliación de tu plan.

[Explorar 2 repos](../../docs/index.html#/explorar?area=configurar-claude-code&topic=claude-consumo)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [claude-code-router](../fichas/claude-code-router.md) | Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local. | Depende de la ruta elegida |
| [Claude-Code-Usage-Monitor](../fichas/claude-code-usage-monitor.md) | Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible. | Sin API de IA en la ruta básica |

### Diseño, marketing y producción

Skills de oficio documentadas para Claude Code.

[Explorar 7 repos](../../docs/index.html#/explorar?area=configurar-claude-code&topic=claude-especialidades)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [Creative Architect](../fichas/creative-architect.md) | Plugin de dirección de arte para Claude Code: prepara fotos de producto, UGC y anuncios con proveedores de imagen o video. | API de IA opcional |
| [Cybersecurity Skills (comunidad)](../fichas/cybersecurity-skills.md) | Biblioteca comunitaria de skills para análisis de seguridad, defensa y pruebas autorizadas con Claude Code, Codex y otros agentes. | Sin API de IA en la ruta básica |
| [impeccable](../fichas/impeccable.md) | Guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio. | Sin API de IA en la ruta básica |
| [Marketing Skills](../fichas/marketingskills.md) | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. | Sin API de IA en la ruta básica |
| [Remotion Agent Skills](../fichas/skills-remotion.md) | Skills oficiales de Remotion para que tu agente de código cree videos con React. | Sin API de IA en la ruta básica |
| [scientific-agent-skills](../fichas/scientific-agent-skills.md) | Colección de skills y recursos para que agentes realicen tareas de investigación científica con herramientas de dominio. | Sin API de IA en la ruta básica |
| [taste-skill](../fichas/taste-skill.md) | Skills "anti-slop" para producir frontends premium (layout, tipografía, motion y espaciado) más skills de generación de imagen para crear mood boards de referencia. | Sin API de IA en la ruta básica |

## Fuentes de compatibilidad

- [claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery/blob/main/README.md), revisado el 2026-11-14.
- [Claude-Code-Usage-Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor/blob/main/README.md), revisado el 2026-11-14.
- [claude-code-router](https://github.com/musistudio/claude-code-router/blob/main/README.md), revisado el 2026-11-14.

La revisión de documentación no equivale a una instalación probada. Consulta cada ficha para acceso, coste, equipo y pasos de arranque.
