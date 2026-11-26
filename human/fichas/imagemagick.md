[🏠 Inicio](../README.md) › [🖼️ Generar y editar imágenes con IA](../categorias/11-generaci-n-de-imagen-visi-n.md) › Restauración, upscaling y edición

# 🖥️ ImageMagick

> Convierte, redimensiona y prepara imágenes desde la terminal. Puedes generar miniaturas y variantes web en tu equipo sin un modelo de IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.9k | ImageMagick | C | 2026-11-26 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 55/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de terminal y biblioteca de código abierto para transformar imágenes.

## ¿Qué hace?

Crea miniaturas, convierte formatos y aplica cambios repetibles a colecciones de imágenes.

## ¿Cómo lo hace?

El comando magick abre la entrada, encadena operaciones como redimensionar y genera un archivo de salida.

Estado en GitHub: activo · último push 2026-11-26 · última versión publicada 7.1.2-36 (2026-11-16) · licencia declarada NOASSERTION (consultado el 2026-11-26).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-26); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ImageMagick/ImageMagick/blob/dcec873ede2912a1b045a50fd54cd138ee5f3fa4/README.md) · [2](https://imagemagick.org/download/) · [3](https://imagemagick.org/license/) · [4](https://github.com/ImageMagick/ImageMagick/releases/tag/7.1.2-36) · [5](https://github.com/ImageMagick/ImageMagick/actions/runs/43933165128/job/133530749467) · [6](https://github.com/ImageMagick/ImageMagick/security/advisories) · [7](https://imagemagick.org/security-policy/) · [8](https://imagemagick.org/command-line-options/#resize)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La CLI trabaja sobre archivos del equipo y funciona sin clave de API. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La conversión y el redimensionado son operaciones locales de imagen. |
| Coste | Sin pago a un modelo en la ruta básica. Descarga y uso local sin pago obligatorio bajo la licencia ImageMagick. La práctica no requiere contratar alojamiento. |
| Equipo | Equipo normal; revisar dependencias. Linux, macOS o Windows con un paquete de la arquitectura correspondiente. Para la muestra basta un equipo de uso general. |

Claude Code, Codex y Antigravity pueden ayudarte a preparar el comando. La tarea de imagen se ejecuta con la herramienta local y funciona sin cuenta de IA.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Sistema compatible y terminal
- Paquete oficial para tu arquitectura
- Un PNG propio de 800 × 800 píxeles

1. Prepara una copia de un PNG propio de 800 × 800 píxeles en una carpeta de prueba. Confirma si tu equipo usa x64 o ARM64.
2. Desde las descargas oficiales elige la publicación 7.1.2-36 o una estable posterior con los avisos revisados. En Linux x64 puedes usar el archivo portable tar.xz. Extráelo y abre una terminal en la carpeta de prueba. En Windows, la versión portable oficial se distribuye en 7z.
3. Ejecuta el archivo magick de la carpeta extraída con -version para confirmar la versión. Luego usa la primera prueba de la ficha y abre la miniatura en el visor de tu equipo.

La documentación oficial enlaza los paquetes preparados para cada sistema y muestra cómo verificar una instalación.

[Instrucciones originales de instalación](https://imagemagick.org/download/)

[Abrir la web o descarga indicada por el autor](https://imagemagick.org/download/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ImageMagick para mi objetivo y necesito pasos guiados. Lee https://imagemagick.org/download/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En una carpeta temporal con una imagen cuadrada propia llamada muestra.png, ejecuta magick muestra.png -resize 320x320 miniatura.png. En el paquete portable, usa la ruta del ejecutable en lugar de magick.

**Qué comprobar:** Se crea miniatura.png. Con una entrada cuadrada de 800 × 800 píxeles, la salida mide 320 × 320. El archivo de origen se conserva.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear imágenes PNG de 320 píxeles de ancho para una galería interna.
- Convertir copias de JPG a WebP para reducir el peso antes de subirlas a un sitio.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Quieres convertir o preparar imágenes propias en tu equipo con acciones repetibles. | Prefieres un editor visual o necesitas generar una imagen con IA. |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Usa copias de archivos propios en la primera prueba. Antes de aceptar archivos de terceros en un servicio, aplica una política de formatos y límites de recursos adecuada y aísla el proceso.

## Stack y modelos

- **Stack:** C
- **Etiquetas:** `imágenes` `conversión` `miniaturas` `webp` `terminal`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ImageMagick/ImageMagick](https://github.com/ImageMagick/ImageMagick)
- 🌐 Web: <https://imagemagick.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-26. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ImageMagick/ImageMagick/blob/dcec873ede2912a1b045a50fd54cd138ee5f3fa4/README.md)
- [Fuente 2](https://imagemagick.org/download/)
- [Fuente 3](https://imagemagick.org/license/)
- [Fuente 4](https://github.com/ImageMagick/ImageMagick/releases/tag/7.1.2-36)
- [Fuente 5](https://github.com/ImageMagick/ImageMagick/actions/runs/43933165128/job/133530749467)
- [Fuente 6](https://github.com/ImageMagick/ImageMagick/security/advisories)
- [Fuente 7](https://imagemagick.org/security-policy/)
- [Fuente 8](https://imagemagick.org/command-line-options/#resize)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
