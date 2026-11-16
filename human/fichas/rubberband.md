[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Procesamiento y limpieza de audio

# 📚 rubberband

> Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramientas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 813 | GPL-2.0 | C++ | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Rubber Band Library, biblioteca y utilidad para estirar el tiempo y cambiar el tono de audio, de Chris Cannam (Breakfast Quay). Licencia GPL-2.0+, con licencia comercial disponible. Es madura, de nicho (~800 estrellas) y no cambia desde marzo de 2025.

## ¿Qué hace?

Cambia la duración sin alterar el tono, o el tono sin alterar la duración, con alta calidad, en tiempo real u offline. Se usa en numerosas aplicaciones de audio.

## ¿Cómo lo hace?

Se compila con Meson. La utilidad de línea de comandos requiere libsndfile (LGPL); hay bindings y plugins LADSPA/LV2.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Filtro rubberband en FFmpeg. | Usa un FFmpeg compilado con librubberband. |
| [ACE-Step-1.5](ace-step-1-5.md) | Ajustar tempo de música generada. (combinación por arquitectura) | Procesa la salida. |
| [AudioCraft](audiocraft.md) | Ajustar duración de audio generado. (combinación por arquitectura) | Procesa la salida. |
| [Ultimate Vocal Remover (UVR)](ultimate-vocal-remover.md) | Combinación recíproca: Ultimate Vocal Remover (UVR) lo enlaza como «UVR usa Rubber Band para las funciones de cambio de tiempo y de tono». | Orden indicado desde Ultimate Vocal Remover (UVR): Instala Rubber Band según el README; después usa las herramientas de tempo y tono. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2025-03-03 · licencia declarada GPL-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/breakfastquay/rubberband/blob/default/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. GPL con alternativa comercial para determinados usos; no necesita API de IA y hardware separado |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es procesamiento de señal, no clonación de voz; los parámetros de ejemplo son marcadores y deben sustituirse con valores reales |
| Coste | El coste depende del proveedor o la ruta. GPL con alternativa comercial para determinados usos; no necesita API de IA y hardware separado |
| Equipo | Preparación según la ruta elegida. Biblioteca o utilidad compilada; libsndfile; audio de prueba |

Es procesamiento de señal, no clonación de voz; los parámetros de ejemplo son marcadores y deben sustituirse con valores reales

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Biblioteca o utilidad compilada
- libsndfile
- audio de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/breakfastquay/rubberband/blob/default/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar rubberband para mi objetivo y necesito pasos guiados. Lee https://github.com/breakfastquay/rubberband/blob/default/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Cambia ligeramente el tempo de una copia de audio y compara duración y artefactos.

**Qué comprobar:** Puedes reconocer qué cambió en tiempo y tono.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Ajustar duración de una narración
- Explorar cambio de tono

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Ajustar duración de una narración; Explorar cambio de tono | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es procesamiento de señal, no clonación de voz; los parámetros de ejemplo son marcadores y deben sustituirse con valores reales

## Stack y modelos

- **Stack:** Biblioteca o utilidad compilada; libsndfile; audio de prueba
- **Etiquetas:** `edicion` `library` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [breakfastquay/rubberband](https://github.com/breakfastquay/rubberband)
- 🌐 Web: <http://breakfastquay.com/rubberband/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/breakfastquay/rubberband/blob/default/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
