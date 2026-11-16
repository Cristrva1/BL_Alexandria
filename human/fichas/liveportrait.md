[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Rostros y retratos animados

# 🧑 LivePortrait

> Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen (humanos, pero también mascotas).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.5k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 50/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** MIT. Los modelos de InsightFace que usa son solo para investigación no comercial. Fuente: [LICENSE](https://github.com/KlingAIResearch/LivePortrait/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

LivePortrait, sistema de animación de retratos con control de stitching y retargeting, del Kuaishou Visual Generation and Interaction Center (KlingAIResearch). El código es MIT (GitHub muestra NOASSERTION), pero depende de modelos de terceros con sus propias licencias, como InsightFace (no comercial). Tiene ~19k estrellas y no cambia desde junio de 2026.

## ¿Qué hace?

Transfiere expresiones y movimientos de un vídeo conductor a un retrato estático (humanos y animales) de forma eficiente. Permite editar ojos y labios y tiene interfaz Gradio.

## ¿Cómo lo hace?

Requiere PyTorch con CUDA (el README fija versiones como torch 2.3) y `pip install -r requirements.txt`; hay requisitos específicos para macOS. Los pesos se descargan de Hugging Face y existe un nodo comunitario para ComfyUI.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [MoviePy](moviepy.md) | Postproducción del vídeo resultante. (combinación por arquitectura) | Edita el resultado con MoviePy. |
| [ComfyUI](comfyui.md) | Nodo comunitario ComfyUI-LivePortraitKJ. | Instala el nodo en ComfyUI. |
| [InsightFace](insightface.md) | Detección facial por defecto. (combinación por arquitectura) | Viene como dependencia. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-06-01 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/KlingAIResearch/LivePortrait/blob/main/readme.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La ruta propia no necesita API; hardware, pesos y servicios de demo son independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Las alternativas CUDA del README no se instalan todas juntas; Animals mode tiene restricciones en macOS por X-Pose y los modelos externos conservan sus licencias |
| Coste | Sin pago a un modelo en la ruta básica. La ruta propia no necesita API; hardware, pesos y servicios de demo son independientes |
| Equipo | Preparación según la ruta elegida. Conda; Python 3.10; PyTorch para tu sistema; FFmpeg; pesos; retrato y movimiento autorizados |

Las alternativas CUDA del README no se instalan todas juntas; Animals mode tiene restricciones en macOS por X-Pose y los modelos externos conservan sus licencias

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Conda
- Python 3.10
- PyTorch para tu sistema
- FFmpeg
- pesos
- retrato y movimiento autorizados

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/KlingTeam/LivePortrait
cd LivePortrait

# create env using conda
conda create -n LivePortrait python=3.10
conda activate LivePortrait
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/KlingAIResearch/LivePortrait/blob/main/readme.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LivePortrait para mi objetivo y necesito pasos guiados. Lee https://github.com/KlingAIResearch/LivePortrait/blob/main/readme.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Anima un retrato propio con un clip corto y compara expresión y bordes.

**Qué comprobar:** Puedes reconocer movimiento transferido y defectos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear una animación consentida de un retrato
- Estudiar retargeting facial

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear una animación consentida de un retrato; Estudiar retargeting facial | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las alternativas CUDA del README no se instalan todas juntas; Animals mode tiene restricciones en macOS por X-Pose y los modelos externos conservan sus licencias

## Stack y modelos

- **Stack:** Conda; Python 3.10; PyTorch para tu sistema; FFmpeg; pesos; retrato y movimiento autorizados
- **Etiquetas:** `image` `vision` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait)
- 🌐 Web: <https://liveportrait.github.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/KlingAIResearch/LivePortrait/blob/main/readme.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
