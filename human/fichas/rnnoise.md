[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Procesamiento y limpieza de audio

# 🧩 rnnoise

> Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6k | BSD-3-Clause | C | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Puntuación de calidad** 41/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

RNNoise, biblioteca de supresión de ruido basada en una red neuronal recurrente, de Xiph.Org (algoritmo de Jean-Marc Valin). Licencia BSD-3-Clause. Es madura y estable (~6k estrellas, v0.2) y no cambia desde febrero de 2025.

## ¿Qué hace?

Elimina ruido de voz en tiempo real con un enfoque híbrido DSP más aprendizaje profundo, con muy bajo coste computacional. Se usa en aplicaciones de VoIP y streaming.

## ¿Cómo lo hace?

Se compila con autotools (`./autogen.sh`, `./configure`, `make install`) y se usa como librería C. FFmpeg incluye el filtro `arnndn` basado en sus modelos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Filtro `arnndn` con modelos RNNoise. | Aplica el filtro con un modelo. |
| [OBS Studio](obs-studio.md) | Supresión de ruido en streaming. | Usa el filtro de supresión de ruido RNNoise de OBS. |
| [whisper.cpp](whisper-cpp.md) | Limpiar audio antes de transcribir. (combinación por arquitectura) | Filtra y luego transcribe. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2025-02-22 · última versión publicada v0.2 (2024-04-15) · licencia declarada BSD-3-Clause (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/xiph/rnnoise/blob/main/README)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca no requiere API remota; cómputo y datos propios separados |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La demo recibe y devuelve PCM RAW, no WAV; autogen descarga archivos de modelo y GitHub es una copia de conveniencia del repositorio Xiph |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca no requiere API remota; cómputo y datos propios separados |
| Equipo | Preparación según la ruta elegida. Compilador y autotools; modelo descargado; audio RAW mono 16-bit 48 kHz |

La demo recibe y devuelve PCM RAW, no WAV; autogen descarga archivos de modelo y GitHub es una copia de conveniencia del repositorio Xiph

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Compilador y autotools
- modelo descargado
- audio RAW mono 16-bit 48 kHz

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/xiph/rnnoise/blob/main/README)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar rnnoise para mi objetivo y necesito pasos guiados. Lee https://github.com/xiph/rnnoise/blob/main/README. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Procesa una copia corta de audio con ruido y escucha si mejora sin deformar la voz.

**Qué comprobar:** Puedes comparar original y salida y verificar formato.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Reducir ruido de una grabación
- Estudiar una red de supresión de ruido

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Reducir ruido de una grabación; Estudiar una red de supresión de ruido | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La demo recibe y devuelve PCM RAW, no WAV; autogen descarga archivos de modelo y GitHub es una copia de conveniencia del repositorio Xiph

## Stack y modelos

- **Stack:** Compilador y autotools; modelo descargado; audio RAW mono 16-bit 48 kHz
- **Etiquetas:** `edicion` `model` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [xiph/rnnoise](https://github.com/xiph/rnnoise)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/xiph/rnnoise/blob/main/README)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
