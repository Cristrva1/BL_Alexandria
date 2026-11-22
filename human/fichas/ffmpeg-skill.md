[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎨 FFmpeg Skill

> Da a agentes herramientas locales de FFmpeg para recortar, reencuadrar, normalizar audio y exportar video con pasos trazables.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.6k | MIT | Python | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

## ¿Qué es?

Da a agentes herramientas locales de FFmpeg para recortar, reencuadrar, normalizar audio y exportar video con pasos trazables.

## ¿Qué hace?

Da a agentes herramientas locales de FFmpeg para recortar, reencuadrar, normalizar audio y exportar video con pasos trazables.

## ¿Cómo lo hace?

Ejecuta operaciones de video y audio mediante herramientas que convierten parámetros en llamadas a FFmpeg.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Ejecuta las operaciones de video y audio que solicita la skill. | — |

Estado en GitHub: activo · último push 2026-11-22 · última versión publicada v4.7.0 (2026-11-22) · licencia declarada MIT (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/kajisho5/ffmpeg-skill/blob/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883/README.md) · [2](https://github.com/kajisho5/ffmpeg-skill/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El componente se usa dentro del agente. El modelo y los conectores externos se contratan por separado. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. El código o las instrucciones no incluyen el consumo del agente ni de los servicios externos. |
| Equipo | Equipo normal; revisar dependencias. FFmpeg 6.1 o posterior con los codecs y filtros de la operación; entorno del agente para la skill. |

Consume el acceso y los límites del agente donde lo configures. No incluye servicios externos de generación, datos o alojamiento.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- FFmpeg 6.1 o posterior con los codecs y filtros de la operación; entorno del agente para la skill.

1. Instala FFmpeg desde su distribución para tu sistema y revisa en Quick start la comprobación de codecs y la ruta de integración del cliente.
2. Comprueba los filtros, prepara un clip propio y prueba un recorte con un archivo de salida nuevo.
3. Comprueba el resultado: el archivo resultante tiene la duración esperada y el original sigue intacto.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/kajisho5/ffmpeg-skill/blob/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/kajisho5/ffmpeg-skill/blob/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FFmpeg Skill para mi objetivo y necesito pasos guiados. Lee https://github.com/kajisho5/ffmpeg-skill/blob/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Comprueba los filtros, prepara un clip propio y prueba un recorte con un archivo de salida nuevo..

**Qué comprobar:** El archivo resultante tiene la duración esperada y el original sigue intacto..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Recortar un anuncio de prueba a quince segundos.
- Reencuadrar una toma propia para formato vertical.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Recortar un anuncio de prueba a quince segundos.; Reencuadrar una toma propia para formato vertical. | no usas un agente compatible con skills |

**Limitaciones:** FFmpeg no necesita una API de modelo. Subtítulos, plugins y ejecución del agente pueden tener requisitos y cobros aparte. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, package.json
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)
- 🌐 Web: <https://www.npmjs.com/package/ffmpeg-skill>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/kajisho5/ffmpeg-skill/blob/c559cb5fcbfbb37b8a48165b0c49e6bdfa674883/README.md)
- [Fuente 2](https://github.com/kajisho5/ffmpeg-skill/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
