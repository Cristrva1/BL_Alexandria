# Alexandría para agentes · Skills de dominio: marketing, SEO y negocio

Categoría 27 «Skills de diseño, contenido y especialidades» › subcategoría `dominio`. 14 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=27&sub=dominio · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `marketingskills` | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email… | 1 Básico | 71 | MIT (OSI permisiva) | sin grupo |
| `scientific-agent-skills` | Colección de skills y recursos para que agentes realicen tareas de… | 2 Intermedio | 71 | MIT (OSI permisiva) | sin grupo |
| `claude-seo` | Skills de Claude Code para revisar SEO técnico, contenido, presencia en… | 2 Intermedio | 70 | MIT (OSI permisiva) | recomendado |
| `agency-agents` | Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing… | 1 Básico | 69 | MIT (OSI permisiva) | sin grupo |
| `financial-services` | Plugins, skills y conectores de Anthropic para flujos de investigación y… | 2 Intermedio | 61 | Apache-2.0 (OSI permisiva) | sin grupo |
| `instagram-agent-skill` | Skills de Claude para investigar ideas, preparar guiones y revisar contenido y… | 2 Intermedio | 56 | MIT (OSI permisiva) | recomendado |
| `social-media-research-skills` | Skills para investigar publicaciones, comentarios, competidores y anuncios en… | 2 Intermedio | 51 | MIT (OSI permisiva) | sin grupo |
| `geo-seo-claude` | Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO… | 1 Básico | 49 | MIT (OSI permisiva) | alternativa |
| `linkedin-agent-skill` | Skills de Claude para preparar publicaciones, comentarios y planificación de… | 2 Intermedio | 47 | MIT (OSI permisiva) | alternativa |
| `arcads-claude-code` | Pack de skills para Claude Code y Cursor que crea anuncios en video e imagen… | 2 Intermedio | 39 | MIT (OSI permisiva) | sin grupo |
| `minimalist-entrepreneur-skills` | Skills basadas en ideas de The Minimalist Entrepreneur para orientar trabajo de… | 2 Intermedio | 36 | — (sin licencia detectada) | sin grupo |
| `claude-ads` | Audita campañas de publicidad con Claude Code y organiza los hallazgos por… | 2 Intermedio | — | MIT | sin grupo |
| `knowledge-work-plugins` | Añade a Claude flujos de trabajo por especialidad, como preparar reuniones de… | 2 Intermedio | — | Apache-2.0 | sin grupo |
| `shopify-ai-toolkit` | Aporta guías y herramientas de Shopify para asistir el desarrollo de temas y… | 2 Intermedio | — | MIT | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Marketing Skills (`marketingskills`)

- **Repo:** https://github.com/coreyhaines31/marketingskills · MIT · nivel 1 · 71/100
- **Qué es:** Colección de skills de marketing para agentes de IA, de Corey Haines (agencia Conversion Factory), MIT y financiada por «Verified Partners» declarados. Muy activa (v2.14.12).
- **Cuándo elegirlo:** Casos: Revisar el texto de una landing; Preparar un plan de medición.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Agente con skills; brief comercial; datos de prueba; cuentas externas solo si las conectas; hardware prerequisites; API de IA: opcional; Agente con skills; brief comercial; datos de prueba; cuentas externas solo si las conectas.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add coreyhaines31/marketingskills --skill cro copywriting` — fuente: https://github.com/coreyhaines31/marketingskills/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala un skill de copy y crea dos propuestas a partir de un brief ficticio Éxito: Puedes comparar audiencia, mensaje y llamada a la acción
- **Combina con:** `claude-code` [20/terminal], `posthog` [10/producto], `mautic` [18/marketing], `open-seo` [18/marketing], `humanizer` [27/escritura], `linkedin-agent-skill`
- **Riesgos y avisos:** Algunas herramientas recomendadas son socios que financian el proyecto; lo declara en su registro. Compatible con Agent Skills; instalar desde una sesión de agente puede elegir una carpeta compartida distinta de .claude y requiere comprobar descubrimiento.

### scientific-agent-skills (`scientific-agent-skills`)

- **Repo:** https://github.com/K-Dense-AI/scientific-agent-skills · MIT · nivel 2 · 71/100
- **Qué es:** Colección MIT de 177 skills científicas y de investigación de K-Dense (antes Claude Scientific Skills), compatible con cualquier agente que siga el estándar Agent Skills.
- **Cuándo elegirlo:** Casos: Explorar un dataset científico; Preparar una revisión bibliográfica.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente compatible; herramienta y skill elegidas; datos no sensibles de muestra; hardware prerequisites; API de IA: opcional; Agente compatible; herramienta y skill elegidas; datos no sensibles de muestra.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add K-Dense-AI/scientific-agent-skills` — fuente: https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige una skill de análisis y verifica dependencias y fuentes con un dataset educativo Éxito: Puedes reproducir un resultado pequeño y revisar las referencias
- **Combina con:** `claude-code` [20/terminal], `open-notebook` [8/notebooklm], `anthropic-skills` [2/catalogos]
- **Riesgos y avisos:** Las integraciones de laboratorio requieren cuentas propias en cada plataforma. Ahora se llama Scientific Agent Skills y admite Claude Code, Codex y Antigravity; la biblioteca no valida por sí sola conclusiones científicas ni autoriza….

### claude-seo (`claude-seo`)

- **Repo:** https://github.com/AgriciDaniel/claude-seo · MIT · nivel 2 · 70/100 · recomendado en «Skills de SEO para agentes»
- **Qué es:** Plugin SEO gratuito y de código abierto (MIT) para Claude Code, de AgriciDaniel. Activo (v2.6.2), con 29 subskills y 20 agentes especialistas.
- **Cuándo elegirlo:** Casos: Preparar una auditoría SEO inicial; Revisar indexabilidad de una landing.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Claude Code; Python 3.11–3.14; web propia; dependencias de navegador; hardware prerequisites; API de IA: opcional; Claude Code; Python 3.11–3.14; web propia; dependencias de navegador.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/AgriciDaniel/claude-seo/blob/main/README.md

  ```bash
  /plugin marketplace add AgriciDaniel/claude-seo
  /plugin install claude-seo@agricidaniel-claude-seo
  /seo setup
  ```
- **Primera prueba propuesta (no ejecutada):** Usa setup y revisa una página de prueba para comprobar los hallazgos técnicos Éxito: Puedes contrastar títulos, enlaces o schema con la página
- **Combina con:** `claude-code` [20/terminal], `posthog` [10/producto], `open-seo` [18/marketing]
- **Alternativas:** `geo-seo-claude`
- **Riesgos y avisos:** Alternativa (elige una): geo-seo-claude. No promete mejorar ranking ni sustituir una auditoría humana; las funciones de datos en vivo requieren configuración adicional.

### The Agency (agency-agents) (`agency-agents`)

- **Repo:** https://github.com/msitarzewski/agency-agents · MIT · nivel 1 · 69/100
- **Qué es:** Colección MIT de personalidades de agentes especializados («The Agency») de msitarzewski, surgida de un hilo de Reddit; uno de los repos más populares del catálogo. Sin releases; tiene app de escritorio aparte para instalarla.
- **Cuándo elegirlo:** Casos: Seleccionar un perfil de frontend; Revisar un brief de marketing.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Agente compatible o app del catálogo; encargo concreto; hardware prerequisites; API de IA: no; Agente compatible o app del catálogo; encargo concreto.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install --cask msitarzewski/agency-agents/agency-agents` — fuente: https://github.com/msitarzewski/agency-agents/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala solo un especialista y pide revisar un componente de prueba con criterios claros Éxito: Puedes reconocer su función y valorar sus recomendaciones
- **Combina con:** `claude-code` [20/terminal], `opencode` [20/terminal], `gemini-cli` [20/terminal]
- **Alternativas:** `wshobson-agents`
- **Riesgos y avisos:** Alternativa (elige una): wshobson-agents. Documenta instaladores para Claude Code, Codex y Antigravity; un perfil experto es una plantilla y no demuestra experiencia profesional ni una entrega validada.

### financial-services (`financial-services`)

- **Repo:** https://github.com/anthropics/financial-services · Apache-2.0 · nivel 2 · 61/100
- **Qué es:** Repositorio oficial de Anthropic (Apache 2.0) con agentes de referencia, skills y conectores de datos para servicios financieros. Activo, sin releases; advierte que nada en él es asesoría financiera, legal o fiscal.
- **Cuándo elegirlo:** Casos: Preparar un análisis de empresa; Estudiar conciliación de registros ficticios.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Claude Code o Cowork; datos financieros ficticios; acceso a conectores si los usas; hardware prerequisites; API de IA: opcional; Claude Code o Cowork; datos financieros ficticios; acceso a conectores si los usas.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/anthropics/financial-services/blob/main/README.md

  ```bash
  # Add the marketplace
  claude plugin marketplace add anthropics/financial-services
  
  # Core skills + connectors (install first)
  claude plugin install financial-analysis@claude-for-financial-services
  ```
- **Primera prueba propuesta (no ejecutada):** Elige una skill de análisis y trabaja sobre un conjunto de cifras de muestra con fuentes explícitas Éxito: Puedes contrastar fórmulas, datos y supuestos del borrador
- **Combina con:** `claude-code` [20/terminal], `anthropic-skills` [2/catalogos], `claude-agent-sdk-python` [3/py]
- **Riesgos y avisos:** Los conectores de datos de socios requieren licencias propias de esos proveedores. Los conectores y cookbooks tienen rutas diferentes; no incluye datos financieros premium ni convierte resultados en asesoría validada.

### instagram-agent-skill (`instagram-agent-skill`)

- **Repo:** https://github.com/Jakeschincariol/instagram-agent-skill · MIT · nivel 2 · 56/100 · recomendado en «Skills para redes sociales»
- **Qué es:** Trece skills de Claude (MIT) de Jake Schincariol para gestionar una cuenta de Instagram, sin registro ni clave de API. Sin releases; último cambio en septiembre de 2026.
- **Cuándo elegirlo:** Casos: Preparar un Reel; Revisar un caption.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Claude o Claude Code; brief de contenido; Python para utilidades opcionales; hardware prerequisites; API de IA: no; Claude o Claude Code; brief de contenido; Python para utilidades opcionales.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Jakeschincariol/instagram-agent-skill/blob/main/README.md

  ```bash
  git clone https://github.com/Jakeschincariol/instagram-agent-skill.git
  cp -r instagram-agent-skill/skills/ig-* ~/.claude/skills/
  ```
- **Primera prueba propuesta (no ejecutada):** Genera un borrador de guion y revisa gancho, datos y llamada a la acción sin publicarlo Éxito: Puedes editar el texto y comprobar sus afirmaciones
- **Combina con:** `claude-code` [20/terminal], `postiz-app` [18/marketing], `social-media-research-skills`
- **Alternativas:** `linkedin-agent-skill`
- **Riesgos y avisos:** Produce ideas y revisiones y no conecta automáticamente tu Instagram; pegar SKILL.md en otro modelo no acredita un plugin nativo allí.

### social-media-research-skills (`social-media-research-skills`)

- **Repo:** https://github.com/ScrapeCreators/social-media-research-skills · MIT · nivel 2 · 51/100
- **Qué es:** Skills de investigación en redes sociales (MIT) de ScrapeCreators, que funcionan con su API de pago. Sin releases; último cambio en agosto de 2026.
- **Cuándo elegirlo:** Casos: Comparar temas de contenido; Analizar comentarios públicos de una marca.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente con skills; API key de ScrapeCreators; consulta acotada; hardware prerequisites; API de IA: no; Agente con skills; API key de ScrapeCreators; consulta acotada.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add ScrapeCreators/social-media-research-skills` — fuente: https://github.com/ScrapeCreators/social-media-research-skills/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Investiga una pequeña muestra pública y revisa origen, fecha y coste antes de ampliar la búsqueda Éxito: Puedes rastrear las observaciones a publicaciones concretas
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `postiz-app` [18/marketing], `instagram-agent-skill`
- **Alternativas:** `last30days-skill`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativa (elige una): last30days-skill. Cada consulta consume créditos de ScrapeCreators. La API externa es de datos y no necesariamente una segunda API LLM; el estándar Agent Skills admite los hosts compatibles pero las redes imponen sus límites.

### GEO-SEO Claude (`geo-seo-claude`)

- **Repo:** https://github.com/zubair-trabzada/geo-seo-claude · MIT · nivel 1 · 49/100 · alternativa en «Skills de SEO para agentes»
- **Qué es:** Skill para Claude Code de zubair-trabzada (MIT) que optimiza sitios para buscadores con IA (GEO) sin descuidar el SEO tradicional. Activa, sin releases.
- **Cuándo elegirlo:** Casos: Revisar schema de una web; Preparar un informe GEO inicial.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Claude Code; Python; Git Bash en Windows; web propia de prueba; hardware prerequisites; API de IA: opcional; Claude Code; Python; Git Bash en Windows; web propia de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/zubair-trabzada/geo-seo-claude/blob/main/README.md

  ```bash
  git clone https://github.com/zubair-trabzada/geo-seo-claude.git
  cd geo-seo-claude
  ./install.sh
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta una revisión de una página propia y contrasta dos hallazgos con el HTML Éxito: Puedes separar observación, heurística y propuesta
- **Combina con:** `claude-code` [20/terminal], `playwright` [32/bibliotecas], `open-seo` [18/marketing]
- **Alternativas:** `claude-seo`
- **Riesgos y avisos:** Revisa el script antes de ejecutar `curl | bash`. Alternativa (elige una): claude-seo. Optimizar citabilidad no garantiza aparecer en resultados AI; la instalación Windows documentada usa Git Bash y no PowerShell.

### linkedin-agent-skill (`linkedin-agent-skill`)

- **Repo:** https://github.com/Jakeschincariol/linkedin-agent-skill · MIT · nivel 2 · 47/100 · alternativa en «Skills para redes sociales»
- **Qué es:** Once skills de Claude (MIT) de Jake Schincariol para gestionar una cuenta de LinkedIn, sin registro ni clave de API. Sin releases; último cambio en septiembre de 2026.
- **Cuándo elegirlo:** Casos: Planificar una semana de contenido; Revisar un perfil profesional.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Claude o Claude Code; experiencia propia y tema; hardware prerequisites; API de IA: no; Claude o Claude Code; experiencia propia y tema.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Jakeschincariol/linkedin-agent-skill/blob/main/README.md

  ```bash
  git clone https://github.com/Jakeschincariol/linkedin-agent-skill.git
  cp -r linkedin-agent-skill/skills/li-* ~/.claude/skills/
  ```
- **Primera prueba propuesta (no ejecutada):** Prepara un borrador basado en un hecho propio y revisa si conserva tu tono antes de publicarlo Éxito: Puedes distinguir hechos, opiniones y sugerencias del modelo
- **Combina con:** `claude-code` [20/terminal], `postiz-app` [18/marketing], `marketingskills`
- **Alternativas:** `instagram-agent-skill`
- **Riesgos y avisos:** Automatizar comentarios en LinkedIn puede chocar con sus condiciones de uso; publica manualmente. La instalación documentada es para Claude y las instrucciones pueden pegarse en otros modelos; no publica ni garantiza alcance.

### Arcads AI Video Skill Pack (`arcads-claude-code`)

- **Repo:** https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial · MIT · nivel 2 · 39/100
- **Qué es:** Paquete de skills (MIT) de «Mr. Paid Social» para crear videos e imágenes publicitarios con la cuenta de Arcads desde Claude Code o Cursor. El README usa enlaces de afiliado y promociona una comunidad de pago.
- **Cuándo elegirlo:** Casos: Prototipar un anuncio vertical; Preparar variantes de una imagen de producto.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP), requiere clave de API; Claude Code o Cursor; cuenta y acceso API Arcads; presupuesto de generación; hardware prerequisites; API de IA: sí; Claude Code o Cursor; cuenta y acceso API Arcads; presupuesto de generación.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial/blob/main/README.md

  ```bash
  git clone https://github.com/krusemediallc/arcads-claude-code.git
  cd arcads-claude-code
  ```
- **Primera prueba propuesta (no ejecutada):** Prepara un brief y revisa el coste y modelo antes de generar una única pieza de prueba Éxito: Puedes identificar proveedor, entrada y resultado generado
- **Combina con:** `ffmpeg` [12/edicion], `hyperframes` [30/motores], `whisper` [29/stt], `claude-code` [20/terminal]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Requiere cuenta de pago de Arcads; cada generación consume créditos. El repositorio es gratuito pero no incluye generaciones ni acceso gratuito a todos los modelos; empieza por crear sin publicar.

### skills (`minimalist-entrepreneur-skills`)

- **Repo:** https://github.com/slavingia/skills · — · nivel 2 · 36/100
- **Qué es:** Diez skills para Claude Code basadas en el libro «The Minimalist Entrepreneur» de Sahil Lavingia (fundador de Gumroad), publicadas en su repositorio `slavingia/skills`.
- **Cuándo elegirlo:** Casos: Explorar un problema de cliente; Preparar preguntas de validación.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Claude Code; idea de negocio; supuestos escritos; hardware prerequisites; API de IA: no; Claude Code; idea de negocio; supuestos escritos.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/slavingia/skills/blob/main/README.md

  ```bash
  /plugin marketplace add slavingia/skills
  /plugin install minimalist-entrepreneur
  ```
- **Primera prueba propuesta (no ejecutada):** Usa una skill para formular una hipótesis de cliente y una prueba pequeña sin gastar ni contactar personas todavía Éxito: Puedes distinguir hipótesis, evidencia pendiente y siguiente experimento
- **Combina con:** `claude-code` [20/terminal], `marketingskills`, `posthog` [10/producto]
- **Riesgos y avisos:** Sin licencia declarada: técnicamente no hay permiso explícito de redistribución. El pack está basado en un libro y documenta Claude Code; sus plantillas no demuestran demanda, ingresos o validez de un precio.

### Claude Ads (`claude-ads`)

- **Repo:** https://github.com/AgriciDaniel/claude-ads · MIT · nivel 2 · —/100
- **Qué es:** Audita campañas de publicidad con Claude Code y organiza los hallazgos por plataforma, evidencia y prioridad.
- **Cuándo elegirlo:** Casos: Crear una lista de comprobaciones para una campaña ficticia.; Preparar un informe a partir de un CSV de métricas inventadas. Evítalo si no usas un agente compatible con skills.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Python, pyproject.toml, requirements.txt; API de IA: no; Claude Code, una cuenta de prueba y Python 3.11 o 3.12 si activas dependencias gestionadas..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/AgriciDaniel/claude-ads/blob/fc3908e786c318776df89a3a098333da377364be/README.md
- **Primera prueba propuesta (no ejecutada):** Selecciona la skill de auditoría y entrega métricas ficticias, sin conectar cuentas. Éxito: El informe separa hallazgos, evidencia y datos que faltan.
- **Riesgos y avisos:** Las operaciones que cambian cuentas dependen de conectores y permisos; el catálogo recomienda empezar solo con datos de muestra.

### Knowledge Work Plugins (`knowledge-work-plugins`)

- **Repo:** https://github.com/anthropics/knowledge-work-plugins · Apache-2.0 · nivel 2 · —/100
- **Qué es:** Añade a Claude flujos de trabajo por especialidad, como preparar reuniones de ventas, revisar datos y organizar soporte.
- **Cuándo elegirlo:** Casos: Preparar preguntas para una reunión ficticia.; Clasificar tres tickets inventados sin abrir un CRM. Evítalo si no usas un agente compatible con skills.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Python; API de IA: no; Claude Cowork o Claude Code y, solo para conectores, cuentas de prueba y permisos limitados..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://claude.com/plugins
- **Primera prueba propuesta (no ejecutada):** Elige un plugin de ventas desde el marketplace y prepara un brief sobre una empresa ficticia. Éxito: Claude devuelve objetivos y preguntas sin conectarse a sistemas reales.
- **Riesgos y avisos:** El anfitrión consume su propio plan; los conectores de trabajo pueden requerir otra cuenta. Revisa cada plugin por separado.

### Shopify AI Toolkit (`shopify-ai-toolkit`)

- **Repo:** https://github.com/Shopify/Shopify-AI-Toolkit · MIT · nivel 2 · —/100
- **Qué es:** Aporta guías y herramientas de Shopify para asistir el desarrollo de temas y aplicaciones con fuentes del fabricante.
- **Cuándo elegirlo:** Casos: Consultar cómo se organiza una sección de tema de prueba.; Preparar una consulta de catálogo para una tienda de desarrollo. Evítalo si no usas un agente compatible con skills.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); JavaScript, package.json; API de IA: no; Un cliente admitido y, si consultas una tienda, una cuenta de desarrollo con alcance mínimo..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Shopify/Shopify-AI-Toolkit/blob/0388268a61051d1e8400996a58b0e3590c1e1500/README.md
- **Primera prueba propuesta (no ejecutada):** Instala la integración para tu cliente en un proyecto de ejemplo y prueba una consulta de documentación. Éxito: El asistente enlaza la guía de Shopify o devuelve la estructura esperada para el ejemplo.
- **Riesgos y avisos:** El README declara telemetría activada por defecto y documenta desactivarla. Operar tiendas y usar modelos puede requerir cuentas o planes separados.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-27-dominio.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Skills de dominio: marketing, SEO y negocio», lee `docs/alexandria/categoria-27-dominio.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-27-dominio.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
