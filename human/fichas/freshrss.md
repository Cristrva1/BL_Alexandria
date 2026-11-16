[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# ⚙️ FreshRSS

> Agregador de noticias RSS autoalojado, ligero y multiusuario, con API para apps móviles, WebSub, extracción por XPath y extensiones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.6k | AGPL-3.0 | PHP | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## ¿Qué es?

Agregador RSS autoalojado de código abierto (AGPL-3.0) mantenido por la comunidad FreshRSS. Proyecto maduro y traducido a más de 20 idiomas.

## ¿Qué hace?

Recoge y organiza feeds RSS/Atom y JSON para varios usuarios, con modo de lectura anónimo, etiquetas, consultas de usuario compartibles en HTML, RSS y OPML, notificaciones instantáneas por WebSub y extracción básica de webs sin feed mediante XPath. Admite varios métodos de inicio de sesión, incluido OpenID Connect.

## ¿Cómo lo hace?

Escrito en PHP; funciona con SQLite, MySQL/MariaDB o PostgreSQL y se instala en un servidor web o con la imagen Docker oficial. Ofrece API compatible con clientes móviles, CLI y sistema de extensiones.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [RSSHub](rsshub.md) | RSSHub genera feeds para webs sin RSS que FreshRSS puede suscribir (combinación por arquitectura). | RSSHub en marcha; después añade sus rutas como feeds en FreshRSS. |
| [wallabag](wallabag.md) | FreshRSS incluye wallabag entre sus servicios para compartir artículos y guardarlos para leer más tarde. | wallabag accesible; después configura su URL en las opciones de compartir de FreshRSS. |
| [coolify](coolify.md) | La imagen Docker oficial de FreshRSS se despliega y respalda fácilmente desde Coolify (combinación por arquitectura). | Coolify primero; luego crea el servicio con la imagen de FreshRSS y un volumen de datos. |

**Notas:** Alternativas (elige una): miniflux.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 1.30.4 (2026-10-21) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/FreshRSS/FreshRSS/blob/edge/README.md) · [2](https://freshrss.github.io/FreshRSS/en/users/08_sharing_services.html)</sub>

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

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/FreshRSS/FreshRSS/blob/edge/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FreshRSS para mi objetivo y necesito pasos guiados. Lee https://github.com/FreshRSS/FreshRSS/blob/edge/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega FreshRSS con Docker, importa un archivo OPML pequeño y actualiza los feeds..

**Qué comprobar:** Los artículos aparecen en la interfaz y un cliente móvil compatible puede sincronizarlos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- centralizar en tu servidor los feeds de noticias y blogs que sigues
- seguir webs sin RSS con reglas de extracción XPath

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: centralizar en tu servidor los feeds de noticias y blogs que sigues; seguir webs sin RSS con reglas de extracción XPath | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** PHP, composer.json, package.json
- **Etiquetas:** `research` `rss` `php` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Miniflux](miniflux.md) | 9.9k | Lector de feeds minimalista y rápido en Go sobre PostgreSQL, con privacidad, búsqueda de texto completo y más de 25 integraciones. |

## Enlaces

- 🐙 GitHub: [FreshRSS/FreshRSS](https://github.com/FreshRSS/FreshRSS)
- 🌐 Web: <https://freshrss.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/FreshRSS/FreshRSS/blob/edge/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
