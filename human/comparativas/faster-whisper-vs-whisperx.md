# faster-whisper vs whisperx

Generado: 2026-06-23T16:56:54.761958+00:00

| Criterio | faster-whisper | whisperX |
|---|---|---|
| Uso real | reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión. | extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |
| Elegir si | el rendimiento importa | necesitas subtítulos precisos |
| Evitar si | necesitas alineación/diarización ([whisperX](#-whisperx)). | te basta texto plano ([whisper](#-whisper)). |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `faster-whisper` si su caso de uso encaja mejor ahora. Deja `whisperx` como alternativa, salvo que el proyecto necesite explicitamente ambos.
