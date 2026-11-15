# 11. Generar y editar imágenes con IA — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `codeformer`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=image,vision,python

**Qué es:** Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas.
**Stack:** Python y entorno indicado; PyTorch; pesos; imagen propia de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La licencia NTU S-Lab restringe el uso y distingue uso no comercial; revisa autorización antes de una producción comercial
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. No copies como comando la anotación entre paréntesis de dlib en el README; los rasgos generados no prueban el aspecto original
- Coste: El coste depende del proveedor o la ruta. La licencia NTU S-Lab restringe el uso y distingue uso no comercial; revisa autorización antes de una producción comercial
- Equipo: Preparación según la ruta elegida. Python y entorno indicado; PyTorch; pesos; imagen propia de prueba
**Repo:** https://github.com/sczhou/CodeFormer

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/sczhou/CodeFormer/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Experimentar con restauración de una fotografía; Comparar restauradores sobre material propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Restaura una copia y compara dos ajustes de fidelidad con la foto original
**Qué comprobar:** Puedes observar el equilibrio entre parecido, limpieza y artefactos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `real-esrgan`
**Alternativas (elige una):** `gfpgan`

## `comfyui`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=image,python

**Qué es:** Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos.
**Stack:** Python o distribución elegida; modelo; RAM y GPU según workflow
**Acceso y costes:**
- API de IA: API de IA opcional. La ruta local usa tu equipo; Cloud y nodos API opcionales son de pago; los pesos tienen licencias propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El modo offline desactiva nodos API opcionales; importar un workflow puede exigir modelos o nodos adicionales
- Coste: El coste depende del proveedor o la ruta. La ruta local usa tu equipo; Cloud y nodos API opcionales son de pago; los pesos tienen licencias propias
- Equipo: Preparación según la ruta elegida. Python o distribución elegida; modelo; RAM y GPU según workflow
**Repo:** https://github.com/Comfy-Org/ComfyUI

**Instalación** [+]:

```
pip install comfy-cli
comfy install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un pipeline reproducible de imagen; Comparar dos ajustes del mismo modelo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga un workflow mínimo y conecta modelo, prompt, sampler y guardado
**Qué comprobar:** Obtienes una imagen y puedes identificar los nodos que la produjeron
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `real-esrgan`
**Alternativas (elige una):** `wan2gp`, `sd-webui-forge`

## `comfyui-ipadapter-plus`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=image,python

**Qué es:** Conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una o varias imágenes de referencia para transferir estilo o identidad.
**Stack:** ComfyUI compatible; custom node; pesos IPAdapter y encoder CLIP Vision adecuados
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa API en la ruta local; pesos y hardware tienen condiciones separadas
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Está en mantenimiento limitado desde abril de 2025; revisa compatibilidad de nodos, nombres de pesos y encoder antes de actualizar un flujo existente
- Coste: Sin pago a un modelo en la ruta básica. No usa API en la ruta local; pesos y hardware tienen condiciones separadas
- Equipo: Preparación según la ruta elegida. ComfyUI compatible; custom node; pesos IPAdapter y encoder CLIP Vision adecuados
**Repo:** https://github.com/cubiq/ComfyUI_IPAdapter_plus

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/cubiq/ComfyUI_IPAdapter_plus/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Transferir un estilo desde una referencia propia; Mantener una dirección visual entre variantes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga un workflow de ejemplo con una referencia propia y varía la intensidad de influencia
**Qué comprobar:** Puedes comparar qué rasgos visuales se conservan en cada salida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `comfyui`

## `controlnet`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=image,python

**Qué es:** Modelos que guían la generación de imágenes con poses, bordes, profundidad o segmentación.
**Stack:** Entorno del proyecto; modelo base y ControlNet compatibles; GPU
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia local no requiere API; pesos del modelo base y control tienen licencias y recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Este repositorio explica la implementación; la extensión WebUI y modelos 1.1 son proyectos o versiones relacionados con instalación distinta
- Coste: Sin pago a un modelo en la ruta básica. La inferencia local no requiere API; pesos del modelo base y control tienen licencias y recursos propios
- Equipo: Preparación según la ruta elegida. Entorno del proyecto; modelo base y ControlNet compatibles; GPU
**Repo:** https://github.com/lllyasviel/ControlNet

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/lllyasviel/ControlNet/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Guiar composición mediante bordes; Generar una ilustración a partir de una pose
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa un dibujo de bordes propio y compara generación con y sin ese control
**Qué comprobar:** Puedes observar cuánto se conserva la estructura del dibujo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `diffusers`, `comfyui`

## `diffusers`
role=library · exec=local · setup=heavy · mcp=False · prov=— · tags=image,python

**Qué es:** Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código.
**Stack:** Python y PyTorch; modelo y pipeline compatibles; GPU o memoria suficientes
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca no obliga a API de pago; pesos, GPU y servicios alojados tienen condiciones separadas
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Instalar Diffusers no descarga todos los modelos; elige el pipeline y comprueba su licencia y hardware
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca no obliga a API de pago; pesos, GPU y servicios alojados tienen condiciones separadas
- Equipo: Preparación según la ruta elegida. Python y PyTorch; modelo y pipeline compatibles; GPU o memoria suficientes
**Repo:** https://github.com/huggingface/diffusers

**Instalación** [+]:

```
pip install --upgrade diffusers[torch]
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Integrar generación de imágenes en Python; Experimentar con modelos de video o audio compatibles
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga un pipeline sencillo y fija semilla y tamaño para producir una imagen de prueba
**Qué comprobar:** Puedes guardar imagen y configuración del pipeline
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `controlnet`, `cosmos`

## `flux`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=image,python

**Qué es:** Repositorio oficial de inferencia de los modelos FLUX.1 de Black Forest Labs para generar imágenes.
**Stack:** Python 3.10; GPU y memoria según variante; pesos y permiso de acceso cuando corresponda
**Acceso y costes:**
- API de IA: API de IA opcional. schnell usa Apache-2.0; varias variantes dev tienen licencia no comercial y ofrecen licencia comercial; API BFL se factura por su ruta
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La licencia del repositorio no sustituye la del modelo; no se puede presentar toda la familia como uso comercial gratuito
- Coste: El coste depende del proveedor o la ruta. schnell usa Apache-2.0; varias variantes dev tienen licencia no comercial y ofrecen licencia comercial; API BFL se factura por su ruta
- Equipo: Preparación según la ruta elegida. Python 3.10; GPU y memoria según variante; pesos y permiso de acceso cuando corresponda
**Repo:** https://github.com/black-forest-labs/flux

**Instalación** [+]:

```
cd $HOME && git clone https://github.com/black-forest-labs/flux
cd $HOME/flux
python3.10 -m venv .venv
source .venv/bin/activate
pip install -e ".[all]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar imagen con FLUX.1 schnell; Comparar un modelo de edición con otro de generación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige primero una variante y licencia y genera una imagen pequeña con el ejemplo de texto a imagen
**Qué comprobar:** Puedes identificar exactamente el checkpoint usado y sus condiciones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `comfyui`, `diffusers`
**Alternativas (elige una):** `stable-diffusion-webui`

## `fooocus`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=image,python

**Qué es:** Herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes.
**Stack:** Distribución oficial; para mínimo Windows documentado NVIDIA 4 GB VRAM y 8 GB RAM; disco para modelos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere API para generación local; hardware y licencias de modelos son independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Descarga desde este repositorio y sus enlaces; sus notas de drivers y memoria son específicas y pueden ser antiguas, no instrucciones universales
- Coste: Sin pago a un modelo en la ruta básica. No requiere API para generación local; hardware y licencias de modelos son independientes
- Equipo: Preparación según la ruta elegida. Distribución oficial; para mínimo Windows documentado NVIDIA 4 GB VRAM y 8 GB RAM; disco para modelos
**Repo:** https://github.com/lllyasviel/Fooocus

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/lllyasviel/Fooocus/blob/main/readme.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Bocetar una imagen para una idea visual; Probar inpainting sin un grafo complejo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa un preset y un prompt sencillo y guarda imagen y ajustes
**Qué comprobar:** Puedes comparar dos variantes cambiando un solo ajuste
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `real-esrgan`

## `gfpgan`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=image,python

**Qué es:** Algoritmo de restauración facial de Tencent ARC que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados.
**Stack:** Python; PyTorch; BasicSR y facexlib; pesos; imagen propia de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere API de IA; pesos, hardware y cómputo tienen condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Los rasgos reconstruidos son estimaciones generadas y pueden cambiar la identidad aparente; no sirven para certificar detalles originales
- Coste: Sin pago a un modelo en la ruta básica. No requiere API de IA; pesos, hardware y cómputo tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Python; PyTorch; BasicSR y facexlib; pesos; imagen propia de prueba
**Repo:** https://github.com/TencentARC/GFPGAN

**Instalación** [+]:

```
git clone https://github.com/TencentARC/GFPGAN.git
    cd GFPGAN

# Install basicsr - https://github.com/xinntao/BasicSR
    # We use BasicSR for both training and inference
    pip install basicsr

    # Install facexlib - https://github.com/xinntao/facexlib
    # We use face detection and face restoration helper in the facexlib package
    pip install facexlib

    pip install -r requirements.txt
    python setup.py develop

    # If you want to enhance the background (non-face) regions with Real-ESRGAN,
    # you also need to install the realesrgan package
    pip install realesrgan
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Mejorar una copia visual de una fotografía; Estudiar restauración facial con un modelo preentrenado
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Restaura una copia de una foto y compara cara y fondo a tamaño completo
**Qué comprobar:** Puedes decidir si los detalles nuevos son aceptables sin perder el original
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `real-esrgan`
**Alternativas (elige una):** `codeformer`

## `invokeai`
role=app · exec=local · setup=heavy · mcp=False · prov=— · tags=image,typescript

**Qué es:** Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables.
**Stack:** Launcher o instalación oficial; modelo admitido; hardware según checkpoint
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La edición local no necesita API de modelo; productos comerciales y modelos tienen condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La interfaz y sus modelos se preparan por separado; comienza con la instalación recomendada y un único modelo
- Coste: El coste depende del proveedor o la ruta. La edición local no necesita API de modelo; productos comerciales y modelos tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Launcher o instalación oficial; modelo admitido; hardware según checkpoint
**Repo:** https://github.com/invoke-ai/InvokeAI

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/invoke-ai/InvokeAI/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Retocar una ilustración por regiones; Organizar variantes de una producción visual
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un canvas, genera una zona pequeña y conserva la imagen original en otra capa
**Qué comprobar:** Puedes comparar la zona editada y sus parámetros
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `diffusers`, `controlnet`
**Alternativas (elige una):** `krita-ai-diffusion`

## `krita-ai-diffusion`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=image,design,python

**Qué es:** Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting.
**Stack:** Krita compatible; plugin; servidor local o Cloud; GPU recomendada para local
**Acceso y costes:**
- API de IA: API de IA opcional. El servidor local consume tu equipo; Cloud tiene condiciones propias; modelos y descargas se presupuestan según ruta
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El autor recomienda al menos 6 GB VRAM NVIDIA para local; CPU es posible pero muy lenta; revisa soporte del backend de tu GPU
- Coste: El coste depende del proveedor o la ruta. El servidor local consume tu equipo; Cloud tiene condiciones propias; modelos y descargas se presupuestan según ruta
- Equipo: Preparación según la ruta elegida. Krita compatible; plugin; servidor local o Cloud; GPU recomendada para local
**Repo:** https://github.com/Acly/krita-ai-diffusion

**Instalación** [?]:

```
Seguir la instalación original: https://docs.interstice.cloud/installation
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Completar un fondo en una ilustración; Usar un boceto para guiar una imagen
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Selecciona una región de una imagen propia y genera una modificación en otra capa
**Qué comprobar:** Puedes aceptar o descartar la capa manteniendo el original
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `comfyui`
**Alternativas (elige una):** `invokeai`

## `open-generative-ai`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=image,video,javascript

**Qué es:** Reúne herramientas de generación de imagen y video. Los modelos alojados consumen servicios externos; la app de escritorio permite configurar motores locales independientes. Las rutas difieren en hardware, instalación, licencia de pesos y costes.
**Stack:** App de escritorio para modelos locales; sd.cpp o Wan2GP; GPU según modelo; clave MuAPI para servicios remotos
**Acceso y costes:**
- API de IA: API de IA opcional. Las rutas MuAPI consumen servicios; escritorio añade sd.cpp y Wan2GP propios; que la interfaz sea abierta no vuelve gratuitos todos sus modelos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Los modelos locales son función de escritorio; Wan2GP se instala aparte y exige GPU compatible, a diferencia del motor de imagen sd.cpp
- Coste: El coste depende del proveedor o la ruta. Las rutas MuAPI consumen servicios; escritorio añade sd.cpp y Wan2GP propios; que la interfaz sea abierta no vuelve gratuitos todos sus modelos
- Equipo: Preparación según la ruta elegida. App de escritorio para modelos locales; sd.cpp o Wan2GP; GPU según modelo; clave MuAPI para servicios remotos
**Repo:** https://github.com/Anil-matcha/Open-Generative-AI

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Anil-matcha/Open-Generative-AI/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar imagen local desde una interfaz; Comparar una ruta local con un servicio de video remoto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** En escritorio configura un modelo local pequeño y genera una imagen con el selector Local
**Qué comprobar:** Puedes identificar el motor local y comprobar que no se usó el proveedor remoto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `remotion`

## `real-esrgan`
role=runtime · exec=local · setup=medium · mcp=False · prov=— · tags=image,python

**Qué es:** Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible generación de detalles nuevos.
**Stack:** Python y PyTorch o binario ncnn compatible; modelo; imagen de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia local no exige API; hardware, modelos y procesamiento tienen recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La superresolución generativa puede añadir detalles; no recupera de forma verificable información ausente en la imagen
- Coste: Sin pago a un modelo en la ruta básica. La inferencia local no exige API; hardware, modelos y procesamiento tienen recursos propios
- Equipo: Preparación según la ruta elegida. Python y PyTorch o binario ncnn compatible; modelo; imagen de prueba
**Repo:** https://github.com/xinntao/Real-ESRGAN

**Instalación** [+]:

```
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

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una ilustración para mayor tamaño; Mejorar visualmente una copia de material de baja resolución
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Amplía una imagen propia y compara detalles y artefactos con la original
**Qué comprobar:** Puedes revisar tamaño de salida, nitidez y detalles inventados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `gfpgan`

## `rembg`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=image,python

**Qué es:** Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor.
**Stack:** Python compatible; CPU o backend GPU elegido; imagen propia; descarga inicial de modelo
**Acceso y costes:**
- API de IA: API de IA opcional. Los modelos ONNX locales no necesitan API; withoutbg es un backend Cloud de créditos; los pesos pueden tener licencias distintas
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Elige CPU o GPU según tu entorno y comprueba el modelo activo; ejecutar rembg no implica que hayas elegido siempre una ruta local
- Coste: El coste depende del proveedor o la ruta. Los modelos ONNX locales no necesitan API; withoutbg es un backend Cloud de créditos; los pesos pueden tener licencias distintas
- Equipo: Preparación según la ruta elegida. Python compatible; CPU o backend GPU elegido; imagen propia; descarga inicial de modelo
**Repo:** https://github.com/danielgatis/rembg

**Instalación** [+]:

```
pip install "rembg[cpu,cli]" # for library + cli
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar una foto de producto; Crear un recorte para una composición
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Quita el fondo de una imagen simple y guarda un PNG con transparencia
**Qué comprobar:** Puedes abrir el PNG y revisar bordes sobre fondos claro y oscuro
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `comfyui`

## `sd-webui-controlnet`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=vision,image,python

**Qué es:** Extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI (AUTOMATIC1111), con preprocesadores para poses, bordes, profundidad y más.
**Stack:** Stable Diffusion WebUI compatible; extensión; pesos de control y preprocesador
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API remota en la ruta local; cada modelo y GPU tienen sus condiciones
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Instalar la extensión no instala necesariamente todos los modelos; múltiples controles aumentan uso de memoria
- Coste: Sin pago a un modelo en la ruta básica. No necesita API remota en la ruta local; cada modelo y GPU tienen sus condiciones
- Equipo: Preparación según la ruta elegida. Stable Diffusion WebUI compatible; extensión; pesos de control y preprocesador
**Repo:** https://github.com/Mikubill/sd-webui-controlnet

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Mikubill/sd-webui-controlnet/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Conservar una composición al generar; Guiar una imagen mediante un boceto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga una referencia de bordes propia y habilita un solo ControlNet antes de generar
**Qué comprobar:** Puedes comparar estructura y parámetros en la WebUI
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `stable-diffusion-webui`, `controlnet`

## `sd-webui-forge`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=image,local,python

**Qué es:** Variante de Stable Diffusion WebUI que experimenta con gestión de recursos y optimización de inferencia; el rendimiento depende de la configuración.
**Stack:** Paquete o entorno compatible; GPU; checkpoint admitido
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API remota; hardware y modelos tienen requisitos y licencias propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La promesa de rapidez y ahorro depende de modelo, versión y equipo; el bloque Python del README es un ejemplo de extensión, no el instalador
- Coste: Sin pago a un modelo en la ruta básica. No necesita API remota; hardware y modelos tienen requisitos y licencias propios
- Equipo: Preparación según la ruta elegida. Paquete o entorno compatible; GPU; checkpoint admitido
**Repo:** https://github.com/lllyasviel/stable-diffusion-webui-forge

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/lllyasviel/stable-diffusion-webui-forge/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un checkpoint con gestión de memoria distinta; Comparar variantes de WebUI en una máquina
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera una imagen pequeña y compara memoria y tiempo con la misma configuración de referencia
**Qué comprobar:** Puedes medir recursos en tu equipo y revisar el resultado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `controlnet`
**Alternativas (elige una):** `stable-diffusion-webui`, `comfyui`

## `stable-diffusion-webui`
role=app · exec=local · setup=heavy · mcp=False · prov=— · tags=vision,image,python

**Qué es:** Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador.
**Stack:** Python y Git según ruta; GPU y checkpoint compatibles; espacio para pesos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia local no necesita API; hardware, modelos y extensiones tienen licencias y costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. En Windows sigue la preparación y webui-user.bat del autor; clonar no instala por sí solo todos los pesos y requisitos
- Coste: Sin pago a un modelo en la ruta básica. La inferencia local no necesita API; hardware, modelos y extensiones tienen licencias y costes propios
- Equipo: Preparación según la ruta elegida. Python y Git según ruta; GPU y checkpoint compatibles; espacio para pesos
**Repo:** https://github.com/AUTOMATIC1111/stable-diffusion-webui

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Bocetar una ilustración propia; Editar una región de una imagen de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera una imagen pequeña con un modelo y semilla identificados y guarda sus parámetros
**Qué comprobar:** Puedes repetir la generación con la misma configuración
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `sd-webui-controlnet`
**Alternativas (elige una):** `sd-webui-forge`, `flux`
