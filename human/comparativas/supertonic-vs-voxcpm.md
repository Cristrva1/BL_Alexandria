# supertonic vs voxcpm

Generado: 2026-06-23T16:56:54.761958+00:00

| Criterio | supertonic | VoxCPM |
|---|---|---|
| Uso real | motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU. | sistema TTS de alta fidelidad de OpenBMB que prescinde del tokenizador tradicional para lograr una prosodia y fluidez muy naturales, con clonación de voz. |
| Elegir si | quieres voz local en tiempo real | quieres voz muy natural/clonada |
| Evitar si | priorizas clonación de máxima fidelidad ([VoxCPM](#-voxcpm)). | priorizas latencia mínima ([supertonic](#-supertonic)). |
| Instalacion | reference_only | deferred |

## Regla practica

Elige `supertonic` si su caso de uso encaja mejor ahora. Deja `voxcpm` como alternativa, salvo que el proyecto necesite explicitamente ambos.
