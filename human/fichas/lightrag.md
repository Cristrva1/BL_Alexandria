[🏠 Inicio](../README.md) › [🧬 Memoria, conocimiento y operación de IA](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📎 LightRAG

> RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.7k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Construye un grafo de entidades a partir de tus documentos y consulta en modo local, global o híbrido. Más barato que GraphRAG.

## Por qué destaca

Calidad de RAG con grafo a menor coste y con actualizaciones incrementales.

## Cómo funciona

Extrae entidades y relaciones con un LLM, las indexa en grafo y vectores, y recupera por ambos caminos.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/HKUDS/LightRAG/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LightRAG para mi objetivo y necesito pasos guiados. Lee https://github.com/HKUDS/LightRAG/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- RAG sobre documentación técnica
- Preguntas que cruzan varios documentos
- Alternativa barata a GraphRAG

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres RAG con grafo sin el coste de GraphRAG | no necesitas relaciones entre entidades; usa RAG vectorial con `llama-index` |

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |
| [RAGFlow](ragflow.md) | 94.2k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. |
| [PageIndex](pageindex.md) | 40.4k | Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos. |

## Enlaces

- 🐙 GitHub: [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)
- 🌐 Web: <https://arxiv.org/abs/2410.05779>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/HKUDS/LightRAG/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
