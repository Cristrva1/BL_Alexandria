[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 🖥️ Anytype Desktop

> Cliente de escritorio de Anytype para organizar notas, objetos y relaciones en un espacio de conocimiento personal.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.1k | Any Source Available License 1.0 (no OSI) | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** Any Source Available License 1.0 (no OSI). Source-available: uso no comercial o comercial solo en redes permitidas. Fuente: [LICENSE](https://github.com/anyproto/anytype-ts/blob/develop/LICENSE.md). GitHub la marca como NOASSERTION.

## ¿Qué es?

Cliente de escritorio de Anytype, una base de conocimiento local-first, P2P y cifrada de extremo a extremo, de Any, una asociación suiza (organización anyproto). Su licencia es la Any Source Available License 1.0, que no es OSI (GitHub muestra NOASSERTION). Sigue en alfa (v0.57.8-alpha), aunque ya tiene ~9k estrellas.

## ¿Qué hace?

Permite crear páginas, tareas, wikis, diarios y bases de datos con bloques componibles (texto, bases, kanban, calendario) y tipos de objeto propios. Funciona sin conexión con almacenamiento local, y sincroniza opcionalmente entre dispositivos P2P con cifrado de conocimiento cero (any-sync). Se extiende mediante una API gRPC.

## ¿Cómo lo hace?

Es una app Electron con TypeScript para macOS, Windows y Linux; el núcleo (anytype-heart) está en Go y se comunica por gRPC/protobuf. Los usuarios descargan los instaladores; compilarlo requiere Node.js, el middleware y, en ARM, un compilador de C++ para recompilar `keytar`. El repo incluye `AGENTS.md` con instrucciones para agentes de programación que contribuyan.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Leer y crear objetos de Anytype desde un agente con el servidor MCP oficial `anyproto/anytype-mcp` (el servidor MCP no está en el catálogo). | Activa la API local en Anytype, crea una clave e instala anytype-mcp en el agente. |
| [markitdown](markitdown.md) | Convertir documentos (DOCX, PDF) a Markdown antes de importarlos. (combinación por arquitectura) | Convierte con MarkItDown e importa los `.md` en Anytype. |
| [activepieces](activepieces.md) | Automatizar altas de objetos mediante la API local de Anytype. (combinación por arquitectura) (la API escucha en el equipo del usuario) | Expón la API solo en local y llama desde Activepieces en la misma máquina. |

**Notas:** Alternativas (elige una): appflowy. La licencia restringe usos comerciales concretos; léela antes de redistribuir.

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v0.57.8-alpha (2026-11-10) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/anyproto/anytype-ts/blob/develop/README.md) · [2](https://github.com/anyproto/anytype-mcp) · [3](https://github.com/anyproto/anytype-ts/blob/main/LICENSE.md)</sub>

## Ver similares

Grupo **Espacios de trabajo local-first tipo Notion**: Anytype Desktop ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [AppFlowy](appflowy.md) ⭐ recomendado | 64 | Si buscas esto: espacio de trabajo para notas, wikis y proyectos colaborativos, con funciones de IA y opciones de alojamiento propio. |
| 2 | **Anytype Desktop** (esta ficha) | 48 | Si buscas esto: cliente de escritorio de Anytype para organizar notas, objetos y relaciones en un espacio de conocimiento personal. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita modelo; sincronización y planes tienen condiciones propias; el código usa ASAL-1.0 |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es source-available con licencia específica; construir el cliente desde fuente requiere también middleware y motor, no solo bun install |
| Coste | El coste depende del proveedor o la ruta. No necesita modelo; sincronización y planes tienen condiciones propias; el código usa ASAL-1.0 |
| Equipo | Preparación según la ruta elegida. Instalador de escritorio para tu sistema; espacio local; cuenta según ruta |

Es source-available con licencia específica; construir el cliente desde fuente requiere también middleware y motor, no solo bun install

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador de escritorio para tu sistema
- espacio local
- cuenta según ruta

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
git clone https://github.com/anyproto/anytype-ts.git && cd anytype-ts
```

Comando copiado literalmente de el README (sección «🏗 Building from Source»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/anyproto/anytype-ts/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Anytype Desktop para mi objetivo y necesito pasos guiados. Lee https://github.com/anyproto/anytype-ts/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea dos objetos de prueba y relaciónalos en una vista sin añadir datos privados.

**Qué comprobar:** Puedes navegar de un objeto al otro y revisar dónde se guardan.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar notas y proyectos personales
- Diseñar una colección con campos propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar notas y proyectos personales; Diseñar una colección con campos propios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es source-available con licencia específica; construir el cliente desde fuente requiere también middleware y motor, no solo bun install

## Stack y modelos

- **Stack:** Instalador de escritorio para tu sistema; espacio local; cuenta según ruta
- **Etiquetas:** `notas` `app` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AppFlowy](appflowy.md) | 78.9k | Espacio de trabajo para notas, wikis y proyectos colaborativos, con funciones de IA y opciones de alojamiento propio. |

## Enlaces

- 🐙 GitHub: [anyproto/anytype-ts](https://github.com/anyproto/anytype-ts)
- 🌐 Web: <https://anytype.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/anyproto/anytype-ts/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
