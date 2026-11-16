[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Apps internas y bases de datos no-code

# ⚙️ Baserow

> Base de datos sin código autoalojable (Django y Vue) con constructor de aplicaciones, automatizaciones, dashboards y API-first.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.3k | MIT | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Puntuación de calidad** 50/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de base de datos sin código de Baserow B.V. con núcleo MIT y funciones premium y enterprise bajo licencia propia. Proyecto maduro que se trasladó de GitLab a GitHub; ofrece nube y autoalojamiento.

## ¿Qué hace?

Permite crear bases relacionales con interfaz de hoja de cálculo, publicar aplicaciones y portales en un dominio propio, automatizar tareas repetitivas, montar dashboards y usar un asistente de IA (Kuma) para generar estructuras. Es API-first y headless, útil como backend sencillo de herramientas internas.

## ¿Cómo lo hace?

Usa Django, Vue.js y PostgreSQL. La vía más rápida es un único contenedor (`docker run -v baserow_data:/baserow/data -p 80:80 -p 443:443 baserow/baserow:<versión>`); también hay Docker Compose, Helm y otras guías. Cada tabla expone endpoints REST documentados automáticamente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | La API REST y los webhooks de Baserow permiten disparar o alimentar flujos de Activepieces (combinación por arquitectura). | Baserow con un token de base de datos; después crea el flujo en Activepieces. |
| [metabase](metabase.md) | Metabase puede leer la base PostgreSQL de Baserow con un usuario de solo lectura para análisis más complejos que sus dashboards (combinación por arquitectura). | Baserow con PostgreSQL accesible; después conecta Metabase con permisos de lectura. |
| [coolify](coolify.md) | El contenedor único de Baserow encaja con un despliegue gestionado por Coolify con volumen persistente (combinación por arquitectura). | Coolify primero; luego crea el servicio con la imagen baserow/baserow y el volumen de datos. |

**Notas:** Alternativas (elige una): grist-core, teable, nocodb. Comprueba qué funciones son premium antes de planificar un despliegue.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 2.4.3 (2026-11-14) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/baserow/baserow/blob/develop/README.md) · [2](https://baserow.io/docs/installation/install-with-docker)</sub>

## Ver similares

Grupo **Herramientas internas y bases de datos no-code**: Baserow ocupa la posición 7 de 7 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ToolJet](tooljet.md) ⭐ recomendado | 75 | Si quieres un builder de apps internas con muchos conectores y opciones de IA. |
| 2 | [Appsmith](appsmith.md) | 72 | Si construyes paneles internos arrastrando componentes sobre APIs y bases de datos. |
| 3 | [NocoDB](nocodb.md) | 70 | Si quieres una interfaz tipo Airtable sobre tu base de datos SQL existente. |
| 4 | [Budibase](budibase.md) | 62 | Si quieres formularios, portales y automatizaciones internas con poco código. |
| 5 | [Teable](teable.md) | 56 | Si quieres una hoja-base de datos rápida sobre PostgreSQL con buen rendimiento en tablas grandes. |
| 6 | [Grist](grist-core.md) | 53 | Si necesitas una hoja de cálculo relacional con fórmulas en Python. |
| 7 | **Baserow** (esta ficha) | 50 | Si buscas una alternativa a Airtable auto-hospedada y fácil de usar. |

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
docker run -v baserow_data:/baserow/data -p 80:80 -p 443:443 baserow/baserow:2.4.3
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/baserow/baserow/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Baserow para mi objetivo y necesito pasos guiados. Lee https://github.com/baserow/baserow/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca el contenedor de la documentación con un volumen de datos y crea una base con una tabla y un formulario..

**Qué comprobar:** El formulario guarda filas en la tabla y la API REST devuelve esos registros con un token..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- crear una base de clientes o inventario compartida sin escribir backend
- publicar un portal o formulario sobre tus propias tablas en tu dominio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: crear una base de clientes o inventario compartida sin escribir backend; publicar un portal o formulario sobre tus propias tablas en tu dominio | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Open-core: el núcleo es MIT, pero las funciones premium y enterprise tienen licencia propia.

## Stack y modelos

- **Stack:** Python, docker-compose.yml
- **Etiquetas:** `data` `no-code` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Grist](grist-core.md) | 12.1k | Hoja de cálculo relacional autoalojable con fórmulas en Python, columnas tipadas y formato portable basado en SQLite. |
| [Teable](teable.md) | 22k | Base de datos colaborativa sin código sobre PostgreSQL, con vistas tipo hoja, formularios, automatizaciones y funciones de IA. |
| [NocoDB](nocodb.md) | 65.5k | Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. |

## Enlaces

- 🐙 GitHub: [baserow/baserow](https://github.com/baserow/baserow)
- 🌐 Web: <https://baserow.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/baserow/baserow/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
