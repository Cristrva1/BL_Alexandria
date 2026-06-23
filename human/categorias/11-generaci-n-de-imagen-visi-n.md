# Generación de Imagen & Visión

Generado: 2026-06-23T16:56:54.761958+00:00

| Repo | Rol | Instalacion | Decision | Uso real |
|---|---|---|---|---|
| ComfyUI | runtime | deferred | defer | motor local modular para crear pipelines visuales de generación con IA mediante un grafo de nodos, donde cada paso (carga de modelo, sampling, postproceso) es un bloque conectable y reutilizable. |
| stable-diffusion-webui | app | deferred | defer | interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. |
| Fooocus | app | reference_only | reference | herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes. |
| InvokeAI | app | deferred | defer | suite profesional y unificada para Stable Diffusion que combina una UI pulida con canvas, capas, inpainting y gestión de modelos y workflows. |
| diffusers | library | deferred | defer | librería de Hugging Face para construir y ejecutar pipelines de modelos de difusión (imagen, video, audio) desde código, con APIs estandarizadas para schedulers y modelos. |
| ControlNet | runtime | deferred | defer | método y modelos para condicionar la generación text-to-image con señales externas como poses, bordes, profundidad o mapas de segmentación, fijando la estructura del resultado. |
| sd-webui-controlnet | runtime | deferred | defer | extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI, con preprocesadores para poses, bordes, profundidad y más. |
| ComfyUI_IPAdapter_plus | runtime | deferred | defer | conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una imagen de referencia para transferir estilo o identidad. |
| GFPGAN | runtime | reference_only | reference | algoritmo de restauración facial que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados. |
| Real-ESRGAN | runtime | reference_only | reference | herramienta de superresolución y restauración para imágenes reales que reescala y limpia material de baja calidad sin rehacerlo. |
| LivePortrait | runtime | deferred | defer | sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen. |
| Deep-Live-Cam | runtime | deferred | defer | herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video con salvaguardas de uso. |
| face_recognition | library | reference_only | reference | librería de Python sencilla para detección y reconocimiento facial, con una API de alto nivel para localizar, comparar e identificar caras en imágenes. |
| Open-Generative-AI | platform | reference_only | reference | plataforma alternativa libre a servicios premium de video/imagen que agrupa más de 200 modelos generativos accesibles desde terminal o integrados con agentes. |
| fluxer | platform | reference_only | reference | plataforma generativa emergente con foco en audio y video mejorados, ofrecida como cliente Canary web/desktop; su API y self-host aún están en finalización. |
