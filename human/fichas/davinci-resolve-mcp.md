[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ DaVinci Resolve MCP

> Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render.

## Cuándo elegir esta ficha

Presentarlo como integración de una instalación existente de Resolve. Mantener edición manual como punto de entrada y exigir edición/build para prometer scripts. Los editores citados cubren montaje, no las operaciones del servidor.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/samuelgursky/davinci-resolve-mcp/blob/cafc7ad692e768aaeb5d0ea912f24ace08be545b/README.md) · [Fuente 2](https://github.com/samuelgursky/davinci-resolve-mcp/commit/cafc7ad692e768aaeb5d0ea912f24ace08be545b) · [Fuente 3](https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.1k | MIT | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

DaVinci Resolve MCP Server, servidor MCP que permite a asistentes de IA controlar DaVinci Resolve mediante su API oficial de scripting, de @samuelgursky. Licencia MIT. Es activo (~4k estrellas, v5.2.11).

## ¿Qué hace?

Cubre toda la API de scripting y añade ayudas guiadas para montaje, color, medios y renderizado. Incluye un panel de control local en el navegador para inspeccionar el estado de Resolve y analizar clips y planos. En la versión gratuita usa un puente desde el menú de scripts, porque Blackmagic limita el scripting externo a Studio.

## ¿Cómo lo hace?

Se instala con `npx davinci-resolve-mcp setup` o clonando y ejecutando `python install.py` (Python 3.10+). En Studio hay que activar el scripting externo «Local». El instalador y el servidor consultan GitHub para buscar actualizaciones.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Cliente MCP configurado por el instalador. | Ejecuta el setup y elige tu cliente. |
| [FFmpeg](ffmpeg.md) | Preparar o convertir medios antes de importarlos. (combinación por arquitectura) | Normaliza los medios con FFmpeg. |
| [whisper](whisper.md) | Generar subtítulos para importarlos en la línea de tiempo. (combinación por arquitectura) | Transcribe y añade el SRT al proyecto. |

**Notas:** Sin alternativas declaradas. Trabaja sobre copias de proyectos: el agente puede modificar la línea de tiempo.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v5.2.11 (2026-11-14) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El conector no incluye un modelo; Studio tiene licencia propia y la edición gratuita necesita otra ruta; el agente mantiene sus límites |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Studio permite scripting externo Local; la edición gratuita usa un puente interno documentado; instalar MCP no activa por sí solo Resolve |
| Coste | El coste depende del proveedor o la ruta. El conector no incluye un modelo; Studio tiene licencia propia y la edición gratuita necesita otra ruta; el agente mantiene sus límites |
| Equipo | Preparación según la ruta elegida. Resolve >=18.5; Python 64 bits; FFmpeg; Studio o puente interno para edición gratuita |

Studio permite scripting externo Local; la edición gratuita usa un puente interno documentado; instalar MCP no activa por sí solo Resolve

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Resolve >=18.5
- Python 64 bits
- FFmpeg
- Studio o puente interno para edición gratuita

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npx davinci-resolve-mcp setup
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DaVinci Resolve MCP para mi objetivo y necesito pasos guiados. Lee https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En un proyecto de prueba consulta el media pool y añade un marcador antes de automatizar montaje.

**Qué comprobar:** El marcador aparece en el clip o timeline esperado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar material desde un agente
- Preparar ajustes de render con revisión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar material desde un agente; Preparar ajustes de render con revisión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Studio permite scripting externo Local; la edición gratuita usa un puente interno documentado; instalar MCP no activa por sí solo Resolve

## Stack y modelos

- **Stack:** Resolve >=18.5; Python 64 bits; FFmpeg; Studio o puente interno para edición gratuita
- **Etiquetas:** `video` `mcp` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md)
- [Fuente 2](https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/docs/install.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
