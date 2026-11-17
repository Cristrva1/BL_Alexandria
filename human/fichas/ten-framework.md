[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Agentes de voz en tiempo real

# 📚 TEN Framework

> Framework para agentes de voz conversacionales en tiempo real, con grafo de extensiones (ASR, LLM, TTS, VAD, turnos), diseñador visual y ejemplos listos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.2k | Apache-2.0 con condiciones adicionales (Agora) | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** hard

**Nivel:** 3 Avanzado — framework de voz con diseñador visual y varios proveedores · corregido a mano

**Puntuación de calidad** 43/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de código abierto impulsado por Agora para agentes de voz conversacionales. Muy activo. Se publica con licencia Apache-2.0 con restricciones adicionales, por lo que no es una licencia OSI.

## ¿Qué hace?

Conecta en tiempo real reconocimiento de voz, LLM, síntesis de voz, detección de actividad de voz y de turnos (TEN VAD, TEN Turn Detection), avatares y herramientas en un grafo de extensiones. Incluye TMAN Designer para editar el grafo sin código, un agente de ejemplo con interfaz web y extensiones para muchos proveedores.

## ¿Cómo lo hace?

Runtime con extensiones en C++, Go, Python y Node.js. Los ejemplos se ejecutan en un contenedor de desarrollo con Docker Compose o en Codespaces y se despliegan como imagen Docker. El transporte en tiempo real usa Agora RTC por defecto.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [dify](dify.md) | TEN incluye una extensión que conecta el agente de voz con aplicaciones de Dify. | Crea la app en Dify; después configura la extensión de Dify en el grafo de TEN con su clave. |
| [OpenClaw](openclaw.md) | TEN incluye una extensión y un ejemplo de agente de voz que delega tareas en OpenClaw. | Instala OpenClaw; después configura su extensión en TEN. |
| [VibeVoice](vibevoice.md) | TEN incluye una extensión de síntesis de voz con VibeVoice. | Despliega VibeVoice; después elige su extensión TTS en el grafo. |
| [whisper](whisper.md) | TEN incluye extensiones de reconocimiento de voz basadas en Whisper. | Configura la extensión ASR de Whisper; después úsala en lugar de Deepgram. |
| [ElevenLabs (SDK de Python)](elevenlabs-python.md) | El ejemplo rápido de TEN usa ElevenLabs para la síntesis de voz (requiere clave). | Crea una clave de ElevenLabs; después ponla en `ELEVENLABS_TTS_KEY` del `.env`. |

**Notas:** Alternativa de Pipecat, LiveKit Agents y Dograh; revisa la licencia antes de usarlo en productos.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada 0.11.75 (2026-11-03) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/TEN-framework/ten-framework/blob/main/README.md) · [2](https://github.com/TEN-framework/ten-framework/blob/main/LICENSE) · [3](https://github.com/TEN-framework/ten-framework/tree/main/ai_agents/agents/ten_packages/extension)</sub>

## Ver similares

Grupo **Agentes de voz en tiempo real**: TEN Framework ocupa la posición 4 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Pipecat](pipecat.md) ⭐ recomendado | 73 | Si quieres componer pipelines de voz en Python con muchos proveedores intercambiables. |
| 2 | [LiveKit Agents](livekit-agents.md) | 73 | Si quieres agentes de voz y video en tiempo real sobre WebRTC con infraestructura probada. |
| 3 | [dograh](dograh.md) | 60 | Si quieres una plataforma con flujos visuales y telefonía lista para agentes de voz. |
| 4 | **TEN Framework** (esta ficha) | 43 | Si quieres un grafo visual de extensiones (ASR, LLM, TTS) para voz en tiempo real. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (bash):**

```
docker compose up -d
```

Comando copiado literalmente de el README (sección «3. Start agent development containers»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/TEN-framework/ten-framework/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar TEN Framework para mi objetivo y necesito pasos guiados. Lee https://github.com/TEN-framework/ten-framework/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona el repo, rellena `.env` con las claves de Agora, OpenAI, Deepgram y ElevenLabs y ejecuta `docker compose up -d`; abre el ejemplo de voz en el navegador..

**Qué comprobar:** Puedes hablar con un agente que responde por voz en tiempo real..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- montar un asistente de voz que conversa en tiempo real con un LLM
- construir un agente de voz con avatar o con transcripción en vivo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: montar un asistente de voz que conversa en tiempo real con un LLM; construir un agente de voz con avatar o con transcripción en vivo | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Licencia Apache-2.0 con condiciones adicionales de Agora (no OSI): no permite alojarlo en dispositivos de usuario final ni usarlo para competir con Agora. El ejemplo rápido necesita claves de pago (Agora, OpenAI, Deepgram, ElevenLabs).

## Stack y modelos

- **Stack:** Python, package.json
- **Etiquetas:** `voice` `agents` `realtime` `framework`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pipecat](pipecat.md) | 17.3k | Framework open source para agentes de voz y apps multimodales en tiempo real. |
| [LiveKit Agents](livekit-agents.md) | 15.2k | Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. |
| [dograh](dograh.md) | 6.1k | Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables. |

## Enlaces

- 🐙 GitHub: [TEN-framework/ten-framework](https://github.com/TEN-framework/ten-framework)
- 🌐 Web: <https://agent.theten.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/TEN-framework/ten-framework/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
