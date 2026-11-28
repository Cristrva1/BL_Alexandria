[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🕸️ graphify

> CLI y skill que convierten código y documentos en un grafo consultable; el código se analiza localmente con AST y la extracción semántica tiene rutas separadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 148k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Graphify, CLI y skill que convierte código y documentos en un grafo de conocimiento consultable, de Graphify Labs. Licencia Apache-2.0. Tiene un recuento de estrellas excepcionalmente alto (~149k), publica muy a menudo (v0.9.111) y ofrece un servicio de pago, Graphify Cloud.

## ¿Qué hace?

Con `/graphify` en el asistente mapea el proyecto (código, docs, PDF, imágenes y vídeos) en un grafo que el agente consulta en lugar de usar grep. El código se analiza en local con Tree-sitter sin LLM; los documentos y medios usan el modelo de tu asistente. Puede funcionar como servidor MCP y usar Ollama para inferencia local.

## ¿Cómo lo hace?

Se instala con `pip install graphifyy` o `uv tool install graphifyy` (paquete oficial con doble «y»; otros `graphify*` de PyPI no están afiliados), con extras como `[mcp]` u `[ollama]`. Luego `graphify install` configura los agentes. Requiere Python 3.10+ y declara no tener telemetría.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Skill e instalación con `graphify install` para Claude Code. | Instala graphifyy y ejecuta `graphify install`. |
| [tree-sitter](tree-sitter.md) | Analiza el código con Tree-sitter. | No requiere instalación aparte: viene en el paquete. |
| [Ollama](ollama.md) | Extra `[ollama]` para inferencia local. | Instala `graphifyy[ollama]` y arranca Ollama. |
| [graphrag](graphrag.md) | Llevar el análisis de grafos a corpus documentales grandes. (combinación por arquitectura) | Usa Graphify para el código y GraphRAG para la documentación. |

**Notas:** Alternativas (elige una): codegraph, serena, codebase-memory-mcp. Ojo con paquetes PyPI de nombre parecido.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.9.111 (2026-11-15) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Graphify-Labs/graphify/blob/v8/README.md)</sub>

## Ver similares

Grupo **Mapas e índices de código para agentes**: graphify ocupa la posición 1 de 4 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **graphify** (esta ficha) ⭐ recomendado | 74 | Si quieres convertir carpetas de código y documentos en un grafo navegable. |
| 2 | [codegraph](codegraph.md) | 66 | Si quieres un grafo de código local para que el agente navegue símbolos y dependencias. |
| 3 | [codebase-memory-mcp](codebase-memory-mcp.md) | 58 | Si quieres un índice persistente del código servido por MCP con poco consumo de tokens. |
| 4 | [Repomix](repomix.md) | 53 | Si quieres empaquetar un repo entero en un archivo para pegarlo en un modelo. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El código se analiza con AST sin LLM; documentos y medios usan el agente, API o backend local configurado |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelos locales documentados. El paquete es graphifyy; el soporte Antigravity es explícito; la extracción semántica y la de código no tienen los mismos costes |
| Coste | El coste depende del proveedor o la ruta. El código se analiza con AST sin LLM; documentos y medios usan el agente, API o backend local configurado |
| Equipo | Preparación según la ruta elegida. Python 3.10+; uv o pipx; carpeta de código |

El paquete es graphifyy; el soporte Antigravity es explícito; la extracción semántica y la de código no tienen los mismos costes

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10+
- uv o pipx
- carpeta de código

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # detects your assistant and registers the skill
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Graphify-Labs/graphify/blob/v8/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar graphify para mi objetivo y necesito pasos guiados. Lee https://github.com/Graphify-Labs/graphify/blob/v8/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Indexa primero solo código y consulta qué funciones dependen de un módulo.

**Qué comprobar:** Cada relación se puede contrastar con un archivo o símbolo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar impacto de un cambio
- Relacionar documentación y estructura de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar impacto de un cambio; Relacionar documentación y estructura de código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El paquete es graphifyy; el soporte Antigravity es explícito; la extracción semántica y la de código no tienen los mismos costes

## Stack y modelos

- **Stack:** Python 3.10+; uv o pipx; carpeta de código
- **Etiquetas:** `code` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [codegraph](codegraph.md) | 77.6k | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. |
| [Serena](serena.md) | 31.4k | Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. |
| [codebase-memory-mcp](codebase-memory-mcp.md) | 48.6k | Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes. |

## Enlaces

- 🐙 GitHub: [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)
- 🌐 Web: <https://www.graphify.com>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Graphify-Labs/graphify/blob/v8/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
