[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 📚 CAMEL

> Framework multiagente de investigación para generar datos sintéticos, automatizar tareas y simular sociedades de agentes con muchos proveedores.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework multiagente de código abierto (Apache-2.0) de la comunidad CAMEL-AI, nacido del artículo «CAMEL: Communicative Agents» (2023). Orientado a investigación sobre las leyes de escala de los agentes; desarrollo activo.

## ¿Qué hace?

Ofrece agentes conversacionales con roles, sociedades de agentes, generación de datos sintéticos, automatización de tareas con herramientas y simulación de mundos. Incluye toolkits (búsqueda, navegador, código, MCP), memorias y lectores de datos, con ejemplos y cookbooks.

## ¿Cómo lo hace?

Se instala con `pip install camel-ai` (extras como `camel-ai[web_tools]`); los modelos se eligen por plataforma (OpenAI, Anthropic, Ollama, vLLM, entre otros). Admite almacenes vectoriales como Qdrant y cookbooks con Firecrawl para ingestar webs.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | CAMEL soporta Ollama como plataforma de modelos para ejecutar agentes con modelos locales. | Ollama con un modelo descargado; después crea el modelo con la plataforma Ollama en CAMEL. |
| [Qdrant](qdrant.md) | CAMEL incluye almacenamiento vectorial en Qdrant para la memoria y la recuperación de los agentes. | Qdrant en marcha; después configura el almacenamiento Qdrant en CAMEL. |
| [firecrawl](firecrawl.md) | Un cookbook oficial de CAMEL muestra tres formas de ingestar webs con Firecrawl. | Clave o instancia de Firecrawl; después usa el lector de Firecrawl de CAMEL. |
| [vLLM](vllm.md) | CAMEL admite vLLM como plataforma de modelos para servir modelos abiertos con API compatible con OpenAI. | vLLM sirviendo el modelo; después apunta CAMEL a su endpoint. |

**Notas:** Alternativas cercanas en el catálogo: crewai, ag2, agentscope.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada v0.2.90 (2026-03-22) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/camel-ai/camel/blob/master/README.md) · [2](https://docs.camel-ai.org/cookbooks/data_processing/ingest_data_from_websites_with_Firecrawl)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
pip install camel-ai
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/camel-ai/camel/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar CAMEL para mi objetivo y necesito pasos guiados. Lee https://github.com/camel-ai/camel/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install camel-ai`, configura la clave de un modelo y ejecuta el ejemplo de ChatAgent..

**Qué comprobar:** El agente responde y el script termina sin errores mostrando la conversación..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- generar datos sintéticos con agentes que dialogan en roles
- montar un experimento de simulación con muchos agentes y medir su comportamiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: generar datos sintéticos con agentes que dialogan en roles; montar un experimento de simulación con muchos agentes y medir su comportamiento | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `agents` `python` `research` `framework`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [camel-ai/camel](https://github.com/camel-ai/camel)
- 🌐 Web: <https://docs.camel-ai.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/camel-ai/camel/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
