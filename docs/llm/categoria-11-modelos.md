# Alexandría para agentes · Modelos, librerías y control

Categoría 11 «Generar y editar imágenes con IA» › subcategoría `modelos`. 2 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=11&sub=modelos · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `diffusers` | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de… | 3 Avanzado | 78 | Apache-2.0 (OSI permisiva) | sin grupo |
| `flux2` | Código oficial de inferencia de los modelos abiertos FLUX.2 de Black Forest… | 3 Avanzado | 47 | Apache-2.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### diffusers (`diffusers`)

- **Repo:** https://github.com/huggingface/diffusers · Apache-2.0 · nivel 3 · 78/100
- **Qué es:** Diffusers, la librería de Hugging Face para modelos de difusión preentrenados. Licencia Apache-2.0. Es muy madura (~35k estrellas, v0.43.0).
- **Cuándo elegirlo:** Casos: Integrar generación de imágenes en Python; Experimentar con modelos de video o audio compatibles.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él, necesita GPU; Python y PyTorch; modelo y pipeline compatibles; GPU o memoria suficientes; hardware prerequisites; API de IA: no; Python y PyTorch; modelo y pipeline compatibles; GPU o memoria suficientes.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install --upgrade diffusers[torch]` — fuente: https://github.com/huggingface/diffusers/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Carga un pipeline sencillo y fija semilla y tamaño para producir una imagen de prueba Éxito: Puedes guardar imagen y configuración del pipeline
- **Combina con:** `flux2`, `peft` [24/entrenamiento], `transformers` [24/entrenamiento], `cosmos` [24/modelos]
- **Riesgos y avisos:** Sin alternativas declaradas. Instalar Diffusers no descarga todos los modelos; elige el pipeline y comprueba su licencia y hardware.

### FLUX.2 (`flux2`)

- **Repo:** https://github.com/black-forest-labs/flux2 · Apache-2.0 · nivel 3 · 47/100
- **Qué es:** Código oficial de inferencia de los modelos FLUX.2 de Black Forest Labs. El código es Apache-2.0, pero los pesos tienen licencias distintas: los modelos 4B [klein] son Apache-2.0 y los 9B y FLUX.2 [dev] (32B) usan la FLUX Non-Commercial…
- **Cuándo elegirlo:** Casos: Generar imágenes de producto en tu propia GPU; Editar una foto combinando varias imágenes de referencia. Evítalo si Necesitas uso comercial con las variantes 9B o [dev] sin licencia, o no tienes GPU; revisa los límites antes de elegirlo.
- **Requisitos:** nivel 3: preparación pesada, necesita GPU; Python 3.12; GPU NVIDIA con CUDA; unos 8 GB de VRAM para klein 4B y bastante más para FLUX.2 [dev]; pesos desde Hugging Face; hardware gpu; API de IA: opcional; Python 3.12; GPU NVIDIA con CUDA; memoria de vídeo según la variante; pesos desde Hugging Face.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/black-forest-labs/flux2/blob/main/README.md

  ```bash
  python3.12 -m venv .venv
  source .venv/bin/activate
  pip install -e . --extra-index-url https://download.pytorch.org/whl/cu129 --no-cache-dir
  ```
- **Primera prueba propuesta (no ejecutada):** Genera una imagen pequeña con FLUX.2 [klein] 4B desde la CLI interactiva Éxito: Obtienes la imagen y sabes qué variante y qué licencia usaste
- **Combina con:** `comfyui` [11/interfaces], `diffusers`, `real-esrgan` [11/edicion], `invokeai` [11/interfaces], `krita-ai-diffusion` [11/interfaces]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Revisa la licencia de cada peso: varios no permiten uso comercial. La licencia del código no cubre todos los pesos: revisa la de cada variante antes de un uso comercial.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-11-modelos.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Modelos, librerías y control», lee `docs/alexandria/categoria-11-modelos.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-11-modelos.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
