
### 🎭 playwright-cli
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto. Resuelve el problema de los árboles de accesibilidad y los JSON de herramientas que inflan el prompt en cada turno.
**Por qué destaca:** alternativa token-eficiente a Playwright MCP, pensada para agentes de código (Claude Code, Cursor, Codex) que necesitan tocar la web sin quemar contexto. Procede del propio ecosistema Playwright de Microsoft, lo que garantiza compatibilidad con su API de automatización.
**Cómo funciona:** envuelve los comandos de Playwright en un CLI que el agente invoca paso a paso (navegar, clickar, leer), devolviendo salidas compactas en lugar de volcar el DOM o el accessibility tree enteros en cada turno.
**Instalación:** parte del ecosistema Playwright; se usa vía `npx playwright`/`npm` dentro del agente de código. Requiere Node.js y los binarios de navegador (`npx playwright install`).
**Casos:** que un agente automatice el browser de forma token-eficiente · alternativa a Playwright MCP cuando el contexto aprieta · flujos de login/scraping guiados por un agente de código.
**Stack:** TypeScript/Node.js, CLI — **Modelo/API:** agentes de código (Claude Code, Cursor, Codex); no requiere un LLM propio.
**Elige si:** tu agente vive en CLI y el contexto es un recurso caro — **Evita si:** necesitas estado persistente entre sesiones o un servidor MCP con recursos expuestos (usa Playwright MCP).
**Combina con:** [playwright](#-playwright) · [browser-use](#-browser-use)
**Repo:** [GitHub](https://github.com/microsoft/playwright)

### 🌐 browser-use
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** biblioteca Python que da a los LLMs la capacidad de usar navegadores reales con interfaz para modelos de visión, dejando que el agente perciba la pantalla y actúe sin selectores fijos. Resuelve la fragilidad del scraping basado en CSS: el agente "ve" la página como un humano y decide la siguiente acción.
**Por qué destaca:** uno de los proyectos de agentes-web más virales y populares, por permitir automatización robusta guiada por modelos multimodales incluso ante pop-ups y cambios de layout. Su adopción masiva y la opción de cloud gestionado lo consolidan como referencia en navegación agentica.
**Cómo funciona:** controla el navegador con Playwright, extrae el estado de la página (DOM simplificado + capturas) y lo pasa a un LLM con visión que devuelve la siguiente acción de click/escritura/navegación, repitiendo el bucle hasta cumplir el objetivo.
**Instalación:** `pip install browser-use` y `playwright install`; requiere clave de un LLM con visión (OpenAI, Anthropic o Google). Para escala/stealth existe cloud gestionado.
**Casos:** agente que entra a un e-commerce, filtra y compra · recuperación ante pop-ups/errores y CAPTCHAs suaves · flujos multi-paso donde los selectores cambian entre visitas.
**Stack:** Python 3.11+, Rust (core), Playwright — **Modelo/API:** multimodales con visión (GPT-4o, Claude, Gemini); agnóstico vía variables de entorno.
**Elige si:** quieres navegación como humano y tolerancia a cambios de UI — **Evita si:** necesitas scripts deterministas y baratos ([playwright](#-playwright)) o no quieres depender de un LLM por paso.
**Combina con:** [playwright](#-playwright) · [gpt-researcher](#-gpt-researcher)
**Repo:** [GitHub](https://github.com/browser-use/browser-use)

### 📸 instaloader
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram. Resuelve el archivado masivo de Instagram sin recurrir a APIs oficiales de pago ni herramientas manuales.
**Por qué destaca:** utilidad veterana y muy usada para archivar Instagram, con CLI lista para usar y soporte de descargas incrementales y sesiones logueadas. Su madurez y mantenimiento continuo la convierten en la opción de facto para este caso concreto.
**Cómo funciona:** consulta los endpoints públicos de Instagram (o autenticados con sesión) y guarda los medios con su metadata en JSON, respetando la estructura del perfil y permitiendo reanudar descargas sin duplicar.
**Instalación:** `pip install instaloader`; se usa como CLI (`instaloader perfil`) o importando el módulo. Para contenido privado o límites altos hace falta iniciar sesión con una cuenta de Instagram.
**Casos:** archivar contenido de perfiles · datasets de medios sociales · backups incrementales de stories y posts de un creador.
**Stack:** Python — **Modelo/API:** N/A.
**Limitaciones:** depende del frontend no oficial de Instagram, así que cambios en la app o el endurecimiento de sus ToS pueden romperlo; el uso masoso puede derivar en bloqueos de cuenta.
**Elige si:** necesitas datos de Instagram de forma fiable — **Evita si:** quieres varias redes a la vez ([snscrape](#-snscrape)) o el contenido requiere API oficial por ToS.
**Combina con:** [snscrape](#-snscrape)
**Repo:** [GitHub](https://github.com/instaloader/instaloader)

### 🐦 snscrape
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** scraper de redes sociales (Twitter/X, Reddit, Telegram, Instagram, etc.) que recolecta posts y perfiles sin necesidad de APIs oficiales ni claves. Resuelve la recolección histórica de datos sociales cuando las APIs de pago no son viables o no existen.
**Por qué destaca:** referencia clásica para datasets sociales históricos sin pagar API, con CLI y librería Python en el mismo paquete. Su fiabilidad depende de los cambios y restricciones de cada plataforma, pero sigue siendo el punto de partida habitual para investigación de medios sociales.
**Cómo funciona:** raspa los endpoints y páginas públicas de cada red, devolviendo los resultados como objetos o JSON desde CLI o como librería, con soporte de rangos de fechas y paginación.
**Instalación:** `pip install snscrape` (o desde el repo para la versión de desarrollo, que suele ir por delante de PyPI). Algunas redes requieren sesión o cookies para funcionar.
**Casos:** recolectar posts/tweets para análisis · datasets sociales históricos · alimentar pipelines de investigación con datos públicos.
**Stack:** Python — **Modelo/API:** N/A.
**Limitaciones:** muy sensible a cambios de frontend y bloqueos de cada plataforma (Twitter/X endureció el acceso); revisa los ToS antes de usarlo a escala, pues varias redes lo prohíben.
**Elige si:** recolectas varias redes y no te sirve una API oficial — **Evita si:** solo necesitas Instagram ([instaloader](#-instaloader)) o la plataforma ya bloqueó el acceso no oficial.
**Combina con:** [instaloader](#-instaloader)
**Repo:** [GitHub](https://github.com/JustAnotherArchivist/snscrape)

---

## 5. MCP & Conectividad

Servidores y clientes Model Context Protocol, y catálogos de APIs para conectar herramientas.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Elige si… | Setup |
|---|---|---|---|---|
| [mcp](#-mcp) | Spec y SDKs oficiales del protocolo MCP | 📚 | Trabajas con el estándar MCP directamente | 🟡 |
| [mcp-use](#-mcp-use) | Framework fullstack para apps/servidores MCP | 📚 | Construyes tu propio servidor/app MCP | 🟡 |
| [servers](#-servers) | Servidores MCP de referencia oficiales | 📂 | Quieres ejemplos canónicos para aprender | 🟡 |
| [awesome-mcp-servers](#-awesome-mcp-servers) | Directorio curado de servidores MCP | 📂 | Buscas un servidor ya hecho antes de construir | 🟢 |
| [mcp-neo4j](#-mcp-neo4j) | Servidores MCP oficiales para grafos Neo4j | 🧩 | Conectas grafos Neo4j a un asistente | 🟡 |
| [n8n-mcp](#-n8n-mcp) | MCP que expone los 1.845 nodos de n8n | 🧩 | Quieres que la IA arme flujos n8n sin errores | 🟡 |
| [public-apis](#-public-apis) | Directorio de miles de APIs públicas | 📂 | Buscas fuentes de datos externas para tu app | 🟢 |

### ⚖️ ¿Cuál elegir? — Crear vs. descubrir MCP

| Repo | Para qué | Evítalo si… |
|---|---|---|
| **mcp** | El SDK/spec base si programas a bajo nivel | Prefieres un framework de alto nivel que abstraiga el protocolo |
| **mcp-use** | Framework para pasar de prueba a app MCP desplegable | Solo quieres consumir un servidor ya hecho, no construir uno |
| **servers** | Implementaciones de referencia mantenidas por el steering group | Buscas algo listo para producción (son demos educativas) |
| **awesome-mcp-servers** | Buscar antes de construir: ¿ya existe el servidor que necesito? | Ya sabes que necesitas uno a medida y no te vale ninguno listado |

### 🧩 mcp
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** núcleo del Model Context Protocol (spec y SDKs oficiales) para que herramientas, datos y clientes de IA interoperen bajo un mismo estándar abierto. Resuelve la fragmentación: cada integración de IA dejaba de ser ad-hoc y pasa a hablar un protocolo común.
**Por qué destaca:** es el protocolo de referencia del ecosistema, adoptado por Claude, Cursor, ChatGPT y muchos otros clientes, lo que lo convierte en la base sobre la que se construye todo lo demás. Su respaldo por Anthropic y la gobernanza abierta le dan tracción real frente a alternativas propietarias.
**Cómo funciona:** define el protocolo MCP (mensajes JSON-RPC 2.0 entre cliente y servidor sobre stdio o HTTP/SSE) y ofrece SDKs en TypeScript y Python para implementar servidores que exponen tools, resources y prompts conformes.
**Instalación:** `npm install @modelcontextprotocol/sdk` o `pip install mcp` según el lenguaje; requiere un cliente MCP (Claude Desktop, Cursor, etc.) para conectar.
**Casos:** base de interoperabilidad para tu app de IA · construir servidores/clientes conforme al estándar · exponer herramientas internas a cualquier asistente compatible.
**Stack:** TypeScript/Python — **Modelo/API:** clientes MCP (Claude, Cursor, ChatGPT); agnóstico respecto al LLM.
**Elige si:** programas MCP a bajo nivel o necesitas conformidad estricta con la spec — **Evita si:** prefieres un framework de alto nivel que abstraiga el protocolo ([mcp-use](#-mcp-use)).
**Combina con:** [mcp-use](#-mcp-use) · [servers](#-servers)
**Repo:** [GitHub](https://github.com/modelcontextprotocol/modelcontextprotocol)

### 🛠️ mcp-use
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. Resuelve el salto del SDK base (verboso) a algo productivo: registro de tools, inspector y despliegue incluidos.
**Por qué destaca:** abstrae el protocolo en una capa de alto nivel con SDK, inspector y documentación, lo que acorta el camino de la idea a producción frente a usar el SDK base. Su enfoque fullstack (TS y Python) y la integración con clientes como ChatGPT/Claude le dan versatilidad.
**Cómo funciona:** envuelve el protocolo MCP exponiendo APIs de alto nivel para registrar tools/resources y conectar con clientes (Claude, ChatGPT), gestionando el ciclo de vida del servidor y el despliegue sin que toques JSON-RPC a mano.
**Instalación:** `npm install mcp-use` o `pip install mcp-use` según el stack; requiere un cliente MCP para probar el resultado.
**Casos:** exponer datos/herramientas internas vía MCP · pasar de local a app desplegable · prototipar un servidor con inspector antes de producción.
**Stack:** TypeScript o Python, React (apps) — **Modelo/API:** ChatGPT, Claude y agentes MCP; agnóstico vía variables de entorno.
**Elige si:** construyes un servidor MCP propio y quieres productividad — **Evita si:** solo buscas usar uno ya hecho ([awesome-mcp-servers](#-awesome-mcp-servers)) o necesitas control a nivel spec.
**Combina con:** [mcp](#-mcp) · [awesome-mcp-servers](#-awesome-mcp-servers) · receta [App MCP](#-8-construir-una-appservidor-mcp)
**Repo:** [GitHub](https://github.com/mcp-use/mcp-use)

### 📚 servers
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 directorio/recurso · Setup 🟡 medio
**Qué es:** colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad. Resuelve la falta de ejemplos canónicos: muestra cómo se construye un servidor MCP correcto, paso a paso.
**Por qué destaca:** es la fuente canónica y didáctica para entender cómo se construye un servidor MCP, respaldada por los mantenedores del propio protocolo. Incluye ejemplos prácticos (filesystem, fetch, git, etc.) que sirven de plantilla para los tuyos.
**Cómo funciona:** cada subdirectorio es un servidor MCP de ejemplo (filesystem, fetch, git…) que se ejecuta con `npx` y se conecta a un cliente compatible mediante el protocolo MCP sobre stdio o HTTP.
**Instalación:** ejecutar un servidor del repo con `npx` (p. ej. `npx -y @modelcontextprotocol/server-filesystem /ruta`) y añadirlo a la config del cliente MCP. Requiere Node.js para los servers TS.
**Casos:** aprender a construir un servidor MCP · plantillas para arrancar el tuyo · ejemplos educativos de features (tools, resources, prompts).
**Stack:** TypeScript/Python — **Modelo/API:** clientes MCP (Claude, Cursor, etc.); sin LLM propio.
**Elige si:** quieres ejemplos canónicos y plantillas fiables — **Evita si:** buscas soluciones listas para producción (son demos educativas, no hardening).
**Combina con:** [mcp-use](#-mcp-use) · [awesome-mcp-servers](#-awesome-mcp-servers)
**Repo:** [GitHub](https://github.com/modelcontextprotocol/servers)

### 🗂️ awesome-mcp-servers
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. Resuelve el "¿ya existe un servidor para X?" antes de que construyas el tuyo desde cero.
**Por qué destaca:** es uno de los listados de referencia más consultados del ecosistema MCP y ayuda a no reinventar servidores que ya existen. Su organización por categorías y su actualización continua lo hacen el punto de partida habitual para descubrir integraciones.
**Cómo funciona:** lista en Markdown con enlaces a cada servidor; eliges uno, sigues su README y lo añades a la config de tu cliente MCP (normalmente vía `npx` o `pip`).
**Instalación:** sin instalación propia; se consulta el README y luego se instala el servidor elegido (normalmente vía `npx` o `pip`) y se registra en el cliente MCP.
**Casos:** descubrir un servidor ya hecho antes de implementar uno · referencia rápida de integraciones por categoría · comparar alternativas para un mismo servicio.
**Stack:** Markdown — **Modelo/API:** cualquier cliente compatible con MCP (Claude, Cursor, ChatGPT).
**Elige si:** buscas antes de construir — **Evita si:** ya sabes que necesitas uno a medida y no te vale ninguno listado.
**Combina con:** [mcp-use](#-mcp-use) · [servers](#-servers)
**Repo:** [GitHub](https://github.com/punkpeye/awesome-mcp-servers)

### 🕸️ mcp-neo4j
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con soporte de despliegue en cloud. Resuelve el acceso natural a grafos desde un LLM: el asistente consulta y escribe Cypher sin que tú escribas el glue a mano.
**Por qué destaca:** lo mantiene el equipo Field GenAI de Neo4j Labs y viene contenedorizado y listo para HTTP, lo que facilita llevar grafos a producción con IA. Al ser oficial, sigue el ritmo de las versiones de Neo4j y del propio protocolo MCP.
**Cómo funciona:** expone consultas Cypher y operaciones sobre el grafo (lectura/escritura, esquema) como tools MCP que el cliente invoca mediante el protocolo, devolviendo resultados estructurados al LLM.
**Instalación:** `pip install mcp-neo4j-cypher` (o imagen Docker) y registrar el servidor en la config del cliente MCP. Requiere una instancia Neo4j accesible (local o Aura cloud) con credenciales.
**Casos:** consultar/escribir grafos Neo4j desde un asistente · backends de conocimiento basados en grafo · exploración de datos relacionales por lenguaje natural.
**Stack:** Python, Docker — **Modelo/API:** clientes MCP (Claude, Cursor, etc.); Neo4j como backend.
**Elige si:** usas Neo4j con IA y quieres que el asistente hable Cypher — **Evita si:** no trabajas con grafos o tu base es relacional pura.
**Combina con:** [graphrag](#-graphrag) · [awesome-mcp-servers](#-awesome-mcp-servers)
**Repo:** [GitHub](https://github.com/neo4j-contrib/mcp-neo4j)

### 🔌 n8n-mcp
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** servidor MCP que expone a la IA la documentación y los esquemas de los más de 1.845 nodos de n8n (816 core + 1.029 comunitarios) para ayudar a construir y depurar flujos. Resuelve el problema de que un LLM invente parámetros de nodos que no existen y genere workflows rotos.
**Por qué destaca:** reduce drásticamente los errores cuando se pide a una IA que arme un workflow de n8n, al darle acceso fiable a los parámetros reales de cada nodo. Su enfoque de "documentación como herramienta MCP" es un patrón replicable para otras plataformas.
**Cómo funciona:** el cliente MCP (Claude, Cursor, Gemini CLI) invoca tools del servidor para consultar nodos, propiedades y ejemplos vía el protocolo MCP; el LLM recibe esquemas exactos en lugar de alucinarlos.
**Instalación:** `npx n8n-mcp` y añadirlo a la config del cliente MCP (p. ej. Claude Desktop). Requiere Node.js y, para flujos reales, una instancia n8n accesible.
**Casos:** que Claude investigue parámetros del nodo de Gmail para armar un flujo · reducir errores al construir workflows · onboarding de IA al catálogo de nodos de n8n.
**Stack:** Node.js/TypeScript, MCP — **Modelo/API:** Claude Desktop/Code, Cursor, Gemini CLI; agnóstico vía MCP.
**Elige si:** generas flujos n8n con IA y quieres menos alucinaciones de parámetros — **Evita si:** no usas n8n o construyes los flujos a mano.
**Combina con:** [n8n](#-n8n) · [n8n-skills](#-n8n-skills) · receta [Bot WhatsApp](#-1-bot-de-whatsapp-con-ia)
**Repo:** [GitHub](https://github.com/czlonkowski/n8n-mcp)

### 🌍 public-apis
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyectos. Resuelve el descubrimiento: en un solo lugar tienes URLs, autenticación y HTTPS de cada API en lugar de buscarlas una a una.
**Por qué destaca:** es una de las referencias más estrelladas de GitHub para encontrar fuentes de datos externas, mantenida por la comunidad y APILayer. Su organización temática y su antigüedad lo convierten en el catálogo de facto para este caso.
**Cómo funciona:** tabla en Markdown organizada por temática con la URL, tipo de autenticación (apiKey, OAuth, ninguno) y nivel de HTTPS de cada API; se navega y se consume cada API según su propia documentación.
**Instalación:** sin instalación; se navega el README (o su versión web) y se consume cada API según su propia documentación y claves.
**Casos:** conectar fuentes externas de datos · encontrar una API para un proyecto · explorar categorías (geocoding, finanzas, weather) antes de decidir stack.
**Stack:** Markdown — **Modelo/API:** N/A (catálogo; cada API define la suya).
**Elige si:** buscas datos externos y no sabes qué API usar — **Evita si:** ya tienes tus fuentes definidas o necesitas SLA empresarial (son APIs públicas, sin garantías).
**Combina con:** [n8n](#-n8n) · [firecrawl](#-firecrawl)
**Repo:** [GitHub](https://github.com/public-apis/public-apis)

---

## 6. Memoria, LLM Ops & Observabilidad

Memoria persistente de agentes, gateways de modelos, trazas/evaluación y logging.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Elige si… | Setup |
|---|---|---|---|---|
| [mem0](#-mem0) | Capa de memoria persistente para agentes | 📚 | Quieres memoria estándar con integraciones amplias | 🟢 |
| [agentmemory](#-agentmemory) | Memoria multi-cliente para agentes de código | 📚 | Tu agente debe recordar entre sesiones y clientes | 🟢 |
| [mempalace](#-mempalace) | Memoria local-first verbatim | 📚 | Quieres memoria sin llamadas a API (privacidad) | 🟢 |
| [turbovec](#-turbovec) | Búsqueda vectorial rápida (TurboQuant) | 📚 | Necesitas vector search embebido eficiente | 🟢 |
| [litellm](#-litellm) | Gateway unificado a 100+ LLMs | 📚 | Cambias de proveedor sin tocar código | 🟢 |
| [langfuse](#-langfuse) | Observabilidad/trazas de LLM | ⚙️ | Quieres ver y evaluar tus llamadas LLM | 🟡 |
| [llmfit](#-llmfit) | Evaluación/ajuste de LLMs | 📚 | Mides calidad/fit de modelos con datos | 🟢 |
| [headroom](#-headroom) | Compactación de contexto | 📚 | Te quedas sin ventana de contexto | 🟢 |
| [sandbox](#-sandbox) | Sandbox all-in-one para agentes | ⚙️ | Necesitas browser+terminal+VSCode+MCP aislados | 🟡 |
| [loguru](#-loguru) | Logging simple para Python | 📚 | Quieres logs limpios sin boilerplate | 🟢 |

### ⚖️ ¿Cuál elegir? — Memoria de agentes

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **mem0** | Memoria estándar para apps/agentes | Popular, integraciones amplias, SDK en Python y TS | Necesitas todo local sin llamadas a API |
| **agentmemory** | Agentes de código que re-explican todo | Recuerdo entre sesiones, memoria multi-cliente vía MCP | Te basta la memoria nativa de un único cliente |
| **mempalace** | Privacidad total, sin API | Verbatim, alto recall, zero API calls | Quieres un SaaS gestionado con escalado automático |
| **turbovec** | Capa de recuperación vectorial embebida | Rapidez (TurboQuant) en Python/Rust, bajo coste de memoria | Ya usas una vector DB completa con persistencia |

### 🧠 mem0
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. Resuelve el "amnesia" del LLM: el agente conserva preferencias y hechos entre sesiones sin reenviar todo el historial.
**Por qué destaca:** es uno de los proyectos de memoria de agentes más adoptados, con SDK estable en Python y TS e integraciones amplias en el ecosistema de frameworks (LangChain, CrewAI, etc.). Su enfoque de extracción+actualización incremental de hechos evita duplicados y desactualizaciones.
**Cómo funciona:** combina extracción de hechos vía LLM con almacenamiento en vector DBs (Qdrant, Chroma, etc.) para indexar y consultar memorias relevantes por similitud, actualizando o borrando recuerdos contradictorios en lugar de solo acumularlos.
**Instalación:** `pip install mem0ai` (también SDK en npm) o servicio gestionado; requiere un LLM y una vector DB configurados (o los defaults del cloud).
**Casos:** recordar preferencias del usuario entre sesiones · memoria long-term para agentes · personalización acumulativa sin inflar el prompt.
**Stack:** Python/TypeScript, vector DBs (Qdrant, Chroma, pgvector) — **Modelo/API:** múltiples LLMs + vector DBs; agnóstico vía variables de entorno.
**Elige si:** quieres memoria estándar lista con integraciones amplias — **Evita si:** necesitas todo local sin llamadas a API ([mempalace](#-mempalace)) o control total del almacenamiento.
**Combina con:** [crewAI](#-crewai) · [langchain](#-langchain) · [agentmemory](#-agentmemory)
**Repo:** [GitHub](https://github.com/mem0ai/mem0)

### 💾 agentmemory
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. Resuelve el "re-explica todo" al cambiar de asistente: la memoria vive fuera del cliente.
**Por qué destaca:** evita re-explicar el contexto al cambiar de asistente, ofreciendo una memoria compartida poco común entre herramientas de coding. Su exposición vía MCP la hace compatible con cualquier cliente que hable el protocolo, no solo uno concreto.
**Cómo funciona:** se conecta vía MCP para que distintos clientes lean y escriban en el mismo almacén persistente del motor iii, manteniendo el contexto de proyecto/sesión al margen del IDE que uses en cada momento.
**Instalación:** instalación del servidor MCP según el repo y configuración en cada cliente compatible (Claude Code, Cursor, etc.); requiere el motor iii como backend.
**Casos:** que el agente "recuerde todo" y no re-expliques el contexto · memoria multi-cliente vía MCP · continuidad de proyecto entre Claude Code y Cursor.
**Stack:** motor iii, MCP — **Modelo/API:** cualquier cliente MCP; sin LLM propio.
**Elige si:** cambias de asistente y quieres una memoria común entre ellos — **Evita si:** te basta la memoria nativa de un único cliente o no usas MCP.
**Combina con:** [mem0](#-mem0) · [ruflo](#-ruflo)
**Repo:** [GitHub](https://github.com/rohitg00/agentmemory)

### 🏛️ mempalace
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos. Resuelve la memoria privada: cero llamadas a API, tus textos no salen de tu máquina.
**Por qué destaca:** prioriza la privacidad total (cero llamadas a API) reportando recall competitivo en benchmarks de memoria de largo plazo. Su diseño verbatim evita la pérdida de detalle que sufren los enfoques que resumen con un LLM remoto.
**Cómo funciona:** guarda los textos verbatim y los recupera mediante un backend de búsqueda conectable, sin depender de un LLM remoto para almacenar ni para indexar; el backend se puede cambiar según tus necesidades.
**Instalación:** `pip install` desde PyPI; se configura el backend de búsqueda local según el repo. No requiere claves de API ni servicios externos.
**Casos:** memoria privada para agentes · recuerdo de largo plazo sin enviar datos a la nube · casos con requisitos de confidencialidad (sanidad, legal).
**Stack:** Python (PyPI) — **Modelo/API:** local, backend conectable; sin proveedor LLM obligatorio.
**Elige si:** la privacidad es prioridad y no quieres llamadas a API — **Evita si:** quieres un SaaS gestionado con escalado automático o integraciones de framework ya hechas ([mem0](#-mem0)).
**Combina con:** [open-notebook](#-open-notebook) · [odysseus](#-odysseus)
**Repo:** [GitHub](https://github.com/MemPalace/mempalace)

### ⚡ turbovec
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida. Resuelve el coste de memoria y cómputo de la búsqueda vectorial cuando una vector DB completa es demasiado para tu escala.
**Por qué destaca:** apuesta por la eficiencia, aplicando una técnica de cuantización moderna para acelerar la búsqueda con bajo coste de memoria. Sus bindings en Python y Rust la hacen usable desde ambos ecosistemas sin cambiar de stack.
**Cómo funciona:** comprime los vectores con TurboQuant y resuelve las consultas por similitud directamente sobre la representación cuantizada, con bindings disponibles en Python y Rust para integrarse en pipelines existentes.
**Instalación:** `pip install` (Python) o crate de Rust según el repo; sin servicios externos ni GPU obligatoria para inferencia.
**Casos:** capa de recuperación para RAG · vector search eficiente embebido · sustituto ligero de una vector DB cuando no necesitas persistencia distribuida.
**Stack:** Python / Rust — **Modelo/API:** N/A (infra de vectores).
**Elige si:** necesitas vector search veloz y embebido sin desplegar una DB — **Evita si:** ya usas una vector DB completa con persistencia y escalado horizontal.
**Combina con:** [mem0](#-mem0) · [graphrag](#-graphrag)
**Repo:** [GitHub](https://github.com/RyanCodrai/turbovec)

### 🔀 litellm
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. Resuelve el lock-in: cambias de proveedor o añades fallback sin reescribir el código de tu app.
**Por qué destaca:** es un estándar de facto para abstraer proveedores, muy adoptado por su routing, control de costos, reintentos y fallback entre modelos. Su amplia cobertura (OpenAI, Anthropic, Google, Bedrock, locales vía Ollama/vLLM) lo hace casi ubicuo en stacks multi-modelo.
**Cómo funciona:** traduce cada petición al formato del proveedor destino y puede correr como proxy/gateway (modo servidor) con balanceo, reintentos, budget tracking y registro de uso, además de como librería embebida.
**Instalación:** `pip install litellm` (o despliegue del proxy vía Docker); requiere las claves de los proveedores que uses vía variables de entorno.
**Casos:** probar varios modelos sin reescribir código · balancear costo/fallback entre proveedores · centralizar control de costos y rate limits.
**Stack:** Python — **Modelo/API:** OpenAI, Anthropic, Google, Bedrock, Azure, locales (Ollama, vLLM), etc.
**Elige si:** trabajas con múltiples modelos o quieres fallback/control de costos — **Evita si:** usas un único proveedor fijo y no necesitas abstracción.
**Combina con:** [langchain](#-langchain) · [langfuse](#-langfuse) · [llm-council](#-llm-council)
**Repo:** [GitHub](https://github.com/BerriAI/litellm)

### 📡 langfuse
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. Resuelve la opacidad: ves qué prompt, qué modelo, qué coste y qué salida tuvo cada paso de tu pipeline.
**Por qué destaca:** es una de las plataformas de LLM observability de referencia, con self-host y cloud e integraciones con los frameworks más usados (LangChain, OpenAI SDK, LiteLLM, CrewAI). Su soporte de OpenTelemetry la hace compatible con instrumentación existente.
**Cómo funciona:** instrumentas tu app con sus SDKs (o vía OpenTelemetry) para enviar trazas, costos y evaluaciones a un backend con UI de análisis, permitiendo seguir el árbol completo de una petición de agente paso a paso.
**Instalación:** Docker Compose para self-host (Postgres + backend + frontend) o cuenta cloud; SDKs vía `pip`/`npm`. El self-host requiere mantener PostgreSQL.
**Casos:** ver el detalle de cada llamada/agente · evaluar prompts y medir costos · depurar flujos multi-paso de agentes.
**Stack:** TypeScript, Docker, PostgreSQL, self-host/cloud — **Modelo/API:** SDKs para múltiples frameworks; agnóstico respecto al LLM.
**Elige si:** operas agentes en serio y necesitas trazas/costes/eval — **Evita si:** haces prototipos triviales o no quieres operar el backend.
**Combina con:** [langchain](#-langchain) · [litellm](#-litellm) · [ag2](#-ag2)
**Repo:** [GitHub](https://github.com/langfuse/langfuse)

### 📏 llmfit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** herramienta para evaluar y medir el "fit" y la calidad de LLMs en una tarea concreta, orientada a comparar modelos con datos. Resuelve la elección subjetiva de modelo: la conviertes en un flujo objetivo y reproducible con métricas.
**Por qué destaca:** proyecto enfocado y de nicho, útil para llevar la elección de modelo a un flujo automatizable en CI en lugar de "probar a ojo". Su integración con pipelines de evaluación lo hace apto para comparaciones sistemáticas.
**Cómo funciona:** ejecuta evaluaciones sobre las salidas de varios modelos frente a un dataset de prueba y reporta métricas de calidad, integrable en pipelines de integración continua para bloquear regresiones.
**Instalación:** instalación según el repo (binario Go o paquete Python); requiere claves de los modelos a comparar y un dataset de evaluación.
**Casos:** comparar modelos para una tarea · CI de calidad de prompts/modelos · bloquear deploys si un modelo regresa en métricas.
**Stack:** Go/Python — **Modelo/API:** múltiples LLMs; agnóstico vía variables de entorno.
**Elige si:** necesitas elegir modelo con datos y reproducibilidad — **Evita si:** ya tienes el modelo decidido o tu caso no justifica un harness de evaluación.
**Combina con:** [litellm](#-litellm) · [langfuse](#-langfuse)
**Repo:** [GitHub](https://github.com/AlexsJones/llmfit)

### 🗜️ headroom
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. Resuelve el dolor habitual de los agentes: quedarse sin ventana de contexto a mitad de una tarea larga.
**Por qué destaca:** proyecto pequeño y específico que ataca un problema real de los agentes de forma directa y agnóstica al proveedor. Su enfoque de "maximizar señal por token" encaja en pipelines donde el contexto crece sin control.
**Cómo funciona:** resume y condensa el contexto entrante para maximizar la señal por token antes de pasarlo al modelo, de forma agnóstica al proveedor, preservando las partes relevantes y descartando ruido.
**Instalación:** instalación según el repo (`pip`/`npm`); requiere un LLM para la condensación (o modo local si lo soporta).
**Casos:** resumir/condensar contexto largo · ganar espacio en la ventana · mantener conversaciones largas dentro del límite de tokens.
**Stack:** Python/TypeScript — **Modelo/API:** agnóstico vía variables de entorno.
**Elige si:** te quedas sin contexto en sesiones largas — **Evita si:** tus prompts ya caben holgados o la pérdida de detalle por resumen es inaceptable.
**Combina con:** [Context-Engineering](#-context-engineering) · [codegraph](#-codegraph)
**Repo:** [GitHub](https://github.com/chopratejas/headroom)

### 📦 sandbox
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. Resuelve el riesgo de dejar que un agente toque tu host: todo corre contenido en un contenedor reproducible.
**Por qué destaca:** concentra en un solo contenedor todas las herramientas que un agente necesita, ofreciendo un entorno reproducible y aislado poco común. Su exposición vía web y MCP lo hace accesible desde cualquier cliente compatible sin configurar cada pieza por separado.
**Cómo funciona:** levanta un contenedor con los servicios (browser, shell, editor, notebooks) expuestos vía web y conectables por clientes MCP, aislando la ejecución del host y limitando el alcance de las acciones del agente.
**Instalación:** `docker run` de la imagen del proyecto; requiere Docker y recursos suficientes para correr navegador + servicios en paralelo.
**Casos:** ejecutar agentes de forma aislada · entorno reproducible para tareas dev · probar agentes que manipulan archivos/terminal sin riesgo al host.
**Stack:** Docker, web, MCP — **Modelo/API:** clientes MCP; sin LLM propio.
**Elige si:** quieres aislar la ejecución de agentes y reproducibilidad — **Evita si:** te basta correr local sin sandbox o no puedes asumir el overhead de Docker.
**Combina con:** [OpenHands](#-openhands) · [ECC](#-ecc)
**Repo:** [GitHub](https://github.com/agent-infra/sandbox)

### 📝 loguru
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa. Resuelve la fricción del módulo `logging` stdlib, que exige boilerplate para algo tan básico como imprimir logs legibles.
**Por qué destaca:** es una de las librerías de logging más populares en Python por su API mínima (un único objeto `logger`) y su gran ergonomía frente al módulo estándar. Su salida con colores, rotación y captura de excepciones en una sola línea la hace ubicua en scripts y pipelines.
**Cómo funciona:** expone un único objeto `logger` preconfigurado con rotación, retención, formato enriquecido (colores, timestamps) y captura de excepciones con traceback en una sola llamada, sin necesidad de handlers ni formatters.
**Instalación:** `pip install loguru`; sin configuración previa, `from loguru import logger` y a usar.
**Casos:** logs legibles sin configuración · instrumentar pipelines y scripts · captura de excepciones con contexto sin boilerplate.
**Stack:** Python — **Modelo/API:** N/A.
**Elige si:** quieres logging fácil y legible en Python sin pelear con stdlib — **Evita si:** ya usas el stdlib `logging` configurado o tienes un stack de observabilidad corporativo.
**Combina con:** cualquier pipeline Python · [litellm](#-litellm)
**Repo:** [GitHub](https://github.com/Delgan/loguru)

---

## 7. Inteligencia de Código, Datos & Entrenamiento

Indexar/mapear repos, grafos de conocimiento, ciencia de datos y entrenar modelos desde cero.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Elige si… | Setup |
|---|---|---|---|---|
| [codegraph](#-codegraph) | Índice semántico de código local | 🧩 | Quieres que la IA entienda repos grandes barato | 🟢 |
| [graphify](#-graphify) | Grafo de conocimiento de proyecto | 🧩 | Visualizas relaciones de código/PDF/imagen | 🟡 |
| [graphrag](#-graphrag) | RAG basado en grafos (Microsoft) | 📚 | Necesitas recuperación contextual por grafo | 🟡 |
| [GitNexus](#-gitnexus) | Exploración visual de repos Git | 🖥️ | Navegas y entiendes un repo concreto visualmente | 🟢 |
| [DeepSeek-Coder](#-deepseek-coder) | Modelo de código open-source | 🧩 | Generas/revisas código con modelo propio | 🔴 |
| [nanoGPT](#-nanogpt) | GPT mínimo entrenable (Karpathy) | 📚 | Aprendes/entrenas un GPT desde cero | 🟡 |
| [nanochat](#-nanochat) | ChatGPT mínimo full-stack (Karpathy) | 📚 | Entrenas un chat end-to-end didáctico | 🟡 |
| [llm.c](#-llmc) | Entrenamiento de LLM en C/CUDA puro | 📚 | Quieres entrenar sin frameworks pesados | 🔴 |
| [how-to-train-your-gpt](#-how-to-train-your-gpt) | Guía para entrenar un GPT | 📂 | Buscas un tutorial práctico paso a paso | 🟢 |
| [cosmos](#-cosmos) | World foundation models de NVIDIA | 🧩 | Generas mundos/datos para IA física | 🔴 |
| [data-science-ipython-notebooks](#-data-science-ipython-notebooks) | Notebooks de ciencia de datos | 📂 | Aprendes/consultas DS y ML con ejemplos | 🟢 |
| [awesome-bigdata](#-awesome-bigdata) | Directorio de big data | 📂 | Buscas herramientas de datos a escala | 🟢 |
| [openai-python](#-openai-python) | SDK oficial de OpenAI | 📚 | Llamas a la API de OpenAI desde Python | 🟢 |

### ⚖️ ¿Cuál elegir? — Entender código vs. grafos

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **codegraph** | Reducir lectura/tokens en repos grandes | 100% local, ahorra tool calls en repos enormes | Tu base de código es pequeña y no justifica el índice |
| **graphify** | Auditoría/onboarding visual | HTML interactivo + reporte + JSON exportable | Solo necesitas índice textual barato |
| **graphrag** | Recuperación contextual avanzada | RAG sobre grafo de conocimiento (Microsoft) | Un RAG simple por fragmentos te basta |
| **GitNexus** | Explorar un repo Git concreto | Navegación visual e ideas sobre el repo | Necesitas indexar muchos repos a escala |

### ⚖️ ¿Cuál elegir? — Entrenar desde cero (didáctico)

| Repo | Nivel | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **nanoGPT** | Intro a entrenar GPT | Minimalista y claro (Karpathy) | Quieres el pipeline completo de chat, no solo el core |
| **nanochat** | Chat full-stack mínimo | Pipeline completo de un ChatGPT (pretrain→SFT→serve) | Solo te interesa el core del modelo |
| **llm.c** | Bajo nivel C/CUDA | Sin frameworks, máximo control y visibilidad | No tienes GPU ni CUDA, o prefieres PyTorch |
| **how-to-train-your-gpt** | Tutorial guiado | Paso a paso explicado | Prefieres solo el código sin guía narrada |

### 📊 codegraph
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟢 fácil
**Qué es:** CLI que indexa tu código y da a los asistentes de IA inteligencia semántica 100% local, permitiéndoles entender la estructura y el flujo de un repo sin leer archivo por archivo ni gastar llamadas a herramientas. Resuelve el coste de contexto de los agentes en repos grandes.
**Por qué destaca:** convierte repos enormes en algo navegable para la IA con coste casi nulo; muy valorado en flujos de agentes de código por su ahorro real de tokens y tool calls. Su acoplamiento con Claude Code, Gemini y Cursor sin modelo propio lo hace fácil de adoptar.
**Cómo funciona:** construye un índice semántico local del repositorio (símbolos, referencias, flujo) que el asistente consulta vía comandos; se acopla a Claude Code, Gemini y Cursor sin necesidad de un modelo propio ni de enviar código a la nube.
**Instalación:** `npm install -g codegraph` (binario autónomo de Node.js) y luego `codegraph index .`. Requiere Node.js; el índice se regenera al cambiar el código.
**Casos:** `codegraph index .` para que el asistente entienda el flujo sin leer archivo por archivo · onboarding de IA en monorepos grandes · reducir tool calls en revisiones de código.
**Stack:** JavaScript/Node.js (binario autónomo) — **Modelo/API:** no requiere IA; se acopla a Claude Code, Gemini, Cursor.
**Elige si:** trabajas repos grandes y el contexto del agente es caro — **Evita si:** tu base de código es pequeña y no justifica mantener un índice.
**Combina con:** [graphify](#-graphify) · [headroom](#-headroom) · receta [Análisis de repos](#-5-análisis-de-repos-grandes)
**Repo:** [GitHub](https://github.com/colbymchenry/codegraph)

### 🕸️ graphify
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** generador de grafos de conocimiento para proyectos locales que mapea código, PDFs, imágenes y video en diagramas interactivos, revelando cómo se conectan las piezas de un sistema. Resuelve el onboarding visual: un índice textual no basta cuando hay relaciones entre archivos.
**Por qué destaca:** combina visualización navegable, reporte legible y datos exportables en un solo paso, ideal para auditorías y onboarding cuando un índice de texto no basta. Su soporte multi-fuente (código + documentos + multimedia) lo diferencia de los indexadores puramente de código.
**Cómo funciona:** analiza las fuentes del proyecto y produce un grafo con nodos y relaciones; opcionalmente usa un LLM (cloud o local) para enriquecer el análisis semántico y generar descripciones de cada nodo.
**Instalación:** `pipx install graphify` o `uv tool install graphify`, luego `/graphify .` sobre el proyecto. Requiere Python 3.10+; el enriquecimiento con LLM necesita claves de API.
**Casos:** `/graphify .` para mapear llamadas de funciones · auditoría rápida de un sistema · onboarding visual de un proyecto heredado.
**Stack:** Python 3.10+, uv/pipx — **Modelo/API:** opcional (OpenAI/Anthropic o locales Llama/Mistral); agnóstico vía variables de entorno.
**Elige si:** quieres ver conexiones visualmente o auditar un sistema — **Evita si:** solo necesitas índice textual barato ([codegraph](#-codegraph)) o tu proyecto es trivial.
**Combina con:** [codegraph](#-codegraph) · [graphrag](#-graphrag)
**Repo:** [GitHub](https://github.com/safishamsi/graphify)

### 🔗 graphrag
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. Resuelve las preguntas que requieren conectar entidades dispersas en muchos documentos, donde el RAG clásico falla.
**Por qué destaca:** proyecto de Microsoft Research muy difundido que mejora las respuestas en preguntas que requieren conectar entidades dispersas en muchos documentos. Su enfoque de resumen por comunidades y recuperación local+global es un patrón de referencia en RAG avanzado.
**Cómo funciona:** un LLM extrae entidades y relaciones para construir el grafo, lo resume por comunidades con un LLM y luego responde combinando recuperación local (entidades concretas) y global (temas del corpus) con embeddings.
**Instalación:** `pip install graphrag` y luego `graphrag index` / `graphrag query` sobre tu corpus. Requiere claves de un LLM y embeddings; el indexado consume bastantes llamadas.
**Casos:** preguntas complejas sobre un corpus · recuperación que entiende relaciones · análisis temático de colecciones grandes de documentos.
**Stack:** Python — **Modelo/API:** múltiples LLMs + embeddings (OpenAI, Azure, locales); configurable vía settings.yaml.
**Elige si:** tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto — **Evita si:** un RAG simple basta o el coste de indexado con LLM es prohibitivo.
**Combina con:** [graphify](#-graphify) · [mcp-neo4j](#-mcp-neo4j) · [turbovec](#-turbovec)
**Repo:** [GitHub](https://github.com/microsoft/graphrag)

### 🧭 GitNexus
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟢 fácil
**Qué es:** herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. Resuelve el "llegar a un proyecto ajeno y no saber por dónde empezar": lo navegas y lo discutes en vez de leer ficheros sueltos.
**Por qué destaca:** facilita comprender un repo concreto de forma interactiva en vez de leer ficheros sueltos, útil cuando llegas a un proyecto ajeno. Su interfaz web con LLM integrado permite hacer preguntas y sugerir ideas sobre el código.
**Cómo funciona:** una interfaz web (TypeScript) recorre el repositorio y lo presenta como vistas navegables, apoyándose en LLMs para responder preguntas y sugerir ideas sobre la estructura y el flujo del proyecto.
**Instalación:** `git clone https://github.com/abhigyanpatwari/GitNexus` y arranque del front web según el README; requiere Node.js y una clave de LLM para las preguntas.
**Casos:** onboarding en un repo nuevo · navegar relaciones y discutir ideas · entender la arquitectura de un proyecto heredado.
**Stack:** web/TypeScript — **Modelo/API:** múltiples LLMs; configurable vía variables de entorno.
**Elige si:** quieres entender un repo puntual de forma visual — **Evita si:** necesitas indexar muchos repos a escala ([codegraph](#-codegraph)) o no quieres front web.
**Combina con:** [codegraph](#-codegraph) · receta [Análisis de repos](#-5-análisis-de-repos-grandes)
**Repo:** [GitHub](https://github.com/abhigyanpatwari/GitNexus)

### 🧩 DeepSeek-Coder
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** familia de modelos open-source especializados en código, entrenados sobre grandes corpus de programación para generar, completar y revisar software. Resuelve la dependencia de APIs propietarias para tareas de código: puedes desplegar el modelo en tu propia infraestructura.
**Por qué destaca:** una de las alternativas abiertas más fuertes para tareas de código, competitiva con modelos propietarios y desplegable en local. Su publicación de pesos y su buena recepción en benchmarks de código la consolidan como referencia open en este nicho.
**Cómo funciona:** modelos transformer ejecutados con PyTorch sobre GPU; se cargan en local (p. ej. vía Hugging Face Transformers o vLLM) o se consumen por la API oficial de DeepSeek, con contextos largos aptos para repos.
**Instalación:** `pip install transformers torch` y descarga de pesos desde Hugging Face, o uso vía API de DeepSeek. El despliegue local requiere GPU con VRAM generosa según el tamaño del modelo.
**Casos:** generación y revisión de código · asistencia técnica con modelo propio · completado de código en entornos on-prem.
**Stack:** Python, PyTorch, GPU — **Modelo/API:** modelos DeepSeek (local vía HF/vLLM o API oficial).
**Limitaciones:** el despliegue local exige GPU potente (VRAM escala con el tamaño del modelo); los pesos grandes son lentos de descargar y de servir.
**Elige si:** quieres un modelo de código abierto y desplegable on-prem — **Evita si:** prefieres APIs comerciales gestionadas o no tienes GPU para servirlo.
**Combina con:** [litellm](#-litellm) · [codegraph](#-codegraph)
**Repo:** [GitHub](https://github.com/deepseek-ai/DeepSeek-Coder)

### 🔬 nanoGPT
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo. Resuelve la opacidad de los frameworks: ves exactamente cómo se entrena un GPT sin capas de abstracción.
**Por qué destaca:** referencia didáctica de Karpathy ampliamente usada para aprender cómo funciona realmente el entrenamiento de un GPT, sin capas de abstracción. Su minimalismo (unos pocos cientos de líneas) lo hace el punto de partida habitual para entender y experimentar.
**Cómo funciona:** define el modelo GPT y su bucle de entrenamiento en PyTorch sobre GPU, reproduciendo resultados tipo GPT-2 con unos pocos cientos de líneas y dependencias mínimas.
**Instalación:** `git clone https://github.com/karpathy/nanoGPT` y `pip install torch numpy transformers datasets tiktoken`. Requiere GPU para entrenar (CPU solo sirve para pruebas triviales).
**Casos:** aprender cómo se entrena un GPT · experimentos pequeños reproducibles · base para afinar modelos propios sobre datos propios.
**Stack:** Python, PyTorch, GPU — **Modelo/API:** entrena modelos propios.
**Limitaciones:** entrenar a escala real exige GPU y tiempo; no es una librería de producción, sino un recurso educativo minimalista.
**Elige si:** quieres entender el entrenamiento de un GPT desde cero — **Evita si:** solo consumes modelos vía API o necesitas un pipeline de chat completo ([nanochat](#-nanochat)).
**Combina con:** [nanochat](#-nanochat) · [llm.c](#-llmc)
**Repo:** [GitHub](https://github.com/karpathy/nanoGPT)

### 💬 nanochat
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible. Resuelve la pregunta "¿cómo se monta un asistente entero?": lo muestra en un solo repo compacto y legible.
**Por qué destaca:** referencia didáctica de Karpathy que muestra el ciclo completo de un asistente conversacional en un solo repo compacto y legible. Su encadenamiento pretrain → SFT → inferencia lo hace el complemento natural de nanoGPT para ver el flujo end-to-end.
**Cómo funciona:** encadena las etapas pretrain → SFT → inferencia en PyTorch sobre GPU, con scripts que entrenan y luego sirven el modelo de chat para que puedas interactuar con él.
**Instalación:** `git clone https://github.com/karpathy/nanochat` y seguir el script de entrenamiento del README (entorno PyTorch con GPU). Requiere GPU seria para entrenar y datos de preentrenamiento.
**Casos:** ver el ciclo completo (pretrain→SFT→chat) · base educativa para entender un asistente entero · punto de partida para experimentos de fine-tuning.
**Stack:** Python, PyTorch, GPU — **Modelo/API:** entrena modelos propios.
**Limitaciones:** entrenar de cero exige GPU y corpus; es educativo, no una alternativa a un modelo comercial servido.
**Elige si:** quieres el pipeline completo de un chat end-to-end — **Evita si:** solo necesitas el core del modelo ([nanoGPT](#-nanogpt)) o un modelo listo para usar.
**Combina con:** [nanoGPT](#-nanogpt)
**Repo:** [GitHub](https://github.com/karpathy/nanochat)

### ⚙️ llm.c
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🔴 pesado
**Qué es:** implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo. Resuelve la abstracción total: muestra qué hace realmente la GPU en cada pasada, sin ocultarlo tras un framework.
**Por qué destaca:** referencia didáctica de Karpathy que reproduce GPT-2 con dependencias mínimas, ideal para entender qué hace realmente la GPU bajo el capó. Su valor educativo sobre el cómputo de bajo nivel es difícil de igualar en otros recursos.
**Cómo funciona:** escribe a mano los kernels de las pasadas forward/backward en C y CUDA, gestionando memoria y operaciones que normalmente oculta un framework como PyTorch, reproduciendo el entrenamiento de GPT-2.
**Instalación:** `git clone https://github.com/karpathy/llm.c`, instalar CUDA toolkit y compilar con `make`. Requiere una GPU NVIDIA con CUDA; sin él no tiene sentido.
**Casos:** entrenar GPT-2 con mínima dependencia · entender el cómputo de bajo nivel · enseñar qué hace realmente un framework bajo el capó.
**Stack:** C, CUDA — **Modelo/API:** entrena modelos propios.
**Limitaciones:** exige GPU NVIDIA con CUDA y toolkit instalado; no es portable a otras arquitecturas y no busca ser productivo, sino pedagógico.
**Elige si:** quieres bajo nivel sin abstracciones y tienes GPU CUDA — **Evita si:** prefieres PyTorch ([nanoGPT](#-nanogpt)) o no tienes CUDA.
**Combina con:** [nanoGPT](#-nanogpt)
**Repo:** [GitHub](https://github.com/karpathy/llm.c)

### 📘 how-to-train-your-gpt
**Etiquetas:** Ejecución 🏠 local-first · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librería de producción. Resuelve el "quiero entenderlo con explicación narrada" frente al código desnudo de nanoGPT.
**Por qué destaca:** repo pequeño y poco conocido, útil como complemento explicado al entrenamiento; honestamente, es un material de aprendizaje modesto frente a referencias como nanoGPT. Su valor está en la narración guiada, no en la robustez del código.
**Cómo funciona:** recorre en Python el proceso de entrenar un GPT con explicaciones intercaladas, apoyándose en el ecosistema PyTorch para mostrar cada etapa de forma didáctica.
**Instalación:** `git clone https://github.com/raiyanyahya/how-to-train-your-gpt` y seguir las instrucciones del repositorio; requiere Python y PyTorch (GPU recomendada para entrenar).
**Casos:** seguir un paso a paso de entrenamiento · material de estudio para principiantes · complemento narrado a nanoGPT.
**Stack:** Python, PyTorch — **Modelo/API:** entrena modelos propios.
**Elige si:** quieres una guía explicada y narrada — **Evita si:** prefieres solo el código limpio ([nanoGPT](#-nanogpt)) o buscas algo productivo.
**Combina con:** [nanoGPT](#-nanogpt) · [nanochat](#-nanochat)
**Repo:** [GitHub](https://github.com/raiyanyahya/how-to-train-your-gpt)

### 🌌 cosmos
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots. Resuelve la escasez de datos físicos: genera escenas/vídeo sintético en lugar de capturarlos a mano.
**Por qué destaca:** iniciativa de NVIDIA con ecosistema y pesos publicados en Hugging Face, una referencia clave para la generación de datos de simulación física. Su procedencia (NVIDIA) y el respaldo de la comunidad de robótica le dan credibilidad en un nicho emergente.
**Cómo funciona:** ejecuta modelos generativos de mundo en Python sobre GPU para producir vídeo/escenas sintéticas que sirven como datos de entrenamiento o simulación para agentes físicos y robótica.
**Instalación:** `git clone https://github.com/NVIDIA/Cosmos`, instalar dependencias del repo y descargar pesos Cosmos desde Hugging Face. Requiere GPU potente (NVIDIA, CUDA) para inferencia y generación.
**Casos:** generar datos/mundos sintéticos · entrenar agentes físicos/robótica · simulación de escenas para entrenamiento.
**Stack:** Python, GPU (NVIDIA/CUDA) — **Modelo/API:** modelos Cosmos de NVIDIA.
**Limitaciones:** exige GPU de gama alta y descarga de pesos grandes; el dominio es muy específico (IA física), sin utilidad para tareas de texto/UI.
**Elige si:** trabajas IA física/robótica y necesitas datos sintéticos — **Evita si:** haces tareas de texto/UI o no tienes GPU para servirlo.
**Combina con:** [diffusers](#-diffusers)
**Repo:** [GitHub](https://github.com/NVIDIA/Cosmos)

### 📓 data-science-ipython-notebooks
**Etiquetas:** Ejecución 🏠 local-first · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** gran colección de notebooks de ciencia de datos y machine learning que cubre desde pandas y NumPy hasta deep learning y big data, con ejemplos listos para ejecutar. Resuelve el "aprender DS con ejemplos reales" sin tener que montarlos tú desde cero.
**Por qué destaca:** uno de los repositorios de referencia más populares para aprender DS de forma práctica, con material abundante y bien organizado por temas. Su antigüedad y su volumen de notebooks lo convierten en un clásico para consulta y estudio.
**Cómo funciona:** son notebooks Jupyter autocontenidos que se abren y ejecutan localmente, mostrando explicaciones y código sobre las librerías clásicas del ecosistema Python (pandas, NumPy, scikit-learn, etc.).
**Instalación:** `git clone https://github.com/donnemartin/data-science-ipython-notebooks` y abrir los notebooks con `jupyter lab` (o `jupyter notebook`). Requiere Python y las librerías de cada notebook.
**Casos:** aprender pandas/NumPy/ML · consultar ejemplos prácticos · material de referencia para clases o autoestudio.
**Stack:** Python, Jupyter — **Modelo/API:** N/A.
**Elige si:** estudias/consultas DS con ejemplos ejecutables — **Evita si:** buscas una librería, no ejemplos, o necesitas material actualizado a las versiones más recientes.
**Combina con:** [dash](#-dash) · [streamlit](#-streamlit)
**Repo:** [GitHub](https://github.com/donnemartin/data-science-ipython-notebooks)

### 🗄️ awesome-bigdata
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para descubrir el ecosistema de datos a escala. Resuelve el "qué uso para X a escala": un panorama del stack de datos grandes en un solo vistazo.
**Por qué destaca:** lista "awesome" ampliamente referenciada que ofrece un panorama completo del stack de datos grandes en un solo vistazo. Su organización por categorías (ingesta, almacenamiento, procesamiento, streaming) facilita comparar alternativas sin navegar decenas de sitios.
**Cómo funciona:** es un documento Markdown con enlaces clasificados por categoría; se consulta directamente en GitHub sin instalar nada, y cada enlace lleva al repo/docs de la herramienta.
**Instalación:** no requiere instalación; se navega online en el repositorio de GitHub y se elige la herramienta según tu caso.
**Casos:** elegir stack de datos a escala · descubrir herramientas por categoría · comparar alternativas de ingesta/almacenamiento/procesamiento.
**Stack:** Markdown — **Modelo/API:** N/A (catálogo).
**Elige si:** diseñas pipelines de datos grandes y necesitas descubrir el ecosistema — **Evita si:** tu proyecto es pequeño y no justifica herramientas de big data.
**Combina con:** [awesome-dataviz](#-awesome-dataviz)
**Repo:** [GitHub](https://github.com/oxnr/awesome-bigdata)

### 🐍 openai-python
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** SDK oficial de OpenAI para Python, que expone de forma tipada y cómoda la API (chat, embeddings, imágenes, audio, asistentes) y es la base habitual para apps que usan sus modelos. Resuelve el glue HTTP: no escribes peticiones a mano, usas clientes tipados con streaming.
**Por qué destaca:** cliente oficial y al día mantenido por OpenAI, con amplia adopción y soporte inmediato de las novedades de la API. Su tipado, streaming y soporte síncrono/async lo hacen la base de facto para integrar GPT en Python.
**Cómo funciona:** envuelve las peticiones HTTP a la API en clientes Python síncronos y asíncronos, con tipado, streaming de respuestas, reintentos y manejo de errores integrados.
**Instalación:** `pip install openai` y configurar `OPENAI_API_KEY` (variable de entorno). Requiere una cuenta OpenAI con clave válida y saldo.
**Casos:** llamar a la API de OpenAI · base para apps que usan GPT · consumir embeddings, imágenes y audio desde Python.
**Stack:** Python — **Modelo/API:** OpenAI (chat, embeddings, imágenes, audio).
**Elige si:** usas modelos de OpenAI desde Python y quieres el cliente oficial — **Evita si:** quieres abstracción multi-proveedor ([litellm](#-litellm)) o no usas OpenAI.
**Combina con:** [litellm](#-litellm) · [langchain](#-langchain)
**Repo:** [GitHub](https://github.com/openai/openai-python)
