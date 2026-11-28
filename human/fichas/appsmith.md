[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Apps internas y bases de datos no-code

# 🧱 Appsmith

> Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 41.3k | Apache-2.0 | TypeScript | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; despliegue con Kubernetes/Helm

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma low-code de código abierto (Apache 2.0) para desarrollar, desplegar y mantener aplicaciones internas, de Appsmith Inc. Se usa en su nube o autoalojada y publica versiones con frecuencia.

## ¿Qué hace?

Permite construir dashboards, paneles de administración, vistas «customer 360», automatización de TI y herramientas de gestión de servicios conectando bases de datos y APIs con componentes visuales y JavaScript. Ofrece plantillas y un portal comunitario, y presenta Appsmith Agents para integrar modelos de IA con datos privados dentro de las herramientas del equipo.

## ¿Cómo lo hace?

Se instala principalmente con Docker (imagen `appsmith/appsmith-ce`) o Kubernetes siguiendo sus guías; también puede usarse Appsmith Cloud. GitHub muestra un monorepo con TypeScript y JavaScript en el frontend y Java en el backend. Las apps se conectan a fuentes como PostgreSQL mediante consultas configuradas en el editor [DATO NO VERIFICADO: base de datos interna que usa la imagen].

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [supabase](supabase.md) | Appsmith consulta PostgreSQL de forma nativa y Supabase ofrece un PostgreSQL gestionado con autenticación, así que sirve como backend de la app interna (combinación por arquitectura). | Supabase primero; crea un usuario con permisos mínimos y conéctalo como fuente PostgreSQL en Appsmith. |
| [activepieces](activepieces.md) | Un botón de Appsmith llama a un webhook de Activepieces para tareas que tocan muchos servicios (combinación por arquitectura). | Crea el webhook en Activepieces, protégelo con un encabezado secreto y configúralo como API en Appsmith. |
| [metabase](metabase.md) | Appsmith cubre los formularios y acciones; Metabase, los análisis y dashboards sobre la misma base (combinación por arquitectura). | Conecta ambos a la base con usuarios distintos: Metabase solo lectura. |

**Notas:** Alternativas (elige una): tooljet, budibase, nocodb.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v2.7.0 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/appsmithorg/appsmith/blob/release/README.md) · [2](https://docs.appsmith.com/connect-data/reference/querying-postgres) · [3](https://docs.appsmith.com/advanced-concepts/version-control-with-git) · [4](https://docs.appsmith.com/getting-started/setup/manage-plans/downgrade-plan?downgrade-plan-type=remove-license-key)</sub>

## Ver similares

Grupo **Herramientas internas y bases de datos no-code**: Appsmith ocupa la posición 2 de 7 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ToolJet](tooljet.md) ⭐ recomendado | 75 | Si quieres un builder de apps internas con muchos conectores y opciones de IA. |
| 2 | **Appsmith** (esta ficha) | 72 | Si construyes paneles internos arrastrando componentes sobre APIs y bases de datos. |
| 3 | [NocoDB](nocodb.md) | 70 | Si quieres una interfaz tipo Airtable sobre tu base de datos SQL existente. |
| 4 | [Budibase](budibase.md) | 63 | Si quieres formularios, portales y automatizaciones internas con poco código. |
| 5 | [Teable](teable.md) | 56 | Si quieres una hoja-base de datos rápida sobre PostgreSQL con buen rendimiento en tablas grandes. |
| 6 | [Grist](grist-core.md) | 54 | Si necesitas una hoja de cálculo relacional con fórmulas en Python. |
| 7 | [Baserow](baserow.md) | 50 | Si buscas una alternativa a Airtable auto-hospedada y fácil de usar. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El autoalojamiento, los planes y las funciones de IA tienen condiciones distintas; consulta la edición que vas a usar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La función principal son interfaces internas sobre datos; una API de negocio no equivale a una API de modelo |
| Coste | El coste depende del proveedor o la ruta. El autoalojamiento, los planes y las funciones de IA tienen condiciones distintas; consulta la edición que vas a usar |
| Equipo | Preparación según la ruta elegida. Cuenta o instancia de prueba;  una fuente de datos de demostración |

La función principal son interfaces internas sobre datos; una API de negocio no equivale a una API de modelo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta o instancia de prueba
- una fuente de datos de demostración

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
helm install appsmith appsmith/appsmith -n appsmith --wait --timeout 10m --set mongodb.enabled=false --set mongodbCommunity.enabled=true --set mongodbOperator.enabled=true
```

Comando copiado literalmente de la documentación del repositorio (sección «Quickstart — fresh install with bundled operator»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/appsmithorg/appsmith/blob/release/deploy/helm/docs/install-mongodb-operator.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Appsmith para mi objetivo y necesito pasos guiados. Lee https://github.com/appsmithorg/appsmith/blob/release/deploy/helm/docs/install-mongodb-operator.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade una tabla a una página y asóciala a una consulta de datos ficticios.

**Qué comprobar:** La tabla se actualiza al ejecutar la consulta y muestra los registros esperados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un panel para que soporte consulte expedientes
- Construir un formulario interno que actualiza datos mediante una API

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Necesitas un panel interno sobre APIs o bases de datos, con lógica JavaScript, widgets propios o versionado con Git en el plan Free. | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Appsmith Free documenta hasta tres repos privados por espacio de trabajo. Las prestaciones de permisos y despliegue dependen de la edición.

## Stack y modelos

- **Stack:** Cuenta o instancia de prueba;  una fuente de datos de demostración
- **Etiquetas:** `ui` `automation` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ToolJet](tooljet.md) | 41.2k | Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA. |
| [Budibase](budibase.md) | 28.4k | Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos. |
| [NocoDB](nocodb.md) | 65.5k | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. |

## Enlaces

- 🐙 GitHub: [appsmithorg/appsmith](https://github.com/appsmithorg/appsmith)
- 🌐 Web: <https://www.appsmith.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/appsmithorg/appsmith/blob/release/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
