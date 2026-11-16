[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Entender código y comprobar su calidad

Índices de código, análisis, calidad, benchmarks y herramientas de desarrollo. Empieza por comprender el proyecto y después elige qué comprobaciones necesitas.

20 repos · 3 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Repomix](../fichas/repomix.md) | Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. | Sin clave propia de API de IA en la ruta básica |
| [ast-grep](../fichas/ast-grep.md) | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. | Sin clave propia de API de IA en la ruta básica |
| [GitHub CLI](../fichas/cli.md) | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Entender y empaquetar código para agentes](#entender-y-empaquetar-código-para-agentes) — 7 repos
- [Calidad, seguridad y benchmarks de código](#calidad-seguridad-y-benchmarks-de-código) — 8 repos
- [CLIs y SDKs de desarrollo](#clis-y-sdks-de-desarrollo) — 5 repos

## Entender y empaquetar código para agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Repomix](../fichas/repomix.md) | Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. | Tu objetivo encaja con estos ejemplos: Preparar contexto de código para una consulta; Compartir una muestra reproducible de un proyecto | Sin clave propia de API de IA en la ruta básica |
| [graphify](../fichas/graphify.md) | CLI y skill que convierten código y documentos en un grafo consultable; el código se analiza localmente con AST y la extracción semántica tiene rutas separadas. | Tu objetivo encaja con estos ejemplos: Explorar impacto de un cambio; Relacionar documentación y estructura de código | API de IA opcional |
| [codegraph](../fichas/codegraph.md) | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. | Tu objetivo encaja con estos ejemplos: Preparar una refactorización; Encontrar rutas de ejecución de un proyecto | API de IA opcional |
| [codebase-memory-mcp](../fichas/codebase-memory-mcp.md) | Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes. | Tu objetivo encaja con estos ejemplos: Navegar dependencias de código; Seleccionar pruebas afectadas por un cambio | API de IA opcional |
| [GitNexus](../fichas/gitnexus.md) | Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. | Tu objetivo encaja con estos ejemplos: Entender una base de código nueva; Inspeccionar el alcance de una refactorización | Sin clave propia de API de IA en la ruta básica |
| [tree-sitter](../fichas/tree-sitter.md) | Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código. | Tu objetivo encaja con estos ejemplos: Construir un analizador de código; Extraer símbolos para una herramienta de edición | Sin clave propia de API de IA en la ruta básica |
| [floorplan](../fichas/floorplan.md) | Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto. | Tu objetivo encaja con estos ejemplos: Explicar la arquitectura a alguien nuevo; Encontrar dónde se inicia una petición de la interfaz | Sin clave propia de API de IA en la ruta básica |

## Calidad, seguridad y benchmarks de código

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [ast-grep](../fichas/ast-grep.md) | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. | Tu objetivo encaja con estos ejemplos: Migrar llamadas de una API; Aplicar reglas de lint personalizadas | Sin clave propia de API de IA en la ruta básica |
| [Ruff](../fichas/ruff.md) | Linter y formateador de Python extremadamente rápido escrito en Rust, compatible con Flake8, isort y Black, con más de 800 reglas. | Tu objetivo encaja con estos ejemplos: sustituir Flake8, isort y Black por una sola herramienta en un proyecto; revisar y corregir el código que genera un agente antes de cada commit | Sin clave propia de API de IA en la ruta básica |
| [Gitleaks](../fichas/gitleaks.md) | Detector de secretos (contraseñas, claves de API, tokens) en repositorios git, archivos y stdin, usable como hook o acción de CI. | Tu objetivo encaja con estos ejemplos: revisar el historial de un repositorio antes de hacerlo público; bloquear commits que contengan claves con un hook pre-commit | Sin clave propia de API de IA en la ruta básica |
| [TruffleHog](../fichas/trufflehog.md) | Busca, clasifica, verifica y analiza credenciales filtradas en git, chats, wikis, logs, almacenes de objetos y sistemas de archivos. | Tu objetivo encaja con estos ejemplos: auditar los repositorios de una organización en busca de claves activas; revisar buckets o logs exportados antes de compartirlos | Sin clave propia de API de IA en la ruta básica |
| [Biome](../fichas/biome.md) | Formateador y linter en un solo binario para JavaScript, TypeScript, JSX, JSON, CSS, GraphQL y más, usable por CLI y LSP. | Tu objetivo encaja con estos ejemplos: sustituir ESLint y Prettier en un proyecto web por una sola herramienta; formatear y revisar el código que genera un agente antes de abrir un PR | Sin clave propia de API de IA en la ruta básica |
| [pre-commit](../fichas/pre-commit.md) | Framework para gestionar y ejecutar hooks de git multilenguaje antes de cada commit: linters, formateadores y escáneres declarados en YAML. | Tu objetivo encaja con estos ejemplos: obligar a pasar formato, lint y escaneo de secretos antes de cada commit; aplicar las mismas comprobaciones en local y en CI | Sin clave propia de API de IA en la ruta básica |
| [SonarQube Community Build](../fichas/sonarqube.md) | Plataforma de inspección continua de calidad y seguridad del código: análisis estático de bugs, vulnerabilidades y mantenibilidad en muchos lenguajes. | Tu objetivo encaja con estos ejemplos: vigilar la calidad y seguridad de un repositorio en cada PR; revisar el código generado por IA con reglas consistentes antes de fusionarlo | Sin clave propia de API de IA en la ruta básica |
| [SWE-bench](../fichas/swe-bench.md) | Benchmark para evaluar si los modelos resuelven issues reales de GitHub. | Tu objetivo encaja con estos ejemplos: Comparar soluciones a issues reproducibles; Estudiar evaluación de agentes de programación | API de IA opcional |

## CLIs y SDKs de desarrollo

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [GitHub CLI](../fichas/cli.md) | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. | Tu objetivo encaja con estos ejemplos: Consultar issues desde terminal; Revisar ejecuciones de Actions | Sin clave propia de API de IA en la ruta básica |
| [fzf](../fichas/fzf.md) | Buscador difuso de línea de comandos y kit de interfaces de terminal para seleccionar archivos, historial o cualquier lista de forma interactiva. | Tu objetivo encaja con estos ejemplos: buscar archivos y comandos del historial al instante en la terminal; construir menús interactivos en scripts de shell | Sin clave propia de API de IA en la ruta básica |
| [lazygit](../fichas/lazygit.md) | Interfaz de terminal sencilla para git: preparar fragmentos o líneas, rebase interactivo, cherry-pick y gestión de ramas con atajos. | Tu objetivo encaja con estos ejemplos: revisar y preparar por partes los cambios que hizo un agente antes de confirmarlos; hacer rebases interactivos y deshacer operaciones sin recordar comandos | Sin clave propia de API de IA en la ruta básica |
| [ripgrep](../fichas/ripgrep.md) | Búsqueda recursiva de texto por expresiones regulares muy rápida que respeta .gitignore y omite archivos ocultos y binarios. | Tu objetivo encaja con estos ejemplos: localizar todas las apariciones de una función en un repositorio grande; buscar texto en miles de archivos de logs o notas en segundos | Sin clave propia de API de IA en la ruta básica |
| [openai-python](../fichas/openai-python.md) | SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API. | Tu objetivo encaja con estos ejemplos: Integrar respuestas de IA en una app Python; Procesar audio o imágenes desde código | API de IA necesaria |

## Recetas relacionadas

- [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md) — Que un agente de código entienda una base de código enorme sin gastar todo su contexto.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
