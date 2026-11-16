[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎞️ video-use

> Edición con agentes y FFmpeg,con transcripción documentada mediante ElevenLabs Scribe.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.1k | MIT | Python | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP); requiere clave de API

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

video-use, edición de vídeo con Claude Code y FFmpeg, de browser-use. Licencia MIT. Creado en abril de 2026, tiene ~31k estrellas y no cambia desde octubre de 2026.

## ¿Qué hace?

Dejas el material en bruto en una carpeta, conversas con el agente y obtienes `final.mp4`: cortes, etalonaje automático (cadenas FFmpeg), subtítulos y montaje para cualquier tipo de contenido.

## ¿Cómo lo hace?

Se instala con `uv sync` o `pip install -e .`, más FFmpeg (obligatorio) y yt-dlp (opcional). La transcripción usa ElevenLabs y requiere su clave de API. Funciona con Claude Code, Codex, Hermes, OpenClaw o cualquier agente con shell.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Motor de edición. | Instala FFmpeg. |
| [Claude Code](claude-code.md) | Agente principal documentado. | Registra la skill en Claude Code. |
| [hermes-agent](hermes-agent.md) | Agente compatible. | Registra la skill en Hermes. |
| [ElevenLabs (SDK de Python)](elevenlabs-python.md) | Combinación recíproca: ElevenLabs (SDK de Python) lo enlaza como «video-use pide una clave de ElevenLabs para la voz; el SDK sirve para elegir y probar voces o generar pistas fuera del flujo. (combinación por arquitectura)». | Orden indicado desde ElevenLabs (SDK de Python): Usa la misma clave en ambos y prueba la voz antes de editar. |

**Notas:** Alternativas (elige una): remotion-superpowers. Depende de ElevenLabs (servicio de pago) para transcribir.

Estado en GitHub: activo · último push 2026-10-08 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/browser-use/video-use/blob/main/README.md)</sub>

## Ver similares

Grupo **Skills y flujos de producción de video**: video-use ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OpenMontage](openmontage.md) ⭐ recomendado | 72 | Si buscas esto: pipelines y herramientas para producir video con un agente,recursos propios,modelos locales o servicios opcionales. |
| 2 | **video-use** (esta ficha) | 60 | Si buscas esto: edición con agentes y FFmpeg,con transcripción documentada mediante ElevenLabs Scribe. |
| 3 | [Remotion Superpowers](remotion-superpowers.md) | 48 | Si buscas esto: orquestación de video con Remotion y servicios audiovisuales externos; requiere claves y revisar costes por etapa. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. El flujo documentado usa ElevenLabs Scribe por fuente y el plan del agente; ejecutar FFmpeg local no elimina ese consumo |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. Documenta Claude Code, Codex y otros agentes con shell; la ruta instalada requiere configurar la transcripción externa y no se debe anunciar como totalmente offline |
| Coste | Consumo de APIs o servicios. El flujo documentado usa ElevenLabs Scribe por fuente y el plan del agente; ejecutar FFmpeg local no elimina ese consumo |
| Equipo | Preparación según la ruta elegida. Agente con shell; Python y uv; FFmpeg; material propio; clave ElevenLabs |

Documenta Claude Code, Codex y otros agentes con shell; la ruta instalada requiere configurar la transcripción externa y no se debe anunciar como totalmente offline

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente con shell
- Python y uv
- FFmpeg
- material propio
- clave ElevenLabs

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/browser-use/video-use/blob/main/install.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar video-use para mi objetivo y necesito pasos guiados. Lee https://github.com/browser-use/video-use/blob/main/install.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Importa un clip corto y revisa transcripción y plan de cortes antes de exportar.

**Qué comprobar:** Puedes contrastar el montaje con el material original.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Editar una entrevista propia
- Seleccionar tomas de un tutorial

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Editar una entrevista propia; Seleccionar tomas de un tutorial | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code, Codex y otros agentes con shell; la ruta instalada requiere configurar la transcripción externa y no se debe anunciar como totalmente offline

## Stack y modelos

- **Stack:** Agente con shell; Python y uv; FFmpeg; material propio; clave ElevenLabs
- **Etiquetas:** `video` `coding-agent` `skills` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Remotion Superpowers](remotion-superpowers.md) | 168 | Orquestación de video con Remotion y servicios audiovisuales externos; requiere claves y revisar costes por etapa. |

## Enlaces

- 🐙 GitHub: [browser-use/video-use](https://github.com/browser-use/video-use)
- 🌐 Web: <https://video-use.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/browser-use/video-use/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
