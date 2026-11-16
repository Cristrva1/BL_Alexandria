[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Sincronización y gestión de archivos

# ⚙️ PhotoPrism

> App de fotos con IA y privacidad primero para explorar, organizar y compartir fotos y vídeos, autoalojada o en la nube.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.5k | AGPL-3.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Aplicación de fotos de código abierto (AGPL-3.0) de PhotoPrism UG, financiada con membresías que desbloquean funciones adicionales. Madura y activa.

## ¿Qué hace?

Indexa fotos y vídeos (incluidos RAW), los etiqueta y clasifica automáticamente, reconoce caras, muestra mapas, permite búsqueda avanzada, álbumes y compartición, y se sincroniza con apps móviles o clientes WebDAV.

## ¿Cómo lo hace?

Escrito en Go con TensorFlow; se despliega con Docker Compose y MariaDB (o SQLite). Ofrece WebDAV para sincronizar desde el escritorio y apps compatibles como PhotoSync para copias desde el móvil.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [server](nextcloud-server.md) | PhotoPrism puede indexar carpetas sincronizadas por Nextcloud montadas en su contenedor (combinación por arquitectura). | Monta la carpeta de fotos de Nextcloud como originales; después indexa en PhotoPrism. |
| [syncthing](syncthing.md) | Syncthing lleva las fotos de otros equipos a la carpeta de originales de PhotoPrism (combinación por arquitectura). | Sincroniza con Syncthing; después ejecuta la indexación. |
| [coolify](coolify.md) | El Compose de PhotoPrism con su base de datos se despliega desde Coolify (combinación por arquitectura). | Coolify primero; después importa el Compose con volúmenes persistentes. |

**Notas:** Alternativas (elige una): immich.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 261029-963b58c50 (2026-10-29) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/photoprism/photoprism/blob/develop/README.md) · [2](https://docs.photoprism.app/user-guide/sync/webdav/) · [3](https://docs.photoprism.app/license/agpl/)</sub>

## Ver similares

Grupo **Gestión de fotos auto-hospedada**: PhotoPrism ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Immich](immich.md) ⭐ recomendado | 81 | Si buscas esto: gestión autoalojada de fotos y vídeos de alto rendimiento, alternativa a Google Photos, con copia automática desde el móvil y búsqueda con IA local. |
| 2 | **PhotoPrism** (esta ficha) | 66 | Si buscas esto: app de fotos con IA y privacidad primero para explorar, organizar y compartir fotos y vídeos, autoalojada o en la nube. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/photoprism/photoprism/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PhotoPrism para mi objetivo y necesito pasos guiados. Lee https://github.com/photoprism/photoprism/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega PhotoPrism con Docker Compose, indexa una carpeta de fotos y busca por etiqueta..

**Qué comprobar:** Las fotos aparecen clasificadas y la búsqueda por etiqueta o lugar devuelve resultados..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- organizar automáticamente un archivo de fotos por lugares, etiquetas y personas
- navegar y compartir una colección familiar desde tu servidor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: organizar automáticamente un archivo de fotos por lugares, etiquetas y personas; navegar y compartir una colección familiar desde tu servidor | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. AGPL-3.0; algunas funciones requieren una membresía de pago y el nombre es marca registrada.

## Stack y modelos

- **Stack:** Go, Dockerfile, compose.yaml, go.mod, package.json
- **Etiquetas:** `self-hosted` `go` `docker` `image`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Immich](immich.md) | 119k | Gestión autoalojada de fotos y vídeos de alto rendimiento, alternativa a Google Photos, con copia automática desde el móvil y búsqueda con IA local. |

## Enlaces

- 🐙 GitHub: [photoprism/photoprism](https://github.com/photoprism/photoprism)
- 🌐 Web: <https://www.photoprism.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/photoprism/photoprism/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
