[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🗣️ CosyVoice

> Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24.4k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

CosyVoice, modelo de voz multilingüe del equipo Qwen/FunAudioLLM de Alibaba, con inferencia, entrenamiento y despliegue. Licencia Apache-2.0. Tiene ~24k estrellas, la versión actual es Fun-CosyVoice 3.0 y el repo no cambia desde mayo de 2026.

## ¿Qué hace?

Genera voz y clona voces zero-shot entre idiomas, con streaming de baja latencia y control por instrucciones.

## ¿Cómo lo hace?

Se instala con conda y `pip install -r requirements.txt` (los ejemplos usan espejos de Aliyun); ttsfrd es opcional para normalizar texto. Puede acelerarse con vLLM (0.9 o 0.11 con versiones fijadas de transformers) y desplegarse con Docker, gRPC o FastAPI. Los modelos están en ModelScope y Hugging Face.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Pipecat](pipecat.md) | TTS en agentes de voz. (combinación por arquitectura) | Expón el servidor FastAPI o gRPC. |
| [vLLM](vllm.md) | Inferencia acelerada documentada. | Instala la versión de vLLM indicada. |
| [FFmpeg](ffmpeg.md) | Postproceso de audio. (combinación por arquitectura) | Convierte la salida. |

**Notas:** Alternativas (elige una): fish-speech, index-tts.

Estado en GitHub: activo · último push 2026-05-25 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ruta propia no necesita API; hardware, datos y modelos externos tienen sus condiciones |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto pertenece a FunAudioLLM; variantes de vLLM requieren entornos específicos y no conviene mezclar todas las dependencias en uno |
| Coste | Sin pago a un modelo en la ruta básica. La ruta propia no necesita API; hardware, datos y modelos externos tienen sus condiciones |
| Equipo | Preparación según la ruta elegida. Conda y Python 3.10 según guía; submódulos; pesos; FFmpeg o sox según ruta |

El proyecto pertenece a FunAudioLLM; variantes de vLLM requieren entornos específicos y no conviene mezclar todas las dependencias en uno

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Conda y Python 3.10 según guía
- submódulos
- pesos
- FFmpeg o sox según ruta

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
    # If you failed to clone the submodule due to network failures, please run the following command until success
    cd CosyVoice
    git submodule update --init --recursive
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar CosyVoice para mi objetivo y necesito pasos guiados. Lee https://github.com/QwenAudio/CosyVoice/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga una variante compatible y prueba una frase del idioma elegido.

**Qué comprobar:** Puedes comprobar voz, texto y archivo generado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar síntesis multilingüe
- Estudiar streaming de voz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar síntesis multilingüe; Estudiar streaming de voz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El proyecto pertenece a FunAudioLLM; variantes de vLLM requieren entornos específicos y no conviene mezclar todas las dependencias en uno

## Stack y modelos

- **Stack:** Conda y Python 3.10 según guía; submódulos; pesos; FFmpeg o sox según ruta
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Fish Speech](fish-speech.md) | 33.7k | Herramientas y modelos de voz Fish Audio con licencias Community o Research según variante. |
| [IndexTTS](index-tts.md) | 25.1k | Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción. |

## Enlaces

- 🐙 GitHub: [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice)
- 🌐 Web: <https://funaudiollm.github.io/cosyvoice3>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/QwenAudio/CosyVoice/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
