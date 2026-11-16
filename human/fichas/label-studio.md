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
| API de IA | API de IA opcional. Etiquetado manual sin API de IA; backend de modelos, hosting y ediciones comerciales pueden añadir costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La función básica es anotación humana; no necesita un modelo para empezar y los backends de ML se configuran por separado |
| Coste | El coste depende del proveedor o la ruta. Etiquetado manual sin API de IA; backend de modelos, hosting y ediciones comerciales pueden añadir costes |
| Equipo | Preparación según la ruta elegida. Docker o Python compatible; datos de muestra; almacenamiento persistente |

La función básica es anotación humana; no necesita un modelo para empezar y los backends de ML se configuran por separado

## Qué puedes hacer con él

Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video.

## Por qué destaca

Usos propuestos: Preparar un dataset de imágenes; Revisar etiquetas de texto o audio.

## Cómo funciona

La función básica es anotación humana; no necesita un modelo para empezar y los backends de ML se configuran por separado

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o Python compatible
- datos de muestra
- almacenamiento persistente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker pull heartexlabs/label-studio:latest
docker run -it -p 8080:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/HumanSignal/label-studio/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Label Studio para mi objetivo y necesito pasos guiados. Lee https://github.com/HumanSignal/label-studio/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un proyecto con cinco imágenes y etiqueta una clase antes de añadir preanotación AI.

**Qué comprobar:** Puedes exportar anotaciones y comprobar el formato.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un dataset de imágenes
- Revisar etiquetas de texto o audio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un dataset de imágenes; Revisar etiquetas de texto o audio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La función básica es anotación humana; no necesita un modelo para empezar y los backends de ML se configuran por separado

## Stack y modelos

- **Stack:** Docker o Python compatible; datos de muestra; almacenamiento persistente
- **Etiquetas:** `data` `vision` `training` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ultralytics YOLO](ultralytics.md) | 63.4k | Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar. |
| [SAM 3](sam3.md) | 12.3k | Tercera versión de Segment Anything de Meta: detecta, segmenta y sigue en imágenes y video todos los objetos que describas con una frase corta. |

## Enlaces

- 🐙 GitHub: [HumanSignal/label-studio](https://github.com/HumanSignal/label-studio)
- 🌐 Web: <https://labelstud.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/HumanSignal/label-studio/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
