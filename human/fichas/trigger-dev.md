[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 Trigger.dev

> Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.8k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de código abierto (Apache 2.0) para crear flujos de IA y tareas en segundo plano en TypeScript. Ofrece un servicio gestionado y guías oficiales de autoalojamiento; publica versiones con frecuencia (serie 4.x).

## ¿Qué hace?

Ejecuta tareas largas sin límites de tiempo (a diferencia de AWS Lambda o Vercel), con reintentos, colas, idempotencia, cron duraderos de hasta un año y escalado elástico. Permite pausar tareas hasta que una persona apruebe o rechace, transmitir respuestas de LLM en tiempo real a tu app y ver trazas y logs de cada ejecución con alertas de error. Casos típicos: agentes de IA, procesamiento de video o PDF, scraping con navegador y trabajos programados.

## ¿Cómo lo hace?

Las tareas se escriben en tu propio código con el SDK `@trigger.dev/sdk` (función `task`) y se despliegan a la nube de Trigger.dev o a una instancia propia. Las «build extensions» añaden paquetes de sistema a la imagen de ejecución, por ejemplo FFmpeg, Playwright o scripts Python. Cada ejecución tiene etiquetas, ramas de vista previa integradas con Vercel y Git, y una API Realtime para suscribirse al estado. El autoalojamiento se hace con Docker Compose o con su chart de Helm para Kubernetes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [AI SDK (Vercel)](vercel-ai.md) | Trigger.dev documenta ejemplos con el AI SDK de Vercel para ejecutar llamadas de IA largas como tareas duraderas y transmitir el resultado. | Mismo proyecto TypeScript: instala el SDK de Trigger.dev y el AI SDK; las claves del proveedor van en las variables de entorno de Trigger. |
| [FFmpeg](ffmpeg.md) | La build extension oficial de FFmpeg permite procesar audio y video dentro de las tareas sin límites de tiempo. | Añade la extensión en `trigger.config` antes de desplegar; no hace falta instalar FFmpeg en tu máquina. |
| [playwright](playwright.md) | La build extension de Playwright instala navegadores en la imagen de ejecución para scraping o pruebas desde tareas en segundo plano. | Declara la extensión en la configuración y despliega; cuida la memoria de cada ejecución. |
| [langfuse](langfuse.md) | Registra trazas y costes de las llamadas a LLM hechas dentro de las tareas (combinación por arquitectura; no encontré guía oficial conjunta). | Langfuse primero para obtener claves; luego instrumenta el código de las tareas con su SDK. |

**Notas:** Alternativas (elige una): windmill, kestra.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v4.8.5 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/triggerdotdev/trigger.dev/blob/main/README.md) · [2](https://trigger.dev/docs/guides/examples/vercel-ai-sdk) · [3](https://trigger.dev/docs/config/extensions/ffmpeg) · [4](https://trigger.dev/docs/config/extensions/playwright)</sub>

## Ver similares

Grupo **Orquestadores de workflows de datos y tareas**: Trigger.dev ocupa la posición 4 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Apache Airflow](airflow.md) ⭐ recomendado | 81 | Si necesitas el estándar de la industria para pipelines por lotes con un ecosistema enorme de operadores. |
| 2 | [Kestra](kestra.md) | 80 | Si prefieres definir flujos en YAML con interfaz web y disparadores por eventos. |
| 3 | [Prefect](prefect.md) | 68 | Si quieres convertir funciones Python en flujos observables con muy poco código. |
| 4 | **Trigger.dev** (esta ficha) | 68 | Si trabajas en TypeScript y quieres tareas de fondo largas sin gestionar colas. |
| 5 | [Windmill](windmill.md) | 61 | Si quieres scripts en varios lenguajes convertidos en flujos y apps internas rápidas. |
| 6 | [Dagster](dagster.md) | 57 | Si piensas en activos de datos (tablas, modelos) con linaje y pruebas. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El servicio y la infraestructura tienen su propio consumo; el LLM solo se paga si tu tarea lo llama |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es infraestructura de tareas duraderas; no incluye por sí misma un modelo de IA |
| Coste | El coste depende del proveedor o la ruta. El servicio y la infraestructura tienen su propio consumo; el LLM solo se paga si tu tarea lo llama |
| Equipo | Preparación según la ruta elegida. Proyecto TypeScript;  entorno y cuenta o despliegue indicado por la guía |

Es infraestructura de tareas duraderas; no incluye por sí misma un modelo de IA

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto TypeScript
-  entorno y cuenta o despliegue indicado por la guía

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://trigger.dev/docs/quick-start)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Trigger.dev para mi objetivo y necesito pasos guiados. Lee https://trigger.dev/docs/quick-start. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta la tarea hello-world del README con un mensaje de prueba.

**Qué comprobar:** El panel muestra la ejecución y el mensaje en los logs.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Procesar en segundo plano un archivo subido por un usuario
- Reintentar una tarea de generación cuando falla el proveedor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Procesar en segundo plano un archivo subido por un usuario; Reintentar una tarea de generación cuando falla el proveedor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es infraestructura de tareas duraderas; no incluye por sí misma un modelo de IA

## Stack y modelos

- **Stack:** Proyecto TypeScript;  entorno y cuenta o despliegue indicado por la guía
- **Etiquetas:** `automation` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Windmill](windmill.md) | 18.6k | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. |
| [Kestra](kestra.md) | 30.2k | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. |

## Enlaces

- 🐙 GitHub: [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev)
- 🌐 Web: <https://trigger.dev/changelog>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/triggerdotdev/trigger.dev/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
