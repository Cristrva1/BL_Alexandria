
### 🖌️ InvokeAI
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🔴 pesado
**Qué es:** suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables. Resuelve la fragmentación de herramientas SD reuniendo generación, edición y control en una sola app self-hosted.
**Por qué destaca:** ofrece la experiencia creativa más estable del ecosistema SD, con un canvas tipo Photoshop (capas, máscaras, regiones) y respaldo de una empresa dedicada (InvokeAI Inc.) que mantiene releases regulares.
**Cómo funciona:** un backend Python/PyTorch ejecuta los modelos de difusión sobre GPU y sirve una SPA (React/TypeScript) con lienzo editable; los workflows se guardan como grafos reproducibles y los modelos se gestionan desde la propia app.
**Instalación:** instalador automático multiplataforma (launcher) o `pip install invokeai`; arranca un servidor web local tras configurar los modelos. Requiere GPU NVIDIA con VRAM generosa (8 GB+) y pesos de SD/SDXL descargados.
**Casos:** trabajo creativo serio con SD · canvas e inpainting profesional con regiones · iteración de campaña visual con workflows reutilizables.
**Stack:** Python, PyTorch, React, TypeScript, Docker — **Modelo/API:** local-first (modelos de difusión open-source).
**Elige si:** trabajas creatividad profesional y quieres una app estable con canvas — **Evita si:** solo haces una prueba puntual ([Fooocus](#-fooocus)) o prefieres grafos nodales ([ComfyUI](#-comfyui)).
**Limitaciones:** setup pesado y exigente en VRAM; la curva de aprendizaje del canvas y los workflows es mayor que en alternativas más simples.
**Combina con:** [diffusers](#-diffusers) · [ControlNet](#-controlnet)
**Repo:** [GitHub](https://github.com/invoke-ai/InvokeAI)

### 🤗 diffusers
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🔴 pesado
**Qué es:** librería de Hugging Face para construir y ejecutar pipelines de modelos de difusión (imagen, video, audio) desde código, con APIs estandarizadas para schedulers, componentes y modelos. Es la capa de abstracción que unifica el zoo de modelos de difusión bajo una misma interfaz Python.
**Por qué destaca:** es el estándar de facto para usar difusión programáticamente, mantenido por Hugging Face y con soporte inmediato para los modelos más nuevos (SDXL, Flux, SD3, video). Su adopción es masiva: casi cualquier proyecto de difusión en Python la usa como base.
**Cómo funciona:** carga modelos open-source desde el Hub y ejecuta su inferencia sobre PyTorch+GPU (o alternativas como Flax/Diffusers-ONNX) mediante clases `Pipeline` componibles; cada paso (scheduler, VAE, U-Net/transformer) es intercambiable.
**Instalación:** `pip install diffusers transformers accelerate`; los pesos se descargan automáticamente desde el Hub al instanciar un pipeline. Requiere GPU para uso práctico (aunque corre en CPU, muy lento) y espacio en disco para los pesos.
**Casos:** generación/transformación visual desde scripts propios · base reutilizable para apps y servicios · experimentación con schedulers y modelos nuevos.
**Stack:** Python, PyTorch, Hugging Face Hub — **Modelo/API:** modelos open-source (local/self-host), agnóstico del proveedor.
**Elige si:** programas generación y quieres control total por código — **Evita si:** quieres una UI lista ([Fooocus](#-fooocus)) o grafos nodales ([ComfyUI](#-comfyui)).
**Limitaciones:** GPU prácticamente obligatoria para latencia razonable; gestionar versiones de pesos y dependencias puede romper pipelines entre releases.
**Combina con:** [ControlNet](#-controlnet) · [cosmos](#-cosmos)
**Repo:** [GitHub](https://github.com/huggingface/diffusers)

### 🧭 ControlNet
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** método y familia de modelos que condicionan la generación text-to-image con señales externas (poses, bordes Canny, profundidad, mapas de segmentación), fijando la estructura del resultado. Resuelve el problema de que el texto por sí solo no controla la composición de la imagen.
**Por qué destaca:** revolucionó el control de la difusión al permitir guiar la composición sin perder calidad; es trabajo de referencia de Lvmin Zhang (lllyasviel) ampliamente citado y adoptado, con versiones 1.0/1.1 y modelos para múltiples condiciones.
**Cómo funciona:** añade una red paralela entrenable ("zero convolution") a un modelo de difusión sobre PyTorch+GPU que inyecta la condición (mapa de control) en cada paso de denoising del U-Net; el modelo base queda congelado durante el fine-tuning.
**Instalación:** `git clone` del repo y entorno con sus dependencias; descargar los pesos de ControlNet además del modelo base de Stable Diffusion. Requiere GPU NVIDIA y disco para varios pares de pesos.
**Casos:** guiar creativos con siluetas/poses/layouts · control compositivo preciso a partir de un boceto o depth map · mantener pose entre variantes de un personaje.
**Stack:** Python, PyTorch, difusión, GPU — **Modelo/API:** local (Stable Diffusion).
**Elige si:** necesitas control estructural fino de la composición — **Evita si:** ya trabajas en SD WebUI ([sd-webui-controlnet](#-sd-webui-controlnet)) o ComfyUI (tienen integración propia) y no necesitas el repo original.
**Limitaciones:** GPU obligatoria; cada tipo de control requiere su par de pesos; el repo original es más de investigación que de producto.
**Combina con:** [diffusers](#-diffusers) · [ComfyUI](#-comfyui)
**Repo:** [GitHub](https://github.com/lllyasviel/ControlNet)

### 🧩 sd-webui-controlnet
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI (AUTOMATIC1111), con preprocesadores para poses, bordes, profundidad y más. Lleva el control composicional al flujo de trabajo habitual de la WebUI sin tocar código.
**Por qué destaca:** es la forma estándar de usar ControlNet dentro del ecosistema AUTOMATIC1111, con panel propio y soporte para múltiples unidades de control simultáneas; muy popular entre quienes ya viven en esa UI.
**Cómo funciona:** se instala como extensión de la WebUI y añade un panel que aplica modelos ControlNet sobre la difusión PyTorch+GPU del propio WebUI, encadenando preprocesador (genera el mapa) + modelo de control (inyecta la condición).
**Instalación:** desde la pestaña Extensions de la WebUI (instalar por URL del repo) o `git clone` en `extensions/`; descargar luego los modelos ControlNet a `models/ControlNet`. Requiere la WebUI ya funcionando con GPU.
**Casos:** afinar creativos en SD WebUI con poses/sketches/mapas · combinar varios ControlNet a la vez (pose + depth) · iterar composición sin salir de la UI.
**Stack:** Python, SD WebUI (AUTOMATIC1111), modelos ControlNet — **Modelo/API:** local (difusión).
**Elige si:** ya usas SD WebUI y quieres ControlNet sin cambiar de entorno — **Evita si:** trabajas en ComfyUI (usa sus propios nodos) o por código ([diffusers](#-diffusers)).
**Combina con:** [stable-diffusion-webui](#-stable-diffusion-webui) · [ControlNet](#-controlnet)
**Repo:** [GitHub](https://github.com/Mikubill/sd-webui-controlnet)

### 🪞 ComfyUI_IPAdapter_plus
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una o varias imágenes de referencia para transferir estilo o identidad. Funciona como un "LoRA de una sola imagen": le das un referente y la salida hereda su look.
**Por qué destaca:** es la implementación de referencia de IPAdapter en ComfyUI (de cubiq), un nodo casi imprescindible para mantener coherencia visual entre piezas de una misma campaña o serie.
**Cómo funciona:** inyecta embeddings de imagen de referencia (extraídos vía CLIP vision) en el modelo de difusión sobre PyTorch+GPU durante el sampling de ComfyUI, ponderando la influencia del referente sin reentrenar el modelo base.
**Instalación:** clonar el repo en `custom_nodes/` de ComfyUI (o instalarlo desde ComfyUI Manager) y colocar los modelos IPAdapter y los pesos de CLIP vision en `models/`. Requiere ComfyUI con GPU.
**Casos:** mantener identidad/estilo entre piezas de una campaña · control por referencia visual sin entrenar un LoRA · transferir el look de un producto a variantes.
**Stack:** Python, ComfyUI, CLIP vision — **Modelo/API:** local (difusión).
**Elige si:** trabajas en ComfyUI y necesitas consistencia visual por referencia — **Evita si:** no usas ComfyUI o te basta con prompts de estilo.
**Limitaciones:** depende de pesos IPAdapter específicos (algunos de pago en civitai); la calidad de la transferencia varía mucho según el referente.
**Combina con:** [ComfyUI](#-comfyui)
**Repo:** [GitHub](https://github.com/cubiq/ComfyUI_IPAdapter_plus)

### 🙂 GFPGAN
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** algoritmo de restauración facial de Tencent ARC que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados. Resuelve el problema concreto de las caras "fundidas" que aparecen al reescalar o comprimir fotos.
**Por qué destaca:** resuelve muy bien un problema acotado y es una utilidad ampliamente reutilizada como paso de postproceso en pipelines de imagen; cuenta con demos públicos (Hugging Face, Replicate) y se integra en muchas UIs de SD.
**Cómo funciona:** detecta el rostro, lo alinea y aplica una red GAN (GFPGANv1) sobre PyTorch (GPU opcional) que regenera detalle realista preservando la identidad; combina la salida con la imagen original para no alterar el resto.
**Instalación:** `pip install gfpgan` o `git clone` con sus dependencias; los pesos del modelo se descargan en el primer uso. En Windows puede necesitar compilación de extensiones de CUDA.
**Casos:** mejorar retratos/frames antes de reutilizarlos · recuperar rostros degradados en material antiguo · postproceso de caras generadas por SD.
**Stack:** Python, PyTorch, GPU opcional — **Modelo/API:** modelos locales.
**Elige si:** restauras rostros borrosos o fundidos — **Evita si:** necesitas upscaling general de la imagen ([Real-ESRGAN](#-real-esrgan)).
**Combina con:** [Real-ESRGAN](#-real-esrgan)
**Repo:** [GitHub](https://github.com/TencentARC/GFPGAN)

### 🔍 Real-ESRGAN
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. A diferencia de los upscalers bicúbicos, infiere detalle plausible al ampliar.
**Por qué destaca:** es uno de los upscalers open-source más usados y citados (del grupo de Xintao Wang), con resultados sólidos en fotos y arte, e integrado como opción nativa en SD WebUI, ComfyUI y muchas UIs.
**Cómo funciona:** emplea una red GAN práctica sobre PyTorch+GPU entrenada con un pipeline de degradaciones sintéticas (blur + ruido + compresión) para inferir detalle al ampliar la imagen; ofrece modelos específicos para anime vs. foto.
**Instalación:** `pip install realesrgan` o ejecutable portable; los modelos preentrenados se descargan al primer uso. GPU recomendada (también hay build CPU).
**Casos:** reescalar creativos antiguos · mejorar detalle de assets comprimidos · upscaling de frames de video en pipelines.
**Stack:** Python, PyTorch, GPU — **Modelo/API:** modelos locales.
**Elige si:** reescalas imágenes o video a más resolución — **Evita si:** solo necesitas arreglar rostros ([GFPGAN](#-gfpgan)) o buscas difusión para reimaginar.
**Combina con:** [GFPGAN](#-gfpgan) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/xinntao/Real-ESRGAN)

### 🧑 LivePortrait
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen (humanos, pero también mascotas). Convierte una foto en un avatar que sigue las expresiones de un "conductor".
**Por qué destaca:** ofrece animación facial rápida y controlable (con retoque de ojos y boca vía "stitching" y retargeting), y ha sido adoptado por plataformas grandes (Kuaishou, Douyin, Jianying); es proyecto de KwaiVGI con pesos públicos.
**Cómo funciona:** usa un modelo de keypoints/warping implícito sobre PyTorch+GPU que deforma la cara de origen siguiendo el movimiento del conductor; un módulo de stitching suaviza la unión con el cuerpo y otro de retargeting controla ojos/boca de forma independiente.
**Instalación:** `git clone`, crear entorno y `pip install -r requirements.txt`; descargar los pesos preentrenados indicados en el repo. Requiere GPU NVIDIA con VRAM generosa.
**Casos:** convertir una foto en avatar/recurso animado · presentadores virtuales a partir de un retrato · animar ilustraciones de personajes para reels.
**Stack:** Python, PyTorch, GPU — **Modelo/API:** modelos locales.
**Elige si:** animas retratos a partir de una foto — **Evita si:** necesitas swap en vivo ([Deep-Live-Cam](#-deep-live-cam)) o no tienes GPU.
**Limitaciones:** GPU obligatoria; la calidad cae con poses extremas o rostros muy distintos al conductor; revisar licencia antes de uso comercial.
**Combina con:** [moviepy](#-moviepy)
**Repo:** [GitHub](https://github.com/KwaiVGI/LivePortrait)

### 🎭 Deep-Live-Cam
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. Convierte un cambio de rostro, que normalmente requiere pipeline complejo, en un flujo de "un clic".
**Por qué destaca:** es de los proyectos de swap en vivo más conocidos por su facilidad de uso (una sola imagen de origen y arrancar); incluye chequeos contra contenido inapropiado (NSFW/real) para desincentivar usos problemáticos.
**Cómo funciona:** combina detección facial (insightface/face_swapper) y reenactment sobre PyTorch+GPU (con backend ONNX Runtime o CUDA) para reemplazar el rostro fotograma a fotograma en un flujo en directo desde la webcam o un archivo.
**Instalación:** `git clone`, instalar dependencias y proveedores de GPU (p. ej. ONNX Runtime con CUDA Execution Provider); descargar los modelos de swap indicados. Requiere GPU NVIDIA para tiempo real fluido.
**Casos:** animar personajes · contenido creativo con rostro (uso responsable y consentido) · prototipos de presentadores virtuales en vivo.
**Stack:** Python, PyTorch, ONNX Runtime, GPU — **Modelo/API:** modelos locales.
**Elige si:** necesitas swap en vivo legítimo con consentimiento — **Evita si:** no puedes garantizar uso ético/consentimiento o no tienes GPU.
**Limitaciones:** uso responsable obligatorio: deepfakes de personas sin consentimiento pueden ser ilegales y violar ToS; GPU requerida para tiempo real; revisar licencia antes de uso comercial.
**Combina con:** [face_recognition](#-face_recognition)
**Repo:** [GitHub](https://github.com/hacksider/Deep-Live-Cam)

### 👤 face_recognition
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** librería de Python con API de alto nivel para detección y reconocimiento facial: localizar caras, compararlas e identificarlas por similitud. Envuelve dlib para que el reconocimiento facial sea trivial desde un script.
**Por qué destaca:** es de las librerías de reconocimiento facial más populares y accesibles, ideal para prototipos por su API mínima (`face_locations`, `face_encodings`, `compare_faces`); muy usada como referencia didáctica.
**Cómo funciona:** envuelve los modelos de dlib (detector HOG/CNN y embeddings faciales de 128 dimensiones) para comparar rostros por distancia entre vectores; el umbral de distancia decide si dos caras son la misma persona.
**Instalación:** `pip install face_recognition` (requiere dlib y, en Windows, herramientas de compilación de C++/CMake). El modelo CNN para mayor precisión necesita GPU.
**Casos:** detectar/identificar rostros en imágenes · etiquetado automático de álbumes · comparar identidad entre dos fotos.
**Stack:** Python, dlib — **Modelo/API:** modelos locales.
**Elige si:** necesitas reconocimiento facial básico y rápido de implementar — **Evita si:** buscas restauración/animación ([GFPGAN](#-gfpgan)/[LivePortrait](#-liveportrait)) o precisión de producción (mejor DeepFace/InsightFace).
**Limitaciones:** la instalación de dlib es frágil en Windows; el modelo por defecto (HOG) es menos preciso que alternativas modernas; el repo recibe mantenimiento esporádico.
**Combina con:** [Deep-Live-Cam](#-deep-live-cam)
**Repo:** [GitHub](https://github.com/ageitgey/face_recognition)

### 🎬 Open-Generative-AI
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma alternativa libre a servicios premium de video/imagen que agrupa más de 200 modelos generativos accesibles desde terminal o integrados con agentes. Centraliza la generación visual sin filtros restrictivos ni suscripción.
**Por qué destaca:** ofrece un hub unificado pensado para conectar la generación visual a flujos de agentes (CLI + integraciones), frente a servicios cerrados como Runway o Pika; su catálogo amplio cubre imagen, video y audio en un solo punto.
**Cómo funciona:** orquesta modelos de difusión y video vía la API en nube MuAPI o sobre GPUs locales, exponiéndolos tras una interfaz de línea de comandos y endpoints reutilizables desde scripts de agentes.
**Instalación:** `git clone` del repo e instalar dependencias de Python/Node.js; configurar la clave de MuAPI (render en nube) o el backend de GPU local. Sin clave, solo queda la vía local con GPU.
**Casos:** generar un clip promocional desde terminal · activos visuales rápidos para agentes · sustituir varias APIs de pago por un único hub.
**Stack:** Python, Node.js — **Modelo/API:** MuAPI (render en nube) o GPUs locales.
**Elige si:** quieres un hub de generación multi-modal sin atarte a un SaaS — **Evita si:** ya tienes tu pipeline local ([ComfyUI](#-comfyui)) o necesitas control fino por nodo.
**Combina con:** [remotion](#-remotion) · receta [Marketing de agencia](#-6-marketing-de-agencia)
**Repo:** [GitHub](https://github.com/Anil-matcha/Open-Generative-AI)

### 🌐 fluxer
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma generativa emergente con foco en audio y video mejorados, ofrecida como cliente Canary web/desktop; su API y self-host aún están en finalización. Apunta a unificar varios modelos generativos tras un cliente único.
**Por qué destaca:** apuesta por audio/video con mejoras continuas y un cliente nativo, aunque es un proyecto poco maduro y con documentación e instalación todavía limitadas (honestamente, oscuro). Útil solo para explorar el rumbo de la plataforma.
**Cómo funciona:** cliente en TypeScript/web que orquesta múltiples modelos generativos a través de servicios, con backend self-host aún no estabilizado y API en finalización según sus propios avisos.
**Instalación:** descargar el cliente Canary (web/desktop) o `git clone` del repo y compilar con el toolchain de Node/TS; self-host sujeto a cambios. No hay paquete estable publicado.
**Casos:** explorar una plataforma generativa emergente · cliente Canary web/desktop para probar audio/video mejorado.
**Stack:** web/TS — **Modelo/API:** múltiples (vía servicios del proyecto).
**Elige si:** quieres probar algo nuevo y seguir su evolución — **Evita si:** necesitas estabilidad de producción (API aún en finalización).
**Limitaciones:** proyecto en finalización: API, docs y self-host inestables; no apto para producción ni para depender de él hoy.
**Combina con:** [Open-Generative-AI](#-open-generative-ai)
**Repo:** [GitHub](https://github.com/fluxerapp/fluxer)

---

## 12. Audio, Voz & Video

Transcripción (STT), síntesis de voz (TTS) y edición/render de video.

### 🔍 Escaneo rápido

| Repo | Qué es | Tipo | Elige si… | Setup |
|---|---|---|---|---|
| [whisper](#-whisper) | Modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo. | STT | Quieres la referencia robusta y no te obsesiona la latencia. | 🟡 |
| [faster-whisper](#-faster-whisper) | Reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión. | STT | El rendimiento, la memoria o el coste de GPU importan. | 🟡 |
| [whisperX](#-whisperx) | Extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. | STT | Necesitas subtítulos precisos o diarización. | 🟡 |
| [supertonic](#-supertonic) | Motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU. | TTS | Quieres voz local en tiempo real y sin nube. | 🟡 |
| [VoxCPM](#-voxcpm) | Sistema TTS de alta fidelidad de OpenBMB que prescinde del tokenizador tradicional para lograr una prosodia y fluidez muy naturales, con clonación de voz a partir de pocos segundos de audio. | TTS | Quieres voz muy natural o clonada y tienes GPU. | 🔴 |
| [TTS](#-tts) | Toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz. | TTS | Quieres flexibilidad y varios modelos en una librería. | 🟡 |
| [OmniVoice-Studio](#-omnivoice-studio) | Suite de voz de escritorio open-source planteada como alternativa a ElevenLabs, con dictado en tiempo real, clonación zero-shot y doblaje de video en hasta 646 idiomas, todo local. | TTS/STT | Quieres suite de voz completa local (dictado + clonación + dubbing). | 🟡 |
| [lossless-cut](#-lossless-cut) | Aplicación de escritorio para recortar, fusionar y reorganizar video/audio sin recodificar, conservando la calidad original. | Video | Cortas material rápido y sin recomprimir. | 🟢 |
| [moviepy](#-moviepy) | Librería Python para edición de video programática: cortar, concatenar, superponer texto, subtítulos y audio, y exportar el resultado. | Video | Ensamblas video por código en Python. | 🟢 |
| [remotion](#-remotion) | Framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a MP4. | Video | Generas video a escala con React y quieres variantes parametrizadas. | 🟡 |
| [videofy_minimal](#-videofy_minimal) | Herramienta minimalista (de Schibsted) que convierte contenido textual en videos cortos de forma local, sin pipeline complejo. | Video | Quieres reels simples ya, sin montar un pipeline entero. | 🟢 |
| [OpenCut](#-opencut) | Editor de video open-source con UI moderna, planteado como alternativa libre tipo CapCut, usable en web o escritorio. | Video | Quieres un editor libre con UI moderna, sin CapCut. | 🟡 |
| [openscreen](#-openscreen) | Herramienta ligera de grabación de pantalla para screencasts y demos, basada en las APIs de captura del navegador. | Video | Necesitas screencast simple desde el navegador. | 🟢 |
| [Youtube2Webpage](#-youtube2webpage) | Script en Perl que genera una página web legible a partir de un video de YouTube, intercalando la transcripción de subtítulos con capturas de pantalla del momento citado. | Video | Quieres video → artículo con transcripción y capturas. | 🟢 |
| [hyperframes](#-hyperframes) | Framework npm para generar animaciones frame a frame de forma programática desde código. | Video | Generas animación por frames con control por código. | 🟡 |

### ⚖️ ¿Cuál elegir? — Transcripción (STT)

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **whisper** | Referencia general de STT | Robustez a ruido/acentos, 99 idiomas | Necesitas máxima velocidad o baja memoria |
| **faster-whisper** | Lotes/latencia importan | Mucho más eficiente (CTranslate2, int8/float16) | Ya te basta whisper y no afinas rendimiento |
| **whisperX** | Subtítulos finos/diarización | Alineación palabra + speakers (wav2vec2+pyannote) | Solo quieres texto plano sin timings |

### ⚖️ ¿Cuál elegir? — Síntesis de voz (TTS)

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **supertonic** | Voz en tiempo real local | Baja latencia on-device (ONNX/WebGPU) | Priorizas fidelidad/clonación por encima de latencia |
| **VoxCPM** | Máxima fluidez/clonación | Sin tokenizador tradicional, prosodia natural | No tienes GPU o priorizas latencia mínima |
| **TTS (Coqui)** | Flexibilidad y multi-idioma | Toolkit completo (XTTS, VITS, Tacotron) reutilizable | Necesitas tiempo real puro o soporte comercial |
| **OmniVoice-Studio** | Suite todo-en-uno (646 idiomas) | Dictado + clonación + dubbing en una app local | Solo necesitas TTS simple por CLI/librería |

### 📝 whisper
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo. Cubre también identificación de idioma y traducción al inglés en la misma red.
**Por qué destaca:** es la referencia de facto del STT abierto, base de innumerables forks y servicios de transcripción; su robustez a ruido y acentos lo convirtió en el punto de partida habitual para cualquier pipeline de voz.
**Cómo funciona:** red Transformer encoder-decoder entrenada con audio supervisado a escala; corre sobre PyTorch y procesa el audio en ventanas de 30 s con desplazamiento. La CLI `whisper` genera SRT/VTT/JSON con timestamps.
**Instalación:** `pip install -U openai-whisper` (requiere ffmpeg en el sistema y PyTorch). El modelo se descarga al primer uso según `--model` (de `tiny` a `large`).
**Casos:** `whisper grabacion.mp3 --model medium` para SRT con timestamps · subtitulado automático de video · transcripción de reuniones y podcasts.
**Stack:** Python 3.9+, PyTorch — **Modelo/API:** local (modelos tiny→large), sin API de pago.
**Elige si:** quieres la referencia robusta y no te obsesiona la latencia — **Evita si:** necesitas más velocidad ([faster-whisper](#-faster-whisper)) o timings por palabra ([whisperX](#-whisperx)).
**Combina con:** [whisperX](#-whisperx) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/openai/whisper)

### ⚡ faster-whisper
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión. Es el mismo modelo de OpenAI, pero con un runtime de inferencia optimizado.
**Por qué destaca:** es la versión preferida en producción por su relación velocidad/calidad y su bajo consumo; muy adoptada en pipelines y servidores de transcripción (WhisperX la usa internamente).
**Cómo funciona:** ejecuta los mismos modelos Whisper convertidos al runtime CTranslate2, con cuantización int8/float16 que acelera tanto CPU como GPU y reduce la VRAM necesaria frente al Whisper original.
**Instalación:** `pip install faster-whisper` (necesita ffmpeg). El modelo se descarga al primer uso; en GPU requiere drivers CUDA compatibles con CTranslate2.
**Casos:** procesar lotes de audio/video con menos latencia · transcripción en producción/servidor · reducir coste de GPU manteniendo calidad.
**Stack:** Python, CTranslate2 — **Modelo/API:** modelos Whisper locales.
**Elige si:** el rendimiento, la memoria o el coste de GPU importan — **Evita si:** necesitas alineación/diarización ([whisperX](#-whisperx)) o te basta el CLI oficial.
**Combina con:** [whisperX](#-whisperx)
**Repo:** [GitHub](https://github.com/SYSTRAN/faster-whisper)

### 🎯 whisperX
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. Convierte la salida "por segmento" de Whisper en timings palabra a palabra con etiqueta de speaker.
**Por qué destaca:** es la opción de referencia cuando los timings finos y el "quién habla" importan, muy usada para subtítulos de reels y entrevistas; combina tres componentes probados en un solo pipeline.
**Cómo funciona:** usa faster-whisper para la transcripción, modelos wav2vec2 (torchaudio) para forzar la alineación fonema/palabra y pyannote para la diarización de hablantes; todo orquestado desde Python.
**Instalación:** `pip install whisperx` (requiere PyTorch y, para diarización, un token de Hugging Face con acceso aceptado a los modelos pyannote).
**Casos:** subtítulos bien ajustados para reels/entrevistas · separar hablantes en podcasts · exportar SRT/VTT con timings de palabra.
**Stack:** Python, faster-whisper, wav2vec2, pyannote — **Modelo/API:** local.
**Elige si:** necesitas subtítulos precisos o diarización — **Evita si:** te basta texto plano ([whisper](#-whisper)) o no quieres gestionar tokens de HF.
**Combina con:** [whisper](#-whisper) · [moviepy](#-moviepy) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/m-bain/whisperX)

### 🔊 supertonic
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🟡 medio
**Qué es:** motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU. Apunta a latencia mínima con privacidad total, sin nube ni llamadas de API.
**Por qué destaca:** logra latencia muy baja con privacidad total al no depender de la nube, atractivo para voz en tiempo real y asistentes on-device; sus modelos se publican gratis en Hugging Face.
**Cómo funciona:** ejecuta modelos ONNX acelerados por WebGPU desde el navegador o por Rust/Python en escritorio, con inferencia optimizada para mantener el tiempo de primer audio bajo.
**Instalación:** clonar el repo y seguir el ejemplo Node/Python, o probar la demo WebGPU (no hay paquete único oficial). Requiere un navegador/entorno con WebGPU o runtime ONNX adecuado.
**Casos:** respuesta por voz en tiempo real · locuciones de anuncios local · asistentes on-device sin enviar audio a la nube.
**Stack:** Python, Rust (ONNX), Node.js, WebGPU — **Modelo/API:** modelos propios de Hugging Face, gratis.
**Elige si:** quieres voz local en tiempo real y sin nube — **Evita si:** priorizas clonación de máxima fidelidad ([VoxCPM](#-voxcpm)) o flexibilidad multi-modelo ([TTS](#-tts)).
**Combina con:** [whisperX](#-whisperx) · [moviepy](#-moviepy)
**Repo:** [GitHub](https://github.com/supertone-inc/supertonic)

### 🗣️ VoxCPM
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** sistema TTS de alta fidelidad de OpenBMB que prescinde del tokenizador tradicional para lograr una prosodia y fluidez muy naturales, con clonación de voz a partir de pocos segundos de audio. Pertenece a la familia CPM de modelos generativos de OpenBMB.
**Por qué destaca:** ofrece una naturalidad sobresaliente y clonación fiel con muy poco audio de referencia, dentro del ecosistema CPM de OpenBMB; su enfoque sin tokenizador reduce los artefactos típicos del TTS discreto.
**Cómo funciona:** modelo de difusión/autorregresivo sobre PyTorch que genera el habla en un espacio continuo en lugar de tokens discretos, modelando directamente la forma de onda; requiere GPU para inferencia en tiempo razonable.
**Instalación:** `pip install voxcpm` (o desde el repo) con PyTorch y GPU recomendada; los pesos se descargan al instanciar el modelo.
**Casos:** clonación de voz de alta calidad · locuciones muy naturales para narración · doblaje de video con voz propia.
**Stack:** Python, PyTorch, GPU — **Modelo/API:** modelos propios locales.
**Elige si:** quieres voz muy natural o clonada y tienes GPU — **Evita si:** priorizas latencia mínima ([supertonic](#-supertonic)) o no tienes GPU.
**Limitaciones:** GPU prácticamente obligatoria; inferencia más lenta que los TTS en tiempo real; revisar licencia antes de uso comercial.
**Combina con:** [TTS](#-tts)
**Repo:** [GitHub](https://github.com/OpenBMB/VoxCPM)

### 🎙️ TTS
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz. Reúne en una sola librería modelos como Tacotron, VITS y XTTS, con CLI y API Python.
**Por qué destaca:** es uno de los kits TTS abiertos más completos y reutilizados; aunque Coqui cerró, su código y modelos (XTTSv2, 16+ idiomas) siguen siendo referencia comunitaria y se mantienen vía fork `coqui-tts`.
**Cómo funciona:** librería Python que carga modelos sobre PyTorch y expone CLI (`tts`) y API para generar o clonar voz; XTTS permite clonación zero-shot a partir de unos segundos de referencia.
**Instalación:** `pip install TTS` (o `coqui-tts`, el fork mantenido). Requiere PyTorch; la clonación con XTTS mejora con GPU.
**Casos:** locuciones automáticas para anuncios/demos · clonación de voz zero-shot · base para apps de voz multilingües.
**Stack:** Python, PyTorch, modelos descargables — **Modelo/API:** local.
**Elige si:** quieres flexibilidad y varios modelos en una librería — **Evita si:** necesitas tiempo real puro ([supertonic](#-supertonic)) o soporte comercial (Coqui está inactivo).
**Limitaciones:** el proyecto original de Coqui está inactivo; usa el fork `coqui-tts` para fixes; revisar licencia de XTTS antes de uso comercial.
**Combina con:** [whisperX](#-whisperx) · [moviepy](#-moviepy)
**Repo:** [GitHub](https://github.com/coqui-ai/TTS)

### 🎚️ OmniVoice-Studio
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** suite de voz de escritorio open-source planteada como alternativa a ElevenLabs, con dictado en tiempo real, clonación zero-shot y doblaje de video en hasta 646 idiomas, todo local. Reúne STT, TTS y dubbing en una sola app sin claves de API.
**Por qué destaca:** combina dictado, clonación y dubbing en una sola app de escritorio sin nube ni API keys, algo poco común; está en beta activa y es un proyecto pequeño y poco conocido, conviene validarlo antes de depender de él.
**Cómo funciona:** envuelve modelos locales de STT y TTS en una interfaz de escritorio Python que orquesta transcripción, síntesis y reemplazo de audio en el video, manteniendo todo on-device.
**Instalación:** clonar el repo e instalar dependencias Python según el README (sin paquete publicado); el README recomienda correr desde fuente por estar en beta.
**Casos:** dictado de escritorio sin nube · doblar videos a otros idiomas · clonar voz sin API keys.
**Stack:** desktop/Python — **Modelo/API:** modelos locales.
**Elige si:** quieres suite de voz completa local (dictado + clonación + dubbing) — **Evita si:** solo necesitas TTS simple por CLI/librería ([TTS](#-tts)) o estabilidad de producción.
**Limitaciones:** beta activa: cosas pueden romperse entre releases; proyecto pequeño, valida mantenimiento antes de adoptarlo.
**Combina con:** [whisperX](#-whisperx)
**Repo:** [GitHub](https://github.com/debpalash/OmniVoice-Studio)

### ✂️ lossless-cut
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟢 fácil
**Qué es:** aplicación de escritorio para recortar, fusionar y reorganizar video/audio sin recodificar, conservando la calidad original. Es la "navaja suiza" del corte sin pérdida para cualquier formato que ffmpeg soporte.
**Por qué destaca:** es la herramienta de referencia para cortes sin pérdida, muy popular por su rapidez y por procesar archivos enormes al instante; distribuye binarios para Windows, macOS y Linux (también en Microsoft Store/Flatpak).
**Cómo funciona:** GUI Electron sobre ffmpeg que opera por copia de stream (sin recompresión), por lo que los cortes son casi instantáneos y sin pérdida; soporta también extracción de subtítulos y metadatos.
**Instalación:** descargar el binario para Windows/macOS/Linux desde releases (también vía Microsoft Store/Flatpak). No requiere GPU ni ffmpeg aparte (lo incluye).
**Casos:** preparar clips para reels/anuncios sin editor pesado · cortes rápidos sin pérdida · extraer pistas de audio/subtítulos de un contenedor.
**Stack:** Node.js/Electron, ffmpeg — **Modelo/API:** N/A.
**Elige si:** cortas material rápido y sin recomprimir — **Evita si:** necesitas edición compositiva, efectos o reencode ([moviepy](#-moviepy)).
**Combina con:** [moviepy](#-moviepy) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/mifi/lossless-cut)

### 🎬 moviepy
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería Python para edición de video programática: cortar, concatenar, superponer texto, subtítulos y audio, y exportar el resultado. Permite ensambrar video como si fueran objetos en código, ideal para pipelines reproducibles.
**Por qué destaca:** es la librería de edición de video más usada en Python, ideal para pipelines reproducibles y generación automatizada de clips; v2.0 modernizó la API (con breaking changes respecto a v1).
**Cómo funciona:** envuelve ffmpeg y NumPy/Pillow para manipular clips como objetos (`VideoFileClip`, `TextClip`, `CompositeVideoClip`) y renderizar el montaje final por código; cada clip tiene `subclip`, `resize`, `set_audio`, etc.
**Instalación:** `pip install moviepy` (incluye ffmpeg vía imageio-ffmpeg). Para subtítulos avanzados puede necesitar ImageMagick.
**Casos:** montar videos cortos desde imágenes, subtítulos y voz · overlays y texto por script · ensamblar reels a partir de TTS + imágenes.
**Stack:** Python, ffmpeg, NumPy/Pillow — **Modelo/API:** capa de ensamblaje final (no genera contenido, lo compone).
**Elige si:** ensamblas video por código en Python — **Evita si:** prefieres React/programático web ([remotion](#-remotion)) o una UI ([OpenCut](#-opencut)).
**Combina con:** [whisperX](#-whisperx) · [TTS](#-tts) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/Zulko/moviepy)

### ⚛️ remotion
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a MP4. Convierte el video en un artefacto versionable y parametrizable desde tu código frontend.
**Por qué destaca:** muy popular para generar video a escala y plantillas parametrizadas (uno de los proyectos de video-por-código más activos del ecosistema JS); permite crear miles de variantes cambiando props.
**Cómo funciona:** renderiza componentes React frame a frame con un navegador headless (Chromium) y los une con ffmpeg; las props alimentan las plantillas, y el reloj de Remotion sincroniza animaciones con el tiempo del video.
**Instalación:** `npm create video` (o `npm i remotion @remotion/cli`). Requiere Node y Chromium para render; el render final usa ffmpeg.
**Casos:** generar variantes de video a escala · plantillas de video programáticas para marketing · animaciones de datos sincronizadas con audio.
**Stack:** Node.js, React, Chromium, ffmpeg — **Modelo/API:** N/A.
**Elige si:** generas video a escala con React y quieres variantes parametrizadas — **Evita si:** trabajas en Python ([moviepy](#-moviepy)) o buscas un editor visual.
**Combina con:** [Open-Generative-AI](#-open-generative-ai) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/remotion-dev/remotion)

### 📲 videofy_minimal
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟢 fácil
**Qué es:** herramienta minimalista (de Schibsted) que convierte contenido textual en videos cortos de forma local, sin pipeline complejo. Encadena TTS/STT y montaje en un solo flujo para pasar de texto a reel con lo mínimo.
**Por qué destaca:** prioriza la simplicidad para pasar de texto a reel rápido; es un proyecto pequeño y experimental, conviene revisar su estado antes de usarlo en serio.
**Cómo funciona:** combina TTS/STT y un montador de video local para sincronizar narración, texto y fondos en un clip corto, orquestando los pasos sin depender de servicios externos.
**Instalación:** clonar el repo e instalar dependencias Python/Node según el README (sin paquete publicado). Requiere los modelos TTS/STT que el proyecto utilice.
**Casos:** transformar noticias/contenido en reels · video corto rápido sin pipeline complejo · prototipos de texto-a-video local.
**Stack:** Python/Node — **Modelo/API:** local + TTS/STT.
**Elige si:** quieres reels simples ya, sin montar un pipeline entero — **Evita si:** necesitas variantes programáticas a escala ([remotion](#-remotion)) o control fino por código ([moviepy](#-moviepy)).
**Limitaciones:** proyecto pequeño y experimental; valida mantenimiento y calidad antes de depender de él.
**Combina con:** [whisper](#-whisper) · [supertonic](#-supertonic)
**Repo:** [GitHub](https://github.com/schibsted/videofy_minimal)

### 🎞️ OpenCut
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** editor de video open-source con UI moderna, planteado como alternativa libre tipo CapCut, usable en web o escritorio. Apunta a llevar la edición no lineal con plantillas y capas a un entorno abierto y sin ataduras de plataforma.
**Por qué destaca:** propuesta abierta y sin ataduras de plataforma que ha ganado tracción rápida como alternativa libre a editores propietarios (CapCut/Premiere); su UI moderna lo hace accesible para creadores no técnicos.
**Cómo funciona:** app web en TypeScript/Next.js que edita en el navegador y procesa video con ffmpeg (WebAssembly o binario local según el modo), manteniendo los proyectos como datos editables.
**Instalación:** usar la versión web o clonar el repo y `npm install && npm run dev`. El render final puede requerir el binario ffmpeg local según el modo.
**Casos:** edición de video con UI libre · cortes y montajes sin software propietario · edición colaborativa en navegador.
**Stack:** web/TS, Next.js, ffmpeg (WASM/local) — **Modelo/API:** N/A.
**Elige si:** quieres un editor libre con UI moderna, sin CapCut — **Evita si:** prefieres edición por código ([moviepy](#-moviepy)) o cortes sin pérdida ([lossless-cut](#-lossless-cut)).
**Combina con:** [lossless-cut](#-lossless-cut)
**Repo:** [GitHub](https://github.com/OpenCut-app/OpenCut)

### 🖥️ openscreen
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟢 fácil
**Qué es:** herramienta ligera de grabación de pantalla para screencasts y demos, basada en las APIs de captura del navegador. El proyecto original está archivado y continúa mediante un fork comunitario.
**Por qué destaca:** opción sencilla y abierta para capturar pantalla sin instalar software nativo; su estado archivado obliga a revisar el fork mantenido antes de adoptarla en serio.
**Cómo funciona:** app web en TypeScript que usa `getDisplayMedia` y demás APIs de captura del navegador para grabar pantalla (con o sin audio) y exportar el video, todo en cliente.
**Instalación:** clonar el repo (o el fork mantenido) y `npm install && npm run dev`. También puede usarse la versión desplegada si existe.
**Casos:** grabar screencasts/demos · capturar tutoriales · grabar una pestaña o ventana para documentación.
**Stack:** web/TS — **Modelo/API:** N/A.
**Elige si:** necesitas screencast simple desde el navegador — **Evita si:** quieres algo mantenido y estable (el original está archivado) o grabación fuera del navegador.
**Limitaciones:** el repo original está archivado; busca el fork comunitario activo antes de depender de él; la grabación depende de los permisos del navegador.
**Combina con:** [OpenCut](#-opencut)
**Repo:** [GitHub](https://github.com/lacymorrow/openscreen)

### 📄 Youtube2Webpage
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** script en Perl que genera una página web legible a partir de un video de YouTube, intercalando la transcripción de subtítulos con capturas de pantalla del momento citado. Convierte una charla en un artículo navegable con contexto visual.
**Por qué destaca:** automatiza el paso de charla a artículo combinando texto e imágenes sincronizadas; es una utilidad de nicho y poco conocida, pero efectiva para su propósito.
**Cómo funciona:** usa yt-dlp para descargar video y subtítulos y ffmpeg para extraer fotogramas en los timestamps relevantes, ensamblando todo en una página HTML estática con texto e imágenes alineadas.
**Instalación:** clonar el repo y ejecutar el script Perl con yt-dlp y ffmpeg instalados en el sistema. Requiere Perl y los binarios mencionados.
**Casos:** convertir una charla en artículo legible · documentar video como texto+imágenes · archivar contenido de YouTube como página estática.
**Stack:** Perl, yt-dlp, ffmpeg — **Modelo/API:** N/A.
**Elige si:** quieres video → artículo con transcripción y capturas — **Evita si:** necesitas edición de video o el contenido no tiene subtítulos.
**Combina con:** [whisper](#-whisper)
**Repo:** [GitHub](https://github.com/obra/Youtube2Webpage)

### 🎞️ hyperframes
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework npm para generar animaciones frame a frame de forma programática desde código. Da control fino sobre cada fotograma para producir secuencias exportables y componerlas en video.
**Por qué destaca:** da control a nivel de frame sobre la animación; es un proyecto pequeño y poco difundido (de HeyGen), conviene comprobar su madurez antes de apostar por él en producción.
**Cómo funciona:** librería TypeScript/Node que renderiza secuencias de frames programáticamente (cada frame es una función del tiempo) y los exporta como imágenes para componerlas en video con ffmpeg u otro montador.
**Instalación:** `npm i hyperframes` (o clonar el repo). El render final de frames a video requiere un montador externo (ffmpeg/remotion).
**Casos:** animaciones generadas por código · secuencias frame a frame para motion graphics · prototipos de animación paramétrica.
**Stack:** Node.js/TypeScript — **Modelo/API:** N/A.
**Elige si:** generas animación por frames con control por código — **Evita si:** prefieres video en React con reloj integrado ([remotion](#-remotion)) o edición visual.
**Limitaciones:** proyecto poco difundido; valida mantenimiento y docs antes de depender de él; el montaje final no es nativo.
**Combina con:** [remotion](#-remotion)
**Repo:** [GitHub](https://github.com/heygen-com/hyperframes)

---

## 13. Documentos & Presentaciones

Conversión de formatos, generación de slides y herramientas de PDF.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Elige si… | Setup |
|---|---|---|---|---|
| [markitdown](#-markitdown) | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. | 📚 | Alimentas LLMs con documentos de formatos variados. | 🟢 |
| [ppt-master](#-ppt-master) | Generador que transforma documentos de texto en presentaciones PowerPoint (.pptx) editables nativas, listas para abrir y ajustar en Office. | 🧩 | Quieres PPTX editable de Office rápido. | 🟢 |
| [pdfcraft](#-pdfcraft) | Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada. | 🖥️ | Manipulas PDFs con privacidad y sin instalar nada. | 🟢 |
| [reveal.js](#-revealjs) | Framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados. | 📚 | Quieres slides web por código, versionables. | 🟢 |

### 📝 markitdown
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. Es la puerta de entrada habitual para ingesta de documentos en pipelines RAG.
**Por qué destaca:** proyecto oficial de Microsoft muy adoptado como paso previo a LLMs, por su salida ordenada y su catálogo de convertidores y plugins; se integra fácil en flujos de ingesta por su CLI y API Python.
**Cómo funciona:** detecta el tipo de archivo y aplica el extractor adecuado (parsers de Office, OCR por modelos de visión, Whisper para audio), normalizando todo a Markdown estructurado con encabezados y tablas.
**Instalación:** `pip install markitdown` (o `pip install 'markitdown[all]'` para todos los formatos). Los convertidores de visión/audio requieren claves de API opcionales.
**Casos:** convertir carpetas de informes (XLSX/PDF) a `.md` · ingesta de datos para IA · preprocesar documentos antes de indexarlos en un vector store.
**Stack:** Python 3.8+ — **Modelo/API:** opcional (visión para OCR, Whisper para audio), agnóstico vía variables de entorno.
**Elige si:** alimentas LLMs con documentos de formatos variados — **Evita si:** ya tienes el texto limpio o necesitas fidelidad de layout total (no es un reconstructor de PDF).
**Combina con:** [ppt-master](#-ppt-master) · [open-notebook](#-open-notebook) · receta [Docs → presentaciones](#-9-documentos--presentaciones)
**Repo:** [GitHub](https://github.com/microsoft/markitdown)

### 📊 ppt-master
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🧩 motor/runtime · Setup 🟢 fácil
**Qué es:** generador que transforma documentos de texto en presentaciones PowerPoint (.pptx) editables nativas, listas para abrir y ajustar en Office. Sustituye el maquetado manual de slides por un borrador estructurado por un LLM.
**Por qué destaca:** entrega un PPTX realmente editable (formas y textos nativos) en lugar de un PDF plano, ahorrando el tedio de maquetar slides desde cero; útil para borradores rápidos a partir de un informe.
**Cómo funciona:** un LLM estructura el contenido en secciones y diapositivas (título, bullets, layout), y luego python-pptx genera el archivo .pptx con sus formas, textos y diseño aplicado a una plantilla.
**Instalación:** `git clone` del repo y `pip install -r requirements.txt`; requiere clave de API del modelo (Anthropic u OpenAI según configuración).
**Casos:** pasar un informe Markdown a un borrador de slides corporativos en segundos · generar una primera versión editable de una presentación a partir de notas.
**Stack:** Python, python-pptx — **Modelo/API:** Claude 3.5 Sonnet o GPT-4o para estructurar (vía API key).
**Elige si:** quieres PPTX editable de Office rápido — **Evita si:** prefieres slides web por código ([reveal.js](#-revealjs)) o control de diseño pixel-perfect.
**Combina con:** [markitdown](#-markitdown) · receta [Docs → presentaciones](#-9-documentos--presentaciones)
**Repo:** [GitHub](https://github.com/hugohe3/ppt-master)

### 📄 pdfcraft
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟢 fácil
**Qué es:** conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada. Apunta a ser la alternativa local y sin nube a los servicios online de PDF.
**Por qué destaca:** todo el procesamiento ocurre en tu navegador, así que los documentos nunca salen de tu equipo ni dependen de un servicio de pago; útil para manipular PDFs sensibles sin subirlos a terceros.
**Cómo funciona:** carga el PDF en el cliente y manipula sus páginas con librerías JS de PDF (p. ej. pdf-lib) en el propio navegador, sin subir nada a la nube; las operaciones son por página o por documento completo.
**Instalación:** abrir la web en el navegador, o `npm install` y ejecutar en local desde el repo. No requiere backend ni GPU.
**Casos:** combinar/dividir/convertir PDF sin subirlos a la nube · manipulación local de documentos sensibles · comprimir PDF antes de enviarlos.
**Stack:** web/TS — **Modelo/API:** N/A.
**Elige si:** manipulas PDFs con privacidad y sin instalar nada — **Evita si:** necesitas conversión a Markdown para IA ([markitdown](#-markitdown)) o edición de contenido (no solo manipulación de páginas).
**Combina con:** [markitdown](#-markitdown)
**Repo:** [GitHub](https://github.com/PDFCraftTool/pdfcraft)

### 🖥️ reveal.js
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados. Convierte las diapositivas en una página web versionable y reproducible por código.
**Por qué destaca:** estándar de facto para slides como código, muy popular y respaldado por una comunidad amplia y años de uso en producción; es la base de herramientas como Reveal y de innumerables charlas técnicas.
**Cómo funciona:** defines las diapositivas como elementos HTML anidados (`<section>`) y la librería JS las renderiza en el navegador con navegación por teclado, animaciones, modo orador y exportación a PDF.
**Instalación:** `npm install reveal.js` (o clonar el repo y abrir `index.html` en el navegador). Para exportar a PDF usa el modo de impresión del navegador.
**Casos:** slides web versionables como código · presentaciones interactivas en el navegador · decks técnicos con demos en vivo embebidas.
**Stack:** JavaScript/HTML — **Modelo/API:** N/A.
**Elige si:** quieres slides web por código, versionables — **Evita si:** necesitas PPTX editable en Office ([ppt-master](#-ppt-master)) o un editor visual de slides.
**Combina con:** [markitdown](#-markitdown)
**Repo:** [GitHub](https://github.com/hakimel/reveal.js)

---

