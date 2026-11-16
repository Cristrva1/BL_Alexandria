[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Procesamiento y limpieza de audio

# 🖥️ Ultimate Vocal Remover (UVR)

> Aplicación de escritorio para separar voz e instrumentos de canciones con modelos de IA (MDX-Net, VR, Demucs), sin necesidad de programar.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.2k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Aplicación de código abierto (MIT) de Anjok07 y aufr33, referencia popular para separar voces. La última versión publicada es la v5.6 (2023); el README remite a una actualización de desarrollo de octubre de 2026.

## ¿Qué hace?

Separa pistas de audio en voz e instrumental (y en stems como batería o bajo con Demucs) usando modelos entrenados por sus desarrolladores (MDX-Net, VR Architecture) y modelos Demucs. Permite procesar por lotes, encadenar modelos (ensembles) y cambiar tempo o tono.

## ¿Cómo lo hace?

Se distribuye como instalador para Windows y macOS que incluye Python y PyTorch; en Linux se instala desde el código. Usa FFmpeg para formatos distintos de WAV y Rubber Band para cambios de tiempo y tono. Funciona en CPU; la GPU (CUDA o Apple Silicon) acelera.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | UVR necesita FFmpeg para procesar archivos que no son WAV. | Instala FFmpeg (o copia el binario a la carpeta de UVR); después abre MP3 u otros formatos. |
| [rubberband](rubberband.md) | UVR usa Rubber Band para las funciones de cambio de tiempo y de tono. | Instala Rubber Band según el README; después usa las herramientas de tempo y tono. |
| [Demucs](demucs.md) | UVR incluye los modelos Demucs v3 y v4 como una de sus arquitecturas de separación. | Descarga los modelos Demucs desde el gestor de modelos de UVR; después elige el método Demucs. |

Estado en GitHub: activo · último push 2026-10-06 · última versión publicada v5.6 (2023-09-26) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Anjok07/ultimatevocalremovergui/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. |
| Equipo | Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y una copia de datos o archivos para la primera prueba.

1. Abre las descargas o la web de la aplicación enlazadas por el autor; elige la versión para tu sistema.
2. Sigue su guía de inicio y configura únicamente la función que necesitas probar.
3. Abre un archivo o caso pequeño, guarda un resultado y comprueba que puedes recuperarlo antes de importar material real.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Anjok07/ultimatevocalremovergui/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/Anjok07/ultimatevocalremovergui/releases)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Ultimate Vocal Remover (UVR) para mi objetivo y necesito pasos guiados. Lee https://github.com/Anjok07/ultimatevocalremovergui/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga el instalador para tu sistema desde las releases, abre una canción y separa con un modelo MDX-Net..

**Qué comprobar:** Obtienes dos archivos: voz e instrumental..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- obtener la pista instrumental o la voz aislada de una canción propia
- preparar stems para remezclar o practicar con una canción

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: obtener la pista instrumental o la voz aislada de una canción propia; preparar stems para remezclar o practicar con una canción | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Separar y redistribuir pistas de música ajena puede infringir derechos de autor. La última versión publicada es la v5.6 (septiembre de 2023).

## Stack y modelos

- **Stack:** Python, requirements.txt
- **Etiquetas:** `audio` `music` `separation` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Anjok07/ultimatevocalremovergui](https://github.com/Anjok07/ultimatevocalremovergui)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Anjok07/ultimatevocalremovergui/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
