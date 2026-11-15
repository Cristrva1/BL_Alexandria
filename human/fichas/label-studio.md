[🏠 Inicio](../README.md) › [🖼️ Visión artificial, rostros y percepción](../categorias/28-vision-percepcion.md) › Visión por computador

# 👁️ Label Studio

> Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28.7k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Crea datasets para entrenar o evaluar modelos con interfaces de anotación configurables y preetiquetado con IA.

## Por qué destaca

Muy flexible y con soporte de casi cualquier tipo de dato.

## Cómo funciona

App web Django donde configuras interfaces de etiquetado en XML y conectas modelos para preetiquetar.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install label-studio
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/HumanSignal/label-studio/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Label Studio para mi objetivo y necesito pasos guiados. Lee https://github.com/HumanSignal/label-studio/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Etiquetar imágenes para YOLO
- Anotar textos para evaluación de LLM
- Transcribir audio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas crear datasets etiquetados | solo evalúas prompts; mira `promptfoo` |

## Stack y modelos

- **Stack:** Python, Django, React
- **Etiquetas:** `data` `vision` `training` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ultralytics YOLO](ultralytics.md) | 63.4k | Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar. |
| [SAM 2](sam2.md) | 20.1k | Segunda versión de Segment Anything de Meta, que segmenta y sigue objetos en imágenes y video. |

## Enlaces

- 🐙 GitHub: [HumanSignal/label-studio](https://github.com/HumanSignal/label-studio)
- 🌐 Web: <https://labelstud.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/HumanSignal/label-studio/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
