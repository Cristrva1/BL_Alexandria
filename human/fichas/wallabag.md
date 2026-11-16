[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# ⚙️ wallabag

> Aplicación autoalojada para guardar páginas web y leerlas más tarde sin distracciones, con apps móviles y extensión de navegador.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.1k | MIT | PHP | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Aplicación «leer más tarde» de código abierto (MIT) mantenida por la comunidad wallabag desde 2013. Madura, con apps oficiales para Android e iOS y servicio alojado (wallabag.it) aparte.

## ¿Qué hace?

Guarda páginas web extrayendo el contenido principal sin anuncios ni ventanas emergentes, permite etiquetar, anotar, marcar como leído y exportar a formatos como EPUB o PDF, y sincroniza con apps móviles y lectores electrónicos compatibles.

## ¿Cómo lo hace?

Escrita en PHP con Symfony; se instala en un servidor con los requisitos documentados o con Docker. Ofrece API REST con OAuth usada por las apps y la extensión wallabagger.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FreshRSS](freshrss.md) | FreshRSS puede enviar artículos a wallabag mediante su servicio de compartir integrado. | wallabag primero; después configúralo en FreshRSS. |
| [Miniflux](miniflux.md) | Miniflux integra wallabag entre sus servicios de terceros para guardar artículos. | wallabag con credenciales de API; después actívalo en las integraciones de Miniflux. |
| [coolify](coolify.md) | wallabag se despliega con Docker y una base de datos, gestionable desde Coolify (combinación por arquitectura). | Coolify primero; luego despliega wallabag con su base de datos y volúmenes. |

**Notas:** Alternativa cercana en el catálogo: karakeep (marcadores con IA).

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 2.6.17 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/wallabag/wallabag/blob/master/README.md) · [2](https://doc.wallabag.org/)</sub>

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

**Entrada documentada (bash):**

```
git clone https://github.com/wallabag/wallabag.git
```

Comando copiado literalmente de el README (sección «Installation»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/wallabag/wallabag/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar wallabag para mi objetivo y necesito pasos guiados. Lee https://github.com/wallabag/wallabag/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala wallabag con Docker o según su documentación y guarda un artículo desde la extensión del navegador..

**Qué comprobar:** El artículo aparece limpio en la lista de lectura y se puede exportar..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- guardar artículos para leerlos sin conexión en el móvil
- archivar lecturas con etiquetas y anotaciones en tu propio servidor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: guardar artículos para leerlos sin conexión en el móvil; archivar lecturas con etiquetas y anotaciones en tu propio servidor | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** PHP, compose.yaml, composer.json, package.json
- **Etiquetas:** `research` `read-later` `php` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [wallabag/wallabag](https://github.com/wallabag/wallabag)
- 🌐 Web: <https://wallabag.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/wallabag/wallabag/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
