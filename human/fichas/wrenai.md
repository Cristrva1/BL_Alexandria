[🏠 Inicio](../README.md) › [📊 Analizar datos, crear dashboards y mapas](../categorias/10-anal-tica-visualizaci-n.md) › BI, dashboards y chat con datos

# 📊 WrenAI

> BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.2k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Define tu modelo de datos una vez y los usuarios (o agentes) preguntan en lenguaje natural para obtener SQL, gráficos y respuestas.

## Por qué destaca

La capa semántica reduce errores frente al text-to-SQL directo.

## Cómo funciona

Un motor semántico (MDL) describe tablas y métricas; el LLM genera SQL contra ese modelo con RAG.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install wrenai
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/Canner/WrenAI/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar WrenAI para mi objetivo y necesito pasos guiados. Lee https://github.com/Canner/WrenAI/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Preguntar a la base de ventas
- Dashboards generados con IA
- Agentes con acceso a datos de negocio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres text-to-SQL confiable para el negocio | solo analizas un CSV; mira `pandas-ai` |

**Limitaciones:** Licencia AGPL-3.0.

## Stack y modelos

- **Stack:** Python, TypeScript, Rust
- **Etiquetas:** `analytics` `data` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Apache Superset](superset.md) | 75.5k | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. |
| [DuckDB](duckdb.md) | 43.1k | Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PandasAI](pandas-ai.md) | 23.9k | Librería para conversar con tus datos (SQL, CSV, Parquet) usando LLM. |

## Enlaces

- 🐙 GitHub: [Canner/WrenAI](https://github.com/Canner/WrenAI)
- 🌐 Web: <https://www.getwren.ai/en/open-core>
- 🧪 Receta: [Analítica de producto con IA](../playbooks/analitica-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Canner/WrenAI/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
