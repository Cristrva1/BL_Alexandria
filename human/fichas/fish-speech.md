[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🗣️ Fish Speech

> Herramientas y modelos de voz Fish Audio con licencias Community o Research según variante.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 33.7k | Fish Audio Community License 1.0 (no OSI) | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; requiere programar con él; necesita GPU

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** Fish Audio Community License 1.0 (no OSI). Licencia comunitaria: el uso comercial está limitado según los ingresos anuales del licenciatario. Fuente: [LICENSE](https://github.com/fishaudio/fish-speech/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Fish Speech, herramientas y modelos de voz de Fish Audio. El código y los pesos usan la «Fish Audio Community License»; los pesos S2-Pro usan la Fish Audio Research License (GitHub muestra NOASSERTION). Tiene ~34k estrellas.

## ¿Qué hace?

Genera voz expresiva (risas, llanto, susurros), clona voces a partir de referencias y produce varios hablantes en un mismo texto. Fish Audio ofrece además un servicio comercial.

## ¿Cómo lo hace?

Se instala desde el repo con Python y PyTorch (GPU recomendable), y se usa con WebUI, API o CLI. Fish Audio advierte que actuará ante violaciones de la licencia.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Pipecat](pipecat.md) | TTS en agentes de voz. (combinación por arquitectura) | Integra el servicio o el modelo local. |
| [FFmpeg](ffmpeg.md) | Postproceso de audio. (combinación por arquitectura) | Convierte la salida. |
| [whisperX](whisperx.md) | Transcribir referencias de voz. (combinación por arquitectura) | Genera el texto de referencia. |

**Notas:** Alternativas (elige una): cosyvoice, gpt-sovits. Licencia no OSI: revisa los términos.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v1.5.1 (2025-05-31) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/fishaudio/fish-speech/blob/main/README.md)</sub>

## Ver similares

Grupo **Clonación de voz y TTS multilingüe**: Fish Speech ocupa la posición 4 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [GPT-SoVITS](gpt-sovits.md) ⭐ recomendado | 69 | Si quieres entrenar una voz propia con pocos minutos de audio y una interfaz web. |
| 2 | [F5-TTS](f5-tts.md) | 64 | Si quieres clonación de voz zero-shot con pocos segundos de audio. |
| 3 | [CosyVoice](cosyvoice.md) | 61 | Si necesitas clonación de voz multilingüe de calidad, con soporte fuerte de chino. |
| 4 | **Fish Speech** (esta ficha) | 61 | Si buscas TTS multilingüe con clonación y buena latencia. |
| 5 | [IndexTTS](index-tts.md) | 53 | Si necesitas controlar duración y emoción de la voz sintetizada. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Código y pesos actuales usan Fish Audio Community License; S2-Pro conserva Research License y no se presume uso comercial idéntico |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La disponibilidad del código no equivale a Apache o MIT ni a un servicio API gratuito; sigue la guía de la variante elegida |
| Coste | El coste depende del proveedor o la ruta. Código y pesos actuales usan Fish Audio Community License; S2-Pro conserva Research License y no se presume uso comercial idéntico |
| Equipo | Preparación según la ruta elegida. Entorno y GPU compatibles; modelo con licencia aplicable; texto y voz autorizados |

La disponibilidad del código no equivale a Apache o MIT ni a un servicio API gratuito; sigue la guía de la variante elegida

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno y GPU compatibles
- modelo con licencia aplicable
- texto y voz autorizados

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker run --gpus device=0 -v ./checkpoints:/app/checkpoints -e LLAMA_CHECKPOINT_PATH=checkpoints/drama-3 -p 8080:8080 fishaudio/fish-speech:server-cuda
```

Comando copiado literalmente de la documentación del repositorio (sección «Run the pre-built image»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/fishaudio/fish-speech/blob/main/docs/en/install.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Fish Speech para mi objetivo y necesito pasos guiados. Lee https://github.com/fishaudio/fish-speech/blob/main/docs/en/install.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige Drama 3 o S2-Pro y prueba una frase corta después de revisar sus condiciones.

**Qué comprobar:** Puedes distinguir la variante y su licencia.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar generación expresiva
- Preparar una prueba de voz multilingüe

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar generación expresiva; Preparar una prueba de voz multilingüe | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La disponibilidad del código no equivale a Apache o MIT ni a un servicio API gratuito; sigue la guía de la variante elegida

## Stack y modelos

- **Stack:** Entorno y GPU compatibles; modelo con licencia aplicable; texto y voz autorizados
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [CosyVoice](cosyvoice.md) | 24.4k | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. |
| [GPT-SoVITS](gpt-sovits.md) | 65.1k | Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y requisitos dependen del modelo y datos. |
| [F5-TTS](f5-tts.md) | 15.6k | Síntesis de voz con clonación a partir de pocos segundos de audio de referencia, basada en flow matching con Diffusion Transformer; incluye app Gradio y CLI. |

## Enlaces

- 🐙 GitHub: [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)
- 🌐 Web: <https://speech.fish.audio>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/fishaudio/fish-speech/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
