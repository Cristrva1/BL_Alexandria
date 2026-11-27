[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 📚 libass

> Dibuja subtítulos ASS y SSA con estilos, posiciones y tiempos en programas de video, bibliotecas multimedia y reproductores compatibles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.2k | ISC | C | 2026-11-27 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; requiere programar con él

**Puntuación de calidad** 47/100 · métricas del 2026-11-27 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca en C para renderizar subtítulos con formato ASS y SSA.

## ¿Qué hace?

Convierte el contenido de un subtítulo en imagen y conserva estilos, tiempos y posiciones.

## ¿Cómo lo hace?

Lee estilos y eventos, compone glifos con fuentes del sistema y devuelve imagen para el fotograma que pide la aplicación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Procesa video con un filtro de subtítulos cuando la compilación incorpora una versión revisada de libass. | — |
| [pysubs2](pysubs2.md) | Convierte y ajusta el archivo de subtítulos antes de revisar cómo se dibuja. | — |

Estado en GitHub: activo · último push 2026-11-21 · última versión publicada 0.17.5 (2026-06-24) · licencia declarada ISC (consultado el 2026-11-27).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-27); no se instaló ni ejecutó. Fuentes: [1](https://github.com/libass/libass/blob/4a05d8127f525943ebf45fdc6497c9e665947f0d/README.md) · [2](https://github.com/libass/libass/blob/4a05d8127f525943ebf45fdc6497c9e665947f0d/COPYING) · [3](https://github.com/libass/libass/releases/tag/0.17.5) · [4](https://github.com/libass/libass/blob/4a05d8127f525943ebf45fdc6497c9e665947f0d/configure.ac) · [5](https://github.com/libass/libass/blob/4a05d8127f525943ebf45fdc6497c9e665947f0d/test/test.c) · [6](https://github.com/libass/libass/blob/4a05d8127f525943ebf45fdc6497c9e665947f0d/.github/workflows/ghci.yml) · [7](https://github.com/libass/libass/actions/runs/28071659368) · [8](https://github.com/libass/libass/actions/runs/28071659370) · [9](https://github.com/libass/libass/security/advisories)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El programa lee subtítulos locales y escribe un PNG. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Dibuja texto por reglas de tipografía y estilos. Funciona sin un modelo de IA. |
| Coste | Sin pago a un modelo en la ruta básica. Biblioteca ISC, sin pago obligatorio para compilar o ejecutar el ejemplo local. |
| Equipo | Equipo normal; revisar dependencias. Equipo de uso general con Linux y herramientas de compilación. Para generar el PNG necesitas libpng y fuentes disponibles para el texto. |

Los agentes de código pueden ayudarte a preparar la compilación. La biblioteca se ejecuta en tu equipo sin cuenta ni suscripción de IA.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Linux y terminal
- Compilador C, make y pkg-config
- Bibliotecas de desarrollo FreeType, FriBidi, HarfBuzz y libpng
- Un ASS propio con un subtítulo activo durante el segundo 1

1. Prepara un entorno Linux de prueba con compilador C, make, pkg-config y bibliotecas de desarrollo de FreeType, FriBidi, HarfBuzz y libpng. El flujo oficial enumera las dependencias por plataforma.
2. Extrae el archivo fuente de la publicación oficial 0.17.5 y abre una terminal en la carpeta extraída. Ejecuta ./configure --enable-test y luego make. En x86, usa NASM si la configuración lo solicita.
3. Prepara un archivo ASS propio con una línea activa entre 0 y 2 segundos. Sigue la primera prueba para dibujarla en un PNG. Abre el PNG y verifica el estilo y la posición.

El archivo fuente oficial incluye configuración Autotools. Revisa las dependencias en el flujo oficial antes de compilar.

[Instrucciones originales de instalación](https://github.com/libass/libass/releases/tag/0.17.5)

[Abrir la web o descarga indicada por el autor](https://github.com/libass/libass/releases/tag/0.17.5)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar libass para mi objetivo y necesito pasos guiados. Lee https://github.com/libass/libass/releases/tag/0.17.5. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En una compilación Autotools con el programa de prueba habilitado, ejecuta ./test/test subtitulo.png muestra.ass 1.0 con una línea ASS propia activa durante el segundo 1.

**Qué comprobar:** Abre subtitulo.png. La imagen muestra el texto con el estilo del archivo y la línea original se conserva.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comprobar si dos líneas con tamaños y posiciones distintos quedan legibles sobre un fotograma
- Integrar subtítulos con estilos en un editor propio que necesite renderizar ASS

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Necesitas dibujar subtítulos ASS o SSA con estilos y posiciones desde una biblioteca o una integración. | Prefieres editar o sincronizar subtítulos desde una interfaz gráfica. |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Esta compilación de prueba es independiente de la versión que incluya tu reproductor. Empieza con un archivo propio. Comprueba la versión real de la biblioteca antes de procesar archivos ajenos.

## Stack y modelos

- **Stack:** C
- **Etiquetas:** `subtítulos` `ass` `ssa` `renderizado` `c`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [libass/libass](https://github.com/libass/libass)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-27. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/libass/libass/blob/4a05d8127f525943ebf45fdc6497c9e665947f0d/README.md)
- [Fuente 2](https://github.com/libass/libass/blob/4a05d8127f525943ebf45fdc6497c9e665947f0d/COPYING)
- [Fuente 3](https://github.com/libass/libass/releases/tag/0.17.5)
- [Fuente 4](https://github.com/libass/libass/blob/4a05d8127f525943ebf45fdc6497c9e665947f0d/configure.ac)
- [Fuente 5](https://github.com/libass/libass/blob/4a05d8127f525943ebf45fdc6497c9e665947f0d/test/test.c)
- [Fuente 6](https://github.com/libass/libass/blob/4a05d8127f525943ebf45fdc6497c9e665947f0d/.github/workflows/ghci.yml)
- [Fuente 7](https://github.com/libass/libass/actions/runs/28071659368)
- [Fuente 8](https://github.com/libass/libass/actions/runs/28071659370)
- [Fuente 9](https://github.com/libass/libass/security/advisories)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
