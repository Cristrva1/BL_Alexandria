# 1. Automatizar procesos y crear herramientas internas — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `activepieces`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=— · tags=automation,typescript,docker

**Qué es:** Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables.
**Stack:** Docker Compose con PostgreSQL y Redis, o una cuenta alojada
**Acceso y costes:**
- API de IA: API de IA opcional. La edición, licencia y alojamiento elegidos determinan el coste; las piezas de IA usan sus proveedores
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. El MCP documentado usa un endpoint de la instancia y autenticación; hay que conceder acceso al cliente y las piezas y servicios conservan sus propios requisitos
- Coste: El coste depende del proveedor o la ruta. La edición, licencia y alojamiento elegidos determinan el coste; las piezas de IA usan sus proveedores
- Equipo: Preparación según la ruta elegida. Docker Compose con PostgreSQL y Redis, o una cuenta alojada
**Repo:** https://github.com/activepieces/activepieces

**Instalación** [?]:

```
Seguir la instalación original: https://www.activepieces.com/docs/install/overview
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Pasar respuestas de un formulario a una aplicación de negocio; Solicitar aprobación humana antes de continuar una automatización
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un flujo con un disparador de prueba y una acción de texto
**Qué comprobar:** El historial del flujo muestra la entrada y la salida de la acción
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nocodb`, `claude-code`, `litellm`

## `appsmith`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=ui,automation,typescript,docker

**Qué es:** Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases.
**Stack:** Cuenta o instancia de prueba;  una fuente de datos de demostración
**Acceso y costes:**
- API de IA: API de IA opcional. El autoalojamiento, los planes y las funciones de IA tienen condiciones distintas; consulta la edición que vas a usar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La función principal son interfaces internas sobre datos; una API de negocio no equivale a una API de modelo
- Coste: El coste depende del proveedor o la ruta. El autoalojamiento, los planes y las funciones de IA tienen condiciones distintas; consulta la edición que vas a usar
- Equipo: Preparación según la ruta elegida. Cuenta o instancia de prueba;  una fuente de datos de demostración
**Repo:** https://github.com/appsmithorg/appsmith

**Instalación** [?]:

```
Seguir la instalación original: https://docs.appsmith.com/getting-started/setup/installation-guides
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un panel para que soporte consulte expedientes; Construir un formulario interno que actualiza datos mediante una API
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade una tabla a una página y asóciala a una consulta de datos ficticios
**Qué comprobar:** La tabla se actualiza al ejecutar la consulta y muestra los registros esperados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `supabase`, `activepieces`, `metabase`
**Alternativas (elige una):** `tooljet`, `budibase`, `nocodb`

## `awesome-n8n-templates`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=automation,prompts

**Qué es:** Colección de plantillas de n8n para estudiar o importar automatizaciones de servicios y tareas habituales.
**Stack:** n8n;  credenciales y dependencias de la plantilla elegida
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Consultar la colección es gratuito; cada flujo puede requerir n8n alojado, servicios o APIs con coste
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Hay ejemplos locales con Ollama y otros con proveedores remotos; no se promete que todas las plantillas funcionen sin API
- Coste: El coste depende del proveedor o la ruta. Consultar la colección es gratuito; cada flujo puede requerir n8n alojado, servicios o APIs con coste
- Equipo: Preparación según la ruta elegida. n8n;  credenciales y dependencias de la plantilla elegida
**Repo:** https://github.com/enescingoz/awesome-n8n-templates

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una plantilla que clasifica correo con Ollama; Adaptar una alerta de precio que avisa por Telegram
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Importa una plantilla JSON en un flujo desactivado y revisa sus nodos
**Qué comprobar:** El lienzo muestra los pasos y puedes identificar qué credenciales faltan
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `self-hosted-ai-starter-kit`

## `budibase`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=automation,agents,docker

**Qué es:** Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos.
**Stack:** Cuenta o instancia Budibase;  datos de ejemplo para una aplicación
**Acceso y costes:**
- API de IA: API de IA opcional. Las funciones de alojamiento y los proveedores de IA dependen del plan y despliegue; la app básica no exige un LLM
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Las licencias del servidor y de las bibliotecas cliente difieren; comprueba la distribución concreta
- Coste: El coste depende del proveedor o la ruta. Las funciones de alojamiento y los proveedores de IA dependen del plan y despliegue; la app básica no exige un LLM
- Equipo: Preparación según la ruta elegida. Cuenta o instancia Budibase;  datos de ejemplo para una aplicación
**Repo:** https://github.com/Budibase/budibase

**Instalación** [?]:

```
Seguir la instalación original: https://docs.budibase.com
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Registrar solicitudes internas y seguir su estado; Montar un proceso que combina formulario, automatización y agente de IA
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una aplicación con un formulario y una tabla de registros
**Qué comprobar:** Un envío del formulario aparece en la tabla de la aplicación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `supabase`, `activepieces`, `ollama`
**Alternativas (elige una):** `appsmith`, `tooljet`, `nocodb`

## `huginn`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=automation,ruby,docker

**Qué es:** Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú".
**Stack:** Docker;  una fuente RSS pública para la prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La automatización básica no necesita LLM; alojamiento y servicios externos se pagan por separado
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Son agentes de eventos, no agentes que requieren un modelo de lenguaje
- Coste: Sin pago a un modelo en la ruta básica. La automatización básica no necesita LLM; alojamiento y servicios externos se pagan por separado
- Equipo: Preparación según la ruta elegida. Docker;  una fuente RSS pública para la prueba
**Repo:** https://github.com/huginn/huginn

**Instalación** [+]:

```
docker run -it -p 3000:3000 ghcr.io/huginn/huginn
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Vigilar novedades de un sitio que publica una fuente RSS; Transformar un webhook entrante en un evento para otros agentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura un agente RSS y observa los eventos que produce
**Qué comprobar:** Aparece un evento con el título y enlace de una publicación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `litellm`, `coolify`, `changedetection`
**Alternativas (elige una):** `node-red`

## `kestra`
role=platform · exec=local · setup=medium · mcp=True · prov=— · tags=automation,data,java,docker

**Qué es:** Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio.
**Stack:** Docker;  directorio temporal y volúmenes de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. El motor autoalojado requiere infraestructura; funciones comerciales y proveedores de IA pueden añadir consumo
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Expone flows por MCP HTTP con autenticación y permisos; el ejemplo Docker usa root y monta su socket, por lo que requiere un entorno de prueba
- Coste: El coste depende del proveedor o la ruta. El motor autoalojado requiere infraestructura; funciones comerciales y proveedores de IA pueden añadir consumo
- Equipo: Preparación según la ruta elegida. Docker;  directorio temporal y volúmenes de prueba
**Repo:** https://github.com/kestra-io/kestra

**Instalación** [+]:

```
docker run --pull=always --rm -it -p 8080:8080 --user=root `
  --name kestra `
  -v "kestra_data:/app/storage" `
  -v "kestra_db:/app/data" `
  -v "/var/run/docker.sock:/var/run/docker.sock" `
  -v "C:/Temp:/tmp" `
  -e KESTRA_PLUGINS_AUTO_INSTALL_ENABLED=true `
  kestra/kestra:latest-slim server local
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Programar una importación diaria de archivos con reintentos; Combinar tareas de datos con una consulta a un modelo Ollama
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta un flujo de ejemplo y abre sus logs en la interfaz de Kestra
**Qué comprobar:** La ejecución muestra su estado final y los mensajes de las tareas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `duckdb`, `superset`, `claude-code`, `ollama`
**Alternativas (elige una):** `windmill`, `trigger-dev`

## `nocodb`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=data,automation,docker

**Qué es:** Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas.
**Stack:** Docker;  carpeta de datos;  navegador
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ruta básica no requiere LLM; hosting, funciones comerciales e integraciones tienen condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El primer ejemplo Docker es de evaluación local; no reutilices los secretos de ejemplo para un despliegue público
- Coste: Sin pago a un modelo en la ruta básica. La ruta básica no requiere LLM; hosting, funciones comerciales e integraciones tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Docker;  carpeta de datos;  navegador
**Repo:** https://github.com/nocodb/nocodb

**Instalación** [+]:

```
docker run -d \
  --name noco \
  -v "$(pwd)"/nocodb:/usr/app/data/ \
  -p 8080:8080 \
  nocodb/nocodb:latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Mantener un inventario sencillo con vistas para distintas personas; Revisar datos de clientes en una interfaz tabular
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una tabla con nombre y estado e introduce dos registros de prueba
**Qué comprobar:** Puedes editar los registros y filtrarlos por su estado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `activepieces`, `metabase`, `coolify`
**Alternativas (elige una):** `appsmith`, `budibase`

## `node-red`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=automation,javascript,docker

**Qué es:** Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js.
**Stack:** Una versión compatible de Node.js;  navegador web
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El flujo básico no necesita una API de IA; sensores, hosting y servicios conectados pueden tener costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. En Windows la guía indica omitir sudo; la instalación es de Node-RED, no de un modelo
- Coste: Sin pago a un modelo en la ruta básica. El flujo básico no necesita una API de IA; sensores, hosting y servicios conectados pueden tener costes
- Equipo: Preparación según la ruta elegida. Una versión compatible de Node.js;  navegador web
**Repo:** https://github.com/node-red/node-red

**Instalación** [?]:

```
Seguir la instalación original: https://nodered.org/docs/getting-started/local
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Mostrar lecturas de un sensor recibidas por MQTT; Convertir un webhook en una secuencia de acciones
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Une un nodo Inject con un nodo Debug y pulsa el disparador
**Qué comprobar:** El panel Debug muestra el mensaje que inyectaste
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `home-assistant`, `ollama`, `grafana`
**Alternativas (elige una):** `huginn`

## `self-hosted-ai-starter-kit`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=automation,local,rag,docker

**Qué es:** Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos.
**Stack:** Docker Compose;  memoria y almacenamiento para el modelo;  archivo .env preparado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ruta con pesos locales evita una API de modelo; siguen existiendo costes de equipo y energía
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El README distingue perfiles CPU, NVIDIA y alternativas de Mac; elige el de tu equipo antes de descargar pesos
- Coste: Sin pago a un modelo en la ruta básica. La ruta con pesos locales evita una API de modelo; siguen existiendo costes de equipo y energía
- Equipo: Preparación según la ruta elegida. Docker Compose;  memoria y almacenamiento para el modelo;  archivo .env preparado
**Repo:** https://github.com/n8n-io/self-hosted-ai-starter-kit

**Instalación** [+]:

```
git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit
cp .env.example .env # you should update secrets and passwords inside
docker compose --profile cpu up
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un asistente local que responde preguntas sobre material de ejemplo; Explorar cómo se conectan n8n, Ollama y una base vectorial
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre n8n y ejecuta el flujo local incluido con una pregunta sencilla
**Qué comprobar:** El flujo devuelve una respuesta usando el servicio Ollama del stack
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `open-webui`, `docling`, `awesome-n8n-templates`

## `tooljet`
role=platform · exec=local · setup=medium · mcp=True · prov=— · tags=ui,automation,docker

**Qué es:** Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA.
**Stack:** Instancia ToolJet de prueba;  conexión de datos ficticios;  cliente MCP si eliges esa ruta
**Acceso y costes:**
- API de IA: API de IA opcional. La edición y alojamiento de ToolJet tienen sus planes; el agente y los proveedores de IA se contabilizan por separado
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. Claude Code y Codex tienen plugins documentados; Antigravity puede conectarse por MCP, sin que esto incluya el alojamiento de la plataforma
- Coste: El coste depende del proveedor o la ruta. La edición y alojamiento de ToolJet tienen sus planes; el agente y los proveedores de IA se contabilizan por separado
- Equipo: Preparación según la ruta elegida. Instancia ToolJet de prueba;  conexión de datos ficticios;  cliente MCP si eliges esa ruta
**Repo:** https://github.com/ToolJet/ToolJet

**Instalación** [?]:

```
Seguir la instalación original: https://docs.tooljet.com/docs/setup/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un panel interno para consultar pedidos y su estado; Pedir a un agente construir una interfaz ToolJet mediante el servidor MCP
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una página con una tabla y enlázala a un pequeño conjunto de datos
**Qué comprobar:** La tabla muestra los datos y puedes revisar la consulta que los obtiene
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `activepieces`
**Alternativas (elige una):** `appsmith`, `budibase`

## `trigger-dev`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=automation,agents,typescript

**Qué es:** Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript.
**Stack:** Proyecto TypeScript;  entorno y cuenta o despliegue indicado por la guía
**Acceso y costes:**
- API de IA: API de IA opcional. El servicio y la infraestructura tienen su propio consumo; el LLM solo se paga si tu tarea lo llama
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es infraestructura de tareas duraderas; no incluye por sí misma un modelo de IA
- Coste: El coste depende del proveedor o la ruta. El servicio y la infraestructura tienen su propio consumo; el LLM solo se paga si tu tarea lo llama
- Equipo: Preparación según la ruta elegida. Proyecto TypeScript;  entorno y cuenta o despliegue indicado por la guía
**Repo:** https://github.com/triggerdotdev/trigger.dev

**Instalación** [?]:

```
Seguir la instalación original: https://trigger.dev/docs/quick-start
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Procesar en segundo plano un archivo subido por un usuario; Reintentar una tarea de generación cuando falla el proveedor
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta la tarea hello-world del README con un mensaje de prueba
**Qué comprobar:** El panel muestra la ejecución y el mensaje en los logs
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vercel-ai`, `ffmpeg`, `playwright`, `langfuse`
**Alternativas (elige una):** `windmill`, `kestra`

## `windmill`
role=platform · exec=local · setup=medium · mcp=True · prov=— · tags=automation,agents,rust,docker

**Qué es:** Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida.
**Stack:** Docker Compose;  espacio para la base y los trabajadores
**Acceso y costes:**
- API de IA: API de IA opcional. La Community Edition tiene condiciones y cuotas; servidor, planes comerciales y APIs de IA son partidas distintas
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. Ofrece MCP remoto autenticado para operar un workspace; conectar Claude Code, Codex o Antigravity no incluye el modelo ni autoriza todas las acciones del workspace
- Coste: El coste depende del proveedor o la ruta. La Community Edition tiene condiciones y cuotas; servidor, planes comerciales y APIs de IA son partidas distintas
- Equipo: Preparación según la ruta elegida. Docker Compose;  espacio para la base y los trabajadores
**Repo:** https://github.com/windmill-labs/windmill

**Instalación** [+]:

```
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/docker-compose.yml -o docker-compose.yml
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/Caddyfile -o Caddyfile
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/.env -o .env

docker compose up -d
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir un script de conciliación en una herramienta interna con formulario; Programar una consulta de datos como tarea recurrente
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un script que reciba un nombre y devuelva un saludo
**Qué comprobar:** La ejecución guarda el resultado del script y sus logs
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `duckdb`, `claude-code`, `polars`
**Alternativas (elige una):** `kestra`, `trigger-dev`
