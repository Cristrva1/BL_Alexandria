[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Música y audio generativo

# 🧩 YuE2

> Modelo abierto de generación de canciones completas (voz y acompañamiento) a partir de letra y estilo, con partitura editable, covers y una skill para agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.5k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** hard

**Nivel:** 4 Experto — preparación difícil; necesita GPU

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Modelo de investigación de código abierto del proyecto Multimodal Art Projection (M-A-P). Desde septiembre de 2026 el repositorio aloja YuE2; el YuE original se conserva en la rama YuE-v1. Código, skill y documentación son Apache-2.0; los pesos son CC BY-NC 4.0 con permiso adicional de los creadores.

## ¿Qué hace?

Genera canciones completas con voz y acompañamiento a partir de letra y estilo, escribe primero una partitura ABC editable, hace covers zero-shot a partir de grabaciones (transcritas con SheetSage2), genera música instrumental y permite editar la composición de forma conversacional. Incluye la skill `yue2-music` para agentes.

## ¿Cómo lo hace?

Un backbone AR–NAR Mixture-of-Transformers predice partitura y tokens semánticos, y genera latentes acústicos con flow matching que un VAE decodifica a audio estéreo de 48 kHz. Requiere Linux, Python 3.12 y GPU NVIDIA con BF16 y 24 GB de VRAM; los pesos se descargan de Hugging Face al primer uso.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | YuE2 incluye la skill `yue2-music` para agentes de código que orquesta generación, covers y edición de partituras (el README recomienda GPT-6 Astra como agente). | Instala YuE2 con `pip install .`; después importa `skills/yue2-music/` en el directorio de skills del agente. |
| [PyTorch](pytorch.md) | YuE2 se ejecuta sobre PyTorch con CUDA en GPU NVIDIA. | Instala PyTorch con CUDA; después instala YuE2. |
| [Audacity](audacity.md) | Las canciones generadas por YuE2 se pueden recortar, mezclar y masterizar en Audacity (combinación por arquitectura). | Genera el audio con YuE2; después ábrelo en Audacity para editarlo. |

**Notas:** Alternativa abierta de ACE-Step 1.5 y AudioCraft (MusicGen). El README dice que YuE2 compite con Suno v5/v6 en WildSongBench [DATO NO VERIFICADO: benchmark del propio equipo].

Estado en GitHub: activo · último push 2026-11-01 · última versión publicada yue2-v0.1.6 (2026-09-09) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/multimodal-art-projection/YuE/blob/main/README.md) · [2](https://github.com/multimodal-art-projection/YuE/blob/main/MODEL_LICENSE)</sub>

## Ver similares

Grupo **Generación de música**: YuE2 ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ACE-Step-1.5](ace-step-1-5.md) ⭐ recomendado | 70 | Si buscas esto: modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. |
| 2 | **YuE2** (esta ficha) | 67 | Si buscas esto: modelo abierto de generación de canciones completas (voz y acompañamiento) a partir de letra y estilo, con partitura editable, covers y una skill para agentes. |
| 3 | [AudioCraft](audiocraft.md) | 52 | Si buscas esto: librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. |

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

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.

1. Elige el modelo y el backend que documenta el proyecto para tu sistema.
2. Prepara las dependencias y los pesos; no uses una cifra promocional como garantía para tu hardware.
3. Procesa una muestra pequeña y revisa calidad, tiempo y memoria antes de aumentar el tamaño de la tarea.

**Entrada documentada (bash):**

```
git clone https://github.com/multimodal-art-projection/YuE.git
```

Comando copiado literalmente de el README (sección «Quick start»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/multimodal-art-projection/YuE/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar YuE2 para mi objetivo y necesito pasos guiados. Lee https://github.com/multimodal-art-projection/YuE/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En Linux con una GPU NVIDIA de 24 GB, clona el repo, ejecuta `python -m pip install .` y genera una canción con `YuE2Pipeline`..

**Qué comprobar:** Obtienes un audio estéreo y la partitura ABC editable..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- generar una maqueta de canción con letra propia para un proyecto personal o académico
- editar la armonía de una canción generada manteniendo la melodía

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: generar una maqueta de canción con letra propia para un proyecto personal o académico; editar la armonía de una canción generada manteniendo la melodía | no tienes el hardware o no aceptas la licencia de los pesos |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Los pesos son CC BY-NC 4.0 con permiso adicional de los creadores: solo uso no comercial; el uso comercial requiere licencia. Exige GPU NVIDIA de 24 GB.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `music` `generation` `audio` `model`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ACE-Step-1.5](ace-step-1-5.md) | 14.8k | Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. |
| [AudioCraft](audiocraft.md) | 23.9k | Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. |

## Enlaces

- 🐙 GitHub: [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE)
- 🌐 Web: <https://map-yue2.github.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/multimodal-art-projection/YuE/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
