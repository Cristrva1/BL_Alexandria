[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 AI-Youtube-Shorts-Generator

> Pipeline de Python que extrae clips verticales de videos de YouTube mediante transcripción y selección de momentos con LLM.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.1k | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere clave de API

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

AI YouTube Shorts Generator, pipeline en Python para extraer clips verticales de vídeos largos de YouTube, de @Anil-matcha. Licencia MIT. Tiene ~6k estrellas (sin releases) y lo «impulsa» MuAPI, cuyas APIs de pago se promocionan en el README.

## ¿Qué hace?

Descarga el vídeo, lo transcribe con Whisper, detecta los momentos más «virales» con un LLM, recorta en 9:16 con seguimiento de caras y genera shorts ordenados por puntuación. Se presenta como alternativa a Opus Clip, Vidyo.ai o SubMagic.

## ¿Cómo lo hace?

Tiene dos modos: `--mode api` usa MuAPI para descarga, transcripción y recorte (de pago), y `--mode local` funciona sin conexión con yt-dlp, faster-whisper y OpenCV. Se instala con `pip install -r requirements.txt` (más `requirements-local.txt` para el modo local).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [faster-whisper](faster-whisper.md) | Transcripción local en el modo offline. | Instala `requirements-local.txt`. |
| [yt-dlp](yt-dlp.md) | Descarga de vídeos en el modo local. | Viene en las dependencias locales. |
| [FFmpeg](ffmpeg.md) | Corte y codificación de los clips. | Instala FFmpeg en el sistema. |

**Notas:** Sin alternativas declaradas. Respeta los derechos de autor y los términos de YouTube al reutilizar vídeos ajenos.

Estado en GitHub: activo · último push 2026-11-12 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. El modo API usa MuAPI; el modo local procesa medios en tu equipo pero conserva llamadas OpenAI o Gemini para ranking |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Local no significa todo offline; las puntuaciones de viralidad son heurísticas del proyecto y no predicen vistas |
| Coste | El coste depende del proveedor o la ruta. El modo API usa MuAPI; el modo local procesa medios en tu equipo pero conserva llamadas OpenAI o Gemini para ranking |
| Equipo | Preparación según la ruta elegida. Python; FFmpeg y dependencias locales si eliges ese modo; clave LLM; video autorizado |

Local no significa todo offline; las puntuaciones de viralidad son heurísticas del proyecto y no predicen vistas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- FFmpeg y dependencias locales si eliges ese modo
- clave LLM
- video autorizado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator.git
   cd AI-Youtube-Shorts-Generator

pip install -r requirements.txt
   # Only if you plan to use --mode local:
   pip install -r requirements-local.txt
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AI-Youtube-Shorts-Generator para mi objetivo y necesito pasos guiados. Lee https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Procesa un video propio corto y revisa los fragmentos propuestos antes de exportar.

**Qué comprobar:** Puedes corregir puntos de corte, subtítulos y encuadre.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Obtener clips de un tutorial propio
- Comparar criterios de selección de momentos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Obtener clips de un tutorial propio; Comparar criterios de selección de momentos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Local no significa todo offline; las puntuaciones de viralidad son heurísticas del proyecto y no predicen vistas

## Stack y modelos

- **Stack:** Python; FFmpeg y dependencias locales si eliges ese modo; clave LLM; video autorizado
- **Etiquetas:** `generativo` `2short-ai-alternative` `ai-clip-generator` `ai-clipping` `auto-clip` `auto-crop` `highlight-detection` `klap-alternative`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Anil-matcha/AI-Youtube-Shorts-Generator](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator)
- 🌐 Web: <https://www.vadoo.tv/ai-youtube-shorts-generator>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
