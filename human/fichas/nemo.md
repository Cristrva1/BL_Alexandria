[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Transcripción (voz a texto)

# 🎙️ NeMo Speech

> Framework actual de NVIDIA para reconocimiento,síntesis y modelos de voz con recetas de inferencia y entrenamiento.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.8k | Apache-2.0 | Python | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Ejecución propia sin API obligatoria; GPU, pesos y datasets tienen condiciones independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El repositorio actual es NeMo Speech; las guías nightly y 3.0 estable son distintas y deben alinearse con la versión instalada |
| Coste | Sin pago a un modelo en la ruta básica. Ejecución propia sin API obligatoria; GPU, pesos y datasets tienen condiciones independientes |
| Equipo | Preparación según la ruta elegida. uv; entorno CUDA compatible; modelo de voz elegido; audio de prueba |

El repositorio actual es NeMo Speech; las guías nightly y 3.0 estable son distintas y deben alinearse con la versión instalada

## Qué puedes hacer con él

Framework actual de NVIDIA para reconocimiento,síntesis y modelos de voz con recetas de inferencia y entrenamiento.

## Por qué destaca

Usos propuestos: Estudiar modelos de voz de NVIDIA; Preparar un experimento ASR.

## Cómo funciona

El repositorio actual es NeMo Speech; las guías nightly y 3.0 estable son distintas y deben alinearse con la versión instalada

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv
- entorno CUDA compatible
- modelo de voz elegido
- audio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/NVIDIA-NeMo/Speech.git
cd Speech
uv sync --extra all --extra cu13     # CUDA 13.x (recommended) — use --extra cu12 for CUDA 12.x
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/NVIDIA-NeMo/Speech/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar NeMo Speech para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA-NeMo/Speech/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige la receta de transcripción y prueba un clip breve antes de entrenar.

**Qué comprobar:** Puedes identificar checkpoint, configuración y salida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar modelos de voz de NVIDIA
- Preparar un experimento ASR

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar modelos de voz de NVIDIA; Preparar un experimento ASR | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El repositorio actual es NeMo Speech; las guías nightly y 3.0 estable son distintas y deben alinearse con la versión instalada

## Stack y modelos

- **Stack:** uv; entorno CUDA compatible; modelo de voz elegido; audio de prueba
- **Etiquetas:** `stt` `tts` `audio` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pipecat](pipecat.md) | 17.3k | Framework open source para agentes de voz y apps multimodales en tiempo real. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisperX](whisperx.md) | 25.3k | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. |

## Enlaces

- 🐙 GitHub: [NVIDIA-NeMo/Speech](https://github.com/NVIDIA-NeMo/Speech)
- 🌐 Web: <https://docs.nvidia.com/nemo/speech/nightly/index.html>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NVIDIA-NeMo/Speech/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
