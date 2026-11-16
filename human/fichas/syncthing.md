[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Sincronización y gestión de archivos

# 🖥️ syncthing

> Aplicación para sincronizar archivos entre dispositivos directamente y controlar qué carpetas se comparten.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 90.4k | MPL-2.0 | Go | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Programa de sincronización continua de archivos entre dispositivos, sin servidor central. Licencia MPL-2.0. Es un proyecto comunitario muy maduro (~90k estrellas, v2.1.7) que prioriza la seguridad de los datos.

## ¿Qué hace?

Sincroniza carpetas entre dos o más equipos directamente, punto a punto, con cifrado TLS y dispositivos autenticados por ID. Sus objetivos declarados, en orden, son: evitar la pérdida de datos, ser seguro frente a atacantes, ser fácil de usar y automático. Ofrece versionado de archivos, carpetas de solo envío o solo recepción y patrones de exclusión.

## ¿Cómo lo hace?

Es un binario en Go con interfaz web local. Se instala con paquetes del sistema, binarios oficiales, Docker (según `README-Docker.md`) o envoltorios de la comunidad. Usa servidores públicos de descubrimiento y relés de la comunidad para encontrar dispositivos y atravesar NAT, y puedes autoalojarlos. No es una copia de seguridad: los borrados también se sincronizan.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Home Assistant](home-assistant.md) | Supervisar carpetas y dispositivos con la integración oficial de Syncthing en Home Assistant. | Crea una clave de API en Syncthing y añade la integración. |
| [coolify](coolify.md) | Desplegar un nodo Syncthing siempre encendido en un servidor (Coolify documenta el servicio Syncthing). | Instala Coolify y añade el servicio Syncthing; empareja tus dispositivos con él. |
| [paperless-ngx](paperless-ngx.md) | Llevar escaneos desde el móvil o el portátil a la carpeta de consumo de Paperless-ngx. (combinación por arquitectura) | Comparte en Syncthing la carpeta `consume` de Paperless-ngx en modo solo recepción. |
| [audiobookshelf](audiobookshelf.md) | Alimentar la biblioteca de Audiobookshelf desde otros equipos. (combinación por arquitectura) | Comparte la carpeta de la biblioteca en Syncthing. |
| [spotDL](spotdl.md) | Combinación recíproca: spotDL lo enlaza como «Syncthing puede sincronizar la carpeta de música descargada entre tus dispositivos (combinación por arquitectura)». | Orden indicado desde spotDL: Descarga con spotDL en una carpeta; después compártela con Syncthing. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (6). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Calibre-Web](calibre-web.md) · [Immich](immich.md) · [Joplin](joplin.md) · [Kavita](kavita.md) · [Logseq](logseq.md) · [PhotoPrism](photoprism.md)

**Notas:** Sin alternativas declaradas. Complementa Syncthing con copias de seguridad reales.

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v2.1.7 (2026-10-21) · licencia declarada MPL-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/syncthing/syncthing/blob/main/README.md) · [2](https://docs.syncthing.net/intro/getting-started.html) · [3](https://www.home-assistant.io/integrations/syncthing/) · [4](https://coolify.io/docs/services/syncthing)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita modelo ni proveedor Cloud obligatorio; red y almacenamiento son recursos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Sincronización no es copia de seguridad: los cambios y borrados pueden propagarse según configuración |
| Coste | Sin pago a un modelo en la ruta básica. No necesita modelo ni proveedor Cloud obligatorio; red y almacenamiento son recursos propios |
| Equipo | Preparación según la ruta elegida. Dos dispositivos compatibles; carpetas de prueba; conexión entre pares |

Sincronización no es copia de seguridad: los cambios y borrados pueden propagarse según configuración

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Dos dispositivos compatibles
- carpetas de prueba
- conexión entre pares

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/syncthing/syncthing/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar syncthing para mi objetivo y necesito pasos guiados. Lee https://github.com/syncthing/syncthing/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sincroniza una carpeta con un archivo ficticio y observa un cambio desde el segundo equipo.

**Qué comprobar:** Ambos equipos muestran el mismo contenido y estado de sincronización.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Compartir una carpeta personal entre equipos
- Mantener una colección de notas sincronizada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Compartir una carpeta personal entre equipos; Mantener una colección de notas sincronizada | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Sincronización no es copia de seguridad: los cambios y borrados pueden propagarse según configuración

## Stack y modelos

- **Stack:** Dos dispositivos compatibles; carpetas de prueba; conexión entre pares
- **Etiquetas:** `archivos` `app` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [syncthing/syncthing](https://github.com/syncthing/syncthing)
- 🌐 Web: <https://syncthing.net/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/syncthing/syncthing/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
