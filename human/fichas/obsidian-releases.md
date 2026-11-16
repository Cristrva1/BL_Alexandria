[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 🖥️ Obsidian: distribución y extensiones

> Repositorio de distribución de Obsidian y sus listados de plugins y temas; no contiene el código completo de la aplicación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.3k | — | — | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Repositorio de Obsidian para las releases públicas de la app y los directorios de plugins y temas de la comunidad. No tiene archivo de licencia y no contiene el código de Obsidian, que no es open source. Es muy activo (~23k estrellas, v1.15.1).

## ¿Qué hace?

Aloja los instaladores de Obsidian y los archivos JSON de los directorios de plugins y temas de la comunidad que la app consulta. Es donde los desarrolladores envían por pull request sus plugins y temas para que aparezcan en Obsidian. No acepta issues: los problemas de plugins van a sus repos y los de Obsidian, al foro.

## ¿Cómo lo hace?

Los usuarios no lo instalan: la app lee estos directorios. Para publicar un plugin o tema se sigue la guía oficial de envío y las políticas para desarrolladores; `manifest.json` y `versions.json` controlan la compatibilidad con versiones de la app.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [obsidian-sample-plugin](obsidian-sample-plugin.md) | Plantilla oficial para crear un plugin que luego se envía a este directorio. | Crea el plugin desde la plantilla, publica una release y abre el PR aquí. |
| [obsidian-minimal](obsidian-minimal.md) | Ejemplo de tema distribuido mediante este directorio. | Instálalo desde el navegador de temas. |
| [obsidian-importer](obsidian-importer.md) | Ejemplo de plugin oficial distribuido mediante este directorio. | Instálalo desde el navegador de plugins. |

**Notas:** Sin alternativas declaradas. Obsidian no es open source; este repo es solo distribución.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.15.1 (2026-11-12) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/obsidianmd/obsidian-releases/blob/master/README.md) · [2](https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin) · [3](https://docs.obsidian.md/Developer+policies)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La lista no usa IA; Obsidian y complementos o servicios pueden tener planes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Este repositorio distribuye releases y catálogos; no contiene el código completo de Obsidian ni todos los plugins listados |
| Coste | El coste depende del proveedor o la ruta. La lista no usa IA; Obsidian y complementos o servicios pueden tener planes propios |
| Equipo | Preparación según la ruta elegida. Navegador; instalador Obsidian compatible |

Este repositorio distribuye releases y catálogos; no contiene el código completo de Obsidian ni todos los plugins listados

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- instalador Obsidian compatible

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/obsidianmd/obsidian-releases/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Obsidian: distribución y extensiones para mi objetivo y necesito pasos guiados. Lee https://github.com/obsidianmd/obsidian-releases/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Identifica una release oficial y revisa compatibilidad de un plugin antes de usarlo.

**Qué comprobar:** Puedes reconocer versión de app y versión mínima del complemento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Encontrar una distribución oficial
- Estudiar el catálogo de temas y plugins

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Encontrar una distribución oficial; Estudiar el catálogo de temas y plugins | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Este repositorio distribuye releases y catálogos; no contiene el código completo de Obsidian ni todos los plugins listados

## Stack y modelos

- **Stack:** Navegador; instalador Obsidian compatible
- **Etiquetas:** `notas` `app` `reference`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [obsidianmd/obsidian-releases](https://github.com/obsidianmd/obsidian-releases)
- 🌐 Web: <https://obsidian.md>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/obsidianmd/obsidian-releases/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
