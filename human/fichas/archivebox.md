[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# 🔍 ArchiveBox

> Archivador web auto-hospedado que guarda páginas en HTML, PDF, capturas y medios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29k | MIT | Python | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Aplicación autoalojada para archivar sitios web en varios formatos. Licencia MIT. Es madura y activa (~29k estrellas, v0.9.77).

## ¿Qué hace?

Guarda cada URL como HTML original, SingleFile, captura PNG, PDF, WARC, texto del artículo, medios (con yt-dlp), repositorios git y metadatos. Acepta URLs sueltas o importaciones programadas desde marcadores, historial, redes sociales o RSS, y ofrece interfaz web, CLI y extensión de navegador. Por defecto también envía cada página a archive.org como redundancia (se puede desactivar).

## ¿Cómo lo hace?

Se instala con Docker Compose (recomendado) o `pip install archivebox` en Linux y macOS; usa Chrome, wget, yt-dlp y otras herramientas estándar. Se añaden URLs con `archivebox add` o desde la interfaz. Los archivos quedan en formatos abiertos legibles sin ArchiveBox.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [yt-dlp](yt-dlp.md) | Descarga de audio y vídeo, integrada como extractor. | Viene en la imagen Docker; en pip instala yt-dlp aparte. |
| [changedetection.io](changedetection.md) | Archivar una nueva copia cuando una página cambia. (combinación por arquitectura) | Usa una notificación de changedetection (webhook) para añadir la URL a ArchiveBox. |
| [karakeep](karakeep.md) | Marcadores del día a día en Karakeep y copias de archivo completas en ArchiveBox. (combinación por arquitectura) | Exporta los enlaces de Karakeep e impórtalos en ArchiveBox. |
| [instaloader](instaloader.md) | Combinación recíproca: instaloader lo enlaza como «Archivar también las publicaciones en formatos de archivo web. (combinación por arquitectura)». | Orden indicado desde instaloader: Pasa las URLs de las publicaciones a ArchiveBox. |

**Notas:** Sin alternativas declaradas. Desactiva el envío a archive.org si archivas páginas privadas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.9.77 (2026-10-27) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ArchiveBox/ArchiveBox/blob/dev/README.md) · [2](https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration#archivedotorg_enabled)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere modelo; almacenamiento, navegador y servidor son recursos propios |
| Claude Code | Compatibilidad por confirmar |
| Codex | Compatibilidad por confirmar |
| Antigravity | Compatibilidad por confirmar |
| Modelos locales | La función básica no necesita un modelo. El README menciona herramientas MCP pero falta confirmar aquí su configuración por cliente; los archivos no garantizan capturar toda web dinámica |
| Coste | Sin pago a un modelo en la ruta básica. No requiere modelo; almacenamiento, navegador y servidor son recursos propios |
| Equipo | Preparación según la ruta elegida. Docker o dependencias nativas; directorio persistente; espacio en disco |

El README menciona herramientas MCP pero falta confirmar aquí su configuración por cliente; los archivos no garantizan capturar toda web dinámica

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o dependencias nativas
- directorio persistente
- espacio en disco

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
pip install archivebox
```

Comando copiado literalmente de el README (sección «ArchiveBoxOpen-source self-hosted web archiving.»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/ArchiveBox/ArchiveBox/blob/dev/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ArchiveBox para mi objetivo y necesito pasos guiados. Lee https://github.com/ArchiveBox/ArchiveBox/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Archiva una página propia y abre las copias HTML y captura desde el panel.

**Qué comprobar:** La captura conserva la URL y se puede consultar después.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preservar documentación que cambia
- Crear una biblioteca de fuentes de una investigación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preservar documentación que cambia; Crear una biblioteca de fuentes de una investigación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README menciona herramientas MCP pero falta confirmar aquí su configuración por cliente; los archivos no garantizan capturar toda web dinámica

## Stack y modelos

- **Stack:** Docker o dependencias nativas; directorio persistente; espacio en disco
- **Etiquetas:** `scraping` `data` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ArchiveBox/ArchiveBox](https://github.com/ArchiveBox/ArchiveBox)
- 🌐 Web: <https://archivebox.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ArchiveBox/ArchiveBox/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
