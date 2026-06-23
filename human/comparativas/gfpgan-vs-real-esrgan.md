# gfpgan vs real-esrgan

Generado: 2026-06-23T16:56:54.761958+00:00

| Criterio | GFPGAN | Real-ESRGAN |
|---|---|---|
| Uso real | algoritmo de restauración facial que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados. | herramienta de superresolución y restauración para imágenes reales que reescala y limpia material de baja calidad sin rehacerlo. |
| Elegir si | restauras rostros | reescalas imágenes |
| Evitar si | necesitas upscaling general ([Real-ESRGAN](#-real-esrgan)). | solo necesitas arreglar rostros ([GFPGAN](#-gfpgan)). |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `gfpgan` si su caso de uso encaja mejor ahora. Deja `real-esrgan` como alternativa, salvo que el proyecto necesite explicitamente ambos.
