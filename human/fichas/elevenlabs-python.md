[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Síntesis y clonación de voz

# 📚 ElevenLabs (SDK de Python)

> SDK oficial de Python para la API de pago de ElevenLabs: voz sintética, clonación, transcripción, música y agentes de voz.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.2k | MIT | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

SDK oficial de Python para la API de ElevenLabs (organización elevenlabs), generado con Fern y con licencia MIT. El cliente es libre, pero el servicio es de pago por uso. Versión v2.78.0 (noviembre de 2026), activo. El servidor MCP oficial (elevenlabs/elevenlabs-mcp) está archivado.

## ¿Qué hace?

Da acceso desde Python a texto a voz (Eleven v4, v4 Turbo, Multilingual v2, Flash v2.5), clonación de voz, transcripción con Scribe v2 (también en tiempo real), música con Eleven Music, gestión de voces y agentes conversacionales en tiempo real (ElevenAgents).

## ¿Cómo lo hace?

Se instala con `pip install elevenlabs` (Python 3.8 o superior) y se autentica con la clave `ELEVENLABS_API_KEY`. Llama a la API de ElevenLabs con un cliente síncrono o asíncrono (`AsyncElevenLabs`) y admite streaming de audio. Toda la inferencia ocurre en los servidores de ElevenLabs.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenMontage](openmontage.md) | OpenMontage usa ElevenLabs para TTS premium, música y efectos de sonido con `ELEVENLABS_API_KEY`; su código importa este SDK. | Crea la clave, añádela al `.env` de OpenMontage y genera una pista corta. |
| [Pipecat](pipecat.md) | Pipecat incluye servicios de ElevenLabs para TTS y STT en agentes de voz en tiempo real. | Instala el extra de ElevenLabs de Pipecat y configura la clave. |
| [LiveKit Agents](livekit-agents.md) | LiveKit Agents documenta un plugin de TTS de ElevenLabs. | Instala el plugin de ElevenLabs y define la clave en el entorno del agente. |
| [video-use](video-use.md) | video-use pide una clave de ElevenLabs para la voz; el SDK sirve para elegir y probar voces o generar pistas fuera del flujo. (combinación por arquitectura) | Usa la misma clave en ambos y prueba la voz antes de editar. |
| [Remotion Superpowers](remotion-superpowers.md) | El plugin usa las skills oficiales de ElevenLabs para locución, efectos y música. (combinación por arquitectura) | Configura la clave de ElevenLabs al instalar el plugin. |
| [TEN Framework](ten-framework.md) | Combinación recíproca: TEN Framework lo enlaza como «El ejemplo rápido de TEN usa ElevenLabs para la síntesis de voz (requiere clave)». | Orden indicado desde TEN Framework: Crea una clave de ElevenLabs; después ponla en `ELEVENLABS_TTS_KEY` del `.env`. |

**Notas:** La clonación de voz exige el consentimiento de la persona. Vigila el consumo de créditos: el SDK no limita el gasto.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v2.78.0 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/elevenlabs/elevenlabs-python/blob/main/README.md) · [2](https://elevenlabs.io/docs/api-reference/introduction) · [3](https://docs.pipecat.ai/server/services/tts/elevenlabs) · [4](https://docs.livekit.io/agents/integrations/tts/elevenlabs/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. Toda llamada usa la API de ElevenLabs con tu ELEVENLABS_API_KEY. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. No ejecuta modelos localmente: es un cliente de un servicio en la nube. |
| Coste | Consumo de APIs o servicios. Consumo por caracteres, minutos o créditos según el plan de ElevenLabs; el SDK es gratuito. |
| Equipo | Equipo normal; revisar dependencias. Python 3.8 o superior y conexión a internet. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Crea una clave en ElevenLabs y guárdala como ELEVENLABS_API_KEY fuera del repositorio.
2. Instala el paquete y convierte una frase corta con el ejemplo del README.
3. Revisa el consumo en tu cuenta antes de generar audio largo o clonar voces (con consentimiento).

**Entrada documentada (consulta la sintaxis original):**

```
pip install elevenlabs
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/elevenlabs/elevenlabs-python/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ElevenLabs (SDK de Python) para mi objetivo y necesito pasos guiados. Lee https://github.com/elevenlabs/elevenlabs-python/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte una frase corta a voz con una voz predefinida.

**Qué comprobar:** Obtienes un MP3 reproducible y el consumo aparece en tu cuenta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Generar una locución para un video
- Prototipar un agente de voz conectado a la API

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Generar una locución para un video; Prototipar un agente de voz conectado a la API | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Servicio de pago en la nube; clonar voces requiere consentimiento de la persona.

## Stack y modelos

- **Stack:** Python, pyproject.toml, requirements.txt
- **Etiquetas:** `tts` `voice` `api` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [elevenlabs/elevenlabs-python](https://github.com/elevenlabs/elevenlabs-python)
- 🌐 Web: <https://elevenlabs.io/docs/api-reference/overview>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/elevenlabs/elevenlabs-python/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
