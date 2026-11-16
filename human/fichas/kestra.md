[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 Kestra

> Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.2k | Apache-2.0 | Java | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

**Puntuación de calidad** 80/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de orquestación de código abierto (Apache 2.0) para flujos de datos, IA e infraestructura, mantenida por Kestra Technologies. Existe desde 2019, publicó la serie 2.0 en 2026 y tiene una edición Enterprise con RBAC y políticas de gobierno.

## ¿Qué hace?

Unifica automatizaciones programadas y disparadas por eventos con una interfaz declarativa e independiente del lenguaje: extrae datos de bases, almacenamiento en la nube o APIs, ejecuta scripts en cualquier lenguaje y coordina pipelines de datos, microservicios y procesos de negocio. Incluye agentes de IA y flujos RAG como tipos de tarea, un servidor MCP y disparadores por herramienta MCP. Casos típicos: ETL nocturnos, pipelines de analítica, aprovisionamiento de infraestructura y flujos con aprobación.

## ¿Cómo lo hace?

Los flujos se definen en YAML («todo como código») y se pueden editar desde un editor YAML, un editor sin código o un copiloto de IA que se mantienen sincronizados, con control de versiones en Git. El motor está escrito en Java y se extiende con cientos de plugins que se pueden descargar bajo demanda desde Maven Central (`KESTRA_PLUGINS_AUTO_INSTALL_ENABLED=true`). Se prueba con un solo `docker run` en el puerto 8080 montando el socket de Docker para ejecutar tareas en contenedores; en producción usa PostgreSQL y almacenamiento de objetos, con plantillas Terraform para la nube. Tiene CLI (`kestractl`) y extensión para VS Code.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | Kestra tiene un plugin JDBC para DuckDB, útil para transformar CSV o Parquet con SQL dentro de un flujo sin levantar un servidor de base de datos. | Nada que instalar aparte: el plugin se descarga en Kestra; guarda los archivos .duckdb en un volumen persistente. |
| [Apache Superset](superset.md) | Kestra carga y transforma los datos en el almacén y Superset los visualiza en dashboards (combinación por arquitectura). | Primero el almacén de datos, luego Kestra para poblarlo y al final Superset conectado a ese almacén. |
| [Claude Code](claude-code.md) | Con el servidor MCP de Kestra, un agente de código puede consultar y gestionar flujos y ejecuciones desde la terminal. | Kestra en marcha y accesible; después registra su servidor MCP en Claude Code según la guía oficial. |
| [Ollama](ollama.md) | Los agentes de IA y flujos RAG de Kestra pueden apuntar a un proveedor de modelos local para no enviar datos a una API externa (combinación por arquitectura; el proveedor exacto depende del plugin de IA) [DATO NO VERIFICADO]. | Ollama primero; desde Kestra en Docker usa la dirección del host. |

**Notas:** Alternativas (elige una): windmill, trigger-dev. El arranque rápido monta `/var/run/docker.sock` como root: úsalo solo en entornos de prueba.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v2.0.10 (2026-11-10) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/kestra-io/kestra/blob/develop/README.md) · [2](https://kestra.io/plugins/plugin-jdbc-duckdb) · [3](https://kestra.io/docs/ai-tools/mcp-server)</sub>

## Ver similares

Grupo **Orquestadores de workflows de datos y tareas**: Kestra ocupa la posición 2 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Apache Airflow](airflow.md) ⭐ recomendado | 81 | Si necesitas el estándar de la industria para pipelines por lotes con un ecosistema enorme de operadores. |
| 2 | **Kestra** (esta ficha) | 80 | Si prefieres definir flujos en YAML con interfaz web y disparadores por eventos. |
| 3 | [Prefect](prefect.md) | 68 | Si quieres convertir funciones Python en flujos observables con muy poco código. |
| 4 | [Trigger.dev](trigger-dev.md) | 68 | Si trabajas en TypeScript y quieres tareas de fondo largas sin gestionar colas. |
| 5 | [Windmill](windmill.md) | 61 | Si quieres scripts en varios lenguajes convertidos en flujos y apps internas rápidas. |
| 6 | [Dagster](dagster.md) | 57 | Si piensas en activos de datos (tablas, modelos) con linaje y pruebas. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El motor autoalojado requiere infraestructura; funciones comerciales y proveedores de IA pueden añadir consumo |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Expone flows por MCP HTTP con autenticación y permisos; el ejemplo Docker usa root y monta su socket, por lo que requiere un entorno de prueba |
| Coste | El coste depende del proveedor o la ruta. El motor autoalojado requiere infraestructura; funciones comerciales y proveedores de IA pueden añadir consumo |
| Equipo | Preparación según la ruta elegida. Docker;  directorio temporal y volúmenes de prueba |

Expone flows por MCP HTTP con autenticación y permisos; el ejemplo Docker usa root y monta su socket, por lo que requiere un entorno de prueba

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
-  directorio temporal y volúmenes de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (powershell):**

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

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/kestra-io/kestra/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Kestra para mi objetivo y necesito pasos guiados. Lee https://github.com/kestra-io/kestra/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta un flujo de ejemplo y abre sus logs en la interfaz de Kestra.

**Qué comprobar:** La ejecución muestra su estado final y los mensajes de las tareas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Programar una importación diaria de archivos con reintentos
- Combinar tareas de datos con una consulta a un modelo Ollama

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Programar una importación diaria de archivos con reintentos; Combinar tareas de datos con una consulta a un modelo Ollama | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Expone flows por MCP HTTP con autenticación y permisos; el ejemplo Docker usa root y monta su socket, por lo que requiere un entorno de prueba

## Stack y modelos

- **Stack:** Docker;  directorio temporal y volúmenes de prueba
- **Etiquetas:** `automation` `data` `java` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Windmill](windmill.md) | 18.6k | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. |
| [Trigger.dev](trigger-dev.md) | 16.8k | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. |
| [Apache Airflow](airflow.md) | 47.5k | Orquestador de workflows de la Apache Software Foundation: DAGs en Python con planificador, workers, reintentos e interfaz de monitorización. |
| [Prefect](prefect.md) | 24.2k | Framework de orquestación en Python: convierte scripts en flujos con decoradores, reintentos, caché, programación y servidor de monitorización. |
| [Dagster](dagster.md) | 16.4k | Orquestador de datos orientado a activos: declaras tablas, modelos o informes como funciones Python y Dagster los mantiene actualizados con linaje. |

## Enlaces

- 🐙 GitHub: [kestra-io/kestra](https://github.com/kestra-io/kestra)
- 🌐 Web: <https://go.kestra.io/home>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/kestra-io/kestra/blob/develop/README.md)
- [Fuente 2](https://kestra.io/docs/ai-orchestration/mcp-server)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
