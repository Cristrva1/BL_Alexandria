# tts vs supertonic

Generado: 2026-06-25T03:39:27.698706+00:00

| Criterio | TTS | supertonic |
|---|---|---|
| Uso real | toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz. | motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU. |
| Elegir si | quieres flexibilidad | quieres voz local en tiempo real |
| Evitar si | necesitas tiempo real puro ([supertonic](#-supertonic)). | priorizas clonación de máxima fidelidad ([VoxCPM](#-voxcpm)). |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `tts` si su caso de uso encaja mejor ahora. Deja `supertonic` como alternativa, salvo que el proyecto necesite explicitamente ambos.
