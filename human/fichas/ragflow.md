[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📎 RAGFlow

> Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 94.2k | Apache-2.0 | Go | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. LLM, embeddings y reranker se configuran por separado; modelos locales necesitan recursos adicionales; APIs remotas tienen consumo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Los mínimos del servidor no incluyen necesariamente ejecutar los modelos; prueba pocos documentos antes de ampliar |
| Coste | El coste depende del proveedor o la ruta. LLM, embeddings y reranker se configuran por separado; modelos locales necesitan recursos adicionales; APIs remotas tienen consumo |
| Equipo | Preparación según la ruta elegida. Docker; configuración inicial orientativa 4 CPU,16 GB RAM,50 GB disco; modelos |

Los mínimos del servidor no incluyen necesariamente ejecutar los modelos; prueba pocos documentos antes de ampliar

## Qué puedes hacer con él

Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable.

## Por qué destaca

Usos propuestos: Consultar manuales de una organización; Combinar documentos en una base de conocimiento.

## Cómo funciona

Los mínimos del servidor no incluyen necesariamente ejecutar los modelos; prueba pocos documentos antes de ampliar

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- configuración inicial orientativa 4 CPU,16 GB RAM,50 GB disco
- modelos

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/infiniflow/ragflow/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar RAGFlow para mi objetivo y necesito pasos guiados. Lee https://github.com/infiniflow/ragflow/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Indexa un PDF propio corto y pregunta por un dato identificable con cita.

**Qué comprobar:** La respuesta permite abrir el fragmento y comprobar su procedencia.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar manuales de una organización
- Combinar documentos en una base de conocimiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar manuales de una organización; Combinar documentos en una base de conocimiento | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los mínimos del servidor no incluyen necesariamente ejecutar los modelos; prueba pocos documentos antes de ampliar

## Stack y modelos

- **Stack:** Docker; configuración inicial orientativa 4 CPU,16 GB RAM,50 GB disco; modelos
- **Etiquetas:** `rag` `docs` `agents` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [Docling](docling.md) | 70.6k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [dify](dify.md) | 161k | Plataforma integral para construir apps de IA con backend y UI listos. |
| [LightRAG](lightrag.md) | 40.7k | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. |

## Enlaces

- 🐙 GitHub: [infiniflow/ragflow](https://github.com/infiniflow/ragflow)
- 🌐 Web: <https://ragflow.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/infiniflow/ragflow/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
