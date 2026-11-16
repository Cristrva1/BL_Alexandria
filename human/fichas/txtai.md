[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📚 txtai

> Framework de IA todo en uno para búsqueda semántica, RAG, pipelines con LLM, flujos y agentes sobre una base de embeddings propia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.4k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de código abierto (Apache-2.0) de NeuML, mantenido de forma continua desde 2020. Requiere Python 3.11 o superior.

## ¿Qué hace?

Ofrece búsqueda vectorial con SQL, almacenamiento de objetos, modelado de temas, análisis de grafos e indexación multimodal; pipelines con LLM para preguntas, etiquetado, transcripción, traducción y resumen; workflows que encadenan pipelines; agentes; y APIs web y MCP con bindings para JavaScript, Java, Rust y Go.

## ¿Cómo lo hace?

Construido en Python con Hugging Face Transformers, Sentence Transformers y FastAPI; se instala con `pip install txtai` y extras opcionales. Funciona en local o en contenedores, y documenta integración con llama.cpp, LiteLLM y generadores propios.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Transformers](transformers.md) | txtai se construye sobre Hugging Face Transformers para embeddings y pipelines. | Se instala como dependencia; elige los modelos del Hub en la configuración. |
| [litellm](litellm.md) | Un notebook oficial muestra cómo integrar LiteLLM como backend de LLM en txtai. | Configura LiteLLM o las claves del proveedor; después usa la ruta de LiteLLM en el pipeline LLM. |
| [llama.cpp](llama-cpp.md) | txtai documenta llama.cpp como backend para ejecutar LLM locales en sus pipelines. | Descarga un modelo GGUF; después configura el pipeline LLM con llama.cpp. |
| [Claude Code](claude-code.md) | La API MCP de txtai permite exponer un índice a agentes de código como herramienta de búsqueda (combinación por arquitectura). | Arranca la API de txtai con MCP; después regístrala en Claude Code. |

**Notas:** Alternativas cercanas en el catálogo: llama-index, haystack.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v9.14.0 (2026-10-06) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/neuml/txtai/blob/master/README.md) · [2](https://neuml.github.io/txtai)</sub>

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
pip install txtai
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/neuml/txtai/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar txtai para mi objetivo y necesito pasos guiados. Lee https://github.com/neuml/txtai/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install txtai`, indexa unas frases y busca por significado..

**Qué comprobar:** La búsqueda devuelve las frases más parecidas aunque no compartan palabras..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- indexar documentos y hacer búsqueda semántica con SQL en local
- montar un RAG o un grafo de conocimiento sin desplegar varios servicios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: indexar documentos y hacer búsqueda semántica con SQL en local; montar un RAG o un grafo de conocimiento sin desplegar varios servicios | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml, setup.py
- **Etiquetas:** `rag` `python` `library` `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [neuml/txtai](https://github.com/neuml/txtai)
- 🌐 Web: <https://neuml.github.io/txtai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/neuml/txtai/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
