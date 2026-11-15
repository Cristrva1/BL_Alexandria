[🏠 Inicio](../README.md) › [🧬 Memoria, conocimiento y operación de IA](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📎 PageIndex

> Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.4k | MIT | Python | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. El proyecto documenta usar Claude Code con una suscripción o una API key. La modalidad cloud de PageIndex tiene requisitos propios. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El README documenta una integración con las sesiones de los agentes indicados. Configurar esa ruta y comprobar sus límites; otras rutas pueden facturar por API.

## Qué puedes hacer con él

Genera un árbol tipo índice del documento y deja que el LLM navegue por él como un experto. Funciona bien con informes largos y estructurados.

## Por qué destaca

Evita los problemas de fragmentación de los embeddings en documentos largos.

## Cómo funciona

Construye una jerarquía de secciones con resúmenes y el modelo decide qué ramas leer para responder.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/VectifyAI/PageIndex/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PageIndex para mi objetivo y necesito pasos guiados. Lee https://github.com/VectifyAI/PageIndex/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Preguntas sobre informes financieros
- Navegar manuales largos
- RAG sin base vectorial

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tus documentos son largos y con estructura clara | tienes miles de documentos cortos; usa búsqueda vectorial |

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `rag` `docs` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Docling](docling.md) | 70.6k | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LightRAG](lightrag.md) | 40.7k | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. |

## Enlaces

- 🐙 GitHub: [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)
- 🌐 Web: <https://pageindex.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/VectifyAI/PageIndex/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
