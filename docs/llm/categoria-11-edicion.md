# Alexandría para agentes · Restauración, upscaling y edición

Categoría 11 «Generar y editar imágenes con IA» › subcategoría `edicion`. 5 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=11&sub=edicion · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `upscayl` | Aplicación de escritorio libre para ampliar y mejorar imágenes con IA… | 1 Básico | 70 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `rembg` | Herramienta para quitar el fondo de imágenes en local, por CLI, librería o… | 2 Intermedio | 68 | MIT (OSI permisiva) | sin grupo |
| `real-esrgan` | Modelo y herramientas de superresolución para ampliar y mejorar visualmente… | 2 Intermedio | 56 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `chainner` | Interfaz por nodos para encadenar procesamiento de imágenes con IA y clásico… | 2 Intermedio | 55 | GPL-3.0 (OSI copyleft) | sin grupo |
| `codeformer` | Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas. | 2 Intermedio | 40 | S-Lab License 1.0 (no comercial) (source-available) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Upscayl (`upscayl`)

- **Repo:** https://github.com/upscayl/upscayl · AGPL-3.0 · nivel 1 · 70/100
- **Qué es:** Aplicación de código abierto (AGPL-3.0) del proyecto Upscayl. Muy popular y con versiones frecuentes (v2.15 según el README).
- **Cuándo elegirlo:** Casos: ampliar fotos antiguas o de baja resolución para imprimirlas; escalar en lote una carpeta de imágenes para una web.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; TypeScript, package.json; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación (documentada en la fuente; no ejecutada):** `brew install --cask upscayl` — fuente: https://github.com/upscayl/upscayl/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala la release para tu sistema, abre una imagen pequeña y amplíala x4 con el modelo por defecto. Éxito: La imagen ampliada se guarda en la carpeta elegida con más detalle que el original.
- **Combina con:** `real-esrgan`, `gallery-dl` [4/social], `codeformer`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. La IA inventa detalles plausibles: no uses el resultado como evidencia documental.

### rembg (`rembg`)

- **Repo:** https://github.com/danielgatis/rembg · MIT · nivel 2 · 68/100
- **Qué es:** rembg, herramienta para quitar el fondo de imágenes en local, de @danielgatis. Licencia MIT. Es madura (~26k estrellas, v2.0.87) y la patrocina PhotoRoom.
- **Cuándo elegirlo:** Casos: Preparar una foto de producto; Crear un recorte para una composición.
- **Requisitos:** nivel 2: pip o CLI; GPU opcional; Python compatible; CPU o backend GPU elegido; imagen propia; descarga inicial de modelo; hardware prerequisites; API de IA: opcional; Python compatible; CPU o backend GPU elegido; imagen propia; descarga inicial de modelo.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install "rembg[cpu,cli]" # for library + cli` — fuente: https://github.com/danielgatis/rembg/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Quita el fondo de una imagen simple y guarda un PNG con transparencia Éxito: Puedes abrir el PNG y revisar bordes sobre fondos claro y oscuro
- **Combina con:** `comfyui` [11/interfaces], `real-esrgan`, `gradio` [25/apps], `codeformer`
- **Riesgos y avisos:** Sin alternativas declaradas. Elige CPU o GPU según tu entorno y comprueba el modelo activo; ejecutar rembg no implica que hayas elegido siempre una ruta local.

### Real-ESRGAN (`real-esrgan`)

- **Repo:** https://github.com/xinntao/Real-ESRGAN · BSD-3-Clause · nivel 2 · 56/100
- **Qué es:** Real-ESRGAN, modelo y herramientas de superresolución de imágenes y vídeo, de @xinntao (Tencent ARC). Licencia BSD-3-Clause. Es muy popular (~38k estrellas, v0.3.0), pero su último cambio es de agosto de 2024.
- **Cuándo elegirlo:** Casos: Preparar una ilustración para mayor tamaño; Mejorar visualmente una copia de material de baja resolución.
- **Requisitos:** nivel 2: preparación media; Python y PyTorch o binario ncnn compatible; modelo; imagen de prueba; hardware prerequisites; API de IA: no; Python y PyTorch o binario ncnn compatible; modelo; imagen de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/xinntao/Real-ESRGAN/blob/master/README.md

  ```bash
  git clone https://github.com/xinntao/Real-ESRGAN.git
      cd Real-ESRGAN

  # Install basicsr - https://github.com/xinntao/BasicSR
      # We use BasicSR for both training and inference
      pip install basicsr
      # facexlib and gfpgan are for face enhancement
      pip install facexlib
      pip install gfpgan
      pip install -r requirements.txt
      python setup.py develop
  ```
- **Primera prueba propuesta (no ejecutada):** Amplía una imagen propia y compara detalles y artefactos con la original Éxito: Puedes revisar tamaño de salida, nitidez y detalles inventados
- **Combina con:** `codeformer`, `comfyui` [11/interfaces], `rembg`
- **Riesgos y avisos:** Sin alternativas declaradas. Sin mantenimiento activo desde 2024. La superresolución generativa puede añadir detalles; no recupera de forma verificable información ausente en la imagen.

### chaiNNer (`chainner`)

- **Repo:** https://github.com/chaiNNer-org/chaiNNer · GPL-3.0 · nivel 2 · 55/100
- **Qué es:** Aplicación de código abierto (GPL-3.0) de la organización chaiNNer, nacida como herramienta de escalado con IA. Activa y multiplataforma.
- **Cuándo elegirlo:** Casos: escalar y restaurar lotes de imágenes con varios modelos en cadena; crear flujos repetibles de conversión y retoque de imágenes.
- **Requisitos:** nivel 2: preparación media, app o instalador listo para usar; Python, package.json, pyproject.toml, requirements.txt; API de IA: no; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/chaiNNer-org/chaiNNer/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala la release, deja que descargue su Python integrado e instala PyTorch o NCNN desde el gestor de dependencias; después escala una imagen con un modelo. Éxito: El flujo de nodos procesa la imagen y guarda el resultado sin errores.
- **Combina con:** `real-esrgan`, `pytorch` [24/entrenamiento], `codeformer`
- **Riesgos y avisos:** Algunos usuarios de NCNN con GPU no NVIDIA obtienen salidas negras por falta de memoria, según el README.

### CodeFormer (`codeformer`)

- **Repo:** https://github.com/sczhou/CodeFormer · S-Lab License 1.0 (no comercial) · nivel 2 · 40/100
- **Qué es:** CodeFormer, modelo de restauración ciega de rostros (NeurIPS 2022) de S-Lab, Nanyang Technological University. Licencia NTU S-Lab License 1.0, solo uso no comercial (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Experimentar con restauración de una fotografía; Comparar restauradores sobre material propio.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python y entorno indicado; PyTorch; pesos; imagen propia de prueba; hardware prerequisites; API de IA: no; Python y entorno indicado; PyTorch; pesos; imagen propia de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/sczhou/CodeFormer` — fuente: https://github.com/sczhou/CodeFormer/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Restaura una copia y compara dos ajustes de fidelidad con la foto original Éxito: Puedes observar el equilibrio entre parecido, limpieza y artefactos
- **Combina con:** `real-esrgan`, `comfyui` [11/interfaces], `rembg`, `deep-live-cam` [28/rostros], `upscayl`, `chainner`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Licencia no comercial. No copies como comando la anotación entre paréntesis de dlib en el README; los rasgos generados no prueban el aspecto original.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-11-edicion.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Restauración, upscaling y edición», lee `docs/alexandria/categoria-11-edicion.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-11-edicion.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
