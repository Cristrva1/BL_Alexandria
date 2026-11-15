[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# ✂️ VideoLingo

> App para reconocer voz, traducir subtítulos y preparar doblaje, con ASR local por defecto y proveedores configurables por etapa.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.3k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. ASR local y algunos TTS no requieren API; traducción y servicios de voz dependen del proveedor; cada etapa puede consumir por separado |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El reconocimiento local actual usa Qwen3-ASR y ForcedAligner por defecto; no se debe seguir describiendo todo el pipeline como WhisperX |
| Coste | El coste depende del proveedor o la ruta. ASR local y algunos TTS no requieren API; traducción y servicios de voz dependen del proveedor; cada etapa puede consumir por separado |
| Equipo | Preparación según la ruta elegida. Python y uv; FFmpeg y modelos según ruta; LLM con salida JSON; video propio |

El reconocimiento local actual usa Qwen3-ASR y ForcedAligner por defecto; no se debe seguir describiendo todo el pipeline como WhisperX

## Qué puedes hacer con él

Combina reconocimiento de voz, alineación, traducción, segmentación y doblaje. La ruta revisada utiliza Qwen3-ASR y ForcedAligner localmente por defecto; traducción y TTS tienen requisitos y costes distintos según proveedor.

## Por qué destaca

Usos propuestos: Subtitular un tutorial propio; Preparar una traducción de una demostración.

## Cómo funciona

El reconocimiento local actual usa Qwen3-ASR y ForcedAligner por defecto; no se debe seguir describiendo todo el pipeline como WhisperX

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- FFmpeg y modelos según ruta
- LLM con salida JSON
- video propio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/Huanshere/VideoLingo.git && cd VideoLingo
uv run start.py
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Huanshere/VideoLingo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar VideoLingo para mi objetivo y necesito pasos guiados. Lee https://github.com/Huanshere/VideoLingo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Procesa un clip corto con voz clara y revisa transcripción, traducción y tiempos antes de doblar.

**Qué comprobar:** Los subtítulos coinciden con las palabras y puedes corregir errores antes de exportar.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Subtitular un tutorial propio
- Preparar una traducción de una demostración

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Subtitular un tutorial propio; Preparar una traducción de una demostración | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El reconocimiento local actual usa Qwen3-ASR y ForcedAligner por defecto; no se debe seguir describiendo todo el pipeline como WhisperX

## Stack y modelos

- **Stack:** Python y uv; FFmpeg y modelos según ruta; LLM con salida JSON; video propio
- **Etiquetas:** `video` `stt` `tts` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [yt-dlp](yt-dlp.md) | 208k | Descargador de audio y video por línea de comandos compatible con miles de sitios. |
| [GPT-SoVITS](gpt-sovits.md) | 65.1k | Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y requisitos dependen del modelo y datos. |
| [whisperX](whisperx.md) | 25.3k | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [VoiceStudio](omnivoice-studio.md) | 111k | App local de voz con modelos descargables,edición AGPL y una oferta comercial separada. |

## Enlaces

- 🐙 GitHub: [Huanshere/VideoLingo](https://github.com/Huanshere/VideoLingo)
- 🌐 Web: <https://docs.videolingo.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Huanshere/VideoLingo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
