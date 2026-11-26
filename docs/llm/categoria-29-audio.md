# Alexandría para agentes · Procesamiento y limpieza de audio

Categoría 29 «Audio, transcripción, voz y música» › subcategoría `audio`. 7 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=29&sub=audio · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `audacity` | Editor y grabador de audio multipista libre para Windows, macOS y Linux, con… | 1 Básico | 67 | GPL-3.0 (mayoría de archivos GPL-2.0-or-later) (OSI copyleft) | sin grupo |
| `pyannote-audio` | Kit de PyTorch para diarización de hablantes (quién habla y cuándo) con modelos… | 3 Avanzado | 64 | MIT (OSI permisiva) | sin grupo |
| `ultimate-vocal-remover` | Aplicación de escritorio para separar voz e instrumentos de canciones con… | 3 Avanzado | 58 | MIT (OSI permisiva) | sin grupo |
| `demucs` | Modelo de separación de fuentes musicales (voz, batería, bajo y resto) con… | 3 Avanzado | 56 | MIT (OSI permisiva) | sin grupo |
| `earshot` | Herramientas locales de audio para que un agente escuche, analice y revise… | 2 Intermedio | 55 | MIT (OSI permisiva) | sin grupo |
| `rubberband` | Biblioteca de audio para modificar duración y tono de una grabación, integrada… | 2 Intermedio | 42 | GPL-2.0 (OSI copyleft) | sin grupo |
| `rnnoise` | Biblioteca de reducción de ruido de audio que utiliza una red neuronal para… | 2 Intermedio | 41 | BSD-3-Clause (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Audacity (`audacity`)

- **Repo:** https://github.com/audacity/audacity · GPL-3.0 (mayoría de archivos GPL-2.0-or-later) · nivel 1 · 67/100
- **Qué es:** Editor de audio libre (GPLv3; la mayoría de archivos GPLv2 o posterior) mantenido por el equipo de Audacity con apoyo de Muse Group. Referencia histórica en edición de audio libre.
- **Cuándo elegirlo:** Casos: limpiar, cortar y normalizar una grabación de voz o podcast; editar stems separados con IA antes de mezclarlos.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; C++, CMakeLists.txt; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/audacity/audacity/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga Audacity desde su web, graba o importa un audio y aplica reducción de ruido y normalización. Éxito: Exportas un MP3 o WAV más limpio.
- **Combina con:** `ffmpeg` [12/edicion], `demucs`, `whisper-cpp` [29/stt], `audiocraft` [29/musica], `yue` [29/musica]

### pyannote.audio (`pyannote-audio`)

- **Repo:** https://github.com/pyannote/pyannote-audio · MIT · nivel 3 · 64/100
- **Qué es:** Kit de diarización de hablantes en Python sobre PyTorch (organización pyannote; pyannoteAI ofrece el servicio premium). Licencia MIT para el código; los modelos se publican en Hugging Face con condiciones propias.
- **Cuándo elegirlo:** Casos: Separar por hablante la grabación de una reunión; Añadir hablantes a una transcripción.
- **Requisitos:** nivel 3: preparación media, requiere programar con él, necesita GPU; Jupyter Notebook, pyproject.toml; hardware model_dependent; API de IA: opcional; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install pyannote.audio` — fuente: https://github.com/pyannote/pyannote-audio/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta community-1 sobre un audio corto con dos voces de prueba Éxito: Los segmentos alternan entre dos hablantes con marcas de tiempo coherentes
- **Combina con:** `whisperx` [29/stt], `pytorch` [24/entrenamiento], `faster-whisper` [29/stt], `ffmpeg` [12/edicion], `sherpa-onnx` [29/stt]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Diarizar personas tiene implicaciones de privacidad: informa a los participantes. Las cifras del README (DER, velocidad en H100) son del autor.

### Ultimate Vocal Remover (UVR) (`ultimate-vocal-remover`)

- **Repo:** https://github.com/Anjok07/ultimatevocalremovergui · MIT · nivel 3 · 58/100
- **Qué es:** Aplicación de código abierto (MIT) de Anjok07 y aufr33, referencia popular para separar voces. La última versión publicada es la v5.6 (2023); el README remite a una actualización de desarrollo de octubre de 2026.
- **Cuándo elegirlo:** Casos: obtener la pista instrumental o la voz aislada de una canción propia; preparar stems para remezclar o practicar con una canción.
- **Requisitos:** nivel 3: preparación sencilla, app o instalador listo para usar, necesita GPU; Python, requirements.txt; hardware model_dependent; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Anjok07/ultimatevocalremovergui/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Descarga el instalador para tu sistema desde las releases, abre una canción y separa con un modelo MDX-Net. Éxito: Obtienes dos archivos: voz e instrumental.
- **Combina con:** `ffmpeg` [12/edicion], `rubberband`, `demucs`

### Demucs (`demucs`)

- **Repo:** https://github.com/adefossez/demucs · MIT · nivel 3 · 56/100
- **Qué es:** Versión mantenida oficialmente por Alexandre Défossez, autor de Demucs, tras dejar Meta (y archivarse facebookresearch/demucs). El código es MIT. El propio autor avisa de que no trabaja activamente en él: respuestas lentas y sin funciones…
- **Cuándo elegirlo:** Casos: separar la voz y la batería de una canción propia para remezclar; generar stems para karaoke o práctica musical.
- **Requisitos:** nivel 3: preparación sencilla, requiere programar con él, necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `python3 -m pip install -U demucs` — fuente: https://github.com/adefossez/demucs/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `python3 -m pip install -U demucs` y ejecuta `demucs cancion.mp3`. Éxito: Obtienes una carpeta con las pistas separadas (drums, bass, vocals, other).
- **Combina con:** `ffmpeg` [12/edicion], `pytorch` [24/entrenamiento], `ultimate-vocal-remover`, `audacity`

### earshot (`earshot`)

- **Repo:** https://github.com/Leonxlnx/earshot · MIT · nivel 2 · 55/100
- **Qué es:** earshot, «oídos para agentes de código»: herramientas locales de análisis de audio, de @Leonxlnx. Licencia MIT. Es muy reciente (octubre de 2026, ~4.9k estrellas, v0.4.1).
- **Cuándo elegirlo:** Casos: Revisar una mezcla con un agente; Analizar un efecto sonoro.
- **Requisitos:** nivel 2: preparación media; Python; uv; espacio para modelos CPU; audio propio; cliente MCP opcional; hardware prerequisites; API de IA: opcional; Python; uv; espacio para modelos CPU; audio propio; cliente MCP opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/Leonxlnx/earshot/blob/main/README.md

  ```bash
  uv tool install "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"
  earshot doctor --fetch     # downloads the two models now (~1.1 GB)
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta doctor y analiza un clip corto antes de solicitar modificaciones o generar sonidos Éxito: Puedes revisar informe, segmentos y archivo original
- **Combina con:** `claude-code` [20/terminal], `remotion` [30/motores], `ffmpeg` [12/edicion]
- **Riesgos y avisos:** Sin alternativas declaradas. Expone MCP y conserva rutas offline; el material de referencia de pago no viene incluido y hay que aportar grabaciones autorizadas.

### rubberband (`rubberband`)

- **Repo:** https://github.com/breakfastquay/rubberband · GPL-2.0 · nivel 2 · 42/100
- **Qué es:** Rubber Band Library, biblioteca y utilidad para estirar el tiempo y cambiar el tono de audio, de Chris Cannam (Breakfast Quay). Licencia GPL-2.0+, con licencia comercial disponible.
- **Cuándo elegirlo:** Casos: Ajustar duración de una narración; Explorar cambio de tono.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Biblioteca o utilidad compilada; libsndfile; audio de prueba; hardware prerequisites; API de IA: no; Biblioteca o utilidad compilada; libsndfile; audio de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/breakfastquay/rubberband/blob/default/README.md
- **Primera prueba propuesta (no ejecutada):** Cambia ligeramente el tempo de una copia de audio y compara duración y artefactos Éxito: Puedes reconocer qué cambió en tiempo y tono
- **Combina con:** `ffmpeg` [12/edicion], `ace-step-1.5` [29/musica], `audiocraft` [29/musica], `ultimate-vocal-remover`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Es procesamiento de señal, no clonación de voz; los parámetros de ejemplo son marcadores y deben sustituirse con valores reales.

### rnnoise (`rnnoise`)

- **Repo:** https://github.com/xiph/rnnoise · BSD-3-Clause · nivel 2 · 41/100
- **Qué es:** RNNoise, biblioteca de supresión de ruido basada en una red neuronal recurrente, de Xiph.Org (algoritmo de Jean-Marc Valin). Licencia BSD-3-Clause. Es madura y estable (~6k estrellas, v0.2) y no cambia desde febrero de 2025.
- **Cuándo elegirlo:** Casos: Reducir ruido de una grabación; Estudiar una red de supresión de ruido.
- **Requisitos:** nivel 2: preparación media; Compilador y autotools; modelo descargado; audio RAW mono 16-bit 48 kHz; hardware prerequisites; API de IA: no; Compilador y autotools; modelo descargado; audio RAW mono 16-bit 48 kHz.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/xiph/rnnoise/blob/main/README
- **Primera prueba propuesta (no ejecutada):** Procesa una copia corta de audio con ruido y escucha si mejora sin deformar la voz Éxito: Puedes comparar original y salida y verificar formato
- **Combina con:** `ffmpeg` [12/edicion], `obs-studio` [12/edicion], `whisper-cpp` [29/stt]
- **Riesgos y avisos:** Sin alternativas declaradas. La demo recibe y devuelve PCM RAW, no WAV; autogen descarga archivos de modelo y GitHub es una copia de conveniencia del repositorio Xiph.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-29-audio.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Procesamiento y limpieza de audio», lee `docs/alexandria/categoria-29-audio.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-29-audio.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
