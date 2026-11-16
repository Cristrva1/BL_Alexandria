[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Apps internas y bases de datos no-code

# ⚙️ Grist

> Hoja de cálculo relacional autoalojable con fórmulas en Python, columnas tipadas y formato portable basado en SQLite.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.1k | Apache-2.0 | TypeScript | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Servidor de la edición Community de Grist (Apache-2.0), mantenido por Grist Labs (Nueva York) con contribuciones relevantes de organismos públicos franceses. Proyecto maduro con desarrollo continuo; Grist Labs vende hosting y una edición con funciones adicionales bajo licencia propietaria.

## ¿Qué hace?

Combina la flexibilidad de una hoja de cálculo con la estructura de una base de datos: columnas con nombre y tipo, referencias entre tablas (también bidireccionales), fórmulas en Python con biblioteca estándar y muchas funciones de Excel, vistas de formulario, tarjeta y gráfico, y reglas de acceso granulares. Sirve para inventarios, CRM sencillos, seguimiento de proyectos o publicar datos en una web estática con grist-static.

## ¿Cómo lo hace?

El servidor está escrito en TypeScript y ejecuta las fórmulas en un sandbox de Python; cada documento es un archivo SQLite autocontenido, legible por cualquier herramienta SQLite y fácil de respaldar. Se prueba con `docker run -p 8484:8484 -it gristlabs/grist` y se persiste montando `/persist`; existen además una app de escritorio (grist-desktop) y una compilación solo navegador (grist-static). Ofrece API REST y webhooks.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | La API REST y los webhooks de Grist permiten disparar flujos de Activepieces cuando cambia una fila o escribir resultados de vuelta en una tabla (combinación por arquitectura). | Grist en marcha con una clave de API; después crea en Activepieces el flujo con peticiones HTTP o webhook. |
| [DuckDB](duckdb.md) | Un documento .grist es SQLite: DuckDB puede adjuntarlo con su extensión sqlite para consultas analíticas sin tocar el servidor (combinación por arquitectura). | Copia el documento .grist; después ábrelo en DuckDB en modo solo lectura. |
| [coolify](coolify.md) | Grist se distribuye como imagen Docker de un solo contenedor, fácil de desplegar y respaldar desde Coolify con su volumen /persist (combinación por arquitectura). | Coolify primero; luego crea el servicio con la imagen gristlabs/grist y un volumen persistente. |
| [Claude Code](claude-code.md) | Un agente de código puede escribir fórmulas Python o scripts contra la API REST de Grist para migrar o limpiar datos (combinación por arquitectura). | Grist accesible y una clave de API de un documento de prueba; después pide al agente el script. |

**Notas:** Alternativas (elige una): baserow, teable, nocodb. Si activas el asistente de IA, las fórmulas y el contexto se envían al proveedor configurado.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.7.22 (2026-10-29) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/gristlabs/grist-core/blob/main/README.md) · [2](https://support.getgrist.com/self-managed/)</sub>

## Ver similares

Grupo **Herramientas internas y bases de datos no-code**: Grist ocupa la posición 6 de 7 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ToolJet](tooljet.md) ⭐ recomendado | 75 | Si quieres un builder de apps internas con muchos conectores y opciones de IA. |
| 2 | [Appsmith](appsmith.md) | 72 | Si construyes paneles internos arrastrando componentes sobre APIs y bases de datos. |
| 3 | [NocoDB](nocodb.md) | 70 | Si quieres una interfaz tipo Airtable sobre tu base de datos SQL existente. |
| 4 | [Budibase](budibase.md) | 62 | Si quieres formularios, portales y automatizaciones internas con poco código. |
| 5 | [Teable](teable.md) | 56 | Si quieres una hoja-base de datos rápida sobre PostgreSQL con buen rendimiento en tablas grandes. |
| 6 | **Grist** (esta ficha) | 53 | Si necesitas una hoja de cálculo relacional con fórmulas en Python. |
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

**Entrada documentada (consulta la sintaxis original):**

```
docker run -p 8484:8484 -it gristlabs/grist
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/gristlabs/grist-core/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Grist para mi objetivo y necesito pasos guiados. Lee https://github.com/gristlabs/grist-core/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca la imagen Docker de prueba, crea un documento con dos tablas enlazadas y una fórmula Python..

**Qué comprobar:** La fórmula se recalcula al editar la tabla referenciada y el documento sigue disponible tras reiniciar con /persist montado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- sustituir una hoja compartida por tablas relacionadas con permisos por fila
- montar un inventario o CRM ligero en tu propio servidor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: sustituir una hoja compartida por tablas relacionadas con permisos por fila; montar un inventario o CRM ligero en tu propio servidor | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Open-core: grist-core es Apache-2.0, pero algunas extensiones de la edición Enterprise usan licencia propietaria.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, package.json
- **Etiquetas:** `data` `spreadsheet` `docker` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Baserow](baserow.md) | 6.3k | Base de datos sin código autoalojable (Django y Vue) con constructor de aplicaciones, automatizaciones, dashboards y API-first. |
| [Teable](teable.md) | 22k | Base de datos colaborativa sin código sobre PostgreSQL, con vistas tipo hoja, formularios, automatizaciones y funciones de IA. |
| [NocoDB](nocodb.md) | 65.5k | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. |

## Enlaces

- 🐙 GitHub: [gristlabs/grist-core](https://github.com/gristlabs/grist-core)
- 🌐 Web: <https://www.getgrist.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/gristlabs/grist-core/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
