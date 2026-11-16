[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Libros, podcasts y bibliotecas personales

# ⚙️ audiobookshelf

> Servidor personal para organizar audiolibros y podcasts, escuchar contenido y conservar el progreso de reproducción.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15k | GPL-3.0 | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

Servidor autoalojado de audiolibros y podcasts, creado por @advplyr. Licencia GPL-3.0. Es maduro y activo (~15k estrellas, v2.37.2), pero el README avisa que no se revisan PR del frontend en Vue porque se está reescribiendo en React.

## ¿Qué hace?

Transmite cualquier formato de audio, guarda el progreso por usuario y lo sincroniza entre dispositivos. Busca y descarga podcasts con descarga automática, obtiene metadatos y portadas, y admite subida masiva, varios usuarios con permisos y copias de seguridad diarias. Tiene PWA, soporte de Chromecast y apps para Android e iOS (en beta) en un repositorio aparte.

## ¿Cómo lo hace?

Es una aplicación Node.js con frontend en Vue (en migración a React). Se instala sobre todo con Docker o Docker Compose; la documentación oficial describe otros métodos. Si va detrás de un proxy inverso, este debe permitir WebSockets, que el README marca como obligatorios. Tiene una API REST documentada.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [coolify](coolify.md) | Desplegar Audiobookshelf como servicio de un clic (Coolify documenta el servicio Audiobookshelf). | Instala Coolify y añade el servicio Audiobookshelf desde su catálogo. |
| [syncthing](syncthing.md) | Llevar audiolibros desde otros equipos a la carpeta de la biblioteca; Audiobookshelf detecta los cambios sin reescanear. (combinación por arquitectura) | Comparte en Syncthing la carpeta que usa la biblioteca de Audiobookshelf. |
| [n8n](n8n.md) | Automatizar tareas (avisos de episodios nuevos, informes de escucha) con la API REST de Audiobookshelf. (combinación por arquitectura) | Crea un token de API en Audiobookshelf y úsalo en un nodo HTTP Request de n8n. |

**Notas:** Sin alternativas declaradas. Antes de contribuir al frontend, revisa el estado de la migración a React.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v2.37.2 (2026-10-23) · licencia declarada GPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/advplyr/audiobookshelf/blob/master/readme.md) · [2](https://www.audiobookshelf.org/docs) · [3](https://api.audiobookshelf.org/) · [4](https://coolify.io/docs/services/audiobookshelf)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa modelo; almacenamiento, servidor y acceso a contenidos pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Los comandos Docker y VS Code del README son para desarrollo; para usar el servidor sigue la guía de instalación |
| Coste | Sin pago a un modelo en la ruta básica. No usa modelo; almacenamiento, servidor y acceso a contenidos pueden costar |
| Equipo | Preparación según la ruta elegida. Servidor o Docker; carpetas de audio; volumen persistente; WebSocket si usas proxy |

Los comandos Docker y VS Code del README son para desarrollo; para usar el servidor sigue la guía de instalación

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servidor o Docker
- carpetas de audio
- volumen persistente
- WebSocket si usas proxy

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://audiobookshelf.org/docs/category/installation)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar audiobookshelf para mi objetivo y necesito pasos guiados. Lee https://audiobookshelf.org/docs/category/installation. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade una grabación propia, reproduce un minuto y comprueba el progreso guardado.

**Qué comprobar:** Puedes retomar la reproducción desde otro dispositivo autorizado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar audiolibros propios o autorizados
- Gestionar una colección de podcasts

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar audiolibros propios o autorizados; Gestionar una colección de podcasts | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los comandos Docker y VS Code del README son para desarrollo; para usar el servidor sigue la guía de instalación

## Stack y modelos

- **Stack:** Servidor o Docker; carpetas de audio; volumen persistente; WebSocket si usas proxy
- **Etiquetas:** `lectura` `server` `javascript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [advplyr/audiobookshelf](https://github.com/advplyr/audiobookshelf)
- 🌐 Web: <https://audiobookshelf.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/advplyr/audiobookshelf/blob/master/readme.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
