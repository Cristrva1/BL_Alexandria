# Alexandría para agentes · Motores de workflow y automatización

Categoría 1 «Automatizar procesos y crear herramientas internas» › subcategoría `motores`. 11 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=1&sub=motores · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `airflow` | Orquestador de workflows de la Apache Software Foundation: DAGs en Python con… | 3 Avanzado | 81 | Apache-2.0 (OSI permisiva) | recomendado |
| `kestra` | Orquestador declarativo de workflows en YAML para datos, infraestructura y… | 2 Intermedio | 80 | Apache-2.0 (OSI permisiva) | alternativa |
| `prefect` | Framework de orquestación en Python: convierte scripts en flujos con… | 2 Intermedio | 68 | Apache-2.0 (OSI permisiva) | alternativa |
| `trigger-dev` | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en… | 2 Intermedio | 68 | Apache-2.0 (OSI permisiva) | alternativa |
| `temporal` | Plataforma de ejecución duradera: workflows en código que sobreviven a fallos… | 2 Intermedio | 67 | MIT (OSI permisiva) | sin grupo |
| `activepieces` | Plataforma open-source de automatización con IA, alternativa extensible a… | 2 Intermedio | 64 | MIT + licencia Enterprise (packages/ee/) (open-core) | sin grupo |
| `dagger` | Pipelines de entrega como código con contenedores: SDKs en 8 lenguajes, cache… | 2 Intermedio | 64 | Apache-2.0 (OSI permisiva) | sin grupo |
| `node-red` | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras… | 1 Básico | 64 | Apache-2.0 (OSI permisiva) | recomendado |
| `huginn` | Sistema de agentes self-hosted para automatizar tareas online y reaccionar a… | 2 Intermedio | 63 | MIT (OSI permisiva) | alternativa |
| `windmill` | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y… | 2 Intermedio | 61 | AGPL-3.0 / Apache-2.0 + licencia propietaria (enterprise) (open-core) | alternativa |
| `dagster` | Orquestador de datos orientado a activos: declaras tablas, modelos o informes… | 2 Intermedio | 57 | Apache-2.0 (OSI permisiva) | alternativa |

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

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-1-motores.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Motores de workflow y automatización», lee `docs/alexandria/categoria-1-motores.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-1-motores.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
