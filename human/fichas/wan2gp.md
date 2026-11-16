[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Video generativo y pipelines automáticos

# 🎬 WanGP

> App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modestas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.8k | NOASSERTION | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🔴 pesado · **MCP** 🔌 sí

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

WanGP, superapp local para modelos generativos abiertos «para GPU modestas», de @deepbeepmeep. Usa la WanGP Community License 2.0, propia (GitHub muestra NOASSERTION), y es gratuita para uso local, también en el trabajo. Es muy activa (~12k estrellas).

## ¿Qué hace?

Ejecuta modelos de vídeo (Wan 2.1/2.2, LTX-2, Hunyuan Video, LongCat…), imagen (Flux, Qwen Image, Z-Image…), audio y voz y 3D desde una interfaz web, con optimizaciones de memoria para GPU de gama media. Incluye un «Showrunner» para series con personajes y escenarios coherentes. Tiene interfaz MCP para que agentes externos usen todas sus funciones.

## ¿Cómo lo hace?

Se instala con PyTorch para CUDA y `requirements.txt` (también Pinokio u otros instaladores). Está optimizada para NVIDIA (RTX 30–50) y ROCm; no tiene ruta para Apple Silicon. El README avisa de servicios de terceros que usan su nombre sin afiliación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Interfaz MCP para que agentes manejen WanGP. (combinación por arquitectura) | Arranca WanGP con `--mcp` y añádelo al agente. |
| [Wan2.2](wan2-2.md) | Ejecuta los modelos Wan 2.2 con menos VRAM. | Descarga el modelo desde la interfaz. |
| [MoviePy](moviepy.md) | Montar en Python los clips generados. (combinación por arquitectura) | Exporta los clips y únelos con MoviePy. |
| [LosslessCut](lossless-cut.md) | Recortar resultados sin recodificar. (combinación por arquitectura) | Abre los vídeos en LosslessCut. |
| [HunyuanVideo 1.5](hunyuanvideo-1-5.md) | Wan2GP incluye Hunyuan Video 1.5 entre sus modelos para GPUs con poca VRAM. | Elige el modelo en la interfaz; los pesos se descargan aparte. |
| [HunyuanVideo](hunyuanvideo.md) | Combinación recíproca: HunyuanVideo lo enlaza como «Interfaz para GPU modestas con soporte de Hunyuan Video». | Orden indicado desde HunyuanVideo: Selecciona Hunyuan Video en WanGP. |

**Notas:** Alternativas (elige una): comfyui. Licencia propia, no OSI: revísala antes de redistribuir.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada manager-v0.1.17 (2026-11-12) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/deepbeepmeep/WanGP/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La app se ofrece sin cuota local; proveedores remotos de Deepy, modelos y recursos de búsqueda pueden costar |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Documenta Claude Code y Codex como proveedores remotos auxiliares; que algunos modelos quepan en 4 GB no garantiza que todos lo hagan |
| Coste | El coste depende del proveedor o la ruta. La app se ofrece sin cuota local; proveedores remotos de Deepy, modelos y recursos de búsqueda pueden costar |
| Equipo | Preparación según la ruta elegida. GPU compatible; Python y PyTorch según guía; pesos del modelo elegido |

Documenta Claude Code y Codex como proveedores remotos auxiliares; que algunos modelos quepan en 4 GB no garantiza que todos lo hagan

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- GPU compatible
- Python y PyTorch según guía
- pesos del modelo elegido

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/deepbeepmeep/Wan2GP/blob/main/docs/INSTALLATION.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar WanGP para mi objetivo y necesito pasos guiados. Lee https://github.com/deepbeepmeep/Wan2GP/blob/main/docs/INSTALLATION.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige un modelo pequeño admitido y genera un clip corto antes de activar Deepy o Showrunner.

**Qué comprobar:** Puedes comprobar memoria, duración y motor de cada tarea.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar varios modelos desde una interfaz
- Preparar clips locales con una GPU limitada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar varios modelos desde una interfaz; Preparar clips locales con una GPU limitada | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code y Codex como proveedores remotos auxiliares; que algunos modelos quepan en 4 GB no garantiza que todos lo hagan

## Stack y modelos

- **Stack:** GPU compatible; Python y PyTorch según guía; pesos del modelo elegido
- **Etiquetas:** `video` `image` `tts` `local` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ComfyUI](comfyui.md) | 147k | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. |

## Enlaces

- 🐙 GitHub: [deepbeepmeep/WanGP](https://github.com/deepbeepmeep/WanGP)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/deepbeepmeep/WanGP/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
