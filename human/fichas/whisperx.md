[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Transcripción (voz a texto)

# 🎯 whisperX

> Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.3k | BSD-2-Clause | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige API de transcripción de pago; diarización requiere acceso autorizado al modelo de Hugging Face y cómputo propio |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Un token de descarga no equivale a facturación de API; etiquetas de hablante no identifican personas y los tiempos necesitan comprobación |
| Coste | Sin pago a un modelo en la ruta básica. No exige API de transcripción de pago; diarización requiere acceso autorizado al modelo de Hugging Face y cómputo propio |
| Equipo | Preparación según la ruta elegida. Python; modelo de transcripción y alineación; HF token y acuerdo para diarización; audio propio |

Un token de descarga no equivale a facturación de API; etiquetas de hablante no identifican personas y los tiempos necesitan comprobación

## Qué puedes hacer con él

Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes.

## Por qué destaca

Usos propuestos: Preparar subtítulos por palabra; Separar intervenciones de una entrevista.

## Cómo funciona

Un token de descarga no equivale a facturación de API; etiquetas de hablante no identifican personas y los tiempos necesitan comprobación

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- modelo de transcripción y alineación
- HF token y acuerdo para diarización
- audio propio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install whisperx
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/m-bain/whisperX/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar whisperX para mi objetivo y necesito pasos guiados. Lee https://github.com/m-bain/whisperX/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Transcribe una conversación de prueba y verifica varias marcas temporales y cambios de hablante.

**Qué comprobar:** Puedes distinguir texto, alineación y etiquetas de hablante.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar subtítulos por palabra
- Separar intervenciones de una entrevista

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar subtítulos por palabra; Separar intervenciones de una entrevista | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Un token de descarga no equivale a facturación de API; etiquetas de hablante no identifican personas y los tiempos necesitan comprobación

## Stack y modelos

- **Stack:** Python; modelo de transcripción y alineación; HF token y acuerdo para diarización; audio propio
- **Etiquetas:** `stt` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper](whisper.md) | 113k | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. |
| [MoviePy](moviepy.md) | 15.2k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [NeMo Speech](nemo.md) | 18.8k | Framework actual de NVIDIA para reconocimiento,síntesis y modelos de voz con recetas de inferencia y entrenamiento. |

## Enlaces

- 🐙 GitHub: [m-bain/whisperX](https://github.com/m-bain/whisperX)
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/m-bain/whisperX/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
