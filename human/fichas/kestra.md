[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 Kestra

> Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.2k | Apache-2.0 | Java | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

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

## Qué puedes hacer con él

Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio.

## Por qué destaca

Usos propuestos: Programar una importación diaria de archivos con reintentos; Combinar tareas de datos con una consulta a un modelo Ollama.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [DuckDB](duckdb.md) | 43.1k | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. |
| [Apache Superset](superset.md) | 75.5k | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Windmill](windmill.md) | 18.6k | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. |
| [Trigger.dev](trigger-dev.md) | 16.8k | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. |

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
