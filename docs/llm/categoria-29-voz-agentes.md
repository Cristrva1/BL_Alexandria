# Alexandría para agentes · Agentes de voz en tiempo real

Categoría 29 «Audio, transcripción, voz y música» › subcategoría `voz-agentes`. 4 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=29&sub=voz-agentes · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `livekit-agents` | Framework para agentes de voz y video en tiempo real sobre la infraestructura… | 2 Intermedio | 73 | Apache-2.0 (OSI permisiva) | alternativa |
| `pipecat` | Framework open source para agentes de voz y apps multimodales en tiempo real. | 2 Intermedio | 73 | BSD-2-Clause (OSI permisiva) | recomendado |
| `dograh` | Plataforma para construir agentes de voz con flujos visuales, telefonía y… | 2 Intermedio | 62 | BSD-2-Clause (OSI permisiva) | alternativa |
| `ten-framework` | Framework para agentes de voz conversacionales en tiempo real, con grafo de… | 3 Avanzado | 46 | Apache-2.0 con condiciones adicionales (Agora) (source-available) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### LiveKit Agents (`livekit-agents`)

- **Repo:** https://github.com/livekit/agents · Apache-2.0 · nivel 2 · 73/100 · alternativa en «Agentes de voz en tiempo real»
- **Qué es:** LiveKit Agents, framework para agentes de voz y vídeo en tiempo real sobre la infraestructura WebRTC de LiveKit. Licencia Apache-2.0; sus modelos de detección de turno usan la «LiveKit Model License». Es activo (~15k estrellas, 1.8.12).
- **Cuándo elegirlo:** Casos: Construir un asistente de voz; Evaluar conversación en tiempo real.
- **Requisitos:** nivel 2: preparación media; Python; LiveKit; proveedores o modelos locales; micrófono de prueba; hardware prerequisites; API de IA: opcional; Python; LiveKit; proveedores o modelos locales; micrófono de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install "livekit-agents[openai,deepgram,cartesia]"` — fuente: https://github.com/livekit/agents/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Usa terminal mode para una conversación breve y revisa cada etapa antes de añadir telefonía Éxito: Puedes comprobar audio de entrada, modelo y respuesta
- **Combina con:** `kokoro` [29/tts], `ollama` [8/motores], `whisper-cpp` [29/stt], `elevenlabs-python` [29/tts]
- **Alternativas:** `pipecat`, `dograh`, `ten-framework`
- **Riesgos y avisos:** Alternativas (elige una): pipecat, dograh. El MCP del README consulta documentación para desarrollar y no controla automáticamente tus agentes; usar Ollama no vuelve locales todos los componentes de….

### Pipecat (`pipecat`)

- **Repo:** https://github.com/pipecat-ai/pipecat · BSD-2-Clause · nivel 2 · 73/100 · recomendado en «Agentes de voz en tiempo real»
- **Qué es:** Pipecat, framework open source en Python para agentes de voz y multimodales en tiempo real, creado por Daily. Licencia BSD-2-Clause. Es maduro y muy activo (~17k estrellas, v1.16.0).
- **Cuándo elegirlo:** Casos: Prototipar un agente de voz; Comparar combinaciones STT/LLM/TTS.
- **Requisitos:** nivel 2: preparación media; uv; proveedores STT, LLM y TTS; micrófono; transporte local o remoto; hardware prerequisites; API de IA: opcional; uv; proveedores STT, LLM y TTS; micrófono; transporte local o remoto.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/pipecat-ai/pipecat/blob/main/README.md

  ```bash
  uv tool install "pipecat-ai[cli]"
  pipecat init
  ```
- **Primera prueba propuesta (no ejecutada):** Crea una prueba local de una pregunta y comprueba transcripción, respuesta y audio por separado Éxito: Puedes localizar en qué etapa falla la conversación
- **Combina con:** `kokoro` [29/tts], `whisper-cpp` [29/stt], `ollama` [8/motores], `nemo` [29/stt], `elevenlabs-python` [29/tts]
- **Alternativas:** `livekit-agents`, `dograh`, `ten-framework`
- **Riesgos y avisos:** Alternativas (elige una): livekit-agents, dograh. Tiene skills específicos de Claude Code; un agente que genera el código no aporta automáticamente el runtime ni créditos de telefonía o voz.

### dograh (`dograh`)

- **Repo:** https://github.com/dograh-hq/dograh · BSD-2-Clause · nivel 2 · 62/100 · alternativa en «Agentes de voz en tiempo real»
- **Qué es:** Dograh AI, plataforma open source y autoalojable para construir agentes de voz, alternativa a Vapi y Retell. Licencia BSD-2-Clause. Tiene ~6k estrellas y es activa (dograh-v1.51.0).
- **Cuándo elegirlo:** Casos: Diseñar un agente de voz; Editar un workflow mediante MCP.
- **Requisitos:** nivel 2: preparación media; Docker o entorno documentado; proveedores de voz/modelo; micrófono de prueba; hardware prerequisites; API de IA: depends; Docker o entorno documentado; proveedores de voz/modelo; micrófono de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `/plugin marketplace add dograh-hq/dograh-plugins` — fuente: https://github.com/dograh-hq/dograh/blob/main/docs/deployment/docker.mdx
- **Primera prueba propuesta (no ejecutada):** Crea un flujo de borrador y prueba una conversación local sin realizar llamadas telefónicas Éxito: Puedes inspeccionar nodos, proveedores y transiciones
- **Combina con:** `ollama` [8/motores], `whisper-cpp` [29/stt], `kokoro` [29/tts]
- **Alternativas:** `pipecat`, `livekit-agents`, `ten-framework`
- **Riesgos y avisos:** Alternativas (elige una): pipecat, livekit-agents. Revisa el túnel público y el registro abierto por defecto. MCP permite consultar y guardar borradores desde clientes compatibles; los plugins Claude y Codex ayudan a configurar y no incluyen suscripciones de voz.

### TEN Framework (`ten-framework`)

- **Repo:** https://github.com/TEN-framework/ten-framework · Apache-2.0 con condiciones adicionales (Agora) · nivel 3 · 46/100 · alternativa en «Agentes de voz en tiempo real»
- **Qué es:** Framework de código abierto impulsado por Agora para agentes de voz conversacionales. Muy activo. Se publica con licencia Apache-2.0 con restricciones adicionales, por lo que no es una licencia OSI.
- **Cuándo elegirlo:** Casos: montar un asistente de voz que conversa en tiempo real con un LLM; construir un agente de voz con avatar o con transcripción en vivo.
- **Requisitos:** nivel 3: framework de voz con diseñador visual y varios proveedores; Python, package.json; API de IA: sí; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d` — fuente: https://github.com/TEN-framework/ten-framework/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repo, rellena `.env` con las claves de Agora, OpenAI, Deepgram y ElevenLabs y ejecuta `docker compose up -d`; abre el ejemplo de voz en el navegador. Éxito: Puedes hablar con un agente que responde por voz en tiempo real.
- **Combina con:** `dify` [3/visual], `openclaw` [21/asistentes], `vibevoice` [29/tts], `whisper` [29/stt], `elevenlabs-python` [29/tts]
- **Alternativas:** `pipecat`, `livekit-agents`, `dograh`
- **Riesgos y avisos:** Alternativa de Pipecat, LiveKit Agents y Dograh; revisa la licencia antes de usarlo en productos.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-29-voz-agentes.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Agentes de voz en tiempo real», lee `docs/alexandria/categoria-29-voz-agentes.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-29-voz-agentes.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
