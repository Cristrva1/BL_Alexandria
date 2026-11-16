[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 👁️ SAM 3

> Tercera versión de Segment Anything de Meta: detecta, segmenta y sigue en imágenes y video todos los objetos que describas con una frase corta.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.3k | SAM License | Python | 2026-11-15 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Puntuación de calidad** 52/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

SAM 3 (Segment Anything with Concepts), modelo de Meta Superintelligence Labs para detectar, segmentar y seguir objetos en imágenes y vídeo a partir de conceptos. Licencia «SAM License» propia (GitHub muestra NOASSERTION). Tiene ~12k estrellas y ya publicó checkpoints SAM 3.1.

## ¿Qué hace?

Segmenta todas las instancias de un concepto descrito con texto o ejemplos, además de prompts clásicos (puntos, cajas) y seguimiento en vídeo.

## ¿Cómo lo hace?

Requiere Python 3.12+, PyTorch 2.10 con CUDA y `pip install -e .` (extras para notebooks y entrenamiento; FlashAttention 3 es opcional). Antes hay que solicitar acceso a los checkpoints en Hugging Face.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Label Studio](label-studio.md) | Pre-etiquetado de máscaras. (combinación por arquitectura) | Conecta el modelo como backend de ML. |
| [supervision](supervision.md) | Visualizar y procesar máscaras. (combinación por arquitectura) | Convierte las máscaras a Detections. |
| [Ultralytics YOLO](ultralytics.md) | Combinar detección YOLO con segmentación por concepto. (combinación por arquitectura) | Usa las cajas como prompts. |

**Notas:** Sin alternativas declaradas. Pesos con acceso restringido.

Estado en GitHub: activo · último push 2026-11-13 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/facebookresearch/sam3/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API remota; los pesos se descargan desde Hugging Face tras aceptar la licencia SAM |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Se ejecuta en tu equipo con PyTorch y una GPU NVIDIA con CUDA 12.6 o superior |
| Coste | Sin pago a un modelo en la ruta básica. Sin pago por uso de un modelo; el coste es tu GPU o una GPU alquilada |
| Equipo | GPU o infraestructura especializada. Python 3.12 o superior; PyTorch 2.7 o superior; GPU con CUDA 12.6 o superior; cuenta de Hugging Face con acceso aprobado a los pesos |

Claude Code, Codex o Antigravity pueden ayudarte a instalarlo, pero el modelo se ejecuta en tu GPU

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.12 o superior
- PyTorch 2.7 o superior
- GPU con CUDA 12.6 o superior
- acceso aprobado a los pesos en Hugging Face

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/facebookresearch/sam3.git
cd sam3
pip install -e .
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/facebookresearch/sam3/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SAM 3 para mi objetivo y necesito pasos guiados. Lee https://github.com/facebookresearch/sam3/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Escribe «perro» como indicación en una foto con varios perros y revisa las máscaras.

**Qué comprobar:** Cada perro aparece con su propia máscara y caja, y puedes ver cuáles faltan o sobran.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Recortar todas las personas o productos de una foto con una frase
- Seguir un objeto descrito con texto a lo largo de un video

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Recortar todas las personas o productos de una foto con una frase; Seguir un objeto descrito con texto a lo largo de un video | No tienes una GPU NVIDIA compatible o necesitas una licencia permisiva como Apache; revisa los límites antes de elegirlo |

**Limitaciones:** Los pesos se descargan solo tras aprobarse la solicitud en Hugging Face; requiere GPU con CUDA y la licencia SAM tiene condiciones propias

## Stack y modelos

- **Stack:** Python 3.12 o superior; PyTorch 2.7 o superior; GPU con CUDA 12.6 o superior; cuenta de Hugging Face con acceso aprobado a los pesos
- **Etiquetas:** `vision` `video` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [facebookresearch/sam3](https://github.com/facebookresearch/sam3)
- 🌐 Web: <https://ai.meta.com/sam3>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/facebookresearch/sam3/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
