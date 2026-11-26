[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Restauración, upscaling y edición

# 🩹 rembg

> Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.5k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — pip o CLI; GPU opcional · corregido a mano

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

rembg, herramienta para quitar el fondo de imágenes en local, de @danielgatis. Licencia MIT. Es madura (~26k estrellas, v2.0.87) y la patrocina PhotoRoom.

## ¿Qué hace?

Elimina fondos con modelos de segmentación (u2net, isnet, BiRefNet, SAM y otros) desde la CLI, una librería de Python, un servidor HTTP o Docker. Procesa imágenes sueltas, carpetas y flujos.

## ¿Cómo lo hace?

Se instala con `pip install "rembg[cpu,cli]"` o con extras `[gpu]`/`[rocm]`, y requiere Python 3.11+. Usa ONNX Runtime; la GPU NVIDIA puede requerir CUDA y cuDNN. Los modelos se descargan la primera vez que se usan.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ComfyUI](comfyui.md) | Nodos de la comunidad para quitar fondos en flujos. (combinación por arquitectura) | Instala un nodo basado en rembg. |
| [Real-ESRGAN](real-esrgan.md) | Ampliar la imagen antes o después del recorte. (combinación por arquitectura) | Amplía primero si la imagen es pequeña. |
| [Gradio](gradio.md) | Interfaz web rápida para uso interno. (combinación por arquitectura) | Envuelve `remove()` en una app Gradio. |
| [CodeFormer](codeformer.md) | Combinación recíproca: CodeFormer lo enlaza como «Recortar el retrato restaurado. (combinación por arquitectura)». | Orden indicado desde CodeFormer: Restaura con CodeFormer y quita el fondo con rembg. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-06 · última versión publicada v2.0.87 (2026-11-06) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/danielgatis/rembg/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Los modelos ONNX locales no necesitan API; withoutbg es un backend Cloud de créditos; los pesos pueden tener licencias distintas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Elige CPU o GPU según tu entorno y comprueba el modelo activo; ejecutar rembg no implica que hayas elegido siempre una ruta local |
| Coste | El coste depende del proveedor o la ruta. Los modelos ONNX locales no necesitan API; withoutbg es un backend Cloud de créditos; los pesos pueden tener licencias distintas |
| Equipo | Preparación según la ruta elegida. Python compatible; CPU o backend GPU elegido; imagen propia; descarga inicial de modelo |

Elige CPU o GPU según tu entorno y comprueba el modelo activo; ejecutar rembg no implica que hayas elegido siempre una ruta local

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python compatible
- CPU o backend GPU elegido
- imagen propia
- descarga inicial de modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install "rembg[cpu,cli]" # for library + cli
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/danielgatis/rembg/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar rembg para mi objetivo y necesito pasos guiados. Lee https://github.com/danielgatis/rembg/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Quita el fondo de una imagen simple y guarda un PNG con transparencia.

**Qué comprobar:** Puedes abrir el PNG y revisar bordes sobre fondos claro y oscuro.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una foto de producto
- Crear un recorte para una composición

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una foto de producto; Crear un recorte para una composición | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Elige CPU o GPU según tu entorno y comprueba el modelo activo; ejecutar rembg no implica que hayas elegido siempre una ruta local

## Stack y modelos

- **Stack:** Python compatible; CPU o backend GPU elegido; imagen propia; descarga inicial de modelo
- **Etiquetas:** `image` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [danielgatis/rembg](https://github.com/danielgatis/rembg)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/danielgatis/rembg/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
