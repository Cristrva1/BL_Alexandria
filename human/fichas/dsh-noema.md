[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 📚 dsh-noema

> Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 144 | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 47/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plugin de código abierto (MIT) de ZSeven-W que añade memoria a largo plazo a DeepSeek Harness usando Noema, un sistema de memoria local sin vectores. Proyecto pequeño y reciente, probado con DSH 0.2.0-rc.2 y publicado en npm sin releases en GitHub.

## ¿Qué hace?

Carga contexto relevante al inicio de cada sesión (`noema_recall`) y ofrece búsqueda, navegación y catálogo de memorias. Importa los archivos de memoria de otras diez herramientas (Codex, Claude Code, opencode, Cursor, Grok, WorkBuddy, Antigravity, Trae, Qoder, Hermes) y los guarda como memorias duraderas. Incluye una página de ajustes para gestionar memorias y servidor, y un bucle que reinicia el servidor MCP si falla.

## ¿Cómo lo hace?

Las memorias son archivos Markdown inspeccionables en `NOEMA_ROOT` (por defecto `~/.agent-memory/`), servidos por el proceso hijo `noema-mcp`. La extracción de entidades combina segmentación jieba con señales de nombres propios y términos técnicos. Se instala con `dsh plugin --profile web add @zseven-w/dsh-noema@latest` y se recarga en caliente mediante Cordis HMR.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | `noema_import` lee sus archivos de memoria para migrarlos. | Instala el plugin en DSH y después ejecuta la importación. |
| [Codex CLI](codex.md) | Fuente de importación soportada. | Igual que arriba. |
| [hermes-agent](hermes-agent.md) | Fuente de importación soportada. | Igual que arriba. |
| [DeepSeek Harness (DSH)](deepseek-harness.md) | Es un plugin para DeepSeek Harness: el anfitrión que carga Noema como memoria persistente. | Instala y arranca DSH antes de añadir el plugin. |

**Notas:** Requiere DeepSeek Harness (deepseek-harness).

Estado en GitHub: activo · último push 2026-10-06 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ZSeven-W/dsh-noema/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La memoria básica no necesita API propia; el agente anfitrión mantiene sus costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Importar archivos de memoria de Claude, Codex o Antigravity no es una integración para ejecutar este plugin dentro de esos clientes |
| Coste | Consumo del agente que ya utilizas. La memoria básica no necesita API propia; el agente anfitrión mantiene sus costes |
| Equipo | Preparación según la ruta elegida. DeepSeek Harness compatible; plugin Noema; directorio de prueba |

Importar archivos de memoria de Claude, Codex o Antigravity no es una integración para ejecutar este plugin dentro de esos clientes

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- DeepSeek Harness compatible
- plugin Noema
- directorio de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ZSeven-W/dsh-noema/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dsh-noema para mi objetivo y necesito pasos guiados. Lee https://github.com/ZSeven-W/dsh-noema/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Guarda un recuerdo ficticio desde DSH y comprueba que puedes verlo y eliminarlo desde ajustes.

**Qué comprobar:** El recuerdo persiste y el panel muestra su contenido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Dar memoria a DeepSeek Harness
- Importar una nota propia de otro agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Dar memoria a DeepSeek Harness; Importar una nota propia de otro agente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Importar archivos de memoria de Claude, Codex o Antigravity no es una integración para ejecutar este plugin dentro de esos clientes

## Stack y modelos

- **Stack:** DeepSeek Harness compatible; plugin Noema; directorio de prueba
- **Etiquetas:** `memoria` `plugin` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ZSeven-W/dsh-noema](https://github.com/ZSeven-W/dsh-noema)
- 🌐 Web: <op.zseven.tech>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ZSeven-W/dsh-noema/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
