[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Interfaces para generar imágenes

# 🖌️ InvokeAI

> Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29.1k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado

**Puntuación de calidad** 73/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Invoke (InvokeAI), suite creativa de IA para medios visuales, de Invoke AI. Licencia Apache-2.0. Es madura (~29k estrellas, v6.14.4).

## ¿Qué hace?

Ofrece una interfaz web profesional con lienzo unificado para generar, retocar (inpainting/outpainting), usar capas y regiones de control, y crear flujos con nodos. Gestiona modelos, LoRA y embeddings. Está pensado para uso profesional con licencia apta para empresas.

## ¿Cómo lo hace?

Se instala con el Launcher oficial en hardware compatible (GPU NVIDIA, AMD o Apple Silicon) o con Docker. Está escrito en Python (PyTorch, diffusers) con frontend React.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [diffusers](diffusers.md) | Ejecutar o entrenar fuera de la UI los mismos modelos. (combinación por arquitectura) | Usa diffusers para scripts y Invoke para trabajo visual. |
| [FLUX.2](flux2.md) | Usar modelos FLUX en el lienzo de Invoke. (combinación por arquitectura) | Instala el modelo desde el gestor de modelos si está soportado. |
| [Real-ESRGAN](real-esrgan.md) | Ampliar resultados finales. (combinación por arquitectura) | Exporta y amplía con Real-ESRGAN. |

**Notas:** Alternativas (elige una): krita-ai-diffusion.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v6.14.4 (2026-11-03) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/invoke-ai/InvokeAI/blob/main/README.md) · [2](https://invoke.ai/start-here/installation/)</sub>

## Ver similares

Grupo **Interfaces de creación de imágenes**: InvokeAI ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **InvokeAI** (esta ficha) ⭐ recomendado | 73 | Si buscas esto: suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables. |
| 2 | [Krita AI Diffusion](krita-ai-diffusion.md) | 55 | Si buscas esto: plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La edición local no necesita API de modelo; productos comerciales y modelos tienen condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La interfaz y sus modelos se preparan por separado; comienza con la instalación recomendada y un único modelo |
| Coste | El coste depende del proveedor o la ruta. La edición local no necesita API de modelo; productos comerciales y modelos tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Launcher o instalación oficial; modelo admitido; hardware según checkpoint |

La interfaz y sus modelos se preparan por separado; comienza con la instalación recomendada y un único modelo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Launcher o instalación oficial
- modelo admitido
- hardware según checkpoint

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/invoke-ai/InvokeAI/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar InvokeAI para mi objetivo y necesito pasos guiados. Lee https://github.com/invoke-ai/InvokeAI/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un canvas, genera una zona pequeña y conserva la imagen original en otra capa.

**Qué comprobar:** Puedes comparar la zona editada y sus parámetros.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Retocar una ilustración por regiones
- Organizar variantes de una producción visual

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Retocar una ilustración por regiones; Organizar variantes de una producción visual | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La interfaz y sus modelos se preparan por separado; comienza con la instalación recomendada y un único modelo

## Stack y modelos

- **Stack:** Launcher o instalación oficial; modelo admitido; hardware según checkpoint
- **Etiquetas:** `image` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Krita AI Diffusion](krita-ai-diffusion.md) | 10.9k | Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting. |

## Enlaces

- 🐙 GitHub: [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI)
- 🌐 Web: <https://invoke-ai.github.io/InvokeAI/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/invoke-ai/InvokeAI/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
