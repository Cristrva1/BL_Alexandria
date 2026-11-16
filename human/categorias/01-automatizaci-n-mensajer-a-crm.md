[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Automatizar procesos y crear herramientas internas

Motores de flujos (Activepieces, Windmill, Node-RED, Huginn, Kestra, Trigger.dev) y apps internas sin código (NocoDB, ToolJet, Appsmith, Budibase). Elige primero el motor del proceso y conecta después datos, canales y modelos; para WhatsApp y atención al cliente se combinan con Evolution API, Dify y Chatwoot.

18 repos · 2 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [NocoDB](../fichas/nocodb.md) | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Motores de workflow y automatización](#motores-de-workflow-y-automatización) — 11 repos
- [Apps internas y bases de datos no-code](#apps-internas-y-bases-de-datos-no-code) — 7 repos

## Motores de workflow y automatización

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [huginn](../fichas/huginn.md) | Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú". | Tu objetivo encaja con estos ejemplos: Vigilar novedades de un sitio que publica una fuente RSS; Transformar un webhook entrante en un evento para otros agentes | Sin clave propia de API de IA en la ruta básica |
| [Apache Airflow](../fichas/airflow.md) | Orquestador de workflows de la Apache Software Foundation: DAGs en Python con planificador, workers, reintentos e interfaz de monitorización. | Tu objetivo encaja con estos ejemplos: programar un ETL diario que descarga, transforma y carga datos en un almacén; coordinar entrenamientos y despliegues de modelos con dependencias y reintentos | Sin clave propia de API de IA en la ruta básica |
| [Kestra](../fichas/kestra.md) | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. | Tu objetivo encaja con estos ejemplos: Programar una importación diaria de archivos con reintentos; Combinar tareas de datos con una consulta a un modelo Ollama | API de IA opcional |
| [activepieces](../fichas/activepieces.md) | Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables. | Tu objetivo encaja con estos ejemplos: Pasar respuestas de un formulario a una aplicación de negocio; Solicitar aprobación humana antes de continuar una automatización | API de IA opcional |
| [Temporal](../fichas/temporal.md) | Plataforma de ejecución duradera: workflows en código que sobreviven a fallos, con reintentos, temporizadores y estado persistido por el servidor. | Tu objetivo encaja con estos ejemplos: procesos de negocio largos como pagos o altas que deben completarse aunque caiga un servicio; agentes de IA con pasos largos que necesitan reintentos y reanudación | Sin clave propia de API de IA en la ruta básica |
| [Prefect](../fichas/prefect.md) | Framework de orquestación en Python: convierte scripts en flujos con decoradores, reintentos, caché, programación y servidor de monitorización. | Tu objetivo encaja con estos ejemplos: convertir un script de ingesta en un flujo con reintentos y ejecución programada; encadenar pasos de datos o ML con dependencias dinámicas y observabilidad | Sin clave propia de API de IA en la ruta básica |
| [Node-RED](../fichas/node-red.md) | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. | Tu objetivo encaja con estos ejemplos: Mostrar lecturas de un sensor recibidas por MQTT; Convertir un webhook en una secuencia de acciones | Sin clave propia de API de IA en la ruta básica |
| [Windmill](../fichas/windmill.md) | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. | Tu objetivo encaja con estos ejemplos: Convertir un script de conciliación en una herramienta interna con formulario; Programar una consulta de datos como tarea recurrente | API de IA opcional |
| [Trigger.dev](../fichas/trigger-dev.md) | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. | Tu objetivo encaja con estos ejemplos: Procesar en segundo plano un archivo subido por un usuario; Reintentar una tarea de generación cuando falla el proveedor | API de IA opcional |
| [Dagger](../fichas/dagger.md) | Pipelines de entrega como código con contenedores: SDKs en 8 lenguajes, cache content-addressed y telemetría OpenTelemetry. | Tu objetivo encaja con estos ejemplos: reemplazar un script CI frágil; correr el mismo pipeline en laptop y CI | Sin clave propia de API de IA en la ruta básica |
| [Dagster](../fichas/dagster.md) | Orquestador de datos orientado a activos: declaras tablas, modelos o informes como funciones Python y Dagster los mantiene actualizados con linaje. | Tu objetivo encaja con estos ejemplos: mantener al día un conjunto de tablas analíticas con dependencias y linaje visibles; probar pipelines de datos con tests unitarios antes de llevarlos a producción | Sin clave propia de API de IA en la ruta básica |

## Apps internas y bases de datos no-code

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [NocoDB](../fichas/nocodb.md) | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. | Tu objetivo encaja con estos ejemplos: Mantener un inventario sencillo con vistas para distintas personas; Revisar datos de clientes en una interfaz tabular | Sin clave propia de API de IA en la ruta básica |
| [Appsmith](../fichas/appsmith.md) | Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases. | Tu objetivo encaja con estos ejemplos: Preparar un panel para que soporte consulte expedientes; Construir un formulario interno que actualiza datos mediante una API | API de IA opcional |
| [ToolJet](../fichas/tooljet.md) | Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA. | Tu objetivo encaja con estos ejemplos: Crear un panel interno para consultar pedidos y su estado; Pedir a un agente construir una interfaz ToolJet mediante el servidor MCP | API de IA opcional |
| [Budibase](../fichas/budibase.md) | Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos. | Tu objetivo encaja con estos ejemplos: Registrar solicitudes internas y seguir su estado; Montar un proceso que combina formulario, automatización y agente de IA | API de IA opcional |
| [Teable](../fichas/teable.md) | Base de datos colaborativa sin código sobre PostgreSQL, con vistas tipo hoja, formularios, automatizaciones y funciones de IA. | Tu objetivo encaja con estos ejemplos: gestionar un catálogo o pipeline comercial con vistas de cuadrícula, kanban y calendario; dar a un equipo tablas en PostgreSQL con permisos y API sin escribir backend | API de IA opcional |
| [Grist](../fichas/grist-core.md) | Hoja de cálculo relacional autoalojable con fórmulas en Python, columnas tipadas y formato portable basado en SQLite. | Tu objetivo encaja con estos ejemplos: sustituir una hoja compartida por tablas relacionadas con permisos por fila; montar un inventario o CRM ligero en tu propio servidor | API de IA opcional |
| [Baserow](../fichas/baserow.md) | Base de datos sin código autoalojable (Django y Vue) con constructor de aplicaciones, automatizaciones, dashboards y API-first. | Tu objetivo encaja con estos ejemplos: crear una base de clientes o inventario compartida sin escribir backend; publicar un portal o formulario sobre tus propias tablas en tu dominio | API de IA opcional |

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
