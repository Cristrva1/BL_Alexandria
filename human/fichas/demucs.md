[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Procesamiento y limpieza de audio

# 📚 Demucs

> Modelo de separación de fuentes musicales (voz, batería, bajo y resto) con Hybrid Transformer; continuación mantenida por su autor tras archivarse el repo de Meta.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.6k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 3 Avanzado — preparación sencilla; requiere programar con él; necesita GPU

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Versión mantenida oficialmente por Alexandre Défossez, autor de Demucs, tras dejar Meta (y archivarse facebookresearch/demucs). El código es MIT. El propio autor avisa de que no trabaja activamente en él: respuestas lentas y sin funciones nuevas.

## ¿Qué hace?

Separa música en stems: batería, bajo, voz y resto (y guitarra y piano con la variante de 6 fuentes). La v4 (Hybrid Transformer Demucs) alcanza 9,0–9,2 dB de SDR en MUSDB HQ. Incluye CLI, API de Python y scripts de entrenamiento.

## ¿Cómo lo hace?

Usa una arquitectura U-Net híbrida en espectrograma y forma de onda con un codificador Transformer entre dominios. Se instala con pip sobre PyTorch; FFmpeg es opcional pero necesario para salida FLAC y algunos formatos. Funciona en CPU o GPU.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Demucs usa FFmpeg para leer formatos de audio adicionales y para exportar en FLAC. | Instala FFmpeg; después ejecuta `demucs --flac cancion.mp3`. |
| [PyTorch](pytorch.md) | Demucs se ejecuta sobre PyTorch; torchaudio incluye además una implementación de Hybrid Demucs. | Instala PyTorch para tu dispositivo; después instala Demucs. |
| [Ultimate Vocal Remover (UVR)](ultimate-vocal-remover.md) | Ultimate Vocal Remover incluye los modelos Demucs v3 y v4 en una interfaz gráfica. | Instala UVR; después descarga los modelos Demucs desde su gestor de modelos. |
| [Audacity](audacity.md) | Los plugins OpenVINO de Intel para Audacity usan Demucs v4 para separar pistas dentro del editor. | Instala Audacity y los plugins OpenVINO; después aplica Music Separation. |

Estado en GitHub: activo · último push 2026-10-26 · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/adefossez/demucs/blob/main/README.md)</sub>

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

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
python3 -m pip install -U demucs
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/adefossez/demucs/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Demucs para mi objetivo y necesito pasos guiados. Lee https://github.com/adefossez/demucs/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `python3 -m pip install -U demucs` y ejecuta `demucs cancion.mp3`..

**Qué comprobar:** Obtienes una carpeta con las pistas separadas (drums, bass, vocals, other)..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- separar la voz y la batería de una canción propia para remezclar
- generar stems para karaoke o práctica musical

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: separar la voz y la batería de una canción propia para remezclar; generar stems para karaoke o práctica musical | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Es un fork (el original de Meta se archivó). El autor no trabaja activamente en él; la licencia de los pesos no es clara (MusDB es de uso para investigación y la variante de 6 fuentes probablemente es no comercial).

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `audio` `music` `separation` `pytorch`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [adefossez/demucs](https://github.com/adefossez/demucs)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/adefossez/demucs/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
