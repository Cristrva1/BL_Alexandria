[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Alojamiento y backend

# ⚙️ supabase

> Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 115k | Apache-2.0 | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado · **MCP** 🔌 sí

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 76/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Supabase, plataforma de desarrollo sobre PostgreSQL que ofrece funciones similares a Firebase con herramientas open source. Licencia Apache-2.0. Es muy madura (~115k estrellas) y tiene servicio alojado y opción de autoalojamiento.

## ¿Qué hace?

Ofrece base de datos Postgres, autenticación, APIs REST y GraphQL autogeneradas, Realtime, funciones de base de datos y Edge Functions, almacenamiento de archivos, vectores para IA y un dashboard.

## ¿Cómo lo hace?

Se usa en supabase.com o se autoaloja con Docker, y tiene CLI para desarrollo local. Combina servicios como PostgREST, Realtime (Elixir) y Storage, con librerías cliente modulares por lenguaje.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [pgvector](pgvector.md) | Extensión de vectores para embeddings. | Activa la extensión en la base de datos. |
| [activepieces](activepieces.md) | Activepieces tiene una pieza oficial `supabase` para usar supabase en flujos. | supabase en marcha con sus credenciales; después añade la pieza `supabase` en un flujo de Activepieces. |
| [coolify](coolify.md) | Autoalojar Supabase. (combinación por arquitectura) | Despliega desde Coolify. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (17). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Appsmith](appsmith.md) · [Budibase](budibase.md) · [Chart.js](chart-js.md) · [Dokploy](dokploy.md) · [Evidence](evidence.md) · [free-for-dev](free-for-dev.md) · [Grafana](grafana.md) · [Onlook](onlook.md) · [plasmic](plasmic.md) · [Plausible Analytics](plausible.md) · [Redash](redash.md) · [social-media-agent](social-media-agent.md) · [swr](swr.md) · [TanStack Query](tanstack-query.md) · [Teable](teable.md) · [tldraw](tldraw.md) · [transformers.js](transformers-js.md)

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.26.08 (2026-08-07) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/supabase/supabase/blob/master/README.md) · [2](https://supabase.com/docs/guides/hosting/overview) · [3](https://github.com/activepieces/activepieces/tree/main/packages/pieces/community/supabase)</sub>

## Ver similares

Grupo **Backends como servicio auto-hospedados**: supabase ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **supabase** (esta ficha) ⭐ recomendado | 76 | Si buscas esto: plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones. |
| 2 | [Appwrite](appwrite.md) | 73 | Si buscas esto: plataforma de backend abierta orientada a agentes y desarrolladores: autenticación, bases de datos, almacenamiento, funciones, mensajería, tiempo real y hosting, con MCP. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La base no exige LLM; Cloud, almacenamiento, cómputo y extras tienen planes y cuotas; self-host requiere infraestructura |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El MCP oficial sirve a clientes compatibles; funciones alojadas, locales y confirmaciones interactivas varían y no deben asumirse idénticas |
| Coste | El coste depende del proveedor o la ruta. La base no exige LLM; Cloud, almacenamiento, cómputo y extras tienen planes y cuotas; self-host requiere infraestructura |
| Equipo | Preparación según la ruta elegida. Proyecto de prueba o entorno local; cuenta para Cloud; cliente MCP opcional |

El MCP oficial sirve a clientes compatibles; funciones alojadas, locales y confirmaciones interactivas varían y no deben asumirse idénticas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto de prueba o entorno local
- cuenta para Cloud
- cliente MCP opcional

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://supabase.com/docs/guides/getting-started)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar supabase para mi objetivo y necesito pasos guiados. Lee https://supabase.com/docs/guides/getting-started. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea datos ficticios en un proyecto de desarrollo y consulta su estructura con permisos de solo lectura.

**Qué comprobar:** Puedes comprobar tablas y acceso sin tocar datos de producción.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un backend para una web
- Conectar un agente a un esquema de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un backend para una web; Conectar un agente a un esquema de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP oficial sirve a clientes compatibles; funciones alojadas, locales y confirmaciones interactivas varían y no deben asumirse idénticas

## Stack y modelos

- **Stack:** Proyecto de prueba o entorno local; cuenta para Cloud; cliente MCP opcional
- **Etiquetas:** `infraestructura` `server` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Appwrite](appwrite.md) | 58.1k | Plataforma de backend abierta orientada a agentes y desarrolladores: autenticación, bases de datos, almacenamiento, funciones, mensajería, tiempo real y hosting, con MCP. |

## Enlaces

- 🐙 GitHub: [supabase/supabase](https://github.com/supabase/supabase)
- 🌐 Web: <https://supabase.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/supabase/supabase/blob/master/README.md)
- [Fuente 2](https://supabase.com/docs/guides/getting-started/mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
