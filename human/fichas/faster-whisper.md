[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Transcripción (voz a texto)

# ⚡ faster-whisper

> Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.8k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## ¿Qué es?

faster-whisper, reimplementación de Whisper sobre CTranslate2, de SYSTRAN. Licencia MIT. Es madura (~27k estrellas, v1.2.1).

## ¿Qué hace?

Transcribe hasta 4 veces más rápido que openai/whisper con la misma precisión y menos memoria, según el proyecto. Admite cuantización de 8 bits, transcripción por lotes, VAD y modelos distil-whisper.

## ¿Cómo lo hace?

Requiere Python 3.9+ y se instala con `pip install faster-whisper`. En GPU necesita cuBLAS y cuDNN 9 para CUDA 12 (con CUDA 11 hay que fijar ctranslate2 3.24.0).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [whisperX](whisperx.md) | Backend de transcripción de WhisperX. | Instala WhisperX, que lo usa por debajo. |
| [Pipecat](pipecat.md) | STT local en agentes de voz. (combinación por arquitectura) | Usa un servicio STT basado en faster-whisper. |
| [MoviePy](moviepy.md) | Generar subtítulos sobre vídeo. (combinación por arquitectura) | Convierte los segmentos a SRT. |

**Notas:** Alternativas (elige una): whisper-cpp.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v1.2.1 (2025-10-31) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/SYSTRAN/faster-whisper/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Sin API de pago para inferencia propia; hardware y almacenamiento aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Las dependencias CUDA y cuDNN cambian con CTranslate2; el ahorro de memoria y velocidad depende del modelo y parámetros |
| Coste | Sin pago a un modelo en la ruta básica. Sin API de pago para inferencia propia; hardware y almacenamiento aparte |
| Equipo | Preparación según la ruta elegida. Python; CTranslate2; CPU o CUDA/cuDNN compatibles; modelo y audio |

Las dependencias CUDA y cuDNN cambian con CTranslate2; el ahorro de memoria y velocidad depende del modelo y parámetros

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- CTranslate2
- CPU o CUDA/cuDNN compatibles
- modelo y audio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install faster-whisper
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/SYSTRAN/faster-whisper/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar faster-whisper para mi objetivo y necesito pasos guiados. Lee https://github.com/SYSTRAN/faster-whisper/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Transcribe un clip corto con una configuración adecuada al equipo y compara salida y tiempo.

**Qué comprobar:** Puedes revisar modelo, cuantización y resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Transcribir lotes pequeños
- Comparar CPU con GPU

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Transcribir lotes pequeños; Comparar CPU con GPU | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las dependencias CUDA y cuDNN cambian con CTranslate2; el ahorro de memoria y velocidad depende del modelo y parámetros

## Stack y modelos

- **Stack:** Python; CTranslate2; CPU o CUDA/cuDNN compatibles; modelo y audio
- **Etiquetas:** `stt` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper.cpp](whisper-cpp.md) | 55.2k | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. |

## Enlaces

- 🐙 GitHub: [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- 🧪 Receta: [Agente de voz en tiempo real](../playbooks/agente-de-voz.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/SYSTRAN/faster-whisper/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
