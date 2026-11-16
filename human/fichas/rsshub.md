[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# ⚙️ RSSHub

> Generador de feeds RSS para miles de webs y redes sin RSS propio; instancia pública o autoalojada con Docker.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47k | AGPL-3.0 | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## ¿Qué es?

Red y servidor de feeds RSS de código abierto (AGPL-3.0) creado por DIYgod y mantenido por una comunidad amplia. Muy usado (más de 5.000 instancias según el proyecto) y en desarrollo continuo.

## ¿Qué hace?

Convierte contenidos de redes sociales, webs de noticias, plataformas de vídeo y otros servicios en feeds RSS, Atom o JSON mediante rutas parametrizables. Se complementa con extensiones como RSSHub Radar para descubrir feeds y con lectores como Folo.

## ¿Cómo lo hace?

Escrito en TypeScript sobre Node.js; se usa la instancia pública rsshub.app o se autoaloja con Docker (imagen diygod/rsshub) o npm. Algunas rutas necesitan cookies, claves o un navegador sin interfaz configurados por variables de entorno; admite caché con Redis.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FreshRSS](freshrss.md) | FreshRSS se suscribe a las rutas de RSSHub como a cualquier feed y las organiza para lectura (combinación por arquitectura). | RSSHub en marcha; después añade sus URLs como feeds en FreshRSS. |
| [Miniflux](miniflux.md) | Miniflux lee los feeds generados por RSSHub y aplica sus filtros y su lectura minimalista (combinación por arquitectura). | RSSHub primero; después suscribe sus rutas en Miniflux. |
| [activepieces](activepieces.md) | Un disparador de RSS en Activepieces puede reaccionar a nuevos elementos de una ruta de RSSHub (combinación por arquitectura). | RSSHub accesible desde Activepieces; después crea el flujo con el disparador de feed. |
| [coolify](coolify.md) | RSSHub se publica como imagen Docker con Redis opcional, un despliegue sencillo de gestionar en Coolify (combinación por arquitectura). | Coolify primero; luego crea el servicio con la imagen diygod/rsshub. |

**Notas:** La instancia pública puede limitar peticiones; para uso intensivo conviene autoalojarla.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2026.11.16-8658.b4990a8 (2026-11-16) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/DIYgod/RSSHub/blob/master/README.md) · [2](https://docs.rsshub.app/)</sub>

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

[Instrucciones originales de instalación](https://github.com/DIYgod/RSSHub/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar RSSHub para mi objetivo y necesito pasos guiados. Lee https://github.com/DIYgod/RSSHub/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega RSSHub con Docker según su documentación y abre una ruta de ejemplo en el navegador..

**Qué comprobar:** La ruta devuelve un feed RSS válido que tu lector puede suscribir..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- seguir canales, perfiles o webs sin RSS desde tu lector de feeds
- alimentar un flujo de monitorización de fuentes con feeds uniformes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: seguir canales, perfiles o webs sin RSS desde tu lector de feeds; alimentar un flujo de monitorización de fuentes con feeds uniformes | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Algunas rutas extraen sitios sin API pública: revisa sus términos de uso.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, docker-compose.yml, package.json
- **Etiquetas:** `research` `rss` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [DIYgod/RSSHub](https://github.com/DIYgod/RSSHub)
- 🌐 Web: <https://docs.rsshub.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/DIYgod/RSSHub/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
