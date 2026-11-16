[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 Haystack

> Framework de deepset para pipelines de RAG y agentes listos para producción.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

Framework de orquestación de IA de código abierto (Apache 2.0) de deepset para aplicaciones LLM en producción con Python. Maduro y activo (v3.5.0); deepset ofrece soporte y plataforma comerciales (Haystack Enterprise).

## ¿Qué hace?

Permite diseñar pipelines modulares y flujos de agentes con control explícito sobre recuperación, enrutamiento, memoria y generación: RAG escalable, aplicaciones multimodales, búsqueda semántica, preguntas y respuestas. Los agentes tienen hooks de ciclo de vida para guardrails y métricas de pasos y tokens. Hayhooks despliega pipelines como API REST o servidores MCP.

## ¿Cómo lo hace?

Se instala con `pip install haystack-ai` (también hay imágenes Docker) y las integraciones van en `haystack-core-integrations`. Recoge telemetría anónima de uso de componentes por defecto; se puede desactivar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Qdrant](qdrant.md) | Document store con integración oficial. | Qdrant primero; luego `qdrant-haystack`. |
| [Docling](docling.md) | Conversión de documentos complejos con la integración oficial de Docling. | Añade el convertidor de Docling al pipeline de indexación. |
| [Ollama](ollama.md) | Generadores con modelos locales (`OllamaChatGenerator`). | Ollama con el modelo descargado primero. |
| [langfuse](langfuse.md) | Trazas con la integración oficial de Langfuse. | Añade el componente tracer de Langfuse. |

**Notas:** Alternativas (elige una): llama-index, langchain. Desactiva la telemetría si tu política lo exige.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v3.5.0 (2026-11-10) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/deepset-ai/haystack/blob/main/README.md) · [2](https://qdrant.tech/documentation/frameworks/haystack/) · [3](https://haystack.deepset.ai/integrations/docling) · [4](https://docs.haystack.deepset.ai/docs/ollamachatgenerator) · [5](https://langfuse.com/integrations/frameworks/haystack)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La biblioteca admite modelos locales y remotos; deepset gestionado, almacenamiento y modelos son costes separados |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. El MCP se publica mediante el proyecto compañero Hayhooks y requiere configurar y servir pipelines; sus modelos y claves se eligen aparte |
| Coste | El coste depende del proveedor o la ruta. La biblioteca admite modelos locales y remotos; deepset gestionado, almacenamiento y modelos son costes separados |
| Equipo | Preparación según la ruta elegida. Python; documentos; componentes de recuperación y generación |

El MCP se publica mediante el proyecto compañero Hayhooks y requiere configurar y servir pipelines; sus modelos y claves se eligen aparte

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- documentos
- componentes de recuperación y generación

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
pip install haystack-ai
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/deepset-ai/haystack/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Haystack para mi objetivo y necesito pasos guiados. Lee https://github.com/deepset-ai/haystack/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Recupera un párrafo de un manual antes de generar la respuesta.

**Qué comprobar:** Puedes inspeccionar el párrafo y contrastar la salida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Responder sobre manuales propios
- Comparar recuperación de dos consultas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Responder sobre manuales propios; Comparar recuperación de dos consultas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP se publica mediante el proyecto compañero Hayhooks y requiere configurar y servir pipelines; sus modelos y claves se eligen aparte

## Stack y modelos

- **Stack:** Python; documentos; componentes de recuperación y generación
- **Etiquetas:** `rag` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |

## Enlaces

- 🐙 GitHub: [deepset-ai/haystack](https://github.com/deepset-ai/haystack)
- 🌐 Web: <https://haystack.deepset.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/deepset-ai/haystack/blob/main/README.md)
- [Fuente 2](https://github.com/deepset-ai/hayhooks/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
