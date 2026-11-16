[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Notas, bóvedas y conocimiento personal

# 📚 obsidian-sample-plugin

> Plantilla oficial para programar un plugin de Obsidian con una estructura inicial y configuración de desarrollo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.7k | 0BSD | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 50/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plantilla oficial para crear plugins de Obsidian en TypeScript. Licencia 0BSD. Es estable (~5k estrellas, 1.0.0).

## ¿Qué hace?

Muestra lo básico de la API de plugins: icono en la barra lateral, comando que abre un modal, pestaña de ajustes, eventos globales e intervalos. Sirve como punto de partida que se clona y se adapta. Depende de la API más reciente (`obsidian.d.ts`) con comentarios TSDoc.

## ¿Cómo lo hace?

Se crea un repo desde la plantilla, se clona dentro de `.obsidian/plugins/` de un vault de pruebas, se ejecuta `npm i` y `npm run dev`, y se recarga Obsidian. Requiere Node.js. Para publicar se siguen la guía de envío y las políticas de desarrolladores.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Obsidian: distribución y extensiones](obsidian-releases.md) | Directorio donde se envía el plugin terminado. | Publica una release en GitHub y abre el PR en obsidian-releases. |
| [obsidian-skills](obsidian-skills.md) | La skill `obsidian-cli` incluye desarrollo de plugins y temas con la CLI de Obsidian. | Instala obsidian-skills en el agente antes de pedirle cambios al plugin. |
| [Claude Code](claude-code.md) | Agente para escribir y depurar el plugin a partir de la plantilla. (combinación por arquitectura) | Abre el repo del plugin con el agente. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-08-02 · última versión publicada 1.0.0 (2020-10-28) · licencia declarada 0BSD (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/obsidianmd/obsidian-sample-plugin/blob/master/README.md) · [2](https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin) · [3](https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La plantilla no usa LLM; publicar y mantener un plugin requiere trabajo y dependencias propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una plantilla para desarrolladores; no ofrece una función de usuario final con solo instalarla como plugin |
| Coste | Sin pago a un modelo en la ruta básica. La plantilla no usa LLM; publicar y mantener un plugin requiere trabajo y dependencias propias |
| Equipo | Preparación según la ruta elegida. Node; TypeScript; Git; Obsidian con bóveda de desarrollo |

Es una plantilla para desarrolladores; no ofrece una función de usuario final con solo instalarla como plugin

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- TypeScript
- Git
- Obsidian con bóveda de desarrollo

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/obsidianmd/obsidian-sample-plugin/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar obsidian-sample-plugin para mi objetivo y necesito pasos guiados. Lee https://github.com/obsidianmd/obsidian-sample-plugin/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Copia la plantilla a un proyecto propio y añade un comando que muestre un mensaje ficticio.

**Qué comprobar:** El comando aparece y funciona en la bóveda de desarrollo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender a programar un plugin
- Prototipar una función para notas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender a programar un plugin; Prototipar una función para notas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una plantilla para desarrolladores; no ofrece una función de usuario final con solo instalarla como plugin

## Stack y modelos

- **Stack:** Node; TypeScript; Git; Obsidian con bóveda de desarrollo
- **Etiquetas:** `notas` `template` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [obsidianmd/obsidian-sample-plugin](https://github.com/obsidianmd/obsidian-sample-plugin)
- 🌐 Web: <https://docs.obsidian.md>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/obsidianmd/obsidian-sample-plugin/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
