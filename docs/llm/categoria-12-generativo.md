# Alexandría para agentes · Video generativo y pipelines automáticos

Categoría 12 «Editar, grabar y generar video» › subcategoría `generativo`. 8 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=12&sub=generativo · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `moneyprinterturbo` | App que genera videos cortos a partir de un tema: guion con LLM, material de… | 2 Intermedio | 74 | MIT (OSI permisiva) | recomendado |
| `ltx-2` | Código oficial de inferencia y entrenamiento LoRA de LTX-2 y LTX-2.5, modelo… | 3 Avanzado | 68 | Apache-2.0 (OSI permisiva) | sin grupo |
| `wan2-2` | Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o… | 3 Avanzado | 67 | Apache-2.0 (OSI permisiva) | recomendado |
| `hunyuanvideo` | Modelo abierto de Tencent de 13B parámetros para generar video a partir de… | 3 Avanzado | 57 | Tencent Hunyuan Community License (source-available) | alternativa |
| `wan2gp` | App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan… | 3 Avanzado | 53 | WanGP Community License 2.0 (no OSI) (source-available) | sin grupo |
| `ai-youtube-shorts-generator` | Pipeline de Python que extrae clips verticales de videos de YouTube mediante… | 2 Intermedio | 48 | MIT (OSI permisiva) | sin grupo |
| `short-video-factory` | Aplicación de escritorio para crear videos cortos de producto combinando guion… | 2 Intermedio | 47 | AGPL-3.0 (OSI copyleft) | alternativa |
| `hunyuanvideo-1-5` | Modelo de video de Tencent de 8,3B parámetros que genera clips desde texto o… | 3 Avanzado | 42 | Tencent Hunyuan Community License (source-available) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### MoneyPrinterTurbo (`moneyprinterturbo`)

- **Repo:** https://github.com/harry0703/MoneyPrinterTurbo · MIT · nivel 2 · 74/100 · recomendado en «Generación automática de videos cortos»
- **Qué es:** MoneyPrinterTurbo, app para generar vídeos cortos a partir de un tema o palabra clave, de @harry0703. Licencia MIT. Es muy popular (~144k estrellas, v1.3.10) y su README está lleno de patrocinios y enlaces de afiliado a proveedores de…
- **Cuándo elegirlo:** Casos: Preparar un borrador de video de producto; Generar variantes de un tutorial propio.
- **Requisitos:** nivel 2: preparación media; Python; FFmpeg; proveedores de guion, voz e imágenes; material propio o autorizado; hardware prerequisites; API de IA: depends; Python; FFmpeg; proveedores de guion, voz e imágenes; material propio o autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README.md

  ```shell
  python -m pip install mpt
  mpt webui
  ```
- **Primera prueba propuesta (no ejecutada):** Crea un video corto de prueba con un guion revisado y comprueba voz, clips y subtítulos Éxito: Puedes rastrear el origen de cada recurso y corregir el resultado
- **Combina con:** `faster-whisper` [29/stt], `kokoro` [29/tts], `ollama` [8/motores]
- **Alternativas:** `short-video-factory`, `openmontage`, `videofy-minimal`
- **Riesgos y avisos:** Alternativas (elige una): openmontage, videofy-minimal, short-video-factory. Revisa los derechos del material de stock y de las voces antes de publicar. El adaptador Codex es del proyecto y no instala el CLI ni promete cobertura de cualquier modelo o cuenta; la imagen local no vuelve local todo el flujo.

### LTX-2 (`ltx-2`)

- **Repo:** https://github.com/Lightricks/LTX-2 · Apache-2.0 · nivel 3 · 68/100
- **Qué es:** Paquete oficial de inferencia y entrenador LoRA de Lightricks para el modelo audio-vídeo LTX-2, que alberga también LTX-2.5. El código es Apache-2.0 y los modelos tienen licencias propias.
- **Cuándo elegirlo:** Casos: generar clips cortos con audio a partir de texto o una imagen en una GPU propia; entrenar un LoRA de estilo o personaje para el modelo. Evítalo si no tienes el hardware o no aceptas la licencia de los pesos.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/Lightricks/LTX-2.git` — fuente: https://github.com/Lightricks/LTX-2/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repositorio, instala las dependencias, descarga los pesos de LTX-2.5 y ejecuta la DistilledPipeline con un prompt corto. Éxito: Se genera un clip de vídeo con audio en la carpeta de salida sin agotar la VRAM.
- **Combina con:** `comfyui` [11/interfaces], `ffmpeg` [12/edicion], `pytorch` [24/entrenamiento]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Revisa las licencias de los pesos antes de uso comercial.

### Wan2.2 (`wan2-2`)

- **Repo:** https://github.com/Wan-Video/Wan2.2 · Apache-2.0 · nivel 3 · 67/100 · recomendado en «Modelos abiertos de video generativo»
- **Qué es:** Wan2.2, familia de modelos abiertos de generación de vídeo de Alibaba (Wan-AI). Licencia Apache-2.0 para los modelos; no reclaman derechos sobre el contenido generado.
- **Cuándo elegirlo:** Casos: Prototipar una escena desde texto; Animar una imagen propia con un modelo local.
- **Requisitos:** nivel 3: preparación pesada; Python y PyTorch >=2.4; GPU; pesos y disco según variante; hardware prerequisites; API de IA: opcional; Python y PyTorch >=2.4; GPU; pesos y disco según variante.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Wan-Video/Wan2.2/blob/main/README.md

  ```sh
  git clone https://github.com/Wan-Video/Wan2.2.git
  cd Wan2.2

  # Ensure torch >= 2.4.0
  # If the installation of `flash_attn` fails, try installing the other packages first and install `flash_attn` last
  pip install -r requirements.txt
  ```
- **Primera prueba propuesta (no ejecutada):** Elige primero el modelo TI2V-5B y la ruta de memoria documentada y genera un clip breve Éxito: Puedes identificar pesos, tamaño, duración y recursos de la ejecución
- **Combina con:** `comfyui` [11/interfaces], `diffusers` [11/modelos], `cosyvoice` [29/tts], `real-esrgan` [11/edicion], `wan2gp`
- **Alternativas:** `hunyuanvideo`, `hunyuanvideo-1-5`
- **Riesgos y avisos:** Alternativas (elige una): hunyuanvideo, hunyuanvideo-1-5. El ejemplo 5B cita al menos 24 GB VRAM; otros ejemplos 14B citan 80 GB; no extrapoles esos mínimos a interfaces optimizadas de terceros.

### HunyuanVideo (`hunyuanvideo`)

- **Repo:** https://github.com/Tencent-Hunyuan/HunyuanVideo · Tencent Hunyuan Community License · nivel 3 · 57/100 · alternativa en «Modelos abiertos de video generativo»
- **Qué es:** HunyuanVideo, modelo abierto de generación de vídeo de 13B parámetros de Tencent Hunyuan. Usa la Tencent Hunyuan Community License, que excluye expresamente la UE, Reino Unido y Corea del Sur (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Estudiar generación local de video; Probar un prompt visual con pesos abiertos.
- **Requisitos:** nivel 3: preparación pesada; Python 3.10.9 y PyTorch según ruta; GPU grande; pesos y licencia; hardware prerequisites; API de IA: no; Python 3.10.9 y PyTorch según ruta; GPU grande; pesos y licencia.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull hunyuanvideo/hunyuanvideo:cuda_12` — fuente: https://github.com/Tencent-Hunyuan/HunyuanVideo/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Comprueba la resolución y memoria de la tabla antes de generar el ejemplo más pequeño viable Éxito: El clip y sus recursos se pueden comparar con la configuración elegida
- **Combina con:** `diffusers` [11/modelos], `comfyui` [11/interfaces], `wan2gp`
- **Alternativas:** `wan2-2`, `hunyuanvideo-1-5`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): wan2-2, hunyuanvideo-1-5. La licencia no aplica en la UE, Reino Unido ni Corea del Sur; para proyectos nuevos valora HunyuanVideo-1.5. La ruta original cita 45 GB VRAM para 544x960x129 y 60 GB para 720x1280x129; no es una instalación ligera para cualquier laptop.

### WanGP (`wan2gp`)

- **Repo:** https://github.com/deepbeepmeep/WanGP · WanGP Community License 2.0 (no OSI) · nivel 3 · 53/100
- **Qué es:** WanGP, superapp local para modelos generativos abiertos «para GPU modestas», de @deepbeepmeep. Usa la WanGP Community License 2.0, propia (GitHub muestra NOASSERTION), y es gratuita para uso local, también en el trabajo.
- **Cuándo elegirlo:** Casos: Probar varios modelos desde una interfaz; Preparar clips locales con una GPU limitada.
- **Requisitos:** nivel 3: preparación pesada; GPU compatible; Python y PyTorch según guía; pesos del modelo elegido; hardware prerequisites; API de IA: opcional; GPU compatible; Python y PyTorch según guía; pesos del modelo elegido.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/deepbeepmeep/WanGP.git` — fuente: https://github.com/deepbeepmeep/WanGP/blob/main/docs/GETTING_STARTED.md
- **Primera prueba propuesta (no ejecutada):** Elige un modelo pequeño admitido y genera un clip corto antes de activar Deepy o Showrunner Éxito: Puedes comprobar memoria, duración y motor de cada tarea
- **Combina con:** `claude-code` [20/terminal], `wan2-2`, `moviepy` [30/motores], `lossless-cut` [12/edicion], `hunyuanvideo-1-5`, `hunyuanvideo`
- **Alternativas:** `comfyui`
- **Riesgos y avisos:** Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): comfyui. Licencia propia, no OSI: revísala antes de redistribuir. Documenta Claude Code y Codex como proveedores remotos auxiliares; que algunos modelos quepan en 4 GB no garantiza que todos lo hagan.

### AI-Youtube-Shorts-Generator (`ai-youtube-shorts-generator`)

- **Repo:** https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator · MIT · nivel 2 · 48/100
- **Qué es:** AI YouTube Shorts Generator, pipeline en Python para extraer clips verticales de vídeos largos de YouTube, de @Anil-matcha. Licencia MIT. Tiene ~6k estrellas (sin releases) y lo «impulsa» MuAPI, cuyas APIs de pago se promocionan en el…
- **Cuándo elegirlo:** Casos: Obtener clips de un tutorial propio; Comparar criterios de selección de momentos.
- **Requisitos:** nivel 2: preparación media, requiere clave de API; Python; FFmpeg y dependencias locales si eliges ese modo; clave LLM; video autorizado; hardware prerequisites; API de IA: sí; Python; FFmpeg y dependencias locales si eliges ese modo; clave LLM; video autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator/blob/main/README.md

  ```bash
  git clone https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator.git
     cd AI-Youtube-Shorts-Generator

  pip install -r requirements.txt
     # Only if you plan to use --mode local:
     pip install -r requirements-local.txt
  ```
- **Primera prueba propuesta (no ejecutada):** Procesa un video propio corto y revisa los fragmentos propuestos antes de exportar Éxito: Puedes corregir puntos de corte, subtítulos y encuadre
- **Combina con:** `faster-whisper` [29/stt], `yt-dlp` [4/social], `ffmpeg` [12/edicion]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Respeta los derechos de autor y los términos de YouTube al reutilizar vídeos ajenos. Local no significa todo offline; las puntuaciones de viralidad son heurísticas del proyecto y no predicen vistas.

### short-video-factory (`short-video-factory`)

- **Repo:** https://github.com/YILS-LIN/short-video-factory · AGPL-3.0 · nivel 2 · 47/100 · alternativa en «Generación automática de videos cortos»
- **Qué es:** Short Video Factory (短视频工厂), app de escritorio para crear vídeos cortos de producto y contenido general, de @YILS-LIN. Licencia AGPL-3.0. Tiene ~6k estrellas (v1.4.0) y su README está principalmente en chino.
- **Cuándo elegirlo:** Casos: Crear un borrador de producto; Preparar variantes de un anuncio propio.
- **Requisitos:** nivel 2: preparación media; App de escritorio; proveedores de guion y voz; clips e imágenes propios; hardware prerequisites; API de IA: depends; App de escritorio; proveedores de guion y voz; clips e imágenes propios.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/YILS-LIN/short-video-factory/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Monta un borrador corto con un texto y tres clips ficticios o propios y revisa cada escena Éxito: El video exportado coincide con guion, voz y subtítulos corregidos
- **Combina con:** `edge-tts` [29/tts], `ffmpeg` [12/edicion], `ollama` [8/motores]
- **Alternativas:** `moneyprinterturbo`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativa (elige una): moneyprinterturbo. No se confirma aquí una ruta completamente local ni que la suscripción de un agente pague las funciones de generación.

### HunyuanVideo 1.5 (`hunyuanvideo-1-5`)

- **Repo:** https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5 · Tencent Hunyuan Community License · nivel 3 · 42/100 · alternativa en «Modelos abiertos de video generativo»
- **Qué es:** Modelo de generación de video de Tencent Hunyuan, publicado en noviembre de 2025 con código de inferencia y entrenamiento en Python. Usa la Tencent Hunyuan Community License (GitHub muestra NOASSERTION), que no se aplica en la UE, el Reino…
- **Cuándo elegirlo:** Casos: Generar un clip corto desde texto con GPU de consumo; Animar una imagen fija en 480p. Evítalo si no tienes una GPU NVIDIA con memoria suficiente o te afecta la exclusión territorial de la licencia.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; Python, requirements.txt; hardware gpu; API de IA: opcional; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5.git` — fuente: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Genera un clip de pocos segundos en 480p con offloading activado Éxito: El video se guarda y anotas tiempo y VRAM usados
- **Combina con:** `comfyui` [11/interfaces], `wan2gp`, `vllm` [23/serving]
- **Alternativas:** `wan2-2`, `hunyuanvideo`
- **Riesgos y avisos:** Alternativas (elige una): hunyuanvideo, wan2-2. Revisa la exclusión territorial y la política de uso aceptable antes de usarlo en un producto.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-12-generativo.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Video generativo y pipelines automáticos», lee `docs/alexandria/categoria-12-generativo.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-12-generativo.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
