[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# ⚙️ Temporal

> Plataforma de ejecución duradera: workflows en código que sobreviven a fallos, con reintentos, temporizadores y estado persistido por el servidor.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24.4k | MIT | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Servidor de ejecución duradera de código abierto (MIT) desarrollado por Temporal Technologies, la empresa de los creadores de Cadence en Uber, del que es un fork. Tecnología madura usada en producción; existe una oferta gestionada (Temporal Cloud) aparte.

## ¿Qué hace?

Ejecuta workflows definidos como código de forma resiliente: persiste cada paso, reintenta automáticamente actividades fallidas, gestiona temporizadores de días o meses y permite consultar, señalar o cancelar ejecuciones en curso. Se usa para orquestar microservicios, transacciones largas, pipelines y, cada vez más, agentes de IA que deben sobrevivir a caídas.

## ¿Cómo lo hace?

El servidor está escrito en Go y almacena el historial en Cassandra, PostgreSQL, MySQL o SQLite (desarrollo); la lógica vive en workers del usuario que usan los SDK oficiales. Para empezar basta la CLI (`brew install temporal` y `temporal server start-dev`), que incluye interfaz web; en producción se despliega con Helm o Docker y una base de datos persistente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenAI Agents SDK](openai-agents-python.md) | El SDK de Python de Temporal publica una integración con el OpenAI Agents SDK para ejecutar agentes como workflows duraderos con reintentos y reanudación. | Servidor de Temporal primero; después instala el SDK de Python de Temporal con la integración y define el agente dentro de un workflow. |
| [Pydantic AI](pydantic-ai.md) | Pydantic AI documenta ejecución duradera de agentes sobre Temporal: cada llamada a modelo y herramienta se convierte en actividad reintentable. | Servidor de Temporal en marcha; después instala pydantic-ai con su extra de Temporal y registra el worker. |
| [LangGraph](langgraph.md) | El SDK de Python de Temporal incluye un módulo contrib para LangGraph que ejecuta grafos de agentes como workflows duraderos. | Servidor de Temporal primero; después usa el módulo temporalio.contrib.langgraph con tu grafo. |
| [Grafana](grafana.md) | El servidor y los SDK exponen métricas de Prometheus y Temporal mantiene paneles de Grafana para vigilar latencias y colas de tareas. | Configura la exportación de métricas a Prometheus; después importa los paneles en Grafana. |
| [Claude Code](claude-code.md) | Un agente de código puede escribir workflows y actividades con los SDK y probarlos contra el servidor de desarrollo local (combinación por arquitectura). | `temporal server start-dev` primero; después pide al agente el worker y ejecútalo en local. |

**Notas:** Temporal no es un orquestador de datos por calendario como Airflow: modela procesos de aplicación duraderos. La persistencia de producción requiere una base de datos dimensionada.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.32.2 (2026-11-02) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/temporalio/temporal/blob/main/README.md) · [2](https://docs.temporal.io/) · [3](https://ai.pydantic.dev/durable_execution/temporal/) · [4](https://github.com/temporalio/sdk-python/tree/main/temporalio/contrib) · [5](https://github.com/temporalio/dashboards)</sub>

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

**Entrada documentada (consulta la sintaxis original):**

```
brew install temporal
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/temporalio/temporal/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Temporal para mi objetivo y necesito pasos guiados. Lee https://github.com/temporalio/temporal/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala la CLI con `brew install temporal`, arranca el servidor de desarrollo y ejecuta el ejemplo hello-world de un SDK..

**Qué comprobar:** El workflow aparece completado en la interfaz web local con su historial de eventos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- procesos de negocio largos como pagos o altas que deben completarse aunque caiga un servicio
- agentes de IA con pasos largos que necesitan reintentos y reanudación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: procesos de negocio largos como pagos o altas que deben completarse aunque caiga un servicio; agentes de IA con pasos largos que necesitan reintentos y reanudación | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Go, go.mod
- **Etiquetas:** `automation` `go` `server` `agents`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [temporalio/temporal](https://github.com/temporalio/temporal)
- 🌐 Web: <https://docs.temporal.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/temporalio/temporal/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
