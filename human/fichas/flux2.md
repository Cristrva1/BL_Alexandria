[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Modelos, librerías y control

# 🌀 FLUX.2

> Código oficial de inferencia de los modelos abiertos FLUX.2 de Black Forest Labs para generar y editar imágenes, con variantes rápidas para GPU domésticas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.9k | Apache-2.0 | Python | 2026-11-15 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta local no necesita API; la mejora opcional de prompts puede usar un modelo por API de OpenRouter, y BFL ofrece su propia API de pago |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Se ejecuta en tu GPU con los pesos de Hugging Face; klein 4B es la variante pensada para tarjetas domésticas |
| Coste | El coste depende del proveedor o la ruta. Local sin pago por modelo con klein 4B; las variantes no comerciales necesitan licencia para uso comercial y la API de BFL se paga por uso |
| Equipo | GPU o infraestructura especializada. Python 3.12; GPU NVIDIA con CUDA; unos 8 GB de VRAM para klein 4B y bastante más para FLUX.2 [dev]; pesos desde Hugging Face |

Claude Code, Codex o Antigravity pueden ayudarte a instalarlo, pero las imágenes se generan en tu GPU o en la API de BFL

## Qué puedes hacer con él

Código oficial de inferencia de los modelos abiertos FLUX.2 de Black Forest Labs para generar y editar imágenes, con variantes rápidas para GPU domésticas.

## Por qué destaca

Usos propuestos: Generar imágenes de producto en tu propia GPU; Editar una foto combinando varias imágenes de referencia.

## Cómo funciona

FLUX.2 [klein] 4B usa Apache 2.0 y cabe en unos 8 GB de VRAM; klein 9B y FLUX.2 [dev] usan una licencia no comercial y [dev] necesita mucha más memoria

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.12
- GPU NVIDIA con CUDA
- memoria de vídeo según la variante
- pesos desde Hugging Face

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e . --extra-index-url https://download.pytorch.org/whl/cu129 --no-cache-dir
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/black-forest-labs/flux2/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FLUX.2 para mi objetivo y necesito pasos guiados. Lee https://github.com/black-forest-labs/flux2/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera una imagen pequeña con FLUX.2 [klein] 4B desde la CLI interactiva.

**Qué comprobar:** Obtienes la imagen y sabes qué variante y qué licencia usaste.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Generar imágenes de producto en tu propia GPU
- Editar una foto combinando varias imágenes de referencia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Generar imágenes de producto en tu propia GPU; Editar una foto combinando varias imágenes de referencia | Necesitas uso comercial con las variantes 9B o [dev] sin licencia, o no tienes GPU; revisa los límites antes de elegirlo |

**Limitaciones:** La licencia del código no cubre todos los pesos: revisa la de cada variante antes de un uso comercial. El código de referencia se probó en GPU de centro de datos

## Stack y modelos

- **Stack:** Python 3.12; GPU NVIDIA con CUDA; unos 8 GB de VRAM para klein 4B y bastante más para FLUX.2 [dev]; pesos desde Hugging Face
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 147k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |
| [diffusers](diffusers.md) | 34.9k | Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. |

## Enlaces

- 🐙 GitHub: [black-forest-labs/flux2](https://github.com/black-forest-labs/flux2)
- 🌐 Web: <https://bfl.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/black-forest-labs/flux2/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
