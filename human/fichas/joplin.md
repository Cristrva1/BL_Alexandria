[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 🖥️ Joplin

> App de notas y tareas centrada en la privacidad, offline first, con sincronización cifrada de extremo a extremo y apps para escritorio y móvil.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 57.2k | AGPL-3.0 | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Aplicación de notas de código abierto (AGPL-3.0 según el archivo de licencia) creada por Laurent Cozic. Muy madura, con ingresos por Joplin Cloud y donaciones.

## ¿Qué hace?

Organiza grandes cantidades de notas en libretas con etiquetas y tareas, en Markdown, con búsqueda de texto completo, importación de Evernote (ENEX), Web Clipper, plugins y temas, y sincronización con cifrado de extremo a extremo.

## ¿Cómo lo hace?

Escrita en TypeScript; apps para Windows, macOS, Linux, Android e iOS y una CLI. Sincroniza con Nextcloud, Dropbox, OneDrive, WebDAV, AWS S3, el sistema de archivos, Joplin Server autoalojado o Joplin Cloud.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [server](nextcloud-server.md) | Nextcloud es uno de los destinos de sincronización documentados por Joplin. | Nextcloud en marcha; después elige Nextcloud como destino en la configuración de sincronización. |
| [syncthing](syncthing.md) | La sincronización por sistema de archivos de Joplin puede apoyarse en una carpeta replicada con Syncthing (combinación por arquitectura). | Elige el destino de sistema de archivos; después sincroniza esa carpeta con Syncthing en un solo sentido de escritura. |
| [Pandoc](pandoc.md) | Las notas exportadas en Markdown se convierten con Pandoc a otros formatos (combinación por arquitectura). | Exporta desde Joplin; después convierte con Pandoc. |

**Notas:** Alternativas (elige una): trilium, siyuan, logseq.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v3.7.22 (2026-10-28) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/laurent22/joplin/blob/dev/README.md) · [2](https://joplinapp.org)</sub>

## Ver similares

Grupo **Notas y bases de conocimiento personales**: Joplin ocupa la posición 4 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [SiYuan](siyuan.md) ⭐ recomendado | 79 | Si quieres bloques referenciables y una base de conocimiento local muy completa. |
| 2 | [Trilium Notes](trilium.md) | 65 | Si quieres jerarquías profundas de notas con scripting y servidor propio. |
| 3 | [Logseq](logseq.md) | 59 | Si piensas en esquemas y grafos con notas diarias, local-first. |
| 4 | **Joplin** (esta ficha) | 58 | Si quieres notas Markdown con sincronización cifrada en todos tus dispositivos. |

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/laurent22/joplin/blob/dev/README.md)

[Abrir la web o descarga indicada por el autor](https://joplinapp.org)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Joplin para mi objetivo y necesito pasos guiados. Lee https://github.com/laurent22/joplin/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Joplin, crea una libreta con notas y configura la sincronización con una carpeta o WebDAV de prueba..

**Qué comprobar:** Las notas aparecen en un segundo dispositivo tras sincronizar..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- sustituir Evernote importando tus notas a una app abierta
- mantener notas cifradas sincronizadas entre el móvil y el ordenador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: sustituir Evernote importando tus notas a una app abierta; mantener notas cifradas sincronizadas entre el móvil y el ordenador | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `notas` `typescript` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Trilium Notes](trilium.md) | 39k | App de notas jerárquicas para bases de conocimiento grandes: clonado de notas, scripts, relaciones, mapas y servidor de sincronización autoalojado. |
| [SiYuan](siyuan.md) | 47.2k | Espacio de conocimiento por bloques, local-first y autoalojable, con referencias bidireccionales, consultas SQL, mapas mentales y funciones de IA. |
| [Logseq](logseq.md) | 45.6k | Plataforma de gestión del conocimiento local-first en forma de esquema, con páginas enlazadas, diario, consultas y grafo, en Markdown u Org. |

## Enlaces

- 🐙 GitHub: [laurent22/joplin](https://github.com/laurent22/joplin)
- 🌐 Web: <https://joplinapp.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/laurent22/joplin/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
