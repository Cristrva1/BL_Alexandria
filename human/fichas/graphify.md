[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🕸️ graphify

> Generador de grafos de conocimiento que mapea código, PDFs, imágenes y video en diagramas interactivos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 145k | Apache-2.0 | Python | 2026-11-09 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Qué es

Resuelve el onboarding visual: un índice textual no basta cuando hay relaciones entre archivos.

## Por qué destaca

Combina visualización navegable, reporte legible y datos exportables en un solo paso, ideal para auditorías y onboarding cuando un índice de texto no basta. Su soporte multi-fuente (código + documentos + multimedia) lo diferencia de los indexadores puramente de código.

## Cómo funciona

Analiza las fuentes del proyecto y produce un grafo con nodos y relaciones; opcionalmente usa un LLM (cloud o local) para enriquecer el análisis semántico y generar descripciones de cada nodo.

## Instalación rápida

`pipx install graphify` o `uv tool install graphify`, luego `/graphify .` sobre el proyecto. Requiere Python 3.10+; el enriquecimiento con LLM necesita claves de API.

## Casos de uso

- `/graphify .` para mapear llamadas de funciones
- Auditoría rápida de un sistema
- Onboarding visual de un proyecto heredado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres ver conexiones visualmente o auditar un sistema | solo necesitas índice textual barato (codegraph) o tu proyecto es trivial |

## Stack y modelos

- **Stack:** Python 3.10+, uv/pipx
- **Modelos / API:** Opcional (OpenAI/Anthropic o locales Llama/Mistral); agnóstico vía variables de entorno.
- **Etiquetas:** `code` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [codegraph](codegraph.md) | 77.3k | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. |
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |

## Enlaces

- 🐙 GitHub: [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)
- 🌐 Web: <https://www.graphify.com>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
