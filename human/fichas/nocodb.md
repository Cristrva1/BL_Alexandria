[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Apps internas y bases de datos no-code

# 🧱 NocoDB

> Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 65.5k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma para crear bases de datos en línea con interfaz de hoja de cálculo, alternativa abierta a Airtable. Desde hace un tiempo usa la Sustainable Use License (no es OSI); es un proyecto muy popular con versiones mensuales.

## ¿Qué hace?

Permite crear, leer, actualizar y borrar tablas, columnas y filas; ordenar, filtrar, agrupar y ocultar columnas; y trabajar con vistas de cuadrícula, galería, formulario, kanban y calendario, con vistas colaborativas o bloqueadas. Expone APIs REST y un SDK, y tiene una «App Store» de integraciones para notificaciones, almacenamiento y más. Casos típicos: CRM ligero, inventarios, seguimiento de proyectos y backends para automatizaciones.

## ¿Cómo lo hace?

Se ejecuta en Docker con SQLite (por defecto) o PostgreSQL (`NC_DB=pg://...`) guardando datos en un volumen; el panel queda en `http://localhost:8080/dashboard`. Para producción existe «Auto-upstall», un script que genera un docker-compose; también hay guías para Kubernetes y Helm. Ya no se publican binarios precompilados.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Pieza oficial de NocoDB en Activepieces para usar la base como origen o destino de flujos. | NocoDB primero; luego la conexión en la pieza. |
| [metabase](metabase.md) | Si NocoDB guarda los datos en PostgreSQL, Metabase puede conectarse a esa base para dashboards (combinación por arquitectura). | Usa NocoDB con PostgreSQL; conecta Metabase con un usuario de solo lectura. |
| [coolify](coolify.md) | Coolify trae una plantilla de servicio oficial (`nocodb`) para desplegar NocoDB con un clic. | Coolify primero; luego despliega la plantilla `nocodb` y configura la base de datos. |

**Notas:** Alternativas (elige una): appsmith, budibase.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada 2026.10.1 (2026-10-29) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/nocodb/nocodb/blob/develop/README.md) · [2](https://www.activepieces.com/pieces/nocodb) · [3](https://github.com/activepieces/activepieces/tree/main/packages/pieces/community/nocodb) · [4](https://github.com/coollabsio/coolify/tree/main/templates/compose)</sub>

## Ver similares

Grupo **Herramientas internas y bases de datos no-code**: NocoDB ocupa la posición 3 de 7 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ToolJet](tooljet.md) ⭐ recomendado | 75 | Si quieres un builder de apps internas con muchos conectores y opciones de IA. |
| 2 | [Appsmith](appsmith.md) | 72 | Si construyes paneles internos arrastrando componentes sobre APIs y bases de datos. |
| 3 | **NocoDB** (esta ficha) | 70 | Si quieres una interfaz tipo Airtable sobre tu base de datos SQL existente. |
| 4 | [Budibase](budibase.md) | 62 | Si quieres formularios, portales y automatizaciones internas con poco código. |
| 5 | [Teable](teable.md) | 56 | Si quieres una hoja-base de datos rápida sobre PostgreSQL con buen rendimiento en tablas grandes. |
| 6 | [Grist](grist-core.md) | 53 | Si necesitas una hoja de cálculo relacional con fórmulas en Python. |
| 7 | [Baserow](baserow.md) | 50 | Si buscas una alternativa a Airtable auto-hospedada y fácil de usar. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ruta básica no requiere LLM; hosting, funciones comerciales e integraciones tienen condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El primer ejemplo Docker es de evaluación local; no reutilices los secretos de ejemplo para un despliegue público |
| Coste | Sin pago a un modelo en la ruta básica. La ruta básica no requiere LLM; hosting, funciones comerciales e integraciones tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Docker;  carpeta de datos;  navegador |

El primer ejemplo Docker es de evaluación local; no reutilices los secretos de ejemplo para un despliegue público

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
-  carpeta de datos
-  navegador

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
docker run -d \
  --name noco \
  -v "$(pwd)"/nocodb:/usr/app/data/ \
  -p 8080:8080 \
  nocodb/nocodb:latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/nocodb/nocodb/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar NocoDB para mi objetivo y necesito pasos guiados. Lee https://github.com/nocodb/nocodb/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una tabla con nombre y estado e introduce dos registros de prueba.

**Qué comprobar:** Puedes editar los registros y filtrarlos por su estado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Mantener un inventario sencillo con vistas para distintas personas
- Revisar datos de clientes en una interfaz tabular

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Mantener un inventario sencillo con vistas para distintas personas; Revisar datos de clientes en una interfaz tabular | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El primer ejemplo Docker es de evaluación local; no reutilices los secretos de ejemplo para un despliegue público

## Stack y modelos

- **Stack:** Docker;  carpeta de datos;  navegador
- **Etiquetas:** `data` `automation` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Appsmith](appsmith.md) | 41.3k | Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases. |
| [Budibase](budibase.md) | 28.4k | Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos. |
| [Grist](grist-core.md) | 12.1k | Hoja de cálculo relacional autoalojable con fórmulas en Python, columnas tipadas y formato portable basado en SQLite. |
| [Baserow](baserow.md) | 6.3k | Base de datos sin código autoalojable (Django y Vue) con constructor de aplicaciones, automatizaciones, dashboards y API-first. |
| [Teable](teable.md) | 22k | Base de datos colaborativa sin código sobre PostgreSQL, con vistas tipo hoja, formularios, automatizaciones y funciones de IA. |

## Enlaces

- 🐙 GitHub: [nocodb/nocodb](https://github.com/nocodb/nocodb)
- 🌐 Web: <https://nocodb.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/nocodb/nocodb/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
