# llmc vs nanogpt

Generado: 2026-06-25T05:01:02.236908+00:00

| Criterio | llm.c | nanoGPT |
|---|---|---|
| Uso real | implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo. | Update Nov 2025** nanoGPT has a new and improved cousin called nanochat. It is very likely you meant to use/find nanochat instead. nanoGPT (this repo) is now very old and deprecated but I will leave it up for posterity. |
| Elegir si | quieres bajo nivel sin abstracciones | quieres nanogpt |
| Evitar si | prefieres PyTorch ([nanoGPT](#-nanogpt)). | ya tienes una herramienta equivalente o no encaja con tu stack actual |
| Instalacion | deferred | deferred |

## Regla practica

Elige `llmc` si su caso de uso encaja mejor ahora. Deja `nanogpt` como alternativa, salvo que el proyecto necesite explicitamente ambos.
