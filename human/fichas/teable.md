[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Apps internas y bases de datos no-code

# ⚙️ Teable

> Base de datos colaborativa sin código sobre PostgreSQL, con vistas tipo hoja, formularios, automatizaciones y funciones de IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 22k | AGPL-3.0 | TypeScript | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de base de datos sin código de código abierto mantenida por Teable (teableio). El núcleo es AGPL-3.0 y los paquetes compartidos MIT; las funciones Enterprise se activan con licencia comercial. Proyecto muy activo que se posiciona como alternativa a Airtable sobre PostgreSQL.

## ¿Qué hace?

Ofrece tablas con vistas de cuadrícula, formulario, kanban, galería y calendario; fórmulas, agrupación, historial de registros, colaboración en tiempo real, consultas SQL y millones de filas. En sus versiones recientes añade chat sobre los datos, automatizaciones disparadas por cambios, horarios o webhooks con pasos de IA, rellenado de campos con IA y un constructor de apps que despliega en contenedores aislados.

## ¿Cómo lo hace?

Está escrito en TypeScript y usa PostgreSQL como almacenamiento, de modo que los datos son tablas SQL reales. El README describe tres formas de ejecutarlo (nube, autoalojado con Docker y desarrollo con pnpm) y una arquitectura con sandbox de agentes en contenedores. Expone API REST y SDK.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Los webhooks y la API de Teable permiten encadenar sus registros con flujos de Activepieces hacia otras apps (combinación por arquitectura). | Teable con un token de API; después crea en Activepieces el disparador webhook o las peticiones HTTP. |
| [supabase](supabase.md) | Teable necesita PostgreSQL: se puede apuntar a una base gestionada como la de Supabase en lugar de mantener una propia (combinación por arquitectura). | Crea el proyecto de Supabase y su cadena de conexión; después configura Teable con esa base. |
| [metabase](metabase.md) | Como los datos de Teable viven en tablas PostgreSQL, Metabase puede leerlos con un usuario de solo lectura para dashboards (combinación por arquitectura). | Teable con datos; después conecta Metabase a PostgreSQL con permisos de lectura. |
| [coolify](coolify.md) | Teable se despliega con Docker Compose y PostgreSQL, un patrón que Coolify gestiona con volúmenes y copias (combinación por arquitectura). | Coolify primero; luego importa el Compose de Teable y configura la base de datos. |

**Notas:** Alternativas (elige una): grist-core, baserow, nocodb. Las funciones de IA y el sandbox de agentes añaden requisitos de contenedores y de proveedor.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada release.2026-11-13T02-21-01Z.3890 (2026-11-13) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/teableio/teable/blob/develop/README.md) · [2](https://help.teable.ai/en/deploy/architecture)</sub>

## Ver similares

Grupo **Herramientas internas y bases de datos no-code**: Teable ocupa la posición 5 de 7 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ToolJet](tooljet.md) ⭐ recomendado | 75 | Si quieres un builder de apps internas con muchos conectores y opciones de IA. |
| 2 | [Appsmith](appsmith.md) | 72 | Si construyes paneles internos arrastrando componentes sobre APIs y bases de datos. |
| 3 | [NocoDB](nocodb.md) | 70 | Si quieres una interfaz tipo Airtable sobre tu base de datos SQL existente. |
| 4 | [Budibase](budibase.md) | 62 | Si quieres formularios, portales y automatizaciones internas con poco código. |
| 5 | **Teable** (esta ficha) | 56 | Si quieres una hoja-base de datos rápida sobre PostgreSQL con buen rendimiento en tablas grandes. |
| 6 | [Grist](grist-core.md) | 53 | Si necesitas una hoja de cálculo relacional con fórmulas en Python. |
| 7 | [Baserow](baserow.md) | 50 | Si buscas una alternativa a Airtable auto-hospedada y fácil de usar. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica y las funciones de IA se configuran por separado; activar un proveedor puede añadir credenciales y consumo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | El coste depende del proveedor o la ruta. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/teableio/teable/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Teable para mi objetivo y necesito pasos guiados. Lee https://github.com/teableio/teable/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Teable con la guía Docker oficial y crea una tabla con un formulario y una vista kanban..

**Qué comprobar:** Los registros enviados por el formulario aparecen en la tabla y en la vista kanban, y se conservan tras reiniciar..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- gestionar un catálogo o pipeline comercial con vistas de cuadrícula, kanban y calendario
- dar a un equipo tablas en PostgreSQL con permisos y API sin escribir backend

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: gestionar un catálogo o pipeline comercial con vistas de cuadrícula, kanban y calendario; dar a un equipo tablas en PostgreSQL con permisos y API sin escribir backend | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Licencia AGPL-3.0 (paquetes bajo packages/ en MIT); la edición Enterprise se activa con licencia comercial.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `data` `no-code` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Grist](grist-core.md) | 12.1k | Hoja de cálculo relacional autoalojable con fórmulas en Python, columnas tipadas y formato portable basado en SQLite. |
| [Baserow](baserow.md) | 6.3k | Base de datos sin código autoalojable (Django y Vue) con constructor de aplicaciones, automatizaciones, dashboards y API-first. |
| [NocoDB](nocodb.md) | 65.5k | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. |

## Enlaces

- 🐙 GitHub: [teableio/teable](https://github.com/teableio/teable)
- 🌐 Web: <https://teable.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/teableio/teable/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
