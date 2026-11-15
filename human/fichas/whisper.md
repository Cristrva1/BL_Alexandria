[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Transcripción (voz a texto)

# 📝 whisper

> Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 113k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Código y pesos MIT para ejecución propia sin API; cómputo independiente |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No es la API hospedada de OpenAI y no usa créditos de ChatGPT; puede inventar texto en silencios o audio difícil y requiere revisión |
| Coste | Sin pago a un modelo en la ruta básica. Código y pesos MIT para ejecución propia sin API; cómputo independiente |
| Equipo | Preparación según la ruta elegida. Python; PyTorch; FFmpeg; modelo con memoria suficiente; audio autorizado |

No es la API hospedada de OpenAI y no usa créditos de ChatGPT; puede inventar texto en silencios o audio difícil y requiere revisión

## Qué puedes hacer con él

Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo.

## Por qué destaca

Usos propuestos: Preparar una transcripción local; Traducir habla al inglés como borrador.

## Cómo funciona

No es la API hospedada de OpenAI y no usa créditos de ChatGPT; puede inventar texto en silencios o audio difícil y requiere revisión

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- PyTorch
- FFmpeg
- modelo con memoria suficiente
- audio autorizado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
pip install -U openai-whisper
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/openai/whisper/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar whisper para mi objetivo y necesito pasos guiados. Lee https://github.com/openai/whisper/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Transcribe una nota de voz breve y corrige manualmente las palabras dudosas.

**Qué comprobar:** Puedes contrastar texto con audio original.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una transcripción local
- Traducir habla al inglés como borrador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una transcripción local; Traducir habla al inglés como borrador | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No es la API hospedada de OpenAI y no usa créditos de ChatGPT; puede inventar texto en silencios o audio difícil y requiere revisión

## Stack y modelos

- **Stack:** Python; PyTorch; FFmpeg; modelo con memoria suficiente; audio autorizado
- **Etiquetas:** `stt` `audio` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisperX](whisperx.md) | 25.3k | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper.cpp](whisper-cpp.md) | 55.2k | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. |

## Enlaces

- 🐙 GitHub: [openai/whisper](https://github.com/openai/whisper)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openai/whisper/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
