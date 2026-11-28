[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📚 agentic-rag-for-dummies

> Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta local basada en Ollama.

## Cuándo elegir esta ficha

RAGFlow ofrece la ruta de aplicación documental. La ficha de ejemplos merece conservarse al aprender la arquitectura de LangGraph y Ollama.

Referencia de consulta del catálogo.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/GiovanniPasq/agentic-rag-for-dummies/blob/c1b339b54f0927bd0b469fcce70f3cd5de4e918d/README.md) · [Fuente 2](https://api.github.com/repos/GiovanniPasq/agentic-rag-for-dummies) · [Fuente 3](https://github.com/GiovanniPasq/agentic-rag-for-dummies/commit/c1b339b54f0927bd0b469fcce70f3cd5de4e918d)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.4k | MIT | Jupyter Notebook | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 47/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto educativo de código abierto (MIT) de Giovanni Pasqualino que enseña a construir un sistema de RAG agéntico modular con LangGraph. Activo (v2.3.1), con cuaderno interactivo y proyecto ejecutable.

## ¿Qué hace?

Muestra paso a paso indexación jerárquica (busca en trozos pequeños y recupera el trozo padre), memoria de conversación, aclaración de consultas ambiguas con intervención humana, orquestación con agentes, descomposición map-reduce en subconsultas paralelas, autocorrección, compresión de contexto, observabilidad con Langfuse y evaluación con RAGAS.

## ¿Cómo lo hace?

Ofrece dos rutas: un cuaderno Jupyter para aprender y un proyecto modular donde se cambian proveedor de LLM, modelo de embeddings, conversor de PDF y flujo del agente. La app ejecutable usa Ollama por defecto (por ejemplo `granite4.1:8b`) y Qdrant como base vectorial, y puede adaptarse a cualquier proveedor de LangChain.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LangGraph](langgraph.md) | Orquesta todo el flujo de recuperación y razonamiento. | Se instala con las dependencias del proyecto. |
| [Ollama](ollama.md) | Proveedor por defecto de la app ejecutable. | Ollama con el modelo descargado antes de lanzar la app. |
| [Qdrant](qdrant.md) | Base vectorial del proyecto. | Sigue la configuración del repositorio (local o servidor) antes de indexar. |
| [langfuse](langfuse.md) | Observabilidad de llamadas, herramientas y grafo. | Opcional; configura las claves en el entorno. |
| [Ragas](ragas.md) | Evaluación de recuperación y respuestas. | Después de tener un corpus indexado. |

**Notas:** Es material de aprendizaje y referencia, no un producto para producción.

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v2.3.1 (2026-10-17) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/GiovanniPasq/agentic-rag-for-dummies/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La app es Ollama-first; Colab alojado no trae Ollama y requiere cambiar de modelo o conectar una instancia; las APIs alternativas consumen |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No confundas instalar langchain-openai con completar todo el proyecto; revisa requisitos y la guía de ejecución de la app o notebook |
| Coste | El coste depende del proveedor o la ruta. La app es Ollama-first; Colab alojado no trae Ollama y requiere cambiar de modelo o conectar una instancia; las APIs alternativas consumen |
| Equipo | Preparación según la ruta elegida. Python; checkout; Ollama local; PDFs propios; Jupyter para notebook |

No confundas instalar langchain-openai con completar todo el proyecto; revisa requisitos y la guía de ejecución de la app o notebook

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- checkout
- Ollama local
- PDFs propios
- Jupyter para notebook

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
pip install -r requirements.txt
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/GiovanniPasq/agentic-rag-for-dummies/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar agentic-rag-for-dummies para mi objetivo y necesito pasos guiados. Lee https://github.com/GiovanniPasq/agentic-rag-for-dummies/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Coloca un PDF breve en docs y pregunta por un dato de una página concreta.

**Qué comprobar:** Puedes ver documentos recuperados y aclarar una consulta ambigua.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender RAG por pasos
- Comparar un pipeline local con otro proveedor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender RAG por pasos; Comparar un pipeline local con otro proveedor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No confundas instalar langchain-openai con completar todo el proyecto; revisa requisitos y la guía de ejecución de la app o notebook

## Stack y modelos

- **Stack:** Python; checkout; Ollama local; PDFs propios; Jupyter para notebook
- **Etiquetas:** `rag` `template` `jupyter-notebook`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [GiovanniPasq/agentic-rag-for-dummies](https://github.com/GiovanniPasq/agentic-rag-for-dummies)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/GiovanniPasq/agentic-rag-for-dummies/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
