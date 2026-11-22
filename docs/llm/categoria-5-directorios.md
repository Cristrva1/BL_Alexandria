# Alexandría para agentes · Directorios, clientes y aprendizaje

Categoría 5 «Conectar herramientas con MCP» › subcategoría `directorios`. 5 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=5&sub=directorios · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `public-apis` | Directorio masivo y muy popular que lista por categorías miles de APIs públicas… | 1 Básico | 73 | MIT (OSI permisiva) | sin grupo |
| `awesome-mcp-servers` | Directorio curado de la comunidad que cataloga por categorías cientos de… | 1 Básico | 67 | MIT (OSI permisiva) | sin grupo |
| `mcp-for-beginners` | Curso abierto de Microsoft para aprender MCP con ejemplos en .NET, Java… | 1 Básico | 62 | MIT (OSI permisiva) | sin grupo |
| `awesome-mcp-clients` | Lista curada de clientes que soportan Model Context Protocol: apps, IDEs y… | 1 Básico | 42 | MIT (OSI permisiva) | sin grupo |
| `mcp` | Directorio de servidores MCP oficiales de Google, ejemplos y orientación para… | 1 Básico | 42 | Apache-2.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### public-apis (`public-apis`)

- **Repo:** https://github.com/public-apis/public-apis · MIT · nivel 1 · 73/100
- **Qué es:** Lista colectiva de APIs gratuitas para software y desarrollo web. Licencia MIT. Es uno de los repos más populares de GitHub (~499k estrellas) y está patrocinado por APILayer, cuyo anuncio encabeza el README.
- **Cuándo elegirlo:** Casos: Encontrar datos de clima para una demo; Comparar APIs públicas de geocodificación.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; necesidad concreta de datos; hardware prerequisites; API de IA: no; Navegador; necesidad concreta de datos.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/public-apis/public-apis/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Elige una API y verifica autenticación, HTTPS, límites y licencia en su sitio oficial Éxito: Sabes qué datos devuelve y si podrás usarlos en tu proyecto
- **Combina con:** `activepieces` [1/motores], `firecrawl` [4/crawlers], `claude-code` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Parte del contenido destacado es publicidad del patrocinador. El nombre CodeX de un compilador enlazado no es OpenAI Codex; no hereda compatibilidad con agentes.

### awesome-mcp-servers (`awesome-mcp-servers`)

- **Repo:** https://github.com/punkpeye/awesome-mcp-servers · MIT · nivel 1 · 67/100
- **Qué es:** Lista curada de servidores MCP de @punkpeye (vinculada a Glama). Licencia MIT. Es muy popular (~98k estrellas) y su README empieza con un anuncio.
- **Cuándo elegirlo:** Casos: Buscar una conexión a archivos propios; Encontrar un servidor para una base de datos.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; cliente y tarea elegidos; hardware prerequisites; API de IA: no; Navegador; cliente y tarea elegidos.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/punkpeye/awesome-mcp-servers/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Filtra por función y sistema operativo y contrasta el README de dos servidores Éxito: Tienes dos candidatos con transporte, permisos y credenciales identificados
- **Combina con:** `awesome-mcp-clients`, `servers` [5/servidores], `mcp-use` [5/sdk]
- **Riesgos y avisos:** Sin alternativas declaradas. Lista sin auditoría de seguridad. Es un directorio comunitario; sus enlaces y etiquetas no equivalen a una auditoría ni a compatibilidad uniforme.

### MCP for Beginners (`mcp-for-beginners`)

- **Repo:** https://github.com/microsoft/mcp-for-beginners · MIT · nivel 1 · 62/100
- **Qué es:** Curso de Microsoft para aprender Model Context Protocol con ejemplos prácticos en C#, Java, JavaScript, Rust, Python y TypeScript. Licencia MIT. Es popular (~18k estrellas, sin releases) y tiene más de 50 traducciones automáticas.
- **Cuándo elegirlo:** Casos: Aprender conceptos MCP desde cero; Comparar un servidor Python con otro TypeScript.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; lenguaje elegido para los ejercicios; hardware prerequisites; API de IA: no; Navegador; lenguaje elegido para los ejercicios.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/microsoft/mcp-for-beginners.git` — fuente: https://github.com/microsoft/mcp-for-beginners/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee la introducción y completa un ejercicio de herramienta con entrada y salida pequeñas Éxito: Puedes explicar el papel del host, cliente y servidor
- **Combina con:** `mcp-python-sdk` [5/sdk], `fastmcp` [5/sdk], `mcp-inspector` [5/sdk], `ai-agents-for-beginners` [19/guias], `generative-ai-for-beginners` [19/guias]
- **Riesgos y avisos:** Sin alternativas declaradas. No necesitas ejecutar todos los lenguajes ni desplegar todos los ejemplos para empezar.

### Awesome MCP Clients (`awesome-mcp-clients`)

- **Repo:** https://github.com/punkpeye/awesome-mcp-clients · MIT · nivel 1 · 42/100
- **Qué es:** Lista curada de clientes MCP de @punkpeye. Licencia MIT. Es pequeña (~7k estrellas) y poco activa (último cambio en junio de 2026); el propio README remite a glama.ai/mcp/clients para la lista más actual.
- **Cuándo elegirlo:** Casos: Encontrar una interfaz para herramientas MCP; Comparar clientes con modelos locales.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; preferencias de sistema y modelo; hardware prerequisites; API de IA: no; Navegador; preferencias de sistema y modelo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/punkpeye/awesome-mcp-clients/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Compara dos clientes por transportes MCP, autenticación y modelos admitidos Éxito: Puedes elegir un cliente cuyo sistema y conexiones encajen con tu caso
- **Combina con:** `awesome-mcp-servers`, `claude-code` [20/terminal], `cline` [20/editor]
- **Riesgos y avisos:** Sin alternativas declaradas. Posiblemente desactualizada frente a Glama. Un cliente descrito como basado en Claude Code no es necesariamente el producto oficial ni comparte sus condiciones.

### Google MCP (`mcp`)

- **Repo:** https://github.com/google/mcp · Apache-2.0 · nivel 1 · 42/100
- **Qué es:** Repositorio de Google con la lista de sus servidores MCP oficiales, guías para desplegar servidores en Google Cloud y ejemplos. Licencia Apache-2.0. Es pequeño (~5k estrellas) y su último cambio es de agosto de 2026.
- **Cuándo elegirlo:** Casos: Conectar un servicio Google a un agente; Aprender a alojar un servidor MCP en Cloud Run.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; servicio Google objetivo; hardware prerequisites; API de IA: no; Navegador; servicio Google objetivo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/google/mcp/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige un servidor oficial Google y consulta su autenticación antes de desplegar Éxito: Distingues servicio gestionado, ejemplo y despliegue en Cloud Run
- **Combina con:** `gemini-cli` [20/terminal], `mcp-use` [5/sdk], `mcp-inspector` [5/sdk]
- **Riesgos y avisos:** Sin alternativas declaradas. Cuidado con los permisos IAM que concedes a agentes. Este repositorio es google/mcp: catálogo y ejemplos Google, no el núcleo de la especificación Model Context Protocol.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-5-directorios.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Directorios, clientes y aprendizaje», lee `docs/alexandria/categoria-5-directorios.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-5-directorios.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
