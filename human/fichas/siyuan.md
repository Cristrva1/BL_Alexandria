[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 🖥️ SiYuan

> Espacio de conocimiento por bloques, local-first y autoalojable, con referencias bidireccionales, consultas SQL, mapas mentales y funciones de IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47.2k | AGPL-3.0 | TypeScript | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 79/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Gestor de conocimiento de código abierto (AGPL-3.0) de B3log. Muy activo; algunas funciones de sincronización en la nube requieren suscripción.

## ¿Qué hace?

Organiza el conocimiento en bloques con referencias bidireccionales, incrustaciones, consultas SQL, bases de datos, mapas mentales, PDF anotables, plantillas y espacio de trabajo colaborativo con agentes de IA; incluye escritura y preguntas con IA vía API de OpenAI.

## ¿Cómo lo hace?

Núcleo en Go y frontend TypeScript; se distribuye como app de escritorio, móvil y contenedor Docker (desde v3.7.0 hay que pasar `serve`), también con Helm. Los datos se guardan en local; la sincronización usa la nube de SiYuan, S3 o WebDAV.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | La IA de SiYuan usa una API compatible con OpenAI, que puede apuntar a un servidor local como Ollama (combinación por arquitectura). | Ollama en marcha; después configura su URL compatible con OpenAI en los ajustes de IA. |
| [server](nextcloud-server.md) | Nextcloud ofrece WebDAV, uno de los destinos de sincronización de datos de SiYuan (combinación por arquitectura). | Crea una carpeta WebDAV en Nextcloud; después configúrala como sincronización en SiYuan. |
| [Claude Code](claude-code.md) | El proyecto se presenta como espacio de trabajo con agentes (tema MCP en GitHub); un agente puede trabajar con sus documentos mediante la API del núcleo (combinación por arquitectura) [DATO NO VERIFICADO: integración MCP concreta]. | SiYuan en marcha con token de API; después configura el acceso del agente. |

**Notas:** Alternativas (elige una): joplin, trilium, logseq.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.8.10 (2026-11-10) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/siyuan-note/siyuan/blob/master/README.md) · [2](https://b3log.org/siyuan)</sub>

## Ver similares

Grupo **Notas y bases de conocimiento personales**: SiYuan ocupa la posición 1 de 4 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **SiYuan** (esta ficha) ⭐ recomendado | 79 | Si quieres bloques referenciables y una base de conocimiento local muy completa. |
| 2 | [Trilium Notes](trilium.md) | 64 | Si quieres jerarquías profundas de notas con scripting y servidor propio. |
| 3 | [Logseq](logseq.md) | 59 | Si piensas en esquemas y grafos con notas diarias, local-first. |
| 4 | [Joplin](joplin.md) | 57 | Si quieres notas Markdown con sincronización cifrada en todos tus dispositivos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica y las funciones de IA se configuran por separado; activar un proveedor puede añadir credenciales y consumo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | El coste depende del proveedor o la ruta. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
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
docker run -d -v workspace_dir_host:workspace_dir_container -p 6806:6806 -e PUID=1001 -e PGID=1002 b3log/siyuan serve --workspace=workspace_dir_container --accessAuthCode="${AuthCode:?Set AuthCode}"
```

Comando copiado literalmente de el README (sección «Entrypoint»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/siyuan-note/siyuan/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SiYuan para mi objetivo y necesito pasos guiados. Lee https://github.com/siyuan-note/siyuan/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala la app de escritorio o la imagen Docker (`b3log/siyuan serve`), crea dos documentos y enlaza un bloque de uno en el otro..

**Qué comprobar:** La referencia bidireccional aparece en ambos documentos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- construir una base de conocimiento personal con referencias entre bloques
- autoalojar un espacio de notas accesible desde el navegador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: construir una base de conocimiento personal con referencias entre bloques; autoalojar un espacio de notas accesible desde el navegador | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile
- **Etiquetas:** `notas` `typescript` `self-hosted` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Joplin](joplin.md) | 57.2k | App de notas y tareas centrada en la privacidad, offline first, con sincronización cifrada de extremo a extremo y apps para escritorio y móvil. |
| [Trilium Notes](trilium.md) | 39k | App de notas jerárquicas para bases de conocimiento grandes: clonado de notas, scripts, relaciones, mapas y servidor de sincronización autoalojado. |
| [Logseq](logseq.md) | 45.6k | Plataforma de gestión del conocimiento local-first en forma de esquema, con páginas enlazadas, diario, consultas y grafo, en Markdown u Org. |

## Enlaces

- 🐙 GitHub: [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan)
- 🌐 Web: <https://b3log.org/siyuan>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/siyuan-note/siyuan/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
