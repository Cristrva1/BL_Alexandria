# 11. Generar y editar imágenes con IA — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `chainner`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=image,python,app,local

**Qué es:** Interfaz por nodos para encadenar procesamiento de imágenes con IA y clásico: escalado, restauración, conversión y lotes, en Windows, macOS y Linux.
**Stack:** Python, package.json, pyproject.toml, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/chaiNNer-org/chaiNNer

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/chaiNNer-org/chaiNNer/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: escalar y restaurar lotes de imágenes con varios modelos en cadena; crear flujos repetibles de conversión y retoque de imágenes
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala la release, deja que descargue su Python integrado e instala PyTorch o NCNN desde el gestor de dependencias; después escala una imagen con un modelo.
**Qué comprobar:** El flujo de nodos procesa la imagen y guarda el resultado sin errores.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `real-esrgan`, `pytorch`, `codeformer`

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
**Combina con:** `real-esrgan`, `comfyui`, `rembg`, `deep-live-cam`, `upscayl`, `chainner`

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
**Combina con:** `flux2`, `krita-ai-diffusion`, `real-esrgan`, `hunyuanvideo-1-5`
**Alternativas (elige una):** `wan2gp`

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
**Combina con:** `flux2`, `peft`, `transformers`, `cosmos`

## `flux2`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=image,python

**Qué es:** Código oficial de inferencia de los modelos abiertos FLUX.2 de Black Forest Labs para generar y editar imágenes, con variantes rápidas para GPU domésticas.
**Stack:** Python 3.12; GPU NVIDIA con CUDA; unos 8 GB de VRAM para klein 4B y bastante más para FLUX.2 [dev]; pesos desde Hugging Face
**Acceso y costes:**
- API de IA: API de IA opcional. La ruta local no necesita API; la mejora opcional de prompts puede usar un modelo por API de OpenRouter, y BFL ofrece su propia API de pago
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Se ejecuta en tu GPU con los pesos de Hugging Face; klein 4B es la variante pensada para tarjetas domésticas
- Coste: El coste depende del proveedor o la ruta. Local sin pago por modelo con klein 4B; las variantes no comerciales necesitan licencia para uso comercial y la API de BFL se paga por uso
- Equipo: GPU o infraestructura especializada. Python 3.12; GPU NVIDIA con CUDA; unos 8 GB de VRAM para klein 4B y bastante más para FLUX.2 [dev]; pesos desde Hugging Face
**Repo:** https://github.com/black-forest-labs/flux2

**Instalación** [+]:

```
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e . --extra-index-url https://download.pytorch.org/whl/cu129 --no-cache-dir
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Generar imágenes de producto en tu propia GPU; Editar una foto combinando varias imágenes de referencia
**Evita si:** Necesitas uso comercial con las variantes 9B o [dev] sin licencia, o no tienes GPU; revisa los límites antes de elegirlo
**Primera prueba propuesta:** Genera una imagen pequeña con FLUX.2 [klein] 4B desde la CLI interactiva
**Qué comprobar:** Obtienes la imagen y sabes qué variante y qué licencia usaste
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `comfyui`, `diffusers`, `real-esrgan`, `invokeai`, `krita-ai-diffusion`

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
**Combina con:** `diffusers`, `flux2`, `real-esrgan`
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
**Combina con:** `comfyui`, `flux2`, `real-esrgan`
**Alternativas (elige una):** `invokeai`

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
**Combina con:** `codeformer`, `comfyui`, `rembg`

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
**Combina con:** `comfyui`, `real-esrgan`, `gradio`, `codeformer`

## `upscayl`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=image,typescript,app,local

**Qué es:** Aplicación de escritorio libre para ampliar y mejorar imágenes con IA (Real-ESRGAN sobre NCNN Vulkan) en Linux, macOS y Windows.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/upscayl/upscayl

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/upscayl/upscayl/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: ampliar fotos antiguas o de baja resolución para imprimirlas; escalar en lote una carpeta de imágenes para una web
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala la release para tu sistema, abre una imagen pequeña y amplíala x4 con el modelo por defecto.
**Qué comprobar:** La imagen ampliada se guarda en la carpeta elegida con más detalle que el original.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `real-esrgan`, `gallery-dl`, `codeformer`
