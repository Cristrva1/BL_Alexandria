[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 🖥️ Evidence

> BI como código: informes y visualizaciones interactivas escritos en SQL y Markdown, autoalojables o publicados en Evidence Studio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.1k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de BI de código abierto (MIT) de Evidence (evidence.dev), con plataforma de publicación comercial (Evidence Studio). Activa.

## ¿Qué hace?

Alternativa basada en código a las herramientas de BI de arrastrar y soltar: los informes se escriben con SQL y Markdown, con gráficos, tablas, filtros y páginas parametrizadas. Se desarrolla con su agente o en local con Claude Code, Cursor u otros, y se autoaloja o publica en Evidence Studio.

## ¿Cómo lo hace?

Se instala con `curl -fsSL https://evidence.studio/install.sh | sh` en macOS/Linux (instalador para Windows aparte). Conecta con bases como PostgreSQL, Snowflake, BigQuery o archivos, y usa DuckDB para combinar los resultados.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DuckDB](duckdb.md) | Evidence usa DuckDB como motor para combinar y consultar las fuentes de datos de los informes. | Nada que instalar aparte; añade archivos o bases como fuentes del proyecto. |
| [Claude Code](claude-code.md) | El README indica que los informes pueden desarrollarse en local con Claude Code, al ser archivos SQL y Markdown. | Crea el proyecto de Evidence; después pide al agente páginas y consultas nuevas. |
| [supabase](supabase.md) | Una base PostgreSQL de Supabase puede ser fuente de datos de Evidence mediante su conector PostgreSQL (combinación por arquitectura). | Crea un usuario de solo lectura en Supabase; después configura la fuente en Evidence. |

**Notas:** Alternativas cercanas en el catálogo: metabase, superset.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada @evidence-dev/evidence@40.1.8 (2026-02-06) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/evidence-dev/evidence/blob/main/README.md) · [2](https://docs.evidence.studio)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
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

[Instrucciones originales de instalación](https://github.com/evidence-dev/evidence/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Evidence para mi objetivo y necesito pasos guiados. Lee https://github.com/evidence-dev/evidence/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Evidence con el script del README, crea un proyecto de ejemplo y abre el servidor local..

**Qué comprobar:** Ves un informe con gráficos generados a partir de las consultas SQL del Markdown..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- publicar informes de negocio versionados en git
- generar dashboards con SQL que un agente de código puede editar

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: publicar informes de negocio versionados en git; generar dashboards con SQL que un agente de código puede editar | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `dataviz` `analytics` `typescript` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [evidence-dev/evidence](https://github.com/evidence-dev/evidence)
- 🌐 Web: <https://evidence.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/evidence-dev/evidence/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
