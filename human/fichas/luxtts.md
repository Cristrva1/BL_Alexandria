[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🗣️ LuxTTS

> Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.6k | Apache-2.0 | Python | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

LuxTTS, modelo TTS ligero basado en ZipVoice para clonar voces, de @ysharma3501. Licencia Apache-2.0 para modelo y código. Es reciente (enero de 2026, ~5.6k estrellas) y no cambia desde junio de 2026.

## ¿Qué hace?

Clona voces con calidad alta y genera audio a más de 150× tiempo real en una GPU, y más rápido que tiempo real en CPU, según el autor. Cabe en ~1 GB de VRAM.

## ¿Cómo lo hace?

Se instala desde el repo con `pip install -r requirements.txt` y descarga el modelo de Hugging Face.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ComfyUI](comfyui.md) | Integrar la síntesis en flujos visuales. (combinación por arquitectura) | Usa un nodo comunitario si existe. |
| [Pipecat](pipecat.md) | TTS local en agentes de voz. (combinación por arquitectura) | Expón el modelo como servicio. |
| [MoviePy](moviepy.md) | Narración de vídeos. (combinación por arquitectura) | Monta el audio generado. |

**Notas:** Alternativas (elige una): kokoro. Se quitan litellm y cosmos de las combinaciones (sin relación).

Estado en GitHub: activo · último push 2026-06-05 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ysharma3501/LuxTTS/blob/master/README.md)</sub>

## Ver similares

Grupo **TTS ligero y rápido**: LuxTTS ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [edge-tts](edge-tts.md) ⭐ recomendado | 60 | Si buscas esto: biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. |
| 2 | **LuxTTS** (esta ficha) | 56 | Si buscas esto: modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. |
| 3 | [Kokoro](kokoro.md) | 52 | Si buscas esto: modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El autor declara modelo y código Apache-2.0; hardware y datos se costean aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La cifra de 150 veces tiempo real es del autor y no una garantía de latencia o calidad en cualquier equipo |
| Coste | Sin pago a un modelo en la ruta básica. El autor declara modelo y código Apache-2.0; hardware y datos se costean aparte |
| Equipo | Preparación según la ruta elegida. Python; dependencias; modelo; equipo; voz con permiso |

La cifra de 150 veces tiempo real es del autor y no una garantía de latencia o calidad en cualquier equipo

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- dependencias
- modelo
- equipo
- voz con permiso

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
git clone https://github.com/ysharma3501/LuxTTS.git
cd LuxTTS
pip install -r requirements.txt
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ysharma3501/LuxTTS/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LuxTTS para mi objetivo y necesito pasos guiados. Lee https://github.com/ysharma3501/LuxTTS/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sintetiza una frase y mide tiempo y calidad en tu propio equipo.

**Qué comprobar:** Puedes comparar texto, referencia y audio generado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una narración local
- Explorar adaptación de voz consentida

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una narración local; Explorar adaptación de voz consentida | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La cifra de 150 veces tiempo real es del autor y no una garantía de latencia o calidad en cualquier equipo

## Stack y modelos

- **Stack:** Python; dependencias; modelo; equipo; voz con permiso
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Kokoro](kokoro.md) | 10.1k | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |

## Enlaces

- 🐙 GitHub: [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ysharma3501/LuxTTS/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
