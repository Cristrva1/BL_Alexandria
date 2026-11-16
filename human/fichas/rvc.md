[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🗣️ RVC WebUI

> Interfaz y herramientas para convertir una grabación a otra voz mediante modelos locales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.3k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

RVC (Retrieval-based Voice Conversion WebUI), framework para convertir el timbre de voz, de RVC-Project. Licencia MIT. Es muy popular (~39k estrellas, 2.3.260718); el README principal está en chino.

## ¿Qué hace?

Convierte una grabación a otra voz con modelos entrenados con poco audio, usando recuperación de características para reducir la fuga de timbre. Incluye entrenamiento, inferencia, separación de voz y conversión en tiempo real.

## ¿Cómo lo hace?

Esta rama apunta a Python 3.12 x64 (se recomienda Ubuntu 24.04) y se instala con pip y requirements por plataforma (CPU, CUDA y otros).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [GPT-SoVITS](gpt-sovits.md) | TTS del mismo ecosistema. | Genera voz con GPT-SoVITS y conviértela con RVC. |
| [FFmpeg](ffmpeg.md) | Preparación de audio. (combinación por arquitectura) | Convierte el audio de entrada. |
| [OBS Studio](obs-studio.md) | Cambiador de voz en tiempo real para streaming. (combinación por arquitectura) | Enruta el audio a OBS. |

**Notas:** Sin alternativas declaradas. Riesgo de suplantación de voz.

Estado en GitHub: activo · último push 2026-08-04 · última versión publicada 2.3.260718 (2026-07-21) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere API en la ruta propia; entrenamiento, hardware y modelos externos se costean aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. RVC convierte audio existente y no es por sí solo texto a voz; menos de diez minutos es un reclamo de entrenamiento y no una garantía universal |
| Coste | Sin pago a un modelo en la ruta básica. No requiere API en la ruta propia; entrenamiento, hardware y modelos externos se costean aparte |
| Equipo | Preparación según la ruta elegida. Python 3.12 según guía; FFmpeg; modelo de conversión; voz autorizada; equipo |

RVC convierte audio existente y no es por sí solo texto a voz; menos de diez minutos es un reclamo de entrenamiento y no una garantía universal

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.12 según guía
- FFmpeg
- modelo de conversión
- voz autorizada
- equipo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (powershell):**

```
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar RVC WebUI para mi objetivo y necesito pasos guiados. Lee https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte un clip propio corto y compara claridad, tono y artefactos.

**Qué comprobar:** Puedes reconocer entrada y voz objetivo del modelo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un efecto de voz consentido
- Estudiar conversión frente a TTS

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un efecto de voz consentido; Estudiar conversión frente a TTS | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** RVC convierte audio existente y no es por sí solo texto a voz; menos de diez minutos es un reclamo de entrenamiento y no una garantía universal

## Stack y modelos

- **Stack:** Python 3.12 según guía; FFmpeg; modelo de conversión; voz autorizada; equipo
- **Etiquetas:** `audio` `tts` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [RVC-Project/Retrieval-based-Voice-Conversion-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
