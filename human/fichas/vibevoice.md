[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 🗣️ VibeVoice

> Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 57.2k | MIT | Python | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; requiere programar con él

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

VibeVoice, familia de modelos de voz open source de Microsoft (TTS y ASR). Licencia MIT. Tiene ~57k estrellas; en septiembre de 2025 Microsoft desactivó el código de VibeVoice-TTS-1.5B tras detectar usos indebidos.

## ¿Qué hace?

VibeVoice-ASR transcribe hasta 60 minutos con identificación de hablantes en más de 50 idiomas, con versión streaming y motor BitNet para CPU. VibeVoice-Realtime-0.5B es un TTS en streaming; el TTS largo multi-hablante está deshabilitado.

## ¿Cómo lo hace?

VibeVoice-ASR está integrado en Transformers y en Azure AI Foundry Labs, y hay código de fine-tuning de ASR. Los modelos se descargan de Hugging Face.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Transformers](transformers.md) | VibeVoice-ASR integrado en Transformers. | Carga el modelo con Transformers. |
| [open-notebook](open-notebook.md) | Narración de podcasts. (combinación por arquitectura) | Usa un TTS compatible para los episodios. |
| [Pipecat](pipecat.md) | ASR o TTS en agentes de voz. (combinación por arquitectura) | Integra el modelo como servicio. |
| [TEN Framework](ten-framework.md) | Combinación recíproca: TEN Framework lo enlaza como «TEN incluye una extensión de síntesis de voz con VibeVoice». | Orden indicado desde TEN Framework: Despliega VibeVoice; después elige su extensión TTS en el grafo. |

**Notas:** Sin alternativas declaradas. Partes del TTS deshabilitadas por uso indebido.

Estado en GitHub: activo · último push 2026-10-08 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/microsoft/VibeVoice/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ejecución propia no exige API; pesos, hardware y datos tienen condiciones por variante |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es una familia que incluye ASR, streaming y TTS; el README raíz remite a guías separadas y no tiene un único instalador universal |
| Coste | Sin pago a un modelo en la ruta básica. La ejecución propia no exige API; pesos, hardware y datos tienen condiciones por variante |
| Equipo | Preparación según la ruta elegida. Modelo y guía específicos; Python y GPU según variante; audio autorizado |

Es una familia que incluye ASR, streaming y TTS; el README raíz remite a guías separadas y no tiene un único instalador universal

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Modelo y guía específicos
- Python y GPU según variante
- audio autorizado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/microsoft/VibeVoice.git
```

Comando copiado literalmente de la documentación del repositorio (sección «Prerequisites»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/microsoft/VibeVoice/blob/main/docs/setup_gradio_demo.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar VibeVoice para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/VibeVoice/blob/main/docs/setup_gradio_demo.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige ASR o TTS y prueba una muestra corta siguiendo esa guía.

**Qué comprobar:** Puedes distinguir transcripción, generación y variante del modelo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar transcripción por hablantes
- Probar generación de voz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar transcripción por hablantes; Probar generación de voz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una familia que incluye ASR, streaming y TTS; el README raíz remite a guías separadas y no tiene un único instalador universal

## Stack y modelos

- **Stack:** Modelo y guía específicos; Python y GPU según variante; audio autorizado
- **Etiquetas:** `tts` `audio` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice)
- 🌐 Web: <https://microsoft.github.io/VibeVoice/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/VibeVoice/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
