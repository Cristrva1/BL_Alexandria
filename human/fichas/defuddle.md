[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 📚 defuddle

> Biblioteca para extraer el contenido principal de una página y convertirlo en texto o Markdown utilizable.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Librería y CLI que extrae el contenido principal de páginas web, de @kepano. Licencia MIT. Es activa (~10k estrellas, 0.19.6) y el propio README avisa de que sigue en desarrollo.

## ¿Qué hace?

Elimina comentarios, barras laterales, cabeceras, pies y otros elementos accesorios, y devuelve HTML limpio o Markdown con metadatos (título, autor, fecha…). Normaliza notas al pie, código y fórmulas para producir una salida consistente. Es el motor de extracción de Obsidian Web Clipper.

## ¿Cómo lo hace?

Se usa con `npx defuddle parse <archivo|url> [--markdown|--json]` o como librería en navegador y Node.js (`npm install defuddle`). Funciona sin modelos de IA.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [obsidian-clipper](obsidian-clipper.md) | El Web Clipper oficial de Obsidian usa Defuddle para extraer contenido. | Instala el Clipper; Defuddle va incluido. |
| [obsidian-skills](obsidian-skills.md) | La skill oficial `defuddle` enseña a los agentes a usarlo para ahorrar tokens. | Instala obsidian-skills en el agente. |
| [crawlee](crawlee.md) | Limpiar el contenido de cada página de un crawler Node.js. (combinación por arquitectura) | Pasa el HTML de cada página a Defuddle. |
| [claude-obsidian](claude-obsidian.md) | Combinación recíproca: claude-obsidian lo enlaza como «Extraer el contenido limpio de páginas web antes de ingerirlas. (combinación por arquitectura)». | Orden indicado desde claude-obsidian: Usa Defuddle (o su skill) para preparar la fuente y déjala en `inbox/`. |
| [Scrapling](scrapling.md) | Combinación recíproca: Scrapling lo enlaza como «Quedarte solo con el contenido principal de los artículos descargados. (combinación por arquitectura)». | Orden indicado desde Scrapling: Pasa el HTML obtenido por Defuddle para limpiarlo. |
| [scrapy](scrapy.md) | Combinación recíproca: scrapy lo enlaza como «Extraer el contenido principal de artículos en un paso posterior. (combinación por arquitectura)». | Orden indicado desde scrapy: Procesa el HTML guardado con Defuddle. |

**Notas:** Sin alternativas declaradas. En desarrollo: la salida puede cambiar entre versiones.

Estado en GitHub: activo · último push 2026-10-25 · última versión publicada 0.19.6 (2026-10-24) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/kepano/defuddle/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La extracción básica no necesita API ni modelo; el contenido y alojamiento son costes externos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Puede perder información en diseños poco habituales; compara una muestra antes de procesar muchas páginas |
| Coste | Sin pago a un modelo en la ruta básica. La extracción básica no necesita API ni modelo; el contenido y alojamiento son costes externos |
| Equipo | Preparación según la ruta elegida. Node.js; archivo HTML de prueba o página pública |

Puede perder información en diseños poco habituales; compara una muestra antes de procesar muchas páginas

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- archivo HTML de prueba o página pública

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm install defuddle
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/kepano/defuddle/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar defuddle para mi objetivo y necesito pasos guiados. Lee https://github.com/kepano/defuddle/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Extrae Markdown de un artículo con menú y comprueba qué texto conserva.

**Qué comprobar:** El resultado prioriza el artículo y elimina navegación irrelevante.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar artículos para lectura
- Limpiar HTML antes de indexarlo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar artículos para lectura; Limpiar HTML antes de indexarlo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Puede perder información en diseños poco habituales; compara una muestra antes de procesar muchas páginas

## Stack y modelos

- **Stack:** Node.js; archivo HTML de prueba o página pública
- **Etiquetas:** `crawlers` `library` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [kepano/defuddle](https://github.com/kepano/defuddle)
- 🌐 Web: <https://defuddle.md>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/kepano/defuddle/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
