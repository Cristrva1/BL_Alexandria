# Alexandría para agentes · Rostros y retratos animados

Categoría 28 «Visión artificial, rostros y percepción» › subcategoría `rostros`. 5 repos. Generado el 2026-11-22 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=28&sub=rostros · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `deep-live-cam` | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen… | 3 Avanzado | 75 | AGPL-3.0 (OSI copyleft) | recomendado |
| `deepface` | Biblioteca Python ligera de reconocimiento facial y análisis de atributos… | 3 Avanzado | 70 | MIT (OSI permisiva) | sin grupo |
| `facefusion` | Plataforma para intercambio y mejora de rostros en imágenes y video. | 2 Intermedio | 56 | OpenRAIL-AS (source-available) | alternativa |
| `insightface` | Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación. | 2 Intermedio | 54 | — (sin licencia detectada) | sin grupo |
| `liveportrait` | Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento… | 3 Avanzado | 50 | MIT (source-available) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Deep-Live-Cam (`deep-live-cam`)

- **Repo:** https://github.com/hacksider/Deep-Live-Cam · AGPL-3.0 · nivel 3 · 75/100 · recomendado en «Intercambio de rostros»
- **Qué es:** Deep-Live-Cam, herramienta de intercambio de rostros (face swap) y deepfake en tiempo real a partir de una sola imagen, de @hacksider. Licencia AGPL-3.0.
- **Cuándo elegirlo:** Casos: Estudiar un efecto facial consentido; Probar un pipeline local de video.
- **Requisitos:** nivel 3: preparación pesada; Python compatible; FFmpeg; modelos ONNX; CPU o GPU según backend; imágenes autorizadas; hardware prerequisites; API de IA: no; Python compatible; FFmpeg; modelos ONNX; CPU o GPU según backend; imágenes autorizadas.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone --depth 1 https://github.com/hacksider/Deep-Live-Cam.git` — fuente: https://github.com/hacksider/Deep-Live-Cam/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Prueba con imágenes propias o autorizadas y revisa artefactos en una salida corta etiquetada como sintética Éxito: Puedes comparar original y resultado y reconocer errores visibles
- **Combina con:** `insightface`, `obs-studio` [12/edicion], `codeformer` [11/edicion]
- **Alternativas:** `facefusion`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): facefusion. Riesgo ético y legal alto (suplantación). El autor advierte instalación técnica; los pesos de reconocimiento o intercambio pueden tener restricciones no comerciales aunque el código sea accesible.

### DeepFace (`deepface`)

- **Repo:** https://github.com/serengil/deepface · MIT · nivel 3 · 70/100
- **Qué es:** Biblioteca de código abierto (MIT) creada por Sefik Ilkin Serengil. Muy popular y activa; su autor ofrece además una API gestionada (deepface.dev).
- **Cuándo elegirlo:** Casos: verificar si dos fotos propias o autorizadas corresponden a la misma persona; buscar una cara dentro de una carpeta de imágenes con consentimiento de las personas.
- **Requisitos:** nivel 3: preparación sencilla, requiere programar con él, necesita GPU; Python, Dockerfile, setup.py; hardware model_dependent; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install deepface` — fuente: https://github.com/serengil/deepface/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install deepface` y ejecuta `DeepFace.verify` con dos imágenes tuyas. Éxito: Obtienes un diccionario con `verified`, la distancia y el umbral usado.
- **Combina con:** `opencv` [28/vision], `dlib` [28/vision], `mediapipe` [28/vision], `ultralytics` [28/vision], `insightface`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Úsalo solo con imágenes propias o con consentimiento; la estimación de atributos como el origen étnico es sensible y puede tener sesgos.

### FaceFusion (`facefusion`)

- **Repo:** https://github.com/facefusion/facefusion · OpenRAIL-AS · nivel 2 · 56/100 · alternativa en «Intercambio de rostros»
- **Qué es:** FaceFusion, plataforma de manipulación facial (intercambio y mejora de rostros) para imágenes y vídeo. Licencia OpenRAIL-AS (GitHub muestra NOASSERTION). Tiene ~31k estrellas y está activa (3.9.2).
- **Cuándo elegirlo:** Casos: Preparar un efecto facial consentido; Evaluar un flujo local de imagen.
- **Requisitos:** nivel 2: preparación media; Sistema compatible; modelos; CPU o GPU; material autorizado; hardware prerequisites; API de IA: no; Sistema compatible; modelos; CPU o GPU; material autorizado.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/facefusion/facefusion` — fuente: https://docs.facefusion.io/installation
- **Primera prueba propuesta (no ejecutada):** Procesa una imagen de prueba y revisa bordes, color y artefactos antes de pasar a video Éxito: Puedes identificar modelo y limitaciones de la salida
- **Combina con:** `ffmpeg` [12/edicion], `insightface`, `real-esrgan` [11/edicion]
- **Alternativas:** `deep-live-cam`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): deep-live-cam. Riesgo ético y legal; licencia RAIL con restricciones de uso. La instalación desde fuente requiere conocimientos técnicos; no debe presentarse la disponibilidad del código como permiso comercial de todos los pesos.

### InsightFace (`insightface`)

- **Repo:** https://github.com/deepinsight/insightface · — · nivel 2 · 54/100
- **Qué es:** InsightFace, proyecto de análisis facial 2D y 3D mantenido por Jia Guo y Jiankang Deng. El código es MIT, pero los datos de entrenamiento y los modelos entrenados con ellos son solo para investigación no comercial; GitHub no detecta…
- **Cuándo elegirlo:** Casos: Estudiar alineación facial; Evaluar detección en un dataset de prueba.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; runtime ONNX; modelos con licencia adecuada; datos autorizados; hardware prerequisites; API de IA: no; Python; runtime ONNX; modelos con licencia adecuada; datos autorizados.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/deepinsight/insightface/blob/master/python-package/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta detección sobre una imagen propia y revisa resultados antes de usar comparaciones Éxito: Puedes identificar modelo, backend y caras detectadas
- **Combina con:** `facefusion`, `deep-live-cam`, `liveportrait`, `deepface`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Los pesos no permiten uso comercial. La licencia de código y modelos es distinta incluso en descargas automáticas; el paquete actual ofrece base y GUI con dependencias diferentes.

### LivePortrait (`liveportrait`)

- **Repo:** https://github.com/KlingAIResearch/LivePortrait · MIT · nivel 3 · 50/100
- **Qué es:** LivePortrait, sistema de animación de retratos con control de stitching y retargeting, del Kuaishou Visual Generation and Interaction Center (KlingAIResearch).
- **Cuándo elegirlo:** Casos: Crear una animación consentida de un retrato; Estudiar retargeting facial.
- **Requisitos:** nivel 3: preparación pesada; Conda; Python 3.10; PyTorch para tu sistema; FFmpeg; pesos; retrato y movimiento autorizados; hardware prerequisites; API de IA: no; Conda; Python 3.10; PyTorch para tu sistema; FFmpeg; pesos; retrato y movimiento autorizados.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/KlingAIResearch/LivePortrait/blob/main/readme.md

  ```bash
  git clone https://github.com/KlingTeam/LivePortrait
  cd LivePortrait
  
  # create env using conda
  conda create -n LivePortrait python=3.10
  conda activate LivePortrait
  ```
- **Primera prueba propuesta (no ejecutada):** Anima un retrato propio con un clip corto y compara expresión y bordes Éxito: Puedes reconocer movimiento transferido y defectos
- **Combina con:** `moviepy` [30/motores], `comfyui` [11/interfaces], `insightface`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Las alternativas CUDA del README no se instalan todas juntas; Animals mode tiene restricciones en macOS por X-Pose y los modelos externos conservan sus….

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-28-rostros.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Rostros y retratos animados», lee `docs/alexandria/categoria-28-rostros.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-28-rostros.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
