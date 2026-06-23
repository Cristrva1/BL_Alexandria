# llmc vs nanogpt

Generado: 2026-06-23T16:56:54.761958+00:00

| Criterio | llm.c | nanoGPT |
|---|---|---|
| Uso real | implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo. | implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo. |
| Elegir si | quieres bajo nivel sin abstracciones | quieres entender el entrenamiento |
| Evitar si | prefieres PyTorch ([nanoGPT](#-nanogpt)). | solo consumes modelos vía API. |
| Instalacion | deferred | reference_only |

## Regla practica

Elige `llmc` si su caso de uso encaja mejor ahora. Deja `nanogpt` como alternativa, salvo que el proyecto necesite explicitamente ambos.
