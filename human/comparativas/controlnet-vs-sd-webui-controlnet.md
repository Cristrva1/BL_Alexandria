# controlnet vs sd-webui-controlnet

Generado: 2026-06-24T18:45:16.466468+00:00

| Criterio | ControlNet | sd-webui-controlnet |
|---|---|---|
| Uso real | método y modelos para condicionar la generación text-to-image con señales externas como poses, bordes, profundidad o mapas de segmentación, fijando la estructura del resultado. | extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI, con preprocesadores para poses, bordes, profundidad y más. |
| Elegir si | necesitas control estructural | ya usas SD WebUI |
| Evitar si | ya trabajas en SD WebUI ([sd-webui-controlnet](#-sd-webui-controlnet)). | trabajas en ComfyUI o por código. |
| Instalacion | deferred | deferred |

## Regla practica

Elige `controlnet` si su caso de uso encaja mejor ahora. Deja `sd-webui-controlnet` como alternativa, salvo que el proyecto necesite explicitamente ambos.
