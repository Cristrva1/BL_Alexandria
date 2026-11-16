[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 LlamaIndex

> Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 52.9k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Framework de código abierto (MIT) de LlamaIndex (run-llama) para aplicaciones RAG y agentes sobre datos propios. Activo (v0.14.26), pero el README avisa de que la empresa ha desplazado su foco principal a LlamaParse, su plataforma comercial de parsing, y a LiteParse; el framework sigue disponible como kit abierto.

## ¿Qué hace?

Conecta LLM con documentos y datos: ingesta, indexación, recuperación, motores de consulta y agentes. Tiene más de 300 paquetes de integración para LLM, embeddings y almacenes vectoriales.

## ¿Cómo lo hace?

Python. Se instala como `llama-index` (núcleo más una selección de integraciones) o como `llama-index-core` más integraciones sueltas (por ejemplo `llama-index-llms-ollama` o `llama-index-embeddings-huggingface`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Qdrant](qdrant.md) | Almacén vectorial con integración oficial. | Qdrant primero; luego `llama-index-vector-stores-qdrant`. |
| [Docling](docling.md) | Lector de documentos complejos con integración oficial de Docling. | Instala el lector de Docling para LlamaIndex antes de indexar PDF complejos. |
| [Ragas](ragas.md) | Evaluar la calidad del RAG (integración documentada por Ragas). | Evalúa tras construir el pipeline. |
| [Ollama](ollama.md) | Modelos locales (`llama-index-llms-ollama`, citado en el README). | Ollama con el modelo descargado primero. |

**Notas:** Alternativas (elige una): haystack, langchain. Ten en cuenta el cambio de foco de la empresa al planificar proyectos largos.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v0.14.26 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/run-llama/llama_index/blob/main/README.md) · [2](https://qdrant.tech/documentation/frameworks/llama-index/) · [3](https://docling-project.github.io/docling/integrations/llamaindex/) · [4](https://docs.ragas.io/en/stable/howtos/integrations/_llamaindex/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. OpenAI consume API; Ollama y embeddings locales evitan esa API; LlamaParse se presupuesta aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Configura también embeddings locales si quieres que todo el procesamiento sea local |
| Coste | El coste depende del proveedor o la ruta. OpenAI consume API; Ollama y embeddings locales evitan esa API; LlamaParse se presupuesta aparte |
| Equipo | Preparación según la ruta elegida. Python; dos documentos; modelo generativo y embeddings |

Configura también embeddings locales si quieres que todo el procesamiento sea local

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- dos documentos
- modelo generativo y embeddings

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
# custom selection of integrations to work with core
pip install llama-index-core
pip install llama-index-llms-openai
pip install llama-index-llms-ollama
pip install llama-index-embeddings-huggingface
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/run-llama/llama_index/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LlamaIndex para mi objetivo y necesito pasos guiados. Lee https://github.com/run-llama/llama_index/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pregunta por una cifra que solo aparece en uno de tus dos documentos.

**Qué comprobar:** Se recupera el documento correcto y puedes contrastar el fragmento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar políticas internas
- Encontrar cláusulas en contratos ficticios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar políticas internas; Encontrar cláusulas en contratos ficticios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Configura también embeddings locales si quieres que todo el procesamiento sea local

## Stack y modelos

- **Stack:** Python; dos documentos; modelo generativo y embeddings
- **Etiquetas:** `rag` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Haystack](haystack.md) | 27k | Framework de deepset para pipelines de RAG y agentes listos para producción. |
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |

## Enlaces

- 🐙 GitHub: [run-llama/llama_index](https://github.com/run-llama/llama_index)
- 🌐 Web: <https://developers.llamaindex.ai>
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/run-llama/llama_index/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
