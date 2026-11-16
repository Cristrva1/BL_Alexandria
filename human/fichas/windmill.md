[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 Windmill

> Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.6k | NOASSERTION | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma «code-first» autoalojable para flujos de trabajo, apps internas y agentes de IA, de Windmill Labs. El código es abierto bajo AGPLv3 y la empresa vende instancias dedicadas, soporte y licencias comerciales; publica versiones casi a diario.

## ¿Qué hace?

Convierte scripts en Python, TypeScript, Go, Bash, SQL, GraphQL, PowerShell, Rust y otros lenguajes en formularios, endpoints HTTP, comandos de CLI y tareas cron, y los compone en flujos, pipelines de datos, agentes o apps React y Svelte. Los equipos de negocio construyen con IA sobre la misma plataforma con revisión, promoción entre entornos y roles. Se presenta como alternativa autoalojada a Retool, Lovable o n8n.

## ¿Cómo lo hace?

Backend en Rust con servidores de API sin estado y workers que toman trabajos de una cola en PostgreSQL; frontend en Svelte 5; aislamiento con nsjail y espacios de nombres de procesos. Los runtimes son Bun para TypeScript, python3 con uv, y Go, Bash, PowerShell, Rust, C#, Java o Ansible. Cada espacio de trabajo tiene tablas Postgres gestionadas y scripts DuckDB que consultan S3, Parquet o bases externas. Se despliega con Docker Compose o Helm y se trabaja en local con la CLI `wmill`, sincronizada con Git, o mediante su servidor MCP.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | Integración nativa: los scripts DuckDB de Windmill consultan CSV, Parquet y JSON en S3 o Azure Blob, tablas de datos y bases externas en SQL dentro de los workers. | No requiere instalación aparte; configura el recurso de almacenamiento S3 del espacio de trabajo. |
| [Claude Code](claude-code.md) | El servidor MCP de Windmill deja que un agente ejecute scripts, gestione recursos y vigile trabajos; `wmill init` genera un AGENTS.md y archivos de skills para trabajar en local. | Windmill en marcha y CLI `wmill` sincronizada; después registra el MCP en el agente. |
| [Polars](polars.md) | Scripts Python de Windmill pueden usar Polars para transformar datos tabulares grandes en los workers, con dependencias resueltas por uv (combinación por arquitectura). | Declara polars como dependencia del script; vigila la memoria del worker con archivos grandes. |
| [coolify](coolify.md) | Combinación recíproca: coolify lo enlaza como «Plantilla de servicio oficial de Coolify para Windmill». | Orden indicado desde coolify: Coolify primero; luego despliega la plantilla `windmill`. |

**Notas:** Alternativas (elige una): kestra, trigger-dev. La AGPLv3 obliga a publicar cambios si ofreces una versión modificada como servicio.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.875.0 (2026-11-14) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/windmill-labs/windmill/blob/main/README.md) · [2](https://www.windmill.dev/docs/core_concepts/mcp)</sub>

## Ver similares

Grupo **Orquestadores de workflows de datos y tareas**: Windmill ocupa la posición 5 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Apache Airflow](airflow.md) ⭐ recomendado | 81 | Si necesitas el estándar de la industria para pipelines por lotes con un ecosistema enorme de operadores. |
| 2 | [Kestra](kestra.md) | 80 | Si prefieres definir flujos en YAML con interfaz web y disparadores por eventos. |
| 3 | [Prefect](prefect.md) | 68 | Si quieres convertir funciones Python en flujos observables con muy poco código. |
| 4 | [Trigger.dev](trigger-dev.md) | 68 | Si trabajas en TypeScript y quieres tareas de fondo largas sin gestionar colas. |
| 5 | **Windmill** (esta ficha) | 61 | Si quieres scripts en varios lenguajes convertidos en flujos y apps internas rápidas. |
| 6 | [Dagster](dagster.md) | 57 | Si piensas en activos de datos (tablas, modelos) con linaje y pruebas. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La Community Edition tiene condiciones y cuotas; servidor, planes comerciales y APIs de IA son partidas distintas |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. Ofrece MCP remoto autenticado para operar un workspace; conectar Claude Code, Codex o Antigravity no incluye el modelo ni autoriza todas las acciones del workspace |
| Coste | El coste depende del proveedor o la ruta. La Community Edition tiene condiciones y cuotas; servidor, planes comerciales y APIs de IA son partidas distintas |
| Equipo | Preparación según la ruta elegida. Docker Compose;  espacio para la base y los trabajadores |

Ofrece MCP remoto autenticado para operar un workspace; conectar Claude Code, Codex o Antigravity no incluye el modelo ni autoriza todas las acciones del workspace

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker Compose
-  espacio para la base y los trabajadores

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/docker-compose.yml -o docker-compose.yml
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/Caddyfile -o Caddyfile
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/.env -o .env

docker compose up -d
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/windmill-labs/windmill/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Windmill para mi objetivo y necesito pasos guiados. Lee https://github.com/windmill-labs/windmill/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un script que reciba un nombre y devuelva un saludo.

**Qué comprobar:** La ejecución guarda el resultado del script y sus logs.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Convertir un script de conciliación en una herramienta interna con formulario
- Programar una consulta de datos como tarea recurrente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Convertir un script de conciliación en una herramienta interna con formulario; Programar una consulta de datos como tarea recurrente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ofrece MCP remoto autenticado para operar un workspace; conectar Claude Code, Codex o Antigravity no incluye el modelo ni autoriza todas las acciones del workspace

## Stack y modelos

- **Stack:** Docker Compose;  espacio para la base y los trabajadores
- **Etiquetas:** `automation` `agents` `rust` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Kestra](kestra.md) | 30.2k | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. |
| [Trigger.dev](trigger-dev.md) | 16.8k | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. |

## Enlaces

- 🐙 GitHub: [windmill-labs/windmill](https://github.com/windmill-labs/windmill)
- 🌐 Web: <https://windmill.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/windmill-labs/windmill/blob/main/README.md)
- [Fuente 2](https://www.windmill.dev/docs/core_concepts/mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
