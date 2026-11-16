# Alexandría para agentes · Música y audio generativo

Categoría 29 «Audio, transcripción, voz y música» › subcategoría `musica`. 3 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=29&sub=musica · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `ace-step-1.5` | Modelo y herramientas para generar música localmente a partir de instrucciones… | 3 Avanzado | 70 | MIT (OSI permisiva) | recomendado |
| `yue` | Modelo abierto de generación de canciones completas (voz y acompañamiento) a… | 4 Experto | 67 | Apache-2.0 (OSI permisiva) | alternativa |
| `audiocraft` | Librería PyTorch de Meta para generar música y efectos de sonido desde texto… | 2 Intermedio | 54 | MIT (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### ACE-Step-1.5 (`ace-step-1.5`)

- **Repo:** https://github.com/ace-step/ACE-Step-1.5 · MIT · nivel 3 · 70/100 · recomendado en «Generación de música»
- **Qué es:** ACE-Step 1.5, modelo y herramientas open source para generar música en local, de ace-step (ACE Studio y StepFun). Licencia MIT. Tiene ~15k estrellas (v0.1.8); la serie XL (DiT de 4B) salió en abril de 2026.
- **Cuándo elegirlo:** Casos: Explorar una base musical de prueba; Comparar variantes de generación local.
- **Requisitos:** nivel 3: preparación pesada; Python 3.11–3.12; uv; modelo y equipo compatibles; espacio para descarga; hardware prerequisites; API de IA: no; Python 3.11–3.12; uv; modelo y equipo compatibles; espacio para descarga.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/ace-step/ACE-Step-1.5/blob/main/README.md

  ```bash
  # 2. Clone & install
  git clone https://github.com/ACE-Step/ACE-Step-1.5.git
  cd ACE-Step-1.5
  uv sync
  
  # 3. Launch Gradio UI (models auto-download on first run)
  uv run acestep
  ```
- **Primera prueba propuesta (no ejecutada):** Genera una pieza muy corta y revisa duración, coherencia y recursos consumidos Éxito: Puedes relacionar parámetros y salida
- **Combina con:** `vllm` [23/serving], `ffmpeg` [12/edicion], `rubberband` [29/audio]
- **Alternativas:** `yue`, `audiocraft`
- **Riesgos y avisos:** Sin alternativas declaradas. CUDA es recomendado y existen rutas MPS, ROCm, XPU o CPU; disponibilidad de una ruta no garantiza igual velocidad o memoria en todas.

### YuE2 (`yue`)

- **Repo:** https://github.com/multimodal-art-projection/YuE · Apache-2.0 · nivel 4 · 67/100 · alternativa en «Generación de música»
- **Qué es:** Modelo de investigación de código abierto del proyecto Multimodal Art Projection (M-A-P). Desde septiembre de 2026 el repositorio aloja YuE2; el YuE original se conserva en la rama YuE-v1.
- **Cuándo elegirlo:** Casos: generar una maqueta de canción con letra propia para un proyecto personal o académico; editar la armonía de una canción generada manteniendo la melodía. Evítalo si no tienes el hardware o no aceptas la licencia de los pesos.
- **Requisitos:** nivel 4: preparación difícil, necesita GPU; Python, pyproject.toml; hardware model_dependent; API de IA: no; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/multimodal-art-projection/YuE.git` — fuente: https://github.com/multimodal-art-projection/YuE/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** En Linux con una GPU NVIDIA de 24 GB, clona el repo, ejecuta `python -m pip install .` y genera una canción con `YuE2Pipeline`. Éxito: Obtienes un audio estéreo y la partitura ABC editable.
- **Combina con:** `claude-code` [20/terminal], `pytorch` [24/entrenamiento], `audacity` [29/audio]
- **Alternativas:** `ace-step-1.5`, `audiocraft`
- **Riesgos y avisos:** Alternativa abierta de ACE-Step 1.5 y AudioCraft (MusicGen). El README dice que YuE2 compite con Suno v5/v6 en WildSongBench [DATO NO VERIFICADO: benchmark del….

### AudioCraft (`audiocraft`)

- **Repo:** https://github.com/facebookresearch/audiocraft · MIT · nivel 2 · 54/100 · alternativa en «Generación de música»
- **Qué es:** AudioCraft, librería PyTorch de Meta para investigación en generación de audio (MusicGen y AudioGen). El código es MIT y los pesos son CC-BY-NC 4.0 (no comercial). Tiene ~24k estrellas y no cambia desde marzo de 2026.
- **Cuándo elegirlo:** Casos: Explorar generación de música; Estudiar sonidos a partir de texto.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python 3.9 y PyTorch 2.1 según guía; modelo; GPU según tamaño; texto propio; hardware prerequisites; API de IA: no; Python 3.9 y PyTorch 2.1 según guía; modelo; GPU según tamaño; texto propio.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install -U audiocraft` — fuente: https://github.com/facebookresearch/audiocraft/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Genera una muestra corta y compara su relación con el prompt sin publicar el resultado Éxito: Puedes identificar modelo, duración y artefactos
- **Combina con:** `ffmpeg` [12/edicion], `moviepy` [30/motores], `remotion` [30/motores], `rubberband` [29/audio], `audacity` [29/audio]
- **Alternativas:** `ace-step-1.5`, `yue`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Pesos no comerciales y dependencias antiguas. Los pesos publicados no permiten asumir uso comercial porque el código sea MIT; las alternativas de instalación del README no se ejecutan todas juntas.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-29-musica.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Música y audio generativo», lee `docs/alexandria/categoria-29-musica.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-29-musica.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
