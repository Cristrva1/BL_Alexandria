[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Sincronización y gestión de archivos

# 🏠 server

> Servidor de Nextcloud para almacenar y compartir archivos, contactos y calendarios en infraestructura propia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 37.5k | AGPL-3.0 | PHP | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

Servidor de Nextcloud: la plataforma autoalojada de archivos, colaboración y productividad mantenida por Nextcloud GmbH y su comunidad. Licencia AGPL-3.0-or-later, sin CLA. Es muy madura y activa (~37k estrellas, v33.0.11).

## ¿Qué hace?

Sincroniza y comparte archivos entre escritorio, móvil y web, y es la base sobre la que se instalan apps como calendario, contactos, Talk, ofimática y flujos de trabajo. Las apps oficiales y de terceros se instalan desde su tienda de apps. Ofrece funciones de IA (Nextcloud Assistant) que pueden usar modelos locales o proveedores externos según los backends que configures.

## ¿Cómo lo hace?

Es una aplicación PHP con frontend en JavaScript/Vue; necesita servidor web, PHP y una base de datos (MySQL/MariaDB, PostgreSQL o SQLite para pruebas). La vía recomendada para autoalojarlo es Nextcloud All-in-One (contenedores Docker que gestionan Apache, base de datos, copias y actualizaciones); también hay paquetes, appliances y proveedores. Este repositorio es el código del servidor para desarrolladores; para producción conviene usar las releases o AIO, no el árbol `master`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [coolify](coolify.md) | Desplegar Nextcloud como servicio de un clic en un servidor propio (Coolify documenta el servicio Nextcloud). | Instala Coolify y añade el servicio Nextcloud desde su catálogo. |
| [Home Assistant](home-assistant.md) | Vigilar el estado del servidor Nextcloud desde Home Assistant con su integración oficial de Nextcloud. | Activa la integración en Home Assistant con un usuario administrador de Nextcloud. |
| [Ollama](ollama.md) | Dar a Nextcloud Assistant un modelo local mediante un backend compatible con la API de OpenAI. (combinación por arquitectura) (la app integration_openai admite endpoints compatibles; la compatibilidad concreta con Ollama es [DATO NO VERIFICADO] en este lote) | Levanta Ollama, instala la app de integración y apunta su URL al endpoint compatible. |
| [CasaOS](casaos.md) | Combinación recíproca: CasaOS lo enlaza como «Nube de archivos como app. (combinación por arquitectura)». | Orden indicado desde CasaOS: Instala Nextcloud desde la tienda o como contenedor. |

**Notas:** Sin alternativas declaradas en el catálogo. Para producción, Nextcloud AIO simplifica mucho el mantenimiento.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v33.0.11 (2026-11-12) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/nextcloud/server/blob/master/README.md) · [2](https://github.com/nextcloud/all-in-one) · [3](https://docs.nextcloud.com/server/latest/admin_manual/ai/index.html) · [4](https://apps.nextcloud.com/apps/integration_openai) · [5](https://coolify.io/docs/services/nextcloud) · [6](https://www.home-assistant.io/integrations/nextcloud/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El servidor básico no necesita IA; infraestructura, soporte y apps opcionales pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Su función principal es almacenamiento y colaboración, por eso pasa al área de organización de archivos; IA es una extensión opcional |
| Coste | Sin pago a un modelo en la ruta básica. El servidor básico no necesita IA; infraestructura, soporte y apps opcionales pueden costar |
| Equipo | Preparación según la ruta elegida. Servidor compatible según guía; dominio o entorno local; almacenamiento |

Su función principal es almacenamiento y colaboración, por eso pasa al área de organización de archivos; IA es una extensión opcional

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servidor compatible según guía
- dominio o entorno local
- almacenamiento

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://nextcloud.com/install/#instructions-server)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar server para mi objetivo y necesito pasos guiados. Lee https://nextcloud.com/install/#instructions-server. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una cuenta de prueba, sube un archivo y comparte un enlace con permisos limitados.

**Qué comprobar:** Puedes abrir el archivo con los permisos configurados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Alojar documentos de un equipo
- Sincronizar archivos y calendarios propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Alojar documentos de un equipo; Sincronizar archivos y calendarios propios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Su función principal es almacenamiento y colaboración, por eso pasa al área de organización de archivos; IA es una extensión opcional

## Stack y modelos

- **Stack:** Servidor compatible según guía; dominio o entorno local; almacenamiento
- **Etiquetas:** `workspaces` `cloud` `collaboration` `decentralized` `design` `distributed` `enterprise` `federation`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [nextcloud/server](https://github.com/nextcloud/server)
- 🌐 Web: <https://nextcloud.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría corregida en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/nextcloud/server/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
