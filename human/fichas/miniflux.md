[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# ⚙️ Miniflux

> Lector de feeds minimalista y rápido en Go sobre PostgreSQL, con privacidad, búsqueda de texto completo y más de 25 integraciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.9k | Apache-2.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Lector de feeds de código abierto (Apache-2.0) creado por Frédéric Guillot. Proyecto maduro, deliberadamente minimalista y «opinionated».

## ¿Qué hace?

Lee Atom, RSS y JSON Feed, importa y exporta OPML, reproduce adjuntos y vídeos de YouTube, organiza por categorías y marcadores, comparte artículos y ofrece búsqueda de texto completo. Elimina píxeles de rastreo y parámetros de seguimiento, y se integra con más de 25 servicios.

## ¿Cómo lo hace?

Escrito en Go como binario único; requiere PostgreSQL. Se instala con paquetes, Docker o binarios, y ofrece API propia y compatibilidad con clientes Fever y Google Reader.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [RSSHub](rsshub.md) | Miniflux suscribe las rutas de RSSHub para seguir webs que no publican feeds (combinación por arquitectura). | RSSHub en marcha; después añade sus rutas en Miniflux. |
| [wallabag](wallabag.md) | wallabag figura entre las integraciones documentadas de Miniflux para guardar artículos. | wallabag con credenciales; después actívalo en Miniflux. |
| [coolify](coolify.md) | Miniflux y PostgreSQL se despliegan con Docker Compose, un patrón gestionable desde Coolify (combinación por arquitectura). | Coolify primero; luego el Compose de Miniflux con su base de datos. |

**Notas:** Alternativas (elige una): freshrss.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada 2.3.5 (2026-11-02) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/miniflux/v2/blob/main/README.md) · [2](https://miniflux.app/docs/)</sub>

## Ver similares

Grupo **Lectores RSS auto-hospedados**: Miniflux ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [FreshRSS](freshrss.md) ⭐ recomendado | 65 | Si buscas esto: agregador de noticias RSS autoalojado, ligero y multiusuario, con API para apps móviles, WebSub, extracción por XPath y extensiones. |
| 2 | **Miniflux** (esta ficha) | 58 | Si buscas esto: lector de feeds minimalista y rápido en Go sobre PostgreSQL, con privacidad, búsqueda de texto completo y más de 25 integraciones. |

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/miniflux/v2/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Miniflux para mi objetivo y necesito pasos guiados. Lee https://github.com/miniflux/v2/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Miniflux con PostgreSQL según la guía, importa un OPML y lee un artículo..

**Qué comprobar:** Los feeds se actualizan, la búsqueda devuelve resultados y no aparecen píxeles de seguimiento..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- leer feeds sin rastreadores en una instancia propia ligera
- enviar artículos automáticamente a un servicio de lectura o notas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: leer feeds sin rastreadores en una instancia propia ligera; enviar artículos automáticamente a un servicio de lectura o notas | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Go, go.mod
- **Etiquetas:** `research` `rss` `go` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [FreshRSS](freshrss.md) | 16.6k | Agregador de noticias RSS autoalojado, ligero y multiusuario, con API para apps móviles, WebSub, extracción por XPath y extensiones. |

## Enlaces

- 🐙 GitHub: [miniflux/v2](https://github.com/miniflux/v2)
- 🌐 Web: <https://miniflux.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/miniflux/v2/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
