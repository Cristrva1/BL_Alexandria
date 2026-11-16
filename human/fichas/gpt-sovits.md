[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🗣️ GPT-SoVITS

> Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y requisitos dependen del modelo y datos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 65.1k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

GPT-SoVITS, WebUI de TTS y conversión de voz con pocos ejemplos, de @RVC-Boss. Licencia MIT. Es muy popular (~65k estrellas, release 20250606v2pro).

## ¿Qué hace?

Clona una voz con unos segundos (zero-shot) o un minuto de audio (few-shot), con soporte multilingüe e inferencia entre idiomas. Incluye herramientas para preparar datasets: separación de voz, segmentación, ASR y etiquetado.

## ¿Cómo lo hace?

Hay combinaciones probadas de Python 3.9–3.12, PyTorch 2.5–2.8 y CUDA 11.8–12.8; se instala con scripts o paquetes integrados para Windows. La GPU NVIDIA es recomendable.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [RVC WebUI](rvc.md) | Conversión de timbre del mismo autor. | Usa RVC para ajustar la voz generada. |
| [FFmpeg](ffmpeg.md) | Preparación de audio. (combinación por arquitectura) | Convierte el audio de entrenamiento. |
| [whisperX](whisperx.md) | Transcribir el dataset. (combinación por arquitectura) | Genera transcripciones alineadas. |
| [VideoLingo](videolingo.md) | Combinación recíproca: VideoLingo lo enlaza como «Doblaje con voz clonada». | Orden indicado desde VideoLingo: Arranca GPT-SoVITS y selecciónalo como TTS. |

**Notas:** Alternativas (elige una): fish-speech. Riesgo de suplantación de voz: usa voces con consentimiento.

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada 20250606v2pro (2025-06-06) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md)</sub>

## Ver similares

Grupo **Clonación de voz y TTS multilingüe**: GPT-SoVITS ocupa la posición 1 de 5 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **GPT-SoVITS** (esta ficha) ⭐ recomendado | 72 | Si quieres entrenar una voz propia con pocos minutos de audio y una interfaz web. |
| 2 | [F5-TTS](f5-tts.md) | 63 | Si quieres clonación de voz zero-shot con pocos segundos de audio. |
| 3 | [CosyVoice](cosyvoice.md) | 61 | Si necesitas clonación de voz multilingüe de calidad, con soporte fuerte de chino. |
| 4 | [Fish Speech](fish-speech.md) | 61 | Si buscas TTS multilingüe con clonación y buena latencia. |
| 5 | [IndexTTS](index-tts.md) | 56 | Si necesitas controlar duración y emoción de la voz sintetizada. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ruta propia no exige API; GPU, datos y licencias de componentes aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El lema de un minuto describe few-shot y no una garantía de calidad con cualquier grabación o idioma |
| Coste | Sin pago a un modelo en la ruta básica. La ruta propia no exige API; GPU, datos y licencias de componentes aparte |
| Equipo | Preparación según la ruta elegida. Conda; Python 3.10; PyTorch compatible; modelos; audio con permiso; GPU según tarea |

El lema de un minuto describe few-shot y no una garantía de calidad con cualquier grabación o idioma

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Conda
- Python 3.10
- PyTorch compatible
- modelos
- audio con permiso
- GPU según tarea

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
conda create -n GPTSoVits python=3.10
conda activate GPTSoVits

pip install -r extra-req.txt --no-deps
pip install -r requirements.txt
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GPT-SoVITS para mi objetivo y necesito pasos guiados. Lee https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sintetiza una frase corta con una voz autorizada y compara inteligibilidad antes de entrenar.

**Qué comprobar:** Puedes revisar referencia, modelo y resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar una voz para contenido propio
- Estudiar adaptación con pocos ejemplos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar una voz para contenido propio; Estudiar adaptación con pocos ejemplos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El lema de un minuto describe few-shot y no una garantía de calidad con cualquier grabación o idioma

## Stack y modelos

- **Stack:** Conda; Python 3.10; PyTorch compatible; modelos; audio con permiso; GPU según tarea
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Fish Speech](fish-speech.md) | 33.7k | Herramientas y modelos de voz Fish Audio con licencias Community o Research según variante. |

## Enlaces

- 🐙 GitHub: [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
