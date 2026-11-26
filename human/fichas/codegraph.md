[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 📊 codegraph

> CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 77.6k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

CodeGraph, CLI que indexa el código en local para dar contexto semántico a asistentes de IA, de @colbymchenry. Licencia MIT. Es muy popular (~78k estrellas, v1.6.2) y prepara una plataforma alojada.

## ¿Qué hace?

Construye un grafo del código (símbolos, llamadas, rutas de frameworks, puentes iOS/React Native) para que el agente obtenga contexto preciso con menos lecturas. Se sirve como MCP (`codegraph serve --mcp`) y mantiene el índice sincronizado mientras editas. El README incluye benchmarks propios con Claude.

## ¿Cómo lo hace?

Se instala con `npm i -g @colbymchenry/codegraph`; el instalador detecta y configura Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Copilot y otros. El núcleo está en Rust y el índice vive en `.codegraph/`. Recoge estadísticas de uso anónimas (sin código ni rutas), desactivables según la sección de telemetría.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Configuración automática del MCP en Claude Code. | Instala CodeGraph y ejecuta el instalador. |
| [Codex CLI](codex.md) | Configuración automática en Codex CLI. | Ejecuta el instalador con Codex presente. |
| [headroom](headroom.md) | Combinar contexto preciso con compresión del resto. (combinación por arquitectura) | Indexa con CodeGraph y envuelve el agente con Headroom. |
| [floorplan](floorplan.md) | Combinación recíproca: floorplan lo enlaza como «Combinar el mapa visual con un índice semántico para el agente. (combinación por arquitectura)». | Orden indicado desde floorplan: Usa Floorplan para entender y CodeGraph para navegar. |

**Notas:** Alternativas (elige una): codebase-memory-mcp, serena, gitnexus, graphify. Telemetría anónima activada.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.6.2 (2026-10-03) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/colbymchenry/codegraph/blob/main/README.md) · [2](https://colbymchenry.github.io/codegraph/)</sub>

## Ver similares

Grupo **Mapas e índices de código para agentes**: codegraph ocupa la posición 2 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [graphify](graphify.md) ⭐ recomendado | 74 | Si quieres convertir carpetas de código y documentos en un grafo navegable. |
| 2 | **codegraph** (esta ficha) | 66 | Si quieres un grafo de código local para que el agente navegue símbolos y dependencias. |
| 3 | [codebase-memory-mcp](codebase-memory-mcp.md) | 58 | Si quieres un índice persistente del código servido por MCP con poco consumo de tokens. |
| 4 | [Repomix](repomix.md) | 53 | Si quieres empaquetar un repo entero en un archivo para pegarlo en un modelo. |
| 5 | [GitNexus](gitnexus.md) | 51 | Si quieres un grafo de conocimiento del código consultable por agentes vía MCP. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El índice básico es local sin API; embeddings opcionales y el agente pueden consumir recursos o servicios según configuración |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración documentada por el proyecto |
| Modelos locales | Modelos locales documentados. La compatibilidad con los tres clientes está documentada; comprueba indexación y sincronización antes de confiar en el mapa |
| Coste | El coste depende del proveedor o la ruta. El índice básico es local sin API; embeddings opcionales y el agente pueden consumir recursos o servicios según configuración |
| Equipo | Preparación según la ruta elegida. Instalador oficial o Node y npm; repositorio de prueba |

La compatibilidad con los tres clientes está documentada; comprueba indexación y sincronización antes de confiar en el mapa

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador oficial o Node y npm
- repositorio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm i -g @colbymchenry/codegraph
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/colbymchenry/codegraph/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar codegraph para mi objetivo y necesito pasos guiados. Lee https://github.com/colbymchenry/codegraph/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Indexa una carpeta y consulta quién llama a una función conocida.

**Qué comprobar:** Los resultados identifican definiciones y relaciones comprobables.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una refactorización
- Encontrar rutas de ejecución de un proyecto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una refactorización; Encontrar rutas de ejecución de un proyecto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La compatibilidad con los tres clientes está documentada; comprueba indexación y sincronización antes de confiar en el mapa

## Stack y modelos

- **Stack:** Instalador oficial o Node y npm; repositorio de prueba
- **Etiquetas:** `code` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [codebase-memory-mcp](codebase-memory-mcp.md) | 48.6k | Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes. |
| [Serena](serena.md) | 31.4k | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. |
| [GitNexus](gitnexus.md) | 48.5k | Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. |
| [graphify](graphify.md) | 148k | CLI y skill que convierten código y documentos en un grafo consultable; el código se analiza localmente con AST y la extracción semántica tiene rutas separadas. |

## Enlaces

- 🐙 GitHub: [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)
- 🌐 Web: <https://colbymchenry.github.io/codegraph/>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/colbymchenry/codegraph/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
