[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🗣️ IndexTTS

> Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.1k | bilibili Model Use License | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** bilibili Model Use License. Licencia de uso del modelo, no OSI. Fuente: [LICENSE](https://github.com/index-tts/index-tts/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

IndexTTS, sistema de TTS zero-shot «de nivel industrial» con control de duración y emoción, de bilibili (organización index-tts). Usa el «bilibili Model Use License Agreement» propio (GitHub muestra NOASSERTION). Tiene ~25k estrellas (v2.5.0).

## ¿Qué hace?

Clona una voz a partir de una sola muestra y permite controlar la duración exacta y la emoción, incluso con texto descriptivo de la emoción mediante un módulo basado en Qwen (`use_qwen_emo`).

## ¿Cómo lo hace?

Se instala con uv a partir del repo; los modelos se descargan al iniciar la WebUI por primera vez, sin necesidad de Git LFS. Se recomienda GPU NVIDIA.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [whisperX](whisperx.md) | Transcribir y alinear las referencias de voz. (combinación por arquitectura) | Prepara las muestras. |
| [FFmpeg](ffmpeg.md) | Preparar y convertir audio. (combinación por arquitectura) | Normaliza las muestras. |
| [Pipecat](pipecat.md) | TTS en agentes de voz. (combinación por arquitectura) | Expón el modelo como servicio TTS. |

**Notas:** Alternativas (elige una): cosyvoice. Licencia no OSI; riesgo de suplantación de voz.

Estado en GitHub: activo · último push 2026-09-29 · última versión publicada v2.5.0 (2026-08-13) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/index-tts/index-tts/blob/main/README.md)</sub>

## Ver similares

Grupo **Clonación de voz y TTS multilingüe**: IndexTTS ocupa la posición 5 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [GPT-SoVITS](gpt-sovits.md) ⭐ recomendado | 72 | Si quieres entrenar una voz propia con pocos minutos de audio y una interfaz web. |
| 2 | [F5-TTS](f5-tts.md) | 63 | Si quieres clonación de voz zero-shot con pocos segundos de audio. |
| 3 | [CosyVoice](cosyvoice.md) | 61 | Si necesitas clonación de voz multilingüe de calidad, con soporte fuerte de chino. |
| 4 | [Fish Speech](fish-speech.md) | 61 | Si buscas TTS multilingüe con clonación y buena latencia. |
| 5 | **IndexTTS** (esta ficha) | 56 | Si necesitas controlar duración y emoción de la voz sintetizada. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Ejecución propia sin API obligatoria; aplica bilibili Model Use License Agreement y hardware independiente |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Industrial-level es una descripción del autor y no una certificación; algunos controles emocionales requieren activar el módulo específico |
| Coste | El coste depende del proveedor o la ruta. Ejecución propia sin API obligatoria; aplica bilibili Model Use License Agreement y hardware independiente |
| Equipo | Preparación según la ruta elegida. uv; entorno compatible; pesos; GPU según configuración; audio autorizado |

Industrial-level es una descripción del autor y no una certificación; algunos controles emocionales requieren activar el módulo específico

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv
- entorno compatible
- pesos
- GPU según configuración
- audio autorizado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/index-tts/index-tts.git && cd index-tts

pip install -U uv  # or see the link above for other install methods
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/index-tts/index-tts/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar IndexTTS para mi objetivo y necesito pasos guiados. Lee https://github.com/index-tts/index-tts/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sintetiza una frase con duración acotada y comprueba pronunciación y tiempo real obtenido.

**Qué comprobar:** Puedes identificar controles que afectaron al resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar narración con duración controlada
- Estudiar expresión de voz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar narración con duración controlada; Estudiar expresión de voz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Industrial-level es una descripción del autor y no una certificación; algunos controles emocionales requieren activar el módulo específico

## Stack y modelos

- **Stack:** uv; entorno compatible; pesos; GPU según configuración; audio autorizado
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [CosyVoice](cosyvoice.md) | 24.4k | Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. |

## Enlaces

- 🐙 GitHub: [index-tts/index-tts](https://github.com/index-tts/index-tts)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/index-tts/index-tts/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
