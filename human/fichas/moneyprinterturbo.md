[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 MoneyPrinterTurbo

> App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 144k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

MoneyPrinterTurbo automatiza la producción de shorts: das un tema o palabras clave y escribe el guion con un LLM, busca clips en Pexels o Pixabay (o usa los tuyos o video generado por IA), genera locución, subtítulos y música, y monta el resultado en 9:16, 16:9 o 1:1. Se usa desde WebUI, API, CLI o pidiéndoselo a un agente con su skill.

## Por qué destaca

Cubre todo el flujo de un canal de videos cortos sin editar a mano y es muy configurable: decenas de proveedores de LLM y TTS (incluida Edge TTS, gratuita), generación en lote y publicación directa en TikTok, Instagram y YouTube Shorts.

## Cómo funciona

Python con Streamlit para la WebUI y FastAPI para la API. El LLM genera el guion y los términos de búsqueda, se descargan clips de stock, se sintetiza la voz, los subtítulos salen del TTS o de faster-whisper y MoviePy compone el video.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MoneyPrinterTurbo para mi objetivo y necesito pasos guiados. Lee https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Producir shorts en lote para TikTok o YouTube Shorts
- Convertir un tema o artículo en un video narrado con subtítulos
- Prototipar formatos de video antes de invertir en edición

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres producir videos cortos narrados a partir de un tema sin editar a mano | necesitas control creativo plano a plano o una identidad visual propia; mira `remotion` u `openmontage` |

**Limitaciones:** El resultado depende del material de stock y del LLM, así que los videos tienden a ser genéricos; revisa derechos y normas de cada plataforma antes de publicar en masa.

## Stack y modelos

- **Stack:** Python, Streamlit, FastAPI, MoviePy, faster-whisper
- **Etiquetas:** `video` `automation` `tts` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [Kokoro](kokoro.md) | 10.1k | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |
| [faster-whisper](faster-whisper.md) | 26.8k | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenMontage](openmontage.md) | 80.5k | Convierte tu agente de código en un estudio de producción de video completo. |
| [videofy_minimal](videofy-minimal.md) | 656 | Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión. |

## Enlaces

- 🐙 GitHub: [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
