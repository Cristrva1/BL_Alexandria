[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Modelos, librerías y control

# 🤗 diffusers

> Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 34.9k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; requiere programar con él; necesita GPU

**Puntuación de calidad** 78/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Diffusers, la librería de Hugging Face para modelos de difusión preentrenados. Licencia Apache-2.0. Es muy madura (~35k estrellas, v0.43.0).

## ¿Qué hace?

Ofrece pipelines listos para generar imágenes, vídeo y audio, schedulers intercambiables y modelos como bloques para crear sistemas propios. Soporta inferencia y entrenamiento (incluido LoRA), cuantización y descarga de modelos del Hub.

## ¿Cómo lo hace?

Se instala con `pip install --upgrade diffusers[torch]` (también hay soporte para Flax). Funciona sobre PyTorch en GPU, CPU o Apple Silicon y descarga pesos desde Hugging Face Hub.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FLUX.2](flux2.md) | Pipeline oficial de FLUX.2. | Carga el modelo con el pipeline FLUX.2. |
| [PEFT](peft.md) | Carga y entrenamiento de LoRA mediante PEFT. | Instala peft y usa `load_lora_weights`. |
| [Transformers](transformers.md) | Codificadores de texto y componentes compartidos. | Se instala como dependencia de muchos pipelines. |
| [cosmos](cosmos.md) | Probar modelos de mundo de NVIDIA con pipelines de difusión. (combinación por arquitectura) | Consulta si existe pipeline para el checkpoint elegido. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (4). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[HunyuanVideo](hunyuanvideo.md) · [InvokeAI](invokeai.md) · [PyTorch](pytorch.md) · [Wan2.2](wan2-2.md)

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.43.0 (2026-11-12) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/huggingface/diffusers/blob/main/README.md) · [2](https://huggingface.co/docs/diffusers/index) · [3](https://huggingface.co/docs/diffusers/main/en/api/pipelines/flux2)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca no obliga a API de pago; pesos, GPU y servicios alojados tienen condiciones separadas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Instalar Diffusers no descarga todos los modelos; elige el pipeline y comprueba su licencia y hardware |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca no obliga a API de pago; pesos, GPU y servicios alojados tienen condiciones separadas |
| Equipo | Preparación según la ruta elegida. Python y PyTorch; modelo y pipeline compatibles; GPU o memoria suficientes |

Instalar Diffusers no descarga todos los modelos; elige el pipeline y comprueba su licencia y hardware

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y PyTorch
- modelo y pipeline compatibles
- GPU o memoria suficientes

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install --upgrade diffusers[torch]
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/huggingface/diffusers/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar diffusers para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/diffusers/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga un pipeline sencillo y fija semilla y tamaño para producir una imagen de prueba.

**Qué comprobar:** Puedes guardar imagen y configuración del pipeline.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Integrar generación de imágenes en Python
- Experimentar con modelos de video o audio compatibles

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Integrar generación de imágenes en Python; Experimentar con modelos de video o audio compatibles | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Instalar Diffusers no descarga todos los modelos; elige el pipeline y comprueba su licencia y hardware

## Stack y modelos

- **Stack:** Python y PyTorch; modelo y pipeline compatibles; GPU o memoria suficientes
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [huggingface/diffusers](https://github.com/huggingface/diffusers)
- 🌐 Web: <https://huggingface.co/docs/diffusers>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/huggingface/diffusers/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
