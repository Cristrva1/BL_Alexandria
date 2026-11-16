[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 🖥️ Logseq

> Plataforma de gestión del conocimiento local-first en forma de esquema, con páginas enlazadas, diario, consultas y grafo, en Markdown u Org.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 45.6k | AGPL-3.0 | Clojure | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Plataforma de conocimiento de código abierto (AGPL-3.0) de Logseq Inc. Muy popular; el equipo trabaja en una versión basada en base de datos que sustituirá al modelo de archivos.

## ¿Qué hace?

Organiza notas como esquemas de bloques con enlaces bidireccionales, diario, etiquetas, consultas, tareas, pizarras y grafo de conocimiento, sobre archivos Markdown u Org-mode en tu equipo. Admite plugins y temas.

## ¿Cómo lo hace?

Escrita en Clojure/ClojureScript; apps para Windows, macOS, Linux, iOS y Android desde las releases (también con script de instalación en Linux). Los datos son archivos locales; la sincronización oficial es un servicio aparte.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [syncthing](syncthing.md) | Un grafo de Logseq es una carpeta de archivos que se puede sincronizar con Syncthing entre equipos (combinación por arquitectura). | Sincroniza la carpeta del grafo; evita editarlo a la vez en dos equipos. |
| [Pandoc](pandoc.md) | Las páginas en Markdown u Org se convierten con Pandoc a otros formatos (combinación por arquitectura). | Exporta o toma los archivos del grafo; después convierte con Pandoc. |
| [Claude Code](claude-code.md) | Al ser archivos Markdown, un agente de código puede leer y reorganizar páginas del grafo (combinación por arquitectura). | Haz copia del grafo; después deja al agente trabajar sobre esa copia. |
| [D2](d2.md) | Combinación recíproca: D2 lo enlaza como «El plugin comunitario Logseq-D2 renderiza bloques D2 en las notas de Logseq». | Orden indicado desde D2: Instala D2 y el plugin Logseq-D2; después escribe bloques D2 en tus páginas. |

**Notas:** Alternativas (elige una): joplin, trilium, siyuan. La migración a la versión con base de datos puede cambiar el formato de almacenamiento.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 2.0.2 (2026-10-07) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/logseq/logseq/blob/master/README.md) · [2](https://docs.logseq.com/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y una copia de datos o archivos para la primera prueba.

1. Abre las descargas o la web de la aplicación enlazadas por el autor; elige la versión para tu sistema.
2. Sigue su guía de inicio y configura únicamente la función que necesitas probar.
3. Abre un archivo o caso pequeño, guarda un resultado y comprueba que puedes recuperarlo antes de importar material real.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/logseq/logseq/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/logseq/logseq/releases)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Logseq para mi objetivo y necesito pasos guiados. Lee https://github.com/logseq/logseq/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Logseq, abre una carpeta vacía como grafo y crea una página enlazada desde el diario..

**Qué comprobar:** La página aparece en el grafo y sus referencias se muestran en ambas notas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- llevar un diario y notas enlazadas en archivos de texto propios
- organizar investigación con bloques, referencias y consultas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: llevar un diario y notas enlazadas en archivos de texto propios; organizar investigación con bloques, referencias y consultas | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Clojure, Dockerfile, package.json
- **Etiquetas:** `notas` `clojure` `app` `local`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Joplin](joplin.md) | 57.2k | App de notas y tareas centrada en la privacidad, offline first, con sincronización cifrada de extremo a extremo y apps para escritorio y móvil. |
| [Trilium Notes](trilium.md) | 39k | App de notas jerárquicas para bases de conocimiento grandes: clonado de notas, scripts, relaciones, mapas y servidor de sincronización autoalojado. |
| [SiYuan](siyuan.md) | 47.2k | Espacio de conocimiento por bloques, local-first y autoalojable, con referencias bidireccionales, consultas SQL, mapas mentales y funciones de IA. |

## Enlaces

- 🐙 GitHub: [logseq/logseq](https://github.com/logseq/logseq)
- 🌐 Web: <https://logseq.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/logseq/logseq/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
