# nanochat vs nanogpt

Generado: 2026-06-25T03:39:27.698706+00:00

| Criterio | nanochat | nanoGPT |
|---|---|---|
| Uso real | pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible. | implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo. |
| Elegir si | quieres el pipeline completo | quieres entender el entrenamiento |
| Evitar si | solo necesitas el core ([nanoGPT](#-nanogpt)). | solo consumes modelos vía API. |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `nanochat` si su caso de uso encaja mejor ahora. Deja `nanogpt` como alternativa, salvo que el proyecto necesite explicitamente ambos.
