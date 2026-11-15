[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Entender código y comprobar su calidad

Índices de código, análisis, calidad, benchmarks y herramientas de desarrollo. Empieza por comprender el proyecto y después elige qué comprobaciones necesitas.

15 repos · 3 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Repomix](../fichas/repomix.md) | Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. | Sin API de IA en la ruta básica |
| [Semgrep](../fichas/semgrep.md) | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. | Sin API de IA en la ruta básica |
| [GitHub CLI](../fichas/cli.md) | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. | Sin API de IA en la ruta básica |

## Secciones

- [Entender y empaquetar código para agentes](#entender-y-empaquetar-código-para-agentes) — 8 repos
- [Calidad, seguridad y benchmarks de código](#calidad-seguridad-y-benchmarks-de-código) — 5 repos
- [CLIs y SDKs de desarrollo](#clis-y-sdks-de-desarrollo) — 2 repos

## Entender y empaquetar código para agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Repomix](../fichas/repomix.md) | Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. | quieres dar tu repo completo a un LLM | Sin API de IA en la ruta básica |
| [graphify](../fichas/graphify.md) | Generador de grafos de conocimiento que mapea código, PDFs, imágenes y video en diagramas interactivos. | quieres ver conexiones visualmente o auditar un sistema | API de IA opcional |
| [codegraph](../fichas/codegraph.md) | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. | trabajas repos grandes y el contexto del agente es caro | Sin API de IA en la ruta básica |
| [codebase-memory-mcp](../fichas/codebase-memory-mcp.md) | Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes. | tu agente trabaja en repos grandes | Sin API de IA en la ruta básica |
| [GitNexus](../fichas/gitnexus.md) | Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. | quieres entender un repo puntual de forma visual | Sin API de IA en la ruta básica |
| [tree-sitter](../fichas/tree-sitter.md) | Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código. | construyes herramientas que entienden código | Sin API de IA en la ruta básica |
| [DeepWiki Open](../fichas/deepwiki-open.md) | Generador de wikis con IA para repos de GitHub, GitLab o Bitbucket, versión abierta de DeepWiki. | quieres documentación automática de un repositorio | Depende de la ruta elegida |
| [floorplan](../fichas/floorplan.md) | Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto. | buscas esta función: Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto. | Sin API de IA en la ruta básica |

## Calidad, seguridad y benchmarks de código

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Semgrep](../fichas/semgrep.md) | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. | quieres análisis de seguridad en CI | Sin API de IA en la ruta básica |
| [ast-grep](../fichas/ast-grep.md) | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. | necesitas buscar o reescribir código por estructura | Sin API de IA en la ruta básica |
| [Defending Code Reference Harness](../fichas/defending-code-reference-harness.md) | Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilidades. | quieres un flujo de seguridad con agentes probado | Sin API de IA en la ruta básica |
| [SWE-bench](../fichas/swe-bench.md) | Benchmark para evaluar si los modelos resuelven issues reales de GitHub. | necesitas medir agentes de código con un estándar | Sin API de IA en la ruta básica |
| [dsh-qa](../fichas/dsh-qa.md) | Plugin de DeepSeek Harness para explorar aplicaciones, guardar evidencia y preparar recorridos de pruebas reproducibles. | buscas esta función: Plugin de DeepSeek Harness para explorar aplicaciones, guardar evidencia y preparar recorridos de pruebas reproducibles. | Sin API de IA en la ruta básica |

## CLIs y SDKs de desarrollo

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [GitHub CLI](../fichas/cli.md) | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. | trabajas con GitHub desde la terminal o con agentes | Sin API de IA en la ruta básica |
| [openai-python](../fichas/openai-python.md) | SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API. | usas modelos de OpenAI desde Python y quieres el cliente oficial | API de IA necesaria |

## Recetas relacionadas

- [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md) — Que un agente de código entienda una base de código enorme sin gastar todo su contexto.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
