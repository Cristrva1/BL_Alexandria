[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🎚️ VoiceStudio

> App local de voz con modelos descargables,edición AGPL y una oferta comercial separada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 111k | AGPL-3.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 76/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

VoiceStudio (antes OmniVoice Studio; repo debpalash/VoiceStudio), estudio de voz con IA que funciona en el dispositivo. La app es AGPL-3.0; los pesos, voces y salidas tienen licencias propias, y hay ediciones Pro y Cloud de pago con licencia comercial. Creado en abril de 2026, tiene ~111k estrellas, una cifra inusual.

## ¿Qué hace?

Clona, diseña, dobla, dicta, transcribe y narra en 646 idiomas, según el proyecto, con modelos descargables desde un gestor de modelos.

## ¿Cómo lo hace?

Se instala con `brew install --cask debpalash/tap/voicestudio`, con los instaladores de escritorio o con Docker. Funciona sin cuenta.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [whisperX](whisperx.md) | Transcripción alineada para doblaje. (combinación por arquitectura) | Prepara transcripciones antes de doblar. |
| [FFmpeg](ffmpeg.md) | Procesado de audio y vídeo. (combinación por arquitectura) | Convierte y monta los resultados. |
| [Kokoro](kokoro.md) | Modelo TTS ligero como alternativa local. (combinación por arquitectura) | Compara la calidad de narración. |

**Notas:** Alternativas (elige una): videolingo. Recuento de estrellas inusual para su edad.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.5.8 (2026-11-12) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/debpalash/VoiceStudio/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La app AGPL puede usarse incluso comercialmente bajo sus términos; existe una edición cerrada comercial y pesos o voces con licencias separadas |
| Claude Code | Referencia para la herramienta; no es una integración |
| Codex | Referencia para la herramienta; no es una integración |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El nombre actual es VoiceStudio; pedir a Claude o Codex ayuda para instalar no es una integración de sus planes ni garantiza igual calidad en todos los idiomas anunciados |
| Coste | El coste depende del proveedor o la ruta. La app AGPL puede usarse incluso comercialmente bajo sus términos; existe una edición cerrada comercial y pesos o voces con licencias separadas |
| Equipo | Preparación según la ruta elegida. Instalador VoiceStudio para tu sistema; modelos; almacenamiento; voces autorizadas |

El nombre actual es VoiceStudio; pedir a Claude o Codex ayuda para instalar no es una integración de sus planes ni garantiza igual calidad en todos los idiomas anunciados

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador VoiceStudio para tu sistema
- modelos
- almacenamiento
- voces autorizadas

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/debpalash/VoiceStudio/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar VoiceStudio para mi objetivo y necesito pasos guiados. Lee https://github.com/debpalash/VoiceStudio/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga un modelo compatible y sintetiza un párrafo propio antes de probar clonación.

**Qué comprobar:** Puedes comprobar modelo, licencia y salida de audio.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una narración local
- Probar transcripción o doblaje de material propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una narración local; Probar transcripción o doblaje de material propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El nombre actual es VoiceStudio; pedir a Claude o Codex ayuda para instalar no es una integración de sus planes ni garantiza igual calidad en todos los idiomas anunciados

## Stack y modelos

- **Stack:** Instalador VoiceStudio para tu sistema; modelos; almacenamiento; voces autorizadas
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [VideoLingo](videolingo.md) | 19.3k | App para reconocer voz, traducir subtítulos y preparar doblaje, con ASR local por defecto y proveedores configurables por etapa. |

## Enlaces

- 🐙 GitHub: [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)
- 🌐 Web: <https://voicestudio.sh>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/debpalash/VoiceStudio/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
