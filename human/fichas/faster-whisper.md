[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Transcripción (voz a texto)

# ⚡ faster-whisper

> Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.8k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

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

## Qué puedes hacer con él

Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización.

## Por qué destaca

Usos propuestos: Transcribir lotes pequeños; Comparar CPU con GPU.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisperX](whisperx.md) | 25.3k | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. |

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
