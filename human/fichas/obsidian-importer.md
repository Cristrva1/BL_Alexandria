[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 🖥️ obsidian-importer

> Plugin oficial para convertir datos de otras aplicaciones en archivos Markdown que puedes abrir en Obsidian.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.8k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plugin oficial de Obsidian para importar notas desde otras apps y formatos. Licencia MIT. Es activo (~2k estrellas, 3.2.0).

## ¿Qué hace?

Convierte notas a Markdown plano desde Airtable, Apple Journal, Apple Notes, Bear, Evernote, Google Keep, Logseq, Microsoft OneNote, Notion, Roam Research, Samsung Notes, Tomboy y archivos CSV, HTML, Markdown o Textbundle. Cada formato tiene una guía en la ayuda oficial. Así se puede migrar a Obsidian sin depender del formato original.

## ¿Cómo lo hace?

Se instala desde Plugins de la comunidad (Importer). Es TypeScript y se compila con npm para desarrollo. Algunas fuentes requieren exportar primero desde la app de origen o iniciar sesión, según la guía.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [obsidian-help](obsidian-help.md) | Guías de importación oficiales por formato. | Lee la guía de tu app de origen y luego ejecuta el Importer. |
| [Obsidian: distribución y extensiones](obsidian-releases.md) | Se distribuye a través del directorio oficial de plugins de la comunidad. | Instálalo desde el navegador de plugins de Obsidian. |
| [markitdown](markitdown.md) | Convertir a Markdown formatos que el Importer no cubre (DOCX, PPTX, PDF). (combinación por arquitectura) | Convierte con MarkItDown y copia los `.md` al vault. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada 3.2.0 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/obsidianmd/obsidian-importer/blob/master/README.md) · [2](https://obsidian.md/help/import)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere modelo; exportar desde la app original puede tener requisitos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Los comandos npm son para desarrollar el plugin; usa el flujo de instalación de Obsidian para importaciones normales |
| Coste | Sin pago a un modelo en la ruta básica. No requiere modelo; exportar desde la app original puede tener requisitos propios |
| Equipo | Preparación según la ruta elegida. Obsidian; plugin Importer; exportación de prueba del formato admitido |

Los comandos npm son para desarrollar el plugin; usa el flujo de instalación de Obsidian para importaciones normales

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Obsidian
- plugin Importer
- exportación de prueba del formato admitido

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/obsidianmd/obsidian-importer/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar obsidian-importer para mi objetivo y necesito pasos guiados. Lee https://github.com/obsidianmd/obsidian-importer/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Importa dos notas ficticias a una bóveda nueva y revisa enlaces y adjuntos.

**Qué comprobar:** Puedes comparar las notas de origen y destino sin mezclar toda tu colección.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Migrar una muestra desde otra app
- Verificar un formato de exportación antes de migrar

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Migrar una muestra desde otra app; Verificar un formato de exportación antes de migrar | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los comandos npm son para desarrollar el plugin; usa el flujo de instalación de Obsidian para importaciones normales

## Stack y modelos

- **Stack:** Obsidian; plugin Importer; exportación de prueba del formato admitido
- **Etiquetas:** `notas` `app` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [obsidianmd/obsidian-importer](https://github.com/obsidianmd/obsidian-importer)
- 🌐 Web: <https://help.obsidian.md/import>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/obsidianmd/obsidian-importer/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
