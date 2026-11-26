[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🎞️ OpenCut

> Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 98.4k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; app o instalador listo para usar

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

OpenCut, editor de vídeo libre para web, escritorio y móvil. Licencia MIT. Es muy popular (~99k estrellas, v0.3.0) y se está reescribiendo desde cero.

## ¿Qué hace?

La nueva versión promete una API del editor, plugins de terceros, una base Rust común para escritorio, móvil y navegador, servidor MCP para agentes, modo headless y scripting. Mientras tanto, la versión utilizable es opencut-classic, que también se prueba en opencut.app.

## ¿Cómo lo hace?

El desarrollo usa proto (moonrepo) para fijar herramientas. Para editar hoy conviene usar opencut-classic o la versión web.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [LosslessCut](lossless-cut.md) | Recortes sin recodificar antes de editar. (combinación por arquitectura) | Corta el material bruto con LosslessCut y edita en OpenCut. |
| [OBS Studio](obs-studio.md) | Grabar el material que luego se edita. (combinación por arquitectura) | Graba con OBS e importa en OpenCut. |
| [whisperX](whisperx.md) | Generar subtítulos con marcas de tiempo. (combinación por arquitectura) | Transcribe con WhisperX e importa los subtítulos. |

**Notas:** Sin alternativas declaradas. En reescritura: el código del repo principal aún no es un editor utilizable.

Estado en GitHub: activo · último push 2026-09-24 · última versión publicada v0.3.0 (2026-04-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OpenCut-app/OpenCut/blob/main/README.md) · [2](https://opencut.app)</sub>

## Ver similares

Grupo **Editores de video**: OpenCut ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **OpenCut** (esta ficha) ⭐ recomendado | 63 | Si buscas esto: editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. |
| 2 | [Shotcut](shotcut.md) | 60 | Si buscas esto: editor de vídeo libre y multiplataforma basado en Qt y MLT, con línea de tiempo, filtros, amplio soporte de formatos y subtítulos por voz. |
| 3 | [Kdenlive](kdenlive.md) | 59 | Si buscas esto: editor de vídeo no lineal libre de KDE basado en MLT: multipista, efectos, titulación, proxys y subtítulos por reconocimiento de voz. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La edición básica no exige IA; hosting y recursos propios son independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El proyecto se reescribe; la versión clásica web y la rama principal no tienen necesariamente las mismas funciones ni instalación |
| Coste | Sin pago a un modelo en la ruta básica. La edición básica no exige IA; hosting y recursos propios son independientes |
| Equipo | Preparación según la ruta elegida. Navegador para versión clásica o herramientas de la nueva rama; clip de prueba |

El proyecto se reescribe; la versión clásica web y la rama principal no tienen necesariamente las mismas funciones ni instalación

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador para versión clásica o herramientas de la nueva rama
- clip de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/OpenCut-app/OpenCut/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenCut para mi objetivo y necesito pasos guiados. Lee https://github.com/OpenCut-app/OpenCut/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prueba un corte corto en la versión disponible y revisa qué funciones pertenecen a la reescritura.

**Qué comprobar:** Puedes exportar o identificar con claridad qué parte aún no está disponible.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Evaluar una alternativa de edición abierta
- Estudiar la arquitectura de un editor con plugins

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Evaluar una alternativa de edición abierta; Estudiar la arquitectura de un editor con plugins | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El proyecto se reescribe; la versión clásica web y la rama principal no tienen necesariamente las mismas funciones ni instalación

## Stack y modelos

- **Stack:** Navegador para versión clásica o herramientas de la nueva rama; clip de prueba
- **Etiquetas:** `video` `ui` `typescript` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Shotcut](shotcut.md) | 15.7k | Editor de vídeo libre y multiplataforma basado en Qt y MLT, con línea de tiempo, filtros, amplio soporte de formatos y subtítulos por voz. |
| [Kdenlive](kdenlive.md) | 6.1k | Editor de vídeo no lineal libre de KDE basado en MLT: multipista, efectos, titulación, proxys y subtítulos por reconocimiento de voz. |

## Enlaces

- 🐙 GitHub: [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)
- 🌐 Web: <https://opencut.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OpenCut-app/OpenCut/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
