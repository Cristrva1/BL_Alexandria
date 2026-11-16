# Alexandría para agentes · SDKs y frameworks para crear MCP

Categoría 5 «Conectar herramientas con MCP» › subcategoría `sdk`. 5 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=5&sub=sdk · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `fastmcp` | La forma rápida y pythónica de crear servidores y clientes MCP, con auth… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | recomendado |
| `mcp-inspector` | Herramienta oficial para probar y depurar servidores MCP desde una interfaz web. | 1 Básico | 69 | Apache-2.0 (en transición desde MIT) (OSI permisiva) | sin grupo |
| `mcp-use` | Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o… | 2 Intermedio | 64 | MIT (OSI permisiva) | recomendado |
| `mcp-python-sdk` | SDK oficial de Python para crear servidores y clientes del Model Context… | 2 Intermedio | 61 | MIT (OSI permisiva) | alternativa |
| `mcp-typescript-sdk` | SDK oficial de TypeScript para crear servidores y clientes del Model Context… | 2 Intermedio | 60 | Apache-2.0 (en transición desde MIT) (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### FastMCP (`fastmcp`)

- **Repo:** https://github.com/PrefectHQ/fastmcp · Apache-2.0 · nivel 2 · 74/100 · recomendado en «SDKs de MCP en Python»
- **Qué es:** Framework Python para construir servidores, clientes y aplicaciones interactivas del Model Context Protocol, hecho por Prefect. Licencia Apache-2.0.
- **Cuándo elegirlo:** Casos: Exponer una función de inventario como herramienta; Probar autenticación de un servidor propio.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python y uv; proyecto de prueba; hardware prerequisites; API de IA: no; Python y uv; proyecto de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `uv add fastmcp` — fuente: https://github.com/PrefectHQ/fastmcp/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Copia la herramienta add del ejemplo y solicita sumar dos números con un cliente MCP Éxito: La herramienta devuelve la suma esperada
- **Combina con:** `claude-code` [20/terminal], `mcp-inspector`, `pydantic-ai` [3/py]
- **Alternativas:** `mcp-python-sdk`
- **Riesgos y avisos:** Alternativas (elige una): mcp-python-sdk. Es un framework para construir servidores y clientes, no un servidor de negocio ya configurado.

### MCP Inspector (`mcp-inspector`)

- **Repo:** https://github.com/modelcontextprotocol/inspector · Apache-2.0 (en transición desde MIT) · nivel 1 · 69/100
- **Qué es:** Herramienta oficial para inspeccionar servidores del Model Context Protocol. El proyecto MCP está pasando de MIT a Apache-2.0 (GitHub muestra NOASSERTION). Es activa (~11k estrellas, 2.15.0).
- **Cuándo elegirlo:** Casos: Depurar un esquema MCP; Reproducir un fallo de una herramienta.
- **Requisitos:** nivel 1: preparación sencilla; Node ^22.23.4 o ^24.22.1 o >=26.12.1; servidor MCP de prueba; hardware prerequisites; API de IA: no; Node ^22.23.4 o ^24.22.1 o >=26.12.1; servidor MCP de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `npx @modelcontextprotocol/inspector                   # web UI (default)` — fuente: https://github.com/modelcontextprotocol/inspector/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta un servidor local, lista herramientas y llama una con datos ficticios Éxito: Puedes inspeccionar argumentos, respuesta y errores sin un agente de IA
- **Combina con:** `fastmcp`, `mcp-typescript-sdk`, `mcp-python-sdk`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Trata los secretos que guarda como credenciales. Las instrucciones CLAUDE.md del repositorio sirven para contribuir al código; no hacen del Inspector un plugin de Claude Code.

### mcp-use (`mcp-use`)

- **Repo:** https://github.com/mcp-use/mcp-use · MIT · nivel 2 · 64/100 · recomendado en «SDKs de MCP en TypeScript»
- **Qué es:** Framework TypeScript para construir, probar y publicar servidores MCP, plugins de ChatGPT y conectores de Claude, de mcp-use. Licencia MIT. Es activo (~11k estrellas, mcp-use@2.12.4).
- **Cuándo elegirlo:** Casos: Construir una herramienta con interfaz embebida; Desplegar un servidor MCP para una app propia.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node.js; plantilla elegida; Python solo para su ruta correspondiente; hardware prerequisites; API de IA: opcional; Node.js; plantilla elegida; Python solo para su ruta correspondiente.
- **Instalación (documentada en la fuente; no ejecutada):** `npx -y create-mcp-use-app@latest` — fuente: https://github.com/mcp-use/mcp-use/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Genera una app MCP de ejemplo y prueba su herramienta desde el inspector incluido Éxito: Puedes ver una respuesta y la interfaz asociada si el cliente admite MCP Apps
- **Combina con:** `claude-code` [20/terminal], `awesome-mcp-servers` [5/directorios], `mcp` [5/directorios], `servers` [5/servidores]
- **Alternativas:** `mcp-typescript-sdk`
- **Riesgos y avisos:** Alternativas (elige una): mcp-typescript-sdk. MCP Apps con widgets requiere capacidades del cliente adicionales a las de un servidor MCP de texto.

### MCP Python SDK (`mcp-python-sdk`)

- **Repo:** https://github.com/modelcontextprotocol/python-sdk · MIT · nivel 2 · 61/100 · alternativa en «SDKs de MCP en Python»
- **Qué es:** SDK oficial en Python del Model Context Protocol. Licencia MIT (el proyecto MCP está migrando a Apache-2.0). Es muy usado (~25k estrellas, v2.3.0).
- **Cuándo elegirlo:** Casos: Conectar una función Python a MCP; Servir un recurso de texto desde una aplicación.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python 3.11+; uv; directorio de proyecto; hardware prerequisites; API de IA: no; Python 3.11+; uv; directorio de proyecto.
- **Instalación (documentada en la fuente; no ejecutada):** `uv add "mcp[cli]"      # or: pip install "mcp[cli]"` — fuente: https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Implementa el servidor add del ejemplo y comprueba su esquema con Inspector Éxito: Una llamada con dos enteros devuelve su suma
- **Combina con:** `mcp-inspector`, `pydantic-ai` [3/py], `claude-code` [20/terminal], `mcp-for-beginners` [5/directorios]
- **Alternativas:** `fastmcp`
- **Riesgos y avisos:** Alternativas (elige una): fastmcp. La documentación revisada usa MCPServer y ofrece migración v2; no confundas este SDK con FastMCP independiente.

### MCP TypeScript SDK (`mcp-typescript-sdk`)

- **Repo:** https://github.com/modelcontextprotocol/typescript-sdk · Apache-2.0 (en transición desde MIT) · nivel 2 · 60/100 · alternativa en «SDKs de MCP en TypeScript»
- **Qué es:** SDK oficial en TypeScript del Model Context Protocol. La rama principal es la v2 estable (v2.4.0), que implementa la especificación MCP 2026-07-28.
- **Cuándo elegirlo:** Casos: Construir un servidor MCP en TypeScript; Crear un cliente que enumere herramientas.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Node.js; TypeScript; gestor de paquetes; hardware prerequisites; API de IA: no; Node.js; TypeScript; gestor de paquetes.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install @modelcontextprotocol/server` — fuente: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el ejemplo v2 para exponer una herramienta y llámala desde Inspector Éxito: Ves el esquema y una respuesta válida de la herramienta
- **Combina con:** `mcp-inspector`, `vercel-ai` [3/ts], `claude-code` [20/terminal]
- **Alternativas:** `mcp-use`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): mcp-use. La rama revisada es v2 con paquetes server y client separados; no mezcles imports de tutoriales v1.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-5-sdk.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «SDKs y frameworks para crear MCP», lee `docs/alexandria/categoria-5-sdk.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-5-sdk.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
