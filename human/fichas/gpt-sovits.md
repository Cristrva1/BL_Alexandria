[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🗣️ GPT-SoVITS

> Clonación de voz y TTS con solo un minuto de audio, con interfaz web para entrenar.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 65.1k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Entrena una voz con muy pocos datos y sintetiza en varios idiomas. Muy popular entre creadores.

## Por qué destaca

Resultados notables con pocos datos de entrenamiento.

## Cómo funciona

Combina un modelo GPT para tokens semánticos con SoVITS para generar el audio.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GPT-SoVITS para mi objetivo y necesito pasos guiados. Lee https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Voces personalizadas para videos
- Doblaje de personajes
- Prototipos de voz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres entrenar una voz con pocos datos | prefieres zero-shot sin entrenar; mira `chatterbox` |

## Stack y modelos

- **Stack:** Python, PyTorch, Gradio
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [RVC WebUI](rvc.md) | 39.3k | Conversión de voz: entrena un modelo con menos de 10 minutos de audio y transforma una voz en otra. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Chatterbox](chatterbox.md) | 27.8k | Modelo de texto a voz open source de Resemble AI con clonación de voz y control de emoción. |
| [Fish Speech](fish-speech.md) | 33.7k | Sistema de texto a voz open source de alta calidad con clonación de voz multilingüe. |

## Enlaces

- 🐙 GitHub: [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/RVC-Boss/GPT-SoVITS/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
