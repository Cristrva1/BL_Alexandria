# Alexandría para agentes · Automatizar procesos y crear herramientas internas

Categoría 1 completa (19 repos, 2 subcategorías). Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=1 · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `airflow` | motores | Orquestador de workflows de la Apache Software Foundation: DAGs en Python con… | 3 Avanzado | 81 | Apache-2.0 (OSI permisiva) | recomendado |
| `kestra` | motores | Orquestador declarativo de workflows en YAML para datos, infraestructura y… | 2 Intermedio | 80 | Apache-2.0 (OSI permisiva) | alternativa |
| `prefect` | motores | Framework de orquestación en Python: convierte scripts en flujos con… | 2 Intermedio | 68 | Apache-2.0 (OSI permisiva) | alternativa |
| `trigger-dev` | motores | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en… | 2 Intermedio | 68 | Apache-2.0 (OSI permisiva) | alternativa |
| `temporal` | motores | Plataforma de ejecución duradera: workflows en código que sobreviven a fallos… | 2 Intermedio | 67 | MIT (OSI permisiva) | sin grupo |
| `activepieces` | motores | Plataforma open-source de automatización con IA, alternativa extensible a… | 2 Intermedio | 64 | MIT + licencia Enterprise (packages/ee/) (open-core) | sin grupo |
| `dagger` | motores | Pipelines de entrega como código con contenedores: SDKs en 8 lenguajes, cache… | 2 Intermedio | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `node-red` | motores | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras… | 1 Básico | 64 | Apache-2.0 (OSI permisiva) | recomendado |
| `huginn` | motores | Sistema de agentes self-hosted para automatizar tareas online y reaccionar a… | 2 Intermedio | 63 | MIT (OSI permisiva) | alternativa |
| `windmill` | motores | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y… | 2 Intermedio | 61 | AGPL-3.0 / Apache-2.0 + licencia propietaria (enterprise) (open-core) | alternativa |
| `dagster` | motores | Orquestador de datos orientado a activos: declaras tablas, modelos o informes… | 2 Intermedio | 57 | Apache-2.0 (OSI permisiva) | alternativa |
| `celery` | motores | Envía trabajos Python a una cola para que procesos separados los ejecuten y la… | 2 Intermedio | — | BSD-3-Clause | sin grupo |
| `tooljet` | internas | Plataforma low-code para herramientas internas, dashboards y flujos, con… | 2 Intermedio | 75 | AGPL-3.0 (OSI copyleft) | recomendado |
| `appsmith` | internas | Plataforma low-code para crear paneles de administración y herramientas… | 3 Avanzado | 72 | Apache-2.0 (OSI permisiva) | alternativa |
| `nocodb` | internas | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de… | 1 Básico | 70 | Sustainable Use License (no OSI) (source-available) | alternativa |
| `budibase` | internas | Plataforma open source para apps internas, automatizaciones y agentes de IA… | 2 Intermedio | 62 | GPL-3.0 + BSL (packages/pro) (source-available) | alternativa |
| `teable` | internas | Base de datos colaborativa sin código sobre PostgreSQL, con vistas tipo hoja… | 2 Intermedio | 56 | AGPL-3.0 (OSI copyleft) | alternativa |
| `grist-core` | internas | Hoja de cálculo relacional autoalojable con fórmulas en Python, columnas… | 1 Básico | 53 | Apache-2.0 (OSI permisiva) | alternativa |
| `baserow` | internas | Base de datos sin código autoalojable (Django y Vue) con constructor de… | 1 Básico | 50 | MIT (open-core) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Apache Airflow (`airflow`)

- **Repo:** https://github.com/apache/airflow · Apache-2.0 · nivel 3 · 81/100 · recomendado en «Orquestadores de workflows de datos y tareas»
- **Qué es:** Plataforma de orquestación de workflows de la Apache Software Foundation (Apache-2.0), creada en Airbnb en 2014 y proyecto de nivel superior de Apache. Muy madura y usada en producción por miles de organizaciones; la serie 3.x es la actual.
- **Cuándo elegirlo:** Casos: programar un ETL diario que descarga, transforma y carga datos en un almacén; coordinar entrenamientos y despliegues de modelos con dependencias y reintentos.
- **Requisitos:** nivel 3: preparación pesada; Python, Dockerfile, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install 'apache-airflow==3.4.0' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.4.0/constraints-3.10.txt"` — fuente: https://github.com/apache/airflow/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Levanta un entorno local de pruebas siguiendo la guía oficial y ejecuta un DAG de ejemplo con dos tareas dependientes. Éxito: El DAG aparece en la interfaz, ambas tareas terminan en verde y puedes leer sus logs.
- **Combina con:** `duckdb` [25/datos], `polars` [25/datos], `grafana` [10/bi], `mlflow` [23/observabilidad], `claude-code` [20/terminal], `dbt` [25/datos]
- **Alternativas:** `kestra`, `prefect`, `trigger-dev`, `windmill`, `dagster`
- **Riesgos y avisos:** Alternativas (elige una): prefect, dagster, kestra. Instalar sin el archivo de constraints suele romper dependencias.

### Kestra (`kestra`)

- **Repo:** https://github.com/kestra-io/kestra · Apache-2.0 · nivel 2 · 80/100 · alternativa en «Orquestadores de workflows de datos y tareas»
- **Qué es:** Plataforma de orquestación de código abierto (Apache 2.0) para flujos de datos, IA e infraestructura, mantenida por Kestra Technologies. Existe desde 2019, publicó la serie 2.0 en 2026 y tiene una edición Enterprise con RBAC y políticas de…
- **Cuándo elegirlo:** Casos: Programar una importación diaria de archivos con reintentos; Combinar tareas de datos con una consulta a un modelo Ollama.
- **Requisitos:** nivel 2: preparación media; Docker;  directorio temporal y volúmenes de prueba; hardware prerequisites; API de IA: opcional; Docker; directorio temporal y volúmenes de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/kestra-io/kestra/blob/develop/README.md

  ```powershell
  docker run --pull=always --rm -it -p 8080:8080 --user=root `
    --name kestra `
    -v "kestra_data:/app/storage" `
    -v "kestra_db:/app/data" `
    -v "/var/run/docker.sock:/var/run/docker.sock" `
    -v "C:/Temp:/tmp" `
    -e KESTRA_PLUGINS_AUTO_INSTALL_ENABLED=true `
    kestra/kestra:latest-slim server local
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta un flujo de ejemplo y abre sus logs en la interfaz de Kestra Éxito: La ejecución muestra su estado final y los mensajes de las tareas
- **Combina con:** `duckdb` [25/datos], `superset` [10/bi], `claude-code` [20/terminal], `ollama` [8/motores]
- **Alternativas:** `airflow`, `prefect`, `trigger-dev`, `windmill`, `dagster`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): windmill, trigger-dev. El arranque rápido monta `/var/run/docker.sock` como root: úsalo solo en entornos de prueba. Expone flows por MCP HTTP con autenticación y permisos; el ejemplo Docker usa root y monta su socket, por lo que requiere un entorno de prueba.

### Prefect (`prefect`)

- **Repo:** https://github.com/PrefectHQ/prefect · Apache-2.0 · nivel 2 · 68/100 · alternativa en «Orquestadores de workflows de datos y tareas»
- **Qué es:** Framework de orquestación de workflows de Prefect Technologies (Apache-2.0), con servidor autoalojable y una nube comercial (Prefect Cloud). Proyecto maduro en su serie 3.x; requiere Python 3.11 o superior según el README.
- **Cuándo elegirlo:** Casos: convertir un script de ingesta en un flujo con reintentos y ejecución programada; encadenar pasos de datos o ML con dependencias dinámicas y observabilidad.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, Dockerfile, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U prefect` — fuente: https://github.com/PrefectHQ/prefect/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install -U prefect`, ejecuta el ejemplo de estrellas de GitHub del README y abre el servidor local. Éxito: El flujo y sus tareas aparecen como completados en la interfaz con sus logs.
- **Combina con:** `duckdb` [25/datos], `polars` [25/datos], `claude-code` [20/terminal], `mlflow` [23/observabilidad]
- **Alternativas:** `airflow`, `kestra`, `trigger-dev`, `windmill`, `dagster`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): airflow, dagster, kestra.

### Trigger.dev (`trigger-dev`)

- **Repo:** https://github.com/triggerdotdev/trigger.dev · Apache-2.0 · nivel 2 · 68/100 · alternativa en «Orquestadores de workflows de datos y tareas»
- **Qué es:** Plataforma de código abierto (Apache 2.0) para crear flujos de IA y tareas en segundo plano en TypeScript. Ofrece un servicio gestionado y guías oficiales de autoalojamiento; publica versiones con frecuencia (serie 4.x).
- **Cuándo elegirlo:** Casos: Procesar en segundo plano un archivo subido por un usuario; Reintentar una tarea de generación cuando falla el proveedor.
- **Requisitos:** nivel 2: preparación media; Proyecto TypeScript;  entorno y cuenta o despliegue indicado por la guía; hardware prerequisites; API de IA: opcional; Proyecto TypeScript; entorno y cuenta o despliegue indicado por la guía.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://trigger.dev/docs/quick-start
- **Primera prueba propuesta (no ejecutada):** Ejecuta la tarea hello-world del README con un mensaje de prueba Éxito: El panel muestra la ejecución y el mensaje en los logs
- **Combina con:** `vercel-ai` [3/ts], `ffmpeg` [12/edicion], `playwright` [32/bibliotecas], `langfuse` [23/observabilidad]
- **Alternativas:** `airflow`, `kestra`, `prefect`, `windmill`, `dagster`
- **Riesgos y avisos:** Alternativas (elige una): windmill, kestra. Es infraestructura de tareas duraderas; no incluye por sí misma un modelo de IA.

### Temporal (`temporal`)

- **Repo:** https://github.com/temporalio/temporal · MIT · nivel 2 · 67/100
- **Qué es:** Servidor de ejecución duradera de código abierto (MIT) desarrollado por Temporal Technologies, la empresa de los creadores de Cadence en Uber, del que es un fork.
- **Cuándo elegirlo:** Casos: procesos de negocio largos como pagos o altas que deben completarse aunque caiga un servicio; agentes de IA con pasos largos que necesitan reintentos y reanudación.
- **Requisitos:** nivel 2: preparación media; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install temporal` — fuente: https://github.com/temporalio/temporal/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala la CLI con `brew install temporal`, arranca el servidor de desarrollo y ejecuta el ejemplo hello-world de un SDK. Éxito: El workflow aparece completado en la interfaz web local con su historial de eventos.
- **Combina con:** `openai-agents-python` [3/py], `pydantic-ai` [3/py], `langgraph` [3/py], `grafana` [10/bi], `claude-code` [20/terminal]
- **Riesgos y avisos:** Temporal no es un orquestador de datos por calendario como Airflow: modela procesos de aplicación duraderos.

### activepieces (`activepieces`)

- **Repo:** https://github.com/activepieces/activepieces · MIT + licencia Enterprise (packages/ee/) · nivel 2 · 64/100
- **Qué es:** Plataforma de automatización con IA de código abierto, presentada como reemplazo libre de Zapier. La edición comunitaria tiene licencia MIT y las funciones Enterprise una licencia comercial; el proyecto es activo, con versiones mensuales.
- **Cuándo elegirlo:** Casos: Pasar respuestas de un formulario a una aplicación de negocio; Solicitar aprobación humana antes de continuar una automatización.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Docker Compose con PostgreSQL y Redis, o una cuenta alojada; hardware prerequisites; API de IA: opcional; Docker Compose con PostgreSQL y Redis, o una cuenta alojada.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/activepieces/activepieces/blob/main/docs/install/options/docker.mdx

  ```bash
  docker run -d --name activepieces -p 8080:80 -v ~/.activepieces:/root/.activepieces -e AP_DB_TYPE=PGLITE -e AP_REDIS_TYPE=MEMORY -e AP_FRONTEND_URL="http://localhost:8080" activepieces/activepieces:latest
  ```
- **Primera prueba propuesta (no ejecutada):** Crea un flujo con un disparador de prueba y una acción de texto Éxito: El historial del flujo muestra la entrada y la salida de la acción
- **Combina con:** `nocodb` [1/internas], `claude-code` [20/terminal], `litellm` [23/serving]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Antes de usarlo comercialmente, revisa qué funciones caen en la licencia Enterprise. El MCP documentado usa un endpoint de la instancia y autenticación; hay que conceder acceso al cliente y las piezas y servicios conservan sus propios requisitos.

### Dagger (`dagger`)

- **Repo:** https://github.com/dagger/dagger · Apache-2.0 · nivel 2 · 64/100
- **Qué es:** Motor de pipelines portable (Apache-2.0).
- **Cuándo elegirlo:** Casos: reemplazar un script CI frágil; correr el mismo pipeline en laptop y CI.
- **Requisitos:** nivel 2: preparación media; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install dagger/tap/dagger` — fuente: https://github.com/dagger/dagger/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** `brew install dagger/tap/dagger` y ejecuta el quickstart del README. Éxito: Pipeline de ejemplo termina en local.
- **Combina con:** `coolify` [22/infraestructura], `portainer` [22/infraestructura]

### Node-RED (`node-red`)

- **Repo:** https://github.com/node-red/node-red · Apache-2.0 · nivel 1 · 64/100 · recomendado en «Automatización por eventos auto-hospedada»
- **Qué es:** Herramienta de programación low-code para aplicaciones basadas en eventos, proyecto de la OpenJS Foundation con licencia Apache 2.0. Existe desde 2013 y sigue publicando versiones (serie 5.x en 2026).
- **Cuándo elegirlo:** Casos: Mostrar lecturas de un sensor recibidas por MQTT; Convertir un webhook en una secuencia de acciones.
- **Requisitos:** nivel 1: preparación sencilla; Una versión compatible de Node.js;  navegador web; hardware prerequisites; API de IA: no; Una versión compatible de Node.js; navegador web.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://nodered.org/docs/getting-started/local
- **Primera prueba propuesta (no ejecutada):** Une un nodo Inject con un nodo Debug y pulsa el disparador Éxito: El panel Debug muestra el mensaje que inyectaste
- **Combina con:** `home-assistant` [15/domotica], `ollama` [8/motores], `grafana` [10/bi], `zigbee2mqtt` [15/domotica]
- **Alternativas:** `huginn`
- **Riesgos y avisos:** Alternativas (elige una): huginn. Los nodos comunitarios son de terceros: revisa su mantenimiento antes de usarlos en producción. En Windows la guía indica omitir sudo; la instalación es de Node-RED, no de un modelo.

### huginn (`huginn`)

- **Repo:** https://github.com/huginn/huginn · MIT · nivel 2 · 63/100 · alternativa en «Automatización por eventos auto-hospedada»
- **Qué es:** Sistema de agentes autoalojado para automatizar tareas en línea, descrito por sus autores como una versión «hackeable» de IFTTT o Zapier en tu propio servidor.
- **Cuándo elegirlo:** Casos: Vigilar novedades de un sitio que publica una fuente RSS; Transformar un webhook entrante en un evento para otros agentes.
- **Requisitos:** nivel 2: preparación media; Docker;  una fuente RSS pública para la prueba; hardware prerequisites; API de IA: no; Docker; una fuente RSS pública para la prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -it -p 3000:3000 ghcr.io/huginn/huginn` — fuente: https://github.com/huginn/huginn/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Configura un agente RSS y observa los eventos que produce Éxito: Aparece un evento con el título y enlace de una publicación
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `coolify` [22/infraestructura], `changedetection` [4/busqueda]
- **Alternativas:** `node-red`
- **Riesgos y avisos:** Alternativas (elige una): node-red. Son agentes de eventos, no agentes que requieren un modelo de lenguaje.

### Windmill (`windmill`)

- **Repo:** https://github.com/windmill-labs/windmill · AGPL-3.0 / Apache-2.0 + licencia propietaria (enterprise) · nivel 2 · 61/100 · alternativa en «Orquestadores de workflows de datos y tareas»
- **Qué es:** Plataforma «code-first» autoalojable para flujos de trabajo, apps internas y agentes de IA, de Windmill Labs. El código es abierto bajo AGPLv3 y la empresa vende instancias dedicadas, soporte y licencias comerciales; publica versiones casi…
- **Cuándo elegirlo:** Casos: Convertir un script de conciliación en una herramienta interna con formulario; Programar una consulta de datos como tarea recurrente.
- **Requisitos:** nivel 2: preparación media, varios servicios con Docker Compose; Docker Compose;  espacio para la base y los trabajadores; hardware prerequisites; API de IA: opcional; Docker Compose; espacio para la base y los trabajadores.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/windmill-labs/windmill/blob/main/README.md

  ```bash
  curl https://raw.githubusercontent.com/windmill-labs/windmill/main/docker-compose.yml -o docker-compose.yml
  curl https://raw.githubusercontent.com/windmill-labs/windmill/main/Caddyfile -o Caddyfile
  curl https://raw.githubusercontent.com/windmill-labs/windmill/main/.env -o .env
  
  docker compose up -d
  ```
- **Primera prueba propuesta (no ejecutada):** Crea un script que reciba un nombre y devuelva un saludo Éxito: La ejecución guarda el resultado del script y sus logs
- **Combina con:** `duckdb` [25/datos], `claude-code` [20/terminal], `polars` [25/datos], `coolify` [22/infraestructura]
- **Alternativas:** `airflow`, `kestra`, `prefect`, `trigger-dev`, `dagster`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): kestra, trigger-dev. La AGPLv3 obliga a publicar cambios si ofreces una versión modificada como servicio. Ofrece MCP remoto autenticado para operar un workspace; conectar Claude Code, Codex o Antigravity no incluye el modelo ni autoriza todas las acciones del….

### Dagster (`dagster`)

- **Repo:** https://github.com/dagster-io/dagster · Apache-2.0 · nivel 2 · 57/100 · alternativa en «Orquestadores de workflows de datos y tareas»
- **Qué es:** Orquestador de pipelines de datos de Dagster Labs (Apache-2.0), con oferta comercial gestionada (Dagster+). Proyecto maduro; el README indica soporte oficial de Python 3.9 a 3.14.
- **Cuándo elegirlo:** Casos: mantener al día un conjunto de tablas analíticas con dependencias y linaje visibles; probar pipelines de datos con tests unitarios antes de llevarlos a producción.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `uv add dagster dagster-webserver dagster-dg-cli` — fuente: https://github.com/dagster-io/dagster/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `uv add dagster dagster-webserver dagster-dg-cli`, define dos activos dependientes y materialízalos desde la interfaz. Éxito: La interfaz muestra el grafo de activos y ambos aparecen materializados con sus metadatos.
- **Combina con:** `duckdb` [25/datos], `polars` [25/datos], `mlflow` [23/observabilidad], `claude-code` [20/terminal], `dbt` [25/datos], `dlt` [25/datos]
- **Alternativas:** `airflow`, `kestra`, `prefect`, `trigger-dev`, `windmill`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): airflow, prefect, kestra.

### Celery (`celery`)

- **Repo:** https://github.com/celery/celery · BSD-3-Clause · nivel 2 · —/100
- **Qué es:** Envía trabajos Python a una cola para que procesos separados los ejecuten y la aplicación no tenga que esperar.
- **Cuándo elegirlo:** Casos: Procesar una miniatura de prueba en segundo plano.; Generar un informe de ejemplo en una cola distinta a la interfaz web.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, Makefile, pyproject.toml, setup.py; API de IA: no; Python compatible con la versión estable elegida y un intermediario local como Redis o RabbitMQ..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html
- **Primera prueba propuesta (no ejecutada):** Completa el tutorial con una tarea que sume dos números y un intermediario local. Éxito: El proceso trabajador recibe la tarea y el resultado contiene la suma esperada.
- **Riesgos y avisos:** Mantén el intermediario fuera de internet y usa cargas de prueba. Si lo alojas, cuenta procesos, memoria y persistencia.

### ToolJet (`tooljet`)

- **Repo:** https://github.com/ToolJet/ToolJet · AGPL-3.0 · nivel 2 · 75/100 · recomendado en «Herramientas internas y bases de datos no-code»
- **Qué es:** Plataforma de código abierto para construir herramientas internas (paneles de administración, dashboards y apps operativas) sobre tus bases de datos, APIs y servicios SaaS, de ToolJet Solutions.
- **Cuándo elegirlo:** Casos: Crear un panel interno para consultar pedidos y su estado; Pedir a un agente construir una interfaz ToolJet mediante el servidor MCP.
- **Requisitos:** nivel 2: preparación media; Instancia ToolJet de prueba;  conexión de datos ficticios;  cliente MCP si eliges esa ruta; hardware prerequisites; API de IA: opcional; Instancia ToolJet de prueba; conexión de datos ficticios; cliente MCP si eliges esa ruta.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/ToolJet/ToolJet/blob/main/README.md

  ```bash
  docker run --name tooljet --restart unless-stopped -p 80:80 --platform linux/amd64 -v tooljet_data:/var/lib/postgresql/13/main tooljet/try:ee-lts-latest
  ```
- **Primera prueba propuesta (no ejecutada):** Crea una página con una tabla y enlázala a un pequeño conjunto de datos Éxito: La tabla muestra los datos y puedes revisar la consulta que los obtiene
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `activepieces` [1/motores]
- **Alternativas:** `appsmith`, `nocodb`, `budibase`, `teable`, `grist-core`, `baserow`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): appsmith, budibase. El contenedor de prueba usa la imagen Enterprise (ee); revisa qué funciones requieren licencia. Claude Code y Codex tienen plugins documentados; Antigravity puede conectarse por MCP, sin que esto incluya el alojamiento de la plataforma.

### Appsmith (`appsmith`)

- **Repo:** https://github.com/appsmithorg/appsmith · Apache-2.0 · nivel 3 · 72/100 · alternativa en «Herramientas internas y bases de datos no-code»
- **Qué es:** Plataforma low-code de código abierto (Apache 2.0) para desarrollar, desplegar y mantener aplicaciones internas, de Appsmith Inc. Se usa en su nube o autoalojada y publica versiones con frecuencia.
- **Cuándo elegirlo:** Casos: Preparar un panel para que soporte consulte expedientes; Construir un formulario interno que actualiza datos mediante una API.
- **Requisitos:** nivel 3: preparación media, despliegue con Kubernetes/Helm; Cuenta o instancia de prueba;  una fuente de datos de demostración; hardware prerequisites; API de IA: opcional; Cuenta o instancia de prueba; una fuente de datos de demostración.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/appsmithorg/appsmith/blob/release/deploy/helm/docs/install-mongodb-operator.md

  ```bash
  helm install appsmith appsmith/appsmith -n appsmith --wait --timeout 10m --set mongodb.enabled=false --set mongodbCommunity.enabled=true --set mongodbOperator.enabled=true
  ```
- **Primera prueba propuesta (no ejecutada):** Añade una tabla a una página y asóciala a una consulta de datos ficticios Éxito: La tabla se actualiza al ejecutar la consulta y muestra los registros esperados
- **Combina con:** `supabase` [22/infraestructura], `activepieces` [1/motores], `metabase` [10/bi]
- **Alternativas:** `tooljet`, `nocodb`, `budibase`, `teable`, `grist-core`, `baserow`
- **Riesgos y avisos:** Alternativas (elige una): tooljet, budibase, nocodb. La función principal son interfaces internas sobre datos; una API de negocio no equivale a una API de modelo.

### NocoDB (`nocodb`)

- **Repo:** https://github.com/nocodb/nocodb · Sustainable Use License (no OSI) · nivel 1 · 70/100 · alternativa en «Herramientas internas y bases de datos no-code»
- **Qué es:** Plataforma para crear bases de datos en línea con interfaz de hoja de cálculo, alternativa abierta a Airtable. Desde hace un tiempo usa la Sustainable Use License (no es OSI); es un proyecto muy popular con versiones mensuales.
- **Cuándo elegirlo:** Casos: Mantener un inventario sencillo con vistas para distintas personas; Revisar datos de clientes en una interfaz tabular.
- **Requisitos:** nivel 1: preparación sencilla; Docker;  carpeta de datos;  navegador; hardware prerequisites; API de IA: no; Docker; carpeta de datos; navegador.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/nocodb/nocodb/blob/develop/README.md

  ```bash
  docker run -d \
    --name noco \
    -v "$(pwd)"/nocodb:/usr/app/data/ \
    -p 8080:8080 \
    nocodb/nocodb:latest
  ```
- **Primera prueba propuesta (no ejecutada):** Crea una tabla con nombre y estado e introduce dos registros de prueba Éxito: Puedes editar los registros y filtrarlos por su estado
- **Combina con:** `activepieces` [1/motores], `metabase` [10/bi], `coolify` [22/infraestructura]
- **Alternativas:** `tooljet`, `appsmith`, `budibase`, `teable`, `grist-core`, `baserow`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): appsmith, budibase. El primer ejemplo Docker es de evaluación local; no reutilices los secretos de ejemplo para un despliegue público.

### Budibase (`budibase`)

- **Repo:** https://github.com/Budibase/budibase · GPL-3.0 + BSL (packages/pro) · nivel 2 · 62/100 · alternativa en «Herramientas internas y bases de datos no-code»
- **Qué es:** Plataforma de operaciones de código abierto para crear agentes, apps y automatizaciones, de Budibase Ltd. El núcleo tiene licencia GPL v3, las librerías de cliente y componentes MPL (las apps que construyes pueden tener la licencia que…
- **Cuándo elegirlo:** Casos: Registrar solicitudes internas y seguir su estado; Montar un proceso que combina formulario, automatización y agente de IA.
- **Requisitos:** nivel 2: preparación media; Cuenta o instancia Budibase;  datos de ejemplo para una aplicación; hardware prerequisites; API de IA: opcional; Cuenta o instancia Budibase; datos de ejemplo para una aplicación.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -d -t --name=budibase -p 10000:80 -v /local/path/data:/data --restart unless-stopped budibase/budibase:latest` — fuente: https://docs.budibase.com/docs/docker
- **Primera prueba propuesta (no ejecutada):** Crea una aplicación con un formulario y una tabla de registros Éxito: Un envío del formulario aparece en la tabla de la aplicación
- **Combina con:** `supabase` [22/infraestructura], `activepieces` [1/motores], `ollama` [8/motores]
- **Alternativas:** `tooljet`, `appsmith`, `nocodb`, `teable`, `grist-core`, `baserow`
- **Riesgos y avisos:** BSL (source-available): no es OSI; revisa usos comerciales y la fecha de cambio de licencia. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): appsmith, tooljet, nocodb. Comprueba qué funciones de IA o administración caen en la licencia de pago. Las licencias del servidor y de las bibliotecas cliente difieren; comprueba la distribución concreta.

### Teable (`teable`)

- **Repo:** https://github.com/teableio/teable · AGPL-3.0 · nivel 2 · 56/100 · alternativa en «Herramientas internas y bases de datos no-code»
- **Qué es:** Plataforma de base de datos sin código de código abierto mantenida por Teable (teableio). El núcleo es AGPL-3.0 y los paquetes compartidos MIT; las funciones Enterprise se activan con licencia comercial.
- **Cuándo elegirlo:** Casos: gestionar un catálogo o pipeline comercial con vistas de cuadrícula, kanban y calendario; dar a un equipo tablas en PostgreSQL con permisos y API sin escribir backend.
- **Requisitos:** nivel 2: preparación media; TypeScript, package.json; API de IA: opcional.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/teableio/teable/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega Teable con la guía Docker oficial y crea una tabla con un formulario y una vista kanban. Éxito: Los registros enviados por el formulario aparecen en la tabla y en la vista kanban, y se conservan tras reiniciar.
- **Combina con:** `activepieces` [1/motores], `supabase` [22/infraestructura], `metabase` [10/bi], `coolify` [22/infraestructura]
- **Alternativas:** `tooljet`, `appsmith`, `nocodb`, `budibase`, `grist-core`, `baserow`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): grist-core, baserow, nocodb. Las funciones de IA y el sandbox de agentes añaden requisitos de contenedores y de proveedor.

### Grist (`grist-core`)

- **Repo:** https://github.com/gristlabs/grist-core · Apache-2.0 · nivel 1 · 53/100 · alternativa en «Herramientas internas y bases de datos no-code»
- **Qué es:** Servidor de la edición Community de Grist (Apache-2.0), mantenido por Grist Labs (Nueva York) con contribuciones relevantes de organismos públicos franceses.
- **Cuándo elegirlo:** Casos: sustituir una hoja compartida por tablas relacionadas con permisos por fila; montar un inventario o CRM ligero en tu propio servidor.
- **Requisitos:** nivel 1: preparación sencilla; TypeScript, Dockerfile, package.json; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -p 8484:8484 -it gristlabs/grist` — fuente: https://github.com/gristlabs/grist-core/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca la imagen Docker de prueba, crea un documento con dos tablas enlazadas y una fórmula Python. Éxito: La fórmula se recalcula al editar la tabla referenciada y el documento sigue disponible tras reiniciar con /persist…
- **Combina con:** `activepieces` [1/motores], `duckdb` [25/datos], `coolify` [22/infraestructura], `claude-code` [20/terminal]
- **Alternativas:** `tooljet`, `appsmith`, `nocodb`, `budibase`, `teable`, `baserow`
- **Riesgos y avisos:** Alternativas (elige una): baserow, teable, nocodb. Si activas el asistente de IA, las fórmulas y el contexto se envían al proveedor configurado.

### Baserow (`baserow`)

- **Repo:** https://github.com/baserow/baserow · MIT · nivel 1 · 50/100 · alternativa en «Herramientas internas y bases de datos no-code»
- **Qué es:** Plataforma de base de datos sin código de Baserow B.V. con núcleo MIT y funciones premium y enterprise bajo licencia propia. Proyecto maduro que se trasladó de GitLab a GitHub; ofrece nube y autoalojamiento.
- **Cuándo elegirlo:** Casos: crear una base de clientes o inventario compartida sin escribir backend; publicar un portal o formulario sobre tus propias tablas en tu dominio.
- **Requisitos:** nivel 1: preparación sencilla; Python, docker-compose.yml; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -v baserow_data:/baserow/data -p 80:80 -p 443:443 baserow/baserow:2.4.3` — fuente: https://github.com/baserow/baserow/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca el contenedor de la documentación con un volumen de datos y crea una base con una tabla y un formulario. Éxito: El formulario guarda filas en la tabla y la API REST devuelve esos registros con un token.
- **Combina con:** `activepieces` [1/motores], `metabase` [10/bi], `coolify` [22/infraestructura]
- **Alternativas:** `tooljet`, `appsmith`, `nocodb`, `budibase`, `teable`, `grist-core`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): grist-core, teable, nocodb. Comprueba qué funciones son premium antes de planificar un despliegue.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-1.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Automatizar procesos y crear herramientas internas», lee `docs/alexandria/categoria-1.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-1.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
