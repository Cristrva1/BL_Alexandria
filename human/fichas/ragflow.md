[🏠 Inicio](../README.md) › [🧬 Memoria, conocimiento y operación de IA](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

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
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Procesa PDFs, tablas e imágenes con parsing visual, crea bases de conocimiento con citas trazables y añade agentes y workflows.

## Por qué destaca

Su parsing de documentos complejos es de los mejores en RAG open source.

## Cómo funciona

Un parser de layout (DeepDoc) divide documentos en fragmentos con estructura; búsqueda híbrida y reranking alimentan al LLM.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/infiniflow/ragflow/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar RAGFlow para mi objetivo y necesito pasos guiados. Lee https://github.com/infiniflow/ragflow/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Base de conocimiento con citas
- RAG sobre contratos y reportes
- Asistente interno con documentos complejos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tus documentos son complejos y necesitas citas fiables | quieres algo ligero en un portátil; mira `anything-llm` |

**Limitaciones:** Consume bastantes recursos (16 GB de RAM recomendados).

## Stack y modelos

- **Stack:** Go, Python, React, Elasticsearch, Docker
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

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/infiniflow/ragflow/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
