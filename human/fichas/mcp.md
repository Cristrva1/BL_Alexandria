[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Directorios, clientes y aprendizaje

# 🧩 Google MCP

> Directorio de servidores MCP oficiales de Google, ejemplos y orientación para desplegarlos en Google Cloud.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.7k | Apache-2.0 | — | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 42/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Repositorio de Google con la lista de sus servidores MCP oficiales, guías para desplegar servidores en Google Cloud y ejemplos. Licencia Apache-2.0. Es pequeño (~5k estrellas) y su último cambio es de agosto de 2026.

## ¿Qué hace?

Enumera servidores remotos gestionados por Google (AlloyDB, BigQuery, Bigtable, Cloud Resource Manager y otros) y servidores de código abierto para sus productos. Explica cómo desplegar servidores propios en Cloud Run y cómo empezar con ejemplos.

## ¿Cómo lo hace?

Es documentación con enlaces; los servidores remotos se habilitan por endpoint en Google Cloud y requieren un proyecto con facturación y permisos IAM.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Gemini CLI](gemini-cli.md) | Usar los servidores de Google desde el agente de Google. (combinación por arquitectura) | Añade el endpoint del servidor a la configuración MCP de Gemini CLI. |
| [mcp-use](mcp-use.md) | Construir y desplegar un servidor propio siguiendo las guías de Cloud Run. (combinación por arquitectura) | Construye con mcp-use y despliega según la guía. |
| [MCP Inspector](mcp-inspector.md) | Probar con MCP Inspector las herramientas de un servidor remoto de Google o de uno propio desplegado en Cloud Run antes de conectarlo al agente (combinación por arquitectura). | Habilita el endpoint en Google Cloud (proyecto con facturación e IAM) y conéctalo después al Inspector con sus credenciales. |

**Notas:** Sin alternativas declaradas. Cuidado con los permisos IAM que concedes a agentes.

Estado en GitHub: activo · último push 2026-08-17 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google/mcp/blob/main/README.md) · [2](https://docs.cloud.google.com/mcp/overview)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Leer es gratuito; servidores, APIs Google y recursos de nube pueden generar gasto |
| Claude Code | Depende del recurso o la configuración |
| Codex | Depende del recurso o la configuración |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. Este repositorio es google/mcp: catálogo y ejemplos Google, no el núcleo de la especificación Model Context Protocol |
| Coste | Sin pago a un modelo en la ruta básica. Leer es gratuito; servidores, APIs Google y recursos de nube pueden generar gasto |
| Equipo | Preparación según la ruta elegida. Navegador; servicio Google objetivo |

Este repositorio es google/mcp: catálogo y ejemplos Google, no el núcleo de la especificación Model Context Protocol

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- servicio Google objetivo

1. Elige un servidor oficial Google y consulta su autenticación antes de desplegar.
2. Comprueba: Distingues servicio gestionado, ejemplo y despliegue en Cloud Run.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google/mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Google MCP para mi objetivo y necesito pasos guiados. Lee https://github.com/google/mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige un servidor oficial Google y consulta su autenticación antes de desplegar.

**Qué comprobar:** Distingues servicio gestionado, ejemplo y despliegue en Cloud Run.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Conectar un servicio Google a un agente
- Aprender a alojar un servidor MCP en Cloud Run

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Conectar un servicio Google a un agente; Aprender a alojar un servidor MCP en Cloud Run | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Este repositorio es google/mcp: catálogo y ejemplos Google, no el núcleo de la especificación Model Context Protocol

## Stack y modelos

- **Stack:** Navegador; servicio Google objetivo
- **Etiquetas:** `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [google/mcp](https://github.com/google/mcp)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google/mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
