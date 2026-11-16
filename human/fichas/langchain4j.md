[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks en TypeScript y multi-lenguaje

# 🕸️ langchain4j

> Biblioteca de Java para integrar LLM, herramientas, agentes, RAG y almacenes vectoriales en aplicaciones de la JVM.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.4k | Apache-2.0 | Java | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

Biblioteca open source (Apache-2.0) para integrar LLMs en aplicaciones Java y de la JVM. Pese al nombre, es un proyecto independiente de LangChain Inc. Es madura y activa (1.23.0) y se publica en Maven Central.

## ¿Qué hace?

Ofrece APIs unificadas para más de 20 proveedores de LLM y más de 30 almacenes de embeddings, así que se puede cambiar de uno a otro sin reescribir código. Incluye un toolbox que va de plantillas de prompt, memoria de chat y function calling a patrones de alto nivel como agentes y RAG. Aporta 'AI Services' declarativos con interfaces y anotaciones, y soporte de MCP.

## ¿Cómo lo hace?

Dependencias Maven o Gradle (`dev.langchain4j:*`), un módulo por proveedor o almacén. Tiene integraciones de primera clase con Quarkus (quarkus-langchain4j), Spring Boot y Helidon. Requiere un JDK moderno; la versión mínima concreta está en la documentación [DATO NO VERIFICADO: no figura en el README].

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Modelos locales mediante el módulo oficial de Ollama. | Instala Ollama y descarga el modelo; añade `langchain4j-ollama`. |
| [Qdrant](qdrant.md) | Almacén vectorial para RAG mediante el módulo oficial. | Despliega Qdrant y añade `langchain4j-qdrant`. |
| [pgvector](pgvector.md) | Embeddings en PostgreSQL mediante el módulo oficial de pgvector. | Habilita la extensión en Postgres y añade `langchain4j-pgvector`. |
| [Milvus](milvus.md) | Almacén vectorial alternativo para volúmenes grandes (módulo oficial). | Elige uno de los almacenes vectoriales; despliega Milvus y añade su módulo. |

**Notas:** Sin alternativas declaradas en el catálogo (spring-ai no figura). Qdrant, pgvector y milvus son alternativas entre sí: elige uno.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 1.23.0 (2026-10-28) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/langchain4j/langchain4j/blob/main/README.md) · [2](https://docs.langchain4j.dev/integrations/language-models/ollama) · [3](https://docs.langchain4j.dev/integrations/embedding-stores/qdrant) · [4](https://docs.langchain4j.dev/integrations/embedding-stores/pgvector) · [5](https://docs.langchain4j.dev/integrations/embedding-stores/milvus) · [6](https://docs.langchain4j.dev/tutorials/mcp)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Ofrece Ollama local y proveedores remotos; recursos, almacenamiento y APIs se pagan según la ruta |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es una biblioteca Java independiente; no es un port con las mismas versiones o API que LangChain Python |
| Coste | El coste depende del proveedor o la ruta. Ofrece Ollama local y proveedores remotos; recursos, almacenamiento y APIs se pagan según la ruta |
| Equipo | Preparación según la ruta elegida. JDK y Maven o Gradle según la integración; modelo |

Es una biblioteca Java independiente; no es un port con las mismas versiones o API que LangChain Python

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- JDK y Maven o Gradle según la integración
- modelo

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.langchain4j.dev/get-started)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar langchain4j para mi objetivo y necesito pasos guiados. Lee https://docs.langchain4j.dev/get-started. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Integra un chat que consulta un objeto de inventario de prueba en Java.

**Qué comprobar:** El resultado devuelve el dato del objeto y puede validarse con un test.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Añadir IA a Spring Boot
- Recuperar documentos desde una aplicación JVM

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Añadir IA a Spring Boot; Recuperar documentos desde una aplicación JVM | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una biblioteca Java independiente; no es un port con las mismas versiones o API que LangChain Python

## Stack y modelos

- **Stack:** JDK y Maven o Gradle según la integración; modelo
- **Etiquetas:** `ts` `anthropic` `chatgpt` `chroma` `embeddings` `gemini` `gpt` `huggingface`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j)
- 🌐 Web: <https://docs.langchain4j.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langchain4j/langchain4j/blob/main/README.md)
- [Fuente 2](https://docs.langchain4j.dev/integrations/language-models/ollama/)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
