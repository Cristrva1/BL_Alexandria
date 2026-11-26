# Alexandría para agentes · BI, dashboards y chat con datos

Categoría 10 «Dashboards, analítica y mapas» › subcategoría `bi`. 6 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=10&sub=bi · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `superset` | Plataforma de exploración y visualización de datos de Apache, alternativa… | 2 Intermedio | 82 | Apache-2.0 (OSI permisiva) | recomendado |
| `grafana` | Plataforma de visualización y observabilidad para métricas, logs y trazas de… | 2 Intermedio | 80 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `metabase` | Herramienta de dashboards y BI para explorar métricas de negocio conectando… | 2 Intermedio | 67 | AGPL-3.0 + licencia comercial (enterprise/) (open-core) | alternativa |
| `evidence` | BI como código: informes y visualizaciones interactivas escritos en SQL y… | 1 Básico | 57 | MIT (OSI permisiva) | sin grupo |
| `redash` | Herramienta para consultar cualquier fuente de datos con SQL, visualizar y… | 2 Intermedio | 57 | BSD-2-Clause (OSI permisiva) | alternativa |
| `wrenai` | BI generativo: convierte preguntas en SQL fiable a través de una capa semántica… | 2 Intermedio | 57 | Multilicencia por ruta (Apache-2.0, AGPL-3.0, CC-BY-4.0) (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-10-bi.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «BI, dashboards y chat con datos», lee `docs/alexandria/categoria-10-bi.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-10-bi.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
