[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 MoneyPrinterTurbo

> App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 144k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 77/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

MoneyPrinterTurbo, app para generar vídeos cortos a partir de un tema o palabra clave, de @harry0703. Licencia MIT. Es muy popular (~144k estrellas, v1.3.10) y su README está lleno de patrocinios y enlaces de afiliado a proveedores de modelos.

## ¿Qué hace?

Genera el guion con un LLM, busca material en Pexels o Pixabay (o usa tus propios clips), sintetiza la voz, crea subtítulos y música de fondo y compone un vídeo vertical u horizontal. Admite muchos proveedores de LLM (OpenAI, Kimi, DeepSeek y compatibles) y de voz (Edge TTS gratuito, Azure, ElevenLabs, Kokoro, Fish Audio, VoxCPM…). Tiene interfaz web y API.

## ¿Cómo lo hace?

Requiere Python 3.11+ y se instala con pip (paquete oficial), desde el código o con Docker. Los subtítulos pueden salir de las marcas de tiempo del TTS o de faster-whisper en local; con GPU el procesamiento es más rápido. Las claves de LLM, de material y de voz se configuran en la interfaz.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [faster-whisper](faster-whisper.md) | Subtítulos locales con faster-whisper, citado en el README. | Activa faster-whisper en la configuración. |
| [Kokoro](kokoro.md) | Voz Kokoro entre los TTS integrados. | Selecciona Kokoro como servicio de voz. |
| [Ollama](ollama.md) | Usar un modelo local mediante un endpoint compatible con OpenAI. (combinación por arquitectura) | Apunta el proveedor compatible con OpenAI a Ollama. |

**Notas:** Alternativas (elige una): openmontage, videofy-minimal, short-video-factory. Revisa los derechos del material de stock y de las voces antes de publicar.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v1.3.10 (2026-11-07) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README.md)</sub>

## Ver similares

Grupo **Generación automática de videos cortos**: MoneyPrinterTurbo ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **MoneyPrinterTurbo** (esta ficha) ⭐ recomendado | 77 | Si buscas esto: app que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. |
| 2 | [short-video-factory](short-video-factory.md) | 46 | Si buscas esto: aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Guion, voz, stock e imagen pueden consumir servicios distintos; ofrece imagen SDXL local y una ruta Codex/ChatGPT sujeta a elegibilidad y límites de cuenta |
| Claude Code | Integración no documentada |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El adaptador Codex es del proyecto y no instala el CLI ni promete cobertura de cualquier modelo o cuenta; la imagen local no vuelve local todo el flujo |
| Coste | El coste depende del proveedor o la ruta. Guion, voz, stock e imagen pueden consumir servicios distintos; ofrece imagen SDXL local y una ruta Codex/ChatGPT sujeta a elegibilidad y límites de cuenta |
| Equipo | Preparación según la ruta elegida. Python; FFmpeg; proveedores de guion, voz e imágenes; material propio o autorizado |

El adaptador Codex es del proyecto y no instala el CLI ni promete cobertura de cualquier modelo o cuenta; la imagen local no vuelve local todo el flujo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- FFmpeg
- proveedores de guion, voz e imágenes
- material propio o autorizado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
python -m pip install mpt
mpt webui
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MoneyPrinterTurbo para mi objetivo y necesito pasos guiados. Lee https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un video corto de prueba con un guion revisado y comprueba voz, clips y subtítulos.

**Qué comprobar:** Puedes rastrear el origen de cada recurso y corregir el resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un borrador de video de producto
- Generar variantes de un tutorial propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un borrador de video de producto; Generar variantes de un tutorial propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El adaptador Codex es del proyecto y no instala el CLI ni promete cobertura de cualquier modelo o cuenta; la imagen local no vuelve local todo el flujo

## Stack y modelos

- **Stack:** Python; FFmpeg; proveedores de guion, voz e imágenes; material propio o autorizado
- **Etiquetas:** `video` `automation` `tts` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenMontage](openmontage.md) | 80.5k | Pipelines y herramientas para producir video con un agente,recursos propios,modelos locales o servicios opcionales. |
| [videofy_minimal](videofy-minimal.md) | 656 | Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión. |
| [short-video-factory](short-video-factory.md) | 6.1k | Aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos. |

## Enlaces

- 🐙 GitHub: [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README.md)
- [Fuente 2](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/docs/codex-provider.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
