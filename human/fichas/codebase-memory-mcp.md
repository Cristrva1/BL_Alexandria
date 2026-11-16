[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧬 codebase-memory-mcp

> Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 48.6k | MIT | C | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

codebase-memory-mcp, motor local de inteligencia de código para agentes vía MCP, de DeusData. Licencia MIT. Es muy activo (~49k estrellas, v0.12.1).

## ¿Qué hace?

Conecta código, documentación, configuración e infraestructura en un grafo de conocimiento local persistente. Expone 17 herramientas MCP y ofrece resolución de tipos híbrida con LSP. Incluye un visor opcional (CBM Lens) y perfiles para agentes.

## ¿Cómo lo hace?

Es un binario nativo en C que se instala con un script (`install.sh` o `install.ps1`, que el README recomienda revisar antes), con Nix o compilando el código. `install` configura los clientes compatibles. Indexa y consulta en local sin telemetría.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Cliente MCP de programación. (combinación por arquitectura) | Instala el binario y ejecuta `install` para configurar el cliente. |
| [Repomix](repomix.md) | Empaquetar módulos concretos tras localizarlos en el grafo. (combinación por arquitectura) | Localiza con el grafo y empaqueta con Repomix. |
| [Codex CLI](codex.md) | Cliente MCP soportado: el README indica que comparte un daemon de coordinación entre Claude Code, Codex, OpenCode y otros clientes configurados. | Ejecuta `install` para configurar Codex como cliente. |

**Notas:** Alternativas (elige una): codegraph, gitnexus, serena, graphify. Revisa el script de instalación antes de ejecutarlo.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v0.12.1 (2026-10-16) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md)</sub>

## Ver similares

Grupo **Mapas e índices de código para agentes**: codebase-memory-mcp ocupa la posición 3 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [graphify](graphify.md) ⭐ recomendado | 75 | Si quieres convertir carpetas de código y documentos en un grafo navegable. |
| 2 | [codegraph](codegraph.md) | 67 | Si quieres un grafo de código local para que el agente navegue símbolos y dependencias. |
| 3 | **codebase-memory-mcp** (esta ficha) | 58 | Si quieres un índice persistente del código servido por MCP con poco consumo de tokens. |
| 4 | [Repomix](repomix.md) | 52 | Si quieres empaquetar un repo entero en un archivo para pegarlo en un modelo. |
| 5 | [GitNexus](gitnexus.md) | 51 | Si quieres un grafo de conocimiento del código consultable por agentes vía MCP. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La extracción y embeddings locales no requieren API; consultar un modelo u otros proveedores puede añadir consumo |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración documentada por el proyecto |
| Modelos locales | Modelos locales documentados. Las funciones de hooks y actividad varían por cliente; los binarios ya compilados no necesitan Node para ejecutar Lens |
| Coste | El coste depende del proveedor o la ruta. La extracción y embeddings locales no requieren API; consultar un modelo u otros proveedores puede añadir consumo |
| Equipo | Preparación según la ruta elegida. Binario para tu sistema; repositorio de prueba; Node 22+ solo para compilar CBM Lens |

Las funciones de hooks y actividad varían por cliente; los binarios ya compilados no necesitan Node para ejecutar Lens

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario para tu sistema
- repositorio de prueba
- Node 22+ solo para compilar CBM Lens

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar codebase-memory-mcp para mi objetivo y necesito pasos guiados. Lee https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Indexa un proyecto pequeño y consulta el impacto de cambiar una función.

**Qué comprobar:** Puedes abrir las referencias y relaciones del grafo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Navegar dependencias de código
- Seleccionar pruebas afectadas por un cambio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Navegar dependencias de código; Seleccionar pruebas afectadas por un cambio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las funciones de hooks y actividad varían por cliente; los binarios ya compilados no necesitan Node para ejecutar Lens

## Stack y modelos

- **Stack:** Binario para tu sistema; repositorio de prueba; Node 22+ solo para compilar CBM Lens
- **Etiquetas:** `code` `mcp` `memory`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [codegraph](codegraph.md) | 77.6k | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. |
| [GitNexus](gitnexus.md) | 48.5k | Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. |
| [Serena](serena.md) | 31.4k | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. |
| [graphify](graphify.md) | 148k | CLI y skill que convierten código y documentos en un grafo consultable; el código se analiza localmente con AST y la extracción semántica tiene rutas separadas. |

## Enlaces

- 🐙 GitHub: [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)
- 🌐 Web: <https://deusdata.github.io/codebase-memory-mcp/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
