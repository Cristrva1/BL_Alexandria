[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Apps internas y bases de datos no-code

# 🧱 ToolJet

> Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 41.2k | AGPL-3.0 | HTML | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 75/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de código abierto para construir herramientas internas (paneles de administración, dashboards y apps operativas) sobre tus bases de datos, APIs y servicios SaaS, de ToolJet Solutions. La edición comunitaria tiene licencia AGPL v3; existen ToolJet Cloud y funciones de IA en la edición Enterprise.

## ¿Qué hace?

Ofrece un constructor visual con más de 80 componentes (tablas, gráficos, formularios, listas), una base de datos sin código integrada, apps de varias páginas con edición multijugador y más de 90 fuentes de datos. Incluye flujos de trabajo con ramas, programados o disparados por webhook, ejecución de JavaScript y Python dentro de las apps, comentarios y control de acceso granular. La generación de apps desde lenguaje natural y el constructor de consultas con IA son de la edición Enterprise.

## ¿Cómo lo hace?

Se prueba con un contenedor Docker (`tooljet/try:ee-lts-latest`, puerto 80) que incluye PostgreSQL en un volumen; en producción se despliega con Docker, Kubernetes o en AWS, GCP y Azure, y se recomienda la versión LTS. Los datos pasan por un proxy del servidor con cifrado AES-256-GCM y soporte de SSO. Trae un servidor MCP (en beta) y plugins para Claude Code, Codex y Grok Build que construyen apps contra los contratos reales de componentes y datos; los conectores propios se crean con la CLI `@tooljet/cli`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin y servidor MCP oficiales: el agente genera páginas, consultas y componentes de ToolJet desde un prompt y modifica apps existentes. | ToolJet en marcha; después instala el plugin o registra el MCP siguiendo la guía de ToolJet MCP (beta). |
| [Codex CLI](codex.md) | También compatible como plugin según el README, para quien trabaja con Codex en lugar de Claude Code. | Igual que con Claude Code; usa solo un agente a la vez sobre la misma app. |
| [activepieces](activepieces.md) | Los flujos de ToolJet aceptan disparadores por webhook y las apps pueden llamar a webhooks de Activepieces para tareas con muchas integraciones (combinación por arquitectura). | Crea primero el webhook en el sistema que recibe y protégelo con un token. |

**Notas:** Alternativas (elige una): appsmith, budibase. El contenedor de prueba usa la imagen Enterprise (ee); revisa qué funciones requieren licencia.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v3.20.257-lts (2026-11-12) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ToolJet/ToolJet/blob/develop/README.md) · [2](https://docs.tooljet.com/docs/build-with-ai/mcp/overview)</sub>

## Ver similares

Grupo **Herramientas internas y bases de datos no-code**: ToolJet ocupa la posición 1 de 7 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **ToolJet** (esta ficha) ⭐ recomendado | 75 | Si quieres un builder de apps internas con muchos conectores y opciones de IA. |
| 2 | [Appsmith](appsmith.md) | 72 | Si construyes paneles internos arrastrando componentes sobre APIs y bases de datos. |
| 3 | [NocoDB](nocodb.md) | 70 | Si quieres una interfaz tipo Airtable sobre tu base de datos SQL existente. |
| 4 | [Budibase](budibase.md) | 63 | Si quieres formularios, portales y automatizaciones internas con poco código. |
| 5 | [Teable](teable.md) | 56 | Si quieres una hoja-base de datos rápida sobre PostgreSQL con buen rendimiento en tablas grandes. |
| 6 | [Grist](grist-core.md) | 54 | Si necesitas una hoja de cálculo relacional con fórmulas en Python. |
| 7 | [Baserow](baserow.md) | 50 | Si buscas una alternativa a Airtable auto-hospedada y fácil de usar. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La edición y alojamiento de ToolJet tienen sus planes; el agente y los proveedores de IA se contabilizan por separado |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. Claude Code y Codex tienen plugins documentados; Antigravity puede conectarse por MCP, sin que esto incluya el alojamiento de la plataforma |
| Coste | El coste depende del proveedor o la ruta. La edición y alojamiento de ToolJet tienen sus planes; el agente y los proveedores de IA se contabilizan por separado |
| Equipo | Preparación según la ruta elegida. Instancia ToolJet de prueba;  conexión de datos ficticios;  cliente MCP si eliges esa ruta |

Claude Code y Codex tienen plugins documentados; Antigravity puede conectarse por MCP, sin que esto incluya el alojamiento de la plataforma

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instancia ToolJet de prueba
- conexión de datos ficticios
- cliente MCP si eliges esa ruta

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker run --name tooljet --restart unless-stopped -p 80:80 --platform linux/amd64 -v tooljet_data:/var/lib/postgresql/13/main tooljet/try:ee-lts-latest
```

Comando copiado literalmente de el README (sección «Try using Docker»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/ToolJet/ToolJet/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ToolJet para mi objetivo y necesito pasos guiados. Lee https://github.com/ToolJet/ToolJet/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una página con una tabla y enlázala a un pequeño conjunto de datos.

**Qué comprobar:** La tabla muestra los datos y puedes revisar la consulta que los obtiene.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un panel interno para consultar pedidos y su estado
- Pedir a un agente construir una interfaz ToolJet mediante el servidor MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un panel interno para consultar pedidos y su estado; Pedir a un agente construir una interfaz ToolJet mediante el servidor MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Claude Code y Codex tienen plugins documentados; Antigravity puede conectarse por MCP, sin que esto incluya el alojamiento de la plataforma

## Stack y modelos

- **Stack:** Instancia ToolJet de prueba;  conexión de datos ficticios;  cliente MCP si eliges esa ruta
- **Etiquetas:** `ui` `automation` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Appsmith](appsmith.md) | 41.3k | Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases. |
| [Budibase](budibase.md) | 28.4k | Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos. |

## Enlaces

- 🐙 GitHub: [ToolJet/ToolJet](https://github.com/ToolJet/ToolJet)
- 🌐 Web: <https://tooljet.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ToolJet/ToolJet/blob/main/README.md)
- [Fuente 2](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
