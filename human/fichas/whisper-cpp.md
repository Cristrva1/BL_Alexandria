[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Transcripción (voz a texto)

# 🎙️ whisper.cpp

> Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 55.2k | MIT | C++ | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## ¿Qué es?

whisper.cpp, implementación en C/C++ sin dependencias del modelo de reconocimiento de voz Whisper de OpenAI, de ggml-org. Licencia MIT. Es muy madura (~55k estrellas, v1.9.5).

## ¿Qué hace?

Transcribe y traduce audio en local con alto rendimiento en CPU y GPU, incluido streaming en tiempo real. Ofrece servidor HTTP, ejemplos y bindings para muchos lenguajes.

## ¿Cómo lo hace?

Se compila con CMake o make y se descargan modelos ggml (por ejemplo `make -j large-v3-turbo`). Soporta Apple Silicon (Metal, Core ML), CUDA, Vulkan y otros backends; el audio debe estar en WAV de 16 kHz.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Convertir audio a WAV de 16 kHz. | Convierte el audio con FFmpeg antes. |
| [llama.cpp](llama-cpp.md) | Mismo ecosistema ggml: voz a texto y luego LLM local. (combinación por arquitectura) | Encadena la transcripción con llama.cpp. |
| [Pipecat](pipecat.md) | STT local en agentes de voz. (combinación por arquitectura) | Expón el servidor de whisper.cpp al pipeline. |

**Notas:** Alternativas (elige una): faster-whisper, whisper.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v1.9.5 (2026-10-06) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ggml-org/whisper.cpp/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Modelo local sin API de pago; hardware y energía independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Clonar es solo el comienzo: sigue compilación, descarga del modelo y formato de audio; no necesitas instalar todas las aceleraciones del README |
| Coste | Sin pago a un modelo en la ruta básica. Modelo local sin API de pago; hardware y energía independientes |
| Equipo | Preparación según la ruta elegida. Compilador y CMake según sistema; modelo Whisper; audio corto compatible |

Clonar es solo el comienzo: sigue compilación, descarga del modelo y formato de audio; no necesitas instalar todas las aceleraciones del README

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Compilador y CMake según sistema
- modelo Whisper
- audio corto compatible

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/ggml-org/whisper.cpp.git
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ggml-org/whisper.cpp/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar whisper.cpp para mi objetivo y necesito pasos guiados. Lee https://github.com/ggml-org/whisper.cpp/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Transcribe una grabación propia corta y compara nombres y números con el audio.

**Qué comprobar:** Puedes identificar modelo y errores de transcripción.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Transcribir una nota offline
- Preparar texto base para subtítulos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Transcribir una nota offline; Preparar texto base para subtítulos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Clonar es solo el comienzo: sigue compilación, descarga del modelo y formato de audio; no necesitas instalar todas las aceleraciones del README

## Stack y modelos

- **Stack:** Compilador y CMake según sistema; modelo Whisper; audio corto compatible
- **Etiquetas:** `stt` `audio` `local` `cpp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [faster-whisper](faster-whisper.md) | 26.8k | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. |
| [whisper](whisper.md) | 113k | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. |

## Enlaces

- 🐙 GitHub: [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ggml-org/whisper.cpp/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
