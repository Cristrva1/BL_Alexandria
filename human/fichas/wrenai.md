[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 📊 WrenAI

> BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.2k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

WrenAI, motor de BI generativo (GenBI) de Canner. El motor (capa semántica MDL, text-to-SQL, MCP, CLI y conectores) es Apache-2.0 y las funciones de seguridad fina y la UI GenBI son comerciales (GitHub muestra NOASSERTION). Es activo (~18k estrellas, wren-v0.18.0).

## ¿Qué hace?

Da a los agentes que ya usas una capa semántica gobernada y una capa de contexto para generar SQL fiable, desplegar paneles y guardar definiciones de negocio en Git. Conecta con más de 22 fuentes (BigQuery, Snowflake, PostgreSQL, ClickHouse, DuckDB y otras) sobre Apache DataFusion.

## ¿Cómo lo hace?

Se instala con `pip install wrenai` (con extras por conector) y se añade como skill con `npx skills add Canner/WrenAI`. Funciona con Claude Code, Cursor, Cline, Codex, clientes MCP y LangChain.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente soportado mediante skill y MCP. | Instala wrenai y añade la skill. |
| [DuckDB](duckdb.md) | Conector DuckDB soportado. | Instala el extra del conector y define el modelo MDL. |
| [langchain](langchain.md) | Integración citada en el README. | Usa WrenAI como herramienta en LangChain. |
| [Apache Superset](superset.md) | Visualizar en Superset las consultas gobernadas. (combinación por arquitectura) | Apunta Superset a la misma base. |

**Notas:** Sin alternativas declaradas. Funciones de seguridad a nivel de fila/columna solo en ediciones de pago.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada wren-v0.18.0 (2026-11-10) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Canner/WrenAI/blob/main/README.md) · [2](https://docs.getwren.ai)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La skill usa el agente; conectores, bases, modelos opcionales y servicios gestionados pueden costar según ruta |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. La capa semántica no garantiza SQL correcto sin definiciones y revisión; la guía actual usa CLI más skills, no solo una app de chat |
| Coste | El coste depende del proveedor o la ruta. La skill usa el agente; conectores, bases, modelos opcionales y servicios gestionados pueden costar según ruta |
| Equipo | Preparación según la ruta elegida. Python; Node para skills; base o muestra jaffle_shop; agente |

La capa semántica no garantiza SQL correcto sin definiciones y revisión; la guía actual usa CLI más skills, no solo una app de chat

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- Node para skills
- base o muestra jaffle_shop
- agente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install wrenai

npx skills add Canner/WrenAI
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Canner/WrenAI/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar WrenAI para mi objetivo y necesito pasos guiados. Lee https://github.com/Canner/WrenAI/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide usar la muestra jaffle_shop y explica una métrica antes de generar su consulta.

**Qué comprobar:** Puedes revisar definición, SQL y resultado sobre la muestra.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Definir ingresos de forma consistente
- Crear dashboards desde preguntas de negocio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Definir ingresos de forma consistente; Crear dashboards desde preguntas de negocio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La capa semántica no garantiza SQL correcto sin definiciones y revisión; la guía actual usa CLI más skills, no solo una app de chat

## Stack y modelos

- **Stack:** Python; Node para skills; base o muestra jaffle_shop; agente
- **Etiquetas:** `analytics` `data` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Canner/WrenAI](https://github.com/Canner/WrenAI)
- 🌐 Web: <https://www.getwren.ai/en/open-core>
- 🧪 Receta: [Analítica de producto con IA](../playbooks/analitica-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Canner/WrenAI/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
