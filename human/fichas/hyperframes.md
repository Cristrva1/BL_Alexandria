[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Video programático y con agentes

# 🎞️ HyperFrames

> Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 84.4k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

HyperFrames define cada video como un archivo HTML con atributos de tiempo y pistas, animado con GSAP, CSS, Lottie, Three.js u otras librerías, y lo renderiza a MP4. Incluye CLI para crear, previsualizar y renderizar, un catálogo de unos 450 bloques (transiciones, subtítulos, gráficos, mapas) y skills para que Claude Code, Codex o Cursor produzcan videos a partir de una petición.

## Por qué destaca

Usa HTML plano en vez de React y licencia Apache 2.0 sin cuotas por render, a diferencia de Remotion. El render es determinista (misma entrada, mismos fotogramas), lo que encaja en CI y pipelines automáticos.

## Cómo funciona

El motor abre la composición en Chrome headless con Puppeteer, avanza fotograma a fotograma mediante adaptadores de animación con búsqueda temporal y codifica con FFmpeg mezclando el audio. Renderiza en local, en Docker o distribuido en AWS Lambda.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
npx hyperframes init my-video
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/heygen-com/hyperframes/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar HyperFrames para mi objetivo y necesito pasos guiados. Lee https://github.com/heygen-com/hyperframes/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Videos de lanzamiento de producto generados por un agente
- Explicar un PR con diffs animados, narración y subtítulos
- Animaciones de datos y mapas para redes sociales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres que un agente de código genere videos con motion graphics a partir de HTML, con licencia permisiva | tu equipo ya trabaja con componentes React y el ecosistema de `remotion`, o prefieres editar en una línea de tiempo visual |

**Limitaciones:** Necesita Node.js 22+ y FFmpeg, el Studio todavía está evolucionando y los modelos generativos de HeyGen del plan Pro son de pago.

## Stack y modelos

- **Stack:** TypeScript, Node.js, Puppeteer, FFmpeg, GSAP
- **Etiquetas:** `video` `agents` `skills` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [GSAP](gsap.md) | 30.6k | Librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincronizados sobre cualquier propiedad del DOM. |
| [Kokoro](kokoro.md) | 10.1k | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |
| [whisperX](whisperx.md) | 25.3k | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [remotion](remotion.md) | 73.2k | Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. |
| [MoviePy](moviepy.md) | 15.2k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Enlaces

- 🐙 GitHub: [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)
- 🌐 Web: <https://hyperframes.heygen.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/heygen-com/hyperframes/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
