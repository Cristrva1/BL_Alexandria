[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Música y audio generativo

# 🎵 AudioCraft

> Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.9k | MIT | Jupyter Notebook | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 52/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

AudioCraft, librería PyTorch de Meta para investigación en generación de audio (MusicGen y AudioGen). El código es MIT y los pesos son CC-BY-NC 4.0 (no comercial). Tiene ~24k estrellas y no cambia desde marzo de 2026.

## ¿Qué hace?

Genera música (MusicGen) y efectos de sonido (AudioGen) a partir de texto, e incluye EnCodec, MAGNeT y otros componentes con código de entrenamiento.

## ¿Cómo lo hace?

Requiere Python 3.9 y PyTorch 2.1.0 (versiones antiguas) y se instala con `pip install -U audiocraft`. Se recomienda tener FFmpeg y conviene una GPU.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Recomendado por el README para E/S de audio. | Instala FFmpeg. |
| [MoviePy](moviepy.md) | Añadir la música generada a vídeos. (combinación por arquitectura) | Monta el audio. |
| [remotion](remotion.md) | Banda sonora para vídeo programático. (combinación por arquitectura) | Usa el audio generado. |
| [rubberband](rubberband.md) | Combinación recíproca: rubberband lo enlaza como «Ajustar duración de audio generado. (combinación por arquitectura)». | Orden indicado desde rubberband: Procesa la salida. |
| [Audacity](audacity.md) | Combinación recíproca: Audacity lo enlaza como «Los plugins OpenVINO de Intel para Audacity generan y continúan música con MusicGen de AudioCraft». | Orden indicado desde Audacity: Instala los plugins OpenVINO y los modelos MusicGen; después usa Music Generation. |

**Notas:** Sin alternativas declaradas. Pesos no comerciales y dependencias antiguas.

Estado en GitHub: activo · último push 2026-03-03 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/facebookresearch/audiocraft/blob/main/README.md)</sub>

## Ver similares

Grupo **Generación de música**: AudioCraft ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ACE-Step-1.5](ace-step-1-5.md) ⭐ recomendado | 70 | Si buscas esto: modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. |
| 2 | [YuE2](yue.md) | 67 | Si buscas esto: modelo abierto de generación de canciones completas (voz y acompañamiento) a partir de letra y estilo, con partitura editable, covers y una skill para agentes. |
| 3 | **AudioCraft** (esta ficha) | 52 | Si buscas esto: librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códec EnCodec. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Código MIT y pesos CC BY-NC 4.0; ejecución propia no exige API pero hardware y licencia de uso son separados |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Los pesos publicados no permiten asumir uso comercial porque el código sea MIT; las alternativas de instalación del README no se ejecutan todas juntas |
| Coste | El coste depende del proveedor o la ruta. Código MIT y pesos CC BY-NC 4.0; ejecución propia no exige API pero hardware y licencia de uso son separados |
| Equipo | Preparación según la ruta elegida. Python 3.9 y PyTorch 2.1 según guía; modelo; GPU según tamaño; texto propio |

Los pesos publicados no permiten asumir uso comercial porque el código sea MIT; las alternativas de instalación del README no se ejecutan todas juntas

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.9 y PyTorch 2.1 según guía
- modelo
- GPU según tamaño
- texto propio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
python -m pip install -U audiocraft
```

Comando copiado literalmente de el README (sección «Installation»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/facebookresearch/audiocraft/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AudioCraft para mi objetivo y necesito pasos guiados. Lee https://github.com/facebookresearch/audiocraft/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera una muestra corta y compara su relación con el prompt sin publicar el resultado.

**Qué comprobar:** Puedes identificar modelo, duración y artefactos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar generación de música
- Estudiar sonidos a partir de texto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar generación de música; Estudiar sonidos a partir de texto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los pesos publicados no permiten asumir uso comercial porque el código sea MIT; las alternativas de instalación del README no se ejecutan todas juntas

## Stack y modelos

- **Stack:** Python 3.9 y PyTorch 2.1 según guía; modelo; GPU según tamaño; texto propio
- **Etiquetas:** `audio` `inference` `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [YuE2](yue.md) | 13.5k | Modelo abierto de generación de canciones completas (voz y acompañamiento) a partir de letra y estilo, con partitura editable, covers y una skill para agentes. |
| [ACE-Step-1.5](ace-step-1-5.md) | 14.8k | Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tamaño. |

## Enlaces

- 🐙 GitHub: [facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/facebookresearch/audiocraft/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
