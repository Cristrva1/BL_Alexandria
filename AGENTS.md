# 🤖 AGENTS.md — Punto de entrada para agentes de IA

Esta biblioteca es un menú curado de repos de IA y automatización, con datos completos para cada uno. Este archivo te dice cómo elegir los repos correctos **gastando el mínimo de tokens**. Es corto, así que léelo entero y luego abre solo lo que necesites.

<!-- BL:STATS -->
**885 repos curados** · **13 áreas de trabajo** · **3 colecciones de configuración** · **103 subcategorías prácticas** · **32 categorías técnicas** · **117 subcategorías técnicas**
<!-- /BL:STATS -->

---

## ⚡ Protocolo de selección (en orden)

0. **Si el usuario describió un proyecto concreto**, genera primero su superguía:
   `uv run repo-intelligence recommend --project "<descripción, con la herramienta si la nombra>" --max-repos 7`
   (o `--project-file proyecto.md` para briefs largos). Después lee `ai_index/CONTEXT_PACKS/latest.md`: ya trae finalistas, orden e instalación.
1. **Lee `INDICE_IA.json`**, el índice compacto con una entrada por repo. Es la única lectura obligatoria.
2. **Empieza por `discovery.areas`** si el usuario nombra un campo (frontend, ciberseguridad, audiovisual, trading) o quiere configurar Claude Code, Codex o Antigravity. Cada área tiene subcategorías con `selectors` (`cat`/`subs`), `repos` explícitos y, cuando aplica, `reference_repos` de consulta. La unión por id evita duplicados. Después filtra por `goals`, `routes`, `cat`/`sub`, `tags`, `role`, `setup` y `one`. `pick: true` es una selección editorial, no una garantía de adecuación.
3. **Desempata** con `alt`: si ya elegiste un repo, **descarta sus `alt`**, porque cumplen la misma función.
4. **Parte de una receta** (`recipes`) si el usuario quiere un producto completo y no una pieza suelta.
5. **Solo para finalistas (menos de 8)**, abre su entrada en `INDICE_IA.detalle.json`: `access` separa API,Claude Code,Codex,Antigravity,modelos locales,coste y equipo; `getting_started` trae preparación,pasos y entrada con fuente. `first_try` indica acción y resultado observable, `practical_examples` escenarios ilustrativos y `editorial_review` el alcance documental. No confundas revisión de fuentes con instalación o ejecución probada.

**Prioridad de audiencia:** personas sin experiencia técnica que necesitan pasos guiados. Explica términos, ofrece dos o tres opciones y una primera prueba pequeña. En el explorador, empieza por **Guíame**. Para CLI, añade `--route codex`, `--route claude`, `--route local_model` o `--route no_api` cuando la persona especifique acceso. No confundas `--tool` (ayuda para construir) con `--route` (acceso de la herramienta elegida).

> Coste: los pasos 1 a 4 son un solo archivo. No leas `Guia.md` ni `Catalogo.md` enteros; son para humanos.

---

## 🗺️ Archivos

| Archivo | Para qué | Cuándo |
|---|---|---|
| **`AGENTS.md`** (este) | Cómo navegar | Siempre, primero |
| **`INDICE_IA.json`** | Índice compacto: id, cat, sub, role, exec, setup, mcp, prov, tags, stars, pick, one, alt | Para preseleccionar |
| **`INDICE_IA.detalle.json`** | Ficha completa por `id` | Solo finalistas |
| `ai_index/CONTEXT_PACKS/latest.md` | Última superguía generada por `recommend` | Si ya hay un proyecto descrito |
| `menu_portable/REPO_MENU.md` | Menú autocontenido para copiar a otro proyecto | Al trabajar fuera de este repo |
| `human/categorias/NN-*.md` | Categoría completa en formato humano | Lectura humana |
| `web/index.html` | Catálogo educativo con curso, salas y recetas | `uv run repo-intelligence web serve` |
| `docs/index.html` | El mismo explorador, portable y sin servidor | Descargar ZIP, extraer y abrir en navegador |
| `human/rutas.md`, `human/formas-de-uso.md` | Entradas por tarea y acceso | Orientación inicial |
| `human/acceso.md`, `human/instalar.md`, `human/vocabulario.md` | Cuentas, primer uso y términos | Personas que empiezan |
| `PRODUCT.md` | Público y propósito confirmados | Al cambiar navegación o interfaz |
| `data/techniques.json` → `human/TECNICAS.md` | Técnicas, ideas, reglas y sitios útiles con fuente pública | Al pedir buenas prácticas de trabajo con agentes |
| `data/retired.json` | Repos retirados por archivados, abandonados, sustituidos o inactivos, con sustitutos | Antes de proponer o reincorporar un repo |
| `human/areas.md`, `human/areas/*.md` | Áreas prácticas, subcategorías y configuración de asistentes | Para orientarse por campo o herramienta |

---

## 🧠 Regla clave: herramienta de código ≠ modelo en ejecución

- **El agente que ayuda a construir o instalar** puede trabajar con muchos repos. Esa ayuda no acredita que su suscripción ejecute la aplicación.
- **El acceso en ejecución** se decide con `access`, que distingue sesión oficial, instrucciones dentro del agente, MCP e integración documentada por un tercero. Consulta fuentes y fecha antes de afirmar compatibilidad o coste.
- `exec: local` describe dónde se ejecuta software, no dónde se ejecuta su modelo. `prov: []` significa "no declarado"; no demuestra ausencia de costes. Algunas suscripciones ofrecen créditos de API bajo condiciones propias; sesión y API siguen siendo rutas distintas.

<!-- BL:AGENT_TOOLS -->
| Herramienta | Repos específicos que le sirven |
|---|---|
| **Claude Code** | `claude-code`, `anthropic-skills`, `claude-plugins-official`, `superpowers`, `awesome-claude-code`, `awesome-claude-skills`, `claude-mem`, `geo-seo-claude`, `agency-agents` — Skills en .claude/skills y plugins con /plugin marketplace. |
| **Codex** | `codex`, `agent-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`, `spec-kit`, `marketingskills`, `taste-skill` — Lee AGENTS.md y skills portables (formato Agent Skills). |
| **Antigravity** | `antigravity-awesome-skills`, `awesome-agent-skills`, `prompt-master`, `stitch-skills` |
| **Gemini CLI** | `gemini-cli`, `awesome-agent-skills`, `antigravity-awesome-skills`, `stitch-skills` |
| **OpenCode** | `opencode`, `awesome-agent-skills`, `antigravity-awesome-skills`, `prompt-master` |
| **Grok** | Sin repos específicos: úsalo como proveedor LLM en runtime (los repos agnósticos lo aceptan vía API compatible con OpenAI). |
| **DeepSeek** | `deepseek-v3` — Es el modelo; el resto es agnóstico vía proveedor compatible con OpenAI. |
<!-- /BL:AGENT_TOOLS -->

---

## 📂 Áreas prácticas e índice técnico

La entrada humana es [Categorías y subcategorías](human/areas.md): áreas de trabajo y colecciones de configuración, con una sola ficha por proyecto. Un recurso puede aparecer en varios temas. Las colecciones de asistentes son para configurar el cliente; no equivalen al filtro de acceso por suscripción.

Las secciones técnicas siguientes conservan sus números y rutas. La lógica compartida `core/taxonomy.py` comprueba selectores, referencias y cobertura completa al generar guías, web y menú portable. Una incorporación nueva debe quedar cubierta por al menos un área de trabajo.

<!-- BL:AGENT_CATEGORIES -->
| # | Categoría | Repos | Subcategorías | Archivo |
|---:|---|---:|---|---|
| 1 | 🤖 Automatizar procesos y crear herramientas internas | 17 | Motores de workflow y automatización, Apps internas y bases de datos no-code | `human/categorias/01-automatizaci-n-mensajer-a-crm.md` |
| 2 | 🧠 Skills, plugins y métodos para agentes | 30 | Catálogos y marketplaces de skills, Metodologías y harness para agentes de código | `human/categorias/02-skills-prompts-gu-as-de-agente.md` |
| 3 | 🕸️ Construir agentes y coordinar equipos de IA | 34 | Frameworks de agentes en Python, Frameworks en TypeScript y multi-lenguaje, Builders visuales y plataformas de agentes, Simulación, evolución y debate entre modelos | `human/categorias/03-frameworks-orquestaci-n-de-agentes.md` |
| 4 | 🕷️ Buscar, extraer y monitorear información web | 28 | Crawlers y extracción para IA, Scraping guiado por LLM, Búsqueda, monitoreo y research web, Redes sociales y descarga de medios | `human/categorias/04-scraping-b-squeda-research-web.md` |
| 5 | 🔌 Conectar herramientas con MCP | 25 | SDKs y frameworks para crear MCP, Servidores MCP destacados, Directorios, clientes y aprendizaje | `human/categorias/05-mcp-conectividad.md` |
| 6 | 🧬 Memoria, RAG y búsqueda de conocimiento | 28 | Memoria persistente para agentes, RAG y motores de conocimiento, Bases vectoriales y búsqueda semántica | `human/categorias/06-memoria-rag-llm-ops.md` |
| 7 | 🧑‍💻 Entender código y comprobar su calidad | 20 | Entender y empaquetar código para agentes, Calidad, seguridad y benchmarks de código, CLIs y SDKs de desarrollo | `human/categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md` |
| 8 | 🏠 Chats, modelos locales y espacios privados | 31 | Motores para correr modelos en local, Interfaces de chat auto-hospedadas, Workspaces privados y segundos cerebros, NotebookLM: alternativas y clientes | `human/categorias/08-ia-local-modelos-chats-workspaces.md` |
| 9 | 🎨 Diseñar y construir interfaces web | 32 | Componentes, iconos y sistemas de diseño, CSS y estilos, Diseño visual, canvas y builders, UI generada con IA y frontends para agentes | `human/categorias/09-dise-o-ui-frontend.md` |
| 10 | 📊 Dashboards, analítica y mapas | 31 | Analítica web y de producto, BI, dashboards y chat con datos, Librerías de gráficos, Recursos y casos de uso, Inteligencia de fuentes abiertas y mapas, Fotogrametría y mapas desde imágenes | `human/categorias/10-anal-tica-visualizaci-n.md` |
| 11 | 🖼️ Generar y editar imágenes con IA | 10 | Interfaces para generar imágenes, Modelos, librerías y control, Restauración, upscaling y edición | `human/categorias/11-generaci-n-de-imagen-visi-n.md` |
| 12 | 🎬 Editar, grabar y generar video | 19 | Edición, grabación y subtítulos, Video generativo y pipelines automáticos | `human/categorias/12-audio-voz-video.md` |
| 13 | 📄 PDF, OCR y procesamiento de documentos | 22 | Conversión de documentos para IA, OCR, Herramientas PDF, Gestión y archivo de documentos | `human/categorias/13-documentos-presentaciones.md` |
| 14 | 📈 Investigar finanzas y mercados | 23 | Agentes de investigación financiera, Modelos y backtesting cuantitativo, Bots y conexiones a exchanges, Ejemplos y aprendizaje | `human/categorias/14-investigar-finanzas-y-mercados.md` |
| 15 | 🗂️ Organizar notas, archivos y servicios personales | 48 | Notas, bóvedas y conocimiento personal, Sincronización y gestión de archivos, Credenciales y privacidad, Libros, podcasts y bibliotecas personales, Automatización del hogar, Herramientas y organización personal, Aprendizaje asistido | `human/categorias/15-notas-archivos-y-servicios-personales.md` |
| 16 | 🔍 Analizar software y comprobar su seguridad | 113 | Ingeniería inversa y formatos binarios, Depuración e inspección de procesos, Tráfico, rendimiento y pruebas, Reconocimiento y superficie de ataque, Explotación, C2 y post-explotación, Active Directory y red interna, Detección, SIEM e IDS, Nube, contenedores e IaC, Análisis y pruebas con agentes, Protección y verificación de software, Directorios y aprendizaje, Skills de análisis y seguridad, Respuesta a incidentes y forense, Inteligencia de amenazas | `human/categorias/16-analisis-de-software-y-seguridad.md` |
| 17 | 🤖 WhatsApp, mensajería y chatbots | 16 | WhatsApp y mensajería, Chatbots y asistentes conversacionales, Comunidades,chat y llamadas | `human/categorias/17-mensajeria-chatbots.md` |
| 18 | 🤖 CRM, ventas y marketing | 17 | CRM, ERP y soporte al cliente, Email, marketing y notificaciones, Reservas y programación de citas | `human/categorias/18-crm-ventas-marketing.md` |
| 19 | 🧠 Aprender IA y escribir mejores prompts | 31 | Prompts y prompt engineering, Guías, cursos y cookbooks, Aprender LLMs desde cero | `human/categorias/19-aprender-ia-prompts.md` |
| 20 | 🕸️ Programar con agentes de código | 21 | Agentes de terminal, Editores y extensiones de código, Agentes para issues y tareas de ingeniería, Interfaces para gestionar sesiones | `human/categorias/20-agentes-de-codigo.md` |
| 21 | 🕸️ Asistentes e investigación con agentes | 17 | Asistentes autónomos y equipos de agentes, Agentes de research autónomo | `human/categorias/21-asistentes-investigacion.md` |
| 22 | 🕸️ Infraestructura, despliegue y herramientas para agentes | 26 | Infraestructura: sandboxes, herramientas y protocolos, Dominios y recursos de infraestructura, Redes y transporte, Alojamiento y backend | `human/categorias/22-infraestructura-despliegue.md` |
| 23 | 🧬 Operar, evaluar y medir modelos de IA | 26 | Serving y gateways de LLM, Ahorro de contexto y tokens, Observabilidad, evaluación y guardrails | `human/categorias/23-operacion-evaluacion-modelos.md` |
| 24 | 🧑‍💻 Modelos abiertos y entrenamiento | 25 | Entrenar y afinar modelos, Modelos abiertos y fundacionales | `human/categorias/24-modelos-entrenamiento.md` |
| 25 | 🧑‍💻 Procesar datos y trabajar con notebooks | 23 | Datos y notebooks, Apps de datos en Python | `human/categorias/25-datos-notebooks.md` |
| 26 | 🎨 Animación, gráficos y creación 3D | 28 | Animación y 3D, Creación, renderizado y animación 3D, Física y simulación | `human/categorias/26-animacion-graficos-3d.md` |
| 27 | 🎨 Skills de diseño, contenido y especialidades | 36 | Skills de diseño para agentes, Escritura y calidad de texto, Skills de dominio: marketing, SEO y negocio | `human/categorias/27-skills-especializadas.md` |
| 28 | 🖼️ Visión artificial, rostros y percepción | 21 | Rostros y retratos animados, Visión por computador | `human/categorias/28-vision-percepcion.md` |
| 29 | 🎬 Audio, transcripción, voz y música | 33 | Transcripción (voz a texto), Síntesis y clonación de voz, Agentes de voz en tiempo real, Música y audio generativo, Procesamiento y limpieza de audio | `human/categorias/29-audio-voz-musica.md` |
| 30 | 🎬 Video con código y agentes creativos | 23 | Motores de video y escenas por código, Skills y métodos de producción audiovisual, Aplicaciones y flujos de producción | `human/categorias/30-video-codigo-agentes.md` |
| 31 | 📄 Presentaciones, diagramas y explicación visual | 12 | Presentaciones, Diagramas y documentación | `human/categorias/31-presentaciones-diagramas.md` |
| 32 | 🕷️ Navegadores y automatización web | 19 | Automatización y pruebas por código, Herramientas de navegación para agentes, Navegadores y servidores de ejecución, Directorios y recursos de navegador | `human/categorias/32-navegadores-automatizacion-web.md` |
<!-- /BL:AGENT_CATEGORIES -->

## 🔗 Recetas

<!-- BL:RECIPES -->
- [💬 Bot de WhatsApp con IA](human/playbooks/bot-de-whatsapp-con-ia.md) — `evolution-api`, `dify`, `chatwoot`, `novu`
- [🎬 Pipeline de Reels / video corto](human/playbooks/pipeline-de-reels-video-corto.md) — `whisperx`, `kokoro`, `comfyui`, `real-esrgan`, `remotion`, `ffmpeg`, `moneyprinterturbo`
- [🔎 Agente de research profundo](human/playbooks/agente-de-research-profundo.md) — `gpt-researcher`, `searxng`, `crawl4ai`, `browser-use`, `markitdown`, `langfuse`
- [🏠 Workspace privado local soberano](human/playbooks/workspace-privado-local-soberano.md) — `ollama`, `odysseus`, `open-notebook`, `mem0`, `searxng`
- [🧠 Análisis de repos grandes](human/playbooks/analisis-de-repos-grandes.md) — `repomix`, `codegraph`, `gitnexus`, `graphify`, `claude-code`
- [📈 Marketing de agencia](human/playbooks/marketing-de-agencia.md) — `marketingskills`, `agency-agents`, `mautic`, `listmonk`, `posthog`
- [🌐 Web app moderna con IA](human/playbooks/web-app-moderna-con-ia.md) — `ui`, `tailwindcss`, `vercel-ai`, `assistant-ui`, `motion`, `recharts`, `swr`
- [🔌 Construir una app o servidor MCP](human/playbooks/construir-una-appservidor-mcp.md) — `awesome-mcp-servers`, `fastmcp`, `mcp-typescript-sdk`, `mcp-inspector`, `servers`, `mcp-use`
- [📊 Documentos → presentaciones](human/playbooks/documentos-presentaciones.md) — `markitdown`, `docling`, `ppt-master`, `slidev`, `marp`
- [🦙 ChatGPT privado con modelos locales](human/playbooks/chatgpt-privado-local.md) — `ollama`, `open-webui`, `searxng`, `litellm`
- [📎 RAG sobre tus documentos](human/playbooks/rag-sobre-documentos.md) — `docling`, `llama-index`, `qdrant`, `litellm`, `ragas`, `langfuse`
- [🛠️ Agente de código potenciado](human/playbooks/agente-de-codigo-potenciado.md) — `claude-code`, `superpowers`, `context7`, `serena`, `claude-mem`, `skillspector`
- [📞 Agente de voz en tiempo real](human/playbooks/agente-de-voz.md) — `pipecat`, `faster-whisper`, `litellm`, `kokoro`, `livekit-agents`
- [📊 Analítica de producto con IA](human/playbooks/analitica-con-ia.md) — `posthog`, `duckdb`, `wrenai`, `superset`, `umami`
<!-- /BL:RECIPES -->

---

## 🏷️ Leyenda de campos

- **`role`**: `platform` (plataforma) · `runtime` (motor) · `library` (librería/SDK) · `skill` (skill/prompt) · `directory` (catálogo) · `app` (app/UI)
- **`exec`**: `local` 🏠 · `cloud` ☁️ · `hybrid` 🔀
- **`setup`**: `easy` 🟢 · `medium` 🟡 · `heavy` 🔴 (GPU o varios servicios)
- **`mcp`**: `true` si expone o consume Model Context Protocol
- **`lib`**: estado del clon local, no novedad. La carpeta histórica de clones fue eliminada por el usuario; no recrearla para consultar la biblioteca.
- **`goals` / `routes`**: tareas y accesos documentados. `no_api` indica una ruta sin clave propia de API de IA; puede usar el agente anfitrión o un servicio online y no promete funcionamiento offline ni ausencia de otras tarifas.
- **`added_at`**: primera incorporación al índice según Git; no fecha de lanzamiento.
- **`getting_started.audience`**: `ready_app`, `agent`, `reading`, `developer` o `setup`; indica la preparación que cabe esperar, sin prometer instalación probada.
- **`alt`**: sustitutos (elige uno) · **`combines_with`** (en detalle): complementarios (úsalos juntos)

---

## 🔧 Mantenimiento

La fuente de verdad son `INDICE_IA.json` + `INDICE_IA.detalle.json`. `Catalogo.md`, `Guia.md`, `human/`, `docs/index.html`, `menu_portable/` y los bloques `<!-- BL:* -->` de este archivo y del README se regeneran con:

```powershell
uv run repo-intelligence guide build
uv run repo-intelligence menu export
uv run repo-intelligence web build
uv run pytest
```

La web pública es [Alexandría](https://cristrva1.github.io/BL_Alexandria/). GitHub Pages publica el contenido generado de `main/docs`: al actualizar el catálogo, ejecuta `guide build` y sube sus resultados para que se desplieguen. El generador conserva `.nojekyll` para servir los archivos estáticos directamente.

### Cómo agregar un repo

Usa `uv run repo-intelligence add` (código en `src/repo_intelligence/curate/add.py`). Lee la identidad con `gh api`, rechaza archivados, duplicados (id numérico, `owner/repo`, URL o id) y retirados (salvo `--force`), y escribe los dos índices, el lote de 4 secciones, la especificación en `curation/altas/` y el informe en `reports/altas/`.

```powershell
uv run repo-intelligence add owner/repo --categoria 16 --sub defensa --ligero   # borrador PENDIENTE
uv run repo-intelligence add --desde curation/altas/mi-lote.json --construir     # lote con 4 secciones
uv run repo-intelligence add wazuh --sugerir-combos [--aplicar-combos]
```

Completo: 3-6 `combina_con` y reciprocidad automática dentro del límite de 6. `--ligero`: 0-6, exento de simetría (`nivel: "ligero"`), ids válidos. No publiques entradas con `PENDIENTE`. Formato del lote en [mantenimiento editorial](human/mantenimiento.md#incorporar-un-repo).

Con un clon local también existe `discover` → `analyze --new` → `enrich --new --auto-merge` (borradores en `data/drafts/`) → `guide build`; la inferencia está en `src/repo_intelligence/analysis/curation.py`.

Ese flujo sirve cuando existe un clon. Para nuevas stars sin clones, usa fuentes de GitHub y el proceso de [mantenimiento editorial](human/mantenimiento.md). `scripts/audit_sources.py` guarda README y evidencias para revisar; no confirma requisitos a partir de keywords. Los scripts `curate_access.py` y `curate_discovery.py` son migraciones editoriales fechadas y requieren revisar sus decisiones antes de reutilizarlas. Un perfil nuevo conserva incertidumbre hasta disponer de evidencia.

La revisión individual de los 679 proyectos está en `curation/review-679-2026-11-14/` y `reports/review-679-2026-11-14.json`. `scripts/apply_review_679.py --apply` exige cobertura total y las instantáneas locales de esa revisión; es una migración fechada,no un auditor automático de proyectos nuevos. Conserva la incertidumbre y el SHA anterior al actualizar una fuente. No publiques el documento privado de importación ni las instantáneas completas de README.

Para la actualización diaria desde stars, sigue [DAILY_STARS.md](DAILY_STARS.md). `uv run python scripts/daily_stars.py` detecta ids públicos faltantes y guarda fuentes en la carpeta ignorada `data/reviews/daily-stars/`; no clasifica ni incorpora automáticamente. La tarea programada de Codex realiza la revisión editorial y la publicación. No recrees clones, no dupliques renombrados y no borres fichas al retirar una star.

Los repos obsoletos se retiran con aprobación y quedan registrados en `data/retired.json`; el detector de stars los omite. Consulta el procedimiento en [mantenimiento editorial](human/mantenimiento.md#retirar-repos-obsoletos).

Al editar a mano una entrada, mantén: `one` de 60 a 175 caracteres en español claro; `alt` simétrico (si A lista a B, B lista a A) y como máximo 5; ids de `alt` y `combines_with` que existan en el índice. Las pruebas lo comprueban.
