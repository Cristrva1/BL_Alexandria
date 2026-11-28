# Alexandría para agentes · Dashboards, analítica y mapas

Categoría 10 completa (33 repos, 6 subcategorías). Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=10 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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

| Repo | Sub | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---|---:|---|---|
| `umami` | producto | Analítica web y de producto respetuosa con la privacidad, sin cookies… | 1 Básico | 74 | MIT (OSI permisiva) | recomendado |
| `posthog` | producto | Plataforma de product analytics y eventos para entender el comportamiento de… | 3 Avanzado | 71 | MIT + licencia Enterprise (ee/) (open-core) | sin grupo |
| `plausible` | producto | Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o… | 2 Intermedio | 59 | AGPL-3.0 (OSI copyleft) | alternativa |
| `matomo` | producto | Alternativa open source a Google Analytics con control total de los datos. | 2 Intermedio | 57 | GPL-3.0 (OSI copyleft) | alternativa |
| `superset` | bi | Plataforma de exploración y visualización de datos de Apache, alternativa… | 2 Intermedio | 82 | Apache-2.0 (OSI permisiva) | recomendado |
| `grafana` | bi | Plataforma de visualización y observabilidad para métricas, logs y trazas de… | 2 Intermedio | 80 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `metabase` | bi | Herramienta de dashboards y BI para explorar métricas de negocio conectando… | 2 Intermedio | 67 | AGPL-3.0 + licencia comercial (enterprise/) (open-core) | alternativa |
| `evidence` | bi | BI como código: informes y visualizaciones interactivas escritos en SQL y… | 1 Básico | 57 | MIT (OSI permisiva) | sin grupo |
| `redash` | bi | Herramienta para consultar cualquier fuente de datos con SQL, visualizar y… | 2 Intermedio | 57 | BSD-2-Clause (OSI permisiva) | alternativa |
| `wrenai` | bi | BI generativo: convierte preguntas en SQL fiable a través de una capa semántica… | 2 Intermedio | 57 | Multilicencia por ruta (Apache-2.0, AGPL-3.0, CC-BY-4.0) (OSI copyleft) | sin grupo |
| `echarts` | graficos | Librería de visualización potente para gráficos y dashboards web (proyecto… | 2 Intermedio | 71 | Apache-2.0 (OSI permisiva) | recomendado |
| `d3` | graficos | Librería JavaScript para visualizaciones de datos a medida con SVG, Canvas y… | 2 Intermedio | 70 | ISC (OSI permisiva) | alternativa |
| `recharts` | graficos | Librería de gráficos para React construida con D3, declarativa y componible. | 2 Intermedio | 69 | MIT (OSI permisiva) | alternativa |
| `chart-js` | graficos | Librería JavaScript para dibujar gráficos en canvas dentro de una página o… | 2 Intermedio | 64 | MIT (OSI permisiva) | alternativa |
| `uplot` | graficos | Biblioteca compacta de gráficos de series temporales en JavaScript, orientada a… | 2 Intermedio | 56 | MIT (OSI permisiva) | sin grupo |
| `awesome-dataviz` | recursos | Directorio curado de herramientas, librerías y recursos de visualización de… | 1 Básico | 58 | CC-BY-4.0 (OSI permisiva) | sin grupo |
| `awesome-bigdata` | recursos | Directorio curado de frameworks, bases de datos y herramientas de big data… | 1 Básico | 46 | MIT (OSI permisiva) | sin grupo |
| `data-analyst-roadmap` | recursos | Hoja de ruta para aprender análisis de datos, con tecnologías, capacidades y… | 1 Básico | 38 | MIT (OSI permisiva) | sin grupo |
| `gods-eye-view` | osint | Visualizador geoespacial en un globo 3D que reúne fuentes abiertas para… | 2 Intermedio | 68 | MIT (solo código) (OSI permisiva) | recomendado |
| `sherlock` | osint | CLI OSINT que busca un nombre de usuario en más de 400 redes sociales y sitios… | 1 Básico | 67 | MIT (OSI permisiva) | recomendado |
| `theharvester` | osint | Herramienta OSINT de reconocimiento que reúne correos, subdominios, IP y… | 2 Intermedio | 66 | GPL-2.0 (OSI copyleft) | sin grupo |
| `maigret` | osint | Recopila un dossier sobre una persona a partir de un nombre de usuario… | 1 Básico | 63 | MIT (OSI permisiva) | alternativa |
| `osiris` | osint | Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes… | 2 Intermedio | 53 | MIT (OSI permisiva) | alternativa |
| `pythia` | osint | Plataforma local que reúne fuentes de actualidad y genera escenarios con… | 3 Avanzado | 47 | MIT (OSI permisiva) | sin grupo |
| `recon-ng` | osint | Framework modular de reconocimiento web OSINT con espacios de trabajo, base de… | 2 Intermedio | 44 | GPL-3.0 (OSI copyleft) | sin grupo |
| `leaflet` | geoespacial | Biblioteca JavaScript ligera para mapas web interactivos: unos 40 kB, capas de… | 2 Intermedio | 70 | BSD-2-Clause (OSI permisiva) | recomendado |
| `maplibre` | geoespacial | Biblioteca abierta de mapas vectoriales interactivos en el navegador con… | 2 Intermedio | 67 | BSD-3-Clause (OSI permisiva) | alternativa |
| `kepler.gl` | geoespacial | Herramienta web de exploración visual de grandes datos geográficos sin código… | 1 Básico | 66 | MIT (OSI permisiva) | sin grupo |
| `deck.gl` | geoespacial | Framework de visualización en WebGL2/WebGPU para grandes conjuntos de datos… | 2 Intermedio | 65 | MIT (OSI permisiva) | sin grupo |
| `qgis` | geoespacial | Sistema de información geográfica libre y multiplataforma: gestión de datos… | 1 Básico | 61 | GPL-2.0 (OSI copyleft) | sin grupo |
| `webodm` | geoespacial | Interfaz para procesar fotografías aéreas y obtener mapas y modelos con el… | 3 Avanzado | 60 | AGPL-3.0 (OSI copyleft) | recomendado |
| `odm` | geoespacial | Herramientas para convertir fotografías aéreas en mapas, nubes de puntos… | 2 Intermedio | 58 | AGPL-3.0 (OSI copyleft) | alternativa |
| `globalbuildingatlas` | geoespacial | Dataset global y código de procesamiento de edificios con polígonos, alturas y… | 1 Básico | 32 | MIT + Commons Clause (source-available) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Umami (`umami`)

- **Repo:** https://github.com/umami-software/umami · MIT · nivel 1 · 74/100 · recomendado en «Analítica web auto-hospedada»
- **Qué es:** Umami, plataforma open source de analítica web y de producto centrada en la privacidad, de Umami Software. Licencia MIT. Es madura (~40k estrellas, v3.5.0).
- **Cuándo elegirlo:** Casos: Medir visitas de una web; Comparar campañas mediante eventos propios.
- **Requisitos:** nivel 1: preparación sencilla; Node >=20.19; pnpm; PostgreSQL >=12.14; configuración .env; hardware prerequisites; API de IA: no; Node >=20.19; pnpm; PostgreSQL >=12.14; configuración .env.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/umami-software/umami/blob/master/README.md

  ```bash
  git clone https://github.com/umami-software/umami.git
  cd umami
  pnpm install
  ```
- **Primera prueba propuesta (no ejecutada):** Añade el script a una página propia de prueba y genera un evento ficticio Éxito: El panel recibe la visita y el evento del sitio correcto
- **Combina con:** `metabase` [10/bi], `grafana` [10/bi], `activepieces` [1/motores]
- **Alternativas:** `plausible`, `matomo`
- **Riesgos y avisos:** Alternativas (elige una): plausible, matomo. Configura DATABASE_URL y APP_SECRET antes de build; cambia la contraseña inicial cuando lo solicite.

### posthog (`posthog`)

- **Repo:** https://github.com/PostHog/posthog · MIT + licencia Enterprise (ee/) · nivel 3 · 71/100
- **Qué es:** PostHog, plataforma de analítica de producto y capa de datos para producto y agentes. Licencia MIT salvo la carpeta `ee` (GitHub muestra NOASSERTION). Es muy activa (~41k estrellas).
- **Cuándo elegirlo:** Casos: Entender abandono en un flujo de registro; Revisar errores y sesiones de una app.
- **Requisitos:** nivel 3: preparación pesada; Cuenta y región de datos; SDK o snippet; cliente MCP opcional; hardware prerequisites; API de IA: opcional; Cuenta y región de datos; SDK o snippet; cliente MCP opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `npx -y @posthog/wizard@latest` — fuente: https://github.com/PostHog/posthog/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Registra un evento ficticio y construye un embudo de dos pasos en un proyecto de prueba Éxito: Puedes ver cada evento y cómo se calcula el embudo
- **Combina con:** `claude-code` [20/terminal], `activepieces` [1/motores], `metabase` [10/bi], `claude-seo` [27/dominio], `marketingskills` [27/dominio], `mautic` [18/marketing]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. El autoalojamiento «hobby» no es para producción. El MCP remoto documenta Claude Code y Codex y enruta por región; empieza consultando datos antes de permitir cambios.

### Plausible Analytics (`plausible`)

- **Repo:** https://github.com/plausible/analytics · AGPL-3.0 · nivel 2 · 59/100 · alternativa en «Analítica web auto-hospedada»
- **Qué es:** Plausible Analytics, analítica web ligera y sin cookies hecha y alojada en la UE. Plausible CE es AGPL-3.0 o posterior y el script de seguimiento es MIT. Es madura (~30k estrellas, v3.2.1).
- **Cuándo elegirlo:** Casos: Medir una web de contenido; Comparar conversiones de una landing.
- **Requisitos:** nivel 2: preparación media; Cuenta Cloud o servidor CE; web propia para el script; hardware prerequisites; API de IA: no; Cuenta Cloud o servidor CE; web propia para el script.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/plausible/community-edition/
- **Primera prueba propuesta (no ejecutada):** Mide una visita y un objetivo de prueba sin añadir datos personales al evento Éxito: El panel muestra el sitio, la visita y el objetivo
- **Combina con:** `activepieces` [1/motores], `grafana` [10/bi], `supabase` [22/infraestructura]
- **Alternativas:** `umami`, `matomo`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): umami, matomo. Para self-hosting sigue el repositorio Community Edition enlazado, no asumas que clonar analytics completa el despliegue.

### Matomo (`matomo`)

- **Repo:** https://github.com/matomo-org/matomo · GPL-3.0 · nivel 2 · 57/100 · alternativa en «Analítica web auto-hospedada»
- **Qué es:** Matomo (antes Piwik), plataforma de analítica web libre y autoalojable. Licencia GPL-3.0 o posterior. Es muy madura (~22k estrellas, 5.14.2) y el README cita más de 1,4 millones de sitios.
- **Cuándo elegirlo:** Casos: Gestionar analítica en servidor propio; Crear informes de comportamiento de una web.
- **Requisitos:** nivel 2: preparación media; Servidor PHP y MySQL compatibles; web de prueba; configuración de privacidad; hardware prerequisites; API de IA: no; Servidor PHP y MySQL compatibles; web de prueba; configuración de privacidad.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/matomo-org/matomo .` — fuente: https://matomo.org/faq/how-to-install/faq_18271/
- **Primera prueba propuesta (no ejecutada):** Añade seguimiento a una página propia y verifica una visita y un objetivo ficticio Éxito: El informe identifica las acciones de la visita de prueba
- **Combina con:** `metabase` [10/bi], `grafana` [10/bi], `activepieces` [1/motores]
- **Alternativas:** `umami`, `plausible`
- **Riesgos y avisos:** Alternativas (elige una): umami, plausible. Ajusta seguimiento y privacidad a tu implementación; instalar Matomo no configura automáticamente todas las políticas del sitio.

### Apache Superset (`superset`)

- **Repo:** https://github.com/apache/superset · Apache-2.0 · nivel 2 · 82/100 · recomendado en «BI y dashboards»
- **Qué es:** Apache Superset, aplicación web de BI de la Apache Software Foundation. Licencia Apache-2.0. Es muy madura (~76k estrellas, 6.1.0).
- **Cuándo elegirlo:** Casos: Explorar métricas de una base SQL; Compartir un dashboard interno.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Entorno del quickstart; motor SQL; driver de conexión; datos ficticios; hardware prerequisites; API de IA: no; Entorno del quickstart; motor SQL; driver de conexión; datos ficticios.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose -f docker-compose-image-tag.yml up` — fuente: https://github.com/apache/superset/blob/master/docs/docs/quickstart.mdx
- **Primera prueba propuesta (no ejecutada):** Conecta una tabla de ventas ficticias y crea un gráfico por mes Éxito: El gráfico coincide con una suma SQL verificable
- **Combina con:** `duckdb` [25/datos], `wrenai`, `echarts` [10/graficos], `hudi` [25/datos], `kestra` [1/motores], `deck.gl` [10/geoespacial]
- **Alternativas:** `metabase`, `redash`
- **Riesgos y avisos:** Alternativas (elige una): metabase, redash. Instala el driver de la base elegida y usa credenciales de lectura para la primera prueba.

### Grafana (`grafana`)

- **Repo:** https://github.com/grafana/grafana · AGPL-3.0 · nivel 2 · 80/100
- **Qué es:** Grafana, plataforma open source de visualización y observabilidad de Grafana Labs. Licencia AGPL-3.0-only con excepciones Apache-2.0. Es muy madura (~78k estrellas, v13.3.1).
- **Cuándo elegirlo:** Casos: Observar consumo de un servicio; Compartir métricas de una operación.
- **Requisitos:** nivel 2: servidor de paneles: hay que conectar fuentes de datos; Servidor o cuenta Cloud; fuente de métricas; permisos de consulta; hardware prerequisites; API de IA: no; Servidor o cuenta Cloud; fuente de métricas; permisos de consulta.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://grafana.com/docs/grafana/latest/setup-grafana/installation/
- **Primera prueba propuesta (no ejecutada):** Conecta una fuente de prueba y grafica una métrica con un rango temporal explícito Éxito: El panel coincide con la consulta y cambia al ajustar el periodo
- **Combina con:** `langfuse` [23/observabilidad], `supabase` [22/infraestructura], `umami` [10/producto]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. AGPL: ofrecerlo modificado como servicio obliga a publicar cambios. Grafana visualiza fuentes existentes; no recopila automáticamente todos los datos de tus sistemas.

### metabase (`metabase`)

- **Repo:** https://github.com/metabase/metabase · AGPL-3.0 + licencia comercial (enterprise/) · nivel 2 · 67/100 · alternativa en «BI y dashboards»
- **Qué es:** Metabase, herramienta open source de BI y paneles. La edición open source es AGPL y el repo incluye también código de las ediciones comerciales (GitHub muestra NOASSERTION). Es muy madura (~50k estrellas, v0.65.4).
- **Cuándo elegirlo:** Casos: Explorar ventas sin escribir cada consulta SQL; Compartir un informe operativo.
- **Requisitos:** nivel 2: preparación media; Ruta Docker o Java según guía; base de prueba; usuario de lectura; hardware prerequisites; API de IA: no; Ruta Docker o Java según guía; base de prueba; usuario de lectura.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install -g @metabase/cli` — fuente: https://github.com/metabase/metabase/blob/master/docs/data-apps/getting-started.md
- **Primera prueba propuesta (no ejecutada):** Crea una pregunta de suma por categoría usando los datos de ejemplo Éxito: El resultado coincide con las filas y puedes guardarlo en un dashboard
- **Combina con:** `duckdb` [25/datos], `posthog` [10/producto], `echarts` [10/graficos]
- **Alternativas:** `superset`, `redash`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): superset, redash. El repositorio contiene varias ediciones; revisa qué funciones de permisos y embedding incluye tu ruta.

### Evidence (`evidence`)

- **Repo:** https://github.com/evidence-dev/evidence · MIT · nivel 1 · 57/100
- **Qué es:** Herramienta de BI de código abierto (MIT) de Evidence (evidence.dev), con plataforma de publicación comercial (Evidence Studio). Activa.
- **Cuándo elegirlo:** Casos: publicar informes de negocio versionados en git; generar dashboards con SQL que un agente de código puede editar.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://evidence.studio/install.sh | sh` — fuente: https://github.com/evidence-dev/evidence/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Evidence con el script del README, crea un proyecto de ejemplo y abre el servidor local. Éxito: Ves un informe con gráficos generados a partir de las consultas SQL del Markdown.
- **Combina con:** `duckdb` [25/datos], `claude-code` [20/terminal], `supabase` [22/infraestructura]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas cercanas en el catálogo: metabase, superset.

### Redash (`redash`)

- **Repo:** https://github.com/getredash/redash · BSD-2-Clause · nivel 2 · 57/100 · alternativa en «BI y dashboards»
- **Qué es:** Redash, herramienta para consultar fuentes de datos con SQL, visualizar y compartir resultados. Licencia BSD-2-Clause. Es madura (~29k estrellas) y sigue publicando versiones (v26.9.0).
- **Cuándo elegirlo:** Casos: Compartir consultas de negocio; Crear dashboards a partir de fuentes SQL.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Servidor según guía; fuente de datos; SQL básico; hardware prerequisites; API de IA: no; Servidor según guía; fuente de datos; SQL básico.
- **Instalación (documentada en la fuente; no ejecutada):** `docker-compose up -d` — fuente: https://github.com/getredash/redash/blob/master/docs/open-source/setup.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta una consulta sobre una tabla ficticia y conviértela en una gráfica Éxito: Puedes revisar consulta, filas y visualización del mismo resultado
- **Combina con:** `duckdb` [25/datos], `supabase` [22/infraestructura], `activepieces` [1/motores]
- **Alternativas:** `superset`, `metabase`
- **Riesgos y avisos:** Alternativas (elige una): metabase, superset. La facilidad de consumir un dashboard no elimina la necesidad de preparar consultas y conexiones correctas.

### WrenAI (`wrenai`)

- **Repo:** https://github.com/Canner/WrenAI · Multilicencia por ruta (Apache-2.0, AGPL-3.0, CC-BY-4.0) · nivel 2 · 57/100
- **Qué es:** WrenAI, motor de BI generativo (GenBI) de Canner. El motor (capa semántica MDL, text-to-SQL, MCP, CLI y conectores) es Apache-2.0 y las funciones de seguridad fina y la UI GenBI son comerciales (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Definir ingresos de forma consistente; Crear dashboards desde preguntas de negocio.
- **Requisitos:** nivel 2: preparación media; Python; Node para skills; base o muestra jaffle_shop; agente; hardware prerequisites; API de IA: depends; Python; Node para skills; base o muestra jaffle_shop; agente.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Canner/WrenAI/blob/main/README.md

  ```bash
  pip install wrenai

  npx skills add Canner/WrenAI
  ```
- **Primera prueba propuesta (no ejecutada):** Pide usar la muestra jaffle_shop y explica una métrica antes de generar su consulta Éxito: Puedes revisar definición, SQL y resultado sobre la muestra
- **Combina con:** `claude-code` [20/terminal], `duckdb` [25/datos], `langchain` [3/py], `superset`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Funciones de seguridad a nivel de fila/columna solo en ediciones de pago. La capa semántica no garantiza SQL correcto sin definiciones y revisión; la guía actual usa CLI más skills, no solo una app de chat.

### echarts (`echarts`)

- **Repo:** https://github.com/apache/echarts · Apache-2.0 · nivel 2 · 71/100 · recomendado en «Librerías de gráficos»
- **Qué es:** Apache ECharts, librería de visualización de la Apache Software Foundation. Licencia Apache-2.0. Es muy madura (~68k estrellas, 6.1.0).
- **Cuándo elegirlo:** Casos: Construir un dashboard interactivo; Combinar mapa y estadísticas en una web.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; JavaScript; contenedor con tamaño; datos; hardware prerequisites; API de IA: no; JavaScript; contenedor con tamaño; datos.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install echarts --save` — fuente: https://github.com/apache/echarts/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una serie de ventas y añade una segunda para comparar Éxito: La leyenda distingue ambas series y el tooltip muestra valores correctos
- **Combina con:** `metabase` [10/bi], `superset` [10/bi], `heroui` [9/componentes], `ant-design` [9/componentes], `awesome-dataviz` [10/recursos], `dash` [25/apps]
- **Alternativas:** `d3`, `recharts`, `chart-js`
- **Riesgos y avisos:** Alternativas (elige una): d3, chart-js, recharts. Npm install del README prepara el desarrollo del repositorio; sigue el handbook para integrar ECharts en tu app.

### D3.js (`d3`)

- **Repo:** https://github.com/d3/d3 · ISC · nivel 2 · 70/100 · alternativa en «Librerías de gráficos»
- **Qué es:** D3 (Data-Driven Documents), librería JavaScript de bajo nivel para visualización de datos. Licencia ISC. Es infraestructura muy madura (~114k estrellas, v7.9.2).
- **Cuándo elegirlo:** Casos: Diseñar una visualización a medida; Explorar relaciones entre datos con interacción.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; JavaScript; HTML/SVG o Canvas; datos de prueba; hardware prerequisites; API de IA: no; JavaScript; HTML/SVG o Canvas; datos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `yarn add d3` — fuente: https://github.com/d3/d3/blob/main/docs/getting-started.md
- **Primera prueba propuesta (no ejecutada):** Construye un gráfico de barras de tres categorías con escala y ejes explícitos Éxito: Cada barra y etiqueta corresponde a su valor
- **Combina con:** `recharts`, `awesome-dataviz` [10/recursos], `marimo` [25/apps]
- **Alternativas:** `echarts`, `recharts`, `chart-js`
- **Riesgos y avisos:** Alternativas (elige una): echarts. Curva de aprendizaje alta. Ofrece piezas de bajo nivel; exige más programación que una biblioteca de gráficos ya montados.

### Recharts (`recharts`)

- **Repo:** https://github.com/recharts/recharts · MIT · nivel 2 · 69/100 · alternativa en «Librerías de gráficos»
- **Qué es:** Recharts, librería de gráficos para React construida con D3. Licencia MIT. Es madura (~28k estrellas, v3.10.1).
- **Cuándo elegirlo:** Casos: Visualizar una serie de ventas; Comparar categorías en un dashboard React.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; React; Node; react-is compatible; datos de prueba; hardware prerequisites; API de IA: no; React; Node; react-is compatible; datos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/recharts/recharts/blob/main/README.md

  ```sh
  # latest stable
  npm install recharts react-is
  ```
- **Primera prueba propuesta (no ejecutada):** Dibuja una línea con cinco valores y comprueba etiquetas y tooltip Éxito: Los puntos corresponden a los datos y el gráfico cabe en móvil
- **Combina con:** `ui` [9/componentes], `d3`, `tailwindcss` [9/estilos], `mui` [9/componentes], `mantine` [9/componentes]
- **Alternativas:** `echarts`, `d3`, `chart-js`
- **Riesgos y avisos:** Alternativas (elige una): chart-js, echarts. El signo $ del ejemplo es un indicador de terminal y no parte del comando; ajusta react-is a la versión de React.

### Chart.js (`chart-js`)

- **Repo:** https://github.com/chartjs/Chart.js · MIT · nivel 2 · 64/100 · alternativa en «Librerías de gráficos»
- **Qué es:** Chart.js, librería JavaScript de gráficos sobre Canvas para diseñadores y desarrolladores. Licencia MIT. Es muy madura (~68k estrellas, v4.6.1).
- **Cuándo elegirlo:** Casos: Añadir gráficos a una página sencilla; Comparar resultados por periodo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; JavaScript; canvas; gestor npm o script distribuido; hardware prerequisites; API de IA: no; JavaScript; canvas; gestor npm o script distribuido.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install chart.js` — fuente: https://github.com/chartjs/Chart.js/blob/master/docs/getting-started/installation.md
- **Primera prueba propuesta (no ejecutada):** Muestra un gráfico con tres categorías y cambia un valor Éxito: El gráfico se actualiza y conserva etiquetas y leyenda
- **Combina con:** `tailwindcss` [9/estilos], `duckdb` [25/datos], `supabase` [22/infraestructura]
- **Alternativas:** `echarts`, `d3`, `recharts`
- **Riesgos y avisos:** Alternativas (elige una): echarts, recharts. El canvas necesita tamaño y alternativa textual adecuados para comunicar los datos a todos los usuarios.

### uPlot (`uplot`)

- **Repo:** https://github.com/leeoniya/uPlot · MIT · nivel 2 · 56/100
- **Qué es:** μPlot, librería compacta de gráficos de series temporales sobre Canvas 2D, de @leeoniya. Licencia MIT. Es madura (~11k estrellas, 1.6.32).
- **Cuándo elegirlo:** Casos: Mostrar métricas temporales de un sensor; Comparar rendimiento de gráficas con tus propios datos.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; JavaScript; datos temporales ordenados; estilos y build distribuidos; hardware prerequisites; API de IA: no; JavaScript; datos temporales ordenados; estilos y build distribuidos.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/leeoniya/uPlot/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Grafica una serie de cien puntos y comprueba tiempos y escala Éxito: El cursor y los valores corresponden a los datos originales
- **Combina con:** `grafana` [10/bi], `swr` [9/componentes], `duckdb` [25/datos]
- **Riesgos y avisos:** Sin alternativas declaradas. Las cifras de rapidez del autor dependen de datos, navegador y equipo; no se garantiza rendimiento sin penalización.

### awesome-dataviz (`awesome-dataviz`)

- **Repo:** https://github.com/hal9ai/awesome-dataviz · CC-BY-4.0 · nivel 1 · 58/100
- **Qué es:** Awesome Dataviz, lista curada de frameworks, librerías y software de visualización open source, creada por @fasouto y mantenida con patrocinio de Hal9. Licencia CC BY 4.0 (GitHub muestra NOASSERTION). Tiene ~4.5k estrellas.
- **Cuándo elegirlo:** Casos: Encontrar una biblioteca de mapas; Comparar gráficos para React y JavaScript.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; tipo de gráfico y framework objetivo; hardware prerequisites; API de IA: no; Navegador; tipo de gráfico y framework objetivo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/hal9ai/awesome-dataviz/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Selecciona dos bibliotecas de un mismo tipo y compara licencia, accesibilidad y formato de datos Éxito: Tienes candidatos con documentación original y requisitos identificados
- **Combina con:** `echarts` [10/graficos], `d3` [10/graficos], `awesome-bigdata`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. El directorio reúne opciones; no se instala completo ni verifica automáticamente la calidad de cada enlace.

### awesome-bigdata (`awesome-bigdata`)

- **Repo:** https://github.com/oxnr/awesome-bigdata · MIT · nivel 1 · 46/100
- **Qué es:** Awesome Big Data, lista curada de frameworks, bases de datos y recursos de big data, mantenida por @oxnr desde 2014. Licencia MIT. Tiene ~15k estrellas y recibe contribuciones activas.
- **Cuándo elegirlo:** Casos: Explorar el ecosistema de datos; Comparar motores antes de montar infraestructura.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; problema de datos definido; hardware prerequisites; API de IA: no; Navegador; problema de datos definido.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/oxnr/awesome-bigdata/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Busca una herramienta de streaming y otra de almacenamiento y compara qué función resuelve cada una Éxito: Puedes elegir candidatos complementarios
- **Combina con:** `awesome-dataviz`, `duckdb` [25/datos], `hudi` [25/datos]
- **Riesgos y avisos:** Sin alternativas declaradas. Recurso, no software. No se instala la colección entera ni se hereda la compatibilidad de sus enlaces.

### data-analyst-roadmap (`data-analyst-roadmap`)

- **Repo:** https://github.com/mtahiraslan/data-analyst-roadmap · MIT · nivel 1 · 38/100
- **Qué es:** Hoja de ruta para aprender análisis de datos, de @mtahiraslan. Licencia MIT. Es pequeña (~1k estrellas) y su último cambio es de octubre de 2025.
- **Cuándo elegirlo:** Casos: Organizar un plan inicial de estudio; Identificar conocimientos para un primer proyecto.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; tiempo de estudio; una tabla pequeña de práctica; hardware prerequisites; API de IA: no; Navegador; tiempo de estudio; una tabla pequeña de práctica.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/mtahiraslan/data-analyst-roadmap/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige SQL o una hoja de cálculo y resuelve una pregunta con una tabla ficticia Éxito: Puedes explicar dato de entrada, cálculo y resultado
- **Combina con:** `duckdb` [25/datos], `marimo` [25/apps], `metabase` [10/bi]
- **Riesgos y avisos:** Sin alternativas declaradas. Recurso introductorio, sin mantenimiento reciente. Es una ruta basada en experiencia del autor, no una garantía de empleo ni un programa que debas completar entero.

### gods-eye-view (`gods-eye-view`)

- **Repo:** https://github.com/bilawalsidhu/gods-eye-view · MIT (solo código) · nivel 2 · 68/100 · recomendado en «Paneles OSINT sobre globo 3D»
- **Qué es:** God's Eye View, visualizador geoespacial en un globo 3D que reúne datos abiertos en tiempo real, de @bilawalsidhu. Licencia MIT (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Explorar información geoespacial pública; Consultar el globo desde un agente MCP.
- **Requisitos:** nivel 2: preparación media; Node y npm; WebGL; claves opcionales para datos o voz; app local para MCP; hardware prerequisites; API de IA: opcional; Node y npm; WebGL; claves opcionales para datos o voz; app local para MCP.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/bilawalsidhu/gods-eye-view/blob/main/README.md

  ```bash
  git clone https://github.com/bilawalsidhu/gods-eye-view.git
  cd gods-eye-view
  npm ci
  npm run doctor
  npm run dev
  ```
- **Primera prueba propuesta (no ejecutada):** Abre una capa pública y contrasta un objeto del globo con su fuente y hora de actualización Éxito: Puedes identificar qué datos son reales, simulados o no disponibles
- **Combina con:** `claude-code` [20/terminal], `hermes-agent` [21/asistentes], `pythia`
- **Alternativas:** `osiris`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativa (elige una): osiris. El seguimiento de cámaras y ALPR plantea cuestiones de privacidad. MCP de Claude y Codex sí está documentado; reutilizar sesión OAuth para voz es otra función experimental y no acredita un contrato Realtime cubierto por tu plan.

### Sherlock (`sherlock`)

- **Repo:** https://github.com/sherlock-project/sherlock · MIT · nivel 1 · 67/100 · recomendado en «Búsqueda de usuarios en redes sociales»
- **Qué es:** Herramienta OSINT de código abierto (MIT) mantenida por el Sherlock Project y su comunidad. Muy popular; el README advierte de que los paquetes de terceros para ParrotOS y Ubuntu 24.04 parecen estar rotos.
- **Cuándo elegirlo:** Casos: comprobar dónde está registrado un nombre de usuario propio o de tu marca; iniciar una investigación OSINT autorizada a partir de un alias.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pipx install sherlock-project` — fuente: https://github.com/sherlock-project/sherlock/blob/master/docs/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pipx install sherlock-project` y busca un nombre de usuario propio. Éxito: La salida lista las URL de los perfiles encontrados y guarda un archivo de resultados.
- **Combina con:** `theharvester`, `claude-code` [20/terminal], `duckdb` [25/datos]
- **Alternativas:** `maigret`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Alternativas (elige una): maigret.

### theHarvester (`theharvester`)

- **Repo:** https://github.com/laramies/theHarvester · GPL-2.0 · nivel 2 · 66/100
- **Qué es:** Herramienta OSINT de código abierto (solo GPL-2.0) creada por Christian Martorella (laramies) y mantenida por la comunidad desde hace años. Activa; requiere Python 3.14 y uv.
- **Cuándo elegirlo:** Casos: inventariar la superficie expuesta de tu propio dominio; fase inicial de reconocimiento en una auditoría de seguridad autorizada.
- **Requisitos:** nivel 2: preparación sencilla, varios servicios con Docker Compose; Python, Dockerfile, docker-compose.yml, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up --build -d` — fuente: https://github.com/laramies/theHarvester/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repositorio, ejecuta `uv sync` y lanza la búsqueda de ejemplo con las fuentes pasivas crtsh y certspotter sobre un dominio propio. Éxito: La terminal informa del resultado de cada fuente y lista subdominios encontrados.
- **Combina con:** `sherlock`, `maigret`, `katana` [4/crawlers], `recon-ng`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Alternativa cercana: recon-ng (framework modular de reconocimiento).

### Maigret (`maigret`)

- **Repo:** https://github.com/soxoj/maigret · MIT · nivel 1 · 63/100 · alternativa en «Búsqueda de usuarios en redes sociales»
- **Qué es:** Herramienta OSINT de código abierto (MIT) creada por soxoj, derivada de Sherlock y ampliada. Activa; el autor advierte de que las comprobaciones de sitios se rompen con el tiempo y requieren mantenimiento.
- **Cuándo elegirlo:** Casos: auditar la huella pública de un alias propio; investigaciones OSINT autorizadas que requieren un informe consolidado.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install maigret` — fuente: https://github.com/soxoj/maigret/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install maigret` (Python 3.10+) y busca un alias propio con salida HTML. Éxito: Se genera un informe HTML con los perfiles encontrados y los datos extraídos.
- **Combina con:** `theharvester`, `claude-code` [20/terminal], `duckdb` [25/datos]
- **Alternativas:** `sherlock`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): sherlock. El README incluye patrocinios de proxies y servicios de pago no necesarios para la herramienta.

### osiris (`osiris`)

- **Repo:** https://github.com/simplifaisoul/osiris · MIT · nivel 2 · 53/100 · alternativa en «Paneles OSINT sobre globo 3D»
- **Qué es:** OSIRIS (Open Source Intelligence & Reconnaissance Integrated System), panel OSINT en tiempo real de @simplifaisoul. Licencia MIT. Es reciente (creado en mayo de 2026, ~12k estrellas, v5.0.0).
- **Cuándo elegirlo:** Casos: Explorar noticias por ubicación; Comparar eventos públicos en un globo.
- **Requisitos:** nivel 2: preparación media; Node y npm; conexión a fuentes públicas; claves opcionales para capas extra; hardware prerequisites; API de IA: opcional; Node y npm; conexión a fuentes públicas; claves opcionales para capas extra.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/simplifaisoul/osiris/blob/master/README.md

  ```bash
  git clone https://github.com/simplifaisoul/osiris.git
  cd osiris
  npm install
  npm run dev
  ```
- **Primera prueba propuesta (no ejecutada):** Activa una capa pública y contrasta un evento con la fuente original y su fecha Éxito: Puedes identificar origen y actualización del evento en el mapa
- **Combina con:** `pythia`, `hermes-agent` [21/asistentes], `claude-code` [20/terminal]
- **Alternativas:** `gods-eye-view`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Alternativa (elige una): gods-eye-view. El acceso a cámaras públicas plantea cuestiones de privacidad y uso responsable. La etiqueta tiempo real no garantiza latencia ni precisión de todas las fuentes; el MCP expone acciones y debe configurarse aparte.

### Pythia (`pythia`)

- **Repo:** https://github.com/jangles-byte/Pythia · MIT · nivel 3 · 47/100
- **Qué es:** PYTHIA, plataforma local de predicción geopolítica de @jangles-byte que fusiona MiroFish (motor de predicción por inteligencia de enjambre) y Osiris (panel de inteligencia global). Licencia MIT.
- **Cuándo elegirlo:** Casos: Resumir fuentes públicas con un LLM local; Comparar escenarios sobre un conjunto de eventos.
- **Requisitos:** nivel 3: preparación pesada; Ollama con modelo descargado; Python y uv; checkout Osiris; dependencias del script; hardware prerequisites; API de IA: no; Ollama con modelo descargado; Python y uv; checkout Osiris; dependencias del script.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/jangles-byte/Pythia/blob/main/README.md

  ```bash
  git clone https://github.com/jangles-byte/Pythia && cd Pythia
  cp .env.example .env          # sensible defaults — no keys needed
  ./run-all.sh                  # starts Osiris + the engine and opens the UI
  ```
- **Primera prueba propuesta (no ejecutada):** Consulta un resumen del estado observado y separa los eventos de los escenarios generados Éxito: Cada evento tiene origen y los escenarios se identifican como hipótesis
- **Combina con:** `osiris`, `mirofish` [3/experimentos], `ollama` [8/motores], `claude-code` [20/terminal], `gods-eye-view`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Sin alternativas declaradas. Las predicciones de LLM no son análisis de inteligencia verificados. Las predicciones son resultados generados y no probabilidades verificadas; MCP stdio permite consultar el motor desde los clientes.

### Recon-ng (`recon-ng`)

- **Repo:** https://github.com/lanmaster53/recon-ng · GPL-3.0 · nivel 2 · 44/100
- **Qué es:** Framework de reconocimiento de código abierto (GPL-3.0) creado por Tim Tomes (lanmaster53). Maduro, con ritmo de cambios bajo (último push en octubre de 2026).
- **Cuándo elegirlo:** Casos: organizar un reconocimiento OSINT autorizado en espacios de trabajo reproducibles; automatizar consultas a varias fuentes con módulos y claves de API.
- **Requisitos:** nivel 2: preparación media; Python, Dockerfile, docker-compose.yml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/lanmaster53/recon-ng/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala las dependencias del README, crea un espacio de trabajo e instala un módulo pasivo del marketplace. Éxito: El módulo se ejecuta y sus resultados aparecen en la tabla correspondiente del espacio de trabajo.
- **Combina con:** `theharvester`, `duckdb` [25/datos], `claude-code` [20/terminal]
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Ritmo de mantenimiento bajo: comprueba que los módulos que necesitas siguen funcionando.

### Leaflet (`leaflet`)

- **Repo:** https://github.com/Leaflet/Leaflet · BSD-2-Clause · nivel 2 · 70/100 · recomendado en «Mapas web interactivos»
- **Qué es:** Biblioteca de código abierto (BSD-2-Clause) creada en 2010 por Volodymyr Agafonkin y mantenida por la comunidad Leaflet. La biblioteca de mapas web interactivos más extendida; muy madura.
- **Cuándo elegirlo:** Casos: añadir un mapa con marcadores y popups a una web; publicar datos GeoJSON propios sobre un mapa base de OpenStreetMap.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; JavaScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `npm install leaflet@beta` — fuente: https://github.com/Leaflet/Leaflet/blob/main/docs/install.md
- **Primera prueba propuesta (no ejecutada):** Crea una página HTML con Leaflet desde CDN, un mapa de OpenStreetMap y un marcador. Éxito: El mapa se desplaza y amplía y el marcador muestra su popup al hacer clic.
- **Combina con:** `webodm`, `qgis`, `claude-code` [20/terminal], `nicegui` [25/apps]
- **Alternativas:** `maplibre`
- **Riesgos y avisos:** Alternativas (elige una): maplibre (mapas vectoriales con WebGL).

### MapLibre GL JS (`maplibre`)

- **Repo:** https://github.com/maplibre/maplibre-gl-js · BSD-3-Clause · nivel 2 · 67/100 · alternativa en «Mapas web interactivos»
- **Qué es:** Biblioteca de código abierto (BSD-3-Clause) de la organización MapLibre, creada como fork de mapbox-gl-js cuando este pasó a una licencia no libre en diciembre de 2020. Madura y con amplio respaldo.
- **Cuándo elegirlo:** Casos: publicar mapas vectoriales con estilo propio sin depender de un proveedor; crear mapas 3D con edificios y terreno en una web.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; TypeScript, docker-compose.yml, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/maplibre/maplibre-gl-js/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una página con MapLibre desde unpkg y el estilo de demostración de MapLibre. Éxito: El mapa vectorial se carga, rota e inclina con el ratón.
- **Combina con:** `deck.gl`, `kepler.gl`, `qgis`
- **Alternativas:** `leaflet`
- **Riesgos y avisos:** Alternativas (elige una): leaflet.

### kepler.gl (`kepler.gl`)

- **Repo:** https://github.com/keplergl/kepler.gl · MIT · nivel 1 · 66/100
- **Qué es:** Aplicación de análisis geoespacial de código abierto (MIT), creada en Uber y hoy proyecto de la OpenJS Foundation dentro del ecosistema vis.gl. Activa.
- **Cuándo elegirlo:** Casos: explorar millones de viajes o eventos geolocalizados en el navegador; incrustar un explorador de mapas en una aplicación React o en un cuaderno.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install --save @kepler.gl/components maplibre-gl` — fuente: https://github.com/keplergl/kepler.gl/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Abre la demo de kepler.gl y carga un CSV con columnas de latitud y longitud. Éxito: El mapa crea capas automáticamente y permite filtrar por tiempo.
- **Combina con:** `deck.gl`, `maplibre`, `jupyterlab` [25/datos], `claude-code` [20/terminal]
- **Riesgos y avisos:** La demo procesa los datos en el navegador; revisa memoria con conjuntos muy grandes.

### deck.gl (`deck.gl`)

- **Repo:** https://github.com/visgl/deck.gl · MIT · nivel 2 · 65/100
- **Qué es:** Framework de visualización de código abierto (MIT) del grupo vis.gl de la OpenJS Foundation, creado originalmente en Uber. Maduro y activo.
- **Cuándo elegirlo:** Casos: visualizar millones de puntos geográficos con interacción fluida; crear mapas 3D de densidad o rutas en una web o cuaderno.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; TypeScript, package.json; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `npm install deck.gl` — fuente: https://github.com/visgl/deck.gl/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala `npm install deck.gl` o `pip install pydeck` y dibuja una capa de puntos con datos de ejemplo. Éxito: El mapa muestra los puntos y permite seleccionar uno con el ratón.
- **Combina con:** `maplibre`, `kepler.gl`, `superset` [10/bi], `jupyterlab` [25/datos], `panel` [25/apps]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Para mapas base comerciales revisa las condiciones y claves del proveedor.

### QGIS (`qgis`)

- **Repo:** https://github.com/qgis/QGIS · GPL-2.0 · nivel 1 · 61/100
- **Qué es:** SIG de escritorio de código abierto (GPL-2.0 o posterior) desarrollado por la comunidad QGIS y miembro de OSGeo. Muy maduro, con versiones LTR y regulares.
- **Cuándo elegirlo:** Casos: preparar y analizar capas geográficas para un estudio o mapa impreso; publicar servicios de mapas WMS/WFS con QGIS Server.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; C++, CMakeLists.txt, requirements.txt; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/qgis/QGIS.git` — fuente: https://github.com/qgis/QGIS/blob/master/INSTALL.md
- **Primera prueba propuesta (no ejecutada):** Instala QGIS, carga una capa GeoJSON y un mapa base, y exporta un mapa en PDF. Éxito: El PDF contiene el mapa con la capa estilizada, leyenda y escala.
- **Combina con:** `leaflet`, `maplibre`, `webodm`, `duckdb` [25/datos]
- **Riesgos y avisos:** Curva de aprendizaje alta para análisis avanzado; la documentación oficial y los tutoriales de la comunidad son amplios.

### WebODM (`webodm`)

- **Repo:** https://github.com/WebODM/WebODM · AGPL-3.0 · nivel 3 · 60/100 · recomendado en «Fotogrametría con drones»
- **Qué es:** WebODM, software de procesamiento de imágenes de drones con interfaz web, liderado por @pierotofy. Licencia AGPL-3.0. Es maduro (~4.3k estrellas, v4.0.1) y desde abril de 2026 es independiente de OpenDroneMap.
- **Cuándo elegirlo:** Casos: Procesar imágenes de dron desde una interfaz; Comparar resultados de dos vuelos de práctica.
- **Requisitos:** nivel 3: preparación pesada; Instalador oficial o Docker; RAM y disco según fotografías; dataset de prueba; hardware prerequisites; API de IA: no; Instalador oficial o Docker; RAM y disco según fotografías; dataset de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/WebODM/WebODM --config core.autocrlf=input --depth 1` — fuente: https://docs.webodm.org/installation/#hardware-requirements
- **Primera prueba propuesta (no ejecutada):** Carga un conjunto pequeño de fotos propias y revisa el informe de procesamiento Éxito: Puedes abrir ortofoto, nube y reporte de calidad del mismo trabajo
- **Combina con:** `blender` [26/creacion-3d], `three.js` [26/animacion], `marimo` [25/apps], `leaflet`, `qgis`
- **Alternativas:** `odm`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. La combinación previa webodm → odm queda obsoleta: WebODM usa ODX, no ODM. El autor distingue los instaladores actuales de productos cobrados por terceros; no extrapoles tutoriales antiguos sin comprobar el origen.

### ODM (`odm`)

- **Repo:** https://github.com/OpenDroneMap/ODM · AGPL-3.0 · nivel 2 · 58/100 · alternativa en «Fotogrametría con drones»
- **Qué es:** ODM (OpenDroneMap), kit de línea de comandos para procesar imágenes aéreas de drones. Licencia AGPL-3.0. Es maduro (~6.6k estrellas, v3.6.2).
- **Cuándo elegirlo:** Casos: Crear un mapa a partir de fotos de dron; Producir una nube de puntos para inspección.
- **Requisitos:** nivel 2: preparación media; Docker; fotografías aéreas propias con solapamiento; RAM y disco según lote; hardware prerequisites; API de IA: no; Docker; fotografías aéreas propias con solapamiento; RAM y disco según lote.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/OpenDroneMap/ODM/blob/master/README.md

  ```bash
  # Windows
  docker run -ti --rm -v c:/Users/youruser/datasets:/datasets opendronemap/odm --project-path /datasets project
  ```
- **Primera prueba propuesta (no ejecutada):** Procesa un lote pequeño de imágenes de prueba y abre la ortofoto y nube de puntos Éxito: Puedes inspeccionar alineación, cobertura y errores visibles
- **Combina con:** `blender` [26/creacion-3d], `three.js` [26/animacion], `marimo` [25/apps]
- **Alternativas:** `webodm`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. Desde abril de 2026, WebODM ya no es su interfaz (ver ficha de webodm). El ejemplo Windows necesita sustituir la ruta del dataset y su carpeta de proyecto; el resultado depende de la calidad de las tomas.

### GlobalBuildingAtlas (`globalbuildingatlas`)

- **Repo:** https://github.com/zhu-xlab/GlobalBuildingAtlas · MIT + Commons Clause · nivel 1 · 32/100
- **Qué es:** GlobalBuildingAtlas, dataset global de edificios en nivel de detalle LoD1 (polígonos, alturas y modelos 3D) del grupo zhu-xlab (TUM). Tiene licencias mixtas: polígonos ODbL más polígonos, LoD1 y mapas de altura CC BY-NC 4.0 (GitHub muestra…
- **Cuándo elegirlo:** Casos: Explorar edificios en un GIS; Preparar una escena urbana de prueba.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador o GIS; espacio de descarga; zona pequeña; licencia de la capa; hardware prerequisites; API de IA: no; Navegador o GIS; espacio de descarga; zona pequeña; licencia de la capa.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/zhu-xlab/GlobalBuildingAtlas/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Selecciona una zona y distingue polígonos, alturas y LoD1 antes de descargar una capa Éxito: Puedes identificar formato, licencia y escala del dato
- **Combina con:** `three.js` [26/animacion], `duckdb` [25/datos], `3dviz-pro-max` [27/skills]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Ojo con la parte CC BY-NC para usos comerciales. GBA.ODbLPolygon usa ODbL, mientras otras capas de polígonos, LoD1 y alturas usan CC BY-NC 4.0; no toda la colección permite el mismo uso comercial.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-10.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Dashboards, analítica y mapas», lee `docs/alexandria/categoria-10.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-10.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
